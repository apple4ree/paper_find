"""Deterministic history, publication classification and change alerts.

Snapshots include collected papers even when topic filtering excludes them.
Old Markdown reports are an explicitly incomplete bootstrap, not raw evidence.
"""
from __future__ import annotations

import json
import re
from dataclasses import asdict
from datetime import date, timedelta
from pathlib import Path

from .config import LOOKBACK_DAYS
from .identity import aliases, identity_groups


def read_legacy_report(path: Path) -> list[dict]:
    records = []
    current = None
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^- \*\*\[(.+)\]\((.+)\)\*\*", line)
        if match:
            current = {"title": match[1], "url": match[2], "date_kind": "unknown"}
            records.append(current)
        elif current and line.startswith("  - "):
            pub = re.search(r"`(\d{4}-\d{2}-\d{2})`", line)
            if pub:
                current["published_date"] = pub[1]
            year = re.search(r"\*\*[^*]+ (20\d{2})\*\*", line)
            if year:
                current["year"] = int(year[1])
    # A paper may occur in multiple topic buckets.
    seen = {}
    for record in records:
        seen.setdefault(record["url"], record)
    return list(seen.values())


def publication_class(record: dict, target: date, lookback: int = LOOKBACK_DAYS) -> str:
    if lookback < 1:
        raise ValueError("lookback must be positive")
    start = target - timedelta(days=lookback - 1)
    # A prior-year conference or old arXiv month cannot become a new paper
    # through a new conference publication/curation date.
    year = record.get("year")
    if year and int(year) < start.year:
        return "older"
    for key in aliases(record):
        if key.startswith("arxiv:"):
            aid = key.split(":", 1)[1]
            if re.match(r"\d{4}\.\d{4,5}$", aid):
                month = (2000 + int(aid[:2]), int(aid[2:4]))
                if month < (start.year, start.month):
                    return "older"
                if month > (target.year, target.month):
                    return "future"
    raw = record.get("published_date")
    if not raw or record.get("date_kind") not in ("publication", "submission"):
        return "unknown"
    try:
        pub = date.fromisoformat(str(raw))
    except ValueError:
        return "unknown"
    if pub > target:
        return "future"
    return "recent" if pub >= start else "older"


def change_alert(label, before, after, min_baseline=20, drop_ratio=0.5, spike_ratio=2.0):
    if before < min_baseline:
        return []
    ratio = after / before
    if ratio <= drop_ratio or ratio >= spike_ratio:
        return [{"kind": "count_drop" if ratio <= drop_ratio else "count_spike",
                 "scope": label, "before": before, "after": after,
                 "ratio": round(ratio, 4), "cause": "undetermined"}]
    return []


