"""
Markdown formatter for the daily paper digest.
"""
from __future__ import annotations

from collections import Counter
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
}

_ABSTRACT_LEN = 250


class PaperFormatter:
    def format(self, categorized: Dict[str, List[Paper]], target_date: date) -> str:
        lines: List[str] = []

        all_papers = {id(p) for plist in categorized.values() for p in plist}
        unique_count = len(all_papers)
        total_entries = sum(len(v) for v in categorized.values())

        lines += [
            f"# Daily Paper Digest — {target_date.strftime('%Y-%m-%d (%A)')}",
            "",
            "> **Sources**: AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · HuggingFace · OpenReview · arXiv · Semantic Scholar  ",
            "> **Topics**: Agent · Harness · Finance",
            "",
            (
                f"**{unique_count} unique papers** "
                f"({total_entries} topic-entries — a paper covering multiple topics is counted once per category)"
            ),
            "",
        ]

        # --- Summary table: rows = topics, columns = conferences ---
        lines += self._summary_table(categorized)
        lines += ["", "---", ""]

        if unique_count == 0:
            lines += [
                "> No matching papers found today.",
                "> Try running with `--skip-arxiv false` or a wider date range.",
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

            # Group by conference
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

    def _summary_table(self, categorized: Dict[str, List[Paper]]) -> List[str]:
        """Build a compact Markdown table: topics × conferences."""
        confs = _CONF_ORDER + ["Other / arXiv"]

        # count[topic][conf] = n
        counts: Dict[str, Counter] = {}
        for topic, papers in categorized.items():
            c: Counter = Counter()
            for p in papers:
                c[p.conference or "Other / arXiv"] += 1
            counts[topic] = c

        header = "| Topic | " + " | ".join(confs) + " | **Total** |"
        sep    = "|-------|" + "|".join(["-------"] * len(confs)) + "|---------|"
        rows: List[str] = [header, sep]

        for topic, papers in categorized.items():
            c = counts[topic]
            cells = " | ".join(str(c.get(cf, 0)) for cf in confs)
            rows.append(f"| **{topic}** | {cells} | **{len(papers)}** |")

        # Totals row
        totals: Counter = Counter()
        for c in counts.values():
            totals.update(c)
        total_cells = " | ".join(str(totals.get(cf, 0)) for cf in confs)
        grand = sum(totals.values())
        rows.append(f"| *Total* | {total_cells} | *{grand}* |")

        return rows

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
        if p.source == "huggingface":
            meta.append("🤗 Featured")
        elif p.source == "huggingface_search":
            meta.append("🤗")
        elif p.source == "openreview":
            meta.append("OpenReview")
        if p.published_date:
            meta.append(f"`{p.published_date}`")

        lines = [f"- **{title_md}**"]
        if authors_str:
            lines.append(f"  - *{authors_str}*")
        if meta:
            lines.append(f"  - {' · '.join(meta)}")
        if p.abstract:
            snippet = p.abstract[:_ABSTRACT_LEN].rstrip()
            if len(p.abstract) > _ABSTRACT_LEN:
                snippet += "…"
            lines.append(f"  - {snippet}")
        lines.append("")
        return lines

    def _footer(self, target_date: date) -> List[str]:
        return [
            "---",
            (
                f"*Generated {target_date} · "
                "Sources: HuggingFace Daily Papers, OpenReview, Semantic Scholar, arXiv*"
            ),
            "",
        ]
