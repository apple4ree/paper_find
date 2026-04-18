"""
CVF OpenAccess scraper for CVPR conference papers.

Fetches the accepted paper list from openaccess.thecvf.com and filters
papers that match Agent / Harness / Finance topic keywords.

Strategy:
  1. Fetch the conference HTML listing page (one request per year).
  2. Parse all paper blocks via regex (title, authors, arXiv ID).
  3. Keep only papers whose title matches at least one topic keyword.
  4. Return Paper objects with conference="CVPR" set; abstracts arrive
     later via deduplication with the arXiv scraper (shared arxiv_id).

No individual paper pages are fetched, so the scraper is very fast
(1-2 HTTP requests per conference year).
"""
from __future__ import annotations

import logging
import re
import time
from datetime import date
from html import unescape
from typing import Dict, List, Optional

import requests

from ..config import TOPICS
from ..models import Paper

logger = logging.getLogger(__name__)

_BASE = "https://openaccess.thecvf.com"
_DELAY = 2.0          # seconds between conference-year requests
_TIMEOUT = 90         # seconds – the full listing page can be large
_CUR_YEAR = date.today().year

# Conference IDs to fetch (canonical name → CVF URL slugs, newest first)
CVF_VENUES: Dict[str, List[str]] = {
    "CVPR": [
        f"CVPR{_CUR_YEAR}",
        f"CVPR{_CUR_YEAR - 1}",
    ],
}

# Flat set of all topic keywords for fast title pre-filter
_TOPIC_KEYWORDS: List[str] = sorted(
    {kw.lower() for kws in TOPICS.values() for kw in kws},
    key=len,
    reverse=True,   # longer keywords first to avoid partial-match noise
)


class CVFScraper:
    """Scrape CVF OpenAccess for CVPR accepted papers."""

    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self.session.headers.update({
            "User-Agent": "paper-find-bot/1.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
        })

    def fetch(self) -> List[Paper]:
        all_papers: Dict[str, Paper] = {}

        for conf_name, venue_ids in CVF_VENUES.items():
            for venue_id in venue_ids:
                year_m = re.search(r"(\d{4})", venue_id)
                year = int(year_m.group(1)) if year_m else None
                try:
                    papers = self._fetch_venue(venue_id, conf_name, year)
                    before = len(all_papers)
                    for p in papers:
                        pid = p.get_id()
                        if pid not in all_papers:
                            all_papers[pid] = p
                    logger.info(
                        "CVF %s: %d papers fetched, %d new",
                        venue_id, len(papers), len(all_papers) - before,
                    )
                except Exception as exc:
                    logger.warning("CVF %s: fetch error — %s", venue_id, exc)
                time.sleep(_DELAY)

        return list(all_papers.values())

    # ------------------------------------------------------------------

    def _fetch_venue(
        self,
        venue_id: str,
        conf_name: str,
        year: Optional[int],
    ) -> List[Paper]:
        url = f"{_BASE}/{venue_id}"
        resp = self.session.get(url, timeout=_TIMEOUT)
        resp.raise_for_status()
        return _parse_listing(resp.text, conf_name, year)


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

# Split the page into per-paper blocks at each <dt class="ptitle"> tag
_DT_SPLIT = re.compile(r'<dt\s[^>]*class="ptitle"[^>]*>', re.IGNORECASE)

# Extract paper-page URL and title from the first <a href="..."> in the block
_TITLE_RE = re.compile(
    r'<a\s+href="(/content/[^"]+\.html)"[^>]*>(.*?)</a>',
    re.DOTALL | re.IGNORECASE,
)

# Authors div
_AUTHORS_RE = re.compile(
    r'<div\s[^>]*class="authors"[^>]*>(.*?)</div>',
    re.DOTALL | re.IGNORECASE,
)

# arXiv absolute URL anywhere in the block
_ARXIV_RE = re.compile(
    r'arxiv\.org/abs/(\d{4}\.\d{4,5})',
    re.IGNORECASE,
)

# Strip HTML tags
_TAG_RE = re.compile(r'<[^>]+>')


def _parse_listing(html: str, conf_name: str, year: Optional[int]) -> List[Paper]:
    blocks = _DT_SPLIT.split(html)
    papers: List[Paper] = []
    for block in blocks[1:]:   # first chunk is header; skip it
        p = _parse_block(block, conf_name, year)
        if p:
            papers.append(p)
    return papers


def _parse_block(block: str, conf_name: str, year: Optional[int]) -> Optional[Paper]:
    # --- Title & paper URL ---
    tm = _TITLE_RE.search(block)
    if not tm:
        return None
    paper_path = tm.group(1)
    title = unescape(_TAG_RE.sub("", tm.group(2))).strip()
    if not title:
        return None

    # --- Topic pre-filter on title (fast path, no abstract yet) ---
    title_lower = title.lower()
    if not any(kw in title_lower for kw in _TOPIC_KEYWORDS):
        return None

    # --- Authors ---
    am = _AUTHORS_RE.search(block)
    authors: List[str] = []
    if am:
        raw = unescape(_TAG_RE.sub("", am.group(1))).strip()
        authors = [a.strip() for a in raw.split(",") if a.strip()]

    # --- arXiv ID ---
    arxiv_m = _ARXIV_RE.search(block)
    arxiv_id: Optional[str] = arxiv_m.group(1) if arxiv_m else None

    # --- URL: prefer arXiv, fall back to CVF page ---
    if arxiv_id:
        url = f"https://arxiv.org/abs/{arxiv_id}"
    else:
        url = f"{_BASE}{paper_path}"

    return Paper(
        title=title,
        authors=authors,
        url=url,
        arxiv_id=arxiv_id,
        conference=conf_name,
        year=year,
        source="cvf",
    )
