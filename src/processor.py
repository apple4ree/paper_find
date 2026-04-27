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

    Two-pass dedup:
      1. Primary key: arxiv:<id> or title:<normalized>
      2. Secondary: cross-link arxiv-keyed and title-keyed entries for the
         same paper (one source had the arXiv ID, another didn't).
    """
    # Pass 1: primary key dedup
    seen: Dict[str, Paper] = {}
    for p in papers:
        pid = p.get_id()
        if pid not in seen:
            seen[pid] = p
        else:
            _merge(seen[pid], p)

    # Pass 2: cross-link arxiv-keyed entries with title-keyed duplicates.
    # Build a title → arxiv-key map for O(n) lookup.
    title_to_arxiv_key: Dict[str, str] = {}
    for pid, p in seen.items():
        if pid.startswith("arxiv:"):
            norm = " ".join(p.title.lower().split())
            title_to_arxiv_key[norm] = pid

    to_remove: List[str] = []
    for pid, p in seen.items():
        if pid.startswith("title:"):
            norm = pid[len("title:"):]
            arxiv_key = title_to_arxiv_key.get(norm)
            if arxiv_key:
                _merge(seen[arxiv_key], p)
                to_remove.append(pid)

    for pid in to_remove:
        del seen[pid]

    return list(seen.values())


def _merge(target: Paper, source: Paper) -> None:
    """Enrich *target* with metadata from *source* in-place."""
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
