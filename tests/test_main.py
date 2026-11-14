import json
import tempfile
import unittest
from contextlib import redirect_stdout
from datetime import date
from io import StringIO
from pathlib import Path
from unittest.mock import patch

import main
from src.collection import CollectionStats
from src.models import Paper


class PipelineTests(unittest.TestCase):
    def run_pipeline(self, directory, scraper, extra=()):
        argv = ['main.py', '--date', '2026-10-10', '--output-dir', str(directory),
                '--skip-s2', '--skip-arxiv', '--skip-openreview', *extra]
        with patch('sys.argv', argv), patch('src.scrapers.huggingface.HuggingFaceScraper', return_value=scraper), redirect_stdout(StringIO()):
            return main.main()

    def test_partial_strict_saves_report_and_diagnostics_before_exit(self):
        class Scraper:
            stats = CollectionStats('huggingface', attempts=[{'query': 'daily', 'status': 'success'}, {'query': 'search', 'status': 'failed'}])
            def fetch(self, day):
                return [Paper('Agent Example', source='huggingface', published_date=day)]
        with tempfile.TemporaryDirectory() as td:
            directory = Path(td)
            self.assertEqual(self.run_pipeline(directory, Scraper(), ['--strict']), 2)
            saved = json.loads((directory / '2026-10-10.json').read_text())
            self.assertFalse(saved['complete'])
            self.assertEqual(saved['sources'][0]['status'], 'partial')
            self.assertEqual(saved['sources'][1]['status'], 'skipped')
            self.assertTrue((directory / '2026-10-10.md').exists())

    def test_total_failure_preserves_latest_and_writes_diagnostics(self):
        class Scraper:
            stats = CollectionStats('huggingface')
            def fetch(self, day):
                raise RuntimeError('credential-bearing exception')
        with tempfile.TemporaryDirectory() as td:
            directory = Path(td)
            (directory / 'latest.md').write_text('preserved')
            self.assertEqual(self.run_pipeline(directory, Scraper()), 2)
            self.assertEqual((directory / 'latest.md').read_text(), 'preserved')
            saved = (directory / '2026-10-10.json').read_text()
            self.assertNotIn('credential-bearing', saved)
            self.assertEqual(json.loads(saved)['sources'][0]['status'], 'failed')

    def test_backfill_does_not_replace_latest(self):
        class Scraper:
            stats = CollectionStats('huggingface', attempts=[{'query': 'daily', 'status': 'success'}])
            def fetch(self, day):
                return [Paper('Agent Example', source='huggingface', published_date=day)]
        with tempfile.TemporaryDirectory() as td:
            directory = Path(td)
            (directory / '2026-10-11.md').write_text('newer')
            (directory / 'latest.md').write_text('preserved')
            self.assertEqual(self.run_pipeline(directory, Scraper()), 0)
            self.assertEqual((directory / 'latest.md').read_text(), 'preserved')
