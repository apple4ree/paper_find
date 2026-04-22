"""
CVF OpenAccess scraper for CVPR.

Strategy:
  1. Fetch the full paper list from openaccess.thecvf.com/CVPR{year}?day=all
  2. Filter entries whose title contains a topic keyword
  3. For each matching paper, try to retrieve the abstract from the paper page
     (falling back to arXiv abs if the arxiv link is available).

Dependencies: beautifulsoup4 (added to requirements.txt)
"""
from __future__ import annotations

import logging
import re
import time
from datetime import date
from typing import List, Optional
from urllib.parse import urljoin

import requests

from ..config import TOPICS
from ..models import Paper

logger = logging.getLogger(__name__)

CVF_BASE = "https://openaccess.thecvf.com"
_DELAY = 2.0          # seconds between HTTP requests
_ABSTRACT_DELAY = 1.5 # seconds between abstract fetches
_CUR_YEAR = date.today().year

# Try current year and one year back
CVF_VENUES = [_CUR_YEAR, _CUR_YEAR - 1]

# Broad title-level keywords used as a fast pre-filter (before full-text match)
_TITLE_FILTERS: dict[str, list[str]] = {
    "Agent": [
        "agent", "agentic", "embodied", "autonomous", "navigation",
        "manipulation", "robotic", "robot", "gui agent", "web agent",
        "tool use", "tool-use", "planning", "task-oriented",
    ],
    "Harness": [
        "benchmark", "harness", "evaluation", "eval", "survey",
        "assessment", "dataset",
    ],
    "Finance": [
        "finance", "financial", "trading", "stock", "market",
        "portfolio", "fraud", "cryptocurrency", "economic", "forecasting",
    ],
}

_ARXIV_RE = re.compile(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})', re.I)


def _title_matches_topics(title: str) -> bool:
    t = title.lower()
    return any(
        kw in t
        for kws in _TITLE_FILTERS.values()
        for kw in kws
    )