def build_audit(categorized, raw_papers, source_runs, target: date, output_dir: Path,
                min_baseline=20, drop_ratio=0.5, spike_ratio=2.0):
    raw = [asdict(p) for p in raw_papers]
    for record in raw:
        if record["published_date"]:
            record["published_date"] = str(record["published_date"])
    selected = {p.get_id() for bucket in categorized.values() for p in bucket}
    today = []
    for group in identity_groups(raw):
        record = dict(raw[group[0]])
        group_keys = set().union(*(aliases(raw[i]) for i in group))
        record["aliases"] = sorted(group_keys)
        record["id"] = next((k for prefix in ("arxiv:", "doi:", "openreview:", "title:", "url:")
                             for k in sorted(group_keys) if k.startswith(prefix)), "")
        record["sources"] = sorted({s for i in group for s in (raw[i].get("sources") or [raw[i]["source"]]) if s})
        record["in_report"] = bool(group_keys & selected)
        evidence = [raw[i] for i in group]
        classes = {publication_class(r, target) for r in evidence}
        # Any older evidence wins over a newer conference/record timestamp.
        record["publication_class"] = ("older" if "older" in classes else
                                       "recent" if "recent" in classes else
                                       "future" if "future" in classes else "unknown")
        record["date_evidence"] = [{"source": r["source"], "date": r.get("published_date"),
                                    "kind": r.get("date_kind"), "year": r.get("year")} for r in evidence]
        today.append(record)

    past = []
    previous = None
    baseline_kind = "unavailable"
    # Only earlier report dates count: reruns and backfills are deterministic,
    # and never compare a historical target to a future latest.md.
    historical_dates = sorted({p.stem for pattern in ("*.md", "*.json")
                               for p in output_dir.glob(pattern)
                               if re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.stem) and p.stem < str(target)})
    for day in historical_dates:
        snapshot = output_dir / f"{day}.json"
        md = output_dir / f"{day}.md"
        if snapshot.exists():
            saved = json.loads(snapshot.read_text(encoding="utf-8"))
            records = saved["papers"]
            kind = "snapshot"
        else:
            records = read_legacy_report(md)
            saved = {"papers": records, "sources": []}
            kind = "legacy_report"
        for record in records:
            past.append({**record, "observed_on": day})
        if day == str(target - timedelta(days=1)):
            previous, baseline_kind = saved, kind

    combined = past + today
    groups = identity_groups(combined)
    component_keys = {}
    first_seen = {}
    previous_keys = set()
    previous_records = [] if previous is None else [r for r in previous["papers"] if r.get("in_report", True)]
    previous_urls = {r.get("url") for r in previous_records if r.get("url")}
    normalized_previous = []
    for group in identity_groups(previous_records):
        merged = dict(previous_records[group[0]])
        merged["aliases"] = sorted(set().union(*(set(previous_records[i].get("aliases") or aliases(previous_records[i])) for i in group)))
        merged["id"] = next(k for prefix in ("arxiv:", "doi:", "openreview:", "title:", "url:")
                            for k in merged["aliases"] if k.startswith(prefix))
        normalized_previous.append(merged)
    previous_records = normalized_previous
    for r in previous_records:
        previous_keys.update(r.get("aliases") or aliases(r))
    current_keys = set()
    for group in groups:
        keys = set().union(*(set(combined[i].get("aliases") or aliases(combined[i])) for i in group))
        for i in group:
            component_keys[i] = keys
        historical = [combined[i]["observed_on"] for i in group if i < len(past)]
        first = min(historical) if historical else str(target)
        for key in keys:
            first_seen[key] = first
        for i in group:
            if i >= len(past) and combined[i]["in_report"]:
                current_keys.update(keys)

    changes = {"added": [], "existing": [], "missing": [], "newly_discovered": [],
               "newly_discovered_recent": [], "newly_discovered_older": [], "newly_discovered_unknown": []}
    for i, record in enumerate(today, start=len(past)):
        record["first_seen"] = min(first_seen[k] for k in record["aliases"])
        if not record["in_report"]:
            continue
        if previous is not None:
            # Expand aliases through all historical records before matching.
            keys = component_keys[i]
            changes["existing" if keys & previous_keys else "added"].append(record["id"])
        if record["first_seen"] == str(target):
            changes["newly_discovered"].append(record["id"])
            cls = record["publication_class"]
            bucket = "unknown" if cls == "future" else cls
            changes[f"newly_discovered_{bucket}"].append(record["id"])
    for r in previous_records:
        if not set(r.get("aliases") or aliases(r)) & current_keys:
            changes["missing"].append(r.get("id") or sorted(aliases(r))[0])
    current_urls = {r["url"] for r in today if r["in_report"] and r.get("url")}
    changes_url = None if previous is None else {
        "added": sorted(current_urls - previous_urls),
        "existing": sorted(current_urls & previous_urls),
        "missing": sorted(previous_urls - current_urls),
    }
    for source in source_runs:
        channels = {source["source"]}
        if source["source"] == "huggingface":
            channels.add("huggingface_search")
        source["report_unique"] = sum(r["in_report"] and bool(channels & set(r["sources"])) for r in today)

    alerts = []
    if previous is not None:
        alerts += change_alert("report_unique", len(previous_records), len(selected), min_baseline, drop_ratio, spike_ratio)
        if len(previous_records) >= min_baseline and len(changes["missing"]) / len(previous_records) >= 0.5:
            alerts.append({"kind": "high_disappearance", "scope": "report_unique",
                           "missing": len(changes["missing"]), "baseline": len(previous_records),
                           "cause": "undetermined"})
    prior_sources = {s["source"]: s for s in (previous or {}).get("sources", [])}
    for source in source_runs:
        if source["status"] in ("partial", "failed", "unknown"):
            alerts.append({"kind": "collection_incomplete", "scope": source["source"], "status": source["status"]})
        if any(a.get("possibly_truncated") for a in source["attempts"]):
            alerts.append({"kind": "result_cap_reached", "scope": source["source"], "cause": "undetermined"})
        prior = prior_sources.get(source["source"])
        if prior and source["status"] != "skipped" and prior["status"] != "skipped":
            notices = change_alert(source["source"], prior["collected_unique"], source["collected_unique"], min_baseline, drop_ratio, spike_ratio)
            for notice in notices:
                notice["search_context_changed"] = prior["context"] != source["context"]
            alerts += notices
    return {"schema_version": 1, "date": str(target), "lookback_days": LOOKBACK_DAYS,
            "publication_window": {"start": str(target - timedelta(days=LOOKBACK_DAYS - 1)), "end": str(target)},
            "baseline": {"date": str(target - timedelta(days=1)), "kind": baseline_kind,
                         "unique_identity": len(previous_records) if previous is not None else None,
                         "unique_url": len(previous_urls) if previous is not None else None},
            "history_kind": "snapshots_and_legacy_reports" if historical_dates else "cold_start",
            "complete": all(s["status"] in ("success", "skipped") for s in source_runs),
            "report_unique": len(selected), "sources": source_runs, "changes": changes,
            "changes_url": changes_url, "alerts": alerts, "papers": today}


