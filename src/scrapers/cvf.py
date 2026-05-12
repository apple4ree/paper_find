"""
CVF (Computer Vision Foundation) Open Access scraper for CVPR papers.

Fetches paper listings from openaccess.thecvf.com for the current and
previous year, then filters on title keywords so we only keep papers
relevant to Agent / Harness / Finance without loading per-paper detail pages.

Page URL pattern:  https://openaccess.thecvf.com/CVPR{YYYY}?day=all
Each entry has the structure:
  <dt class="ptitle"><a href="/content/CVPR2025/html/…">Title</a></dt>
  <dd>  pdf  [arXiv link]  [supp]  </dd>
  <dd class="note">Author1, Author2, …</dd>
"""
from __future__ import annotations

import logging
import re
import time
from datetime import date
from html.parser import HTMLParser
from typing import Dict, List, Optional, Tuple

import requests

from ..models import Paper

logger = logging.getLogger(__name__)

CVF_BASE = "https://openaccess.thecvf.com"
_ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})")
_CUR_YEAR = date.today().year

# Years to scrape (current + previous)
_YEARS = [_CUR_YEAR, _CUR_YEAR - 1]

# Title-level keywords for quick pre-filtering (no abstracts available)
# Keys must match TOPICS keys in config.py
_TITLE_KEYWORDS: Dict[str, List[str]] = {
    "Agent": [
        "agent",
        "agentic",
        "multi-agent",
        "multiagent",
        "embodied",
        "autonomous",
        "navigation",
        "manipulation",
        "grounding",
        "instruction follow",
        "planning",
        "policy",
        "robot",
        "gui",
        "tool use",
        "tool-use",
        "function call",
        "interactive",
        "human-robot",
        "human robot",
        "task-oriented",
        "task oriented",
        "visual agent",
    ],
    "Harness": [
        "benchmark",
        "evaluation",
        "harness",
        "assess",
        "metric",
        "survey",
        "test suite",
        "baseline",
        "comparison",
        "diagnostic",
        "probing",
        "capability",
    ],
    "Finance": [
        "financ",
        "trading",
        "stock",
        "portfolio",
        "market",
        "risk",
        "fraud",
        "crypto",
        "blockchain",
        "economic",
        "investment",
        "defi",
        "forex",
    ],
}


class CVFScraper:
    """Scrape CVPR proceedings from the CVF Open Access website."""

    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": "paper-find-bot/1.0"})

    def fetch(self) -> List[Paper]:
        collected: Dict[str, Paper] = {}
        for year in _YEARS:
            venue = f"CVPR{year}"
            try:
                papers = self._fetch_venue(venue, year)
                new = 0
                for p in papers:
                    pid = p.get_id()
                    if pid not in collected:
                        collected[pid] = p
                        new += 1
                logger.info("CVF %s: %d matching papers", venue, new)
            except Exception as exc:
                logger.warning("CVF %s error: %s", venue, exc)
            time.sleep(1.5)
        return list(collected.values())

    def _fetch_venue(self, venue: str, year: int) -> List[Paper]:
        url = f"{CVF_BASE}/{venue}?day=all"
        resp = self.session.get(url, timeout=90)
        resp.raise_for_status()
        raw_entries = _parse_cvf_listing(resp.text)

        papers: List[Paper] = []
        for title, href, authors_str, arxiv_id in raw_entries:
            if not _title_matches(title):
                continue

            url_paper = (
                f"https://arxiv.org/abs/{arxiv_id}"
                if arxiv_id
                else f"{CVF_BASE}{href}" if href.startswith("/") else href
            )
            authors = [a.strip() for a in authors_str.split(",") if a.strip()]

            papers.append(
                Paper(
                    title=title,
                    abstract="",
                    authors=authors,
                    url=url_paper,
                    arxiv_id=arxiv_id,
                    conference="CVPR",
                    year=year,
                    source="cvf",
                    published_date=date(year, 6, 1),  # CVPR is held in June
                )
            )
        return papers


# ---------------------------------------------------------------------------
# HTML parsing
# ---------------------------------------------------------------------------

