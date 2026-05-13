"""
OpenReview scraper for ICLR, NeurIPS, and ICML conference papers.

Uses the OpenReview API v2 to search for accepted papers by topic keyword.
Only queries venues whose conference dates have already passed.

Approximate conference calendars (used to decide which years to query):
  ICLR   → May of that year
  ICML   → July of that year
  NeurIPS → December of that year

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
_DELAY = 1.5    # seconds between requests
_LIMIT = 25     # results per search call

_TODAY = date.today()
_CUR_YEAR = _TODAY.year
_CUR_MONTH = _TODAY.month


def _past_years_for(conf: str) -> List[int]:
    """Return the list of years whose proceedings are likely already published."""
    # Approximate months when each conference concludes
    conf_month = {"ICLR": 5, "ICML": 7, "NeurIPS": 12}
    month = conf_month.get(conf, 12)

    years = []
    for y in (_CUR_YEAR, _CUR_YEAR - 1):
        if y < _CUR_YEAR:
            years.append(y)
        elif y == _CUR_YEAR and _CUR_MONTH >= month:
            years.append(y)
    return years if years else [_CUR_YEAR - 1]


# Build venue IDs for conferences whose proceedings already exist
VENUE_CONF: Dict[str, List[str]] = {}
for _conf, _tpl in {
    "ICLR": "ICLR.cc/{year}/Conference",
    "NeurIPS": "NeurIPS.cc/{year}/Conference",
    "ICML": "ICML.cc/{year}/Conference",
}.items():
    _venues = [_tpl.format(year=y) for y in _past_years_for(_conf)]
    if _venues:
        VENUE_CONF[_conf] = _venues

logger.debug("OpenReview venues to query: %s", VENUE_CONF)

# Representative search terms per topic
TOPIC_QUERIES: Dict[str, List[str]] = {
    "Agent": [
        "llm agent",
        "autonomous agent",
        "multi-agent",
        "agentic",
        "tool use",
    ],
    "Harness": [
        "evaluation harness",
        "lm eval",
        "llm evaluation",
        "benchmark",
        "evaluation framework",
    ],
    "Finance": [
        "financial",
        "trading",
        "portfolio",
        "fraud detection",
        "cryptocurrency",
    ],
}

_ARXIV_ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})")
_YEAR_RE = re.compile(r"/(\d{4})/")


class OpenReviewScraper:
    """Search OpenReview-hosted conference papers by topic keyword."""

    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": "paper-find-bot/1.0"})

    def fetch(self) -> List[Paper]:
        """Return ICLR/NeurIPS/ICML papers matching Agent/Harness/Finance keywords."""
        seen: Dict[str, Paper] = {}

        for conf_name, venue_ids in VENUE_CONF.items():
            for venue_id in venue_ids:
                year_m = _YEAR_RE.search(venue_id)
                year = int(year_m.group(1)) if year_m else None

                for topic, queries in TOPIC_QUERIES.items():
                    for query in queries:
                        try:
                            batch = self._search(query, venue_id, conf_name, year)
                            for p in batch:
                                pid = p.get_id()
                                if pid not in seen:
                                    seen[pid] = p
                            if batch:
                                logger.debug(
                                    "OpenReview [%s %s / '%s']: %d",
                                    conf_name, year or "?", query, len(batch),
                                )
                        except Exception as exc:
                            logger.warning(
                                "OpenReview [%s %s / '%s']: %s",
                                conf_name, year or "?", query, exc,
                            )
                        time.sleep(_DELAY)

        logger.info("OpenReview: %d unique papers collected", len(seen))
        return list(seen.values())

    # ------------------------------------------------------------------

    def _search(
        self,
        query: str,
        venue_id: str,
        conf_name: str,
        year: Optional[int],
    ) -> List[Paper]:
        resp = self.session.get(
            f"{_API}/notes/search",
            params={
                "term": query,
                "content.venueid": venue_id,
                "offset": 0,
                "limit": _LIMIT,
            },
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()

        papers: List[Paper] = []
        for item in data.get("notes") or []:
            p = _parse_note(item, conf_name, year)
            if p:
                papers.append(p)
        return papers


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def _field(content: dict, key: str) -> str:
    """Extract string value from an OpenReview v2 content dict."""
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