def audit_markdown(audit):
    lines = ["## Collection audit", "",
             "Counts describe search observations, not the number of newly published papers.", "",
             "| Source | Status | Successful / failed queries | Request failures | Collected unique | In report |",
             "|---|---|---:|---:|---:|---:|"]
    for s in audit["sources"]:
        lines.append(f"| {s['source']} | {s['status']} | {s['queries_succeeded']} / {s['queries_failed']} | {s['request_failures']} | {s['collected_unique']} | {s['report_unique']} |")
    for s in audit["sources"]:
        if s["context"].get("effective_daily_date"):
            lines.append(f"\nHuggingFace curated-list date: {s['context']['effective_daily_date']} (requested {audit['date']}).\n")
    c = audit["changes"]
    lines += ["", f"Previous-day baseline: **{audit['baseline']['kind']}**.",
              f"Added to report: **{len(c['added'])}** · existing: **{len(c['existing'])}** · absent today: **{len(c['missing'])}**.",
              "Absent today means not returned/selected; it does not mean deleted or invalid.",
              "Source report counts overlap when multiple sources return the same paper.",
              f"First observed in available history: **{len(c['newly_discovered'])}**; recent publication: **{len(c['newly_discovered_recent'])}**, older: **{len(c['newly_discovered_older'])}**, unverified/future date: **{len(c['newly_discovered_unknown'])}**.",
              f"Recent publication window (inclusive): {audit['publication_window']['start']} to {audit['publication_window']['end']}.",
              "Legacy reports omit filtered-out papers and request evidence; first-seen history is incomplete.", ""]
    for alert in audit["alerts"]:
        lines.append(f"- Alert: `{alert['scope']}` / `{alert['kind']}`" +
                     (f" ({alert['before']} → {alert['after']}; cause undetermined)" if "before" in alert else ""))
    lines += ["", f"Full query outcomes and paper-level changes: [{audit['date']}.json]({audit['date']}.json)", ""]
    return "\n".join(lines)
