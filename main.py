#!/usr/bin/env python3
"""
Daily paper digest: Agent | Harness | Finance
Conferences: AAAI, NeurIPS, ICML, ICLR, CVPR, KDD + HuggingFace

Usage
-----
  python main.py                       # today's papers (cross-run dedup on)
  python main.py --date 2025-04-10     # specific date
  python main.py --fresh               # skip history dedup (show all papers)
  python main.py --skip-arxiv          # skip the (slow) arXiv scraper
  python main.py --skip-s2             # skip Semantic Scholar
  python main.py --skip-hf             # skip HuggingFace
  python main.py --s2-key <key>        # use an S2 API key for higher limits
"""
from __future__ import annotations

import argparse
import logging
import os
import sys
from collections import Counter
from datetime import date
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Daily paper digest builder")
    p.add_argument(
        "--date",
        default=str(date.today()),
        help="Target date (YYYY-MM-DD).  Defaults to today.",
    )
    p.add_argument(
        "--output-dir",
        default="output",
        help="Directory where markdown reports are written.",
    )
    p.add_argument(
        "--fresh",
        action="store_true",
        help=(
            "Disable cross-run deduplication — include ALL matched papers "
            "even if they appeared in previous digests. "
            "Useful for rebuilding a specific date."
        ),
    )
    p.add_argument("--skip-hf",    action="store_true", help="Skip HuggingFace scraper.")
    p.add_argument("--skip-s2",    action="store_true", help="Skip Semantic Scholar scraper.")
    p.add_argument("--skip-arxiv", action="store_true", help="Skip arXiv scraper.")
    p.add_argument(
        "--s2-key",
        default=os.environ.get("SS_API_KEY", ""),
        help="Semantic Scholar API key (or set SS_API_KEY env var).",
    )
    return p.parse_args()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    args = parse_args()

    try:
        target_date = date.fromisoformat(args.date)
    except ValueError:
        logger.error("Invalid date: %s  (expected YYYY-MM-DD)", args.date)
        return 1

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    all_papers = []
    source_counts: Counter = Counter()

    # ---- HuggingFace -------------------------------------------------------
    if not args.skip_hf:
        logger.info("=== HuggingFace Papers ===")
        from src.scrapers.huggingface import HuggingFaceScraper
        hf_papers = HuggingFaceScraper().fetch(target_date)
        logger.info("  collected %d papers", len(hf_papers))
        all_papers.extend(hf_papers)
        for p in hf_papers:
            source_counts[p.source] += 1

    # ---- Semantic Scholar --------------------------------------------------
    if not args.skip_s2:
        logger.info("=== Semantic Scholar (conference papers) ===")
        from src.scrapers.semantic_scholar import SemanticScholarScraper
        ss_papers = SemanticScholarScraper(api_key=args.s2_key or None).fetch()
        logger.info("  collected %d papers", len(ss_papers))
        all_papers.extend(ss_papers)
        source_counts["semantic_scholar"] += len(ss_papers)

    # ---- arXiv -------------------------------------------------------------
    if not args.skip_arxiv:
        logger.info("=== arXiv (recent submissions) ===")
        from src.scrapers.arxiv import ArxivScraper
        arxiv_papers = ArxivScraper().fetch(target_date)
        logger.info("  collected %d papers", len(arxiv_papers))
        all_papers.extend(arxiv_papers)
        source_counts["arxiv"] += len(arxiv_papers)

    if not all_papers:
        logger.warning("No papers collected — check network access and try again.")

    # ---- Process (within-run dedup + topic assignment) ---------------------
    logger.info("=== Processing %d raw papers ===", len(all_papers))
    from src.processor import PaperProcessor
    categorized = PaperProcessor().process(all_papers)

    # ---- Cross-run deduplication (skip if --fresh) -------------------------
    history_file = output_dir / "seen_papers.json"
    total_skipped = 0

    if args.fresh:
        logger.info("--fresh flag set: skipping cross-run deduplication")
    else:
        from src.history import SeenPapersHistory
        history = SeenPapersHistory(history_file)

        # Collect all unique paper objects across topics
        all_categorized_papers = {
            id(p): p
            for plist in categorized.values()
            for p in plist
        }

        # Filter each topic bucket
        for topic in list(categorized.keys()):
            new_papers, skipped = history.filter_new(categorized[topic])
            total_skipped += skipped
            categorized[topic] = new_papers

        # Deduplicate skipped count (a paper in 2 topics counts once)
        # Recalculate by checking which papers survive across all topics
        surviving_ids = {
            p.get_id()
            for plist in categorized.values()
            for p in plist
        }
        all_ids = {p.get_id() for p in all_categorized_papers.values()}
        total_skipped = len(all_ids) - len(surviving_ids)

        logger.info(
            "Cross-run dedup: skipped %d already-reported papers", total_skipped
        )

        # Gather surviving papers (unique objects) to add to history
        new_paper_objects = [
            p
            for plist in categorized.values()
            for p in plist
        ]
        # Deduplicate the list itself before adding to history
        seen_in_loop: set[str] = set()
        unique_new: list = []
        for p in new_paper_objects:
            pid = p.get_id()
            if pid not in seen_in_loop:
                seen_in_loop.add(pid)
                unique_new.append(p)

        history.add_papers(unique_new, target_date)
        history.prune(target_date)
        history.save()

    # ---- Format & save -----------------------------------------------------
    from src.formatter import PaperFormatter
    report = PaperFormatter().format(categorized, target_date)

    date_file = output_dir / f"{target_date}.md"
    latest_file = output_dir / "latest.md"

    date_file.write_text(report, encoding="utf-8")
    latest_file.write_text(report, encoding="utf-8")

    total_entries = sum(len(v) for v in categorized.values())
    unique_count = len({id(p) for plist in categorized.values() for p in plist})
    logger.info(
        "Report written → %s  (%d unique new papers)", date_file, unique_count
    )

    # ---- Stdout summary ----------------------------------------------------
    print(f"\n{'='*60}")
    print(f"  Daily Paper Digest  {target_date}")
    print(f"{'='*60}")

    print(f"\n  {'Source':<25} {'Raw':>5}")
    print(f"  {'-'*35}")
    source_label = {
        "huggingface":        "HuggingFace (daily)",
        "huggingface_search": "HuggingFace (search)",
        "semantic_scholar":   "Semantic Scholar",
        "arxiv":              "arXiv",
    }
    for src, cnt in sorted(source_counts.items(), key=lambda x: -x[1]):
        label = source_label.get(src, src)
        print(f"  {label:<25} {cnt:>5}")
    print(f"  {'─'*35}")
    print(f"  {'Total raw':<25} {len(all_papers):>5}")
    if not args.fresh:
        print(f"  {'Already reported':<25} {total_skipped:>5}  ← cross-run dedup")

    print(f"\n  {'Topic':<15} {'New papers':>10}")
    print(f"  {'-'*28}")
    for topic, papers in categorized.items():
        print(f"  {topic:<15} {len(papers):>10}")
    print(f"  {'─'*28}")
    print(f"  {'Unique new':<15} {unique_count:>10}")

    print(f"\n  Output: {date_file}")
    if not args.fresh:
        print(f"  History: {history_file}")
    print(f"{'='*60}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
