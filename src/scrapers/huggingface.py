"""
HuggingFace Daily Papers scraper.

Three fetch modes (tried in order, stopping at first success):
  1. Daily API     — https://huggingface.co/api/daily_papers?date=YYYY-MM-DD
  2. HTML scrape   — https://huggingface.co/papers?date=YYYY-MM-DD
     Parses arxiv IDs from page links; falls back to today's page if the
     date-specific URL contains no papers.
  3. Topic search  — https://huggingface.co/api/papers?q=<query>
     Supplements the curated list with topic-relevant papers.
"""
from __future__ import annotations

import json
import logging
import re
import time
from datetime import date, timedelta
from typing import List, Optional

import requests

from ..config import TOPICS
from ..models import Paper

logger = logging.getLogger(__name__)

HF_DAILY_API = "https://huggingface.co/api/daily_papers"
HF_SEARCH_API = "https://huggingface.co/api/papers"
HF_PAPERS_PAGE = "https://huggingface.co/papers"

MAX_FALLBACK_DAYS = 3
SEARCH_DELAY = 1.5
SEARCH_LIMIT = 50

# Realistic browser headers that prevent most CDN-level 403 blocks
_BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/html, */*;q=0.9",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://huggingface.co/",
    "DNT": "1",
}

# Representative search terms per topic for the HuggingFace search API
HF_TOPIC_QUERIES: dict[str, list[str]] = {
    "Agent": ["llm agent", "autonomous agent", "multi-agent", "agentic"],
    "Harness": ["evaluation harness", "lm eval", "llm benchmark"],
    "Finance": [
        "financial llm",
        "stock prediction",
        "portfolio optimization",
        "algorithmic trading",
    ],
}

# Regex to pull bare arXiv IDs from an HF papers page
_ARXIV_HREF_RE = re.compile(r"/papers/([\d]{4}\.\d{4,5}(?:v\d+)?)")
# JSON blobs embedded in the page that carry paper data
_SCRIPT_JSON_RE = re.compile(
    r'<script[^>]+type=["\']application/json["\'][^>]*>(.*?)</script>',
    re.DOTALL,
)


class HuggingFaceScraper:
    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self.session.headers.update(_BROWSER_HEADERS)

    def fetch(self, target_date: date) -> List[Paper]:
        """Return HuggingFace papers for *target_date*.

        Combines the daily curated list with topic-based search results.
        """
        all_papers: dict[str, Paper] = {}

        # --- 1. Daily curated papers ---
        daily = self._fetch_daily(target_date)
        for p in daily:
            all_papers[p.get_id()] = p
        logger.info("HuggingFace daily: %d papers", len(daily))

        # --- 2. Topic search papers ---
        search_papers = self._fetch_by_topics()
        new_count = 0
        for p in search_papers:
            pid = p.get_id()
            if pid not in all_papers:
                all_papers[pid] = p
                new_count += 1
        logger.info("HuggingFace search: %d additional papers", new_count)

        return list(all_papers.values())

    # ------------------------------------------------------------------
    # Daily curated list
    # ------------------------------------------------------------------

    def _fetch_daily(self, target_date: date) -> List[Paper]:
        """Fetch curated papers, falling back to recent days and HTML scraping."""
        for offset in range(MAX_FALLBACK_DAYS + 1):
            d = target_date - timedelta(days=offset)
            papers = self._fetch_date_api(d) or self._fetch_date_html(d)
            if papers:
                if offset:
                    logger.info(
                        "HuggingFace: no papers for %s, using %s instead",
                        target_date,
                        d,
                    )
                return papers
        logger.warning(
            "HuggingFace: no curated papers found in the last %d days",
            MAX_FALLBACK_DAYS,
        )
        return []

    def _fetch_date_api(self, d: date) -> List[Paper]:
        """Try the JSON API endpoint."""
        try:
            resp = self.session.get(
                HF_DAILY_API,
                params={"date": str(d)},
                timeout=30,
            )
            resp.raise_for_status()
            data = resp.json()
            if not data:
                return []
        except Exception as exc:
            logger.debug("HuggingFace API failed (%s): %s", d, exc)
            return []

        return [p for p in (_parse_item(item, "huggingface") for item in data) if p]

    def _fetch_date_html(self, d: date) -> List[Paper]:
        """Fallback: scrape the HuggingFace papers HTML page for arxiv IDs."""
        url = HF_PAPERS_PAGE
        params: dict = {}
        if str(d) != str(date.today()):
            params["date"] = str(d)

        try:
            resp = self.session.get(url, params=params, timeout=30)
            resp.raise_for_status()
            html = resp.text
        except Exception as exc:
            logger.debug("HuggingFace HTML failed (%s): %s", d, exc)
            return []

        papers: List[Paper] = []
        seen_ids: set[str] = set()

        # Strategy A: pull structured JSON from embedded <script> tags
        for m in _SCRIPT_JSON_RE.finditer(html):
            try:
                blob = json.loads(m.group(1))
                extracted = _extract_papers_from_blob(blob, d)
                for p in extracted:
                    if p.get_id() not in seen_ids:
                        seen_ids.add(p.get_id())
                        papers.append(p)
            except (json.JSONDecodeError, Exception):
                pass

        # Strategy B: collect bare arXiv IDs from href attributes
        for arxiv_id_raw in _ARXIV_HREF_RE.findall(html):
            arxiv_id = arxiv_id_raw.split("v")[0]
            key = f"arxiv:{arxiv_id}"
            if key not in seen_ids:
                seen_ids.add(key)
                papers.append(
                    Paper(
                        title=arxiv_id,
                        url=f"https://arxiv.org/abs/{arxiv_id}",
                        arxiv_id=arxiv_id,
                        source="huggingface",
                        published_date=d,
                    )
                )

        return papers

    # ------------------------------------------------------------------
    # Topic-based search
    # ------------------------------------------------------------------

    def _fetch_by_topics(self) -> List[Paper]:
        """Search HuggingFace paper database by topic keywords."""
        results: List[Paper] = []
        seen_ids: set[str] = set()

        for topic, queries in HF_TOPIC_QUERIES.items():
            for query in queries:
                try:
                    batch = self._search_query(query)
                    for p in batch:
                        pid = p.get_id()
                        if pid not in seen_ids:
                            seen_ids.add(pid)
                            results.append(p)
                except Exception as exc:
                    logger.error(
                        "HuggingFace search error [%s / %s]: %s", topic, query, exc
                    )
                time.sleep(SEARCH_DELAY)

        return results

    def _search_query(self, query: str) -> List[Paper]:
        resp = self.session.get(
            HF_SEARCH_API,
            params={"q": query, "limit": SEARCH_LIMIT},
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()

        if isinstance(data, list):
            items = data
        elif isinstance(data, dict):
            items = data.get("papers") or data.get("data") or []
        else:
            return []

        return [p for p in (_parse_item(item, "huggingface_search") for item in items) if p]


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def _parse_item(item: dict, source: str = "huggingface") -> Optional[Paper]:
    pd = item.get("paper") or item

    title = (pd.get("title") or "").strip()
    if not title:
        return None

    arxiv_id = (pd.get("id") or "").replace("arxiv:", "").strip() or None

    authors: List[str] = []
    for a in pd.get("authors") or []:
        if isinstance(a, dict):
            name = a.get("name") or a.get("fullname") or ""
        else:
            name = str(a)
        if name:
            authors.append(name)

    abstract = (pd.get("abstract") or "").strip()

    url = ""
    if arxiv_id:
        url = f"https://arxiv.org/abs/{arxiv_id}"
    elif pd.get("url"):
        url = pd["url"]

    pub_date: Optional[date] = None
    for key in ("publishedAt", "published_at", "publicationDate"):
        raw = pd.get(key) or item.get(key)
        if raw:
            try:
                pub_date = date.fromisoformat(str(raw)[:10])
                break
            except ValueError:
                pass

    return Paper(
        title=title,
        abstract=abstract,
        authors=authors,
        url=url,
        arxiv_id=arxiv_id,
        source=source,
        published_date=pub_date,
    )


def _extract_papers_from_blob(blob, fallback_date: date) -> List[Paper]:
    """Try to pull Paper objects from an arbitrary JSON blob embedded in HF pages."""
    papers: List[Paper] = []

    def _walk(obj):
        if isinstance(obj, dict):
            title = obj.get("title") or ""
            arxiv_id = (obj.get("id") or obj.get("arxivId") or "").replace("arxiv:", "").strip()
            if title and len(title) > 10:
                p = Paper(
                    title=title.strip(),
                    abstract=(obj.get("abstract") or "").strip(),
                    url=f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else obj.get("url", ""),
                    arxiv_id=arxiv_id or None,
                    source="huggingface",
                    published_date=fallback_date,
                )
                papers.append(p)
            else:
                for v in obj.values():
                    _walk(v)
        elif isinstance(obj, list):
            for item in obj:
                _walk(item)

    _walk(blob)
    return papers
