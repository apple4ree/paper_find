"""
CVF (Computer Vision Foundation) open access scraper for CVPR and ICCV.

Fetches paper listings from https://openaccess.thecvf.com/ and filters
by topic keywords. Papers are organized by conference year.

Page structure: each paper entry contains title, author list, and links
to the abstract/PDF. Abstract is fetched per-paper only for keyword matches
found in the title (to avoid hitting the server for every paper).
"""
from __future__ import annotations

import logging
import re
import time
from datetime import date
from typing import Dict, List, Optional
from urllib.parse import urljoin

import requests

from ..config import TOPICS
from ..models import Paper

logger = logging.getLogger(__name__)

_BASE = "https://openaccess.thecvf.com"
_DELAY = 1.0          # seconds between per-paper abstract fetches
_CUR_YEAR = date.today().year

# Conferences and the years we pull. CVPR happens every year; ICCV is odd years.
CVF_VENUES: Dict[str, List[int]] = {
    "CVPR": [_CUR_YEAR, _CUR_YEAR - 1],
    "ICCV": [y for y in [_CUR_YEAR, _CUR_YEAR - 1] if y % 2 == 1],
}

# Title-level keywords (quick filter before fetching the full abstract)
_TITLE_KEYWORDS: List[str] = []
for kw_list in TOPICS.values():
    _TITLE_KEYWORDS.extend(kw_list)
_TITLE_KEYWORDS = list(dict.fromkeys(k.lower() for k in _TITLE_KEYWORDS))

_ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})")


class CvfScraper:
    """Scrape CVF open access proceedings for topic-relevant papers."""

    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": "paper-find-bot/1.0"})

    def fetch(self) -> List[Paper]:
        seen: Dict[str, Paper] = {}

        for conf_name, years in CVF_VENUES.items():
            for year in years:
                try:
                    papers = self._fetch_conference(conf_name, year)
                    for p in papers:
                        pid = p.get_id()
                        if pid not in seen:
                            seen[pid] = p
                    logger.info("CVF %s %d: %d papers", conf_name, year, len(papers))
                except Exception as exc:
                    logger.warning("CVF %s %d: %s", conf_name, year, exc)

        logger.info("CVF: %d unique papers total", len(seen))
        return list(seen.values())

    # ------------------------------------------------------------------

    def _fetch_conference(self, conf_name: str, year: int) -> List[Paper]:
        url = f"{_BASE}/{conf_name}{year}?day=all"
        try:
            resp = self.session.get(url, timeout=30)
            resp.raise_for_status()
        except Exception as exc:
            logger.warning("CVF page fetch failed (%s %d): %s", conf_name, year, exc)
            return []

        return self._parse_listing(resp.text, conf_name, year)

    def _parse_listing(self, html: str, conf_name: str, year: int) -> List[Paper]:
        """Parse the CVF listing page (no external deps — pure regex)."""
        papers: List[Paper] = []

        # Each paper block looks like:
        #   <dt class="ptitle"><a href="/content/CVPR2025/html/Foo_Bar_CVPR_2025_paper.html">Title</a></dt>
        #   <dd><form ...><a href="...pdf">pdf</a> | <a href="...supplemental">supp</a></form>
        #       <a href="/content/CVPR2025/html/...">Abstract</a></dd>

        title_re = re.compile(
            r'<dt class="ptitle">\s*<a href="([^"]+)"[^>]*>\s*(.*?)\s*</a>\s*</dt>',
            re.DOTALL,
        )
        author_block_re = re.compile(
            r'<div class="authors">(.*?)</div>', re.DOTALL
        )
        author_name_re = re.compile(r'<a [^>]*>([^<]+)</a>')

        # Find all paper entries with their surrounding block
        # We iterate title tags and grab the nearest author block
        title_matches = list(title_re.finditer(html))

        for i, m in enumerate(title_matches):
            abstract_path = m.group(1)
            raw_title = re.sub(r"<[^>]+>", "", m.group(2)).strip()
            title = re.sub(r"\s+", " ", raw_title)

            # Quick keyword filter on title
            title_lower = title.lower()
            if not any(kw in title_lower for kw in _TITLE_KEYWORDS):
                continue

            # Extract authors from the block between this title and the next
            start = m.end()
            end = title_matches[i + 1].start() if i + 1 < len(title_matches) else len(html)
            block = html[start:end]

            authors: List[str] = []
            ab_m = author_block_re.search(block)
            if ab_m:
                authors = author_name_re.findall(ab_m.group(1))

            abstract_url = urljoin(_BASE, abstract_path)
            abstract, arxiv_id = self._fetch_abstract(abstract_url)

            url = f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else abstract_url

            papers.append(Paper(
                title=title,
                abstract=abstract,
                authors=authors,
                url=url,
                arxiv_id=arxiv_id,
                conference=conf_name,
                year=year,
                source="cvf",
                published_date=date(year, 6, 1),  # CVPR ≈ June
            ))

        return papers

    def _fetch_abstract(self, url: str) -> tuple[str, Optional[str]]:
        """Fetch abstract text and arXiv ID from a CVF paper page."""
        time.sleep(_DELAY)
        try:
            resp = self.session.get(url, timeout=30)
            resp.raise_for_status()
            html = resp.text
        except Exception as exc:
            logger.debug("CVF abstract fetch failed (%s): %s", url, exc)
            return "", None

        # Abstract
        abs_m = re.search(
            r'<div id="abstract"[^>]*>\s*<p>(.*?)</p>', html, re.DOTALL
        )
        abstract = ""
        if abs_m:
            abstract = re.sub(r"<[^>]+>", "", abs_m.group(1)).strip()
            abstract = re.sub(r"\s+", " ", abstract)

        # arXiv link
        arxiv_id: Optional[str] = None
        am = _ARXIV_RE.search(html)
        if am:
            arxiv_id = am.group(1)

        return abstract, arxiv_id
