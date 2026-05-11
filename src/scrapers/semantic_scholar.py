"""
Semantic Scholar scraper.

Searches the S2 Paper Search API for each topic keyword, then filters
results whose `venue` field matches one of our target conferences.

API endpoint: https://api.semanticscholar.org/graph/v1/paper/search
Rate limits (without key):  ~100 requests / 5 min
Rate limits (with key):     ~1 000 requests / 5 min
"""
from __future__ import annotations

import logging
import time
from datetime import date
from typing import Dict, List, Optional

import requests

from ..config import CONFERENCES, SS_FIELDS, TOPICS
from ..models import Paper

logger = logging.getLogger(__name__)

SS_SEARCH_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

_DELAY_NO_KEY = 1.5
_DELAY_WITH_KEY = 0.5

# Per-topic search terms: broad enough to cover Agent / Harness / Finance papers
# published at the six required conferences (AAAI, NeurIPS, ICML, ICLR, CVPR, KDD)
# as well as other top venues.
TOPIC_SEARCH_TERMS: Dict[str, List[str]] = {
    "Agent": [
        # Core agent terms
        "llm agent",
        "language model agent",
        "autonomous agent",
        "multi-agent system",
        "agentic workflow",
        # Tool / action
        "tool-augmented language model",
        "function calling language model",
        # Specialised agent types
        "gui agent",
        "web agent",
        "code agent",
        "embodied language agent",
        # Planning / reasoning
        "agent planning",
        "agent reasoning",
        # Conference-specific: CVPR / vision agents
        "vision language agent",
        "multimodal agent",
    ],
    "Harness": [
        "evaluation harness",
        "lm eval",
        "benchmarking framework",
        "evaluation suite",
        "language model benchmark",
        "llm evaluation",
        "capability evaluation",
        "model assessment framework",
        "safety benchmark",
    ],
    "Finance": [
        # LLM × Finance
        "financial large language model",
        "financial llm",
        "finllm",
        # Market prediction
        "stock market prediction",
        "stock price prediction",
        "market forecasting deep learning",
        # Portfolio / risk
        "portfolio optimization deep learning",
        "portfolio management reinforcement learning",
        "credit risk prediction",
        "systemic risk neural",
        # Trading
        "algorithmic trading deep learning",
        "high-frequency trading machine learning",
        "market microstructure machine learning",
        # Fraud / AML
        "fraud detection deep learning",
        "anti-money laundering machine learning",
        # Crypto
        "cryptocurrency prediction",
        "blockchain machine learning",
        # Sentiment / NLP
        "financial sentiment analysis",
        "financial news nlp",
        # Fintech / general
        "fintech deep learning",
        "robo-advisor machine learning",
    ],
}


class SemanticScholarScraper:
    def __init__(
        self,
        api_key: Optional[str] = None,
        session: Optional[requests.Session] = None,
    ):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": "paper-find-bot/1.0"})
        self._has_key = bool(api_key)
        if api_key:
            self.session.headers["x-api-key"] = api_key
        self._delay = _DELAY_WITH_KEY if self._has_key else _DELAY_NO_KEY

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def fetch(self) -> List[Paper]:
        """Return recent conference papers matching our topic keywords."""
        seen: Dict[str, Paper] = {}
        current_year = date.today().year
        year_range = f"{current_year - 1}-{current_year}"

        for topic, terms in TOPIC_SEARCH_TERMS.items():
            for term in terms:
                try:
                    results = self._search(term, year_range)
                    new_count = 0
                    for p in results:
                        pid = p.get_id()
                        if pid not in seen:
                            seen[pid] = p
                            new_count += 1
                    logger.debug(
                        "S2 [%s / %s]: %d results (%d new)",
                        topic, term, len(results), new_count,
                    )
                except requests.exceptions.HTTPError as exc:
                    if exc.response is not None and exc.response.status_code == 429:
                        logger.warning("S2 rate limited; sleeping 30s then retrying")
                        time.sleep(30)
                        try:
                            results = self._search(term, year_range)
                            for p in results:
                                pid = p.get_id()
                                if pid not in seen:
                                    seen[pid] = p
                        except Exception as retry_exc:
                            logger.error(
                                "S2 retry failed [%s / %s]: %s", topic, term, retry_exc
                            )
                    else:
                        logger.error("S2 HTTP error [%s / %s]: %s", topic, term, exc)
                except Exception as exc:
                    logger.error("S2 error [%s / %s]: %s", topic, term, exc)
                time.sleep(self._delay)

        logger.info("Semantic Scholar: %d unique papers collected", len(seen))
        return list(seen.values())

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _search(self, query: str, year_range: str, limit: int = 100) -> List[Paper]:
        params = {
            "query": query,
            "fields": SS_FIELDS,
            "limit": limit,
            "year": year_range,
        }
        resp = self.session.get(SS_SEARCH_URL, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()

        papers: List[Paper] = []
        for item in data.get("data") or []:
            p = self._parse_item(item)
            if p:
                papers.append(p)
        return papers

    def _parse_item(self, item: dict) -> Optional[Paper]:
        title = (item.get("title") or "").strip()
        if not title:
            return None

        venue = (item.get("venue") or "").strip()
        matched_conf = _match_conference(venue)
        if not matched_conf:
            return None

        ext_ids = item.get("externalIds") or {}
        arxiv_id = ext_ids.get("ArXiv") or None

        url = ""
        if arxiv_id:
            url = f"https://arxiv.org/abs/{arxiv_id}"
        else:
            pdf_info = item.get("openAccessPdf") or {}
            url = pdf_info.get("url") or ""
        if not url:
            paper_id = item.get("paperId") or ""
            url = f"https://www.semanticscholar.org/paper/{paper_id}"

        authors = [
            a.get("name", "") for a in (item.get("authors") or []) if a.get("name")
        ]

        pub_date: Optional[date] = None
        raw_date = item.get("publicationDate") or ""
        if raw_date:
            try:
                pub_date = date.fromisoformat(str(raw_date)[:10])
            except ValueError:
                pass

        return Paper(
            title=title,
            abstract=(item.get("abstract") or "").strip(),
            authors=authors,
            url=url,
            arxiv_id=arxiv_id,
            conference=matched_conf,
            year=item.get("year"),
            source="semantic_scholar",
            published_date=pub_date,
        )


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _match_conference(venue: str) -> Optional[str]:
    """Return canonical conference name if *venue* matches any alias."""
    venue_lower = venue.lower()
    for conf_name, aliases in CONFERENCES.items():
        if any(alias.lower() in venue_lower for alias in aliases):
            return conf_name
    return None
