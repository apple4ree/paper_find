"""
Cross-run paper deduplication.

Persists the IDs of every paper already included in a previous digest so
that subsequent runs can filter them out.  Stored as JSON at
``output/.seen_papers.json``.

On first use, if the JSON file does not yet exist, the DB is seeded by
scanning existing ``output/*.md`` files for arXiv and Semantic-Scholar
URLs — this prevents a fresh install from re-reporting every paper that
already appeared in prior digests.
"""
from __future__ import annotations

import json
import logging
import re
from datetime import date
from pathlib import Path
from typing import Dict, List

from .models import Paper

logger = logging.getLogger(__name__)

# Matches arXiv IDs in URLs like https://arxiv.org/abs/2501.05366 (with
# optional version suffix, which we strip).
_ARXIV_URL_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", re.I)

# Semantic Scholar paper URL — extract the hash so we can deduplicate
# papers that did not carry an arXiv ID.
_S2_URL_RE = re.compile(r"semanticscholar\.org/paper/([0-9a-f]{8,})", re.I)

# Markdown bullet of the form ``- **[Title](url)**``
_MD_TITLE_RE = re.compile(r"-\s+\*\*\[(.+?)\]\((.+?)\)\*\*")


class SeenPapersDB:
    """JSON-backed store: paper_id → first-seen date (YYYY-MM-DD)."""

    def __init__(self, path: Path, output_dir: Path | None = None):
        self.path = Path(path)
        self._seen: Dict[str, str] = {}
        self._loaded_from_disk = False
        self._load()
        if not self._loaded_from_disk and output_dir is not None:
            self._seed_from_outputs(Path(output_dir))

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def _load(self) -> None:
        if not self.path.exists():
            return
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
            self._seen = dict(data.get("papers", {}))
            self._loaded_from_disk = True
            logger.info(
                "Loaded %d previously-seen paper IDs from %s",
                len(self._seen), self.path,
            )
        except Exception as exc:
            logger.warning("Could not load seen-papers db (%s): %s", self.path, exc)
            self._seen = {}

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        data = {"papers": self._seen}
        self.path.write_text(
            json.dumps(data, indent=2, sort_keys=True),
            encoding="utf-8",
        )
        logger.info(
            "Saved seen-papers db (%d entries) to %s",
            len(self._seen), self.path,
        )

    # ------------------------------------------------------------------
    # Seeding from existing markdown outputs
    # ------------------------------------------------------------------

    def _seed_from_outputs(self, output_dir: Path) -> None:
        """Populate the DB by scanning previous markdown digests."""
        if not output_dir.exists():
            return

        md_files = sorted(p for p in output_dir.glob("*.md") if p.name != "latest.md")
        if not md_files:
            return

        for md in md_files:
            try:
                text = md.read_text(encoding="utf-8")
            except Exception as exc:
                logger.debug("Skipping %s during seed: %s", md, exc)
                continue

            # Derive a date for this file (filename stem, e.g. "2026-04-19")
            first_seen = md.stem

            for m in _ARXIV_URL_RE.finditer(text):
                pid = f"arxiv:{m.group(1)}"
                self._seen.setdefault(pid, first_seen)

            for m in _S2_URL_RE.finditer(text):
                pid = f"s2:{m.group(1)}"
                self._seen.setdefault(pid, first_seen)

            # Title-based fallback for papers without a recognizable URL
            for m in _MD_TITLE_RE.finditer(text):
                title, url = m.group(1), m.group(2)
                if _ARXIV_URL_RE.search(url) or _S2_URL_RE.search(url):
                    continue  # already captured above
                normalized = " ".join(title.lower().split())
                pid = f"title:{normalized}"
                self._seen.setdefault(pid, first_seen)

        logger.info(
            "Seeded seen-papers db with %d entries from %d markdown files",
            len(self._seen), len(md_files),
        )

    # ------------------------------------------------------------------
    # Filtering
    # ------------------------------------------------------------------

    def filter_new(
        self,
        categorized: Dict[str, List[Paper]],
        target_date: date,
    ) -> Dict[str, List[Paper]]:
        """Remove papers whose IDs are already in the DB, record new ones."""
        filtered: Dict[str, List[Paper]] = {topic: [] for topic in categorized}
        newly_seen = 0
        skipped = 0

        # Collect unique new IDs first (a paper may appear in multiple topics)
        new_ids: set[str] = set()

        for topic, papers in categorized.items():
            for p in papers:
                pid = p.get_id()
                if pid in self._seen:
                    skipped += 1
                    continue
                filtered[topic].append(p)
                new_ids.add(pid)

        date_str = str(target_date)
        for pid in new_ids:
            self._seen[pid] = date_str
            newly_seen += 1

        logger.info(
            "Cross-run dedup: %d new papers kept, %d already-seen papers filtered",
            newly_seen, skipped,
        )
        return filtered
