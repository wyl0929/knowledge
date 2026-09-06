<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-09-03
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-09-03
 * @FilePath     : /project/knowledge/physics/mirror_symmetric_ttg/Phase_S/tasks.md
 * @Description  : Phase S 执行任务单 — 精读 + 报告撰写
-->
# Phase S 执行任务单

> 创建: 2026-09-03 | 父计划: `Phase_S/plan.md` | 上游: `../paper_search_results.md`（文献搜集，✅ 2026-09-03，v2 编号）
>
> **单一事实源声明**: 16 篇精读清单以本文件为准；`plan.md` §2 保留精读理由与周程，不再维护第二份清单。
>
> **分区规则**:
> - `当前待办（🤖 AI 执行队列）` — run-task 自动执行区
> - `👤 人类任务（仅登记）` — 只做进度追踪，run-task 跳过
> - 状态: ⬜ 待做 / 🔄 进行中 / ✅ 完成
>
> **周程对齐**: Week 1 = Q1 人类精读（8 篇）→ S-REP-2 / S-APP-A | Week 2 = Q2（8 篇）→ S-REP-3 / S-APP-B | Week 3 = Q3 交叉 + S-Q3-MAP / S-REP-4 / S-APP-C + 收尾
>
> **PDF 位置**: 实验 `../references/exp/`（22 篇，含 Cao 2018 TBG 基线）| 理论 `../references/thm/`（24 篇）| 综述 `../references/rev/`（1 篇）
>
> **与 TBG Phase_S 的差异**: 本 pack 全新（无 cards.md），16 篇精读全部为 **P0 人类精读**（从零读原文，产出 8 节 review）；AI 队列只负责依赖精读完成的组装/初稿任务。

> **🔒 质量保证（QC）规范** — 继承 `../../twisted_bilayer_graphene/Phase_S/tasks.md`（强制）:
> - **证据分级**: 每个数据/论断标注 📜Q（原文文字直接支持，附位置）/ 📊F（读图估算）/ 💭I（推断）
> - **禁止无源数字**: 任何数字必须能 grep 到原文全文文本；grep 不到 → 删除或降级为 📊F/💭I
> - **禁止跨论文迁移**: 数据只从所读论文原文取
> - **反向核对 pass**: 每篇 review 完成前，提取全部数字与专名，逐一与原文全文文本比对
> - **报告准入**: report 正文只用 📜Q 条目；📊F 仅入卡片并标 ⚠️；💭I 不入 report
> - **更正日志**: 每篇 review 末尾记录修正历史；人类只审更正日志 + 高风险清单

---

## 当前待办（🤖 AI 执行队列）

> ⚠️ 依赖关系: S-REP-2/S-APP-A 依赖 Week 1 人类精读；S-REP-3/S-APP-B 依赖 Week 2；S-Q3-MAP/S-REP-4/S-APP-C 依赖全部。依赖未满足时执行器应中止并回报，不得跳过。

### [ ] S-REP-2: report.md §2 实验现象综合（初稿）

**目标**: 从 8 篇 Q1 精读组装"实验上观察到了什么"综合章节

**父计划**: `Phase_S/plan.md#四`（report §2）

**输入**: 8 篇 `paper_review_E*.md`（E1/E2/E4/E6/E7/E9/E13/E14）

**执行步骤**:
1. 按 report §2 结构（超导与关联相 / Dirac+flat 谱学 / 位移场可调性 / 遗留问题）归并
2. 每条论断标注来源 review + 证据分级
3. 写入 `report.md` §2

**成功判据**:
- [ ] 8 篇各至少被引用一次
- [ ] 全部数字带 📜Q/📊F/💭I 标注，report 正文只用 📜Q
- [ ] 覆盖"超导/关联相、能带谱学、可调性"三主线

---

### [ ] S-APP-A: 组装 appendix_A 实验表征方法横向对比表

**目标**: 从 Q1 精读提取实验表征手段横向对比表

**父计划**: `Phase_S/plan.md#三`

**输入**: 8 篇 `paper_review_E*.md`

**执行步骤**: 逐篇提取 表征技术（ARPES/STM/输运）/ 可观测量 / 分辨率 / 结论强度 → 横向表 → `Phase_S/appendix_A_methods.md`

**成功判据**:
- [ ] 覆盖 ARPES（E6）、STM（E4/E7/E9）、输运（E1/E2/E13/E14）三类手段
- [ ] 每类技术补方法说明一句话 + 局限

---

### [ ] S-REP-3: report.md §3 理论解释综合（初稿）

**目标**: 从 8 篇 Q2 精读组装"理论上如何解释"综合章节

**父计划**: `Phase_S/plan.md#四`（report §3）

**输入**: 8 篇 `paper_review_*.md`（T1/T2/T3/T4/T5/T10/T13/T21）

**成功判据**:
- [ ] 8 篇各至少被引用一次
- [ ] 覆盖"魔角层级、隐藏对称性、关联态/超导理论、开放张力"四小节
- [ ] 证据分级同 QC 规范

---

### [ ] S-APP-B: 组装 appendix_B 理论谱系演进树

