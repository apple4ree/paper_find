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
    "cvf": 1,               # same priority as openreview (official proceedings)
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

    Two-pass strategy:
      Pass 1 — deduplicate by primary key (arxiv_id or normalized title).
      Pass 2 — collapse title-keyed entries that share a normalized title
               with an already-seen arxiv-keyed entry.  This catches the
               common case where OpenReview returns a paper without an
               arxiv_id while the same paper was also fetched from arXiv.
    """
    seen: Dict[str, Paper] = {}
    for p in papers:
        pid = p.get_id()
        if pid not in seen:
            seen[pid] = p
        else:
            _merge(seen[pid], p)

    # Build a lookup: normalized_title → arxiv key (from pass 1)
    title_to_arxiv_key: Dict[str, str] = {}
    for pid, p in seen.items():
        if pid.startswith("arxiv:"):
            norm = " ".join(p.title.lower().split())
            title_to_arxiv_key[norm] = pid

    # Pass 2: drop title-keyed entries that already exist under an arxiv key
    final: Dict[str, Paper] = {}
    for pid, p in seen.items():
        if pid.startswith("title:"):
            norm = pid[len("title:"):]
            if norm in title_to_arxiv_key:
                _merge(seen[title_to_arxiv_key[norm]], p)
                continue  # skip: already represented by the arxiv entry
        final[pid] = p

    return list(final.values())


def _merge(existing: Paper, incoming: Paper) -> None:
    """Enrich *existing* paper record with metadata from *incoming*."""
    if incoming.conference and not existing.conference:
        existing.conference = incoming.conference
    if incoming.abstract and not existing.abstract:
        existing.abstract = incoming.abstract
    if incoming.year and not existing.year:
        existing.year = incoming.year
    if incoming.published_date and not existing.published_date:
        existing.published_date = incoming.published_date
    if _SOURCE_PRIORITY.get(incoming.source, 99) < _SOURCE_PRIORITY.get(existing.source, 99):
        existing.source = incoming.source


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
