"""
Markdown formatter for the daily paper digest.
"""
from __future__ import annotations

from datetime import date
from typing import Dict, List

from .models import Paper

# Tier-1 conferences displayed first, in this order
_CONF_ORDER = ["AAAI", "NeurIPS", "ICML", "ICLR", "CVPR", "KDD"]

# Label shown for papers not attributed to a specific conference
_OTHER_LABEL = "Other / arXiv"


class PaperFormatter:
    def format(self, categorized: Dict[str, List[Paper]], target_date: date) -> str:
        lines: List[str] = []

        unique_papers = {id(p) for plist in categorized.values() for p in plist}
        unique_count = len(unique_papers)
        total_entries = sum(len(v) for v in categorized.values())

        # Per-conference counts across all topics (for header table)
        conf_counts: Dict[str, int] = {}
        all_papers_seen: Dict[int, Paper] = {}
        for plist in categorized.values():
            for p in plist:
                pid = id(p)
                if pid not in all_papers_seen:
                    all_papers_seen[pid] = p
                    key = p.conference or _OTHER_LABEL
                    conf_counts[key] = conf_counts.get(key, 0) + 1

        lines += [
            f"# Daily Paper Digest — {target_date.strftime('%Y-%m-%d (%A)')}",
            "",
            "**Venues:** AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview",
            "",
            "**Topics:** Agent · Harness · Finance",
            "",
        ]

        # Conference breakdown table
        if conf_counts:
            lines += ["| Conference | Papers |", "|:-----------|-------:|"]
            for conf in _CONF_ORDER:
                if conf in conf_counts:
                    lines.append(f"| {conf} | {conf_counts[conf]} |")
            for conf in sorted(conf_counts):
                if conf not in _CONF_ORDER:
                    lines.append(f"| {conf} | {conf_counts[conf]} |")
            lines += [
                f"| **Total unique** | **{unique_count}** |",
                "",
            ]

        lines += [
            (
                f"> {unique_count} unique papers · "
                f"{total_entries} topic-entries "
                f"(a paper in multiple topics is counted once per topic)"
            ),
            "",
            "---",
            "",
        ]

        if unique_count == 0:
            lines += [
                "> No matching papers found today.",
                "> Check network access or try a wider date range.",
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

            # Group by conference
            by_conf: Dict[str, List[Paper]] = {}
            for p in papers:
                key = p.conference or _OTHER_LABEL
                by_conf.setdefault(key, []).append(p)

            # Tier-1 conferences first, then others alphabetically, Other at end
            others = sorted(
                k for k in by_conf
                if k not in _CONF_ORDER and k != _OTHER_LABEL
            )
            ordered_confs = (
                [c for c in _CONF_ORDER if c in by_conf]
                + others
                + ([_OTHER_LABEL] if _OTHER_LABEL in by_conf else [])
            )

            for conf in ordered_confs:
                conf_papers = by_conf[conf]
                lines.append(f"### {conf}  ({len(conf_papers)})")
                lines.append("")
                for p in conf_papers:
                    lines += self._format_paper(p)

        lines += self._footer(target_date)
        return "\n".join(lines)

    # ------------------------------------------------------------------

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
                "Sources: HuggingFace Daily Papers, OpenReview (ICLR/NeurIPS/ICML), "
                "Semantic Scholar, arXiv*"
            ),
            "",
        ]
