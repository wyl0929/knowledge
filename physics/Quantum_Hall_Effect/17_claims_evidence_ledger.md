<!--
Field: 量子霍尔效应
Mode: quick_scan
Domain archetype: science_technical
Created date: 2026-06-10
-->

# 17 Claims Evidence Ledger / 中心论断与证据账本

Last updated: 2026-06-10

## Gate verdict / 门控结论

- **概念边界状态**：`resolved` — 11_term_disambiguation.md 已完成 5 组核心概念区分，边界清晰
- **中心论断状态**：`mixed` — 大部分基础论断被充分证实，前沿论断（高温 QAHE、分数陈绝缘体）为 provisional
- **任务可操作化状态**：`provisional` — Chern 数计算任务可完全操作化；$\mathbb{Z}_2$ 计算和输运模拟的操作化需进一步定义

---

## 中心论断台账

### CL-01: IQHE 源于朗道量子化 + 无序局域化

| 项目 | 内容 |
|------|------|
| 论断 | 二维电子气在强磁场下形成离散朗道能级；无序导致体态局域化，边缘态手征输运产生量子化霍尔平台 |
| 证据类型 | 理论推导 + 大量实验 |
| 证据强度 | **confirmed** |
| 证据来源 | TKNN (1982), 标准凝聚态教材, 40 年实验积累 |
| 对下游判断的影响 | IQHE 的计算方法是成熟的，可作为测试基准 |
| 概念边界依赖 | IQHE vs FQHE (11_term) |

### CL-02: FQHE 是强关联拓扑序

| 项目 | 内容 |
|------|------|
| 论断 | FQHE 的物理本质是电子-电子关联导致的不可压缩量子液体，基态有拓扑简并，激发有分数电荷和分数统计 |
| 证据类型 | Laughlin 波函数 + 数值精确对角化 + 实验 |
| 证据强度 | **confirmed**（对基本图像） |
| 证据来源 | Laughlin (1983), Jain 复合费米子 (1989), 广泛数值/实验验证 |
| 未解决问题 | $\nu=5/2$ 的非阿贝尔统计本质（suspected, 未被直接验证） |
| 对下游判断的影响 | FQHE 的多体数值方法壁垒高，不建议用户直接切入 |
| 概念边界依赖 | IQHE vs FQHE, 拓扑序 vs 对称破缺序 |

### CL-03: QAHE 可在零磁场下实现

| 项目 | 内容 |
|------|------|
| 论断 | 磁性拓扑绝缘体中，自旋-轨道耦合 + 内禀磁性 → 非零 Chern 数 → 零场量子霍尔效应 |
| 证据类型 | 理论提出 (Haldane 1988) + 实验实现 (Chang et al. 2013) |
| 证据强度 | **confirmed**（实验层面） |
| 证据来源 | Haldane (1988), Chang et al. Science (2013), 后续多组重复 |
| 限制 | 当前验证温度 ~30 mK–1 K，高温 QAHE 仍为 provisional |
| 对下游判断的影响 | QAHE 材料搜索是可操作的数值研究课题 |
| 概念边界依赖 | QAHE vs QHE, Chern 数 vs 其他不变量 |

### CL-04: Chern 数可通过能带结构可靠计算

| 项目 | 内容 |
|------|------|
| 论断 | 对绝缘体或无能带交叉的系统，Chern 数可以通过 Berry 曲率的布里渊区积分可靠计算，Fukui-Hatsugai-Suzuki 离散方案数值稳定 |
| 证据类型 | 数学定理 (Chern-Weil) + 大量数值验证 |
| 证据强度 | **confirmed** |
| 证据来源 | TKNN (1982), FHS (2005), 广泛代码实现 |
| 对下游判断的影响 | 用户可在 TBPM 框架内实现 Chern 数计算 |
| 概念边界依赖 | Chern 数定义与计算 (11_term) |

### CL-05: $\mathbb{Z}_2$ 不变量计算需要时间反演对称性

| 项目 | 内容 |
|------|------|
| 论断 | $\mathbb{Z}_2$ 拓扑不变量仅在时间反演对称性下良好定义；计算需要跟踪 TRIM 点对的 Berry 联络演化 (Wilson loop) |
| 证据类型 | 理论推导 + 数值验证 |
| 证据强度 | **confirmed** |
| 证据来源 | Fu-Kane (2006), Soluyanov-Vanderbilt (2011) |
| 数值注意 | 非共线自旋和 SOC 使计算复杂度显著增加 |
| 对下游判断的影响 | QSHE 计算比 QAHE 复杂，需确认工具链支持 |

### CL-06: 高温 QAHE 材料可能存在于本征磁性拓扑绝缘体

