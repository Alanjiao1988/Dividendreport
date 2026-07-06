# Dividendreport

红利股分析报告归档 · Dividend income equity analysis reports.

由 `dividend-income-equity-analysis` 技能自动发布。每份报告都标注**数据基准日**与**对应企业**。

_This is research and archival material, not personalized investment advice._

## 报告索引 / Report Index

| 数据基准日 As-of | 企业 Company | 代码 Ticker | 交易所 Exchange | 报告 Report | 结论 Summary |
|---|---|---|---|---|---|
| 2026-07-06 | 华润电力 China Resources Power | 836.HK | HKEX | [报告](reports/836.HK/2026-07-06-华润电力-836.HK.md) | C 级观察名单; 0% 预扣税; 40% 净利润派息率精确执行, TTM 净息率 6.5% 无水分; 扩张期 FCF 为负、净负债/权益 150.8%; 现价 HK$17.31 处合理持有区, 积累区 12.0–14.7, 强买 ≤12.0; 否决未触发. |
| 2026-07-06 | 香港电讯 HKT Trust | 6823.HK | HKEX | [报告](reports/6823.HK/2026-07-06-香港电讯-6823.HK.md) | Grade B core income; 0% 预扣税; 100% AFF 派出、DPS 连续 14 年递增; 现价 HK$11.87 净息率 6.9% 处合理持有区, 累积区 HK$10.93–11.68. |
| 2026-07-06 | 中国神华 China Shenhua Energy | 1088.HK | HKEX | [报告](reports/1088.HK/2026-07-06-中国神华-1088.HK.md) | Grade C watchlist; 65% payout floor, zero cut in 18 yrs, net cash[...] |
| 2026-07-06 | 香港中华煤气 Towngas | 0003.HK | HKEX | [报告](reports/0003.HK/2026-07-06-香港中华煤气-0003.HK.md) | C级观察仓；冻结股息(13年零增长)、FCF覆盖0.8x；当[...] |
| 2026-07-06 | British American Tobacco | BTI | NYSE (ADR) | [报告](reports/BTI/2026-07-06-British-American-Tobacco-BTI.md) | Grade B core-income quality; 0% UK WHT; progressive dividend (FY2025[...] |
| 2026-07-03 | 中银香港 BOC Hong Kong | 2388.HK | HKEX | [报告](reports/2388.HK/2026-07-03-中银香港-BOC-Hong-Kong-2388.HK.md) | Core income; net yield ~4.9%; 56% payout, CET1 24%; divide[...] |
| 2026-07-03 | GSK plc | GSK.L | LSE | [报告](reports/GSK.L/2026-07-03-GSK-plc-GSK.L.md) | Quality income watchlist; current yield ~3.3%, buy zone below £17.50. |
| 2026-07-03 | Shell plc | SHEL | NYSE (ADS) | [报告](reports/SHEL/2026-07-03-Shell-plc-SHEL.md) | Grade B cyclical income; 0% UK withholding; dividend safe (~3x FCF cover); at ~$78 yield ~3.7% [...] |
| 2026-07-02 | 中国平安 Ping An Insurance | 2318.HK | HKEX | [报告](reports/2318.HK/2026-07-02-中国平安-2318.HK.md) | Grade B core income; 10% 预扣; 13 年连增、派息率仅营运利润 36%、覆盖 2.7x; 现价 HK$52.30 净息率 5.25% 处合理持有区上段, 累积区 HK$38.7–42.9; -30% 回撤为行业贝塔非分红危机. |
| 2026-07-02 | AstraZeneca PLC | AZN | NYSE | [报告](reports/AZN/2026-07-02-AstraZeneca-PLC-AZN.md) | Watchlist: top-quality, 0% WHT, ~2x-covered progressive dividend, but yield only ~1.6% — a[...] |

最近更新 / Last updated: 2026-07-06 21:59 (Asia/Hong_Kong)

---

更多信息 / Notes

- 目录结构：每家公司有独立目录，路径为 `reports/<TICKER>/`，每份报告以 `{YYYY-MM-DD}-{公司中文名}-{TICKER}.md` 命名并包含数据基准日与结论要点。
- 自动化：本仓库由 `dividend-income-equity-analysis` 技能自动发布报告条目与内容；如需手动添加或修订，请参照下节的贡献指南。

贡献 / Contributing

如果你想提交报告、修正或补充信息：

1. 在本地将报告文件放到对应目录，例如 `reports/1088.HK/2026-07-06-中国神华-1088.HK.md`。
2. 确保报告顶部包含数据基准日（As-of）、公司名称、代码与交易所信息，以及简要结论（Summary）。
3. 发起 pull request 到本仓库的默认分支，PR 描述请说明来源（手动/自动化）与数据基准日。

文件格式示例（Markdown）：

```markdown
# 公司名 (TICKER)

交易所 Exchange: HKEX

- 数据基准日 As-of: 2026-07-06
- 报告摘要 Summary: ...

## 分析内容

（财务摘要、派息历史、自由现金流、估值与结论）
```

许可 / License

本仓库为研究与归档用途。报告中包含的数据与观点仅供参考，不构成投资建议。

联系方式 / Contact

如有问题或建议，请在 Issues 中提交或联系仓库维护者。
