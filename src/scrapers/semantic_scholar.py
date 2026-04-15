"""
Semantic Scholar scraper.

Searches the S2 Paper Search API for each topic keyword, then filters
results whose `venue` field matches one of our target conferences.

API endpoint: https://api.semanticscholar.org/graph/v1/paper/search
Rate limits (without key):  ~100 requests / 5 min
Rate limits (with key):     ~1 000 requests / 5 min
"""
from __future__ import annotations

import logging
import time
from datetime import date
from typing import Dict, List, Optional

import requests

from ..config import CONFERENCES, LOOKBACK_DAYS, SS_FIELDS, TOPICS
from ..models import Paper

logger = logging.getLogger(__name__)

SS_SEARCH_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

# Representative search terms per topic (avoid exhaustive queries to save quota)
TOPIC_SEARCH_TERMS: Dict[str, List[str]] = {
    "Agent": ["llm agent", "autonomous agent", "multi-agent", "agentic workflow"],
    "Harness": ["evaluation harness", "lm eval", "benchmarking framework", "eval suite"],
    "Finance": ["financial llm", "stock market prediction", "portfolio optimization",
                "algorithmic trading", "credit risk", "fraud detection"],
}


class SemanticScholarScraper:
    def __init__(
        self,
        api_key: Optional[str] = None,
        session: Optional[requests.Session] = None,
    ):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": "paper-find-bot/1.0"})
        if api_key:
            self.session.headers["x-api-key"] = api_key

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def fetch(self) -> List[Paper]:
        """Return recent conference papers matching our topic keywords."""
        seen: Dict[str, Paper] = {}
        current_year = date.today().year
        year_range = f"{current_year - 1}-{current_year}"

        for topic, terms in TOPIC_SEARCH_TERMS.items():
            for term in terms:
                try:
                    results = self._search(term, year_range)
                    for p in results:
                        pid = p.get_id()
                        if pid not in seen:
                            seen[pid] = p
                except Exception as exc:
                    logger.error("S2 error [%s / %s]: %s", topic, term, exc)
                # Polite delay to stay within rate limits
                time.sleep(1.5)

        return list(seen.values())

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _search(self, query: str, year_range: str, limit: int = 100) -> List[Paper]:
        params = {
            "query": query,
            "fields": SS_FIELDS,
            "limit": limit,
            "year": year_range,
        }
        resp = self.session.get(SS_SEARCH_URL, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()

        papers: List[Paper] = []
        for item in data.get("data") or []:
            p = self._parse_item(item)
            if p:
                papers.append(p)
        return papers

    def _parse_item(self, item: dict) -> Optional[Paper]:
        title = (item.get("title") or "").strip()
        if not title:
            return None

        # Conference matching: check venue field against known aliases
        venue = (item.get("venue") or "").strip()
        matched_conf = _match_conference(venue)
        if not matched_conf:
            return None  # Skip papers not from our target conferences

        ext_ids = item.get("externalIds") or {}
        arxiv_id = ext_ids.get("ArXiv") or None

        # Prefer ArXiv URL, then openAccessPdf, then S2 page
        url = ""
        if arxiv_id:
            url = f"https://arxiv.org/abs/{arxiv_id}"
        else:
            pdf_info = item.get("openAccessPdf") or {}
            url = pdf_info.get("url") or ""
        if not url:
            paper_id = item.get("paperId") or ""
            url = f"https://www.semanticscholar.org/paper/{paper_id}"

        authors = [
            a.get("name", "") for a in (item.get("authors") or []) if a.get("name")
        ]

        pub_date: Optional[date] = None
        raw_date = item.get("publicationDate") or ""
        if raw_date:
            try:
                pub_date = date.fromisoformat(str(raw_date)[:10])
            except ValueError:
                pass

        return Paper(
            title=title,
            abstract=(item.get("abstract") or "").strip(),
            authors=authors,
            url=url,
            arxiv_id=arxiv_id,
            conference=matched_conf,
            year=item.get("year"),
            source="semantic_scholar",
            published_date=pub_date,
        )


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _match_conference(venue: str) -> Optional[str]:
    """Return canonical conference name if *venue* matches any alias."""
    venue_lower = venue.lower()
    for conf_name, aliases in CONFERENCES.items():
        if any(alias.lower() in venue_lower for alias in aliases):
            return conf_name
    return None
