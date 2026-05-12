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
        "--skip-cvf",
        action="store_true",
        help="Skip the CVF Open Access scraper (CVPR).",
    )
    p.add_argument(
        "--s2-key",
        default=os.environ.get("SS_API_KEY", ""),
        help="Semantic Scholar API key (or set SS_API_KEY env var).",
    )
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

    # ---- OpenReview --------------------------------------------------------
    if not args.skip_openreview:
        logger.info("=== OpenReview (ICLR / NeurIPS / ICML) ===")
        from src.scrapers.openreview import OpenReviewScraper
        or_papers = OpenReviewScraper().fetch()
        logger.info("  collected %d papers", len(or_papers))
        all_papers.extend(or_papers)
        source_counts["openreview"] += len(or_papers)

    # ---- CVF Open Access ---------------------------------------------------
    if not args.skip_cvf:
        logger.info("=== CVF Open Access (CVPR) ===")
        from src.scrapers.cvf import CVFScraper
        cvf_papers = CVFScraper().fetch()
        logger.info("  collected %d papers", len(cvf_papers))
        all_papers.extend(cvf_papers)
        source_counts["cvf"] += len(cvf_papers)

    if not all_papers:
        logger.warning("No papers collected — check network access and try again.")

    # ---- Process -----------------------------------------------------------
    logger.info("=== Processing %d raw papers ===", len(all_papers))
    from src.processor import PaperProcessor
    categorized = PaperProcessor().process(all_papers)

    # ---- Format & save -----------------------------------------------------
    from src.formatter import PaperFormatter
    report = PaperFormatter().format(categorized, target_date)

    date_file = output_dir / f"{target_date}.md"
    latest_file = output_dir / "latest.md"

    date_file.write_text(report, encoding="utf-8")
    latest_file.write_text(report, encoding="utf-8")

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
        "huggingface":        "HuggingFace (daily)",
        "huggingface_search": "HuggingFace (search)",
        "openreview":         "OpenReview (ICLR/NeurIPS/ICML)",
        "semantic_scholar":   "Semantic Scholar",
        "arxiv":              "arXiv",
        "cvf":                "CVF Open Access (CVPR)",
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

    return 0


if __name__ == "__main__":
    sys.exit(main())
