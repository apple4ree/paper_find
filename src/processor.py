"""
Paper processor: deduplication, conference detection, and topic assignment.
"""
from __future__ import annotations

import logging
import re
from typing import Dict, List, Optional

from .config import CONFERENCES, TOPICS
from .models import Paper

logger = logging.getLogger(__name__)

# Source display priority (lower = shown first in output)
_SOURCE_PRIORITY = {
    "huggingface": 0,
    "openreview": 1,        # conference-accepted papers rank highly
    "huggingface_search": 2,
    "arxiv": 3,
    "semantic_scholar": 4,
}

_PUNCT_RE = re.compile(r"[^\w\s]")


def _norm_title(title: str) -> str:
    """Normalize title for fuzzy deduplication: lowercase, strip punctuation, collapse spaces."""
    return " ".join(_PUNCT_RE.sub(" ", title.lower()).split())


class PaperProcessor:
    """Deduplicate papers, detect conferences, and assign topic labels."""

    def process(self, papers: List[Paper]) -> Dict[str, List[Paper]]:
        """Return a dict mapping each topic to its de-duplicated, filtered papers."""
        # 1. Deduplicate across all sources (two-pass)
        deduped = _deduplicate(papers)
        logger.info("Dedup: %d → %d papers", len(papers), len(deduped))

        # 2. Try to infer conference from title/abstract when not already set
        for p in deduped:
            if not p.conference:
                p.conference = _detect_conference(p)

        # 3. Assign topic labels
        categorized: Dict[str, List[Paper]] = {topic: [] for topic in TOPICS}
        for p in deduped:
            matched = _match_topics(p)
            if matched:
                p.topics = matched
                for topic in matched:
                    categorized[topic].append(p)

        # 4. Sort each bucket: HuggingFace featured first, then newest first
        for topic in categorized:
            categorized[topic].sort(
                key=lambda p: (
                    _SOURCE_PRIORITY.get(p.source, 99),
                    -(p.published_date.toordinal() if p.published_date else 0),
                )
            )

        for topic, plist in categorized.items():
            logger.info("  %s: %d papers", topic, len(plist))

        return categorized


# ---------------------------------------------------------------------------
# Module-level helpers
# ---------------------------------------------------------------------------

def _merge_into(existing: Paper, incoming: Paper) -> None:
    """Enrich *existing* with metadata from *incoming*."""
    if incoming.conference and not existing.conference:
        existing.conference = incoming.conference
    if incoming.abstract and not existing.abstract:
        existing.abstract = incoming.abstract
    if incoming.year and not existing.year:
        existing.year = incoming.year
    if incoming.published_date and not existing.published_date:
        existing.published_date = incoming.published_date
    if incoming.arxiv_id and not existing.arxiv_id:
        existing.arxiv_id = incoming.arxiv_id
        if not existing.url or "semanticscholar" in existing.url:
            existing.url = f"https://arxiv.org/abs/{incoming.arxiv_id}"
    if _SOURCE_PRIORITY.get(incoming.source, 99) < _SOURCE_PRIORITY.get(existing.source, 99):
        existing.source = incoming.source


def _deduplicate(papers: List[Paper]) -> List[Paper]:
    """Two-pass deduplication: first by arxiv_id, then by normalized title.

    A paper scraped from OpenReview may lack an arXiv link while the same
    paper from arXiv/Semantic Scholar has one, giving them different get_id()
    keys despite being identical.  We resolve this by building a secondary
    index on normalized titles and unifying any collisions.
    """
    # Pass 1: index by the primary key (arxiv_id or normalized title)
    by_key: Dict[str, Paper] = {}
    for p in papers:
        pid = p.get_id()
        if pid not in by_key:
            by_key[pid] = p
        else:
            _merge_into(by_key[pid], p)

    candidates = list(by_key.values())

    # Pass 2: secondary dedup by normalized title across different primary keys
    by_title: Dict[str, Paper] = {}
    final: List[Paper] = []
    for p in candidates:
        nt = _norm_title(p.title)
        if nt in by_title:
            _merge_into(by_title[nt], p)
        else:
            by_title[nt] = p
            final.append(p)

    return final


def _detect_conference(paper: Paper) -> Optional[str]:
    combined = f"{paper.title} {paper.abstract}".lower()
    for conf_name, aliases in CONFERENCES.items():
        if any(alias.lower() in combined for alias in aliases):
            return conf_name
    return None


def _match_topics(paper: Paper) -> List[str]:
    combined = f"{paper.title} {paper.abstract}".lower()
    return [
        topic
        for topic, keywords in TOPICS.items()
        if any(kw.lower() in combined for kw in keywords)
    ]
