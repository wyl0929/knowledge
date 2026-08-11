<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-11 17:40:29
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-11 17:42:13
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/Phase_S/plan.md
 * @Description  : Phase S 执行计划书 — TBG Edge State / Domain Wall 文献调研
-->

# Phase S 执行计划书

> 创建: 2026-08-11 | 基于: 64 篇粗读卡片 + 27 篇已有精读笔记
>
> **目标**: 回答导师三个问题，产出结构化调查报告
>
> **导师三问**: ① edge state 实验上如何表征？② 理论如何解释？③ 理论如何与实验结合？

---

## 一、当前状态审计

### 1.1 已完成工作（Phase S1）

| 产出 | 数量 | 位置 |
|---|---|---|
| 粗读卡片（Q1/Q2/Q3 三问框架，合并为单文件） | **64 篇** | `Phase_S/cards.md`（522 行，按 Q1/Q2/Q3 三节组织） |
| 已有精读笔记 | **27 篇** | `note/` 下 9 个子目录 |
| 论文 registry | **64 篇**（39T + 18E + 3S + 4R） | `../14_paper_registry.md` |

### 1.2 待完成

| 缺口 | 数量 | 说明 |
|---|---|---|
| 卡片已有但未精读 | **~30 篇** | T22–T39 + E2/E4/E5/E6/E8/E11/E12/E14/E16/E18 + S1–S3 + R1–R4（卡片内容已按 Q1/Q2/Q3 框架完整填充） |
| 跨领域精读（在 `multilayer_graphene/subfields/` 下） | **5 篇** | Ju 2015 / Li 2016 / Mania 2019 / Mahapatra 2022 / Zhang 2024 — cards.md 中标记 ⏭️ 跳过但需在报告中交叉引用 |

### 1.3 不做的事项（scope out）

| 方向 | 理由 |
|---|---|
| T31/T36（Josephson 结畴壁） | 偏离 edge state 表征/解释主线，仅需卡片级了解 |
| T20/T26（关联态、CDW） | 超出 TBPM 单粒子框架，不深入 |
| T33–T39（2024–2026 预印本） | 未同行评审，报告中归入"前沿展望"而非"核心论据" |
| 三层石墨烯畴壁实验（registry §七盲区） | 实验数据极度匮乏，留作后续 Phase |

---

## 二、Phase S2：精读 + 报告撰写

### 2.1 总体时间线

```
Week 1 (Q1): 精读 7 篇实验 → 产出 paper_review + report.md §2 初稿
Week 2 (Q2): 精读 8 篇理论 → 产出 paper_review + report.md §3 初稿
Week 3 (Q3): 交叉重读 15 篇中 theory↔expt 映射链路 → report.md §4 + 全文润色
```

### 2.2 Week 1 — Q1 精读：实验如何表征？（7 篇）

| # | 论文 | 精读理由 | 产出位置 |
|---|---|---|---|
| **E9** | Huang et al., PRL 121, 037702 (2018) | **STM 首次发现 mTBG 螺旋态**——Q1 的核心实验基准 | `note/mTBG_experiments/`（已有，用三问框架重读） |
| **E10** | Rickhaus et al., Nano Lett. 18, 6725 (2018) | **FP+AB 振荡输运**——Q1 中最丰富的表征数据，直接证明 1D 相干性 | `note/mTBG_experiments/`（同上） |
| **E13** | Verbakel et al., PRB 103, 165134 (2021) | **谷保护唯一直接实验证据（FFT）**——Q1 的定论性工作 | `note/mTBG_experiments/`（同上） |
| **E4** | Yin et al., Nat. Commun. 7, 11760 (2016) | **STM 首次成像双层畴壁边缘态**——Q1 的早期实验基准 | `note/non_twisted_experiments/` |
| **E14** | Zheng et al., PRL 129, 076803 (2022) | **电子 Kagome 晶格**——证明网络干涉产生 2D 超结构 | `note/mTBG_experiments/` |
| **E12** | Xu et al., Nat. Commun. 10, 4008 (2019) | **巨幅 AB 振荡**——T15 散射理论的实验对标 | `note/mTBG_experiments/` |
| **E1** | Ju et al., Nature 520, 650 (2015) | **领域奠基实验**——s-SNOM + 输运双探针范式 | ⏭️ 已有精读（domain-wall/），交叉引用 |

