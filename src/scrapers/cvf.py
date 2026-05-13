"""
CVF (Computer Vision Foundation) open-access scraper.

Fetches CVPR (and optionally ICCV/ECCV) paper listings from
https://openaccess.thecvf.com/ and filters by topic keywords.

Strategy:
  1. Download the full conference index page (?day=all)
  2. Parse paper titles and abstract-page URLs from the HTML
     using only Python's built-in html.parser — no extra deps.
  3. Filter: keep papers whose title contains a topic keyword.
  4. For each matching paper, fetch its abstract page to get
     the abstract and full author list.

This gives comprehensive CVPR coverage without requiring an API key.
"""
from __future__ import annotations

import logging
import re
import time
from datetime import date
from html.parser import HTMLParser
from typing import List, Optional, Tuple
from urllib.parse import urljoin

import requests

from ..config import MIN_YEAR, TOPICS
from ..models import Paper

logger = logging.getLogger(__name__)

_BASE = "https://openaccess.thecvf.com"
_DELAY_INDEX = 3.0      # wait after fetching the big index page
_DELAY_PAPER = 1.0      # wait between individual paper-page requests
_TODAY = date.today()

# Which CVF conferences to scrape, and approximate month they conclude
_CVF_CONFERENCES = [
    ("CVPR",  6),   # typically June
    ("ICCV",  10),  # typically October (odd years only)
    ("ECCV",  10),  # typically October (even years only)
    ("WACV",  1),   # typically January
]


def _conference_years(conf: str, conf_month: int) -> List[int]:
    """Return years whose proceedings are publicly available."""
    years = []
    for y in range(_TODAY.year, _TODAY.year - 3, -1):
        # ICCV is odd years only; ECCV is even years only
        if conf == "ICCV" and y % 2 == 0:
            continue
        if conf == "ECCV" and y % 2 != 0:
            continue
        if y < _TODAY.year:
            years.append(y)
        elif y == _TODAY.year and _TODAY.month >= conf_month:
            years.append(y)
    return years


# ---------------------------------------------------------------------------
# HTML parsers
# ---------------------------------------------------------------------------

class _IndexParser(HTMLParser):
    """Extract (title, paper_page_href) pairs from a CVF index page.

    The CVF HTML structure uses:
      <dt class="ptitle"><a href="/CVPR2025/html/...">Title</a></dt>
    """

    def __init__(self):
        super().__init__()
        self._in_ptitle = False
        self._current_href: str = ""
        self._current_title: str = ""
        self.papers: List[Tuple[str, str]] = []  # (title, href)

    def handle_starttag(self, tag: str, attrs):
        attr = dict(attrs)
        if tag == "dt" and "ptitle" in attr.get("class", ""):
            self._in_ptitle = True
        if self._in_ptitle and tag == "a":
            self._current_href = attr.get("href", "")

    def handle_data(self, data: str):
        if self._in_ptitle and self._current_href:
            self._current_title += data

    def handle_endtag(self, tag: str):
        if tag == "dt" and self._in_ptitle:
            title = self._current_title.strip()
            href = self._current_href.strip()
            if title and href:
                self.papers.append((title, href))
            self._in_ptitle = False
            self._current_href = ""
            self._current_title = ""


class _PaperPageParser(HTMLParser):
    """Extract abstract and authors from a CVF individual paper page.

    Structure:
      <div id="papertitle">Title</div>
      <div id="authors"><b>Author1, Author2, ...</b></div>
      <div id="abstract">Abstract text</div>
    """

    def __init__(self):
        super().__init__()
        self._in_target: Optional[str] = None  # 'abstract' | 'authors'
        self._in_bold = False
        self.abstract: str = ""
        self.authors: str = ""

    def handle_starttag(self, tag: str, attrs):
        attr = dict(attrs)
        div_id = attr.get("id", "")
        if tag == "div" and div_id in ("abstract", "authors"):
            self._in_target = div_id
        if self._in_target == "authors" and tag == "b":
            self._in_bold = True

    def handle_data(self, data: str):
        if self._in_target == "abstract":
            self.abstract += data
        elif self._in_target == "authors" and self._in_bold:
            self.authors += data

    def handle_endtag(self, tag: str):
        if tag == "div":
            self._in_target = None
        if tag == "b":
            self._in_bold = False


