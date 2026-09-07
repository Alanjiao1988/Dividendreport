"""Render archive navigation from reports/index.json without touching reports."""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def cell(value):
    return str(value).replace('|', '&#124;').replace('\n', ' ')


def rendered_files(entries):
    ordered = sorted(entries, key=lambda e: (e['as_of_date'], e['ticker'], datetime.fromisoformat(e['published_at'].replace('Z', '+00:00')), e['path']), reverse=True)
    groups = defaultdict(list)
    for entry in ordered:
        groups[entry['ticker']].append(entry)
    root = [
        '# Dividendreport', '',
        '红利股分析报告归档 · Dividend income equity analysis reports.', '',
        f'归档含 **{len(entries)} 份报告、{len(groups)} 个不同标的**；同一标的的多个版本不构成独立样本。', '',
        '以下为各报告基准日的历史结论。价格、税务、评分与买入区间未因本次归档整理而重新研究；旧版 Fair / Strong Buy 等标签沿用原文，不代表当前建议。', '',
        '索引以 [reports/index.json](reports/index.json) 为唯一维护入口；本页及各标的 README 由本地工具生成。', '',
        '[发布契约与验证方式](PUBLISHING.md) · [历史修复依据](ARCHIVE-REPAIRS.md)', '',
        '## 报告索引 / Report Index', '',
        '| 数据基准日 As-of | 企业 Company | 代码 Ticker | 交易所 Exchange | 报告 Report | 结论 Summary |',
        '|---|---|---|---|---|---|',
    ]
    for e in ordered:
        row=[e['as_of_date'],e['company'],e['ticker'],e['exchange'],f"[报告](<{e['path']}>)",e['summary']]
        root.append('| ' + ' | '.join(map(cell,row)) + ' |')
    latest=max(entries,key=lambda e:datetime.fromisoformat(e['published_at']))['published_at']
    root.extend(['', f'最近报告声明发布时间 / Latest author-declared publication timestamp: {latest}', '',
                 '_This is research and archival material, not personalized investment advice._', ''])
    outputs={'README.md':'\n'.join(root)}
    for ticker, versions in groups.items():
        newest=versions[0]
        lines=[f"# {newest['company']} ({ticker})", '', f"交易所 Exchange: {newest['exchange']}", '',
               '历史版本按数据基准日列出；最新研究请沿版本链阅读。摘要保留原报告当时的判断。', '',
               '| 数据基准日 As-of | 报告 Report | 结论 Summary | 评分 Score | 组合角色 Role | 前一版本 Supersedes |',
               '|---|---|---|---|---|---|']
        for e in versions:
            name=Path(e['path']).name
            prev=e.get('supersedes')
            previous=f"[前一版](<{Path(prev).name}>)" if prev else '—'
            row=[e['as_of_date'],f'[{name}](<{name}>)',e['summary'],e['score'],e['portfolio_role'],previous]
            lines.append('| '+' | '.join(map(cell,row))+' |')
        lines.extend(['', '[完整索引与发布契约](../../PUBLISHING.md)', ''])
        outputs[f'reports/{ticker}/README.md']='\n'.join(lines)
    return outputs


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=ROOT)
    args=parser.parse_args()
    root=args.root.resolve()
    entries=json.loads((root/'reports/index.json').read_text(encoding='utf-8'))
    # Never turn an unsafe/unvalidated path from JSON into a write target.
    from validate_archive import validate_entries
    errors=validate_entries(entries,root)
    if errors:
        parser.exit(1,'\n'.join(errors)+'\n')
    for relative,text in rendered_files(entries).items():
        path=root/relative
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(text,encoding='utf-8',newline='\n')
    print(f'Rendered {len(rendered_files(entries))} navigation pages; archived report bodies untouched.')


if __name__=='__main__':
    main()
