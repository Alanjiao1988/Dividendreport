"""Validate archive records, evidence transcription and generated navigation locally."""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from collections import defaultdict
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
REPORT_SUFFIXES = {'.md', '.html'}


class ReportHTMLParser(HTMLParser):
    """Extract static body text without treating markup or script data as evidence."""

    VOID_TAGS = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
                 'link', 'meta', 'param', 'source', 'track', 'wbr'}
    BLOCK_TAGS = {'address', 'article', 'aside', 'blockquote', 'body', 'br', 'caption',
                  'dd', 'div', 'dl', 'dt', 'figcaption', 'figure', 'footer', 'h1',
                  'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'hr', 'li', 'main',
                  'nav', 'ol', 'p', 'pre', 'section', 'table', 'tbody', 'td',
                  'th', 'thead', 'tr', 'ul'}
    IGNORED_TAGS = {'head', 'script', 'style', 'template'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.stack = []
        self.html_attributes = None
        self.has_body = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.html_attributes = attrs
        if tag == 'body':
            self.has_body = True
        suppressed = bool(self.stack and self.stack[-1][1])
        suppressed = suppressed or tag in self.IGNORED_TAGS or 'hidden' in attrs
        if tag in self.BLOCK_TAGS:
            self.parts.append('\n')
        if tag not in self.VOID_TAGS:
            self.stack.append((tag, suppressed))

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                break
        if tag in self.BLOCK_TAGS:
            self.parts.append('\n')

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_data(self, data):
        if self.stack and not self.stack[-1][1] and any(tag == 'body' for tag, _ in self.stack):
            self.parts.append(data)

    @property
    def text(self):
        return ' '.join(''.join(self.parts).split())


def plain(text):
    return unicodedata.normalize('NFKC', text).replace('**', '').replace('`', '').replace(',', '')


def contains_value(text, value):
    text, value = plain(text), plain(value)
    if re.fullmatch(r'\d+(?:\.\d+)?%?', value):
        # A range can attach its percent sign only to the second endpoint.
        number = value.rstrip('%')
        return re.search(r'(?<![\d.])' + re.escape(number) + r'(?!\d|\.\d)', text) is not None
    return value in text


def validate_entries(entries, root=ROOT):
    root = Path(root).resolve()
    schema = json.loads((root / 'reports/index.schema.json').read_text(encoding='utf-8'))
    Draft202012Validator.check_schema(schema)
    errors = [f'{e.json_path}: {e.message}' for e in
              Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(entries)]
    if errors:
        return errors
    groups = defaultdict(list)
    paths = set()
    for entry in entries:
        label = f"{entry['ticker']} {entry['as_of_date']}"
        relative = Path(entry['path'])
        path = (root / relative).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            errors.append(f'{label}: report path must resolve to an existing file inside archive')
            continue
        if entry['path'] in paths:
            errors.append(f'{label}: duplicate report path')
        paths.add(entry['path'])
        if (relative.suffix not in REPORT_SUFFIXES
                or relative.parent.as_posix() != f"reports/{entry['ticker']}"
                or not relative.name.startswith(entry['as_of_date'] + '-')
                or not relative.name.endswith('-' + entry['ticker'] + relative.suffix)):
            errors.append(f'{label}: report path disagrees with ticker/date')
        groups[entry['ticker']].append(entry)
        text = path.read_text(encoding='utf-8')
        metadata = re.search(r'<!--\s*dividend-report-meta\s*\n(.*?)-->', text, re.S)
        if not metadata:
            # An optional block would let a report silently skip every metadata cross-check.
            errors.append(f'{label}: report is missing its dividend-report-meta block')
        else:
            fields = dict(line.split(':', 1) for line in metadata.group(1).splitlines() if ':' in line)
            fields = {k.strip(): v.strip() for k, v in fields.items()}
            for key in ('ticker', 'company', 'exchange', 'as_of_date', 'published_at', 'ruleset'):
                if fields.get(key) != entry[key]:
                    errors.append(f'{label}: report metadata disagrees with index {key}')
            # The index is the sole maintenance entry, so a second version chain must not diverge.
            if fields.get('supersedes') != entry.get('supersedes'):
                errors.append(f'{label}: report metadata disagrees with index supersedes')
        if entry['summary_provenance'] == 'repaired_with_evidence' and not entry['summary_evidence']:
            errors.append(f'{label}: a repaired summary must record its transcription evidence')
        if entry['ruleset'] != 'pre-2.2' and entry['summary_provenance'] != 'repaired_with_evidence':
            errors.append(f'{label}: a report published under the current ruleset must carry summary evidence')
        if datetime.fromisoformat(entry['published_at'].replace('Z', '+00:00')).date().isoformat() < entry['as_of_date']:
            errors.append(f'{label}: publication predates analysis cutoff')
        if re.search(r'\b(?:HK|US|HKD|USD)\s*\\?\.[0-9]|\$\s*\.[0-9]|\bat\s+\.(?:\s|$)', entry['summary']):
            errors.append(f'{label}: damaged monetary literal in summary')
        evidence_text = text
        if relative.suffix == '.html':
            document = ReportHTMLParser()
            document.feed(text)
            document.close()
            if document.html_attributes is None or not document.has_body:
                errors.append(f'{label}: HTML report must contain html and body elements')
            elif document.html_attributes.get('data-ruleset') != entry['ruleset']:
                errors.append(f'{label}: HTML ruleset disagrees with index ruleset')
            evidence_text = document.text
        for evidence in entry['summary_evidence']:
            excerpt, value = evidence['source_excerpt'], evidence['value']
            if relative.suffix == '.html':
                excerpt = ' '.join(excerpt.split())
            if not excerpt or excerpt not in evidence_text:
                errors.append(f'{label}: evidence excerpt is absent from archived report')
            if not contains_value(excerpt, value) or not contains_value(entry['summary'], value):
                errors.append(f'{label}: evidence value is inconsistent with source/summary')
    for ticker, versions in groups.items():
        ordered = sorted(versions, key=lambda e: (e['as_of_date'], datetime.fromisoformat(e['published_at'].replace('Z', '+00:00')), e['path']))
        for i, entry in enumerate(ordered):
            expected = ordered[i - 1]['path'] if i else None
            if entry.get('supersedes') != expected:
                errors.append(f"{ticker}: supersedes must identify the immediate prior version, or be absent on oldest")
    return errors


def validate_archive(root=ROOT):
    root = Path(root).resolve()
    entries = json.loads((root / 'reports/index.json').read_text(encoding='utf-8'))
    errors = validate_entries(entries, root)
    if errors:
        return errors
    from render_index import rendered_files
    views = rendered_files(entries)
    for relative, expected in views.items():
        path = root / relative
        if not path.is_file() or path.read_text(encoding='utf-8') != expected:
            errors.append(f'{relative}: navigation differs from canonical index; regenerate views')
        # Managed views use angle-bracket destinations, including valid parentheses.
        for angle, ordinary in re.findall(r'\]\(<([^>]+)>\)|\]\(([^()\s]+)\)', expected):
            link = urlsplit(angle or ordinary)
            if link.scheme or link.netloc or not link.path:
                continue
            target = (path.parent / unquote(link.path)).resolve()
            if not target.is_relative_to(root) or not target.is_file():
                errors.append(f'{relative}: missing or unsafe local link {angle or ordinary}')
    indexed = {e['path'] for e in entries}
    actual = {p.relative_to(root).as_posix() for p in (root / 'reports').glob('*/*')
              if p.is_file() and p.suffix in REPORT_SUFFIXES and p.name != 'README.md'}
    for orphan in sorted(actual - indexed):
        errors.append(f'{orphan}: archived report missing from index')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    errors = validate_archive(args.root)
    if errors:
        parser.exit(1, '\n'.join(errors) + '\n')
    entries = json.loads((args.root / 'reports/index.json').read_text(encoding='utf-8'))
    print(f"Archive valid: {len(entries)} reports, {len({e['ticker'] for e in entries})} tickers; index, evidence and navigation checked.")


if __name__ == '__main__':
    main()
