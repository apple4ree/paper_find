"""
Markdown formatter for the daily paper digest.
"""
from __future__ import annotations

from datetime import date
from typing import Dict, List

from .models import Paper

# The six mandatory conferences are always shown first.
MANDATORY_CONFS = ["AAAI", "NeurIPS", "ICML", "ICLR", "CVPR", "KDD"]

_SOURCE_BADGE = {
    "huggingface":        "🤗 HF Featured",
    "huggingface_search": "🤗 HF",
    "openreview":         "OpenReview",
    "cvf":                "CVF",
    "arxiv":              "arXiv",
    "semantic_scholar":   "S2",
}


class PaperFormatter:
    def format(self, categorized: Dict[str, List[Paper]], target_date: date) -> str:
        lines: List[str] = []

        unique_papers = {id(p) for plist in categorized.values() for p in plist}
        unique_count = len(unique_papers)
        total_entries = sum(len(v) for v in categorized.values())

        lines += [
            f"# Daily Paper Digest — {target_date.strftime('%Y-%m-%d (%A)')}",
            "",
            "| Mandatory Conferences | Additional Sources | Topics |",
            "|---|---|---|",
            "| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD | HuggingFace · OpenReview · arXiv · Semantic Scholar · CVF | Agent · Harness · Finance |",
            "",
            (
                f"**{unique_count} unique papers** "
                f"({total_entries} topic-entries — cross-topic papers counted once per category)"
            ),
            "",
        ]

        # Per-conference breakdown table
        conf_stats = self._conference_stats(categorized)
        if unique_count > 0:
            lines += self._conf_table(conf_stats)

        lines += ["---", ""]

        if unique_count == 0:
            lines += [
                "> No matching papers found today.",
                "> Try running with a wider date range or check network access.",
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

            # Group by conference; mandatory ones first, then alphabetical
            by_conf: Dict[str, List[Paper]] = {}
            for p in papers:
                key = p.conference or "Other / arXiv"
                by_conf.setdefault(key, []).append(p)

            ordered_confs = (
                MANDATORY_CONFS
                + sorted(k for k in by_conf if k not in MANDATORY_CONFS)
            )

            for conf in ordered_confs:
                if conf not in by_conf:
                    continue
                badge = self._conf_badge(conf)
                lines.append(f"### {badge}")
                lines.append("")
                for p in by_conf[conf]:
                    lines += self._format_paper(p)
                lines.append("")

        lines += self._footer(target_date)
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Conference summary table
    # ------------------------------------------------------------------

    def _conference_stats(
        self, categorized: Dict[str, List[Paper]]
    ) -> Dict[str, Dict[str, int]]:
        """Return {conf: {topic: count}} for the summary table."""
        stats: Dict[str, Dict[str, int]] = {}
        for topic, papers in categorized.items():
            for p in papers:
                conf = p.conference or "Other"
                stats.setdefault(conf, {}).setdefault(topic, 0)
                stats[conf][topic] += 1
        return stats

    def _conf_table(self, stats: Dict[str, Dict[str, int]]) -> List[str]:
        topics = ["Agent", "Harness", "Finance"]
        lines = [
            "| Conference | Agent | Harness | Finance | Total |",
            "|---|---|---|---|---|",
        ]
        all_confs = MANDATORY_CONFS + sorted(
            c for c in stats if c not in MANDATORY_CONFS
        )
        for conf in all_confs:
            counts = stats.get(conf, {})
            a = counts.get("Agent", 0)
            h = counts.get("Harness", 0)
            f = counts.get("Finance", 0)
            total = a + h + f
            if total == 0 and conf not in MANDATORY_CONFS:
                continue
            a_s = str(a) if a else "—"
            h_s = str(h) if h else "—"
            f_s = str(f) if f else "—"
            t_s = str(total) if total else "—"
            lines.append(f"| **{conf}** | {a_s} | {h_s} | {f_s} | {t_s} |")
        lines.append("")
        return lines

    # ------------------------------------------------------------------

    def _conf_badge(self, conf: str) -> str:
        if conf in MANDATORY_CONFS:
            return conf
        return conf

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
        src_badge = _SOURCE_BADGE.get(p.source, p.source)
        if src_badge:
            meta.append(src_badge)
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
                "Sources: HuggingFace Daily Papers, OpenReview (ICLR/NeurIPS/ICML/AAAI), "
                "CVF Open Access (CVPR), Semantic Scholar, arXiv*"
            ),
            "",
        ]