class _CVFListingParser(HTMLParser):
    """
    Extract (title, href, authors, arxiv_id) tuples from the CVF listing page.

    State machine:
      - Watching for <dt class="ptitle">  → enter title mode
      - Inside title mode, grab the first <a> href and its text
      - After </dt>, watch for first <dd> (links row) then <dd class="note"> (authors)
    """

    def __init__(self) -> None:
        super().__init__()
        self.entries: List[Tuple[str, str, str, Optional[str]]] = []

        self._in_ptitle: bool = False
        self._title_text: str = ""
        self._title_href: str = ""

        self._links_row: bool = False   # first <dd> after <dt class="ptitle">
        self._links_html: str = ""

        self._in_note: bool = False     # <dd class="note">
        self._note_text: str = ""

        self._pending_title: str = ""
        self._pending_href: str = ""
        self._pending_links: str = ""

    # -- tag handlers --------------------------------------------------------

    def handle_starttag(self, tag: str, attrs) -> None:  # type: ignore[override]
        d = dict(attrs)

        if tag == "dt" and d.get("class") == "ptitle":
            self._in_ptitle = True
            self._title_text = ""
            self._title_href = ""
            self._links_row = False
            self._in_note = False
            return

        if tag == "a" and self._in_ptitle and not self._title_href:
            self._title_href = d.get("href", "")
            return

        if tag == "dd":
            cls = d.get("class", "")
            if cls == "note" and self._pending_title:
                self._in_note = True
                self._note_text = ""
            elif cls != "note" and self._pending_title and not self._links_row:
                # First plain <dd> after the title: links row
                self._links_row = True
                self._links_html = ""

    def handle_endtag(self, tag: str) -> None:  # type: ignore[override]
        if tag == "dt" and self._in_ptitle:
            self._in_ptitle = False
            if self._title_text.strip():
                self._pending_title = self._title_text.strip()
                self._pending_href = self._title_href

        if tag == "dd":
            if self._in_note and self._pending_title:
                arxiv_id: Optional[str] = None
                m = _ARXIV_RE.search(self._pending_links)
                if m:
                    arxiv_id = m.group(1)
                self.entries.append((
                    self._pending_title,
                    self._pending_href,
                    self._note_text.strip(),
                    arxiv_id,
                ))
                # Reset for next paper
                self._pending_title = ""
                self._pending_href = ""
                self._pending_links = ""
                self._in_note = False
                self._links_row = False
            elif self._links_row:
                # Save links HTML before clearing the flag so arXiv IDs are
                # available when the note <dd> is processed next.
                self._pending_links = self._links_html
                self._links_row = False

    def handle_data(self, data: str) -> None:  # type: ignore[override]
        if self._in_ptitle:
            self._title_text += data
        elif self._links_row:
            self._links_html += data
        elif self._in_note:
            self._note_text += data

    def handle_starttag_html(self, tag: str, attrs) -> None:  # type: ignore[override]
        if self._links_row:
            d = dict(attrs)
            href = d.get("href", "")
            if href:
                self._links_html += f" {href} "


def _parse_cvf_listing(
    html: str,
) -> List[Tuple[str, str, str, Optional[str]]]:
    """Parse CVF listing HTML and return list of (title, href, authors, arxiv_id)."""
    # Also collect href attrs from links in the dd row so we can find arXiv links.
    # We patch the parser to store raw href values from anchor tags.
    class _FullParser(_CVFListingParser):
        def handle_starttag(self, tag: str, attrs) -> None:
            super().handle_starttag(tag, attrs)
            if tag == "a" and self._links_row:
                d = dict(attrs)
                href = d.get("href", "")
                if href:
                    self._links_html += f" {href} "

    parser = _FullParser()
    parser.feed(html)
    return parser.entries


# ---------------------------------------------------------------------------
# Title-level keyword matching
# ---------------------------------------------------------------------------

def _title_matches(title: str) -> bool:
    """Return True if the title contains at least one keyword from any topic."""
    t = title.lower()
    for kw_list in _TITLE_KEYWORDS.values():
        if any(kw in t for kw in kw_list):
            return True
    return False