### 2.3 Week 2 — Q2 精读：理论如何解释？（8 篇）

| # | 论文 | 精读理由 | 产出位置 |
|---|---|---|---|
| **T1** | Martin et al., PRL 100, 036804 (2008) | **EFW 拓扑零模原始理论**——后续所有理论的逻辑起点 | `note/fundamental_theory/`（已有） |
| **T5** | San-Jose & Prada, PRB 88, 121408(R) (2013) | **螺旋网络概念起源**——mTBG 畴壁物理的开创性理论 | `note/fundamental_theory/`（已有） |
| **T9** | Efimkin & MacDonald, PRB 98, 035404 (2018) | **螺旋网络系统理论**——Q2 的核心解释框架 | `note/helical_network/`（已有，重读） |
| **T12** | Tsim, Nam & Koshino, PRB 101, 125409 (2020) | **TZM 推翻网络图景**——mTBG 畴壁物理的关键转折 | `note/helical_network/`（已有，重读） |
| **T15** | De Beule et al., PRL 125, 096402 (2020) | **网络散射统一理论**——网络 ↔ TZM 之争的中间地带方案 | `note/helical_network/`（已有，重读） |
| **T23** | Enaldiev et al., Acad. Nano 1 (2023) | **非手征 1D 态**——补充纯拓扑图景 | `note/network_theory_advanced/` |
| **T29** | Hou, Yuan & Jiang, PRB 110, L161406 (2024) | **TZM 裁决——NQCP 电导平台**——十年之争的最新答案 | `note/network_theory_advanced/` |
| **T35** | Li, Chen & Yao, Nano Lett. 25, 17025 (2025) | **大转角 Umklapp 新机制**——突破小转角范式，前沿展望核心 | `note/new_directions/` |

### 2.4 Week 3 — Q3：理论如何与实验结合？（交叉串联）

不新增精读，而是基于前两周已读的 15 篇，逐条追踪 `cards.md` Q3 映射表中的每条链路：

```
Martin 2008 ──→ Ju 2015 / Li 2016 (EFW 从预言到验证)
San-Jose 2013 → Efimkin 2018 ──→ Huang 2018 / Rickhaus 2018 (网络模型)
Tsim 2020 → Hou 2024 ──→ 待实验验证 (TZM 从提议到裁决)
De Beule 2020 ──→ Xu 2019 (AB 振荡散射机制)
Li/Chen/Yao 2025 ──→ 待实验验证 (大转角新范式)
```

产出：`report.md` §4（理论-实验映射）终稿 + Q3 映射表终稿。

### 2.5 人类 vs Agent 分工

| 任务 | 负责人 | 说明 |
|---|---|---|
| P0 精读（8 篇） | **人类** | 需要判断力——理解公式细节、评估声明的可靠性、发现隐藏的关联 |
| P1 交叉阅读（7 篇） | **人类为主 + Agent 辅助摘要** | 不需要完整精读报告，但需要理解关键机制 |
| 报告撰写 §2（Q1 综合） | **Agent 初稿 → 人类修订** | Agent 可从卡片 + 精读中组装，人修正不准确之处 |
| 报告撰写 §3（Q2 综合） | **Agent 初稿 → 人类修订** | 同上 |
| 报告撰写 §4（理论-实验映射） | **人类** | 需要原创性综合——这是报告的核心价值，Agent 只能做素材准备 |
| 报告 §5（与个人研究关联） | **人类** | 你的 TBPM 能做什么、不能做什么——Agent 无法替代 |
| 格式化/排版/引用 | **Agent** | 纯机械工作 |

---

## 三、Phase S 交付物清单

