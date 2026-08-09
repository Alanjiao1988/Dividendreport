# Dividendreport

红利股分析报告归档 · Dividend income equity analysis reports.

由 `dividend-income-equity-analysis` 技能自动发布。每份报告都标注**数据基准日**与**对应企业**。

_This is research and archival material, not personalized investment advice._

## ⚠️ 维护规则 / Maintenance rule（发布新报告时必读）

**本仓库的报告索引固定采用下方的「纵向卡片」格式，禁止改回宽表格（`| 数据基准日 | 企业 | ... |` 那种多列 Markdown 表格）。** 宽表格在手机端会被压缩到无法阅读或需要横向滚动，这是本次改版明确要解决的问题。无论是人工提交，还是 `dividend-income-equity-analysis` 技能自动发布新报告，在更新 `README.md` 的报告索引时都必须遵守：

1. **不要**重新引入 6 列表格（`数据基准日 / 企业 / 代码 / 交易所 / 报告 / 结论`）。
2. 每条新报告追加为一个卡片，结构固定为：
   - 三级标题：`### 代码 Ticker · 企业 Company`
   - 一行元信息：`📅 数据基准日 As-of ｜ 🏛️ 交易所 Exchange ｜ [报告](相对路径)`
   - 折叠的结论：`<details><summary>结论摘要 Summary (点击展开 / tap to expand)：<第一句摘要></summary>` … 完整结论正文 … `</details>`
3. 新报告默认追加在列表**最前面**（按数据基准日倒序），与现有排序保持一致。
4. 如果某次自动化发布仍生成了宽表格，请在合入前手动转换为上述卡片格式，而不是保留表格。

## 报告索引 / Report Index

