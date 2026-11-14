#!/usr/bin/env python3
"""Offline URL comparison of historical reports; does not infer failures."""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.audit import read_legacy_report


def compare(before, after):
    old = {p['url']: p for p in read_legacy_report(Path(before))}
    new = {p['url']: p for p in read_legacy_report(Path(after))}
    return {
        'before': len(old), 'after': len(new), 'identity_basis': 'exact_url',
        'existing': sorted(old.keys() & new.keys()),
        'added': [new[u] for u in sorted(new.keys() - old.keys())],
        'missing': [old[u] for u in sorted(old.keys() - new.keys())],
        'cause': 'not_inferable_from_reports_alone',
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('before')
    parser.add_argument('after')
    args = parser.parse_args()
    print(json.dumps(compare(args.before, args.after), ensure_ascii=False, indent=2))
