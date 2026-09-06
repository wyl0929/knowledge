<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-09-03
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-09-03
 * @FilePath     : /project/knowledge/physics/mirror_symmetric_ttg/Phase_S/plan.md
 * @Description  : Phase S 执行计划书 — mirror-symmetric TTG 文献调研
-->
# Phase S 执行计划书

> 创建: 2026-09-03 | 基于: `../paper_search_results.md`（42 篇：实验 19 + 理论 22 + 综述 1）
>
> **目标**: 回答导师假说，产出结构化调查报告
>
> **导师假说**: 该体系 flat band + Dirac cone 共存的能带结构 → 高可调性 → 与其超导相关。
>
> **三问**: ① 实验上观察到了什么现象？② 理论上做了哪些解释？③ "flat+Dirac 高可调性 → 超导" 这条因果链在文献中有多强的证据？

---

## 一、当前状态审计

### 1.1 已完成工作

| 产出 | 数量 | 位置 |
|---|---|---|
| 结构化文献列表 | **42 篇**（实验 19 + 理论 22 + 综述 1） | `../paper_search_results.md` |
| 体系定义 + 假说 + 三问 | — | `../USER_BRIEF.md` |
| 精读笔记 | **8 篇**（Q1 实验，已完成） | `../note/experiments/` |

### 1.2 待完成 / 前置问题

| 缺口 | 说明 |
|---|---|
| 术语统一 | `multilayer_graphene/11_term_disambiguation.md` §2.1 把 "ATTG=两个独立转角" 与文献 "alternating twist=等转角异号=mirror-symmetric" 冲突，精读前需定稿术语表 |
| 精读 | 8 篇 Q2 理论，另 4–5 篇交叉引用（Q1 实验 8 篇已完成） |
| 报告 | `report.md`（三问综合）+ 附录 |

### 1.3 不做的事项（scope out）

| 方向 | 理由 |
|---|---|
| 螺旋 TTG（Devakul 2023 Sci. Adv.，已从登记表剔除） | 非本构型，仅对比时提及 |
| TMD 摩尔三层（WSe₂/MoTe₂ 等） | 非石墨烯 |
| 大转角 QH / FCI 细节（T14 Hofstadter、T19 FCI） | 偏离 flat band + Dirac 主线，卡片级即可 |
| 配对机制定论 | 文献未定（声子 vs 自旋涨落 vs 量子几何），报告只呈现张力，不下定论 |

---

## 二、Phase S2：精读 + 报告撰写

> 📋 逐篇可执行任务与状态见 `tasks.md`（单一事实源）。本节保留精读理由与周程。

### 2.1 总体时间线

```
Week 1 (Q1): 精读 8 篇实验 → report.md §2 初稿
Week 2 (Q2): 精读 8 篇理论 → report.md §3 初稿
Week 3 (Q3): 交叉串联 flat+Dirac→可调性→超导 证据链 → report.md §4 + 全文
```

### 2.2 Week 1 — Q1 精读：实验现象（8 篇）

| # | 论文 | 精读理由 | 产出 |
|---|---|---|---|
| **E1** | Hao et al., Science 371, 1133 (2021) [2012.02773] | 首个 alternating-twist(mirror-symmetric) TTG 超导，**位移场 D 可调**——Q1 核心实验基准 | `paper_review_E1.md` |
| **E2** | Park & Cao et al., Nature 590, 249 (2021) | 强耦合超导（高 Tc/TF），确立 TTG 超导地位 | `paper_review_E2.md` |
| **E4** | Kim, Choi, … Nadj-Perge, Nature 606, 494 (2022) [10.1038/s41586-022-04715-z] | 非常规超导（节点/无节点转变 + peak-dip-hump）——Q3 配对机制入口 | `paper_review_E4_kim2022_nature.md` ✅ |
| **E6** | Li et al., Adv. Mater. 34, 2205996 (2022) [2209.02199] | **ARPES 直接观测 Dirac 带 + 摩尔平带共存**——导师假说最硬的实验证据 | `paper_review_E6.md` ★★ |
| **E7** | Turkel et al., Science 376, 193 (2022) | STM "有序无序"：平带中关联/无序的竞争如何影响超导 | `paper_review_E7.md` |
| **E9** | Kim et al., Nature 623, 942 (2023) [2304.10586] | STM 成像谷间相干序——序参量直接观测 | `paper_review_E9.md` |
| **E14** | Zhou et al., Nat. Phys. 21, 1773 (2025) [2404.09909] | 双穹顶超导相图——超导与范霍夫奇点的关系 | `paper_review_E14.md` |
| **E13** | Pierce et al., Nat. Phys. 21, 1237 (2025) [2401.12284] | 轻/重电子（Dirac vs flat）可调——"高可调性"的实验表达 | `paper_review_E13.md` |