### CVX · Chevron Corporation
📅 2026-08-06 ｜ 🏛️ NYSE ｜ [报告](reports/CVX/2026-08-06-Chevron-CVX.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：Grade B - a near-unimpeachable dividend attached to a disqualifying yield, and waiting will not fix it.</summary>

Grade B - a near-unimpeachable dividend attached to a disqualifying yield, and waiting will not fix it. **The last twelve months contain a Strait-of-Hormuz windfall**: Q2 2026 alone earned $12.07bn / $6.11 diluted EPS at $104 Brent versus $2.21bn / $1.11 in Q1 at $81; Brent touched ~$120 in April and is back to $79-82 today, so every TTM figure is a peak-cycle artifact and everything here is normalized at **$70 Brent mid-cycle**. The dividend itself: **39 consecutive annual increases** (+4% to $1.78/qtr in Jan 2026, $7.12 annualized), zero special or variable payouts, no scrip, no ATM, and cash dividends covered by free cash flow in **every one of the last five years** (worst 1.27x in 2024); the 2025 accounting payout hit 104% of net income as post-Hess DD&A rose to $11.9bn annualized, yet cash cover was still 1.30x - only the cash measure is honest for this company. The balance sheet is the real moat: net debt ratio 15.6%->**13.1%**, net debt/CFFO **0.6x**, a record **$8.4bn** of total debt retired in Q2 alone, and leverage sitting below its own 20-25% target with an estimated ~$25bn of headroom. The key structural point: **the buyback is the shock absorber and the dividend sits behind it** - in 2023-25 dividends plus buybacks exceeded FCF by ~$6.5bn/$12.0bn/$10.5bn, all funded from the cash balance and debt, while **the dividend itself was never debt-funded**; across six single-driver sensitivities the derived DPS does not move once, every shock lands on the repurchase line. Nor is the asset base in decline: production +20% y/y (H1 3,965 MBOED), and in 2024->2025 Brent fell $12 while recurring FCF rose $15.0bn->$16.6bn on Hess consolidation, TCO's FGP flipping from capex sink to cash distributor, and cost cuts; $3bn of structural savings landed six months early, Hess synergies hit $1.5bn (150% of target), guidance is >10% annual adjusted-FCF growth at a flat $70 Brent reaching $28-30bn by 2030, with capex held at the $18-19bn floor. **But 30% US withholding** (no US-HK treaty; W-8BEN gives no rate relief) cuts a 3.77% headline gross yield to **2.64% net** - a permanent ~$4.2m/yr loss per $1bn invested that a DRIP cannot avoid, since reinvestment occurs on the after-tax amount. Across all nine scenario cells in section 13 the after-tax yield on today's cost moves only between **2.64% and 2.98%** - three years out, including the Bull case, it never reaches 3%. N=$4.984 net (mid_cycle @$70 Brent, stripping the $92 H1 realization, the $104 Q2 quarter, $1.4bn of Q2 timing effects and $1.8bn of FY2025 asset sales), B=N because the Bear outcome is a **freeze, not a cut** ($15.9-16.4bn of distributable cash against a $14.2bn dividend cost at $55-58 Brent, with 2020 as precedent when debt went $23.7bn->$42.8bn to maintain and raise the payout), so the accumulation band is **empty**; r 7.0-9.5% net (the cyclical floor, not pushed lower because Forecast Confidence is only Medium). Fair/hold $52.46-71.20, strong buy <=$52.46. At $188.63 the stock sits **2.65x above** the fair upper bound and would have to fall 62.3% to enter it - and $52.46 is precisely the March 2020 COVID low. The conflict worth stating plainly: a 7-9.5% required net yield implies a 10.0-13.6% required gross yield at this withholding rate, which Chevron has touched once in fifty years; even tax-free the required gross yield implies $75-102, and an AA-rated major does not yield 9% gross outside a solvency panic. The conclusion is not that the framework is wrong or the company is bad - Chevron's shareholder return is deliberately built as ~2.6% net dividend + ~3% share retirement + >10% FCF growth at flat $70 Brent, a total-return proposition in which the dividend is by design the smallest part. Veto **not triggered** - the risk is overpaying, not a dividend cut. Grade stays B (the business earns it); Portfolio Role overridden to **Watchlist** because the after-tax income mandate is not met. The highest-value fix is not timing but holding structure: removing the 30% withholding lifts the yield from 2.64% to 3.77% and the fair ceiling from $71 to $102. Also watch the deliberate increase in political-risk exposure (Iraq West Qurna 2 / Nasiriyah heads of agreement, a publicly courted Venezuela re-entry) and the one variable most likely to rewrite this analysis favourably - the 20-year, 2.67GW Microsoft West Texas data-centre PPA. Withholding is `market_default`-assumed, not broker-observed.

</details>

### VZ · Verizon Communications Inc.
📅 2026-08-06 ｜ 🏛️ NYSE ｜ [报告](reports/VZ/2026-08-06-Verizon-VZ.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：Supersedes the 2026-07-31 report.</summary>

**Supersedes the 2026-07-31 report.** Fundamental verdict, N=$2.02, B=$1.98, score 75/B and the untriggered veto all carry over unchanged; **the one substantive change is that the required net yield is tightened from 4.5-5.5% to 5.0-6.5%**, moving the fair upper bound (the add-trigger) from $44.89 down to $40.40. Two reasons: (i) `buy-zone.md` requires a *conservative balance sheet* to justify a downward adjustment, and that is precisely the one condition VZ fails — net unsecured leverage 2.5x versus its own 2.0-2.25x target, ~$158.2bn total debt, $7.35bn LTM interest — so there is no basis for pushing r_low below the 5% telecom floor; (ii) this framework anchors on after-tax **dividend** income, and folding the tax-free buyback yield into a required *dividend* yield mixes two measures — buyback value belongs in the total-return narrative instead. The quality verdict is unchanged: 30% US withholding turns a 6.06% headline gross yield into **4.24% net**, the single biggest structural drag for an HK holder, and that is the lowest after-tax income yield since 2021. The dividend itself is close to unimpeachable — 20 straight annual increases (+2.5% to $0.7075/qtr, announced Jan 2026, effective from the May payment), no scrip, no ATM, five years of cumulative FCF $92.0bn covering cumulative dividends $55.0bn (1.67x), with not one year funded by debt, asset sales or issuance. 2026 is a genuine inflection under Dan Schulman: 2Q26 adjusted EBITDA $13.7bn (+7.2%) and 40.1% margin both all-time records, 1H26 FCF $10.2bn (+16.0%), the first positive Q1 postpaid phone net adds since 2013, postpaid phone churn 0.97%->0.92%, broadband at 17.1m connections after the Frontier close on 2026-01-20 ($9.8bn cash + $12.9bn assumed debt), a $9bn opex/capex savings programme, buybacks cutting shares 4,217m->4,155m (-1.5%) in six months with the 2026 target raised to $4.5bn, plus a $1bn+ Google dark-fiber contract. Guidance raised twice: FY26 FCF $21.9-22.1bn (+9-10%), adj EPS $4.99-5.04, capex $16.0-16.5bn. The catch: 2Q26 wireless service revenue still -0.7%, total revenue -0.7%, GAAP net income -22.9%, leverage 2.2x->2.5x, and a reported but **unsigned** ~$10bn EchoStar AWS-3 spectrum deal (first reported by Bloomberg in Sep 2025) that would defer deleveraging by ~2 years and force buybacks to pause — carried as a standalone persistent sensitivity (accumulation bound -$1.40), excluded from Base. Because buybacks shrink the count, dividend cash cost is locked at ~$11.8bn in all nine scenario cells — per-share growth is entirely self-funded by share retirement, so the durability of DPS growth depends on the buyback continuing; even in Bear (FCF $20.0bn, $6bn/yr debt paydown) the payout is 84% of distributable cash and 59% of FCF, so the rational cut is the buyback, not the dividend — which is why B sits only 2% below N and the accumulation band is nearly empty. Fair/hold $31.08-40.40, accumulate 30.46-31.08, strong buy <=30.46. At $46.70 the stock sits 15.6% above the fair upper bound (4.0% above on the prior calibration). The structural point worth stating plainly: the strong-buy boundary implies a 9.51% gross yield, which VZ has approached only once — the October 2023 lead-cable panic at ~8.8% — so the accumulation band is in practice near-unreachable, correctly reflecting that a US ordinary share is a structurally inefficient vehicle for an HK taxable income mandate. Veto not triggered — the risk is overpaying, not a dividend cut. Hold if owned (~6.55% total after-tax shareholder yield including the 2.31% untaxed buyback); reassess adding below $40.40. Withholding is legal_structure-assumed, not broker-observed.

</details>

### VZ · Verizon Communications Inc.
📅 2026-07-31 ｜ 🏛️ NYSE ｜ [报告](reports/VZ/2026-07-31-Verizon-VZ.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：_(superseded by the 2026-08-06 report)_ Grade B core income — quality yes, price no.</summary>

_(superseded by the 2026-08-06 report)_ Grade B core income — quality yes, price no. The 30% US withholding turns a 6.14% headline gross yield into **4.30% net** for an HK holder, the single biggest structural drag. The dividend itself is close to unimpeachable: 20 straight annual increases (latest +2.5% to $0.7075/qtr in Jan 2026), no scrip, no ATM, and five years of cumulative FCF $92.0bn covering cumulative dividends $55.0bn (1.67x) with not one year funded by debt, asset sales or issuance — debt growth financed spectrum and M&A, never the payout. 2026 is a genuine inflection under Dan Schulman: 2Q26 adjusted EBITDA $13.7bn (+7.2%) and 40.1% margin are both all-time records, 1H26 FCF $10.2bn (+16.0%), postpaid phone churn 0.97%->0.92%, broadband at 17.1m connections after the Frontier close on 2026-01-20 ($9.8bn cash + $12.9bn assumed debt), a $9bn opex/capex savings programme, and the first real buyback in years — shares 4,217m->4,155m (-1.5%) in six months, 2026 target raised to $4.5bn. Guidance raised twice this year: FY26 FCF $21.9-22.1bn (+9-10%), adj EPS $4.99-5.04, capex $16.0-16.5bn. The catch: wireless service revenue guided ~flat, total revenue -0.7% in 2Q26, GAAP net income -22.9%, net unsecured debt/EBITDA up 2.2x->2.5x on Frontier, LTM interest expense $7.35bn, and a reported but **unsigned** ~$10bn EchoStar AWS-3 spectrum deal that would defer deleveraging and buybacks. Because buybacks shrink the count, total dividend cash cost stays flat at ~$11.7bn across all three scenarios — per-share growth is self-funded; even in Bear (FCF $18.5bn, $5bn/yr debt paydown) the payout is 92% of distributable cash, so the rational cut is the buyback, not the dividend. N=$2.02 net (three_year_base_average, capex normalized to $17.0-17.5bn, cross-checked against mid-cycle $2.05), B=$1.98 (frozen, not cut), r 4.5-5.5% net (one notch below the 5-7% telecom anchor, crediting the ~2.3%/yr buyback yield); fair/hold $36.91-44.89, accumulate 36.00-36.91, strong buy <=36.00. At $46.11 the stock sits 2.7% above the fair upper bound after a ~6% one-week pop on Q2 results and the $1bn+ Google dark-fiber deal. Veto not triggered — the risk is overpaying, not a dividend cut. Withholding is legal_structure-assumed, not broker-observed.

</details>

### 0883.HK · 中国海洋石油 CNOOC Limited
📅 2026-07-31 ｜ 🏛️ HKEX ｜ [报告](reports/0883.HK/2026-07-31-中国海洋石油-0883.HK.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：Grade B cyclical income — hold, not an add point.</summary>

Grade B cyclical income — hold, not an add point. **Withholding upgraded from "assumed" to confirmed 10%**: the announcement exempts "natural person" holders, but shares registered via HKSCC Nominees are deemed non-resident-enterprise holdings, so every broker-held retail position (IBKR included) suffers the 10% PRC EIT — the same mechanism already broker-observed on 0941.HK. 0883 has no tax edge over PetroChina or China Mobile. TTM net yield 4.84% at HK$23.82 (gross 5.37%), normalized 5.29%. The business is near-flawless: net cash RMB 148.7bn (D/E 0.12), all-in cost $27.9/boe (lowest global quartile), production 573→777 MMBOE in five years (7.9% CAGR) with reserves +6.9% and >100% replacement, payout floor lifted 40%→45% for 2025-27, zero dilution since the Apr-2022 A-share IPO, no scrip/DRIP, FCF cover 1.43-3.20x in every one of five years. The problem is price and cycle position: the stock sits 0.3% below its 2026-01-28 all-time high of HK$23.90 while FY2026 earnings carry a one-off Hormuz premium — Brent ran $61 (Jan) → $118 (Mar) → $82 (Jul) after the strait closed on 2026-02-28 and reopened on a US-Iran deal, and EIA's July STEO cut 2027 Brent to $64.76 from $79.39 one month earlier. FY2026 Base net DPS HK$1.53 (6.42%) is transient and must not anchor entry; FY2027 Base falls back to HK$1.152 (4.84%) — exactly today's TTM, i.e. normalization is already fully priced. FY2027-28 Bear (realized $55-56) leaves FCF cover at 0.83x/0.71x, funded from the cash pile. N=HK$1.26 (mid_cycle at realized $68/bbl, 840 MMBOE — independently equal to the 5-yr median gross HK$1.40 × 0.9), B=HK$0.88, r 7.5-10%; fair/hold HK$12.60-16.80, accumulate 8.80-12.60, strong buy <=8.80 — price must fall 29.5% to reach fair. Veto not triggered; the risk is overpaying, not a dividend cut. Watch H1 2026 results (late Aug 2026), whether 2027 Brent really settles at $65, and the 45% policy's expiry at end-2027. Supersedes the 2026-07-17 report.

</details>

### 0941.HK · 中国移动 China Mobile
📅 2026-07-31 ｜ 🏛️ HKEX ｜ [报告](reports/0941.HK/2026-07-31-中国移动-China-Mobile-0941.HK.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：Grade B core income — hold, not an add point.</summary>

Grade B core income — hold, not an add point. 10% PRC withholding applies via HKSCC Nominees (broker-observed, IBKR) despite HK incorporation, because the company is a PRC tax-resident enterprise; TTM net yield 5.70% at HK$83.25, normalized 5.85%. Net cash RMB 130-276bn, D/E ~0.07, zero dilution (no scrip, no DRIP, no issuance since Dec 2021, and no buyback ever), 6 straight years of DPS growth to HK$5.27. But 57% of the four-year DPS growth came from ratcheting the payout ratio 65%->75.5%, not from earnings (DPS CAGR 6.7% vs EPS CAGR 2.9%) — that lever has only ~5pp left, after which DPS growth converges to ~2-3% earnings growth. FY2025 broke a four-year coverage streak: FCF RMB 82bn < dividends RMB 104bn (0.79x), funded from the cash pile not debt; OCF fell RMB 316bn->233bn unexplained, though Q1 2026 OCF +128% points to working-capital timing. Payout is ratio-linked, not progressive, so the Bear case is a -7.4% cut to HK$4.88, not merely slower growth. N=HK$4.87 (mid_cycle, normalized to a 77% payout, deliberately below the Base 78-80% ratchet), B=HK$4.39, r 5.5-7.0%; fair/hold HK$69.6-88.6, accumulate 62.7-69.6, strong buy <=62.7 — price must fall 16.4% to accumulate. Current 6.33% gross yield is the lowest of the past six annual observations. Veto not triggered. Watch H1 2026 results (~14 Aug 2026) for OCF recovery, and mobile ARPU (RMB 46.8, falling) — the highest-leverage driver.

</details>

### PBR · Petróleo Brasileiro S.A. — Petrobras
📅 2026-07-31 ｜ 🏛️ NYSE (ADR) ｜ [报告](reports/PBR/2026-07-31-Petrobras-PBR.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：Grade D opportunistic — watchlist, not an entry point.</summary>

Grade D opportunistic — watchlist, not an entry point. Brazil ended 30 years of tax-free dividends on 2026-01-01: Law 15,270/2025 imposes 10% WHT on dividends and LC 224/2025 raised JCP to 17.5%; Petrobras pays 100% in JCP form, so the HK investor now loses 17.5% with no treaty and no credit (HK is on Brazil's IN 1037 tax-haven list — ADR depositary-level withholding should preserve 17.5% vs 25%, unverified). The widely quoted "$0.96 / 5.02% yield" is already net — gross TTM is ~$1.17 / 6.1%. The dividend itself is honest: 45%-of-FCF formula followed to the decimal (FY2025 $7,507m = 45.5% of FCF), five straight years of FCF-funded payouts with net deleveraging and zero dilution — veto not triggered. But FCF halved from $39.9bn (2022) to $16.5bn (2025) as capex tripled ($6.3bn→$20.3bn), DPS fell 83% from $5.77 to $0.99/ADR, and the stock re-rated +45% y/y to $19.12 while record production (3.34 mmboed, +14.1% y/y) accrues to capex not shareholders. Normalized net yield only 4.3% at mid-cycle Brent $70 / FX 5.30 (N=$0.83); fair/hold $6.92-9.22, accumulate $3.33-6.92, strong buy <=$3.33 — robust even at a 6% required yield. Watch the $75bn gross-debt gate ($71.2bn now) that makes the 45% policy mandatory, and the October 2026 election. Own PBR.A ($16.85) if ever bought: identical DPS, 11.9% cheaper, 5.71% vs 5.02% net.

</details>

### SHEL · Shell plc
📅 2026-07-31 ｜ 🏛️ NYSE (ADS) ｜ [报告](reports/SHEL/2026-07-31-Shell-plc-SHEL.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：Grade B cyclical income; 0% UK withholding and the depositary currently charges no fee; dividend uncut and raised 6 straight years, Q2 2026 declared…</summary>

Grade B cyclical income; 0% UK withholding and the depositary currently charges no fee; dividend uncut and raised 6 straight years, Q2 2026 declared $0.7812/ADS (run-rate +9.1% YoY), costing only 19% of mid-cycle CFFO with 2.8x operating-FCF cover even in trough 2025, gearing 18.7% (net debt $52.6bn → $41.8bn in one quarter), share count −27.5% in 4.5 years with no scrip and no issuance; but Q2 2026 adjusted earnings $9.84bn carry a Hormuz war premium (Brent $92 vs EIA 2027 forecast $65) and at $90.51 near the all-time high net yield is only 3.27% — a four-year low; N normalized to mid-cycle Brent $70 = $3.40/ADS; fair/hold $52.31-68.00, accumulate $48.55-52.31, strong buy <=$48.55; veto not triggered — the risk here is overpaying, not a dividend cut. Supersedes the 2026-07-03 report.

</details>

### TTE · TotalEnergies SE
📅 2026-07-30 ｜ 🏛️ NYSE / Euronext Paris ｜ [报告](reports/TTE/2026-07-30-TotalEnergies-SE-TTE.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：Grade B core income on watchlist; French WHT only 12.8% for individuals (10% under HK treaty) and the NYSE line converted from ADR to ordinary shares…</summary>

Grade B core income on watchlist; French WHT only 12.8% for individuals (10% under HK treaty) and the NYSE line converted from ADR to ordinary shares on 2025-12-08 — no depositary fee; progressive DPS uncut through 2020 and 2025, FY2025 €3.40 (+5.6%), FY2026 run-rate €3.60 (+5.9%, only 2 of 4 interims declared), FCF cover 1.26x even in trough 2025, gearing 13.1%, share count −19% in five years; at €75.68 / $86.75 net yield only 4.15% — above the fair-value ceiling because Brent spiked 25% in a month to $89.74; fair/hold €54.60-69.76 ($62.67-80.08), accumulate €49.14-54.60 ($56.40-62.67), strong buy <=€49.14 ($56.40); veto not triggered.

</details>

### GSK.L · GSK plc
📅 2026-07-21 ｜ 🏛️ LSE ｜ [报告](reports/GSK.L/2026-07-21-GSK-plc-GSK.L.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：Grade B quality income watchlist; 0% UK withholding; progressive dividend, FY2025 DPS 66p (+8.2% YoY), 2026 guided 70p, FCF cover 1.53x (1.92x…</summary>

Grade B quality income watchlist; 0% UK withholding; progressive dividend, FY2025 DPS 66p (+8.2% YoY), 2026 guided 70p, FCF cover 1.53x (1.92x ex-Zantac), net debt/EBITDA ~1.3x, £2bn buyback completed (genuine ~3.1% share reduction); at 1,880.5p ($50.72 ADR) net yield only 3.5% — above the disciplined fair-value ceiling; fair/hold 1,167-1,750p, accumulate 917-1,167p, strong buy <=917p; veto not triggered.

</details>

### 0005.HK · 汇丰控股 HSBC Holdings plc
📅 2026-07-17 ｜ 🏛️ HKEX ｜ [报告](reports/0005.HK/2026-07-17-汇丰控股-HSBC-Holdings-0005.HK.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：Grade B cyclical income; 0% UK withholding; 50% payout of EPS ex-notables 2026-28, ~2x earnings cover, CET1 14.0%; at HK$155.6 net yield only 3.8% —…</summary>

Grade B cyclical income; 0% UK withholding; 50% payout of EPS ex-notables 2026-28, ~2x earnings cover, CET1 14.0%; at HK$155.6 net yield only 3.8% — below 5-yr range low after ~65% rally; fair/hold HK$87-122, accumulate 73-87, strong buy <=73; veto not triggered.

</details>

### 0144.HK · 招商局港口 China Merchants Port Holdings
📅 2026-07-17 ｜ 🏛️ HKEX ｜ [报告](reports/0144.HK/2026-07-17-招商局港口-China-Merchants-Port-Holdings-0144.HK.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：Grade B cyclical income; 0% withholding (HK-incorporated); payout policy floor >=45% of profit, FY2025 DPS HK$0.739 (-16.6% YoY on lower earnings),…</summary>

Grade B cyclical income; 0% withholding (HK-incorporated); payout policy floor >=45% of profit, FY2025 DPS HK$0.739 (-16.6% YoY on lower earnings), FCF cover 2.8x, net gearing 19.3%; at HK$14.01 normalized net yield only 5.3-5.9% — below historical median; fair/hold HK$10.71-13.64, accumulate 9.29-10.71, strong buy <=9.29; veto not triggered.

</details>

### 0883.HK · 中国海洋石油 CNOOC Limited
📅 2026-07-17 ｜ 🏛️ HKEX ｜ [报告](reports/0883.HK/2026-07-17-中国海洋石油-0883.HK.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：Grade B cyclical income; 10% withholding assumed (PRC tax-resident red-chip, verify broker statement); payout floor >=45% for 2025-27, FY2025 DPS…</summary>

Grade B cyclical income; 10% withholding assumed (PRC tax-resident red-chip, verify broker statement); payout floor >=45% for 2025-27, FY2025 DPS HK$1.28 (-9% YoY), FCF cover 1.75x, net cash; at HK$22.72 net yield 5.1% — below 5-yr yield band low after rally; fair/hold HK$13.5-17.7, accumulate 10.4-13.5, strong buy <=10.4; veto not triggered.

</details>

### 0008.HK · PCCW Limited 电讯盈科
📅 2026-07-07 ｜ 🏛️ HKEX ｜ [报告](reports/0008.HK/2026-07-07-PCCW-Limited-电讯盈科-0008.HK.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：Net yield ~7.0%; stable HKT-funded DPS, leverage watch; accumulation zone HK.25-4.78.</summary>

Net yield ~7.0%; stable HKT-funded DPS, leverage watch; accumulation zone HK.25-4.78.

</details>

### 0316.HK · 东方海外国际 Orient Overseas (International) Limited
📅 2026-07-07 ｜ 🏛️ HKEX ｜ [报告](reports/0316.HK/2026-07-07-东方海外国际-Orient-Overseas-(International)-Limited-0316.HK.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：Cyclical income: TTM net yield ~6.95%, buy zone below current price, value-trap veto unclear.</summary>

Cyclical income: TTM net yield ~6.95%, buy zone below current price, value-trap veto unclear.

</details>

### 0003.HK · 香港中华煤气
📅 2026-07-06 ｜ 🏛️ HKEX ｜ [报告](reports/0003.HK/2026-07-06-香港中华煤气-0003.HK.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：典型『冻结股息』公用事业收息股。名义 DPS 已 13 年不变（HK$0.35），2021 年终止送红股后股东回报实质零增长；股息连续 5 年超过每股盈利（派息比率 108–130%），2023–24 年 FCF 覆盖仅约 0.4x，2025 年因资本开支收缩改善至约 0.8x。预扣税…</summary>

典型『冻结股息』公用事业收息股。名义 DPS 已 13 年不变（HK$0.35），2021 年终止送红股后股东回报实质零增长；股息连续 5 年超过每股盈利（派息比率 108–130%），2023–24 年 FCF 覆盖仅约 0.4x，2025 年因资本开支收缩改善至约 0.8x。预扣税 0%（香港注册普通公司，legal_structure）。TTM 净股息率 5.35%（HK$6.54），正常化同为 5.35%，熊市情景 4.3%。当前处于合理持有区（HK$5.00–7.00）上半段，不是有安全边际的买点；HK$5.00 以下（净息率 ≥7%）才进入积累区，<HK$4.00 强力买入。Value-trap veto 未触发，但有两项黄灯。

</details>

### 0823.HK · 领展房产基金
📅 2026-07-06 ｜ 🏛️ HKEX ｜ [报告](reports/0823.HK/2026-07-06-领展房产基金-0823.HK.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：资产优质、负债表 A 级（A/A2/A 稳定）、6.7% 免税收益率真实——香港 REIT 分派在信托层面完税，港人个人持有人 0% 预扣，对比美股 REIT 对港人扣 30%（到手仅 4.7%）。但 DPU 五年内三次下滑，从 FY2022 峰值 HK$3.0567 降至 FY2026 的…</summary>

资产优质、负债表 A 级（A/A2/A 稳定）、6.7% 免税收益率真实——香港 REIT 分派在信托层面完税，港人个人持有人 0% 预扣，对比美股 REIT 对港人扣 30%（到手仅 4.7%）。但 DPU 五年内三次下滑，从 FY2022 峰值 HK$3.0567 降至 FY2026 的 HK$2.5361（累计 −17%，FY2026 再降 6.9%）。组合值 HK$2,160 亿，收入结构：香港零售 50.9%、停车场 20.1%、内地零售 10.9%、澳新 8.5%。TTM 净息率 6.72%（HK$37.76），正常化 6.2–6.6%。现价处于合理持有区上半段，不是有安全边际的买点；积累区 HK$30.0–32.7，强力买入 ≤HK$30.0。末期分派已于 2026-06-11 除净、7 月 28 日派付，下一笔现金待 2026 年 11 月。Veto 未触发。

</details>

### 1088.HK · 中国神华 China Shenhua Energy
📅 2026-07-06 ｜ 🏛️ HKEX ｜ [报告](reports/1088.HK/2026-07-06-中国神华-1088.HK.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：Grade C watchlist; 65% payout floor, zero cut in 18 yrs, net cash, but 2025 FCF cover only 0.68x (capex peak); at HK$46.08 net yield only ~4.5% —…</summary>

Grade C watchlist; 65% payout floor, zero cut in 18 yrs, net cash, but 2025 FCF cover only 0.68x (capex peak); at HK$46.08 net yield only ~4.5% — historically compressed; buy zone <HK$28.3.

</details>

### 6823.HK · 香港电讯 HKT Trust and HKT Limited
📅 2026-07-06 ｜ 🏛️ HKEX ｜ [报告](reports/6823.HK/2026-07-06-香港电讯-6823.HK.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：Grade B core income; 0% withholding; policy = 100% payout of AFF, DPS raised 14 straight years (FY2025 81.77 HK cents, +3.8%); at HK$11.87 net yield…</summary>

Grade B core income; 0% withholding; policy = 100% payout of AFF, DPS raised 14 straight years (FY2025 81.77 HK cents, +3.8%); at HK$11.87 net yield 6.9% — fair/hold zone; accumulate HK$10.93-11.68, strong buy <=HK$10.93; yellow flags: zero retention + net debt/EBITDA ~3.0x.

</details>

### 836.HK · 华润电力 China Resources Power
📅 2026-07-06 ｜ 🏛️ HKEX ｜ [报告](reports/836.HK/2026-07-06-华润电力-836.HK.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：Grade C watchlist; 0% withholding (HK-incorporated); 40% payout ratio executed precisely (FY2025 DPS HK$1.127, 40.2%); TTM net yield 6.5% with no…</summary>

Grade C watchlist; 0% withholding (HK-incorporated); 40% payout ratio executed precisely (FY2025 DPS HK$1.127, 40.2%); TTM net yield 6.5% with no one-off inflation; negative est. FCF in capex-heavy build-out, net debt/equity 150.8%; at HK$17.31 in fair/hold zone, accumulate 12.0-14.7, strong buy <=12.0; veto not triggered.

</details>

### BTI · British American Tobacco
📅 2026-07-06 ｜ 🏛️ NYSE (ADR) ｜ [报告](reports/BTI/2026-07-06-British-American-Tobacco-BTI.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：分红质地为全球烟草中最优之一——数十年未减息、正常化 FCF 覆盖约 1.4x、杠杆回到目标区间、回购逐年加码；FY2025 DPS 上调 2.0% 至 245.04p，六年 CAGR 约 2.6% 且无一年下调，季度等额支付、无特别股息噪音。英国注册公司，股息预扣税 0%，毛息=净息。但…</summary>

分红质地为全球烟草中最优之一——数十年未减息、正常化 FCF 覆盖约 1.4x、杠杆回到目标区间、回购逐年加码；FY2025 DPS 上调 2.0% 至 245.04p，六年 CAGR 约 2.6% 且无一年下调，季度等额支付、无特别股息噪音。英国注册公司，股息预扣税 0%，毛息=净息。但 2025–26 股价大涨（52 周约 +35%，接近历史高位区），股息率已从 2023–24 年的 8–10% 压缩至约 5.3%。公允区 $43.7–54.6（3,267–4,084p），积累区 $41.5–43.7，强力买入 ≤$41.5；当前 $61.76 高于公允区上限，纯收息角度当前价格没有安全边际。质地打 B，价格打『等』。Veto 未触发。

</details>

### 2388.HK · 中银香港 BOC Hong Kong
📅 2026-07-03 ｜ 🏛️ HKEX ｜ [报告](reports/2388.HK/2026-07-03-中银香港-BOC-Hong-Kong-2388.HK.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：Core income; net yield ~4.9%; 56% payout, CET1 24%; dividend very safe, forward growth capped by NIM compression.</summary>

Core income; net yield ~4.9%; 56% payout, CET1 24%; dividend very safe, forward growth capped by NIM compression.

</details>

### GSK.L · GSK plc
📅 2026-07-03 ｜ 🏛️ LSE ｜ [报告](reports/GSK.L/2026-07-03-GSK-plc-GSK.L.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：Quality income watchlist; current yield ~3.3%, buy zone below £17.50.</summary>

Quality income watchlist; current yield ~3.3%, buy zone below £17.50.

</details>

### SHEL · Shell plc
📅 2026-07-03 ｜ 🏛️ NYSE (ADS) ｜ [报告](reports/SHEL/2026-07-03-Shell-plc-SHEL.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：Grade B cyclical income; 0% UK withholding; dividend safe (~3x FCF cover); at ~$78 yield ~3.7% below hist median - buy on weakness (<~$71).</summary>

Grade B cyclical income; 0% UK withholding; dividend safe (~3x FCF cover); at ~$78 yield ~3.7% below hist median - buy on weakness (<~$71).

</details>

### 2318.HK · 中国平安 Ping An Insurance
📅 2026-07-02 ｜ 🏛️ HKEX ｜ [报告](reports/2318.HK/2026-07-02-中国平安-2318.HK.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：Grade B core income; 10% withholding; 13-yr rising DPS (FY2025 RMB 2.70, +5.9%), payout only 36% of operating profit, coverage 2.7x; at HK$52.30 net…</summary>

Grade B core income; 10% withholding; 13-yr rising DPS (FY2025 RMB 2.70, +5.9%), payout only 36% of operating profit, coverage 2.7x; at HK$52.30 net yield 5.25% — fair/hold zone upper band; accumulate HK$38.7-42.9, strong buy <=HK$38.7; -30% drawdown is sector beta, not a dividend crisis; veto not triggered.

</details>

### AZN · AstraZeneca PLC
📅 2026-07-02 ｜ 🏛️ NYSE ｜ [报告](reports/AZN/2026-07-02-AstraZeneca-PLC-AZN.md)

<details>
<summary>结论摘要 Summary (点击展开 / tap to expand)：Watchlist: top-quality, 0% WHT, ~2x-covered progressive dividend, but yield only ~1.6% — a growth compounder, not income at .</summary>

Watchlist: top-quality, 0% WHT, ~2x-covered progressive dividend, but yield only ~1.6% — a growth compounder, not income at .

</details>

最近更新 / Last updated: 2026-08-06 (Asia/Hong_Kong)
