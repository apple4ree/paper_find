"""
CVF (Computer Vision Foundation) scraper for CVPR / ICCV / ECCV proceedings.

The CVF open-access page at https://openaccess.thecvf.com lists paper titles
and PDF links for all accepted papers.  We fetch the index page for each
target year, extract paper metadata, and filter by topic keywords.

This gives us CVPR coverage independent of Semantic Scholar.
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

# CVF open-access index pages
_CVF_BASE = "https://openaccess.thecvf.com"
_CUR_YEAR = date.today().year

# Conference → list of CVF index URLs to try (current + previous year)
_CVF_URLS: dict[str, list[str]] = {
    "CVPR": [
        f"{_CVF_BASE}/CVPR{_CUR_YEAR}.py",
        f"{_CVF_BASE}/CVPR{_CUR_YEAR - 1}.py",
    ],
}

_DELAY = 2.0

# All topic keywords for local filtering (lowercase, merged)
_ALL_KEYWORDS: list[str] = sorted(
    {kw.lower() for kws in TOPICS.values() for kw in kws}
)

# Regex patterns for CVF page parsing
_PAPER_TITLE_RE = re.compile(
    r'<dt class="ptitle"><br><a href="([^"]+)"[^>]*>(.*?)</a>', re.DOTALL
)
_ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})")
_AUTHOR_RE = re.compile(r'<dd>(.*?)</dd>', re.DOTALL)

_BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html, */*;q=0.9",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://openaccess.thecvf.com/",
}


class CVFScraper:
    """Fetch CVPR (and optionally ICCV/ECCV) papers from CVF open access."""

    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self.session.headers.update(_BROWSER_HEADERS)

    def fetch(self) -> List[Paper]:
        seen: dict[str, Paper] = {}
        for conf_name, urls in _CVF_URLS.items():
            for url in urls:
                year_m = re.search(r"(\d{4})", url)
                year = int(year_m.group(1)) if year_m else None
                try:
                    papers = self._fetch_index(url, conf_name, year)
                    for p in papers:
                        pid = p.get_id()
                        if pid not in seen:
                            seen[pid] = p
                    logger.info(
                        "CVF [%s %s]: %d relevant papers", conf_name, year or "?", len(papers)
                    )
                except Exception as exc:
                    logger.warning("CVF [%s %s]: %s", conf_name, year or "?", exc)
                time.sleep(_DELAY)

        logger.info("CVF total: %d unique papers", len(seen))
        return list(seen.values())

    def _fetch_index(
        self, url: str, conf_name: str, year: Optional[int]
    ) -> List[Paper]:
        resp = self.session.get(url, timeout=60)
        resp.raise_for_status()
        html = resp.text
        return _parse_cvf_html(html, conf_name, year)


# ---------------------------------------------------------------------------
# HTML parsing
# ---------------------------------------------------------------------------

def _parse_cvf_html(html: str, conf_name: str, year: Optional[int]) -> List[Paper]:
    """Extract papers from a CVF proceedings index page."""
    papers: List[Paper] = []

    # Each paper block looks like:
    #   <dt class="ptitle"><br><a href="/content/CVPR2025/html/...">Title</a>
    #   <dd>Author A, Author B, ...<br><a href="/content/.../papers/...pdf">pdf</a>
    #   ...

    # Split by paper title entries
    blocks = re.split(r'<dt class="ptitle">', html)
    for block in blocks[1:]:  # skip preamble
        paper = _parse_block(block, conf_name, year)
        if paper and _is_relevant(paper):
            papers.append(paper)

    return papers


def _parse_block(block: str, conf_name: str, year: Optional[int]) -> Optional[Paper]:
    # Title
    title_m = re.search(r'<a href="([^"]+)"[^>]*>(.*?)</a>', block, re.DOTALL)
    if not title_m:
        return None

    detail_path = title_m.group(1).strip()
    title = re.sub(r"<[^>]+>", "", title_m.group(2)).strip()
    title = re.sub(r"\s+", " ", title)
    if not title:
        return None

    # URL
    url = f"{_CVF_BASE}{detail_path}" if detail_path.startswith("/") else detail_path

    # arXiv ID from any link in the block
    arxiv_id: Optional[str] = None
    m = _ARXIV_RE.search(block)
    if m:
        arxiv_id = m.group(1)
        url = f"https://arxiv.org/abs/{arxiv_id}"

    # Authors — first <dd> block
    authors: List[str] = []
    dd_m = _AUTHOR_RE.search(block)
    if dd_m:
        raw = dd_m.group(1)
        # Strip HTML tags, split on comma
        raw_text = re.sub(r"<[^>]+>", "", raw)
        authors = [a.strip() for a in raw_text.split(",") if a.strip()]

    return Paper(
        title=title,
        authors=authors,
        url=url,
        arxiv_id=arxiv_id,
        conference=conf_name,
        year=year,
        source="cvf",
        published_date=date(year, 1, 1) if year else None,
    )


def _is_relevant(paper: Paper) -> bool:
    combined = f"{paper.title} {paper.abstract}".lower()
    return any(kw in combined for kw in _ALL_KEYWORDS)
