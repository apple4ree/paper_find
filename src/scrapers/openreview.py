"""
OpenReview scraper for ICLR, NeurIPS, and ICML conference papers.

Primary:  /notes/search  — fast keyword search per venue
Fallback: /notes         — bulk fetch with local keyword filtering
          (used when /notes/search returns 403 or 5xx)

API base: https://api2.openreview.net
"""
from __future__ import annotations

import logging
import re
import time
from datetime import date, datetime
from typing import Dict, List, Optional, Tuple

import requests

from ..models import Paper

logger = logging.getLogger(__name__)

_API = "https://api2.openreview.net"
_DELAY = 1.5        # seconds between requests
_SEARCH_LIMIT = 50  # results per /notes/search call
_BULK_LIMIT = 100   # results per /notes page
_BULK_MAX_PAGES = 20  # cap at 2 000 papers per venue

_CUR_YEAR = date.today().year

VENUE_CONF: Dict[str, List[str]] = {
    "ICLR": [
        f"ICLR.cc/{_CUR_YEAR}/Conference",
        f"ICLR.cc/{_CUR_YEAR - 1}/Conference",
    ],
    "NeurIPS": [
        f"NeurIPS.cc/{_CUR_YEAR}/Conference",
        f"NeurIPS.cc/{_CUR_YEAR - 1}/Conference",
    ],
    "ICML": [
        f"ICML.cc/{_CUR_YEAR}/Conference",
        f"ICML.cc/{_CUR_YEAR - 1}/Conference",
    ],
}

TOPIC_QUERIES: Dict[str, List[str]] = {
    "Agent": [
        "llm agent",
        "autonomous agent",
        "multi-agent",
        "agentic",
        "tool use",
        "tool-use",
        "gui agent",
        "web agent",
        "code agent",
    ],
    "Harness": [
        "evaluation harness",
        "lm eval",
        "llm evaluation",
        "benchmark",
        "evaluation framework",
        "evaluation suite",
    ],
    "Finance": [
        "financial",
        "trading",
        "portfolio",
        "fraud detection",
        "cryptocurrency",
        "stock",
        "fintech",
    ],
}

# All topic keywords merged for bulk-fetch local filtering
_ALL_KEYWORDS: List[str] = sorted(
    {kw.lower() for kws in TOPIC_QUERIES.values() for kw in kws}
)

_ARXIV_ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})")
_YEAR_RE = re.compile(r"/(\d{4})/")

_BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, */*;q=0.9",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://openreview.net/",
}


class OpenReviewScraper:
    """Search OpenReview-hosted conference papers by topic keyword."""

    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self.session.headers.update(_BROWSER_HEADERS)
        # Track whether /notes/search is usable (set to False on first 403)
        self._search_blocked: bool = False

    def fetch(self) -> List[Paper]:
        """Return ICLR/NeurIPS/ICML papers matching Agent/Harness/Finance keywords."""
        seen: Dict[str, Paper] = {}

        for conf_name, venue_ids in VENUE_CONF.items():
            for venue_id in venue_ids:
                year_m = _YEAR_RE.search(venue_id)
                year = int(year_m.group(1)) if year_m else None

                papers = self._fetch_venue(venue_id, conf_name, year)
                for p in papers:
                    pid = p.get_id()
                    if pid not in seen:
                        seen[pid] = p

                time.sleep(_DELAY)

        logger.info("OpenReview: %d unique papers collected", len(seen))
        return list(seen.values())

    # ------------------------------------------------------------------
    # Per-venue entry point
    # ------------------------------------------------------------------

    def _fetch_venue(
        self, venue_id: str, conf_name: str, year: Optional[int]
    ) -> List[Paper]:
        if not self._search_blocked:
            papers = self._search_venue(venue_id, conf_name, year)
            if papers is not None:  # None means search is blocked
                return papers

        # Fallback: bulk fetch + local filter
        return self._bulk_venue(venue_id, conf_name, year)

    # ------------------------------------------------------------------
    # Primary: /notes/search  (fast, keyword-aware)
    # ------------------------------------------------------------------

    def _search_venue(
        self, venue_id: str, conf_name: str, year: Optional[int]
    ) -> Optional[List[Paper]]:
        """Return papers or None if the search endpoint is blocked."""
        results: Dict[str, Paper] = {}

        for topic, queries in TOPIC_QUERIES.items():
            for query in queries:
                try:
                    batch = self._search_query(query, venue_id, conf_name, year)
                    for p in batch:
                        pid = p.get_id()
                        if pid not in results:
                            results[pid] = p
                    if batch:
                        logger.debug(
                            "OpenReview search [%s %s / '%s']: %d",
                            conf_name, year or "?", query, len(batch),
                        )
                except _SearchBlocked:
                    logger.warning(
                        "OpenReview /notes/search blocked for %s — switching to bulk fetch",
                        conf_name,
                    )
                    self._search_blocked = True
                    return None
                except Exception as exc:
                    logger.warning(
                        "OpenReview search [%s %s / '%s']: %s",
                        conf_name, year or "?", query, exc,
                    )
                time.sleep(_DELAY)

        return list(results.values())

    def _search_query(
        self, query: str, venue_id: str, conf_name: str, year: Optional[int]
    ) -> List[Paper]:
        resp = self.session.get(
            f"{_API}/notes/search",
            params={
                "term": query,
                "content.venueid": venue_id,
                "offset": 0,
                "limit": _SEARCH_LIMIT,
            },
            timeout=30,
        )
        if resp.status_code in (401, 403):
            raise _SearchBlocked(resp.status_code)
        resp.raise_for_status()
        data = resp.json()

        return [
            p
            for p in (
                _parse_note(item, conf_name, year)
                for item in data.get("notes") or []
            )
            if p
        ]

    # ------------------------------------------------------------------
    # Fallback: /notes  (bulk fetch + local keyword filter)
    # ------------------------------------------------------------------

    def _bulk_venue(
        self, venue_id: str, conf_name: str, year: Optional[int]
    ) -> List[Paper]:
        """Paginate through all notes for a venue and filter locally."""
        papers: List[Paper] = []

        for page in range(_BULK_MAX_PAGES):
            offset = page * _BULK_LIMIT
            try:
                batch, total = self._bulk_page(venue_id, conf_name, year, offset)
            except Exception as exc:
                logger.warning(
                    "OpenReview bulk [%s %s] page %d: %s",
                    conf_name, year or "?", page, exc,
                )
                break

            papers.extend(batch)
            logger.debug(
                "OpenReview bulk [%s %s] page %d: %d/%d",
                conf_name, year or "?", page, len(papers), total,
            )

            if offset + _BULK_LIMIT >= total:
                break

            time.sleep(_DELAY)

        logger.info(
            "OpenReview bulk [%s %s]: %d relevant papers",
            conf_name, year or "?", len(papers),
        )
        return papers

    def _bulk_page(
        self, venue_id: str, conf_name: str, year: Optional[int], offset: int
    ) -> Tuple[List[Paper], int]:
        resp = self.session.get(
            f"{_API}/notes",
            params={
                "content.venueid": venue_id,
                "offset": offset,
                "limit": _BULK_LIMIT,
            },
            timeout=60,
        )
        resp.raise_for_status()
        data = resp.json()
        total = data.get("count") or 0

        papers: List[Paper] = []
        for item in data.get("notes") or []:
            p = _parse_note(item, conf_name, year)
            if p and _is_relevant(p):
                papers.append(p)

        return papers, total


# ---------------------------------------------------------------------------
# Internal exceptions
# ---------------------------------------------------------------------------

class _SearchBlocked(Exception):
    pass


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def _is_relevant(paper: Paper) -> bool:
    combined = f"{paper.title} {paper.abstract}".lower()
    return any(kw in combined for kw in _ALL_KEYWORDS)


def _field(content: dict, key: str) -> str:
    v = content.get(key, "")
    if isinstance(v, dict):
        return str(v.get("value") or "")
    return str(v or "")


def _parse_note(item: dict, conf_name: str, year: Optional[int]) -> Optional[Paper]:
    content = item.get("content") or {}

    title = _field(content, "title").strip()
    if not title:
        return None

    abstract = _field(content, "abstract").strip()

    raw_authors = content.get("authors") or []
    if isinstance(raw_authors, dict):
        raw_authors = raw_authors.get("value") or []
    authors = [str(a) for a in raw_authors if a]

    arxiv_id: Optional[str] = None
    for key in ("ARXIV", "arxiv", "_bibtex", "pdf", "code"):
        m = _ARXIV_ID_RE.search(_field(content, key))
        if m:
            arxiv_id = m.group(1)
            break

    paper_id = item.get("id") or item.get("forum") or ""
    url = f"https://openreview.net/forum?id={paper_id}" if paper_id else ""
    if arxiv_id:
        url = f"https://arxiv.org/abs/{arxiv_id}"

    pub_date: Optional[date] = None
    for ts_key in ("cdate", "odate", "mdate"):
        cdate = item.get(ts_key)
        if cdate:
            try:
                pub_date = datetime.fromtimestamp(int(cdate) / 1000).date()
                break
            except (ValueError, TypeError, OSError):
                pass

    return Paper(
        title=title,
        abstract=abstract,
        authors=authors,
        url=url,
        arxiv_id=arxiv_id,
        conference=conf_name,
        year=year,
        source="openreview",
        published_date=pub_date,
    )
