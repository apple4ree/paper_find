"""
Paper processor: deduplication, conference detection, and topic assignment.
"""
from __future__ import annotations

import logging
from typing import Dict, List, Optional

from .config import CONFERENCES, TOPICS
from .models import Paper
from .identity import identity_groups

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
    """Merge duplicates, keeping the richest metadata."""
    result = []
    for group in identity_groups([vars(p) for p in papers]):
        existing = papers[group[0]]
        existing.sources = sorted({s for i in group for s in (papers[i].sources or [papers[i].source]) if s})
        for i in group[1:]:
            p = papers[i]
            # Enrich existing record rather than replacing it
            if p.conference and not existing.conference:
                existing.conference = p.conference
            if p.abstract and not existing.abstract:
                existing.abstract = p.abstract
            if p.year:
                existing.year = min(existing.year, p.year) if existing.year else p.year
            verified = p.date_kind in ("publication", "submission")
            current_verified = existing.date_kind in ("publication", "submission")
            if p.published_date and (not existing.published_date or
                    (verified and (not current_verified or p.published_date < existing.published_date))):
                existing.published_date = p.published_date
                existing.date_kind = p.date_kind
            if p.arxiv_id and not existing.arxiv_id:
                existing.arxiv_id = p.arxiv_id
            # Prefer higher-priority source when merging duplicates
            if _SOURCE_PRIORITY.get(p.source, 99) < _SOURCE_PRIORITY.get(existing.source, 99):
                existing.source = p.source
        result.append(existing)
    return result


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
