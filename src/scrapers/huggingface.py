"""
HuggingFace Daily Papers scraper.

Endpoint: https://huggingface.co/api/daily_papers?date=YYYY-MM-DD
Returns a JSON array of curated papers for the given date.
Falls back to the most recent available day if the requested date has no data.
"""
from __future__ import annotations

import logging
from datetime import date, timedelta
from typing import List, Optional

import requests

from ..models import Paper

logger = logging.getLogger(__name__)

HF_API = "https://huggingface.co/api/daily_papers"
MAX_FALLBACK_DAYS = 3  # Try up to N previous days if today has no papers


class HuggingFaceScraper:
    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": "paper-find-bot/1.0"})

    def fetch(self, target_date: date) -> List[Paper]:
        """Return curated HuggingFace papers for *target_date*.

        Tries up to MAX_FALLBACK_DAYS earlier dates if the requested day is
        not yet populated (e.g. running just after midnight UTC).
        """
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
        logger.warning("HuggingFace: no papers found in the last %d days", MAX_FALLBACK_DAYS)
        return []

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _fetch_date(self, d: date) -> List[Paper]:
        try:
            resp = self.session.get(HF_API, params={"date": str(d)}, timeout=30)
            resp.raise_for_status()
            data = resp.json()
        except Exception as exc:
            logger.error("HuggingFace fetch error (%s): %s", d, exc)
            return []

        papers: List[Paper] = []
        for item in data:
            paper = self._parse_item(item)
            if paper:
                papers.append(paper)
        return papers

    def _parse_item(self, item: dict) -> Optional[Paper]:
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
            source="huggingface",
            published_date=pub_date,
        )
