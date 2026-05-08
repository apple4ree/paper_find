"""
OpenReview scraper for ICLR, NeurIPS, and ICML conference papers.

Uses the OpenReview API v2 text-search endpoint (/notes/search) WITHOUT a
venue filter at the API level — the venue filter was unreliable and caused
ICLR results to be silently dropped.  Instead we filter results locally by
checking each note's content.venueid field against our target venue IDs.

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
_LIMIT = 50     # results per search call (increased from 25)

_CUR_YEAR = date.today().year

# Map canonical conference name → list of OpenReview venue IDs to check.
# We try current year and previous year to capture freshly-accepted papers.
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

# Flattened lookup: lowercase venue_id prefix → canonical name + year
_VENUE_MAP: Dict[str, Tuple[str, int]] = {
    vid.lower(): (conf, int(re.search(r"/(\d{4})/", vid).group(1)))  # type: ignore[union-attr]
    for conf, vids in VENUE_CONF.items()
    for vid in vids
}

# Representative search terms per topic (broader = more recall)
TOPIC_QUERIES: Dict[str, List[str]] = {
    "Agent": [
        "llm agent",
        "language model agent",
        "autonomous agent",
        "multi-agent",
        "agentic",
        "tool use",
        "function calling",
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
        "model assessment",
    ],
    "Finance": [
        "financial",
        "trading",
        "portfolio",
        "fraud detection",
        "cryptocurrency",
        "stock market",
        "fintech",
        "risk management",
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

        for topic, queries in TOPIC_QUERIES.items():
            for query in queries:
                try:
                    batch = self._search(query)
                    new_count = 0
                    for p in batch:
                        pid = p.get_id()
                        if pid not in seen:
                            seen[pid] = p
                            new_count += 1
                    if batch:
                        logger.debug(
                            "OpenReview ['%s']: %d results (%d new)", query, len(batch), new_count
                        )
                except Exception as exc:
                    logger.warning("OpenReview ['%s']: %s", query, exc)
                time.sleep(_DELAY)

        logger.info("OpenReview: %d unique papers collected", len(seen))
        return list(seen.values())

    # ------------------------------------------------------------------

    def _search(self, query: str) -> List[Paper]:
        """Text-search OpenReview; filter by target venue IDs locally."""
        resp = self.session.get(
            f"{_API}/notes/search",
            params={"term": query, "offset": 0, "limit": _LIMIT},
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()

        papers: List[Paper] = []
        for item in data.get("notes") or []:
            content = item.get("content") or {}
            raw_venue_id = _field(content, "venueid").strip()

            # Match this note's venue ID to one of our target conferences
            result = _match_venue(raw_venue_id)
            if not result:
                continue
            conf_name, year = result

            p = _parse_note(item, conf_name, year)
            if p:
                papers.append(p)

        return papers


# ---------------------------------------------------------------------------
# Venue matching
# ---------------------------------------------------------------------------

def _match_venue(raw_venue_id: str) -> Optional[Tuple[str, int]]:
    """Return (conf_name, year) if *raw_venue_id* matches a target venue."""
    lower = raw_venue_id.lower()
    # Exact match first
    if lower in _VENUE_MAP:
        return _VENUE_MAP[lower]
    # Prefix / substring match (handles track suffixes like /Spotlight)
    for vid_prefix, info in _VENUE_MAP.items():
        if lower.startswith(vid_prefix):
            return info
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


def _parse_note(item: dict, conf_name: str, year: int) -> Optional[Paper]:
    content = item.get("content") or {}

    title = _field(content, "title").strip()
    if not title:
        return None

    abstract = _field(content, "abstract").strip()

    # Authors: plain list or {"value": [...]}
    raw_authors = content.get("authors") or []
    if isinstance(raw_authors, dict):
        raw_authors = raw_authors.get("value") or []
    authors = [str(a) for a in raw_authors if a]

    # arXiv ID: check known fields and any URL-shaped value
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

    # Creation timestamp is in milliseconds
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