**目标**: 组装理论解释谱系（2019→2026 演进树）

**父计划**: `Phase_S/plan.md#三`

**输入**: 8 篇 Q2 精读 + `paper_search_results.md` 理论表

**执行步骤**: 按时间线组织 → 每节点三要素（假设/预言/局限）→ 演进树（继承/推翻/并存）→ `Phase_S/appendix_B_theory.md`

**成功判据**:
- [ ] 覆盖 T1→T21 全谱系（含 2019 奠基 → 2026 最新）
- [ ] 演进树含继承/并存关系标注（本方向以"并存"为主，少"推翻"）

---

### [ ] S-Q3-MAP: Q3 证据链映射表（人类主导）

**目标**: 逐条验证 flat+Dirac→可调性→超导 的映射链路（见 `plan.md` §2.4）

**父计划**: `Phase_S/plan.md#2.4`

**成功判据**:
- [ ] 每条链路（结构→观测 / 可调性→超导 / 配对机制张力）含理论预言 vs 实验证据对照
- [ ] 每条链路标注确定性等级（confirmed / suspected / NEEDS_VERIFICATION）

---

### [ ] S-REP-4: report.md §4 证据链（人类主导）

**父计划**: `Phase_S/plan.md#四`（report §4）

**输入**: S-Q3-MAP 产物 + 全部精读

**成功判据**:
- [ ] §4 明确回答"假说成立程度"：flat+Dirac→高可调性 有强证据，→超导 是 suspected/NEEDS_VERIFICATION 的区分清晰

---

### [ ] S-REP-5: report.md §5 与个人研究关联（人类主导）

**父计划**: `Phase_S/plan.md#四`（report §5）

**成功判据**:
- [ ] 列出 tbplas 能对标/复现的实验（E6 能带、E1/T21 位移场扫描）与理论（T3/T15）
- [ ] 标注 tbplas 不能做什么（超导配对、强关联）

---

### [ ] S-APP-C: appendix_C 证据分级表（人类主导）

**父计划**: `Phase_S/plan.md#三`

**成功判据**:
- [ ] 假说三环节（flat+Dirac 共存 / 高可调性 / 与超导关联）各成证据条目
- [ ] 与 §4 一致

---

### [ ] S-FMT / S-LOG: 格式化 + 收尾

**目标**: report 全文排版引用统一 + 更新本 pack `99_update_log.md` 与父 `physics/README.md`

**成功判据**:
- [ ] 全部 review + report 引用格式统一（arXiv/DOI）
- [ ] `99_update_log.md` 记录 Phase S 完成

---

## 👤 人类任务（仅登记 — 16 篇精读）

> run-task 跳过本节。精读按 `paper-reading` SKILL 的 8 节模板产出 `paper_review_{ID}.md`。

### Week 1 — Q1 实验精读（8 篇）

### [x] S-Q1-E1: Hao et al. 2021 [2012.02773] — 首个 ATTG 位移场可调超导
- **父计划**: `Phase_S/plan.md#2.2` | **产出**: `note/experiments/paper_review_E1_hao2021_science.md` ✅
- **成功判据**: D 可调超导相图完整；为 Q1 核心实验基准

### [x] S-Q1-E2: Park & Cao et al. 2021 — 强耦合超导（Nature 590, 249）
- **产出**: `note/experiments/paper_review_E2_park2021_nature.md` ✅ | **成功判据**: Tc/TF 与 D 调控数据完整

### [x] S-Q1-E4: Kim et al. 2022 [10.1038/s41586-022-04715-z] — 非常规超导证据（Nature 606, 494）
- **产出**: `note/experiments/paper_review_E4_kim2022_nature.md` ✅（2026-09-04） | **成功判据**: 节点/无节点转变 + peak-dip-hump 论证完整（Q3 入口）
- **注（2026-09-03）**: 原 "E20 Cao [2104.10176]" 为误记——该 arXiv 实为 **Fischer et al. npj Quantum Mater. 7, 5 (2022)**（=T11 理论文）。"Unconventional superconductivity" 的**实验侧**由 **E4（Kim/Nadj-Perge, Nature 606, 494）** 承担。

### [x] S-Q1-E6: Li et al. 2022 [2209.02199] — ARPES 观测 Dirac+flat 共存 ★★
- **产出**: `note/experiments/paper_review_E6_li2022_advmater.md` ✅ | **成功判据**: Dirac 带 + 摩尔平带共存证据完整（假说最硬实验证据）

### [x] S-Q1-E7: Turkel et al. 2022 Science 376, 193 — STM 有序无序
- **产出**: `note/experiments/paper_review_E7_turkel2022_science.md` ✅ | **成功判据**: 无序/关联竞争如何影响超导的论证完整

### [x] S-Q1-E9: Kim et al. 2023 [2304.10586] — STM 成像谷间相干序
- **产出**: `note/experiments/paper_review_E9_kim2023_nature.md` ✅ | **成功判据**: 序参量成像证据完整

