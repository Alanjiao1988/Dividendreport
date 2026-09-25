import copy
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from render_index import rendered_files
from validate_archive import contains_value, validate_archive, validate_entries


class ArchiveTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'reports/0316.HK').mkdir(parents=True)
        shutil.copyfile(ROOT / 'reports/index.schema.json', self.root / 'reports/index.schema.json')
        self.entries = []
        for day in ('01', '02'):
            entry = dict(as_of_date=f'2026-01-{day}', ticker='0316.HK', company='Fictional', exchange='HKEX',
                         path=f'reports/0316.HK/2026-01-{day}-Fictional-(Holding)-0316.HK.md',
                         summary='Archived price HK$4.78.', score='75 / B', portfolio_role='Watchlist',
                         published_at=f'2026-01-{day}T20:00:00+08:00',
                         ruleset='pre-2.2', summary_provenance='repaired_with_evidence',
                         summary_evidence=[dict(field='price', value='4.78', source_excerpt='Price: HK$4.78.')])
            if self.entries:
                entry['supersedes'] = self.entries[-1]['path']
            self.entries.append(entry)
            self.write_report(entry)
        for name in ('PUBLISHING.md', 'ARCHIVE-REPAIRS.md', 'MIGRATION.md'):
            (self.root / name).write_text('Fixture documentation\n', encoding='utf8')
        self.write_views()

    def write_report(self, entry):
        meta = [f"ticker: {entry['ticker']}", f"company: {entry['company']}",
                f"exchange: {entry['exchange']}", f"as_of_date: {entry['as_of_date']}",
                f"published_at: {entry['published_at']}", f"ruleset: {entry['ruleset']}"]
        if entry.get('supersedes'):
            meta.append(f"supersedes: {entry['supersedes']}")
        body = '\n'.join(['<!-- dividend-report-meta'] + meta + ['-->', 'Price: HK$4.78.', ''])
        (self.root / entry['path']).write_text(body, encoding='utf8')

    def use_v24(self):
        entry = self.entries[1]
        entry['ruleset'] = '2.4'
        entry['score'] = 'Not assessed'
        self.write_report(entry)
        return entry

    def use_v25_html(self, content='<p>Price: HK$<strong>4.78</strong>.</p>'):
        entry = self.entries[1]
        old_path = self.root / entry['path']
        entry['ruleset'] = '2.5'
        entry['score'] = '71-81 / B (provisional)'
        entry['path'] = Path(entry['path']).with_suffix('.html').as_posix()
        self.write_report(entry)
        path = self.root / entry['path']
        metadata = path.read_text(encoding='utf8').split('-->', 1)[0] + '-->'
        path.write_text('<!doctype html><html><head><meta charset="UTF-8"></head>'
                        f'<body>{metadata}{content}</body></html>', encoding='utf8')
        old_path.unlink()
        return entry

    def write_views(self):
        (self.root / 'reports/index.json').write_text(json.dumps(self.entries), encoding='utf8')
        for relative, text in rendered_files(self.entries).items():
            (self.root / relative).write_text(text, encoding='utf8')

    def test_valid_archive_including_balanced_parenthesis_links(self):
        self.assertEqual(validate_archive(self.root), [])

    def test_missing_previous_version_fails(self):
        del self.entries[1]['supersedes']
        self.assertTrue(any('supersedes' in e for e in validate_entries(self.entries, self.root)))

    def test_duplicate_path_and_self_cycle_fail(self):
        self.entries[1] = copy.deepcopy(self.entries[0])
        self.entries[1]['supersedes'] = self.entries[1]['path']
        self.assertTrue(any('duplicate' in e for e in validate_entries(self.entries, self.root)))

    def test_missing_metadata_or_unsafe_path_fails_before_render(self):
        del self.entries[0]['score']
        self.assertTrue(validate_entries(self.entries, self.root))
        self.entries[0]['score'] = '75 / B'
        self.entries[0]['path'] = '../../outside.md'
        self.assertTrue(validate_entries(self.entries, self.root))

    def test_changed_excerpt_or_wrong_value_fails(self):
        self.entries[0]['summary_evidence'][0]['source_excerpt'] = 'Price: HK$999.'
        self.assertTrue(any('excerpt' in e for e in validate_entries(self.entries, self.root)))
        self.entries[0]['summary_evidence'][0]['source_excerpt'] = 'Price: HK$4.78.'
        self.entries[0]['summary_evidence'][0]['value'] = '14.78'
        self.assertTrue(any('value' in e for e in validate_entries(self.entries, self.root)))

    def test_damaged_currency_and_metadata_mismatch_fail(self):
        self.entries[0]['summary'] = 'Price HK.78'
        self.assertTrue(any('damaged' in e for e in validate_entries(self.entries, self.root)))
        self.entries[0]['as_of_date'] = '2025-12-31'
        self.assertTrue(any('metadata' in e for e in validate_entries(self.entries, self.root)))

    def test_navigation_drift_and_missing_target_are_detected(self):
        (self.root / 'README.md').write_text('stale', encoding='utf8')
        self.assertTrue(any('navigation' in e for e in validate_archive(self.root)))
        self.write_views()
        (self.root / 'PUBLISHING.md').unlink()
        self.assertTrue(any('local link' in e for e in validate_archive(self.root)))

    def test_numeric_boundaries_allow_punctuation_but_not_different_amount(self):
        self.assertTrue(contains_value('Range HK$4.25-4.78.', '4.78'))
        self.assertFalse(contains_value('HK$14.78', '4.78'))
        self.assertFalse(contains_value('HK$4.789', '4.78'))

    def test_report_without_metadata_block_fails(self):
        (self.root / self.entries[0]['path']).write_text('Price: HK$4.78.\n', encoding='utf8')
        self.assertTrue(any('missing its dividend-report-meta' in e
                            for e in validate_entries(self.entries, self.root)))

    def test_metadata_version_chain_must_match_index(self):
        self.entries[1]['supersedes'] = self.entries[0]['path']
        self.write_report(self.entries[1])
        del self.entries[1]['supersedes']
        self.assertTrue(any('index supersedes' in e
                            for e in validate_entries(self.entries, self.root)))

    def test_metadata_ruleset_must_match_index(self):
        self.entries[0]['ruleset'] = '2.2'
        self.assertTrue(any('index ruleset' in e
                            for e in validate_entries(self.entries, self.root)))

    def test_repaired_summary_requires_evidence(self):
        self.entries[0]['summary_evidence'] = []
        self.assertTrue(any('transcription evidence' in e
                            for e in validate_entries(self.entries, self.root)))

    def test_original_summary_may_omit_evidence_but_current_ruleset_may_not(self):
        self.entries[0]['summary_provenance'] = 'original_unverified'
        self.entries[0]['summary_evidence'] = []
        self.assertEqual(validate_entries(self.entries, self.root), [])
        self.entries[0]['ruleset'] = '2.2'
        self.write_report(self.entries[0])
        self.assertTrue(any('current ruleset' in e
                            for e in validate_entries(self.entries, self.root)))

    def test_navigation_exposes_ruleset_and_evidence_coverage(self):
        readme = rendered_files(self.entries)['README.md']
        self.assertIn('pre-2.2', readme)
        self.assertIn('MIGRATION.md', readme)
        self.assertIn('摘要证据覆盖', readme)

    def test_v24_markdown_preserves_previous_version_and_navigation(self):
        entry = self.use_v24()
        self.write_views()
        self.assertEqual(validate_archive(self.root), [])
        views = rendered_files(self.entries)
        self.assertIn(f"[报告](<{entry['path']}>)", views['README.md'])
        self.assertIn('pre-2.2 1 份、2.2 0 份、2.4 1 份', views['README.md'])
        self.assertIn('Not assessed', views['reports/0316.HK/README.md'])
        self.assertIn(Path(self.entries[0]['path']).name, views['reports/0316.HK/README.md'])
        self.assertTrue((self.root / self.entries[0]['path']).is_file())

    def test_v24_preserves_exact_markdown_evidence_validation(self):
        entry = self.use_v24()
        entry['summary_evidence'][0]['source_excerpt'] = 'Price: HK$<strong>4.78</strong>.'
        self.assertTrue(any('excerpt' in e for e in validate_entries(self.entries, self.root)))

    def test_v24_requires_transcription_evidence(self):
        entry = self.use_v24()
        entry['summary_provenance'] = 'original_unverified'
        entry['summary_evidence'] = []
        self.assertTrue(any('current ruleset' in e for e in validate_entries(self.entries, self.root)))
        entry['summary_provenance'] = 'repaired_with_evidence'
        self.assertTrue(any('transcription evidence' in e for e in validate_entries(self.entries, self.root)))

    def test_markdown_format_remains_required(self):
        entry = self.use_v24()
        entry['path'] = Path(entry['path']).with_suffix('.html').as_posix()
        self.assertTrue(any('.path' in e for e in validate_entries(self.entries, self.root)))

    def test_v22_and_v24_counts_are_not_combined(self):
        self.entries[0]['ruleset'] = '2.2'
        self.write_report(self.entries[0])
        self.use_v24()
        self.write_views()
        self.assertEqual(validate_archive(self.root), [])
        self.assertIn('pre-2.2 0 份、2.2 1 份、2.4 1 份', rendered_files(self.entries)['README.md'])

    def test_v25_html_preserves_markdown_predecessor_and_score_range(self):
        entry = self.use_v25_html()
        self.write_views()
        self.assertEqual(validate_archive(self.root), [])
        self.assertIn('HTML报告（下载后打开）', rendered_files(self.entries)['README.md'])
        self.assertIn('71-81 / B (provisional)', rendered_files(self.entries)['reports/0316.HK/README.md'])
        self.assertTrue((self.root / entry['supersedes']).is_file())

    def test_html_evidence_decodes_entities_and_normalizes_whitespace(self):
        self.use_v25_html('<p>Price:&#32;HK$<strong>4.78</strong>.\n</p>')
        self.assertEqual(validate_entries(self.entries, self.root), [])

    def test_html_evidence_cannot_come_from_comments_scripts_or_attributes(self):
        for content in ('<!-- Price: HK$4.78. -->', '<script>Price: HK$4.78.</script>',
                        '<style>/* Price: HK$4.78. */</style>',
                        '<p title="Price: HK$4.78.">Nothing</p>'):
            with self.subTest(content=content):
                entry = self.entries[1]
                if entry['path'].endswith('.html'):
                    entry['path'] = Path(entry['path']).with_suffix('.md').as_posix()
                    self.write_report(entry)
                self.use_v25_html(content)
                self.assertTrue(any('excerpt' in e for e in validate_entries(self.entries, self.root)))

    def test_html_evidence_cannot_come_from_explicitly_hidden_content(self):
        for attribute in ('hidden', 'aria-hidden="true"', 'inert',
                          'style="display: none"', 'style="visibility: hidden !important;"'):
            with self.subTest(attribute=attribute):
                entry = self.entries[1]
                if entry['path'].endswith('.html'):
                    entry['path'] = Path(entry['path']).with_suffix('.md').as_posix()
                    self.write_report(entry)
                self.use_v25_html(f'<div {attribute}><p>Price: HK$4.78.</p></div>')
                self.assertTrue(any('excerpt' in e for e in validate_entries(self.entries, self.root)))

    def test_html_metadata_and_utf8_remain_required(self):
        entry = self.use_v25_html()
        path = self.root / entry['path']
        text = path.read_text(encoding='utf8')
        path.write_text(text.replace('charset="UTF-8"', 'charset="ASCII"'), encoding='utf8')
        self.assertTrue(any('UTF-8' in e for e in validate_entries(self.entries, self.root)))
        path.write_text(text.replace('ruleset: 2.5', 'ruleset: 2.4'), encoding='utf8')
        self.assertTrue(any('metadata' in e for e in validate_entries(self.entries, self.root)))

    def test_unindexed_html_is_detected(self):
        (self.root / 'reports/0316.HK/unindexed.html').write_text('<html></html>', encoding='utf8')
        self.assertTrue(any('missing from index' in e for e in validate_archive(self.root)))

    def test_v25_score_ranges_have_order_and_provisional_label(self):
        entry = self.use_v25_html()
        for score in ('81-71 / B (provisional)', '71-81 / B',
                      '40-71 / B-D (provisional)', '71 / D-B (provisional)'):
            with self.subTest(score=score):
                entry['score'] = score
                self.assertTrue(validate_entries(self.entries, self.root))
        entry['score'] = '40-71 / D-B (provisional)'
        self.assertEqual(validate_entries(self.entries, self.root), [])

    def test_v25_still_requires_summary_evidence(self):
        entry = self.use_v25_html()
        entry['summary_evidence'] = []
        self.assertTrue(any('transcription evidence' in e for e in validate_entries(self.entries, self.root)))

    def test_legacy_score_format_is_not_silently_migrated(self):
        self.entries[0]['score'] = '71-81 / B (provisional)'
        self.assertTrue(validate_entries(self.entries, self.root))
