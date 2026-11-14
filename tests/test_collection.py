import unittest
from datetime import date
from unittest.mock import Mock, patch

import requests

from src.collection import CollectionStats, observed_query
from src.scrapers.arxiv import ArxivScraper, _parse_arxiv_xml, _arxiv_date_range
from src.scrapers.huggingface import HuggingFaceScraper
from src.scrapers.openreview import OpenReviewScraper, _parse_note
from src.scrapers.semantic_scholar import SemanticScholarScraper


def http_error(code):
    response = requests.Response()
    response.status_code = code
    return requests.HTTPError('private credentials must not be serialized', response=response)


class CollectionTests(unittest.TestCase):
    def test_zero_success_and_recovered_retry(self):
        class Scraper:
            stats = CollectionStats('test')
            failures = 1
            @observed_query
            def query(self, term):
                if self.failures:
                    self.failures -= 1
                    raise http_error(429)
                return []
        s = Scraper()
        with self.assertRaises(requests.HTTPError):
            s.query('agent')
        s.query('agent')
        result = s.stats.summary()
        self.assertEqual(result['status'], 'success')
        self.assertEqual(result['queries_succeeded'], 1)
        self.assertEqual(result['request_failures'], 1)
        self.assertEqual(result['attempts'][0]['http_status'], 429)
        self.assertNotIn('private', str(result))

    @patch('src.scrapers.huggingface.time.sleep')
    def test_hf_fallback_and_search_failure_visible(self, sleep):
        session = Mock()
        empty, daily, failure = Mock(), Mock(), Mock()
        empty.json.return_value = []
        daily.json.return_value = [{'paper': {'title': 'Agent paper', 'id': '2610.00001'}}]
        failure.raise_for_status.side_effect = http_error(503)
        session.get.side_effect = [empty, daily, failure]
        with patch('src.scrapers.huggingface.HF_TOPIC_QUERIES', {'Agent': ['agent']}):
            s = HuggingFaceScraper(session)
            papers = s.fetch(date(2026, 10, 10))
        result = s.stats.summary(papers)
        self.assertEqual(result['status'], 'partial')
        self.assertEqual(result['queries_failed'], 1)
        self.assertEqual(result['context']['effective_daily_date'], '2026-10-09')
        self.assertEqual(result['collected_unique'], 1)

    def test_hf_curation_date_is_not_publication(self):
        paper = HuggingFaceScraper(Mock())._parse_item({
            'publishedAt': '2026-10-10', 'paper': {'id': '2501.00001', 'title': 'Agent'}})
        self.assertIsNone(paper.published_date)

    @patch('src.scrapers.semantic_scholar.time.sleep')
    def test_s2_retry_and_partial_results(self, sleep):
        session = Mock()
        fail, success = Mock(), Mock()
        fail.raise_for_status.side_effect = http_error(429)
        success.json.return_value = {'data': [{'title': 'agent paper', 'venue': 'ICLR',
                                              'externalIds': {'ArXiv': '2501.00001'}}]}
        session.get.side_effect = [fail, success, fail, fail]
        with patch('src.scrapers.semantic_scholar.TOPIC_SEARCH_TERMS', {'Agent': ['one', 'two']}):
            s = SemanticScholarScraper(session=session)
            papers = s.fetch(date(2024, 1, 2))
        result = s.stats.summary(papers)
        self.assertEqual(result['status'], 'partial')
        self.assertEqual(result['queries_succeeded'], 1)
        self.assertEqual(result['queries_failed'], 1)
        self.assertEqual(result['request_failures'], 3)
        self.assertEqual(result['context']['year_range'], '2023-2024')

    @patch('src.scrapers.arxiv.time.sleep')
    def test_arxiv_failure_is_not_zero_success(self, sleep):
        session = Mock()
        session.get.side_effect = requests.Timeout('secret')
        with patch('src.scrapers.arxiv.TOPIC_SEARCH_TERMS', {'Agent': ['agent']}), \
             patch('src.scrapers.arxiv.TOPIC_CATEGORIES', {'Agent': ['cs.AI']}):
            s = ArxivScraper(session)
            self.assertEqual(s.fetch(date(2026, 10, 10)), [])
        self.assertEqual(s.stats.summary()['status'], 'failed')

    def test_arxiv_bad_xml_and_error_feed_raise(self):
        with self.assertRaises(Exception):
            _parse_arxiv_xml('not xml')
        with self.assertRaises(ValueError):
            _parse_arxiv_xml('<feed xmlns="http://www.w3.org/2005/Atom"><entry><id>http://arxiv.org/api/errors</id></entry></feed>')
        self.assertEqual(_parse_arxiv_xml('<feed xmlns="http://www.w3.org/2005/Atom"/>'), [])

    def test_weekend_window_does_not_shrink(self):
        self.assertEqual(_arxiv_date_range(date(2026, 10, 9))[0], date(2026, 10, 7))
        self.assertEqual(_arxiv_date_range(date(2026, 10, 10))[0], date(2026, 10, 8))
        self.assertEqual(_arxiv_date_range(date(2026, 10, 11))[0], date(2026, 10, 9))
        self.assertEqual(_arxiv_date_range(date(2026, 10, 12))[0], date(2026, 10, 9))

    @patch('src.scrapers.openreview.time.sleep')
    def test_openreview_target_year_and_truncation(self, sleep):
        response, session = Mock(), Mock()
        response.json.return_value = {'notes': [{'id': str(i), 'content': {'title': f'agent {i}'}} for i in range(25)]}
        session.get.return_value = response
        with patch('src.scrapers.openreview.TOPIC_QUERIES', {'Agent': ['agent']}):
            s = OpenReviewScraper(session)
            s.fetch(date(2024, 1, 2))
        self.assertEqual(s.stats.context['venues']['ICLR'][0], 'ICLR.cc/2024/Conference')
        self.assertTrue(s.stats.attempts[0]['possibly_truncated'])

    def test_openreview_modification_date_not_publication(self):
        p = _parse_note({'id': 'x', 'mdate': 1791590400000,
                         'content': {'title': 'Agent'}}, 'ICLR', 2026)
        self.assertIsNone(p.published_date)
        self.assertEqual(p.date_kind, 'record_created')
