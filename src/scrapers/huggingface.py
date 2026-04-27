"""
HuggingFace Daily Papers scraper.

Three fetch modes (in priority order):
  1. Daily curated list  — https://huggingface.co/api/daily_papers?date=YYYY-MM-DD
     Returns the ~20-50 papers HuggingFace editors highlight each day.
     Falls back to the most recent available day if the requested date has no data.

  2. Topic search        — https://huggingface.co/api/papers?q=<query>
     Searches the full HuggingFace paper database by keyword.

  3. Web scraping fallback — https://huggingface.co/papers
     Used when the JSON API returns 403 (e.g. missing auth token).

Authentication: set HF_TOKEN env var or pass hf_token= to the constructor.
"""
from __future__ import annotations

import logging
import os
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
HF_PAPERS_URL = "https://huggingface.co/papers"

MAX_FALLBACK_DAYS = 3
SEARCH_DELAY = 1.0
SEARCH_LIMIT = 50

HF_TOPIC_QUERIES: dict[str, list[str]] = {
    "Agent": ["llm agent", "autonomous agent", "multi-agent", "agentic"],
    "Harness": ["evaluation harness", "lm eval", "llm benchmark"],
    "Finance": ["financial llm", "stock prediction", "portfolio optimization", "algorithmic trading"],
}

_ARXIV_ID_RE = re.compile(r"(\d{4}\.\d{4,5})")


class HuggingFaceScraper:
    def __init__(
        self,
        session: Optional[requests.Session] = None,
        hf_token: Optional[str] = None,
    ):
        self.session = session or requests.Session()
        token = hf_token or os.environ.get("HF_TOKEN", "")
        headers: dict = {"User-Agent": "paper-find-bot/1.0"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        self.session.headers.update(headers)

    def fetch(self, target_date: date) -> List[Paper]:
        all_papers: dict[str, Paper] = {}

        daily = self._fetch_daily(target_date)
        for p in daily:
            all_papers[p.get_id()] = p
        logger.info("HuggingFace daily: %d papers", len(daily))

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
        for offset in range(MAX_FALLBACK_DAYS + 1):
            d = target_date - timedelta(days=offset)
            papers = self._fetch_date(d)
            if papers:
                if offset:
                    logger.info(
                        "HuggingFace: no papers for %s, using %s instead",
                        target_date, d,
                    )
                return papers
        # API failed — try web scraping fallback
        logger.info("HuggingFace: API unavailable, trying web scraping fallback")
        return self._scrape_web(target_date)

    def _fetch_date(self, d: date) -> List[Paper]:
        try:
            resp = self.session.get(
                HF_DAILY_API, params={"date": str(d)}, timeout=30
            )
            resp.raise_for_status()
            data = resp.json()
        except requests.exceptions.HTTPError as exc:
            if exc.response is not None and exc.response.status_code in (401, 403):
                logger.warning("HuggingFace daily API auth error (%s): %s", d, exc)
            else:
                logger.error("HuggingFace daily fetch error (%s): %s", d, exc)
            return []
        except Exception as exc:
            logger.error("HuggingFace daily fetch error (%s): %s", d, exc)
            return []

        papers: List[Paper] = []
        for item in data:
            paper = self._parse_item(item, source="huggingface")
            if paper:
                papers.append(paper)
        return papers

    # ------------------------------------------------------------------
    # Web scraping fallback (parses the /papers HTML page)
    # ------------------------------------------------------------------

    def _scrape_web(self, target_date: date) -> List[Paper]:
        """Parse arXiv IDs and titles from the HuggingFace /papers HTML page."""
        try:
            resp = self.session.get(HF_PAPERS_URL, timeout=30)
            resp.raise_for_status()
            html = resp.text
        except Exception as exc:
            logger.error("HuggingFace web scrape error: %s", exc)
            return []

        # Extract arXiv IDs mentioned in href attributes like /papers/2501.12345
        paper_ids = list(dict.fromkeys(re.findall(r'/papers/(\d{4}\.\d{4,5})', html)))
        logger.info("HuggingFace web: found %d paper IDs", len(paper_ids))

        papers: List[Paper] = []
        for arxiv_id in paper_ids[:60]:  # cap to avoid hammering arXiv
            papers.append(Paper(
                title=f"arXiv:{arxiv_id}",  # title will be enriched by arXiv scraper
                arxiv_id=arxiv_id,
                url=f"https://arxiv.org/abs/{arxiv_id}",
                source="huggingface",
                published_date=target_date,
            ))
        return papers

    # ------------------------------------------------------------------
    # Topic-based search
    # ------------------------------------------------------------------

    def _fetch_by_topics(self) -> List[Paper]:
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
        try:
            resp = self.session.get(
                HF_SEARCH_API,
                params={"q": query, "limit": SEARCH_LIMIT},
                timeout=30,
            )
            resp.raise_for_status()
            data = resp.json()
        except Exception as exc:
            logger.error("HuggingFace search fetch error (%s): %s", query, exc)
            return []

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
    # Shared parser
    # ------------------------------------------------------------------

    def _parse_item(self, item: dict, source: str = "huggingface") -> Optional[Paper]:
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
