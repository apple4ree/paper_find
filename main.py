#!/usr/bin/env python3
"""
Daily paper digest: Agent | Harness | Finance
Conferences: AAAI, NeurIPS, ICML, ICLR, CVPR, KDD + HuggingFace

Usage
-----
  python main.py                       # today's papers
  python main.py --date 2025-04-10     # specific date
  python main.py --skip-arxiv          # skip the (slow) arXiv scraper
  python main.py --skip-s2             # skip Semantic Scholar
  python main.py --skip-hf             # skip HuggingFace
  python main.py --skip-openreview     # skip OpenReview (ICLR/NeurIPS/ICML)
  python main.py --s2-key <key>        # use an S2 API key for higher limits
"""
from __future__ import annotations

import argparse
import logging
import json
from copy import deepcopy
import os
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from typing import List

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Entry point
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
        "--skip-hf",
        action="store_true",
        help="Skip the HuggingFace scraper.",
    )
    p.add_argument(
        "--skip-s2",
        action="store_true",
        help="Skip the Semantic Scholar scraper.",
    )
    p.add_argument(
        "--skip-arxiv",
        action="store_true",
        help="Skip the arXiv scraper.",
    )
    p.add_argument(
        "--skip-openreview",
        action="store_true",
        help="Skip the OpenReview scraper (ICLR / NeurIPS / ICML).",
    )
    p.add_argument(
        "--s2-key",
        default=os.environ.get("SS_API_KEY", ""),
        help="Semantic Scholar API key (or set SS_API_KEY env var).",
    )
    p.add_argument('--strict', action='store_true', help='Exit 2 after saving diagnostics when collection is incomplete or count alerts fire.')
    p.add_argument('--drop-ratio', type=float, default=0.5)
    p.add_argument('--spike-ratio', type=float, default=2.0)
    p.add_argument('--min-baseline', type=int, default=20)
    return p.parse_args()


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

    from src.collection import CollectionStats
    from src.scrapers.huggingface import HuggingFaceScraper
    from src.scrapers.semantic_scholar import SemanticScholarScraper
    from src.scrapers.arxiv import ArxivScraper
    from src.scrapers.openreview import OpenReviewScraper

    if not (0 < args.drop_ratio < 1 < args.spike_ratio) or args.min_baseline < 1:
        logger.error("Invalid alert thresholds")
        return 1
    source_runs = []
    for name, skipped, factory in [
        ("huggingface", args.skip_hf, HuggingFaceScraper),
        ("semantic_scholar", args.skip_s2, lambda: SemanticScholarScraper(api_key=args.s2_key or None)),
        ("arxiv", args.skip_arxiv, ArxivScraper),
        ("openreview", args.skip_openreview, OpenReviewScraper),
    ]:
        papers = []
        stats = CollectionStats(name, skipped=skipped)
        if not skipped:
            logger.info("=== %s ===", name)
            try:
                scraper = factory()
                stats = scraper.stats
                papers = scraper.fetch(target_date)
            except Exception as exc:
                stats.fatal_error = type(exc).__name__
                logger.error("%s collection failed: %s", name, type(exc).__name__)
            all_papers.extend(papers)
            source_counts[name] = len(papers)
        source_runs.append(stats.summary(papers))

    if not all_papers:
        logger.warning("No papers collected — check network access and try again.")

    # ---- Process -----------------------------------------------------------
    logger.info("=== Processing %d raw papers ===", len(all_papers))
    from src.processor import PaperProcessor
    categorized = PaperProcessor().process(deepcopy(all_papers))

    # ---- Format & save -----------------------------------------------------
    from src.formatter import PaperFormatter
    from src.audit import build_audit
    audit = build_audit(categorized, all_papers, source_runs, target_date, output_dir,
                        args.min_baseline, args.drop_ratio, args.spike_ratio)
    report = PaperFormatter().format(categorized, target_date, audit)

    date_file = output_dir / f"{target_date}.md"
    latest_file = output_dir / "latest.md"

    def save_atomic(path, content):
        temp = path.with_suffix(path.suffix + '.tmp')
        temp.write_text(content, encoding='utf-8')
        temp.replace(path)

    save_atomic(output_dir / f"{target_date}.json", json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    save_atomic(date_file, report)
    latest_date = max((p.stem for p in output_dir.glob('????-??-??.md')), default=str(target_date))
    if str(target_date) >= latest_date and all_papers:
        save_atomic(latest_file, report)

    total = sum(len(v) for v in categorized.values())
    unique = len({id(p) for plist in categorized.values() for p in plist})
    logger.info("Report written → %s  (%d unique papers)", date_file, unique)

    # Print a summary to stdout
    print(f"\n{'='*60}")
    print(f"  Daily Paper Digest  {target_date}")
    print(f"{'='*60}")

    print(f"\n  {'Source':<25} {'Raw':>5}")
    print(f"  {'-'*35}")
    source_label = {
        "huggingface":        "HuggingFace (daily+search)",
        "huggingface_search": "HuggingFace (search)",
        "openreview":         "OpenReview (ICLR/NeurIPS/ICML)",
        "semantic_scholar":   "Semantic Scholar",
        "arxiv":              "arXiv",
    }
    for src, cnt in sorted(source_counts.items(), key=lambda x: -x[1]):
        label = source_label.get(src, src)
        print(f"  {label:<25} {cnt:>5}")
    print(f"  {'─'*35}")
    print(f"  {'Total raw':<25} {len(all_papers):>5}")

    print(f"\n  {'Topic':<15} {'Papers':>7}")
    print(f"  {'-'*25}")
    for topic, papers in categorized.items():
        print(f"  {topic:<15} {len(papers):>7}")
    print(f"  {'─'*25}")
    print(f"  {'Unique total':<15} {unique:>7}")

    print(f"\n  Output: {date_file}")
    print(f"{'='*60}")

    for alert in audit['alerts']:
        logger.warning("Collection alert: %s", alert)
    actionable = any(a['kind'] in ('collection_incomplete', 'count_drop', 'count_spike', 'high_disappearance') for a in audit['alerts'])
    if not all_papers and not all(s['status'] == 'skipped' for s in source_runs):
        return 2
    return 2 if args.strict and actionable else 0


if __name__ == "__main__":
    sys.exit(main())
