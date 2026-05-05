"""
CVF (Computer Vision Foundation) Open Access scraper for CVPR papers.

CVPR, ICCV, and ECCV proceedings are published open-access at:
  https://openaccess.thecvf.com/CVPR{year}.py

Each conference year page contains a full list of accepted papers with
titles, authors, and abstracts.  We fetch the HTML, parse the paper
entries, then filter by topic keywords.

Conference pages tried (current year first):
  CVPR {year}, CVPR {year-1}
"""
from __future__ import annotations

import logging
import re
import time
from datetime import date
from typing import Dict, List, Optional

import requests
from html.parser import HTMLParser

from ..config import TOPICS
from ..models import Paper

logger = logging.getLogger(__name__)

CVF_BASE = "https://openaccess.thecvf.com"
_CUR_YEAR = date.today().year

# Conferences hosted on CVF that we want to scrape
CVF_CONFERENCES = {
    "CVPR": [f"CVPR{_CUR_YEAR}", f"CVPR{_CUR_YEAR - 1}"],
}

# Topic keyword sets (title + abstract matching)
_TOPIC_KWS: Dict[str, List[str]] = {
    topic: [kw.lower() for kw in kws]
    for topic, kws in TOPICS.items()
}

_DELAY = 2.0  # seconds between requests


# ---------------------------------------------------------------------------
# HTML parser for CVF paper listings
# ---------------------------------------------------------------------------

class _CVFParser(HTMLParser):
    """Pull paper records from the CVF open-access HTML page.

    Each paper is wrapped in a <dt class="ptitle"> (title) followed by
    <dd> blocks containing authors and an abstract.

    The page structure (simplified):

      <dt class="ptitle">
        <a href="/content/CVPR2025/html/...">Paper Title</a>
      </dt>
      <dd>
        <form>  ... author list ...  </form>
        <div class="abstract">Abstract text...</div>
      </dd>
    """

    def __init__(self) -> None:
        super().__init__()
        self.papers: List[Dict] = []
        self._in_ptitle = False
        self._in_abstract = False
        self._in_author_form = False
        self._cur: Optional[Dict] = None
        self._buf = ""

    def handle_starttag(self, tag: str, attrs) -> None:
        attr = dict(attrs)
        if tag == "dt" and "ptitle" in attr.get("class", ""):
            self._cur = {"title": "", "url": "", "authors": [], "abstract": ""}
            self._in_ptitle = True
        elif self._in_ptitle and tag == "a":
            href = attr.get("href", "")
            if href and self._cur is not None:
                self._cur["url"] = CVF_BASE + href if href.startswith("/") else href
        elif tag == "div" and "abstract" in attr.get("class", ""):
            self._in_abstract = True
            self._buf = ""
        elif tag == "form" and self._cur is not None and not self._in_abstract:
            self._in_author_form = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "dt" and self._in_ptitle:
            self._in_ptitle = False
        elif tag == "div" and self._in_abstract:
            self._in_abstract = False
            if self._cur is not None:
                self._cur["abstract"] = self._buf.strip()
        elif tag == "form" and self._in_author_form:
            self._in_author_form = False
        elif tag == "dd" and self._cur is not None and self._cur.get("title"):
            self.papers.append(self._cur)
            self._cur = None

    def handle_data(self, data: str) -> None:
        text = data.strip()
        if not text:
            return
        if self._in_ptitle and self._cur is not None and not self._cur["title"]:
            self._cur["title"] = text
        elif self._in_abstract:
            self._buf += " " + text
        elif self._in_author_form and self._cur is not None:
            # Author names appear as plain text nodes inside the form
            if "," not in text and len(text) < 60:
                self._cur["authors"].append(text)


# ---------------------------------------------------------------------------
# ArXiv ID extractor (from paper detail pages)
# ---------------------------------------------------------------------------

_ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", re.I)


def _extract_arxiv_id(text: str) -> Optional[str]:
    m = _ARXIV_RE.search(text)
    return m.group(1) if m else None


# ---------------------------------------------------------------------------
# Scraper class
# ---------------------------------------------------------------------------

class CVFScraper:
    """Scrape CVF open-access proceedings and filter by topic keywords."""

    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self.session.headers.update({
            "User-Agent": "paper-find-bot/1.0",
            "Accept": "text/html,application/xhtml+xml",
        })

    def fetch(self) -> List[Paper]:
        """Return CVPR papers that match Agent / Harness / Finance topics."""
        all_papers: Dict[str, Paper] = {}

        for conf_name, page_ids in CVF_CONFERENCES.items():
            for page_id in page_ids:
                year = int(re.search(r"\d{4}", page_id).group())
                try:
                    raw = self._fetch_page(page_id)
                    filtered = self._filter_by_topic(raw, conf_name, year)
                    new = 0
                    for p in filtered:
                        pid = p.get_id()
                        if pid not in all_papers:
                            all_papers[pid] = p
                            new += 1
                    logger.info(
                        "CVF [%s %d]: %d matching / %d new",
                        conf_name, year, len(filtered), new,
                    )
                except Exception as exc:
                    logger.warning("CVF [%s %d]: %s", conf_name, year, exc)
                time.sleep(_DELAY)

        return list(all_papers.values())

    # ------------------------------------------------------------------

    def _fetch_page(self, page_id: str) -> List[Dict]:
        url = f"{CVF_BASE}/{page_id}.py"
        resp = self.session.get(url, timeout=60)
        resp.raise_for_status()

        parser = _CVFParser()
        parser.feed(resp.text)
        logger.debug("CVF %s: parsed %d papers from HTML", page_id, len(parser.papers))
        return parser.papers

    def _filter_by_topic(
        self, raw: List[Dict], conf_name: str, year: int
    ) -> List[Paper]:
        results: List[Paper] = []
        for item in raw:
            title = (item.get("title") or "").strip()
            abstract = (item.get("abstract") or "").strip()
            if not title:
                continue
            combined = f"{title} {abstract}".lower()
            if not any(
                kw in combined
                for kws in _TOPIC_KWS.values()
                for kw in kws
            ):
                continue

            arxiv_id = _extract_arxiv_id(item.get("url", "") + " " + abstract)
            url = item.get("url", "")
            if arxiv_id:
                url = f"https://arxiv.org/abs/{arxiv_id}"

            authors = [a for a in item.get("authors", []) if a]

            results.append(Paper(
                title=title,
                abstract=abstract,
                authors=authors,
                url=url,
                arxiv_id=arxiv_id,
                conference=conf_name,
                year=year,
                source="cvf",
                published_date=date(year, 6, 1),  # CVPR is held in June
            ))
        return results
