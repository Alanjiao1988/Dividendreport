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
                         summary_evidence=[dict(field='price', value='4.78', source_excerpt='Price: HK$4.78.')])
            if self.entries:
                entry['supersedes'] = self.entries[-1]['path']
            self.entries.append(entry)
            (self.root / entry['path']).write_text(f"<!-- dividend-report-meta\nticker: 0316.HK\nas_of_date: {entry['as_of_date']}\n-->\nPrice: HK$4.78.\n", encoding='utf8')
        for name in ('PUBLISHING.md', 'ARCHIVE-REPAIRS.md'):
            (self.root / name).write_text('Fixture documentation\n', encoding='utf8')
        self.write_views()

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
