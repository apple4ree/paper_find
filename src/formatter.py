"""
Markdown formatter for the daily paper digest.
"""
from __future__ import annotations

from collections import Counter
from datetime import date, datetime, timezone, timedelta
from typing import Dict, List

from .models import Paper

_CONF_ORDER = ["AAAI", "NeurIPS", "ICML", "ICLR", "CVPR", "KDD"]

_SOURCE_BADGE = {
    "huggingface":        "🤗 HuggingFace Featured",
    "huggingface_search": "🤗 HuggingFace",
    "openreview":         "OpenReview",
    "cvf":                "CVF OpenAccess",
    "aaai":               "AAAI DL",
    "arxiv":              "arXiv",
    "semantic_scholar":   "Semantic Scholar",
}

KST = timezone(timedelta(hours=9))


class PaperFormatter:
    def format(self, categorized: Dict[str, List[Paper]], target_date: date) -> str:
        lines: List[str] = []

        unique_ids = {id(p) for plist in categorized.values() for p in plist}
        unique_count = len(unique_ids)
        total_entries = sum(len(v) for v in categorized.values())

        now_kst = datetime.now(KST).strftime("%Y-%m-%d %H:%M KST")

        lines += [
            f"# Daily Paper Digest — {target_date.strftime('%Y-%m-%d (%A)')}",
            "",
            "> **Sources**: AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · HuggingFace · OpenReview · arXiv · Semantic Scholar",
            "> **Topics**: Agent · Harness · Finance",
            f"> **Generated**: {now_kst}",
            "",
        ]

        # Top-level summary table
        lines += self._summary_table(categorized, unique_count, total_entries)
        lines += ["", "---", ""]

        if unique_count == 0:
            lines += [
                "> No matching papers found today.",
                "> Try running with a larger lookback window.",
                "",
            ]
            lines += self._footer(target_date)
            return "\n".join(lines)

        for topic, papers in categorized.items():
            lines.append(f"## {topic}  ({len(papers)} papers)")
            lines.append("")

            if not papers:
                lines += ["*No papers found for this topic today.*", ""]
                continue

            # Group by conference, preserve defined order
            by_conf: Dict[str, List[Paper]] = {}
            for p in papers:
                key = p.conference or "Other / arXiv"
                by_conf.setdefault(key, []).append(p)

            ordered_confs = _CONF_ORDER + sorted(
                k for k in by_conf if k not in _CONF_ORDER
            )

            for conf in ordered_confs:
                if conf not in by_conf:
                    continue
                conf_papers = by_conf[conf]
                lines.append(f"### {conf}  ({len(conf_papers)})")
                lines.append("")
                for p in conf_papers:
                    lines += self._format_paper(p)
                lines.append("")

        lines += self._footer(target_date)
        return "\n".join(lines)

    # ------------------------------------------------------------------

    def _summary_table(
        self,
        categorized: Dict[str, List[Paper]],
        unique_count: int,
        total_entries: int,
    ) -> List[str]:
        # Collect all papers (deduplicated by object id)
        seen_ids: set[int] = set()
        all_papers: List[Paper] = []
        for plist in categorized.values():
            for p in plist:
                if id(p) not in seen_ids:
                    seen_ids.add(id(p))
                    all_papers.append(p)

        conf_counts: Counter = Counter()
        source_counts: Counter = Counter()
        for p in all_papers:
            if p.conference:
                conf_counts[p.conference] += 1
            source_counts[p.source] += 1

        lines: List[str] = [
            f"**{unique_count} unique papers** "
            f"({total_entries} topic-entries — cross-topic papers counted once per topic)",
            "",
            "| Topic | Papers |",
            "|-------|-------:|",
        ]
        for topic, papers in categorized.items():
            lines.append(f"| {topic} | {len(papers)} |")
        lines += [
            "",
            "| Conference | Papers |",
            "|-----------|-------:|",
        ]
        for conf in _CONF_ORDER:
            if conf in conf_counts:
                lines.append(f"| {conf} | {conf_counts[conf]} |")
        for conf, cnt in sorted(conf_counts.items(), key=lambda x: -x[1]):
            if conf not in _CONF_ORDER:
                lines.append(f"| {conf} | {cnt} |")
        if not conf_counts:
            lines.append("| — | — |")
        lines += [
            "",
            "| Source | Papers |",
            "|--------|-------:|",
        ]
        source_label = {
            "huggingface":        "HuggingFace (daily)",
            "huggingface_search": "HuggingFace (search)",
            "openreview":         "OpenReview",
            "cvf":                "CVF OpenAccess (CVPR)",
            "aaai":               "AAAI Digital Library",
            "semantic_scholar":   "Semantic Scholar",
            "arxiv":              "arXiv",
        }
        for src, cnt in sorted(source_counts.items(), key=lambda x: -x[1]):
            label = source_label.get(src, src)
            lines.append(f"| {label} | {cnt} |")
        return lines

    def _format_paper(self, p: Paper) -> List[str]:
        title_md = f"[{p.title}]({p.url})" if p.url else p.title

        authors_str = ""
        if p.authors:
            shown = p.authors[:3]
            authors_str = ", ".join(shown)
            if len(p.authors) > 3:
                authors_str += " et al."

        meta: List[str] = []
        if p.conference:
            year = f" {p.year}" if p.year else ""
            meta.append(f"**{p.conference}{year}**")
        badge = _SOURCE_BADGE.get(p.source, p.source)
        if badge:
            meta.append(badge)
        if p.published_date:
            meta.append(f"`{p.published_date}`")

        lines = [f"- **{title_md}**"]
        if authors_str:
            lines.append(f"  - *{authors_str}*")
        if meta:
            lines.append(f"  - {' · '.join(meta)}")
        if p.abstract:
            snippet = p.abstract[:300].rstrip()
            if len(p.abstract) > 300:
                snippet += "…"
            lines.append(f"  - {snippet}")
        lines.append("")
        return lines

    def _footer(self, target_date: date) -> List[str]:
        return [
            "---",
            (
                f"*Generated {target_date} · "
                "Sources: HuggingFace Daily Papers, CVF OpenAccess, AAAI DL, "
                "OpenReview, Semantic Scholar, arXiv*"
            ),
            "",
        ]
