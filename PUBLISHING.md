# 归档发布与修复

`reports/index.json` 是索引唯一维护入口，格式由 `reports/index.schema.json` 定义。报告正文保存其基准日的研究，不因导航修复而改成当前观点。修复记录见 [ARCHIVE-REPAIRS.md](ARCHIVE-REPAIRS.md)。

每条记录须包含 `as_of_date`、`ticker`、`company`、`exchange`、`path`、`summary`、`score`、`portfolio_role`、`published_at`、`ruleset`、`summary_provenance` 和 `summary_evidence`。评分使用 `75 / B` 形式，等级范围 A–E；无法评估时使用 `Not assessed`。发布日期带时区，数据基准日不随修复更新。


`ruleset` 记录报告产生时的规则版本：`pre-2.2`、`2.2` 或 `2.4`。不得为通过归档校验而降低报告规则版本。技能 v2.2 变更了所需收益率推导、预测期长度、收息区间标签、保险行业现金口径与以股代息口径，因此 `pre-2.2` 报告的区间、标签与 veto 结论不得当作当前判断复用；v2.4 的价格独立质量评分等记录及归档兼容说明见 [MIGRATION.md](MIGRATION.md)。

`summary_provenance` 取 `original_unverified` 或 `repaired_with_evidence`。前者保留原作者摘要文字，允许 `summary_evidence` 为空数组——这是显式记录的豁免，不代表内容已核实；后者必须附非空 `summary_evidence`。以 `ruleset: 2.2` 或 `2.4` 发布的新报告必须为 `repaired_with_evidence`。

每份报告正文开头须有 `dividend-report-meta` 注释块，字段 `ticker`、`company`、`exchange`、`as_of_date`、`published_at`、`ruleset` 与索引一致；索引有 `supersedes` 时注释块须给出相同值，索引没有时注释块也不得出现该字段。缺少注释块会使全部元数据交叉核对失效，因此验证器将其视为错误而非跳过。

港股代码补至至少四位并保留有效五位代码，例如 `0836.HK`。路径为 `reports/<ticker>/<YYYY-MM-DD>-<company-slug>-<ticker>.md`。新文件名采用可读名称与连字符；保留已有合法路径，括号本身不是断链。移动路径时同步所有引用。

摘要为不超过 600 个 Unicode 字符的单行文字，不含表格分隔符。保留原报告的结论、时点与关键限制。修复或重写的关键数字须在 `summary_evidence` 中记录 `field`、`value`、`source_excerpt`，摘录须来自对应原文。原样保留且未补录证据的历史摘要可以为空数组；这不代表其内容已经逐条核实。验证器核对已提供摘录的存在和数字转录，不判断上下文经济含义，也不替代来源审阅。

摘要摘录保持 Markdown 原始文本精确匹配，表格摘录包含必要的列分隔符。用户要求从其他格式转换时，应实际转换标题、正文、表格、来源与锚点，图表可用等值数据表替代；不得只改扩展名。转换后重新核对可见原文摘录，不添加隐藏数字或改写研究结论来使摘要过检。

同一代码按 `as_of_date`、带时区的 `published_at`、路径依次排序；较新版本的 `supersedes` 必须指向紧邻前版，最早版本不含此字段。保留全部历史报告。记录中的发布时间优先恢复原文声明；若仅能用首次入库提交，则通过 `publication_provenance` 标明 `git_first_add` 与提交号。声明时间、Git 入库时间及其冲突须如实区分。

本地生成时间与归档发布时间分开保留；格式转换不覆盖原研究基准日、生成时间或归档发布时间，可另记转换日期。新报告可采用规则 `2.4` 并将兼容评分记为 `Not assessed`，不得用未完成的质量分项拼成总分。

安装本地验证依赖后执行：

```text
python -m pip install -r requirements-dev.txt
python -X utf8 scripts/render_index.py
python -X utf8 scripts/validate_archive.py
python -X utf8 -m unittest discover -s tests -v
```

生成器先校验索引，再同步根 README 和全部 ticker README；不修改报告正文。验证器只读检查字段、日期、路径、版本链、已记录数字证据及导航一致性。提交前检查差异，确认没有意外更新投资结论。新报告按用户授权发布；历史修复不能充当收益回测或新版本技能的分析结果。

Markdown 报告可在 GitHub 文件页直接阅读。本地发布不需要 GitHub Actions、GitHub Pages 或其他托管；推送与合并只针对获授权的仓库和分支，并在完成后核对远端提交、报告与索引。