### 2.3 Week 2 — Q2 精读：理论解释（8 篇）

| # | 论文 | 精读理由 | 产出 |
|---|---|---|---|
| **T3** | Călugăru et al., PRB 103, 195411 (2021) [2102.06201] | **隐藏非局域对称性 + Dirac/flat 能带结构起源**——Q2 核心理论 | `paper_review_T3.md` ★★ |
| **T4** | Xie et al., PRB 104, 115167 (2021) [2106.14905] | 投影 HF 基态相图——关联态理论基线 | `paper_review_T4.md` |
| **T1** | Khalaf et al., PRB 100, 085109 (2019) [1901.10485] | 多层魔角层级——为什么 mirror-symmetric TTG 出现 Dirac+flat | `paper_review_T1.md` |
| **T2** | Mora, Regnault & Bernevig, PRL 123, 026402 (2019) [1901.05469] | 三层 moiré 平带 + 完美金属相 | `paper_review_T2.md` |
| **T5** | Xie, Peng, Zhang & Liu, npj Comput. Mater. 8, 110 (2022) [2111.06292] | 交替扭转多层配分规则 + 双平带——平带"分层"的通用理论 | `paper_review_T5.md` |
| **T10** | Christos, Sachdev & Scheurer, PRX 12, 021018 (2022) [2106.02063] | 关联绝缘体 + 半金属 + 超导三相共存（Sachdev 组）——Q3 关键 | `paper_review_T10.md` ★ |
| **T13** | Yu, Xie, Bernevig & Das Sarma, PRB 108, 035129 (2023) [2301.04171] | 拓扑重费米子图像——连接 flat band 与关联/超导的现代框架 | `paper_review_T13.md` |
| **T21** | Liang, Zhao & Zhang [2606.20849] | **位移场驱动半金属(Dirac)↔超导相变**——假说的最新直接理论支撑 | `paper_review_T21.md` ★★🔮 |

### 2.4 Week 3 — Q3：flat+Dirac 高可调性 → 超导 的证据链（交叉串联）

不新增精读，逐条追踪以下映射链路：

```
T3 (Dirac+flat 结构 + 隐藏对称性)
  └→ E6 (ARPES 直接确认 Dirac+flat 共存)         [结构→观测]
T3/T1 (能带可被 D 连续调)
  └→ E1/E2 (D 可调超导)                           [可调性→超导]
T21 (D 驱动半金属↔超导相变)                       [可调性→超导 的最新理论]
E13 (轻/重电子可调) + E14 (双穹顶)                [可调性的实验表达]
配对机制张力: T11 (自旋涨落) vs T10 (Sachdev) vs T20 (隐藏量子几何) vs R1 (量子几何综述)
```

产出：`report.md` §4（flat+Dirac→可调性→超导 证据分级表，逐条标 confirmed/suspected/NEEDS_VERIFICATION）。

### 2.5 人类 vs Agent 分工

| 任务 | 负责人 |
|---|---|
| P0 精读（16 篇核心） | **人类**（公式细节、声明可靠性、隐藏关联） |
| P1 交叉阅读（4–5 篇备选） | 人类为主 + Agent 摘要 |
| report §2（Q1 实验综合）/ §3（Q2 理论综合） | Agent 初稿 → 人类修订 |
| report §4（flat+Dirac→超导 证据链） | **人类**（原创综合，核心价值） |
| 术语表统一 | 人类定稿（涉及跨 pack 一致性） |
| QC 反向核对 + 排版引用 | Agent |

