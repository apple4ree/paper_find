"""
OpenReview scraper for AAAI, ICLR, NeurIPS, and ICML conference papers.

Strategy:
  - Search OpenReview /notes/search by topic keyword (no venue filter in the API
    call, since the `content.venueid` query parameter is unreliable and causes
    inconsistent results across runs).
  - Filter results in Python by checking each note's `content.venueid` field
    against known venue-ID prefixes per conference.
  - This covers AAAI 2024/2025 (which moved to OpenReview), ICLR, NeurIPS, ICML.

API base: https://api2.openreview.net
"""
from __future__ import annotations

import logging
import re
import time
from datetime import date, datetime
from typing import Dict, List, Optional

import requests

from ..models import Paper

logger = logging.getLogger(__name__)

_API = "https://api2.openreview.net"
_DELAY = 1.5     # seconds between requests (be polite)
_LIMIT = 50      # results per search call

_CUR_YEAR = date.today().year

# Venue-ID prefixes per canonical conference name.
# Accepted papers at each conference have a content.venueid that *starts with*
# one of these prefixes.  We check both current and previous year.
_VENUE_PREFIXES: Dict[str, List[str]] = {
    "AAAI": [
        f"AAAI.org/{_CUR_YEAR}/",
        f"AAAI.org/{_CUR_YEAR - 1}/",
    ],
    "ICLR": [
        f"ICLR.cc/{_CUR_YEAR}/",
        f"ICLR.cc/{_CUR_YEAR - 1}/",
    ],
    "NeurIPS": [
        f"NeurIPS.cc/{_CUR_YEAR}/",
        f"NeurIPS.cc/{_CUR_YEAR - 1}/",
    ],
    "ICML": [
        f"ICML.cc/{_CUR_YEAR}/",
        f"ICML.cc/{_CUR_YEAR - 1}/",
    ],
}

# Human-readable venue substrings used as fallback when venueid is absent
_VENUE_TEXT: Dict[str, List[str]] = {
    "AAAI":    ["aaai"],
    "ICLR":    ["iclr"],
    "NeurIPS": ["neurips", "nips"],
    "ICML":    ["icml"],
}

# Topic search terms sent to the OpenReview full-text search endpoint
TOPIC_QUERIES: Dict[str, List[str]] = {
    "Agent": [
        "llm agent",
        "autonomous agent",
        "multi-agent",
        "agentic",
        "tool use",
        "language agent",
        "gui agent",
        "web agent",
    ],
    "Harness": [
        "evaluation harness",
        "lm eval",
        "llm evaluation",
        "llm benchmark",
        "evaluation framework",
        "benchmark suite",
    ],
    "Finance": [
        "financial language model",
        "stock market",
        "portfolio optimization",
        "algorithmic trading",
        "fraud detection",
        "cryptocurrency",
        "financial forecasting",
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
        """Return AAAI/ICLR/NeurIPS/ICML papers matching Agent/Harness/Finance."""
        seen: Dict[str, Paper] = {}

        for topic, queries in TOPIC_QUERIES.items():
            for query in queries:
                try:
                    batch = self._search_keyword(query)
                    before = len(seen)
                    for p in batch:
                        pid = p.get_id()
                        if pid not in seen:
                            seen[pid] = p
                    gained = len(seen) - before
                    if gained:
                        logger.debug(
                            "OpenReview ['%s']: %d results, +%d new (total %d)",
                            query, len(batch), gained, len(seen),
                        )
                except Exception as exc:
                    logger.warning(
                        "OpenReview [%s / '%s']: %s", topic, query, exc
                    )
                time.sleep(_DELAY)

        logger.info("OpenReview: %d unique papers collected", len(seen))
        return list(seen.values())

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _search_keyword(self, query: str) -> List[Paper]:
        """Full-text search; filter results by target-conference venue IDs."""
        resp = self.session.get(
            f"{_API}/notes/search",
            params={"term": query, "limit": _LIMIT, "offset": 0},
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()

        papers: List[Paper] = []
        for item in data.get("notes") or []:
            content = item.get("content") or {}
            venueid = _field(content, "venueid")
            conf = _match_by_venueid(venueid)
            if not conf:
                # Fallback: check the human-readable venue string
                conf = _match_by_venue_text(_field(content, "venue"))
            if not conf:
                continue

            year_m = _YEAR_RE.search(venueid or _field(content, "venue"))
            year = int(year_m.group(1)) if year_m else None
            p = _parse_note(item, conf, year)
            if p:
                papers.append(p)

        return papers


# ---------------------------------------------------------------------------
# Venue matching helpers
# ---------------------------------------------------------------------------

def _match_by_venueid(venueid: str) -> Optional[str]:
    """Return canonical conference name if venueid starts with a known prefix."""
    if not venueid:
        return None
    for conf, prefixes in _VENUE_PREFIXES.items():
        if any(venueid.startswith(p) for p in prefixes):
            return conf
    return None


def _match_by_venue_text(venue: str) -> Optional[str]:
    """Fallback: match human-readable venue field by substring."""
    if not venue:
        return None
    v = venue.lower()
    for conf, substrings in _VENUE_TEXT.items():
        if any(s in v for s in substrings):
            return conf
    return None


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def _field(content: dict, key: str) -> str:
    """Extract string value from an OpenReview v2 content dict.

    Field values may be plain strings or wrapped as {"value": "..."}.
    """
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
