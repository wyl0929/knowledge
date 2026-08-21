<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-13 12:40:27
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-19 11:11:24
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/Phase_S/tasks.md
 * @Description  : Phase S2 执行任务单 — 精读 + 报告撰写
-->

# Phase S 执行任务单

> 创建: 2026-08-13 | 父计划: `Phase_S/plan.md` | 上游: `../task_edge_state_search.md`（文献搜集，✅ 已完成 2026-08-06）
>
> **单一事实源声明**: 15 篇精读清单以本文件为准；`plan.md` §2 保留精读理由与周程，不再维护第二份清单。
>
> **分区规则**:
> - `当前待办（🤖 AI 执行队列）` — run-task 自动执行区
> - `👤 人类任务（仅登记）` — 只做进度追踪，run-task 跳过
> - 状态: ⬜ 待做 / 🔄 进行中 / ✅ 完成
>
> **周程对齐**: Week 1 = Q1 人类精读 → S-REP-2 | Week 2 = Q2 → S-REP-3 | Week 3 = Q3 交叉 + S-REP-4/5 + 附录收尾

> **🔒 质量保证（QC）规范** — 2026-08-19 起强制（起因: E4 Yin 2016 精读出现 4 处无源/错标数据）:
> - **证据分级**: 每个数据/论断标注 📜Q（原文文字直接支持，附位置）/ 📊F（读图估算）/ 💭I（推断）
> - **禁止无源数字**: 任何数字必须能 grep 到原文全文文本；grep 不到 → 删除或降级为 📊F/💭I
> - **禁止跨论文迁移**: 数据只从所读论文原文取，不从其他论文/领域常识脑补
> - **反向核对 pass**: 每篇 review 完成前，提取全部数字与专名，逐一与原文全文文本比对
> - **报告准入**: report 正文只用 📜Q 条目；📊F 仅入卡片并标 ⚠️；💭I 不入 report
> - **更正日志**: 每篇 review 末尾记录修正历史；人类只审更正日志 + 高风险清单（📊F/💭I 条目 + 与其他文献矛盾处 + 核心量化结论）

---

## 当前待办（🤖 AI 执行队列）

> ⚠️ 依赖关系: S-REP-2 依赖 Q1 精读；S-REP-3 依赖 Q2 精读；S-FMT / S-LOG 依赖全部完成。依赖未满足时执行器应中止并回报，不得跳过。

### [x] S-APP-A: 组装 appendix_A 实验方法横向对比表

**目标**: 从 Q1 卡片组装实验表征方法横向对比表，作为 report.md 附录 A

**父计划**: `Phase_S/plan.md#三`

**输入**:
- 卡片: `Phase_S/cards.md` Q1 节（实验卡片 E1–E18）
- 精读: `../note/experiments/` + `../note/experiments/`
- 跨领域: `../note/experiments/paper_review_*.md`（Ju 2015 / Li 2016 / Mania 2019 / Zhang 2024）

**执行步骤**:
1. 从 cards.md Q1 节逐篇提取: 表征技术（s-SNOM / STM / 输运 / STEM）、可观测量、边-体区分策略
2. 生成横向对比表: 行=论文，列=技术 / 可观测量 / 分辨率 / 边体区分 / 结论强度
3. 每类技术补一段方法说明（原理一句话 + 适用边界 + 局限）
4. 写入 `Phase_S/appendix_A_methods.md`

**约束**:
- 只使用 cards.md 与已有精读，不新增精读、不臆造数据
- 每个论断标注来源卡片 ID（如 E9）
- QC 强制: 所有数字带证据分级（📜Q/📊F/💭I），📊F/💭I 条目标 ⚠️；无未标注数字

**预期输出**: `Phase_S/appendix_A_methods.md`（3–4 页）

**成功判据**:
- [x] Q1 实验卡片（E1–E18）每篇至少出现一次
- [x] 4 类技术（s-SNOM / STM / 输运 / STEM）各有方法说明
- [x] 与 cards.md 无事实冲突（逐条来源标注）
- [x] QC 检查: 全部数字带证据分级标注，无未标注数字

