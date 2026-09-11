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
        body = '\n'.join(['<!-- dividend-report-meta'] + meta + ['-->', ''])
        if Path(entry['path']).suffix == '.html':
            body = ('<!DOCTYPE html>\n' + body
                    + f'<html lang="zh-CN" data-ruleset="{entry["ruleset"]}">'
                    '<head><title>Fixture</title></head><body>'
                    '<p>Price: <strong>HK$4.78</strong> &amp; cash.</p>'
                    '</body></html>\n')
        else:
            body += 'Price: HK$4.78.\n'
        (self.root / entry['path']).write_text(body, encoding='utf8')

    def add_html_report(self, day='03'):
        entry = copy.deepcopy(self.entries[-1])
        entry.update(as_of_date=f'2026-01-{day}', published_at=f'2026-01-{day}T20:00:00+08:00',
                     path=f'reports/0316.HK/2026-01-{day}-Fictional-0316.HK.html',
                     ruleset='2.4', score='Not assessed', supersedes=self.entries[-1]['path'],
                     summary_evidence=[dict(field='price', value='4.78',
                                            source_excerpt='Price: HK$4.78 & cash.')])
        self.entries.append(entry)
        self.write_report(entry)
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

    def test_html_and_markdown_versions_validate_together(self):
        self.add_html_report()
        self.add_html_report('04')
        self.write_views()
        self.assertEqual(validate_archive(self.root), [])
        readme = (self.root / 'README.md').read_text(encoding='utf8')
        self.assertIn('pre-2.2 2 份、2.2 0 份、2.4 2 份', readme)
        self.assertIn('[HTML 报告]', readme)
        self.assertIn('下载后用浏览器打开', readme)
        ticker_readme = (self.root / 'reports/0316.HK/README.md').read_text(encoding='utf8')
        self.assertIn('[前一版](<2026-01-03-Fictional-0316.HK.html>)', ticker_readme)

    def test_html_evidence_decodes_entities_and_preserves_inline_text(self):
        entry = self.add_html_report()
        entry['summary_evidence'][0]['source_excerpt'] = 'Price:\n HK$4.78 & cash.'
        self.assertEqual(validate_entries(self.entries, self.root), [])
        entry['summary_evidence'][0]['source_excerpt'] = '<strong>HK$4.78</strong>'
        self.assertTrue(any('excerpt' in e for e in validate_entries(self.entries, self.root)))

    def test_html_evidence_excludes_non_body_and_hidden_text(self):
        entry = self.add_html_report()
        path = self.root / entry['path']
        fragments = [
            '<!-- Price: HK$4.78 & cash. -->',
            '<script>Price: HK$4.78 & cash.</script>',
            '<style>Price: HK$4.78 & cash.</style>',
            '<template><p>Price: HK$4.78 &amp; cash.</p></template>',
            '<div hidden><p>Price: HK$4.78 &amp; cash.</p></div>',
        ]
        for fragment in fragments:
            with self.subTest(fragment=fragment):
                self.write_report(entry)
                body = path.read_text(encoding='utf8').replace(
                    '<p>Price: <strong>HK$4.78</strong> &amp; cash.</p>', fragment)
                path.write_text(body, encoding='utf8')
                self.assertTrue(any('excerpt' in e for e in validate_entries(self.entries, self.root)))
        self.write_report(entry)
        body = path.read_text(encoding='utf8').replace(
            '<p>Price: <strong>HK$4.78</strong> &amp; cash.</p>', '')
        body = body.replace('<title>Fixture</title>', '<title>Price: HK$4.78 &amp; cash.</title>')
        path.write_text(body, encoding='utf8')
        self.assertTrue(any('excerpt' in e for e in validate_entries(self.entries, self.root)))

    def test_html_void_tags_do_not_hide_following_evidence(self):
        entry = self.add_html_report()
        path = self.root / entry['path']
        body = path.read_text(encoding='utf8').replace(
            '<body>', '<body><img hidden><br/><hr>')
        path.write_text(body, encoding='utf8')
        self.assertEqual(validate_entries(self.entries, self.root), [])

    def test_html_document_and_embedded_ruleset_must_be_valid(self):
        entry = self.add_html_report()
        path = self.root / entry['path']
        body = path.read_text(encoding='utf8')
        path.write_text(body.replace('data-ruleset="2.4"', 'data-ruleset="2.2"'), encoding='utf8')
        self.assertTrue(any('HTML ruleset' in e for e in validate_entries(self.entries, self.root)))
        path.write_text(body[:body.index('<html')] + 'Price: HK$4.78 & cash.', encoding='utf8')
        self.assertTrue(any('html and body' in e for e in validate_entries(self.entries, self.root)))

    def test_html_ruleset_requires_evidence_and_matching_metadata(self):
        entry = self.add_html_report()
        entry['summary_evidence'] = []
        self.assertTrue(any('transcription evidence' in e for e in validate_entries(self.entries, self.root)))
        entry['summary_provenance'] = 'original_unverified'
        self.assertTrue(any('current ruleset' in e for e in validate_entries(self.entries, self.root)))
        entry['company'] = 'Changed'
        self.assertTrue(any('metadata disagrees' in e for e in validate_entries(self.entries, self.root)))

    def test_unindexed_html_report_is_detected(self):
        entry = self.add_html_report()
        self.entries.pop()
        self.write_views()
        self.assertTrue(any(entry['path'] in e and 'missing from index' in e
                            for e in validate_archive(self.root)))

    def test_unsupported_report_extension_or_ruleset_is_rejected(self):
        entry = self.add_html_report()
        entry['ruleset'] = '9.9'
        self.assertTrue(validate_entries(self.entries, self.root))
        entry['ruleset'] = '2.4'
        entry['path'] = entry['path'].replace('.html', '.txt')
        self.assertTrue(validate_entries(self.entries, self.root))