# ---------------------------------------------------------------------------
# Topic-keyword matching
# ---------------------------------------------------------------------------

_ALL_KEYWORDS = {
    kw.lower()
    for keywords in TOPICS.values()
    for kw in keywords
}

# Shorter, faster set of title-level keywords (avoids fetching abstracts for
# papers that clearly don't match any topic)
_TITLE_KEYWORDS: List[str] = sorted(_ALL_KEYWORDS, key=len, reverse=True)


def _title_matches(title: str) -> bool:
    t = title.lower()
    return any(kw in t for kw in _TITLE_KEYWORDS)


# ---------------------------------------------------------------------------
# Main scraper class
# ---------------------------------------------------------------------------

class CVFScraper:
    """Scrape CVPR (and related CVF) papers for Agent/Harness/Finance topics."""

    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": "paper-find-bot/1.0"})

    def fetch(self) -> List[Paper]:
        papers: List[Paper] = []
        seen_titles: set = set()

        for conf, conf_month in _CVF_CONFERENCES:
            for year in _conference_years(conf, conf_month):
                if year < MIN_YEAR:
                    continue
                try:
                    batch = self._fetch_conference(conf, year)
                    for p in batch:
                        key = p.get_id()
                        if key not in seen_titles:
                            seen_titles.add(key)
                            papers.append(p)
                    logger.info("CVF %s %d: %d topic-matching papers", conf, year, len(batch))
                except Exception as exc:
                    logger.error("CVF %s %d error: %s", conf, year, exc)

        logger.info("CVF total: %d papers", len(papers))
        return papers

    # ------------------------------------------------------------------

    def _fetch_conference(self, conf: str, year: int) -> List[Paper]:
        index_url = f"{_BASE}/{conf}{year}?day=all"
        logger.info("CVF: fetching index %s", index_url)
        try:
            resp = self.session.get(index_url, timeout=60)
            resp.raise_for_status()
        except Exception as exc:
            logger.error("CVF index fetch failed (%s %d): %s", conf, year, exc)
            return []

        time.sleep(_DELAY_INDEX)

        parser = _IndexParser()
        parser.feed(resp.text)

        if not parser.papers:
            logger.warning("CVF %s %d: no papers found in index (HTML structure may have changed)", conf, year)
            return []

        logger.debug("CVF %s %d: %d total papers in index", conf, year, len(parser.papers))

        # Filter by title keywords first (cheap)
        candidates = [
            (title, href)
            for title, href in parser.papers
            if _title_matches(title)
        ]
        logger.debug("CVF %s %d: %d title-matching candidates", conf, year, len(candidates))

        results: List[Paper] = []
        for title, href in candidates:
            paper = self._fetch_paper(title, href, conf, year)
            if paper:
                results.append(paper)
            time.sleep(_DELAY_PAPER)

        return results

    def _fetch_paper(
        self, title: str, href: str, conf: str, year: int
    ) -> Optional[Paper]:
        paper_url = urljoin(_BASE, href)
        abstract = ""
        authors: List[str] = []

        try:
            resp = self.session.get(paper_url, timeout=30)
            resp.raise_for_status()
            pp = _PaperPageParser()
            pp.feed(resp.text)
            abstract = pp.abstract.strip()
            authors = [
                a.strip()
                for a in pp.authors.replace(";", ",").split(",")
                if a.strip()
            ]
        except Exception as exc:
            logger.debug("CVF paper page fetch failed (%s): %s", paper_url, exc)
            # Still create a paper with just the title

        # Try to extract an arXiv ID from the paper page URL or abstract
        arxiv_id = _extract_arxiv_id(abstract + " " + paper_url)

        url = (
            f"https://arxiv.org/abs/{arxiv_id}"
            if arxiv_id
            else paper_url
        )

        return Paper(
            title=title,
            abstract=abstract,
            authors=authors,
            url=url,
            arxiv_id=arxiv_id,
            conference=conf,
            year=year,
            source="cvf",
            published_date=date(year, 6, 1),  # approximate: June of conference year
        )


# ---------------------------------------------------------------------------

_ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})")


def _extract_arxiv_id(text: str) -> Optional[str]:
    m = _ARXIV_RE.search(text)
    return m.group(1) if m else None
