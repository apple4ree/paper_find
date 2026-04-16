"""
ArXiv scraper.

Fetches papers submitted in the last LOOKBACK_DAYS from relevant categories
and filters by topic keywords.  Uses submittedDate range queries for
precise daily targeting, with weekend/holiday fallback logic.

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
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}

# ArXiv API recommends 3-second delay between requests
ARXIV_DELAY = 3.0

# Max results per query (arXiv API hard cap is 2000; we use 300 for safety)
MAX_RESULTS_PER_QUERY = 300

# Top keywords to search per topic (keep each concise for URL length)
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

# ArXiv categories grouped by topic affinity
TOPIC_CATEGORIES: Dict[str, List[str]] = {
    "Agent": ["cs.AI", "cs.LG", "cs.CL", "cs.MA"],
    "Harness": ["cs.AI", "cs.LG", "cs.CL"],
    "Finance": ["cs.AI", "cs.LG", "q-fin.TR", "q-fin.PM", "q-fin.RM", "q-fin.ST", "q-fin.CP"],
}


def _arxiv_date_range(target_date: date) -> Tuple[date, date]:
    """Return (start, end) dates for arXiv query, accounting for weekends.

    arXiv does not accept new submissions on Saturday/Sunday, so on Mondays
    we look back to include the previous Friday's batch.
    """
    weekday = target_date.weekday()  # 0=Mon … 6=Sun
    if weekday == 6:  # Sunday → look at Friday
        start = target_date - timedelta(days=2)
    elif weekday == 5:  # Saturday → look at Friday
        start = target_date - timedelta(days=1)
    elif weekday == 0:  # Monday → include Fri/Sat/Sun too
        start = target_date - timedelta(days=3)
    else:
        start = target_date - timedelta(days=LOOKBACK_DAYS)
    return start, target_date


class ArxivScraper:
    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": "paper-find-bot/1.0"})

    def fetch(self, target_date: date) -> List[Paper]:
        """Return arXiv papers submitted around *target_date* that match topics."""
        start_date, end_date = _arxiv_date_range(target_date)
        logger.info(
            "ArXiv: querying submissions from %s to %s", start_date, end_date
        )

        seen: Dict[str, Paper] = {}

        for topic, terms in TOPIC_SEARCH_TERMS.items():
            categories = TOPIC_CATEGORIES[topic]
            for term in terms:
                for cat in categories:
                    try:
                        results = self._search(
                            term, cat, start_date, end_date,
                            max_results=MAX_RESULTS_PER_QUERY,
                        )
                        for p in results:
                            pid = p.get_id()
                            if pid not in seen:
                                seen[pid] = p
                        logger.debug(
                            "ArXiv [%s/%s/%s]: %d results", topic, term, cat, len(results)
                        )
                    except Exception as exc:
                        logger.error(
                            "ArXiv error [%s / %s / %s]: %s", topic, term, cat, exc
                        )
                    # Respect arXiv's recommended 3-second delay
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
        # Format: YYYYMMDDHHMMSS
        date_from = start_date.strftime("%Y%m%d") + "000000"
        date_to = end_date.strftime("%Y%m%d") + "235959"

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

    # ArXiv ID
    id_url = entry.findtext("atom:id", "", NS) or ""
    arxiv_id: Optional[str] = None
    if id_url:
        arxiv_id = id_url.rstrip("/").split("/")[-1]  # e.g. "2310.12345v2"

    # Authors
    authors = [
        (a.findtext("atom:name", "", NS) or "").strip()
        for a in entry.findall("atom:author", NS)
    ]
    authors = [a for a in authors if a]

    # Published date
    published_str = entry.findtext("atom:published", "", NS) or ""
    pub_date: Optional[date] = None
    if published_str:
        try:
            pub_date = datetime.fromisoformat(
                published_str.replace("Z", "+00:00")
            ).date()
        except ValueError:
            pass

    # URL: prefer the abs link
    url = f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else id_url

    # Detect conference mention
    combined = f"{title} {abstract}".lower()
    conference = _match_conference(combined)

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
