"""
HuggingFace Daily Papers scraper.

Three fetch modes (tried in order):
  1. Daily curated API  — https://huggingface.co/api/daily_papers?date=YYYY-MM-DD
     Returns ~20-50 papers HuggingFace editors highlight each day.
     Falls back to the most recent available day if the requested date has no data.

  2. Topic search API   — https://huggingface.co/api/papers?q=<query>
     Searches the full HuggingFace paper database by keyword.

  3. HTML fallback      — https://huggingface.co/papers
     Scraped directly when the JSON APIs return 403/rate-limit errors.
     Extracts paper arXiv IDs embedded in the page's Next.js JSON state.
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

MAX_FALLBACK_DAYS = 3   # Try up to N previous days if today has no papers
SEARCH_DELAY = 1.0       # Seconds between search requests
SEARCH_LIMIT = 50        # Papers per topic search query

# Representative search terms per topic for the HuggingFace search API
HF_TOPIC_QUERIES: dict[str, list[str]] = {
    "Agent": ["llm agent", "autonomous agent", "multi-agent", "agentic"],
    "Harness": ["evaluation harness", "lm eval", "llm benchmark"],
    "Finance": ["financial llm", "stock prediction", "portfolio optimization", "algorithmic trading"],
}

# Regex to extract Next.js embedded JSON from HF papers page
_NEXT_DATA_RE = re.compile(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', re.DOTALL)
# ArXiv IDs referenced anywhere in the page HTML
_ARXIV_ID_RE = re.compile(r'"id"\s*:\s*"(\d{4}\.\d{4,5})"')


class HuggingFaceScraper:
    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": "paper-find-bot/1.0"})

    def fetch(self, target_date: date) -> List[Paper]:
        """Return HuggingFace papers for *target_date*.

        Combines:
          1. Daily curated API list (with fallback for missing dates)
          2. Topic-based search via the HF papers API
          3. HTML page scraping when API calls return 403
        """
        all_papers: dict[str, Paper] = {}
        api_blocked = False

        # --- 1. Daily curated papers ---
        daily, api_blocked = self._fetch_daily(target_date)
        for p in daily:
            all_papers[p.get_id()] = p
        logger.info("HuggingFace daily: %d papers", len(daily))

        # --- 2. Topic search papers (skip if API is blocked) ---
        if not api_blocked:
            search_papers = self._fetch_by_topics()
            new_count = 0
            for p in search_papers:
                pid = p.get_id()
                if pid not in all_papers:
                    all_papers[pid] = p
                    new_count += 1
            logger.info("HuggingFace search: %d additional papers", new_count)

        # --- 3. HTML fallback when API is blocked ---
        if api_blocked:
            logger.info("HuggingFace: API blocked, trying HTML fallback")
            html_papers = self._fetch_html_fallback()
            new_count = 0
            for p in html_papers:
                pid = p.get_id()
                if pid not in all_papers:
                    all_papers[pid] = p
                    new_count += 1
            logger.info("HuggingFace HTML fallback: %d papers", new_count)

        return list(all_papers.values())

    # ------------------------------------------------------------------
    # Daily curated list
    # ------------------------------------------------------------------

    def _fetch_daily(self, target_date: date):
        """Fetch today's curated papers, with fallback to recent days.

        Returns (papers, api_blocked) where api_blocked=True means every
        attempt received a 403, signalling the caller to use HTML fallback.
        """
        blocked_count = 0
        for offset in range(MAX_FALLBACK_DAYS + 1):
            d = target_date - timedelta(days=offset)
            papers, was_blocked = self._fetch_date(d)
            if was_blocked:
                blocked_count += 1
                continue
            if papers:
                if offset:
                    logger.info(
                        "HuggingFace: no papers for %s, using %s instead",
                        target_date, d,
                    )
                return papers, False
        if blocked_count > 0:
            logger.warning("HuggingFace daily API blocked (403) — will try HTML fallback")
            return [], True
        logger.warning(
            "HuggingFace: no curated papers found in the last %d days",
            MAX_FALLBACK_DAYS,
        )
        return [], False

    def _fetch_date(self, d: date):
        """Fetch curated papers for a single date.

        Returns (papers, was_blocked).
        """
        try:
            resp = self.session.get(
                HF_DAILY_API, params={"date": str(d)}, timeout=30
            )
            if resp.status_code == 403:
                return [], True
            resp.raise_for_status()
            data = resp.json()
        except Exception as exc:
            logger.error("HuggingFace daily fetch error (%s): %s", d, exc)
            return [], False

        papers: List[Paper] = []
        for item in data:
            paper = self._parse_item(item, source="huggingface")
            if paper:
                papers.append(paper)
        return papers, False

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
        """Search HuggingFace papers by a single query string."""
        try:
            resp = self.session.get(
                HF_SEARCH_API,
                params={"q": query, "limit": SEARCH_LIMIT},
                timeout=30,
            )
            if resp.status_code == 403:
                return []
            resp.raise_for_status()
            data = resp.json()
        except Exception as exc:
            logger.error("HuggingFace search fetch error (%s): %s", query, exc)
            return []

        # The response may be a list or a dict with a "papers" key
        if isinstance(data, list):
            items = data
        elif isinstance(data, dict):
            items = data.get("papers") or data.get("data") or []
        else:
            return []

        papers: List[Paper] = []
        for item in items:
            p = self._parse_item(item, source="huggingface_search")
            if p:
                papers.append(p)
        return papers

    # ------------------------------------------------------------------
    # HTML fallback scraper
    # ------------------------------------------------------------------

    def _fetch_html_fallback(self) -> List[Paper]:
        """Scrape https://huggingface.co/papers when the JSON API is blocked.

        Extracts arXiv IDs embedded in the Next.js page state and resolves
        paper metadata from the HF paper detail API or arXiv.
        """
        try:
            resp = self.session.get(HF_PAPERS_PAGE, timeout=30)
            resp.raise_for_status()
            html = resp.text
        except Exception as exc:
            logger.error("HuggingFace HTML fallback error: %s", exc)
            return []

        arxiv_ids: list[str] = []

        # Strategy 1: extract from the __NEXT_DATA__ JSON blob
        m = _NEXT_DATA_RE.search(html)
        if m:
            try:
                data = json.loads(m.group(1))
                _collect_arxiv_ids(data, arxiv_ids)
            except Exception:
                pass

        # Strategy 2: find "arxiv.org/abs/XXXX.XXXXX" patterns in raw HTML
        if not arxiv_ids:
            arxiv_ids = re.findall(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})', html)

        # Strategy 3: find bare IDs in JSON-like snippets (e.g. "id":"2501.00001")
        if not arxiv_ids:
            arxiv_ids = _ARXIV_ID_RE.findall(html)

        seen: set[str] = set()
        papers: List[Paper] = []
        for aid in arxiv_ids:
            base_id = aid.split("v")[0]
            if base_id in seen:
                continue
            seen.add(base_id)

            # Minimal Paper object — no abstract since we'd need another call
            papers.append(
                Paper(
                    title=f"arXiv:{base_id}",  # will be enriched if S2 also finds it
                    abstract="",
                    url=f"https://arxiv.org/abs/{base_id}",
                    arxiv_id=base_id,
                    source="huggingface",
                )
            )

        logger.info(
            "HuggingFace HTML fallback: extracted %d arXiv IDs", len(papers)
        )
        return papers

    # ------------------------------------------------------------------
    # Shared parser
    # ------------------------------------------------------------------

    # (module-level helper _collect_arxiv_ids defined below the class)

    def _parse_item(self, item: dict, source: str = "huggingface") -> Optional[Paper]:
        pd = item.get("paper") or item  # some responses nest under "paper"

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


# ---------------------------------------------------------------------------
# Module-level helpers
# ---------------------------------------------------------------------------

def _collect_arxiv_ids(obj, out: list) -> None:
    """Recursively walk a parsed JSON object collecting arXiv paper IDs."""
    if isinstance(obj, dict):
        v = obj.get("id") or obj.get("arxivId") or ""
        if isinstance(v, str) and re.match(r"\d{4}\.\d{4,5}", v):
            out.append(v)
        for child in obj.values():
            _collect_arxiv_ids(child, out)
    elif isinstance(obj, list):
        for item in obj:
            _collect_arxiv_ids(item, out)
