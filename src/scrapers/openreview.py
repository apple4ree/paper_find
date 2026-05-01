"""
OpenReview scraper for ICLR, NeurIPS, and ICML conference papers.

Uses the OpenReview API v2:
  - /notes           : list accepted papers by venueid (stable, paginated)
  - /notes/search    : keyword search within a venue (falls back to /notes if unavailable)

Covers current and previous year for each hosted venue.

API base: https://api2.openreview.net
"""
from __future__ import annotations

import logging
import os
import re
import time
from datetime import date, datetime
from typing import Dict, List, Optional, Tuple

import requests

from ..config import TOPICS
from ..models import Paper

logger = logging.getLogger(__name__)

_API    = "https://api2.openreview.net"
_DELAY  = 1.5     # seconds between requests
_LIMIT  = 100     # results per page (max 1000 for /notes, 25 for /notes/search)

_CUR_YEAR = date.today().year

# Venue ID formats for OpenReview-hosted conferences
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

# Keyword search terms per topic (used by /notes/search)
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

# Keyword filter for /notes bulk-listing (topic keyword must appear in title/abstract)
_TOPIC_KEYWORDS: List[str] = sorted(
    {kw.lower() for kws in TOPICS.values() for kw in kws},
    key=len,
    reverse=True,
)

_ARXIV_ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})")
_YEAR_RE     = re.compile(r"/(\d{4})/")


class OpenReviewScraper:
    """Fetch ICLR/NeurIPS/ICML papers matching Agent/Harness/Finance keywords."""

    def __init__(
        self,
        session: Optional[requests.Session] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
    ):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": "paper-find-bot/1.0"})

        u = username or os.environ.get("OPENREVIEW_USER", "")
        p = password or os.environ.get("OPENREVIEW_PASS", "")
        if u and p:
            self._login(u, p)

    def _login(self, username: str, password: str) -> None:
        try:
            resp = self.session.post(
                f"{_API}/login",
                json={"id": username, "password": password},
                timeout=15,
            )
            resp.raise_for_status()
            token = resp.json().get("token", "")
            if token:
                self.session.headers["Authorization"] = f"Bearer {token}"
                logger.info("OpenReview: logged in as %s", username)
        except Exception as exc:
            logger.warning("OpenReview login failed: %s", exc)

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def fetch(self) -> List[Paper]:
        seen: Dict[str, Paper] = {}

        for conf_name, venue_ids in VENUE_CONF.items():
            for venue_id in venue_ids:
                year_m = _YEAR_RE.search(venue_id)
                year = int(year_m.group(1)) if year_m else None

                # Strategy 1: keyword search (fast, targeted)
                search_papers = self._fetch_by_search(venue_id, conf_name, year)
                for p in search_papers:
                    pid = p.get_id()
                    if pid not in seen:
                        seen[pid] = p

                # Strategy 2: bulk listing with local keyword filter
                # Only run if search returned nothing (API might block search endpoint)
                if not search_papers:
                    bulk_papers = self._fetch_bulk(venue_id, conf_name, year)
                    for p in bulk_papers:
                        pid = p.get_id()
                        if pid not in seen:
                            seen[pid] = p

        logger.info("OpenReview: %d unique papers collected", len(seen))
        return list(seen.values())

    # ------------------------------------------------------------------
    # Strategy 1: /notes/search  (keyword-aware)
    # ------------------------------------------------------------------

    def _fetch_by_search(
        self, venue_id: str, conf_name: str, year: Optional[int]
    ) -> List[Paper]:
        results: List[Paper] = []
        for topic, queries in TOPIC_QUERIES.items():
            for query in queries:
                try:
                    batch = self._search(query, venue_id, conf_name, year)
                    for p in batch:
                        results.append(p)
                    logger.debug(
                        "OpenReview search [%s %s / '%s']: %d",
                        conf_name, year or "?", query, len(batch),
                    )
                except requests.exceptions.HTTPError as exc:
                    code = exc.response.status_code if exc.response is not None else 0
                    if code in (403, 404):
                        logger.info(
                            "OpenReview /notes/search not available (%d) for %s — will try bulk",
                            code, venue_id,
                        )
                        return results   # abort search strategy for this venue
                    logger.warning("OpenReview search [%s %s / '%s']: %s", conf_name, year, query, exc)
                except Exception as exc:
                    logger.warning("OpenReview search [%s %s / '%s']: %s", conf_name, year, query, exc)
                time.sleep(_DELAY)
        return results

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
        return [
            p for item in (data.get("notes") or [])
            if (p := _parse_note(item, conf_name, year)) is not None
        ]

    # ------------------------------------------------------------------
    # Strategy 2: /notes  (bulk list, local keyword filter)
    # ------------------------------------------------------------------

    def _fetch_bulk(
        self, venue_id: str, conf_name: str, year: Optional[int]
    ) -> List[Paper]:
        """Fetch all accepted papers for a venue and filter locally."""
        papers: List[Paper] = []
        offset = 0

        while True:
            try:
                resp = self.session.get(
                    f"{_API}/notes",
                    params={
                        "content.venueid": venue_id,
                        "details": "replyCount",
                        "offset": offset,
                        "limit": _LIMIT,
                    },
                    timeout=30,
                )
                resp.raise_for_status()
            except requests.exceptions.HTTPError as exc:
                code = exc.response.status_code if exc.response is not None else 0
                logger.warning("OpenReview bulk [%s %s]: HTTP %d", conf_name, year, code)
                break
            except Exception as exc:
                logger.warning("OpenReview bulk [%s %s]: %s", conf_name, year, exc)
                break

            data = resp.json()
            notes = data.get("notes") or []
            if not notes:
                break

            for item in notes:
                p = _parse_note(item, conf_name, year)
                if p and _is_topic_relevant(p):
                    papers.append(p)

            total = data.get("count", 0)
            offset += len(notes)
            if offset >= total:
                break
            time.sleep(_DELAY)

        logger.debug("OpenReview bulk [%s %s]: %d relevant papers", conf_name, year or "?", len(papers))
        return papers


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _is_topic_relevant(paper: Paper) -> bool:
    combined = f"{paper.title} {paper.abstract}".lower()
    return any(kw in combined for kw in _TOPIC_KEYWORDS)


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
