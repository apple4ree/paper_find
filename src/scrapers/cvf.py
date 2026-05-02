"""
CVF Open Access scraper for CVPR papers.

Fetches accepted paper listings from openaccess.thecvf.com and filters
by topic keywords.  Tries the current year first, then falls back to
the previous year so that the most recent CVPR proceedings are always
included.

CVF page structure (simplified):
  <dt class="ptitle"><a href="/content/CVPR{year}/html/...">Title</a></dt>
  <dd>Author1, Author2, ...</dd>
  <dd>
    <a href=".../paper.pdf">pdf</a>
    | <a href="https://arxiv.org/abs/XXXX.XXXXX">arXiv</a>
  </dd>
"""
from __future__ import annotations

import logging
import re
import time
from datetime import date
from typing import List, Optional, Dict

import requests

try:
    from bs4 import BeautifulSoup
    _BS4_OK = True
except ImportError:
    _BS4_OK = False

from ..models import Paper

logger = logging.getLogger(__name__)

CVF_BASE = "https://openaccess.thecvf.com"
_DELAY = 0.5
_ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})")

# Keywords per topic for title-based pre-filtering (lowercase)
CVF_KEYWORDS: Dict[str, List[str]] = {
    "Agent": [
        "agent", "agentic", "embodied", "navigation", "manipulation",
        "autonomous", "multi-agent", "multiagent", "tool use", "tool-use",
        "gui agent", "web agent", "language-guided", "instruction following",
        "instruction-following", "robot", "planning", "reasoning agent",
        "vision-language agent", "vlm agent", "action",
    ],
    "Harness": [
        "benchmark", "evaluation", "harness", "dataset", "assessment",
        "metric", "survey", "framework", "leaderboard", "test suite",
    ],
    "Finance": [
        "financial", "finance", "trading", "stock", "portfolio",
        "fraud", "cryptocurrency", "market", "invoice", "receipt",
        "document understanding", "chart understanding",
    ],
}

# Conferences hosted on CVF
CVF_CONFERENCES = ["CVPR", "ICCV", "ECCV", "WACV"]


class CVFScraper:
    """Scrape CVF Open Access proceedings for topic-relevant papers."""

    def __init__(self, session: Optional[requests.Session] = None):
        if not _BS4_OK:
            raise ImportError(
                "beautifulsoup4 is required for CVFScraper: pip install beautifulsoup4"
            )
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": "paper-find-bot/1.0"})

    def fetch(self, conferences: Optional[List[str]] = None, years: Optional[List[int]] = None) -> List[Paper]:
        """Return CVF papers matching topic keywords.

        Args:
            conferences: list of conferences to scrape (default: ["CVPR"])
            years: list of years to try (default: [current_year, current_year-1])
        """
        if conferences is None:
            conferences = ["CVPR"]
        if years is None:
            cur = date.today().year
            years = [cur, cur - 1]

        seen: Dict[str, Paper] = {}

        for conf in conferences:
            for year in years:
                try:
                    batch = self._fetch_conference(conf, year)
                    new_count = 0
                    for p in batch:
                        pid = p.get_id()
                        if pid not in seen:
                            seen[pid] = p
                            new_count += 1
                    logger.info("CVF [%s %s]: %d papers (%d new)", conf, year, len(batch), new_count)
                except Exception as exc:
                    logger.warning("CVF [%s %s]: %s", conf, year, exc)
                time.sleep(_DELAY)

        logger.info("CVF total: %d unique papers", len(seen))
        return list(seen.values())

    # ------------------------------------------------------------------

    def _fetch_conference(self, conf: str, year: int) -> List[Paper]:
        url = f"{CVF_BASE}/{conf}{year}?day=all"
        try:
            resp = self.session.get(url, timeout=60)
            resp.raise_for_status()
        except requests.exceptions.HTTPError as exc:
            if exc.response is not None and exc.response.status_code == 404:
                logger.debug("CVF [%s %s]: 404 (proceedings not yet available)", conf, year)
                return []
            raise
        except Exception as exc:
            logger.error("CVF [%s %s] fetch error: %s", conf, year, exc)
            return []

        return self._parse_html(resp.text, conf, year)

    def _parse_html(self, html: str, conf: str, year: int) -> List[Paper]:
        soup = BeautifulSoup(html, "html.parser")
        papers: List[Paper] = []

        # CVF lists papers as <dt class="ptitle"> / <dd> pairs inside <dl>
        for dt in soup.find_all("dt", class_="ptitle"):
            title_tag = dt.find("a")
            if not title_tag:
                continue
            title = title_tag.get_text(strip=True)

            if not _matches_any_topic(title):
                continue

            paper_path = title_tag.get("href", "")
            full_url = f"{CVF_BASE}{paper_path}" if paper_path.startswith("/") else paper_path

            # Authors and links are in subsequent <dd> siblings
            authors: List[str] = []
            arxiv_id: Optional[str] = None
            pdf_url = ""

            sibling = dt.find_next_sibling()
            while sibling and sibling.name == "dd":
                text = sibling.get_text(separator=" ", strip=True)

                # First <dd> usually contains author names (comma-separated, no links or few)
                if not authors and not sibling.find("a", href=re.compile(r"arxiv|\.pdf")):
                    raw = text.strip().rstrip(";")
                    if raw and len(raw) < 500:
                        authors = [a.strip() for a in raw.split(",") if a.strip()]

                # Look for arXiv link
                for a_tag in sibling.find_all("a", href=True):
                    href = a_tag["href"]
                    m = _ARXIV_RE.search(href)
                    if m:
                        arxiv_id = m.group(1)
                    if href.endswith(".pdf"):
                        pdf_url = href if href.startswith("http") else f"{CVF_BASE}{href}"

                sibling = sibling.find_next_sibling()

            # Build final URL
            if arxiv_id:
                url = f"https://arxiv.org/abs/{arxiv_id}"
            elif pdf_url:
                url = pdf_url
            else:
                url = full_url

            papers.append(Paper(
                title=title,
                abstract="",
                authors=authors,
                url=url,
                arxiv_id=arxiv_id,
                conference=conf,
                year=year,
                source="cvf",
                published_date=None,
            ))

        return papers


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _matches_any_topic(title: str) -> bool:
    """Return True if the title matches any topic keyword."""
    lower = title.lower()
    for keywords in CVF_KEYWORDS.values():
        if any(kw in lower for kw in keywords):
            return True
    return False
