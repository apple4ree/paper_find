"""
CVF Open Access scraper for CVPR papers.

Fetches the full paper listing from openaccess.thecvf.com and filters by
topic keywords found in the title.  CVF listing pages do not expose
abstracts, so the abstract field is left empty; papers that also appear on
arXiv will have their abstract filled in during deduplication.

Page URL format: https://openaccess.thecvf.com/CVPR{year}?day=all
"""
from __future__ import annotations

import logging
import re
import time
from datetime import date
from typing import Dict, List, Optional

import requests
from bs4 import BeautifulSoup

from ..config import TOPICS
from ..models import Paper

logger = logging.getLogger(__name__)

CVF_BASE = "https://openaccess.thecvf.com"
_DELAY = 3.0  # seconds between page fetches — be polite to CVF
_ARXIV_RE = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", re.IGNORECASE)

# Conferences hosted on CVF open access.  Extend with "ICCV", "WACV" etc. if needed.
CVF_CONF_NAMES: List[str] = ["CVPR"]


class CVFScraper:
    """Scrapes CVF Open Access for conference paper listings."""

    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": "paper-find-bot/1.0"})

    def fetch(self, target_date: date) -> List[Paper]:
        """Return CVPR papers (current + previous year) matching topic keywords."""
        current_year = target_date.year
        seen: Dict[str, Paper] = {}

        for conf in CVF_CONF_NAMES:
            for year in [current_year, current_year - 1]:
                url = f"{CVF_BASE}/{conf}{year}?day=all"
                try:
                    batch = self._fetch_listing(url, conf, year)
                    added = sum(
                        1 for p in batch
                        if p.get_id() not in seen
                        or not seen.update({p.get_id(): p})  # type: ignore[func-returns-value]
                    )
                    for p in batch:
                        pid = p.get_id()
                        if pid not in seen:
                            seen[pid] = p
                    logger.info(
                        "CVF %s %d: %d topic-matched papers (%d new)",
                        conf, year, len(batch), added,
                    )
                except requests.exceptions.HTTPError as exc:
                    if exc.response is not None and exc.response.status_code == 404:
                        logger.info("CVF %s %d: not yet published (404)", conf, year)
                    else:
                        logger.warning("CVF %s %d: HTTP error — %s", conf, year, exc)
                except Exception as exc:
                    logger.warning("CVF %s %d: fetch failed — %s", conf, year, exc)

                time.sleep(_DELAY)

        return list(seen.values())

    def _fetch_listing(self, url: str, conf: str, year: int) -> List[Paper]:
        resp = self.session.get(url, timeout=120)
        resp.raise_for_status()
        return _parse_cvf_page(resp.text, conf, year)


# ---------------------------------------------------------------------------
# HTML parsing
# ---------------------------------------------------------------------------

def _topic_matches(title: str) -> bool:
    """Return True if the title contains at least one topic keyword."""
    title_lower = title.lower()
    return any(
        kw.lower() in title_lower
        for keywords in TOPICS.values()
        for kw in keywords
    )


def _parse_cvf_page(html: str, conf: str, year: int) -> List[Paper]:
    soup = BeautifulSoup(html, "html.parser")
    papers: List[Paper] = []

    for dt in soup.find_all("dt", class_="ptitle"):
        a_tag = dt.find("a")
        if not a_tag:
            continue

        title = a_tag.get_text(strip=True)
        if not title or not _topic_matches(title):
            continue

        # Collect the <dd> siblings that immediately follow this <dt>
        dds: List = []
        node = dt.next_sibling
        while node is not None:
            if hasattr(node, "name"):
                if node.name == "dd":
                    dds.append(node)
                elif node.name in ("dt", "h2", "h3"):
                    break
            node = node.next_sibling

        # --- Authors ---
        # First <dd> contains a bibtex <form> then the author string.
        authors: List[str] = []
        if dds:
            author_dd = BeautifulSoup(str(dds[0]), "html.parser")
            for form in author_dd.find_all("form"):
                form.decompose()
            raw = author_dd.get_text(separator=",", strip=True)
            authors = [a.strip() for a in raw.split(",") if a.strip()]

        # --- arXiv ID ---
        # Second (and sometimes third) <dd> contains pdf / supp / arXiv links.
        arxiv_id: Optional[str] = None
        for dd in dds[1:]:
            for a in dd.find_all("a", href=True):
                m = _ARXIV_RE.search(a["href"])
                if m:
                    arxiv_id = m.group(1)
                    break
            if arxiv_id:
                break

        # Build URL — prefer arXiv, fall back to CVF paper page
        if arxiv_id:
            url = f"https://arxiv.org/abs/{arxiv_id}"
        else:
            paper_href = a_tag.get("href", "")
            url = (
                f"{CVF_BASE}{paper_href}"
                if paper_href.startswith("/")
                else paper_href
            )

        papers.append(
            Paper(
                title=title,
                abstract="",  # CVF listing pages do not show abstracts
                authors=authors,
                url=url,
                arxiv_id=arxiv_id,
                conference=conf,
                year=year,
                source="cvf",
                published_date=None,
            )
        )

    logger.debug("CVF %s %d raw page: parsed %d matching papers", conf, year, len(papers))
    return papers
