# 归档发布与修复

`reports/index.json` 是索引唯一维护入口，格式由 `reports/index.schema.json` 定义。报告正文保存其基准日的研究，不因导航修复而改成当前观点。修复记录见 [ARCHIVE-REPAIRS.md](ARCHIVE-REPAIRS.md)。

每条记录须包含 `as_of_date`、`ticker`、`company`、`exchange`、`path`、`summary`、`score`、`portfolio_role`、`published_at`、`ruleset`、`summary_provenance` 和 `summary_evidence`。评分使用 `75 / B` 形式，等级范围 A–E；无法评估时使用 `Not assessed`。规则 2.5 另支持 `71-81 / B (provisional)`、`40-71 / D-B (provisional)` 和暂定单点评分；数字区间从低到高，等级区间从差到好，不用中点代替区间。发布日期带时区，数据基准日不随修复更新。


`ruleset` 记录报告产生时的规则版本：`pre-2.2`、`2.2`、`2.4` 或 `2.5`。不得为通过归档校验而降低报告规则版本。技能 v2.2 变更了所需收益率推导、预测期长度、收息区间标签、保险行业现金口径与以股代息口径，因此 `pre-2.2` 报告的区间、标签与 veto 结论不得当作当前判断复用；v2.4/v2.5 的质量评分、暂定区间及归档兼容说明见 [MIGRATION.md](MIGRATION.md)。

`summary_provenance` 取 `original_unverified` 或 `repaired_with_evidence`。前者保留原作者摘要文字，允许 `summary_evidence` 为空数组——这是显式记录的豁免，不代表内容已核实；后者必须附非空 `summary_evidence`。以 `ruleset: 2.2`、`2.4` 或 `2.5` 发布的新报告必须为 `repaired_with_evidence`。

每份报告正文开头须有 `dividend-report-meta` 注释块，字段 `ticker`、`company`、`exchange`、`as_of_date`、`published_at`、`ruleset` 与索引一致；索引有 `supersedes` 时注释块须给出相同值，索引没有时注释块也不得出现该字段。缺少注释块会使全部元数据交叉核对失效，因此验证器将其视为错误而非跳过。

港股代码补至至少四位并保留有效五位代码，例如 `0836.HK`。路径为 `reports/<ticker>/<YYYY-MM-DD>-<company-slug>-<ticker>.md`；规则 2.5 还接受同名模式的 `.html` 单文件报告。旧规则仍保留 Markdown 契约，不批量转换或重评历史报告。新文件名采用可读名称与连字符；保留已有合法路径，括号本身不是断链。移动路径时同步所有引用。

摘要为不超过 600 个 Unicode 字符的单行文字，不含表格分隔符。保留原报告的结论、时点与关键限制。修复或重写的关键数字须在 `summary_evidence` 中记录 `field`、`value`、`source_excerpt`，摘录须来自对应原文。原样保留且未补录证据的历史摘要可以为空数组；这不代表其内容已经逐条核实。验证器核对已提供摘录的存在和数字转录，不判断上下文经济含义，也不替代来源审阅。

Markdown 摘要摘录保持原始文本精确匹配，表格摘录包含必要的列分隔符。HTML 摘录匹配静态正文文本：解码字符实体、归一化空白，排除注释、head/script/style/template/noscript、属性值及显式隐藏节点；不向隐藏区域塞入证据数字。解析器不模拟完整 CSS 渲染，发布者仍须核对浏览器可见正文。HTML 必须包含 html/body 元素及 UTF-8 声明。用户要求转换格式时，应实际转换标题、正文、表格、来源与锚点；不得只改扩展名。

同一代码按 `as_of_date`、带时区的 `published_at`、路径依次排序；较新版本的 `supersedes` 必须指向紧邻前版，最早版本不含此字段。保留全部历史报告。记录中的发布时间优先恢复原文声明；若仅能用首次入库提交，则通过 `publication_provenance` 标明 `git_first_add` 与提交号。声明时间、Git 入库时间及其冲突须如实区分。

本地生成时间与归档发布时间分开保留；格式转换不覆盖原研究基准日、生成时间或归档发布时间，可另记转换日期。新规则 2.5 报告按 rubric 2 保留质量／85、收息／15、综合／100、暂定状态及覆盖度；索引 `score` 只承载综合评分及等级，摘要保留其余关键信息。缺项应按规则输出区间，不能把已评估小计、下界或中点当成总分。

安装本地验证依赖后执行：

```text
python -m pip install -r requirements-dev.txt
python -X utf8 scripts/render_index.py
python -X utf8 scripts/validate_archive.py
python -X utf8 -m unittest discover -s tests -v
```

生成器先校验索引，再同步根 README 和全部 ticker README；不修改报告正文。验证器只读检查字段、日期、路径、版本链、已记录数字证据及导航一致性。提交前检查差异，确认没有意外更新投资结论。新报告按用户授权发布；历史修复不能充当收益回测或新版本技能的分析结果。

Markdown 报告可在 GitHub 文件页直接阅读；HTML 文件页可能显示源码，须下载后用浏览器打开，不代表已部署网站。HTML 正文、样式及图表内嵌，不依赖外部资源。本地发布不需要 GitHub Actions、GitHub Pages 或其他托管；推送与合并只针对获授权的仓库和分支，并在完成后核对远端提交、报告与索引。
