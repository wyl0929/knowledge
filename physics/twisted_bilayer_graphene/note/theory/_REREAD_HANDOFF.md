<!--
 * @Author       : AI (2026-09-08 交接)
 * @Description  : 交接文件 — 按理论论文新框架（五块演绎结构）重读 note/theory 下 39 篇 review。供新对话直接执行，自包含。
-->

# 交接文件：理论文章按五块框架重读（note/theory 39 篇）

> **任务一句话**：按 `note/shared/method/theory_paper_reading.md` 的**五块演绎结构**，重读 `note/theory/` 下全部 39 篇理论 review，逐篇重写并归档旧版。
> **为什么重读**：旧 review 分两类——(a) 7 篇按"4 块辨识结构（理论版）"重写过，但这套框架是"系统辨识换轴"，词汇错误（黑箱/四层变量/判别表），已被 §新框架否定；(b) 31 篇是早期粗读（无 TL;DR、60–165 行的叙事体），未按任何结构整理。新框架 = 五块演绎结构，见 `theory_paper_reading.md`。
> **唯一范本**：`note/theory/paper_review_T05_sanjose2013_prb.md`（2026-09-08 已按五块重写，全量反向核对通过）。

---

## 1. 新框架速览（五块演绎结构）

理论论文不是"系统辨识"（黑箱溯因），而是**演绎系统**（白箱演绎）：研究对象是作者自写的理想模型，"未知"在**解的性质**而非模型内部；结构 = `{假设} → 推导链 → {预言/定理 + 合法域}`。

重写时按五块：

```
头部表格(编号/标题/作者/期刊/DOI/类型/PDF/精读日期)
┌ 块1 模型白箱 ──────── 哈密顿量/作用量 + 参数分册 + 显式假设清单
├ 块2 推导链 ────────── 每步"输入→输出→所用假设/定理→合法域"，顺论文演绎顺序
├ 块3 结论清单(分层) ── 每条标"定理 / 估算 / 预言"，注明依赖假设 + 可检验性
├ 块4 假设-结论依赖图 ─ 哪个假设失效 → 哪个结论崩塌（含金量所在）
└ 块5 接口 ──────────── 可检验性 / 设计原则 / 后续文献修正
支撑节 —— 局限与未解决 / 与其他工作的关系 / 对后续的影响
          / 理论模型映射(供计算对标) / 目的接口(三问引用式 + 增量价值)
          / 反向核对 pass / 更正日志
```

**要点**（完整版见 `note/shared/method/theory_paper_reading.md`）：
- **块1 参数分册**替代旧"四层变量表"，**删掉"反推量 θ̂"层**（理论论文不反推自数据）；分四类：自由参数 / 导出量 / 模型内部量 / 预言量。
- **块2 推导链**：论文各节是一条演绎链（典型四层：前提定理层 → 模型层 → 推导层 → 边界层），每步只记"输入→输出→所用近似→合法域"，**不重推代数**；合法域跟着推导记。
- **块3 结论分层**：定理式主张 / 估算 / 预言三类，保留作者动词强度（propose/estimate/believe/find/show）；"没写什么"与"写了什么"同等重要（如未讨论量子化电导 → 显式声明不引入）。
- **块4 假设-结论依赖图**是含金量所在。
- **块5 接口**：跨论文对标（如 T9/T12/T29 对 T5 的修正）标**时间倒挂 💭I**。
- 全文声明"无 ±"，数字统一 📜Q[~]；📊F 几乎不出现，「推导」等级成为主角。

---

## 2. 当前状态清单（39 篇，三类）

| 类 | 结构 | 篇数 | 处理 |
|---|---|---|---|
| **A** | 五块（新框架） | 1 | ✅ 已完成，跳过 |
| **B** | 4 块辨识结构（旧框架，需按五块重写） | 7 | 批次 1（= S-Q2 队列） |
| **C** | 旧叙事/粗读（无 TL;DR，60–165 行） | 31 | 批次 2（从粗读到五块精读） |

**A 类（已完成，跳过）**：T05 San-Jose & Prada 2013。

**B 类（4 块 → 五块重写，7 篇，均为 Phase S S-Q2 队列篇目）**：

