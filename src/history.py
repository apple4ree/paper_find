"""
Cross-run deduplication: tracks paper IDs already published in previous digests.

State is persisted in output/seen_papers.json as:
  { "<paper_id>": "<YYYY-MM-DD first seen>" }

On each run:
  1. Load existing history.
  2. Filter today's papers to only those NOT in history  → "new papers".
  3. Add new paper IDs to history (keyed to today's date).
  4. Prune entries older than HISTORY_DAYS so the file stays small.
  5. Save.

The file is committed to git by the GitHub Actions workflow, so the history
persists across daily runs.
"""
from __future__ import annotations

import json
import logging
from datetime import date, timedelta
from pathlib import Path
from typing import Dict, List, Set

from .models import Paper

logger = logging.getLogger(__name__)

# Keep IDs for this many days; older entries are pruned automatically.
# Must be >= LOOKBACK_DAYS in config so we cover every paper we could re-fetch.
HISTORY_DAYS = 30


class SeenPapersHistory:
    """Persistent set of paper IDs already included in past digests."""

    def __init__(self, history_file: Path):
        self.history_file = history_file
        # paper_id → date-string of first inclusion
        self._seen: Dict[str, str] = {}
        self._load()

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def _load(self) -> None:
        if not self.history_file.exists():
            logger.info("History: no existing file at %s — starting fresh", self.history_file)
            return
        try:
            raw = self.history_file.read_text(encoding="utf-8")
            self._seen = json.loads(raw)
            logger.info("History: loaded %d previously seen paper IDs", len(self._seen))
        except Exception as exc:
            logger.warning(
                "History: could not load %s (%s) — starting fresh", self.history_file, exc
            )
            self._seen = {}

    def save(self) -> None:
        """Write history back to disk (call after adding new papers)."""
        self.history_file.parent.mkdir(parents=True, exist_ok=True)
        self.history_file.write_text(
            json.dumps(self._seen, indent=2, sort_keys=True),
            encoding="utf-8",
        )
        logger.info("History: saved %d paper IDs to %s", len(self._seen), self.history_file)

    # ------------------------------------------------------------------
    # Filtering
    # ------------------------------------------------------------------

    def filter_new(self, papers: List[Paper]) -> tuple[List[Paper], int]:
        """Return (new_papers, skipped_count) — papers NOT seen before."""
        seen_ids = set(self._seen.keys())
        new: List[Paper] = []
        skipped = 0
        for p in papers:
            if p.get_id() in seen_ids:
                skipped += 1
            else:
                new.append(p)
        return new, skipped

    # ------------------------------------------------------------------
    # Updating
    # ------------------------------------------------------------------

    def add_papers(self, papers: List[Paper], seen_date: date) -> None:
        """Mark *papers* as seen on *seen_date*."""
        date_str = str(seen_date)
        for p in papers:
            pid = p.get_id()
            if pid not in self._seen:
                self._seen[pid] = date_str

    def prune(self, as_of: date) -> None:
        """Remove entries first seen more than HISTORY_DAYS ago."""
        cutoff = str(as_of - timedelta(days=HISTORY_DAYS))
        before = len(self._seen)
        self._seen = {pid: d for pid, d in self._seen.items() if d >= cutoff}
        removed = before - len(self._seen)
        if removed:
            logger.info("History: pruned %d entries older than %s", removed, cutoff)
