"""
ArXiv scraper.

Fetches papers submitted in the last LOOKBACK_DAYS from relevant categories
and filters by topic keywords.  Uses submittedDate range queries for
precise daily targeting, with weekend/holiday fallback logic.

AAAI, CVPR, KDD and other non-OpenReview conferences are covered here because
their accepted papers almost always have an arXiv preprint with the conference
name mentioned in the abstract or comments.

API endpoint: http://export.arxiv.org/api/query  (Atom/XML)
"""
from __future__ import annotations

import logging
import time
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta, timezone
from typing import Dict, List, Optional, Tuple

import requests

from ..config import CONFERENCES, LOOKBACK_DAYS, TOPICS
from ..models import Paper

logger = logging.getLogger(__name__)

ARXIV_API = "http://export.arxiv.org/api/query"
NS = {
    "atom":  "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}

ARXIV_DELAY           = 3.0   # arXiv API recommends 3-second delay
MAX_RESULTS_PER_QUERY = 300   # arXiv hard cap is 2000; 300 is safe and fast

# Search terms per topic
TOPIC_SEARCH_TERMS: Dict[str, List[str]] = {
    "Agent": [
        "agent",
        "multi-agent",
        "agentic",
        "tool use",
        "autonomous agent",
    ],
    "Harness": [
        "harness",
        "lm eval",
        "evaluation framework",
        "llm benchmark",
        "evaluation suite",
    ],
    "Finance": [
        "financial",
        "trading",
        "portfolio",
        "stock market",
        "fraud detection",
        "cryptocurrency",
        "fintech",
    ],
}

# ArXiv categories grouped by topic
TOPIC_CATEGORIES: Dict[str, List[str]] = {
    "Agent":   ["cs.AI", "cs.LG", "cs.CL", "cs.MA"],
    "Harness": ["cs.AI", "cs.LG", "cs.CL"],
    "Finance": ["cs.AI", "cs.LG", "q-fin.TR", "q-fin.PM", "q-fin.RM", "q-fin.ST", "q-fin.CP"],
}

# Extra conference-specific queries to catch AAAI, CVPR, KDD papers
# that mention the venue in title/abstract/comments but may not be in
# standard venue fields.
CONFERENCE_EXTRA_QUERIES: Dict[str, Tuple[str, List[str]]] = {
    # (keyword, [categories])
    "aaai":  ("AAAI",  ["cs.AI", "cs.LG", "cs.CL"]),
    "cvpr":  ("CVPR",  ["cs.CV", "cs.LG", "cs.AI"]),
    "kdd":   ("KDD",   ["cs.LG", "cs.AI", "cs.SI"]),
    "iclr":  ("ICLR",  ["cs.LG", "cs.AI", "cs.CL"]),
    "icml":  ("ICML",  ["cs.LG", "cs.AI", "cs.CL"]),
    "neurips": ("NeurIPS", ["cs.LG", "cs.AI", "cs.CL", "cs.CV"]),
}


def _arxiv_date_range(target_date: date) -> Tuple[date, date]:
    weekday = target_date.weekday()  # 0=Mon … 6=Sun
    if weekday == 6:    # Sunday → Friday
        start = target_date - timedelta(days=2)
    elif weekday == 5:  # Saturday → Friday
        start = target_date - timedelta(days=1)
    elif weekday == 0:  # Monday → include Fri/Sat/Sun
        start = target_date - timedelta(days=3)
    else:
        start = target_date - timedelta(days=LOOKBACK_DAYS)
    return start, target_date


class ArxivScraper:
    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": "paper-find-bot/1.0"})

    def fetch(self, target_date: date) -> List[Paper]:
        start_date, end_date = _arxiv_date_range(target_date)
        logger.info("ArXiv: querying submissions from %s to %s", start_date, end_date)

        seen: Dict[str, Paper] = {}

        # --- Topic + category queries ---
        for topic, terms in TOPIC_SEARCH_TERMS.items():
            categories = TOPIC_CATEGORIES[topic]
            for term in terms:
                for cat in categories:
                    try:
                        results = self._search(term, cat, start_date, end_date)
                        for p in results:
                            pid = p.get_id()
                            if pid not in seen:
                                seen[pid] = p
                        logger.debug("ArXiv [%s/%s/%s]: %d", topic, term, cat, len(results))
                    except Exception as exc:
                        logger.error("ArXiv error [%s/%s/%s]: %s", topic, term, cat, exc)
                    time.sleep(ARXIV_DELAY)

        # --- Conference-specific queries to find AAAI/CVPR/KDD/etc. papers ---
        for keyword, (conf_name, cats) in CONFERENCE_EXTRA_QUERIES.items():
            for cat in cats:
                try:
                    results = self._search(keyword, cat, start_date, end_date)
                    for p in results:
                        pid = p.get_id()
                        if pid not in seen:
                            # Force-set conference for these targeted queries
                            if not p.conference:
                                p.conference = conf_name
                            seen[pid] = p
                        elif not seen[pid].conference:
                            seen[pid].conference = conf_name
                    logger.debug("ArXiv [conf:%s/%s]: %d", keyword, cat, len(results))
                except Exception as exc:
                    logger.error("ArXiv conf-query error [%s/%s]: %s", keyword, cat, exc)
                time.sleep(ARXIV_DELAY)

        logger.info("ArXiv: %d unique papers collected", len(seen))
        return list(seen.values())

    # ------------------------------------------------------------------

    def _search(
        self,
        keyword: str,
        category: str,
        start_date: date,
        end_date: date,
        max_results: int = MAX_RESULTS_PER_QUERY,
    ) -> List[Paper]:
        date_from = start_date.strftime("%Y%m%d") + "000000"
        date_to   = end_date.strftime("%Y%m%d") + "235959"

        query = (
            f'cat:{category} AND '
            f'submittedDate:[{date_from} TO {date_to}] AND '
            f'(ti:"{keyword}" OR abs:"{keyword}")'
        )
        params = {
            "search_query": query,
            "start": 0,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        resp = self.session.get(ARXIV_API, params=params, timeout=60)
        resp.raise_for_status()
        return _parse_arxiv_xml(resp.text)


# ---------------------------------------------------------------------------
# XML parsing helpers
# ---------------------------------------------------------------------------

def _parse_arxiv_xml(xml_text: str) -> List[Paper]:
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as exc:
        logger.error("ArXiv XML parse error: %s", exc)
        return []

    papers: List[Paper] = []
    for entry in root.findall("atom:entry", NS):
        p = _parse_entry(entry)
        if p:
            papers.append(p)
    return papers


def _parse_entry(entry: ET.Element) -> Optional[Paper]:
    title = (entry.findtext("atom:title", "", NS) or "").strip().replace("\n", " ")
    if not title:
        return None

    abstract = (entry.findtext("atom:summary", "", NS) or "").strip().replace("\n", " ")

    id_url = entry.findtext("atom:id", "", NS) or ""
    arxiv_id: Optional[str] = None
    if id_url:
        arxiv_id = id_url.rstrip("/").split("/")[-1]

    authors = [
        (a.findtext("atom:name", "", NS) or "").strip()
        for a in entry.findall("atom:author", NS)
    ]
    authors = [a for a in authors if a]

    published_str = entry.findtext("atom:published", "", NS) or ""
    pub_date: Optional[date] = None
    if published_str:
        try:
            pub_date = datetime.fromisoformat(published_str.replace("Z", "+00:00")).date()
        except ValueError:
            pass

    # ArXiv journal_ref or comment may mention the accepted venue
    comment   = (entry.findtext("arxiv:comment", "", NS) or "").strip()
    jref      = (entry.findtext("arxiv:journal_ref", "", NS) or "").strip()
    combined  = f"{title} {abstract} {comment} {jref}".lower()
    conference = _match_conference(combined)

    url = f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else id_url

    return Paper(
        title=title,
        abstract=abstract,
        authors=authors,
        url=url,
        arxiv_id=arxiv_id,
        conference=conference,
        source="arxiv",
        published_date=pub_date,
    )


def _match_conference(text: str) -> Optional[str]:
    for conf_name, aliases in CONFERENCES.items():
        if any(alias.lower() in text for alias in aliases):
            return conf_name
    return None
