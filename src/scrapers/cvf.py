"""
CVF OpenAccess scraper for CVPR (and ICCV/WACV if needed).

Fetches accepted papers from https://openaccess.thecvf.com/
and filters by Agent / Harness / Finance topic keywords.

The CVF site lists all accepted papers in structured HTML:
  https://openaccess.thecvf.com/CVPR<YEAR>?day=all
"""
from __future__ import annotations

import logging
import re
import time
from datetime import date
from typing import List, Optional

import requests

from ..config import TOPICS
from ..models import Paper

logger = logging.getLogger(__name__)

_BASE = "https://openaccess.thecvf.com"
_DELAY = 2.0            # seconds between HTTP requests
_CUR_YEAR = date.today().year

# Conferences exposed by CVF OpenAccess
CVF_VENUES = [
    ("CVPR", f"CVPR{_CUR_YEAR}"),
    ("CVPR", f"CVPR{_CUR_YEAR - 1}"),
    ("ICCV", f"ICCV{_CUR_YEAR - 1}"),   # ICCV is biennial
]

_ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})")


class CVFScraper:
    """Scrape CVF OpenAccess paper listings for CVPR / ICCV."""

    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": "paper-find-bot/1.0"})

    def fetch(self) -> List[Paper]:
        """Return CVF papers that match Agent / Harness / Finance topics."""
        all_papers: list[Paper] = []
        seen: set[str] = set()

        for conf_name, venue_tag in CVF_VENUES:
            try:
                papers = self._fetch_venue(conf_name, venue_tag)
                for p in papers:
                    pid = p.get_id()
                    if pid not in seen:
                        seen.add(pid)
                        all_papers.append(p)
                logger.info("CVF [%s]: %d papers collected", venue_tag, len(papers))
            except Exception as exc:
                logger.warning("CVF [%s] error: %s", venue_tag, exc)
            time.sleep(_DELAY)

        return all_papers

    def _fetch_venue(self, conf_name: str, venue_tag: str) -> List[Paper]:
        url = f"{_BASE}/{venue_tag}?day=all"
        resp = self.session.get(url, timeout=60)
        resp.raise_for_status()
        return _parse_cvf_html(resp.text, conf_name, venue_tag)


# ---------------------------------------------------------------------------
# HTML parsing  (no external dependency — uses stdlib re only)
# ---------------------------------------------------------------------------

_PAPER_BLOCK_RE = re.compile(
    r'<dt class="ptitle">(.*?)</dd>',
    re.DOTALL,
)
_TITLE_RE = re.compile(r'<a[^>]*>\s*(.*?)\s*</a>', re.DOTALL)
_AUTHOR_RE = re.compile(r'<i>(.*?)</i>', re.DOTALL)
_ARXIV_LINK_RE = re.compile(r'href="(https://arxiv\.org/[^"]+)"')
_PAPER_LINK_RE = re.compile(r'href="(/[^"]+\.html)"')
_YEAR_RE = re.compile(r"\d{4}")


def _parse_cvf_html(html: str, conf_name: str, venue_tag: str) -> List[Paper]:
    year_m = _YEAR_RE.search(venue_tag)
    year = int(year_m.group()) if year_m else None

    all_keywords = [kw.lower() for kws in TOPICS.values() for kw in kws]

    papers: List[Paper] = []
    for block_m in _PAPER_BLOCK_RE.finditer(html):
        block = block_m.group(0)

        title_m = _TITLE_RE.search(block)
        if not title_m:
            continue
        title = re.sub(r"<[^>]+>", "", title_m.group(1)).strip()
        if not title:
            continue

        # Topic filter: skip papers with no keyword match
        title_lower = title.lower()
        if not any(kw in title_lower for kw in all_keywords):
            continue

        authors: List[str] = []
        auth_m = _AUTHOR_RE.search(block)
        if auth_m:
            raw = re.sub(r"<[^>]+>", "", auth_m.group(1))
            authors = [a.strip() for a in raw.split(",") if a.strip()]

        arxiv_id: Optional[str] = None
        url = ""
        arxiv_m = _ARXIV_LINK_RE.search(block)
        if arxiv_m:
            arxiv_url = arxiv_m.group(1)
            m2 = _ARXIV_RE.search(arxiv_url)
            if m2:
                arxiv_id = m2.group(1)
                url = f"https://arxiv.org/abs/{arxiv_id}"
        if not url:
            link_m = _PAPER_LINK_RE.search(block)
            if link_m:
                url = f"{_BASE}{link_m.group(1)}"

        papers.append(
            Paper(
                title=title,
                authors=authors,
                url=url,
                arxiv_id=arxiv_id,
                conference=conf_name,
                year=year,
                source="cvf",
            )
        )

    return papers