> 完成记录: [log.md](log.md#ai-0819-T01) → AI: 0819_T01
> ⚠️ 附加产出: §A.5 卡片更正日志（E11 STEM→TEM、E11 ~5 nm 无源、E4 "无磁场"→有 LL 光谱、E10 dG/dV→dG/dn_in、E2 圆偏振光待核、S3 年份 2024→2025、E15 "唯一"→首批），待人类确认后回写 cards.md

---

### [x] S-APP-B: 组装 appendix_B 理论谱系演进树

**目标**: 组装理论解释谱系（2008→2026 演进树），作为 report.md 附录 B

**父计划**: `Phase_S/plan.md#三`

**输入**:
- 卡片: `Phase_S/cards.md` Q2 节（理论卡片 T1–T39）
- 精读: `../note/theory/` + `../note/theory/` + `../note/theory/` + `../note/theory/`

**执行步骤**:
1. 按时间线组织理论节点: 奠基(2008–2013) → 网络模型(2013–2020) → TZM 挑战(2020–2024) → 超越网络(2022–2026)
2. 每个节点提取三要素: 核心假设 / 关键预言 / 已知局限
3. 绘制演进树（mermaid 或缩进文本），标注节点间的继承/推翻/并存关系
4. 写入 `Phase_S/appendix_B_theory.md`

**约束**:
- 只使用 cards.md 与已有精读，不新增精读
- 每个节点标注来源卡片 ID（如 T12）
- QC 强制: 所有数字带证据分级（📜Q/📊F/💭I），📊F/💭I 条目标 ⚠️；无未标注数字

**预期输出**: `Phase_S/appendix_B_theory.md`（3–4 页）

**成功判据**:
- [x] 覆盖 T1–T39 全部理论卡片
- [x] 每个节点含假设/预言/局限三要素
- [x] 演进树含继承/推翻/并存三类关系标注
- [x] QC 检查: 全部数字带证据分级标注，无未标注数字

> 完成记录: [log.md](log.md#ai-0819-T03) → AI: 0819_T03
> ⚠️ 附加产出: §B.5 QC 更正日志累计 **35 条**（三批 PDF 反向核对: AI:0819_T04 / AI:0820_T01 / AI:0820_T02，39 篇理论卡片全部 pdf✓）。cards.md 与 review_T23.md 已回写；其余 23 篇 review 的无源内容修订已登记为任务 **S-REV**（见下）

---

### [x] S-REV: 逐篇修订理论 review 的无源内容（23 篇）

**目标**: 按 `appendix_B_theory.md` §B.5 的 35 条更正日志，逐篇修订理论 review 文件中的无源数字/机制表述，每篇补证据分级与末尾更正日志

**父计划**: `Phase_S/plan.md#2.6`（QC 第二层，Agent 职责）

**输入**:
- 更正清单: `Phase_S/appendix_B_theory.md` §B.5（35 条，含各篇 📜Q 核对结果，**唯一事实源**）
- 已回写卡片: `Phase_S/cards.md` Q2 节（39 卡片已全部 pdf✓，修订后 review 须与卡片一致）
- PDF 原文: `reference/pdfs/`（39 篇理论论文；`pdftotext` 提取后 grep，方法见 /memories/literature-review-qc.md）
- 已完成范例: `note/theory/paper_review_T23_moulsdale2024_acadnano.md`（T04 已修，含更正日志格式）

**待修清单**（23 篇，按 §B.5 条目号）:
- `note/theory/paper_review_T01_martin2008_prl.md`（T1: §B.5#9 4e²/h 加注 + ΔC_v 语言）
- `note/theory/`: efimkin2018（T9 #1 公式）、hou2020（T11 #2 金属→半金属）、tsim2020（T12 #13 置换散射）、fujimoto2021（T13 #14 AB 无源）、debeule2021（T18 #15 周期驱动）、margetis2021（T21 #16 引用无源）
- `note/theory/`: T22（#21）、T24（#22）、T25（#23）、T26（#33）、T27（#24）、T28（#34）、T29（#3 三处数字）、T30（#25）、T32（#26）
- `note/theory/`: T33（#27）、T34（#28）、T35（#4/#5 转角/能隙）、T36（#29）、T37（#30）、T38（#31）、T39（#32）

**执行步骤**:
1. 逐篇: `read_file` 该 review → 对照 §B.5 对应条目与 cards.md 对应卡片
2. 需要再核对处: `pdftotext` 提取对应 PDF → grep 验证 → 用 📜Q 表述替换无源内容
3. 每篇末尾追加「更正日志」节: 日期 + 修正项 + 依据（§B.5 条目号 / PDF grep 位置）
4. 全部完成后更新本任务状态

**约束**:
- 只删改被 §B.5 证伪/无源的内容，不动已 📜Q 核对通过的部分
- 修订后每篇数字必须能 grep 到原文（或标 💭I⚠️）
- review 修订结果与 cards.md / appendix_B 必须三方一致
- 禁止新增精读、禁止引入 §B.5 之外的新论断

**预期输出**: 23 篇 review 文件更新（每篇含证据分级 + 更正日志）

**成功判据**:
- [x] 23 篇全部修订完成，无遗漏
- [x] 每篇末尾有更正日志节
- [x] 无源数字清零（grep 复核 pass）
- [x] 与 cards.md / appendix_B §B.5 无冲突

> 完成记录: [log.md](log.md#ai-0820-T04) → AI: 0820_T04

> 交接说明（来自 AI:0820_T02 会话）: 本任务为新对话独立执行单元，输入已全部固化于磁盘（§B.5 35 条 + cards.md + 39 篇 PDF + log.md 里程碑），不依赖前对话上下文。`/tmp` 下提取文本可能已清空，需自行重新 pdftotext。

---

### ⬜ S-REP-2: report.md §2 初稿（Q1 实验综合）

**目标**: 起草 report.md §2「Edge state 实验上如何表征？」初稿，供人类修订

**父计划**: `Phase_S/plan.md#2.5`

**前置依赖**: S-Q1-E4 / E9 / E10 / E12 / E13 / E14 全部 ✅

**输入**:
- 卡片: `Phase_S/cards.md` Q1 节
- 精读: `../note/experiments/paper_review_E*.md` + `../note/experiments/paper_review_E04_yin2016_natcommun.md`
- 跨领域: `../note/experiments/paper_review_E01_ju2015_nature.md`（E1 交叉引用，不重读）

**执行步骤**:
1. 按 plan.md §四 报告预览结构起草 §2.1–2.4 四小节
2. §2.1 表征技术谱系（s-SNOM / STM / 输运 / STEM）
3. §2.2 每种技术的可观测量和边-体区分策略
4. §2.3 表征演进: 从「存在性验证」到「性质裁决」
5. §2.4 遗留问题: 网络连通性？三层体系？
6. 在文中标注「初稿待人类修订」

**约束**:
- 只引用已完成精读与卡片，不引入未读论文
- 每个论断标注来源（卡片 ID 或 review 文件）
- QC 强制: 正文数字只允许 📜Q 等级；📊F/💭I 不得进入正文论断；跨论文数据须核对其来源论文原文

**预期输出**: `Phase_S/report.md` §2 初稿（3–4 页）

**成功判据**:
- [ ] §2.1–2.4 四小节齐全
- [ ] Q1 七篇（E1/E4/E9/E10/E12/E13/E14）每篇至少引用一次
- [ ] 全文标注「初稿待人类修订」
- [ ] QC 检查: 正文全部数字为 📜Q 等级（有原文文字支持）

---

### ⬜ S-REP-3: report.md §3 初稿（Q2 理论综合）

**目标**: 起草 report.md §3「理论如何解释 edge state？」初稿，供人类修订

**父计划**: `Phase_S/plan.md#2.5`

**前置依赖**: S-Q2-T1 / T5 / T9 / T12 / T15 / T23 / T29 / T35 全部 ✅

**输入**:
- 卡片: `Phase_S/cards.md` Q2 节
- 精读: `../note/theory/paper_review_T01_martin2008_prl.md`、`paper_review_T05_sanjose2013_prb.md`
- 精读: `../note/theory/paper_review_T09_efimkin2018_prb.md`、`paper_review_T12_tsim2020_prb.md`、`paper_review_T15_debeule2020_prl.md`
- 精读: `../note/theory/paper_review_T23_moulsdale2024_acadnano.md`、`paper_review_T29_hou2024_prb.md`
- 精读: `../note/theory/paper_review_T35_li2025_nanolett.md`

**执行步骤**:
1. 按 plan.md §四 报告预览结构起草 §3.1–3.5 五小节
2. §3.1 奠基: valley Chern 数框架（2008–2013）
3. §3.2 网络模型时代（2013–2020）
4. §3.3 TZM 挑战与裁决（2020–2024）
5. §3.4 超越网络: 应变、大转角、非手征（2022–2026）
6. §3.5 开放张力: 网络 vs 独立通道、手征 vs 非手征
7. 在文中标注「初稿待人类修订」

**约束**:
- 只引用已完成精读与卡片，不引入未读论文
- 每个论断标注来源（卡片 ID 或 review 文件）
- QC 强制: 正文数字只允许 📜Q 等级；📊F/💭I 不得进入正文论断；跨论文数据须核对其来源论文原文

**预期输出**: `Phase_S/report.md` §3 初稿（3–4 页）

**成功判据**:
- [ ] §3.1–3.5 五小节齐全
- [ ] Q2 八篇每篇至少引用一次
- [ ] 全文标注「初稿待人类修订」
- [ ] QC 检查: 正文全部数字为 📜Q 等级（有原文文字支持）

---

### ⬜ S-FMT: report.md 排版/引用/交叉链接统一

**目标**: 对 report.md 全文做格式统一、引用规范、附录链接检查

**父计划**: `Phase_S/plan.md#2.5`

**前置依赖**: report.md §0–§5 全部就绪 + appendix_A–D 全部生成

**输入**: `Phase_S/report.md` + `Phase_S/appendix_*.md` + `../14_paper_registry.md`

**执行步骤**:
1. 统一论文引用格式（作者+年份+期刊卷页，附 arXiv ID / DOI / Zotero key）
2. 补 report.md 目录与执行摘要（§0）排版
3. 检查报告正文对 appendix_A–D 的交叉链接有效性
4. 统一表格、标题层级、术语拼写（EFW / LSW / TZM / NQCP）

**约束**:
- 纯机械工作，不改变内容论断

**预期输出**: 格式统一后的 `Phase_S/report.md`

**成功判据**:
- [ ] 全部论文引用含 arXiv ID 或 DOI
- [ ] 附录交叉链接全部有效
- [ ] 标题层级无跳级（## → ### → ####）

---

### ⬜ S-LOG: 更新 99_update_log.md

**目标**: 记录 Phase S 完成状态与新增笔记清单

**父计划**: `Phase_S/plan.md#三`

**前置依赖**: S-FMT ✅

**执行步骤**:
1. 在 `../99_update_log.md` 追加 Phase S 条目: 日期、目标、完成内容、新增/修改文件列表
2. 标注 report.md 交付状态与导师对齐节点结果

**约束**:
- 只追加不删除

**预期输出**: `../99_update_log.md` 新增 Phase S 条目

**成功判据**:
- [ ] 新增文件列表完整（report + 4 附录 + 14 篇 review 更新）

---

## 👤 人类任务（仅登记，不入 AI 执行队列）

### Week 1 — Q1 实验精读（6 篇 + 1 交叉引用）

> E1 Ju 2015 已有精读（domain-wall/），不重读，仅由 S-REP-2 交叉引用。

### [x] S-Q1-E4: Yin 2016 — 双层畴壁边缘态 STM 成像

**父计划**: `Phase_S/plan.md#2.2`

**输入**: `../note/experiments/paper_review_E04_yin2016_natcommun.md` + cards.md E4 卡片

**目标**: 用三问框架补全精读，Q1 早期实验基准

**成功判据**:
- [x] review 含 8 节模板 + Q1 表征视角（技术/可观测量/边体区分）
- [x] cards.md E4 卡片状态 → ✅
- [x] QC 检查: 全部数字带证据分级（📜Q/📊F/💭I），末尾有更正日志

---

### [x] S-Q1-E9: Huang 2018 — STM 首次发现 mTBG 螺旋态

**父计划**: `Phase_S/plan.md#2.2`

**输入**: `../note/experiments/paper_review_E09_huang2018_prl.md`（8 节模板已有）+ cards.md E9 卡片

**目标**: 三问框架重读，确认 Q1 核心实验基准

**成功判据**:
- [x] review 中 Q1 要点与卡片一致、无遗漏
- [x] cards.md E9 卡片状态 → ✅

---

### [x] S-Q1-E10: Rickhaus 2018 — FP+AB 振荡输运

**父计划**: `Phase_S/plan.md#2.2`

**输入**: `../note/experiments/paper_review_E10_rickhaus2018_nanolett.md` + cards.md E10 卡片

**目标**: 三问框架重读，提取 1D 相干性表征数据

**成功判据**:
- [x] review 中 FP/AB 振荡数据与卡片一致
- [x] cards.md E10 卡片状态 → ✅

---

### [ ] S-Q1-E12: Xu 2019 — 巨幅 AB 振荡

**父计划**: `Phase_S/plan.md#2.2`

**输入**: `../note/experiments/paper_review_E12_xu2019_natcommun.md` + cards.md E12 卡片

**目标**: 精读补全，作为 T15 散射理论的实验对标

**成功判据**:
- [ ] review 含 8 节模板，AB 振荡机制描述完整
- [ ] cards.md E12 卡片状态 → ✅

---

### [ ] S-Q1-E13: Verbakel 2021 — 谷保护 FFT 证据

**父计划**: `Phase_S/plan.md#2.2`

**输入**: `../note/experiments/paper_review_E13_verbakel2021_prb.md` + cards.md E13 卡片

**目标**: 三问框架重读，确认 Q1 定论性证据

**成功判据**:
- [ ] review 中 FFT 谷保护论证与卡片一致
- [ ] cards.md E13 卡片状态 → ✅

---

### [ ] S-Q1-E14: Zheng 2022 — 电子 Kagome 晶格

**父计划**: `Phase_S/plan.md#2.2`

**输入**: `../note/experiments/paper_review_E14_zheng2022_prl.md` + cards.md E14 卡片

**目标**: 精读补全，网络干涉产生 2D 超结构的证据链

**成功判据**:
- [ ] review 含 8 节模板，PLL/Kagome 论证完整
- [ ] cards.md E14 卡片状态 → ✅

---

### Week 2 — Q2 理论精读（8 篇）

### [ ] S-Q2-T1: Martin 2008 — EFW 拓扑零模原始理论

**父计划**: `Phase_S/plan.md#2.3`

**输入**: `../note/theory/paper_review_T01_martin2008_prl.md` + cards.md T1 卡片

**成功判据**:
- [ ] review 中 EFW 零模推导与后续理论的逻辑起点清晰
- [ ] cards.md T1 卡片状态 → ✅

---

### [ ] S-Q2-T5: San-Jose & Prada 2013 — 螺旋网络概念起源

**父计划**: `Phase_S/plan.md#2.3`

**输入**: `../note/theory/paper_review_T05_sanjose2013_prb.md` + cards.md T5 卡片

**成功判据**:
- [ ] review 中网络概念与 T9 的承接关系清晰
- [ ] cards.md T5 卡片状态 → ✅

---

### [ ] S-Q2-T9: Efimkin & MacDonald 2018 — 螺旋网络系统理论

**父计划**: `Phase_S/plan.md#2.3`

**输入**: `../note/theory/paper_review_T09_efimkin2018_prb.md` + cards.md T9 卡片

**成功判据**:
- [ ] review 中网络模型预言（FP 振荡来源）与 E10/E14 对标点明确
- [ ] cards.md T9 卡片状态 → ✅

---

### [ ] S-Q2-T12: Tsim 2020 — TZM 推翻网络图景

**父计划**: `Phase_S/plan.md#2.3`

**输入**: `../note/theory/paper_review_T12_tsim2020_prb.md` + cards.md T12 卡片

**成功判据**:
- [ ] review 中 TZM 对网络模型的推翻逻辑完整
- [ ] cards.md T12 卡片状态 → ✅

---

### [ ] S-Q2-T15: De Beule 2020 — 网络散射统一理论

**父计划**: `Phase_S/plan.md#2.3`

**输入**: `../note/theory/paper_review_T15_debeule2020_prl.md` + cards.md T15 卡片

**成功判据**:
- [ ] review 中网络↔TZM 中间地带方案与 E12 对标点明确
- [ ] cards.md T15 卡片状态 → ✅

---

### [ ] S-Q2-T23: Enaldiev 2023 — 非手征 1D 态

**父计划**: `Phase_S/plan.md#2.3`

**输入**: `../note/theory/paper_review_T23_moulsdale2024_acadnano.md` + cards.md T23 卡片

**成功判据**:
- [ ] review 含 8 节模板（若缺失先补全）
- [ ] cards.md T23 卡片状态 → ✅

---

### [ ] S-Q2-T29: Hou 2024 — TZM 裁决 NQCP 电导平台

**父计划**: `Phase_S/plan.md#2.3`

**输入**: `../note/theory/paper_review_T29_hou2024_prb.md` + cards.md T29 卡片

**成功判据**:
- [ ] review 含 8 节模板，NQCP 裁决逻辑完整
- [ ] cards.md T29 卡片状态 → ✅

---

### [ ] S-Q2-T35: Li/Chen/Yao 2025 — 大转角 Umklapp 新机制

**父计划**: `Phase_S/plan.md#2.3`

**输入**: `../note/theory/paper_review_T35_li2025_nanolett.md` + cards.md T35 卡片

**成功判据**:
- [ ] review 含 8 节模板，Umklapp 机制描述完整
- [ ] cards.md T35 卡片状态 → ✅

---

### Week 3 — Q3 交叉串联 + 核心章节（人类主导）

### [ ] S-Q3-MAP: Q3 映射表终稿（五条链路逐条验证）

**父计划**: `Phase_S/plan.md#2.4`

**输入**: cards.md Q3 节 + Week 1/2 全部精读

**成功判据**:
- [ ] 五条映射链路（Martin→Ju/Li、San-Jose→Huang/Rickhaus、Tsim→Hou、De Beule→Xu、Li/Yao→待验证）各含实验证据与理论预言对照
- [ ] 每条链路标注确定性等级

---

### [ ] S-REP-4: report.md §4 理论-实验映射（人类主导）

**父计划**: `Phase_S/plan.md#2.5`

**输入**: S-Q3-MAP 产物 + 全部精读

**成功判据**:
- [ ] §4.1–4.3 三小节齐全，五条链路完整
- [ ] TBPM 在图谱中的位置（§4.3）有明确论断

---

### [ ] S-REP-5: report.md §5 与个人研究关联（人类主导）

**父计划**: `Phase_S/plan.md#2.5`

**输入**: 全部精读 + 本组 TBPM 能力边界（M≤2560、rescale:-1 等约束）

**成功判据**:
- [ ] 明确列出 TBPM 可直接对标/复现/超越的实验与理论清单
- [ ] 标注 TBPM 不能做什么

---

### [ ] S-APP-C: appendix_C 理论-实验对标表（人类主导）

**父计划**: `Phase_S/plan.md#三`

**输入**: 全部精读 + S-Q3-MAP 产物

**成功判据**:
- [ ] 每篇核心理论有其对应的实验对标条目
- [ ] 与 §4 映射链路一致

---

### [ ] S-APP-D: appendix_D 已知/未知/伪 gap 表（人类主导）

**父计划**: `Phase_S/plan.md#三`

**输入**: 全部精读 + cards.md 全节

**成功判据**:
- [ ] 三类 gap（已知/未知/伪）各成条目
- [ ] 伪 gap 标注信息来源（可能被曲解的论断）

---

## 已完成

（暂无）
