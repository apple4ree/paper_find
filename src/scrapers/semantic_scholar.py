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

# Delay between S2 requests (seconds): 1.5s without key, 0.5s with key
_DELAY_NO_KEY = 1.5
_DELAY_WITH_KEY = 0.5

# Representative search terms per topic — broad enough to catch most papers
TOPIC_SEARCH_TERMS: Dict[str, List[str]] = {
    "Agent": [
        "llm agent",
        "language model agent",
        "autonomous agent",
        "multi-agent system",
        "agentic workflow",
        "tool-augmented language model",
        "function calling",
        "gui agent",
        "web agent",
        "code agent",
    ],
    "Harness": [
        "evaluation harness",
        "lm eval",
        "benchmarking framework",
        "evaluation suite",
        "language model benchmark",
        "llm evaluation",
        "capability evaluation",
    ],
    "Finance": [
        "financial large language model",
        "stock market prediction",
        "portfolio optimization",
        "algorithmic trading",
        "credit risk prediction",
        "fraud detection deep learning",
        "cryptocurrency prediction",
        "financial sentiment analysis",
        "market microstructure",
        "fintech deep learning",
    ],
}

# Venue-scoped searches: for conferences NOT on OpenReview (AAAI, CVPR, KDD)
# we explicitly inject venue aliases to raise recall.
# Each entry: (topic, search_term, venue_hint)
VENUE_SCOPED_TERMS: List[tuple[str, str, str]] = [
    # CVPR — visual agents, video understanding, embodied AI
    ("Agent",   "visual agent",             "CVPR"),
    ("Agent",   "embodied agent",           "CVPR"),
    ("Agent",   "robot agent vision",       "CVPR"),
    ("Harness", "vision benchmark",         "CVPR"),
    ("Harness", "visual evaluation",        "CVPR"),
    ("Finance", "financial image",          "CVPR"),
    # KDD — data-mining angle on finance + agents
    ("Agent",   "agent data mining",        "KDD"),
    ("Agent",   "recommendation agent",     "KDD"),
    ("Finance", "financial data mining",    "KDD"),
    ("Finance", "stock prediction graph",   "KDD"),
    ("Finance", "fraud detection graph",    "KDD"),
    ("Harness", "evaluation data mining",   "KDD"),
    # AAAI — broad AI; supplement Semantic Scholar keyword search
    ("Agent",   "planning agent aaai",      "AAAI"),
    ("Finance", "financial forecasting",    "AAAI"),
]


class SemanticScholarScraper:
    def __init__(
        self,
        api_key: Optional[str] = None,
        session: Optional[requests.Session] = None,
    ):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": "paper-find-bot/1.0"})
        self._has_key = bool(api_key)
        if api_key:
            self.session.headers["x-api-key"] = api_key
        self._delay = _DELAY_WITH_KEY if self._has_key else _DELAY_NO_KEY

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def fetch(self) -> List[Paper]:
        """Return recent conference papers matching our topic keywords."""
        seen: Dict[str, Paper] = {}
        current_year = date.today().year
        year_range = f"{current_year - 1}-{current_year}"

        # --- General topic keyword search ---
        for topic, terms in TOPIC_SEARCH_TERMS.items():
            for term in terms:
                self._run_search(term, year_range, seen, label=f"{topic}/{term}")

        # --- Venue-scoped searches for AAAI / CVPR / KDD ---
        for topic, term, venue_hint in VENUE_SCOPED_TERMS:
            scoped_query = f"{term} {venue_hint}"
            self._run_search(scoped_query, year_range, seen, label=f"{topic}/{venue_hint}/{term}")

        logger.info("Semantic Scholar: %d unique papers collected", len(seen))
        return list(seen.values())

    def _run_search(
        self,
        query: str,
        year_range: str,
        seen: Dict[str, Paper],
        label: str = "",
    ) -> None:
        """Execute one search query, merge results into *seen*, handle rate limits."""
        try:
            results = self._search(query, year_range)
            for p in results:
                pid = p.get_id()
                if pid not in seen:
                    seen[pid] = p
            logger.debug("S2 [%s]: %d results", label, len(results))
        except requests.exceptions.HTTPError as exc:
            if exc.response is not None and exc.response.status_code == 429:
                logger.warning("S2 rate limited; sleeping 30s then retrying [%s]", label)
                time.sleep(30)
                try:
                    for p in self._search(query, year_range):
                        pid = p.get_id()
                        if pid not in seen:
                            seen[pid] = p
                except Exception as retry_exc:
                    logger.error("S2 retry failed [%s]: %s", label, retry_exc)
            else:
                logger.error("S2 HTTP error [%s]: %s", label, exc)
        except Exception as exc:
            logger.error("S2 error [%s]: %s", label, exc)
        time.sleep(self._delay)

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