| 编号 | 论文 | 现有 review 行数 | S-Q2 任务 | cards 状态 |
|---|---|---|---|---|
| T01 | Martin 2008 PRL（EFW 拓扑零模） | 277 | S-Q2-T1 [ ] | 待 → ✅ |
| T09 | Efimkin & MacDonald 2018 PRB（螺旋网络系统理论） | 263 | S-Q2-T9 [ ] | 待 → ✅ |
| T12 | Tsim 2020 PRB（TZM 推翻网络） | 248 | S-Q2-T12 [ ] | 待 → ✅ |
| T15 | De Beule 2020 PRL（散射统一） | 262 | S-Q2-T15 [ ] | 待 → ✅ |
| T23 | Moulsdale 2024 ACS Nano（非手征 1D 态） | 235 | S-Q2-T23 [ ] | 待 → ✅ |
| T29 | Hou 2024 PRB（NQCP 裁决） | 260 | S-Q2-T29 [ ] | 待 → ✅ |
| T35 | Li 2025 Nano Lett（大转角 Umklapp） | 231 | S-Q2-T35 [ ] | 待 → ✅ |

> ⚠️ S-Q2-T23 任务标题写"Enaldiev 2023"，但输入 review/PDF 实为 **Moulsdale, Enaldiev, Geim & Fal'ko 2024 ACS Nano**（同一篇，作者含 Enaldiev）。执行以文件名 `T23_moulsdale2024` 为准。

**C 类（旧叙事/粗读 → 五块精读，31 篇）**：
T02 Li 2010 · T03 Jung 2011 · T04 Qiao 2011 · T06 Zhang 2013 · T07 Vaezi 2013 · T08 Jaskólski 2016 · T10 Ramires 2018 · T11 Hou 2020 · T13 Fujimoto 2021 · T14 Chou 2020 · T16 Thomson 2021 · T17 Padhi 2020 · T18 De Beule 2021 · T19 Chou 2021 · T20 Kwan 2021 · T21 Margetis 2021 · T22 Sinner 2023 · T24 Hsu 2023 · T25 Wittig 2023 · T26 Wang 2024 · T27 Georgoulea 2024 · T28 Mondal 2023 · T30 Wittig 2024 · T31 Kundu 2024 · T32 Ghadimi 2024 · T33 Sanchez-Sanchez 2024 · T34 Wen 2024 · T36 Du 2025 · T37 McDowell 2026 · T38 Hung 2026 · T39 Phong 2026

（C 类 31 篇中 T33/T37/T38/T39 为 arXiv 预印本，期刊/年份以原文为准。）

---

## 3. 执行优先级

1. **批次 1（先做）**：B 类 7 篇，按 S-Q2 队列顺序 **T01 → T09 → T12 → T15 → T23 → T29 → T35**。这是 Phase S Q2 理论综合（S-REP-3）的前置依赖，价值最高。
2. **批次 2（后做）**：C 类 31 篇，建议按**主题聚类**而非编号：畴壁 TPH 先驱（T02/T03/T04/T06/T07/T08）→ 网络模型与散射（T10/T11/T14/T16/T17/T18/T19/T20/T21）→ 非手征/局域态（T22/T24/T25/T30）→ 关联/应变/异质应变（T26/T27）→ 近年新机制（T28/T31/T32/T33/T34/T36）→ 前沿预印本（T37/T38/T39）。

---

## 4. 每篇执行流程（标准操作）

1. **定位 PDF**：`reference/pdfs/` 下按 review 头部"PDF"字段；若头部无，用作者关键词 glob（如 `reference/pdfs/*Sinner*`）。**若 PDF 缺失**：标 `NEEDS_VERIFICATION`，跳过该篇并在台账注明。
2. **提取**：`pdftotext -layout "<pdf>" /tmp/TXX.txt`（公式类再用 `-raw` 复核）。
3. **精读**：读摘要分诊（确认是理论论文）→ 按五块逐块填（模型白箱 → 推导链 → 结论清单 → 假设依赖图 → 接口）。
4. **QC 反向核对**：全文数字/公式逐一 grep 原文，找不到 → 删除或降级 💭I/📊F；OCR 公式破碎（分数/根号/ħ）用 `-raw` + 公式自洽反推双确认。
5. **四个陷阱 + 两险点检查**（见 §6）。
6. **重写 review**（五块），**旧版归档**：`cp note/theory/paper_review_TXX_*.md archive/paper_review_TXX_*.backup_$(date +%Y%m%d).md`。
7. **更新台账**：批次 1 更新 `Phase_S/tasks.md`（S-Q2-TXX → [x] + 完成记录）与 `Phase_S/cards.md`（卡片 → ✅ + 补"关键参数"）；批次 2 更新 cards.md 卡片状态（若卡片存在）。

