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
    "cvf": 1,               # CVF = CVPR/ICCV accepted papers
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

def _enrich(existing: "Paper", candidate: "Paper") -> None:
    """Copy missing metadata from *candidate* into *existing* in-place."""
    if candidate.conference and not existing.conference:
        existing.conference = candidate.conference
    if candidate.abstract and not existing.abstract:
        existing.abstract = candidate.abstract
    if candidate.year and not existing.year:
        existing.year = candidate.year
    if candidate.published_date and not existing.published_date:
        existing.published_date = candidate.published_date
    if candidate.arxiv_id and not existing.arxiv_id:
        existing.arxiv_id = candidate.arxiv_id
        # Upgrade URL to arxiv canonical form
        if not existing.url or "semanticscholar" in existing.url:
            existing.url = f"https://arxiv.org/abs/{candidate.arxiv_id}"
    if _SOURCE_PRIORITY.get(candidate.source, 99) < _SOURCE_PRIORITY.get(existing.source, 99):
        existing.source = candidate.source


def _deduplicate(papers: List[Paper]) -> List[Paper]:
    """Merge duplicates, keeping the richest metadata.

    Two passes:
      1. Primary key: arXiv ID (stripped of version) or normalised title.
      2. Secondary: after pass 1, merge any two records that share the same
         normalised title (catches cases where one copy has an arXiv ID and
         the other doesn't, producing different primary keys).
    """
    # --- Pass 1: primary-key dedup ---
    by_id: Dict[str, "Paper"] = {}
    for p in papers:
        pid = p.get_id()
        if pid not in by_id:
            by_id[pid] = p
        else:
            _enrich(by_id[pid], p)

    # --- Pass 2: title-based dedup (catches arxiv vs non-arxiv copies) ---
    by_title: Dict[str, "Paper"] = {}
    kept: Dict[str, "Paper"] = {}  # pid → paper

    for pid, p in by_id.items():
        norm_title = " ".join(p.title.lower().split())
        if norm_title in by_title:
            # Merge into the earlier record
            _enrich(by_title[norm_title], p)
            # If the earlier record used a title-based ID, swap to arxiv ID
            existing_pid = by_title[norm_title].get_id()
            if existing_pid != pid and existing_pid in kept:
                # Re-key if the existing paper now has an arXiv ID
                new_pid = by_title[norm_title].get_id()
                if new_pid != existing_pid:
                    kept[new_pid] = kept.pop(existing_pid)
        else:
            by_title[norm_title] = p
            kept[pid] = p

    return list(kept.values())


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