### [x] S-Q1-E13: Pierce et al. 2025 [2401.12284] — 轻/重电子可调（Nat. Phys. 21, 1237）
- **产出**: `note/experiments/paper_review_E13_pierce2025_natphys.md` ✅ | **成功判据**: Dirac vs flat 可调性证据完整（"高可调性"实验表达）

### [x] S-Q1-E14: Zhou et al. 2025 [2404.09909] — 双穹顶超导（Nat. Phys. 21, 1773）
- **产出**: `note/experiments/paper_review_E14_zhou2025_natphys.md` ✅ | **成功判据**: 双穹顶相图与范霍夫奇点关系完整

### Week 2 — Q2 理论精读（8 篇）

### [ ] S-Q2-T3: Călugăru et al. 2021 [2102.06201] — 隐藏非局域对称性 ★★（PRB 103, 195411）
- **父计划**: `Phase_S/plan.md#2.3` | **产出**: `note/theory/paper_review_T3.md`
- **成功判据**: Dirac+flat 结构起源 + 位移场破缺对称性论证完整

### [ ] S-Q2-T4: Xie et al. 2021 [2106.14905] — TSTG II 投影 HF 相图（PRB 104, 115167）
- **产出**: `note/theory/paper_review_T4.md` | **成功判据**: 基态相图（关联绝缘/超导候选）完整

### [ ] S-Q2-T1: Khalaf et al. 2019 [1901.10485] — 多层魔角层级（PRB 100, 085109）
- **产出**: `note/theory/paper_review_T1.md` | **成功判据**: mirror-symmetric TTG 出现 Dirac+flat 的层级论证完整

### [ ] S-Q2-T2: Mora et al. 2019 [1901.05469] — 三层平带 + 完美金属（PRL 123, 026402）
- **产出**: `note/theory/paper_review_T2.md` | **成功判据**: 平带 + 完美金属相论证完整

### [ ] S-Q2-T5: Xie, Peng, Zhang & Liu 2022 [2111.06292] — 交替扭转多层配分规则（npj Comput. Mater. 8, 110）
- **产出**: `note/theory/paper_review_T5.md` | **成功判据**: 双平带 + 配分规则完整

### [ ] S-Q2-T10: Christos, Sachdev & Scheurer 2022 [2106.02063] — 关联绝缘+半金属+超导（PRX 12, 021018）
- **产出**: `note/theory/paper_review_T10.md` | **成功判据**: 三相共存理论（Q3 证据链关键）

### [ ] S-Q2-T13: Yu et al. 2023 [2301.04171] — 拓扑重费米子（PRB 108, 035129）
- **产出**: `note/theory/paper_review_T13.md` | **成功判据**: 重费米子图像连接 flat band 与超导完整

### [ ] S-Q2-T21: Liang, Zhao & Zhang 2026 [2606.20849] — 位移场驱动半金属↔超导 ★★🔮
- **产出**: `note/theory/paper_review_T21.md` | **成功判据**: D 驱动半金属↔超导相变论证完整（假说最新直接支撑）

---

## 已完成

### Week 1 — Q1 实验精读（8/8 完成）

| 任务 | 产出 | 状态 |
|------|------|------|
| S-Q1-E1 Hao 2021 | `note/experiments/paper_review_E1_hao2021_science.md` | ✅ 2026-09-03 |
| S-Q1-E2 Park 2021 | `note/experiments/paper_review_E2_park2021_nature.md` | ✅ 2026-09-03 |
| S-Q1-E4 Kim 2022 | `note/experiments/paper_review_E4_kim2022_nature.md` | ✅ 2026-09-04 |
| S-Q1-E6 Li 2022 | `note/experiments/paper_review_E6_li2022_advmater.md` | ✅ 2026-09-03 |
| S-Q1-E7 Turkel 2022 | `note/experiments/paper_review_E7_turkel2022_science.md` | ✅ 2026-09-03 |
| S-Q1-E9 Kim 2023 | `note/experiments/paper_review_E9_kim2023_nature.md` | ✅ 2026-09-03 |
| S-Q1-E13 Pierce 2025 | `note/experiments/paper_review_E13_pierce2025_natphys.md` | ✅ 2026-09-03 |
| S-Q1-E14 Zhou 2025 | `note/experiments/paper_review_E14_zhou2025_natphys.md` | ✅ 2026-09-03 |

> **信息更正汇总（2026-09-03）**：
> - E4（原 E20/E3）：原 "Cao [2104.10176]" 为误记——该 arXiv 实为 Fischer et al. npj Quantum Mater. 7, 5 (2022)（=T11 理论文）；"unconventional SC" 实验侧由 E4（Kim/Nadj-Perge, Nature 606, 494）承担。
> - E13（原 E10）Pierce：期刊实为 **Nat. Phys. 21, 1237 (2025)**，非 "Nature 2024"。
> - E14（原 E11）Zhou：期刊实为 **Nat. Phys. 21, 1773 (2025)**，标题 "Gate-tunable double-dome…"，非 "Nature 2024"。
> - E6 Li：期刊确认为 **Adv. Mater. 34, 2205996 (2022)**。
> - 全部 8 篇均确认 msTTG（mirror-symmetric / alternating-twist）构型。
