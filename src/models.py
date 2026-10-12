"""
Paper data model.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional
from .identity import aliases


@dataclass
class Paper:
    title: str
    abstract: str = ""
    authors: List[str] = field(default_factory=list)
    url: str = ""
    arxiv_id: Optional[str] = None
    conference: Optional[str] = None
    year: Optional[int] = None
    # 'huggingface' | 'huggingface_search' | 'openreview' | 'semantic_scholar' | 'arxiv'
    source: str = ""
    topics: List[str] = field(default_factory=list)
    published_date: Optional[date] = None
    # record_created is deliberately not evidence of first publication.
    date_kind: str = "publication"
    sources: List[str] = field(default_factory=list)

    def get_id(self) -> str:
        """Stable key used for deduplication.

        Prefer arXiv ID because the same paper may appear across all three
        sources.  Fall back to a normalised title string.
        """
        keys = aliases(vars(self))
        for prefix in ("arxiv:", "doi:", "openreview:", "title:", "url:"):
            matches = sorted(k for k in keys if k.startswith(prefix))
            if matches:
                return matches[0]
        raise ValueError("Paper has no identity")
