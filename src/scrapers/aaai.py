"""
AAAI Digital Library scraper.

Uses the AAAI OJS (Open Journal Systems) search API to find papers
from AAAI proceedings matching Agent / Harness / Finance topics.

Endpoint: https://ojs.aaai.org/index.php/AAAI/search/search
Supports keyword search with JSON-friendly URL params.
"""
from __future__ import annotations

import logging
import re
import time
from datetime import date
from typing import Dict, List, Optional

import requests

from ..config import TOPICS
from ..models import Paper

logger = logging.getLogger(__name__)

_BASE = "https://ojs.aaai.org"
_SEARCH_URL = f"{_BASE}/index.php/AAAI/search/search"
_DELAY = 2.0
_CUR_YEAR = date.today().year

_ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})")

# Representative queries per topic for AAAI search
TOPIC_QUERIES: Dict[str, List[str]] = {
    "Agent": [
        "llm agent",
        "autonomous agent",
        "multi-agent",
        "agentic",
        "tool use language model",
    ],
    "Harness": [
        "evaluation harness",
        "benchmark language model",
        "llm evaluation",
        "evaluation framework",
    ],
    "Finance": [
        "financial language model",
        "stock prediction",
        "portfolio optimization",
        "fraud detection",
        "algorithmic trading",
    ],
}


class AAAIScraper:
    """Search AAAI Digital Library for relevant papers."""

    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": "paper-find-bot/1.0"})

    def fetch(self) -> List[Paper]:
        seen: Dict[str, Paper] = {}

        for topic, queries in TOPIC_QUERIES.items():
            for query in queries:
                try:
                    batch = self._search(query)
                    new = 0
                    for p in batch:
                        pid = p.get_id()
                        if pid not in seen:
                            seen[pid] = p
                            new += 1
                    logger.debug("AAAI ['%s']: %d results (%d new)", query, len(batch), new)
                except Exception as exc:
                    logger.warning("AAAI search error ['%s']: %s", query, exc)
                time.sleep(_DELAY)

        logger.info("AAAI: %d unique papers collected", len(seen))
        return list(seen.values())

    def _search(self, query: str, limit: int = 50) -> List[Paper]:
        params = {
            "query": query,
            "searchField": "query",
            "dateFromYear": str(_CUR_YEAR - 1),
            "dateToYear": str(_CUR_YEAR),
        }
        resp = self.session.get(_SEARCH_URL, params=params, timeout=30)
        resp.raise_for_status()
        return _parse_aaai_html(resp.text)


# ---------------------------------------------------------------------------
# HTML parsing (stdlib re only)
# ---------------------------------------------------------------------------

_ARTICLE_RE = re.compile(
    r'<div[^>]+class="[^"]*obj_article_summary[^"]*"[^>]*>(.*?)</div>\s*</div>',
    re.DOTALL,
)
_TITLE_RE = re.compile(r'<h3[^>]*class="[^"]*title[^"]*"[^>]*>.*?<a[^>]*>(.*?)</a>', re.DOTALL)
_AUTHOR_RE = re.compile(r'<div[^>]*class="[^"]*authors[^"]*"[^>]*>(.*?)</div>', re.DOTALL)
_LINK_RE = re.compile(r'href="(https://ojs\.aaai\.org/[^"]+/view/[^"]+)"')
_YEAR_RE = re.compile(r"\b(20\d{2})\b")


def _parse_aaai_html(html: str) -> List[Paper]:
    papers: List[Paper] = []
    all_keywords = [kw.lower() for kws in TOPICS.values() for kw in kws]

    for block_m in _ARTICLE_RE.finditer(html):
        block = block_m.group(1)

        title_m = _TITLE_RE.search(block)
        if not title_m:
            continue
        title = re.sub(r"<[^>]+>", "", title_m.group(1)).strip()
        if not title:
            continue

        if not any(kw in title.lower() for kw in all_keywords):
            continue

        authors: List[str] = []
        auth_m = _AUTHOR_RE.search(block)
        if auth_m:
            raw = re.sub(r"<[^>]+>", "", auth_m.group(1))
            authors = [a.strip() for a in re.split(r"[,;]", raw) if a.strip()]

        url = ""
        link_m = _LINK_RE.search(block)
        if link_m:
            url = link_m.group(1)

        year: Optional[int] = None
        year_m = _YEAR_RE.search(url)
        if year_m:
            year = int(year_m.group(1))

        papers.append(
            Paper(
                title=title,
                authors=authors,
                url=url,
                conference="AAAI",
                year=year,
                source="aaai",
            )
        )

    return papers