| 项目 | 内容 |
|------|------|
| 论断 | MnBi₂Te₄ 家族（本征磁性拓扑绝缘体）具备层内铁磁 + 层间反铁磁 + 拓扑非平庸能带，可能在 ~10 K 量级实现 QAHE |
| 证据类型 | 初步实验 + DFT 计算 |
| 证据强度 | **suspected**（正在快速推进中） |
| 证据来源 | NEEDS_VERIFICATION: 具体实验 T_C 和 QAHE 温度的定量关系 |
| 对下游判断的影响 | 该方向是数值研究的黄金机会，但需跟踪实验进展 |
| 概念边界依赖 | QAHE 的定义, 高温 vs 低温的限定 |

### CL-07: 无序对 QAHE 的影响尚未完全理解

| 项目 | 内容 |
|------|------|
| 论断 | QAHE 在理论清洁极限下成立；实际材料中无序可能增强、压制或改变拓扑相 |
| 证据类型 | 模型计算 + 零星实验 |
| 证据强度 | **suspected**（定性理解不完整） |
| 对下游判断的影响 | 无序-拓扑相互作用是 TBPM 方法的强项——用户工具链的价值点 |
| 概念边界依赖 | 拓扑边缘态 vs 平庸边界态 (11_term) |

---

## Operationalization Contract / 任务可操作化契约

### 对下游项目判断的可操作化评估

| 候选任务 | 输入集合 | 目标变换 | 编码/读出 | 指标定义 | 失败判据 | 后选择 | 可操作化状态 |
|---------|---------|---------|----------|---------|---------|--------|:---:|
| Chern 数计算 | TB 哈密顿量 $\{H(\mathbf{k})\}$ | $C = \frac{1}{2\pi}\int_{\text{BZ}} \Omega(k)d^2k$ | FHS 离散格点 + 占据态求和 | $|C - C_{\text{int}}| < 0.01$ | 数值不收敛 / 对 k 网格敏感 | 无（直接积分） | **specified** |
| 无序下 Chern 数 | $H + V_{\text{dis}}(\mathbf{r})$ | 同上有序 + $N_{\text{dis}}$ 平均 | Kubo/GK 公式 + 无序构型采样 | $\sigma_{xy}(E_F)$ 平台宽度 vs 无序强度 | 平台因无序模糊化 → 识阈 | 仅保留化学势在能隙内的构型 | **provisional** |
| $\mathbb{Z}_2$ 计算 | TB + SOC + 非共线自旋 | Wilson loop winding | Wannier 电荷中心演化 | $\mathbb{Z}_2=0$ vs $1$ 区分 | Wilson loop 跳跃歧义 | 无 | **provisional** |
| 输运性质 | $H + leads + disorder$ | $G = \frac{e^2}{h}T$ (Landauer) | TBPM 波包传播 / NEGF | 电导量子化 vs 无序 | 平台不出现 / 非物理振荡 | 带宽截断 | **provisional** |

### 门控最终判断

- **可直接进入 MVP 的任务**：清洁极限下的 Chern 数计算
- **需先验证操作化定义的任务**：无序下的拓扑输运、$\mathbb{Z}_2$ 不变量
- **暂不推荐的任务**：FQHE 数值模拟（方法栈差距大）

允许进入的下游层级：
- introductory_explanation
- provisional_gap
- project_candidate
- mvp_design
- strong_claim_not_allowed

Need verification: NEEDS_VERIFICATION

## Core Claim / 中心论断

Claim ID:

论断内容：

论断类型：
- concept_definition
- mechanism
- phenomenon
- platform_bridge
- novelty
- feasibility
- recommendation
- operationalization

依赖哪些概念边界：

支持哪些下游文件或项目：

证据：

反证或替代解释：

证据状态：
- unresolved
- working_definition
- source_checked
- contested
- rejected

允许用于什么层级的结论：
- introductory_explanation
- provisional_gap
- project_candidate
- mvp_design
- strong_claim_not_allowed

若该论断失效，需要撤回或修改什么：

Need verification: NEEDS_VERIFICATION

Last updated: 2026-06-10

---

## Operationalization Gate / 任务可操作化门

### 任务可操作化结论

准备进入 priority project 或 MVP 的项目必须说明：实验、指标、读出、失败事件和 baseline 是否足以检验项目声称的任务。

### 支撑下游项目的任务定义

- 声称要验证的任务：
- 输入对象与允许输入集合：
- 目标变换：
- 解码或读出要求：
- 失败 / 泄漏 / 后选择处理：
- baseline 公平性要求：
- 阳性结果能证明什么：
- 阳性结果不能证明什么：
- 阴性结果意味着什么：
- operational_status: unspecified / provisional / metric_checked / resource_checked

---

## Ledger Table / 汇总表

| Claim ID | 论断类型 | 论断内容 | 证据状态 | 允许结论层级 | 支持下游文件 | operational_status | Need verification |
|---|---|---|---|---|---|---|---|
|  | concept_definition / mechanism / phenomenon / platform_bridge / novelty / feasibility / recommendation / operationalization |  | unresolved | introductory_explanation |  | unspecified | NEEDS_VERIFICATION |

