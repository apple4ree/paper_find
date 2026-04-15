"""
ArXiv scraper.

Fetches papers submitted in the last LOOKBACK_DAYS from relevant categories
and filters by topic keywords.  Also flags papers that mention a target
conference in their title or abstract.

API endpoint: http://export.arxiv.org/api/query  (Atom/XML)
"""
from __future__ import annotations

import logging
import time
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta, timezone
from typing import Dict, List, Optional

import requests

from ..config import ARXIV_CATEGORIES, CONFERENCES, LOOKBACK_DAYS, TOPICS
from ..models import Paper

logger = logging.getLogger(__name__)

ARXIV_API = "http://export.arxiv.org/api/query"
NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}

# Top keywords to search per topic (keep query short for reliability)
TOPIC_SEARCH_TERMS: Dict[str, List[str]] = {
    "Agent": ["agent", "multi-agent", "agentic"],
    "Harness": ["harness", "lm eval", "evaluation framework"],
    "Finance": ["financial", "trading", "portfolio", "stock market", "fraud detection"],
}

# ArXiv categories grouped by topic affinity
TOPIC_CATEGORIES: Dict[str, List[str]] = {
    "Agent": ["cs.AI", "cs.LG", "cs.CL"],
    "Harness": ["cs.AI", "cs.LG", "cs.CL"],
    "Finance": ["cs.AI", "cs.LG", "q-fin.TR", "q-fin.PM", "q-fin.RM", "q-fin.ST"],
}


class ArxivScraper:
    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": "paper-find-bot/1.0"})

    def fetch(self, target_date: date) -> List[Paper]:
        """Return arXiv papers submitted around *target_date* that match topics."""
        cutoff = datetime.combine(
            target_date - timedelta(days=LOOKBACK_DAYS),
            datetime.min.time(),
            tzinfo=timezone.utc,
        )

        seen: Dict[str, Paper] = {}

        for topic, terms in TOPIC_SEARCH_TERMS.items():
            categories = TOPIC_CATEGORIES[topic]
            for term in terms:
                for cat in categories:
                    try:
                        results = self._search(term, cat, max_results=50)
                        for p in results:
                            # Discard papers older than the cutoff
                            if p.published_date:
                                pub_dt = datetime.combine(
                                    p.published_date,
                                    datetime.min.time(),
                                    tzinfo=timezone.utc,
                                )
                                if pub_dt < cutoff:
                                    continue
                            pid = p.get_id()
                            if pid not in seen:
                                seen[pid] = p
                    except Exception as exc:
                        logger.error(
                            "ArXiv error [%s / %s / %s]: %s", topic, term, cat, exc
                        )
                    time.sleep(0.5)  # Be polite to arXiv

        return list(seen.values())

    # ------------------------------------------------------------------

    def _search(self, keyword: str, category: str, max_results: int = 50) -> List[Paper]:
        query = f'cat:{category} AND (ti:"{keyword}" OR abs:"{keyword}")'
        params = {
            "search_query": query,
            "start": 0,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        resp = self.session.get(ARXIV_API, params=params, timeout=30)
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
