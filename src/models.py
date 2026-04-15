"""
Paper data model.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional


@dataclass
class Paper:
    title: str
    abstract: str = ""
    authors: List[str] = field(default_factory=list)
    url: str = ""
    arxiv_id: Optional[str] = None
    conference: Optional[str] = None
    year: Optional[int] = None
    # 'huggingface' | 'semantic_scholar' | 'arxiv'
    source: str = ""
    topics: List[str] = field(default_factory=list)
    published_date: Optional[date] = None

    def get_id(self) -> str:
        """Stable key used for deduplication.

        Prefer arXiv ID because the same paper may appear across all three
        sources.  Fall back to a normalised title string.
        """
        if self.arxiv_id:
            # Strip version suffix (e.g. "2310.12345v2" → "2310.12345")
            base = self.arxiv_id.split("v")[0]
            return f"arxiv:{base}"
        # Normalise title: lowercase, collapse whitespace
        normalized = " ".join(self.title.lower().split())
        return f"title:{normalized}"