### 2.6 质量保证（QC）——三层防线

继承 `../../twisted_bilayer_graphene/Phase_S/plan.md` §2.6：

1. **写作时防错**：证据分级 📜Q（原文直接支持）/ 📊F（读图估算）/ 💭I（推断）；禁止无源数字。
2. **写完后查错**：Agent 对每篇 review 提取数字/专名，与 PDF→txt→grep 逐一比对，找不到支持的删除或降级，附录记"更正日志"。
3. **人类抽检**：只查更正日志 + 📊F/💭I 条目 + 文献间矛盾 + report 核心量化结论。

---

## 三、Phase S 交付物清单

| 文件 | 内容 | 状态 |
|---|---|---|
| `plan.md` | 本文件 | ✅ 已完成 |
| `tasks.md` | 16 篇精读清单 + 执行队列 | ✅ 已建（执行中） |
| `report.md` | 回答三问的综合调查报告 | ⬜ 待写 |
| `paper_review_*.md` | 16 篇精读笔记 | 🔄 8/16（Q1 实验 8 篇完成） |
| `appendix_A_methods.md` | 实验表征手段横向对比（ARPES/STM/输运） | ⬜ |
| `appendix_B_theory.md` | 理论解释谱系（2019→2026 演进树） | ⬜ |
| `appendix_C_evidence_chain.md` | flat+Dirac→可调性→超导 证据分级表 | ⬜ 人类主导 |
| `99_update_log.md`（本 pack） | 记录 Phase S 完成 | ⬜ |

---

## 四、报告结构预览

```
report.md
├── 0. 执行摘要（1 页）
│   ├── 调研范围：42 篇，2019–2026
│   ├── 核心发现（3–5 条）
│   └── 假说检验结论：flat+Dirac→高可调性→超导 证据强度
│
├── 1. 引言：为什么关心 mirror-symmetric TTG？（0.5 页）
│
├── 2. 实验上观察到了什么？（3–4 页）
│   ├── 2.1 超导与关联相（Hao/Park/Cao/Zhou double-dome）
│   ├── 2.2 能带谱学：Dirac + flat 共存的直接观测（ARPES/STM）
│   ├── 2.3 可调性：位移场 D 与轻/重电子
│   └── 2.4 遗留问题：配对机制、无序角色
│
├── 3. 理论上如何解释？（3–4 页）
│   ├── 3.1 魔角层级与三层平带（Khalaf/Mora）
│   ├── 3.2 隐藏非局域对称性与 Dirac+flat 起源（Călugăru）
│   ├── 3.3 关联态与超导理论（Sachdev/PHF/重费米子）
│   └── 3.4 开放张力：配对机制未定论
│
├── 4. flat+Dirac 高可调性 → 超导：证据链（2–3 页）
│   └── 逐条映射（见 §2.4），标证据等级
│
├── 5. 与个人研究的关联（1 页）
│   └── tbplas 能算什么（band/DOS，对照 E6 能带；D 场扫描，对照 E1/T21）
│
└── 附录（appendix_A–C）
```

---

## 五、与导师的对齐节点

| 时机 | 发送内容 | 目的 |
|---|---|---|
| **现在** | 本 plan + 文献列表 | 确认三问范围与假说表述 |
| **Week 1 末** | Q1 精读摘要 + report §2 初稿 | 确认实验现象覆盖面 |
| **Week 2 末** | Q2 精读摘要 + report §3 初稿 | 确认理论谱系完整性 |
| **Week 3 末** | report 完整初稿（含证据链分级表） | 获取假说检验结论的反馈 |

---

## 六、参考文献索引

| 用法 | 位置 |
|---|---|
| 结构化文献列表（42 篇全貌 + 标记） | `../paper_search_results.md` |
| 术语统一（待与父 pack 对齐） | `../../multilayer_graphene/11_term_disambiguation.md` §2.1 |
| 精读笔记（16 篇） | `../note/experiments/` 与 `../note/theory/`（待建） |
| QC 规范与长期 memory | `../../twisted_bilayer_graphene/Phase_S/plan.md` §2.6 + `/memories/literature-review-qc.md` |
