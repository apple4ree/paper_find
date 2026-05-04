"""
CVF Open Access scraper for CVPR papers.

Fetches the proceedings index from openaccess.thecvf.com and filters
papers whose titles contain any of the configured topic keywords.

For keyword-matching papers, the abstract page is fetched to get the
arXiv ID (if any) and the abstract text so topic-matching works on the
full abstract during the processing step.

Rate limiting: 2 s between per-paper detail fetches.
"""
from __future__ import annotations

import logging
import re
import time
from datetime import date
from html.parser import HTMLParser
from typing import List, Optional

import requests

from ..config import TOPICS
from ..models import Paper

logger = logging.getLogger(__name__)

CVF_BASE = "https://openaccess.thecvf.com"
_DETAIL_DELAY = 2.0   # seconds between detail-page fetches
_INDEX_TIMEOUT = 90   # seconds for the (large) proceedings index

_CUR_YEAR = date.today().year
CVPR_YEARS = [_CUR_YEAR, _CUR_YEAR - 1]

# Flat list of all topic keywords (lowercase) for fast title matching
_ALL_KWS: list[str] = sorted(
    {kw.lower() for kws in TOPICS.values() for kw in kws},
    key=len,
    reverse=True,  # match longer strings first
)

_ARXIV_RE = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", re.IGNORECASE)
_AUTHOR_RE = re.compile(r"<i>(.*?)</i>", re.DOTALL)
_ABSTRACT_RE = re.compile(r'<div[^>]*id=["\']abstract["\'][^>]*>(.*?)</div>', re.DOTALL | re.IGNORECASE)


class _CVFIndexParser(HTMLParser):
    """Parse CVF Open Access proceedings index page.

    Extracts ``(href, title)`` pairs from:
        <dt class="ptitle"><a href="/content/…">Title text</a></dt>
    """

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.entries: list[tuple[str, str]] = []
        self._in_ptitle = False
        self._href = ""
        self._buf: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        d = dict(attrs)
        if tag == "dt" and "ptitle" in (d.get("class") or ""):
            self._in_ptitle = True
        elif tag == "a" and self._in_ptitle:
            self._href = d.get("href") or ""
            self._buf = []

    def handle_data(self, data: str) -> None:
        if self._in_ptitle and self._href:
            self._buf.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._in_ptitle and self._href:
            title = "".join(self._buf).strip()
            if title and self._href:
                self.entries.append((self._href, title))
            self._href = ""
            self._buf = []
        elif tag == "dt" and self._in_ptitle:
            self._in_ptitle = False


class CVFScraper:
    """Scrape CVPR proceedings from the CVF Open Access portal."""

    def __init__(self, session: Optional[requests.Session] = None) -> None:
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": "paper-find-bot/1.0"})

    def fetch(self) -> List[Paper]:
        seen: dict[str, Paper] = {}
        for year in CVPR_YEARS:
            for p in self._fetch_year(year):
                pid = p.get_id()
                if pid not in seen:
                    seen[pid] = p
        logger.info("CVF: %d CVPR papers matched topics", len(seen))
        return list(seen.values())

    # ------------------------------------------------------------------

    def _fetch_year(self, year: int) -> List[Paper]:
        url = f"{CVF_BASE}/CVPR{year}?day=all"
        try:
            resp = self.session.get(url, timeout=_INDEX_TIMEOUT)
            if resp.status_code == 404:
                logger.debug("CVF: CVPR%d proceedings not yet available", year)
                return []
            resp.raise_for_status()
        except Exception as exc:
            logger.error("CVF: CVPR%d index fetch failed: %s", year, exc)
            return []

        parser = _CVFIndexParser()
        try:
            parser.feed(resp.text)
        except Exception as exc:
            logger.error("CVF: CVPR%d HTML parse error: %s", year, exc)
            return []

        logger.info("CVF: CVPR%d index → %d total papers", year, len(parser.entries))

        papers: List[Paper] = []
        for href, title in parser.entries:
            if not _title_matches(title):
                continue
            detail_url = (CVF_BASE + href) if href.startswith("/") else href
            p = self._fetch_detail(title, detail_url, year)
            papers.append(p)
            time.sleep(_DETAIL_DELAY)

        logger.info("CVF: CVPR%d → %d topic-matched papers", year, len(papers))
        return papers

    def _fetch_detail(self, title: str, detail_url: str, year: int) -> Paper:
        """Fetch abstract page to extract arXiv ID, authors, and abstract."""
        arxiv_id: Optional[str] = None
        abstract = ""
        authors: list[str] = []

        try:
            resp = self.session.get(detail_url, timeout=30)
            if resp.status_code == 200:
                html = resp.text
                # arXiv ID
                m = _ARXIV_RE.search(html)
                if m:
                    arxiv_id = m.group(1)
                # Abstract
                ma = _ABSTRACT_RE.search(html)
                if ma:
                    raw = re.sub(r"<[^>]+>", " ", ma.group(1)).strip()
                    abstract = re.sub(r"\s+", " ", raw)
                # Authors: look for <i> tag that precedes the author list
                mi = _AUTHOR_RE.search(html)
                if mi:
                    raw_authors = mi.group(1)
                    raw_authors = re.sub(r"<[^>]+>", "", raw_authors)
                    authors = [a.strip() for a in raw_authors.split(",") if a.strip()]
        except Exception as exc:
            logger.debug("CVF: detail fetch failed (%s): %s", detail_url, exc)

        url = f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else detail_url

        return Paper(
            title=title,
            abstract=abstract,
            authors=authors,
            url=url,
            arxiv_id=arxiv_id,
            conference="CVPR",
            year=year,
            source="cvf",
        )


def _title_matches(title: str) -> bool:
    tl = title.lower()
    return any(kw in tl for kw in _ALL_KWS)
