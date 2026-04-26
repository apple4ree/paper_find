"""
Paper processor: deduplication, conference detection, and topic assignment.
"""
from __future__ import annotations

import logging
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


class PaperProcessor:
    """Deduplicate papers, detect conferences, and assign topic labels."""

    def process(self, papers: List[Paper]) -> Dict[str, List[Paper]]:
        """Return a dict mapping each topic to its de-duplicated, filtered papers."""
        # 1. Deduplicate across all sources
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

def _deduplicate(papers: List[Paper]) -> List[Paper]:
    """Merge duplicates, keeping the richest metadata.

    Two-pass approach:
      1. Group by arXiv ID (most reliable stable key).
      2. For papers without an arXiv ID, group by normalized title so that
         OpenReview and Semantic Scholar entries for the same paper merge.
    """
    # Pass 1: index by arXiv ID
    by_arxiv: Dict[str, Paper] = {}
    no_arxiv: List[Paper] = []
    for p in papers:
        if p.arxiv_id:
            base = p.arxiv_id.split("v")[0]
            key = f"arxiv:{base}"
            if key not in by_arxiv:
                by_arxiv[key] = p
            else:
                _merge(by_arxiv[key], p)
        else:
            no_arxiv.append(p)

    # Build reverse map: normalized title → arXiv paper (for cross-linking)
    title_to_arxiv: Dict[str, Paper] = {
        _norm_title(p.title): p for p in by_arxiv.values()
    }

    # Pass 2: papers without arXiv ID — try to merge by title into an
    # already-seen arXiv paper, otherwise keep in a separate title index.
    by_title: Dict[str, Paper] = {}
    for p in no_arxiv:
        nt = _norm_title(p.title)
        if nt in title_to_arxiv:
            # Same paper already found via arXiv — just enrich it
            _merge(title_to_arxiv[nt], p)
        elif nt in by_title:
            _merge(by_title[nt], p)
        else:
            by_title[nt] = p

    return list(by_arxiv.values()) + list(by_title.values())


def _norm_title(title: str) -> str:
    return " ".join(title.lower().split())


def _merge(target: Paper, source: Paper) -> None:
    """Enrich *target* with metadata from *source* without replacing good data."""
    if source.conference and not target.conference:
        target.conference = source.conference
    if source.abstract and not target.abstract:
        target.abstract = source.abstract
    if source.year and not target.year:
        target.year = source.year
    if source.published_date and not target.published_date:
        target.published_date = source.published_date
    if source.arxiv_id and not target.arxiv_id:
        target.arxiv_id = source.arxiv_id
        target.url = f"https://arxiv.org/abs/{source.arxiv_id}"
    if _SOURCE_PRIORITY.get(source.source, 99) < _SOURCE_PRIORITY.get(target.source, 99):
        target.source = source.source


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
