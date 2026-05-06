"""
Markdown formatter for the daily paper digest.
"""
from __future__ import annotations

from datetime import date
from typing import Dict, List

from .models import Paper

# Conference display order within each topic section
_CONF_ORDER = ["AAAI", "NeurIPS", "ICML", "ICLR", "CVPR", "KDD"]

_SOURCE_BADGE = {
    "huggingface":        "HuggingFace Featured",
    "huggingface_search": "HuggingFace",
    "openreview":         "OpenReview",
    "arxiv":              "arXiv",
    "semantic_scholar":   "Semantic Scholar",
    "cvf":                "CVF",
}


class PaperFormatter:
    def format(self, categorized: Dict[str, List[Paper]], target_date: date) -> str:
        lines: List[str] = []

        # Unique papers across all topics
        unique_papers = {
            id(p)
            for plist in categorized.values()
            for p in plist
        }
        unique_count = len(unique_papers)
        total_entries = sum(len(v) for v in categorized.values())

        lines += [
            f"# Daily Paper Digest — {target_date.strftime('%Y-%m-%d (%A)')}",
            "",
            "| Source | Topics |",
            "|--------|--------|",
            "| AAAI · NeurIPS · ICML · ICLR · **CVPR** · **KDD** · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview · CVF | Agent · Harness · Finance |",
            "",
            (
                f"**{unique_count} unique papers** "
                f"({total_entries} topic-entries — cross-topic papers counted once per category)"
            ),
            "",
            "---",
            "",
        ]

        if unique_count == 0:
            lines += [
                "> No matching papers found today.",
                "> Try running with `--lookback` set to a larger value.",
                "",
            ]
            lines += self._footer(target_date)
            return "\n".join(lines)

        for topic, papers in categorized.items():
            lines.append(f"## {topic}  ({len(papers)})")
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
                lines.append(f"### {conf}")
                lines.append("")
                for p in by_conf[conf]:
                    lines += self._format_paper(p)
                lines.append("")

        lines += self._footer(target_date)
        return "\n".join(lines)

    # ------------------------------------------------------------------

    def _format_paper(self, p: Paper) -> List[str]:
        title_md = f"[{p.title}]({p.url})" if p.url else p.title

        # Author line (cap at 3 + "et al.")
        authors_str = ""
        if p.authors:
            shown = p.authors[:3]
            authors_str = ", ".join(shown)
            if len(p.authors) > 3:
                authors_str += " et al."

        # Meta badges
        meta: List[str] = []
        if p.conference:
            year = f" {p.year}" if p.year else ""
            meta.append(f"**{p.conference}{year}**")
        if p.source == "huggingface":
            meta.append("🤗 Featured")
        elif p.source == "huggingface_search":
            meta.append("🤗")
        elif p.source == "openreview":
            meta.append("OpenReview")
        elif p.source == "cvf":
            meta.append("CVF")
        if p.published_date:
            meta.append(f"`{p.published_date}`")

        lines = [f"- **{title_md}**"]
        if authors_str:
            lines.append(f"  - *{authors_str}*")
        if meta:
            lines.append(f"  - {' · '.join(meta)}")
        if p.abstract:
            snippet = p.abstract[:280].rstrip()
            if len(p.abstract) > 280:
                snippet += "…"
            lines.append(f"  - {snippet}")
        lines.append("")
        return lines

    def _footer(self, target_date: date) -> List[str]:
        return [
            "---",
            (
                f"*Generated {target_date} · "
                "Sources: HuggingFace Daily Papers, CVF Open Access, OpenReview, Semantic Scholar, arXiv*"
            ),
            "",
        ]
