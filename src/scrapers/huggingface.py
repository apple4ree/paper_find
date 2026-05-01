"""
HuggingFace Daily Papers scraper.

Two fetch modes:
  1. Daily curated list  — https://huggingface.co/api/daily_papers?date=YYYY-MM-DD
     Returns the ~20-50 papers HuggingFace editors highlight each day.
     Falls back to the most recent available day if the requested date has no data.
     Requires HF_TOKEN env var (Bearer auth) if the API returns 403.

  2. Topic search        — https://huggingface.co/api/papers?q=<query>
     Searches the full HuggingFace paper database by keyword.
     Used to supplement the daily curated list with topic-relevant papers.

  3. HTML fallback       — https://huggingface.co/papers?date=YYYY-MM-DD
     Parses the public-facing HTML page when the JSON API is unavailable.
     Extracts arXiv IDs from the page and resolves metadata via arXiv API.
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

HF_DAILY_API    = "https://huggingface.co/api/daily_papers"
HF_SEARCH_API   = "https://huggingface.co/api/papers"
HF_PAPERS_HTML  = "https://huggingface.co/papers"
ARXIV_ABSTRACT  = "https://export.arxiv.org/api/query"

MAX_FALLBACK_DAYS = 3
SEARCH_DELAY      = 1.0
SEARCH_LIMIT      = 50

_ARXIV_ID_RE = re.compile(r"\b(\d{4}\.\d{4,5})\b")

HF_TOPIC_QUERIES: dict[str, list[str]] = {
    "Agent":   ["llm agent", "autonomous agent", "multi-agent", "agentic"],
    "Harness": ["evaluation harness", "lm eval", "llm benchmark"],
    "Finance": ["financial llm", "stock prediction", "portfolio optimization", "algorithmic trading"],
}


class HuggingFaceScraper:
    def __init__(self, session: Optional[requests.Session] = None, hf_token: Optional[str] = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": "paper-find-bot/1.0"})
        token = hf_token or os.environ.get("HF_TOKEN", "")
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"
            logger.info("HuggingFace: using Bearer token auth")

    def fetch(self, target_date: date) -> List[Paper]:
        """Return HuggingFace papers for *target_date*.

        Combines:
          - The daily curated list (API, with HTML fallback)
          - Topic-based search results from the HF paper database
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
        for offset in range(MAX_FALLBACK_DAYS + 1):
            d = target_date - timedelta(days=offset)
            papers = self._fetch_date_api(d)
            if papers:
                if offset:
                    logger.info("HuggingFace: no papers for %s, using %s instead", target_date, d)
                return papers
            # If API fails, try HTML fallback for the same date
            papers = self._fetch_date_html(d)
            if papers:
                if offset:
                    logger.info("HuggingFace HTML fallback: using %s", d)
                return papers
        logger.warning("HuggingFace: no curated papers found in the last %d days", MAX_FALLBACK_DAYS)
        return []

    def _fetch_date_api(self, d: date) -> List[Paper]:
        try:
            resp = self.session.get(HF_DAILY_API, params={"date": str(d)}, timeout=30)
            resp.raise_for_status()
            data = resp.json()
        except Exception as exc:
            logger.debug("HuggingFace API fetch error (%s): %s", d, exc)
            return []

        papers: List[Paper] = []
        for item in data:
            paper = self._parse_item(item, source="huggingface")
            if paper:
                papers.append(paper)
        return papers

    def _fetch_date_html(self, d: date) -> List[Paper]:
        """Scrape the public HuggingFace Papers HTML page and resolve arXiv IDs."""
        try:
            resp = self.session.get(
                HF_PAPERS_HTML,
                params={"date": str(d)},
                timeout=30,
                headers={"Accept": "text/html"},
            )
            resp.raise_for_status()
        except Exception as exc:
            logger.debug("HuggingFace HTML fetch error (%s): %s", d, exc)
            return []

        arxiv_ids = list(dict.fromkeys(_ARXIV_ID_RE.findall(resp.text)))
        if not arxiv_ids:
            return []

        logger.info("HuggingFace HTML: found %d arXiv IDs on %s", len(arxiv_ids), d)
        papers: List[Paper] = []
        for aid in arxiv_ids[:60]:
            p = self._resolve_arxiv(aid, d)
            if p:
                papers.append(p)
            time.sleep(0.5)
        return papers

    def _resolve_arxiv(self, arxiv_id: str, pub_date: date) -> Optional[Paper]:
        """Fetch metadata for a single arXiv paper via the arXiv API."""
        try:
            resp = self.session.get(
                ARXIV_ABSTRACT,
                params={"id_list": arxiv_id, "max_results": 1},
                timeout=20,
            )
            resp.raise_for_status()
        except Exception as exc:
            logger.debug("arXiv resolve error (%s): %s", arxiv_id, exc)
            return Paper(
                title=f"[arXiv:{arxiv_id}]",
                url=f"https://arxiv.org/abs/{arxiv_id}",
                arxiv_id=arxiv_id,
                source="huggingface",
                published_date=pub_date,
            )

        import xml.etree.ElementTree as ET
        NS = {"atom": "http://www.w3.org/2005/Atom"}
        try:
            root = ET.fromstring(resp.text)
            entry = root.find("atom:entry", NS)
            if entry is None:
                return None
            title = (entry.findtext("atom:title", "", NS) or "").strip().replace("\n", " ")
            abstract = (entry.findtext("atom:summary", "", NS) or "").strip().replace("\n", " ")
            authors = [
                (a.findtext("atom:name", "", NS) or "").strip()
                for a in entry.findall("atom:author", NS)
            ]
            authors = [a for a in authors if a]
        except ET.ParseError:
            title = f"[arXiv:{arxiv_id}]"
            abstract, authors = "", []

        return Paper(
            title=title or f"[arXiv:{arxiv_id}]",
            abstract=abstract,
            authors=authors,
            url=f"https://arxiv.org/abs/{arxiv_id}",
            arxiv_id=arxiv_id,
            source="huggingface",
            published_date=pub_date,
        )

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
                    logger.debug("HuggingFace search error [%s / %s]: %s", topic, query, exc)
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
            logger.debug("HuggingFace search fetch error (%s): %s", query, exc)
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