| 文件 | 内容 | 预估篇幅 | 状态 |
|---|---|---|---|
| `plan.md` | 本文件 | — | ✅ 已完成 |
| `report.md` | 回答导师三问的综合调查报告 | 10–12 页 | ⬜ 待写 |
| `appendix_A_methods.md` | 实验表征方法横向对比表 | 3–4 页 | ⬜ Agent 组装 |
| `appendix_B_theory.md` | 理论解释谱系（从 2008→2026 的演进树） | 3–4 页 | ⬜ Agent 组装 |
| `appendix_C_theory_expt_map.md` | 每篇核心理论的实验对标 | 3–4 页 | ⬜ 人类主导 |
| `appendix_D_gap_table.md` | 已知/未知/伪 gap 表 | 2–3 页 | ⬜ 人类主导 |
| 15 篇 paper_review_*.md | Q1 (7) + Q2 (8) 精读产出 | 每篇 ~5 页 | ⬜ 待做 |
| `99_update_log.md`（父级） | 记录 Phase S 完成和新增笔记 | — | ⬜ |

---

## 四、报告结构预览

```
report.md
├── 0. 执行摘要（1 页）
│   ├── 调研范围：64 篇论文，2008–2026
│   ├── 核心发现（3–5 条）
│   └── 与本组 TBPM 计算的关联
│
├── 1. 引言：为什么关心 mTBG 的 edge state？（0.5 页）
│
├── 2. Edge state 实验上如何表征？（3–4 页）
│   ├── 2.1 表征技术谱系（s-SNOM / STM / 输运 / STEM）
│   ├── 2.2 每种技术的可观测量和边-体区分策略
│   ├── 2.3 表征的演进：从"存在性验证"到"性质裁决"
│   └── 2.4 遗留问题：网络连通性？三层体系？
│
├── 3. 理论如何解释 edge state？（3–4 页）
│   ├── 3.1 奠基：valley Chern 数框架（2008–2013）
│   ├── 3.2 网络模型时代（2013–2020）
│   ├── 3.3 TZM 挑战与裁决（2020–2024）
│   ├── 3.4 超越网络：应变、大转角、非手征（2022–2026）
│   └── 3.5 开放张力：网络 vs 独立通道、手征 vs 非手征
│
├── 4. 理论如何与实验结合？（2–3 页）
│   ├── 4.1 五条映射链路
│   │   ├── 马丁→李→Ju：EFW 从预言到验证（2008→2015）
│   │   ├── San-Jose→Efimkin→Huang/Rickhaus：网络模型（2013→2018）
│   │   ├── Tsim→Hou：TZM 从提议到裁决（2020→2024）
│   │   ├── De Beule→Xu：AB 振荡理论→巨幅实验（2020→2019）
│   │   └── Li/Chen/Yao：大转角新范式→待实验验证（2025→?）
│   ├── 4.2 理论与实验的反馈模式演变
│   └── 4.3 TBPM 在这张图谱中的位置
│
├── 5. 与个人研究的关联（1 页）
│   └── 你的 TBPM 可以直接对标/复现/超越的实验和理论
│
└── 附录（指向 appendix_A–D）
```

---

## 五、与导师的对齐节点

| 时机 | 发送内容 | 目的 |
|---|---|---|
| **现在** | 本 plan + report.md 目录预览 | 确认方向和覆盖面是否正确 |
| **Week 1 末** | Q1 精读摘要 + report.md §2 初稿 | 确认实验表征的覆盖面和技术细节深度 |
| **Week 2 末** | Q2 精读摘要 + report.md §3 初稿 | 确认理论解释的谱系完整性和张力表达 |
| **Week 3 末** | 报告完整初稿 | 获取修改意见，Q3 映射链路是否自洽 |
| **Week 3 末** | 最终报告 | 交付 |

---

## 六、参考文献索引

| 用法 | 位置 |
|---|---|
| 快速查找某篇论文的粗读卡片 | `cards.md`（合并文件，522 行，按 Q1/Q2/Q3 三节组织，Ctrl+F 定位） |
| 论文的完整精读笔记 | `../note/<子目录>/paper_review_*.md`（9 个子目录，60 篇精读） |
| 跨领域已有精读 | `../multilayer_graphene/subfields/domain-wall/paper_review_*.md` |
| 论文 registry（60 篇全貌） | `../14_paper_registry.md` |