class CVFScraper:
    """Scrape CVPR proceedings from CVF OpenAccess."""

    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self.session.headers.update({
            "User-Agent": (
                "Mozilla/5.0 (compatible; paper-find-bot/1.0; "
                "+https://github.com/apple4ree/paper_find)"
            ),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
        })

    def fetch(self) -> List[Paper]:
        """Return CVPR papers matching Agent / Harness / Finance topics."""
        try:
            from bs4 import BeautifulSoup
        except ImportError:
            logger.error(
                "beautifulsoup4 not installed; skipping CVF scraper. "
                "Run: pip install beautifulsoup4"
            )
            return []

        all_papers: dict[str, Paper] = {}

        for year in CVF_VENUES:
            conf_name = f"CVPR{year}"
            url = f"{CVF_BASE}/{conf_name}?day=all"
            logger.info("CVF: fetching %s", url)

            try:
                resp = self.session.get(url, timeout=60)
                resp.raise_for_status()
            except Exception as exc:
                logger.error("CVF: failed to fetch %s: %s", url, exc)
                time.sleep(_DELAY)
                continue

            soup = BeautifulSoup(resp.text, "html.parser")
            entries = self._parse_paper_list(soup, year)
            logger.info("CVF: found %d entries in %s", len(entries), conf_name)

            # Filter by title keyword first (fast)
            matched = [e for e in entries if _title_matches_topics(e["title"])]
            logger.info(
                "CVF: %d papers pass title filter for %s", len(matched), conf_name
            )

            for entry in matched:
                pid = self._make_id(entry)
                if pid in all_papers:
                    continue

                # Try to get the abstract (from paper page or arXiv)
                abstract, arxiv_id = self._fetch_abstract(entry, BeautifulSoup)

                p = Paper(
                    title=entry["title"],
                    abstract=abstract,
                    authors=entry["authors"],
                    url=entry.get("arxiv_url") or entry.get("paper_url") or "",
                    arxiv_id=arxiv_id,
                    conference="CVPR",
                    year=year,
                    source="cvf",
                    published_date=date(year, 6, 1),  # CVPR is typically in June
                )
                all_papers[pid] = p
                time.sleep(_ABSTRACT_DELAY)

            time.sleep(_DELAY)

        logger.info("CVF: %d unique matching papers collected", len(all_papers))
        return list(all_papers.values())

    # ------------------------------------------------------------------
    # HTML parsing helpers
    # ------------------------------------------------------------------

    def _parse_paper_list(self, soup, year: int) -> list[dict]:
        """Extract paper entries from the CVF listing page."""
        entries = []

        # CVF uses <dt class="ptitle"> for titles and <dd> for authors/links
        for dt in soup.select("dt.ptitle"):
            a_tag = dt.find("a")
            if not a_tag:
                continue
            title = a_tag.get_text(strip=True)
            href = a_tag.get("href", "")
            paper_url = urljoin(CVF_BASE, href) if href else ""

            # Authors are in the immediately following <dd>
            authors: list[str] = []
            arxiv_url = ""
            arxiv_id: Optional[str] = None

            dd = dt.find_next_sibling("dd")
            if dd:
                # First <dd>: typically "Author1, Author2, ..."
                author_text = dd.get_text(separator=", ", strip=True)
                # Split and clean up
                authors = [n.strip() for n in re.split(r",\s*", author_text) if n.strip()]

                # Second <dd>: pdf / arXiv links
                dd2 = dd.find_next_sibling("dd")
                if dd2:
                    for a in dd2.find_all("a", href=True):
                        m = _ARXIV_RE.search(a["href"])
                        if m:
                            arxiv_id = m.group(1)
                            arxiv_url = f"https://arxiv.org/abs/{arxiv_id}"
                            break

            if title:
                entries.append(
                    {
                        "title": title,
                        "authors": authors,
                        "paper_url": paper_url,
                        "arxiv_url": arxiv_url,
                        "arxiv_id": arxiv_id,
                    }
                )
        return entries

    def _fetch_abstract(
        self, entry: dict, BeautifulSoup
    ) -> tuple[str, Optional[str]]:
        """Return (abstract, arxiv_id) for a paper entry."""
        arxiv_id = entry.get("arxiv_id")

        # If we have an arXiv ID, fetch abstract from arXiv (more reliable)
        if arxiv_id:
            try:
                resp = self.session.get(
                    f"https://arxiv.org/abs/{arxiv_id}", timeout=30
                )
                resp.raise_for_status()
                soup = BeautifulSoup(resp.text, "html.parser")
                blockquote = soup.select_one("blockquote.abstract")
                if blockquote:
                    # Remove the "Abstract:" label span
                    for span in blockquote.find_all("span", class_="descriptor"):
                        span.decompose()
                    return blockquote.get_text(strip=True), arxiv_id
            except Exception as exc:
                logger.debug("CVF: arXiv abstract fetch failed (%s): %s", arxiv_id, exc)

        # Fall back to CVF paper page
        paper_url = entry.get("paper_url")
        if paper_url:
            try:
                resp = self.session.get(paper_url, timeout=30)
                resp.raise_for_status()
                soup = BeautifulSoup(resp.text, "html.parser")
                # CVF paper pages have <div id="abstract">
                div = soup.select_one("#abstract") or soup.select_one(".abstract")
                if div:
                    return div.get_text(strip=True), arxiv_id
            except Exception as exc:
                logger.debug("CVF: paper page abstract fetch failed (%s): %s", paper_url, exc)

        return "", arxiv_id

    @staticmethod
    def _make_id(entry: dict) -> str:
        arxiv_id = entry.get("arxiv_id")
        if arxiv_id:
            base = arxiv_id.split("v")[0]
            return f"arxiv:{base}"
        normalized = " ".join(entry["title"].lower().split())
        return f"title:{normalized}"
