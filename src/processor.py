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
    "openreview": 1,
    "cvf": 1,           # same tier as OpenReview (accepted conference papers)
    "huggingface_search": 2,
    "arxiv": 3,
    "semantic_scholar": 4,
}

# Titles that start with these prefixes are not actual papers
_NON_PAPER_PREFIXES = (
    "review:",
    "comment:",
    "response to",
    "rebuttal:",
    "meta-review:",
)


class PaperProcessor:
    """Deduplicate papers, detect conferences, and assign topic labels."""

    def process(self, papers: List[Paper]) -> Dict[str, List[Paper]]:
        """Return a dict mapping each topic to its de-duplicated, filtered papers."""
        # 1. Remove non-paper entries (review submissions, rebuttals, etc.)
        papers = [p for p in papers if not _is_non_paper(p)]

        # 2. Deduplicate across all sources
        deduped = _deduplicate(papers)
        logger.info("Dedup: %d → %d papers", len(papers), len(deduped))

        # 3. Try to infer conference from title/abstract when not already set
        for p in deduped:
            if not p.conference:
                p.conference = _detect_conference(p)

        # 4. Assign topic labels
        categorized: Dict[str, List[Paper]] = {topic: [] for topic in TOPICS}
        for p in deduped:
            matched = _match_topics(p)
            if matched:
                p.topics = matched
                for topic in matched:
                    categorized[topic].append(p)

        # 5. Sort each bucket: HuggingFace featured first, then newest first
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

def _normalize_title(title: str) -> str:
    """Aggressive title normalization for dedup comparison.

    Strips punctuation, lowercases, and collapses whitespace so that
    small formatting differences (colons, hyphens, extra spaces) don't
    prevent two records for the same paper from being merged.
    """
    t = title.lower().strip()
    t = re.sub(r"[^\w\s]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def _enrich(existing: Paper, new: Paper) -> None:
    """Update *existing* in-place with better data from *new*."""
    if new.conference and not existing.conference:
        existing.conference = new.conference
    if new.abstract and not existing.abstract:
        existing.abstract = new.abstract
    if new.year and not existing.year:
        existing.year = new.year
    if new.published_date and not existing.published_date:
        existing.published_date = new.published_date
    # Upgrade to a better source priority
    if _SOURCE_PRIORITY.get(new.source, 99) < _SOURCE_PRIORITY.get(existing.source, 99):
        existing.source = new.source
    # Grab an arXiv ID if the existing record lacks one
    if new.arxiv_id and not existing.arxiv_id:
        existing.arxiv_id = new.arxiv_id
        # Prefer the arXiv URL over an S2 landing page
        if not existing.url or "semanticscholar.org" in existing.url:
            existing.url = f"https://arxiv.org/abs/{new.arxiv_id}"


def _deduplicate(papers: List[Paper]) -> List[Paper]:
    """Merge duplicates, keeping the richest metadata.

    Two-phase dedup:
      Phase 1 — exact paper ID (arXiv:<id> or title:<normalised>)
      Phase 2 — normalised title cross-check so that the same paper
                 seen once with an arXiv ID and once without is merged.
    """
    seen: Dict[str, Paper] = {}          # canonical_id → Paper
    title_to_id: Dict[str, str] = {}     # normalised_title → canonical_id

    for p in papers:
        pid = p.get_id()
        norm = _normalize_title(p.title)

        # --- Phase 1: exact ID match ---
        if pid in seen:
            _enrich(seen[pid], p)
            continue

        # --- Phase 2: same title, different ID type ---
        if norm in title_to_id:
            canonical = title_to_id[norm]
            _enrich(seen[canonical], p)
            continue

        # New paper — register it
        seen[pid] = p
        title_to_id[norm] = pid

    return list(seen.values())


def _is_non_paper(paper: Paper) -> bool:
    """Return True if this entry is a peer-review artefact, not an actual paper."""
    title_lower = paper.title.lower().strip()
    return any(title_lower.startswith(prefix) for prefix in _NON_PAPER_PREFIXES)


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
