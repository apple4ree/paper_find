"""
Markdown formatter for the daily paper digest.
"""
from __future__ import annotations

from collections import Counter
from datetime import date
from typing import Dict, List

from .models import Paper

_CONF_ORDER = ["AAAI", "NeurIPS", "ICML", "ICLR", "CVPR", "KDD"]

_SOURCE_LABEL = {
    "huggingface":        "🤗 HuggingFace Featured",
    "huggingface_search": "🤗 HuggingFace",
    "openreview":         "OpenReview",
    "arxiv":              "arXiv",
    "semantic_scholar":   "Semantic Scholar",
}


class PaperFormatter:
    def format(self, categorized: Dict[str, List[Paper]], target_date: date) -> str:
        lines: List[str] = []

        unique_ids   = {id(p) for plist in categorized.values() for p in plist}
        unique_count = len(unique_ids)
        total_entries = sum(len(v) for v in categorized.values())

        # Source breakdown
        source_ctr: Counter = Counter()
        all_seen: set[int] = set()
        for plist in categorized.values():
            for p in plist:
                oid = id(p)
                if oid not in all_seen:
                    all_seen.add(oid)
                    source_ctr[p.source] += 1

        # Conference breakdown
        conf_ctr: Counter = Counter()
        all_seen2: set[int] = set()
        for plist in categorized.values():
            for p in plist:
                oid = id(p)
                if oid not in all_seen2:
                    all_seen2.add(oid)
                    conf_ctr[p.conference or "Other/arXiv"] += 1

        # KST date string  (UTC+9)
        kst_str = target_date.strftime("%Y-%m-%d (%A) KST")

        lines += [
            f"# Daily Paper Digest — {kst_str}",
            "",
            "| 대상 학회 | 주제 |",
            "|-----------|------|",
            "| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD + HuggingFace | Agent · Harness · Finance |",
            "",
            f"**총 {unique_count}편** "
            f"(토픽 항목 합계 {total_entries} — 복수 토픽 논문은 각 항목에 중복 표시, 논문 자체는 중복 제거됨)",
            "",
        ]

        # Source summary table
        lines += ["<details><summary>소스별 수집 현황</summary>", ""]
        lines += ["| 소스 | 논문 수 |", "|------|------:|"]
        for src, cnt in sorted(source_ctr.items(), key=lambda x: -x[1]):
            label = _SOURCE_LABEL.get(src, src)
            lines.append(f"| {label} | {cnt} |")
        lines += ["", "</details>", "", "---", ""]

        if unique_count == 0:
            lines += [
                "> 오늘 매칭되는 논문이 없습니다.",
                "> 네트워크 접근을 확인하거나 `--lookback` 값을 늘려보세요.",
                "",
            ]
            lines += self._footer(target_date)
            return "\n".join(lines)

        for topic, papers in categorized.items():
            lines.append(f"## {topic}  ({len(papers)}편)")
            lines.append("")

            if not papers:
                lines += ["*이 주제에 해당하는 논문이 없습니다.*", ""]
                continue

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
            f"*생성일: {target_date} · "
            "수집 소스: HuggingFace Daily Papers, OpenReview (ICLR/NeurIPS/ICML), "
            "Semantic Scholar, arXiv · "
            "중복 제거 기준: arXiv ID 우선, 없으면 정규화된 제목*",
            "",
        ]