---

## 5. 验收判据（每篇）

- [ ] 五块齐全，块1 有显式假设清单、块4 有假设-结论依赖图
- [ ] 全部数字/公式 grep 命中原文（📜Q），无无源数字
- [ ] 结论按"定理/估算/预言"分层，保留作者动词强度
- [ ] 四陷阱检查通过（无后世语言污染 / 无脑补参数 / 无推演当原文 / 无预言写成事实）
- [ ] 跨论文对标标时间倒挂 💭I
- [ ] 旧版已归档 `archive/`，更正日志含本次重写条目
- [ ] 台账已更新（批次 1：tasks.md + cards.md；批次 2：cards.md）

---

## 6. 关键注意事项

1. **词汇纪律**：理论 review **只用白箱演绎词汇**（模型白箱/推导链/结论清单/假设-结论依赖图），**不出现**"黑箱三要素/四层变量/判别表/可辨识实验"这类实验框架词（除非在"为什么不用"的说明里）。这是本次重读与旧 4 块版的根本区别。
2. **四个陷阱**：① 后世语言污染（Chern/Z₂/"闭合-重开"，grep 证伪后标 💭I）；② 常识脑补参数（原文没有的数值，如 t⊥≈0.4 eV，数值+eV grep 删除）；③ 推演当原文（如 4e²/h 须标 [推导] 且核对谷×自旋×方向，原文未讨论的量显式声明不引入）；④ 预言写成事实（保留 propose/predict/may have implication）。
3. **两险点**：OCR/公式破碎（`-raw` + 自洽反推）；符号家族歧义（同字母不同层，如 γ⊥ vs l⊥）。
4. **证据分级**：📜Q（原文，附位置）/ 推导 / 📊F（读图）/ 💭I（推断）；不确定度轴 [±]/[~]/[读图]/[相对]；理论论文全文无 ± → 统一 📜Q[~]。QC 唯一权威：`/home/wyl/.agents/skills/paper-reading/references/LITERATURE_QC_PROTOCOL.md`。
5. **三层分离**：通用物理（valley Chern / Landauer-Büttiker / miniband 等）锚点引用 `note/shared/physics/`（[PHY-*]），不复制讲义；锚点表见 `note/shared/README.md`。
6. **共享物理锚点**：理论篇主要用 `[PHY-BERRY]`、`[PHY-LB]`、`[PHY-MB]`、`[PHY-GATE]`、`[PHY-AB]`。
7. **归档约定**：`archive/paper_review_TXX_*.backup_YYYYMMDD.md`（项目根 `archive/` 目录，已有 E 系列样例可参照）。

---

## 7. 相关文档路径索引

| 用途 | 路径 |
|---|---|
| 理论方法+五块模板（权威） | `note/shared/method/theory_paper_reading.md` |
| 入口/公共规范（目的层·三层分离·证据分级·三档） | `note/shared/method/paper_reading_methodology.md` |
| 理论阅读案例/范本/检查清单 | `note/shared/method/theory_paper_reading_case_T05.md` |
| 五块落地范本（对照用） | `note/theory/paper_review_T05_sanjose2013_prb.md` |
| QC 协议（唯一权威） | `/home/wyl/.agents/skills/paper-reading/references/LITERATURE_QC_PROTOCOL.md` |
| 笔记模板 | `/home/wyl/.agents/skills/paper-reading/templates/paper_review.md` |
| 机制五问 | `note/shared/method/mechanism_questions.md` |
| 共享物理锚点表 | `note/shared/README.md` |
| 台账 | `Phase_S/tasks.md`（S-Q2 队列）、`Phase_S/cards.md`（T 卡片）、`Phase_S/log.md`（执行日志，追加） |
| PDF | `reference/pdfs/` |

---

## 8. 交接边界（本次对话已完成 / 新对话待做）

**已完成**：方法论定型（入口/实验/理论三份文档）+ T05 按五块重写 + 本交接文件。

**待做（新对话）**：按 §3 优先级、§4 流程重读 38 篇（B 类 7 + C 类 31），逐篇过 §5 验收。

**执行日志**：每篇完成后在 `Phase_S/log.md` 追加一条（格式参照已有 `ai-0908-T01`）。

---

*创建: 2026-09-08 | 供新对话执行*
