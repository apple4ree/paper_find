import json
import tempfile
import unittest
from copy import deepcopy
from datetime import date
from pathlib import Path

from scripts.compare_reports import compare
from src.audit import build_audit, change_alert, publication_class
from src.collection import CollectionStats
from src.formatter import PaperFormatter
from src.models import Paper
from src.processor import PaperProcessor, _deduplicate


DAY = date(2026, 10, 10)


def paper(title, aid=None, published=None, year=None, source='arxiv', kind='publication'):
    return Paper(title, url=f'https://arxiv.org/abs/{aid}' if aid else '', arxiv_id=aid,
                 published_date=published, year=year, source=source, date_kind=kind)


def audit(papers, day, directory, sources=None):
    sources = sources or [CollectionStats('arxiv', attempts=[{'query': 'agent', 'status': 'success'}]).summary(papers)]
    categorized = PaperProcessor().process(deepcopy(papers))
    return build_audit(categorized, papers, sources, day, directory)


def save(result, directory):
    (directory / f"{result['date']}.json").write_text(json.dumps(result))


class AuditTests(unittest.TestCase):
    def test_old_new_unknown_future_and_inclusive_boundary(self):
        cases = [
            ({'published_date': '2026-10-08', 'date_kind': 'publication'}, 'recent'),
            ({'published_date': '2026-10-07', 'date_kind': 'publication'}, 'older'),
            ({'published_date': '2026-10-11', 'date_kind': 'publication'}, 'future'),
            ({'published_date': '2026-10-10', 'date_kind': 'record_created'}, 'unknown'),
            ({'published_date': 'invalid', 'date_kind': 'publication'}, 'unknown'),
            ({'year': 2025}, 'older'),
            ({'arxiv_id': '2501.00001', 'published_date': '2026-10-10', 'date_kind': 'publication'}, 'older'),
            ({'arxiv_id': '2610.00001'}, 'unknown'),
            ({'arxiv_id': '2611.00001'}, 'future'),
        ]
        for record, expected in cases:
            with self.subTest(record=record):
                self.assertEqual(publication_class(record, DAY), expected)

    def test_metadata_enrichment_dedups_and_preserves_earliest_date(self):
        papers = [paper('Agent Example', published=date(2025, 1, 1)),
                  paper('  agent example ', '2501.00001v2', date(2026, 10, 10), source='openreview', kind='record_created')]
        merged = _deduplicate(papers)
        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0].get_id(), 'arxiv:2501.00001')
        self.assertEqual(merged[0].published_date, date(2025, 1, 1))
        self.assertEqual(merged[0].sources, ['arxiv', 'openreview'])

    def test_added_existing_missing_and_first_seen_are_different(self):
        with tempfile.TemporaryDirectory() as td:
            directory = Path(td)
            older = paper('Agent returning', '2501.00001', date(2025, 1, 1))
            existing = paper('Agent existing', '2610.00002', date(2026, 10, 8))
            missing = paper('Agent missing', '2610.00003', date(2026, 10, 8))
            save(audit([older], date(2026, 10, 8), directory), directory)
            save(audit([existing, missing], date(2026, 10, 9), directory), directory)
            recent = paper('Agent newly published', '2610.00004', date(2026, 10, 10))
            archive = paper('Agent old discovery', '2501.00005', date(2025, 1, 1))
            unknown = paper('Agent unknown discovery', '2610.00006')
            result = audit([existing, older, recent, archive, unknown], DAY, directory)
            c = result['changes']
            self.assertEqual(c['existing'], [existing.get_id()])
            self.assertEqual(len(c['added']), 4)
            self.assertEqual(c['missing'], [missing.get_id()])
            self.assertNotIn(older.get_id(), c['newly_discovered'])
            self.assertEqual(c['newly_discovered_recent'], [recent.get_id()])
            self.assertEqual(c['newly_discovered_older'], [archive.get_id()])
            self.assertEqual(c['newly_discovered_unknown'], [unknown.get_id()])
            save(result, directory)
            self.assertEqual(audit([existing, older, recent, archive, unknown], DAY, directory), result)

    def test_identity_survives_title_only_to_arxiv_and_future_backfill(self):
        with tempfile.TemporaryDirectory() as td:
            directory = Path(td)
            old = paper('Agent Example', published=date(2026, 10, 8))
            save(audit([old], date(2026, 10, 9), directory), directory)
            # A future snapshot must never seed a historical first-seen date.
            save(audit([paper('Agent Future', '2610.00009')], date(2026, 10, 12), directory), directory)
            enriched = paper('agent example', '2610.00001v2', date(2026, 10, 8))
            result = audit([enriched], DAY, directory)
            self.assertEqual(result['changes']['existing'], [enriched.get_id()])
            self.assertEqual(result['changes']['newly_discovered'], [])
            self.assertEqual(result['changes']['missing'], [])

    def test_no_yesterday_is_not_a_zero_baseline(self):
        with tempfile.TemporaryDirectory() as td:
            directory = Path(td)
            save(audit([paper('Agent earlier')], date(2026, 10, 8), directory), directory)
            result = audit([paper('Agent now')], DAY, directory)
            self.assertEqual(result['baseline']['kind'], 'unavailable')
            self.assertIsNone(result['changes_url'])
            self.assertEqual(result['changes']['added'], [])
            self.assertEqual(result['changes']['missing'], [])

    def test_all_sources_and_recent_evidence_are_preserved(self):
        with tempfile.TemporaryDirectory() as td:
            papers = [paper('Agent Example', '2501.00001', date(2025, 1, 1)),
                      paper('Agent Example', published=date(2026, 10, 10), source='openreview', kind='record_created')]
            result = audit(papers, DAY, Path(td))
            r = result['papers'][0]
            self.assertEqual(r['publication_class'], 'older')
            self.assertEqual(r['sources'], ['arxiv', 'openreview'])
            self.assertEqual(len(r['date_evidence']), 2)
            formatted = PaperFormatter().format(PaperProcessor().process(deepcopy(papers)), DAY, result)
            self.assertIn('publication: older', formatted)
            self.assertIn('Collection audit', formatted)

    def test_drop_spike_partial_skip_and_context_change(self):
        self.assertEqual(change_alert('total', 647, 284)[0]['kind'], 'count_drop')
        self.assertEqual(change_alert('total', 20, 40)[0]['kind'], 'count_spike')
        self.assertEqual(change_alert('total', 2, 0), [])
        self.assertEqual(change_alert('total', 0, 100), [])
        with tempfile.TemporaryDirectory() as td:
            directory = Path(td)
            prior = CollectionStats('arxiv', attempts=[{'query': 'one', 'status': 'success'}])
            papers = [paper(f'Agent {i}') for i in range(30)]
            save(audit(papers, date(2026, 10, 9), directory, [prior.summary(papers)]), directory)
            failed = CollectionStats('arxiv', attempts=[{'query': 'one', 'status': 'failed'}], context={'start_date': '2026-10-09'})
            result = audit([], DAY, directory, [failed.summary()])
            self.assertFalse(result['complete'])
            self.assertTrue(any(a['kind'] == 'collection_incomplete' for a in result['alerts']))
            notice = next(a for a in result['alerts'] if a.get('scope') == 'arxiv' and a['kind'] == 'count_drop')
            self.assertTrue(notice['search_context_changed'])
            self.assertEqual(notice['cause'], 'undetermined')
            skipped = CollectionStats('arxiv', skipped=True).summary()
            result = audit([], DAY, directory, [skipped])
            self.assertFalse(any(a.get('scope') == 'arxiv' for a in result['alerts']))

    def test_real_october_reports_exact_url_regression(self):
        root = Path(__file__).resolve().parents[1] / 'output'
        result = compare(root / '2026-10-09.md', root / '2026-10-10.md')
        self.assertEqual((result['before'], result['after']), (647, 284))
        self.assertEqual((len(result['existing']), len(result['added']), len(result['missing'])), (203, 81, 444))

    def test_huggingface_report_count_includes_search_channel(self):
        with tempfile.TemporaryDirectory() as td:
            p = paper('Agent Search', '2610.00001', source='huggingface_search')
            source = CollectionStats('huggingface', attempts=[{'query': 'search', 'status': 'success'}]).summary([p])
            result = audit([p], DAY, Path(td), [source])
            self.assertEqual(result['sources'][0]['report_unique'], 1)

    def test_high_turnover_detected_even_with_stable_total(self):
        with tempfile.TemporaryDirectory() as td:
            directory = Path(td)
            old = [paper(f'Agent old {i}') for i in range(20)]
            save(audit(old, date(2026, 10, 9), directory), directory)
            new = [paper(f'Agent new {i}') for i in range(20)]
            result = audit(new, DAY, directory)
            self.assertTrue(any(a['kind'] == 'high_disappearance' for a in result['alerts']))
            self.assertFalse(any(a['kind'] == 'count_drop' for a in result['alerts']))
