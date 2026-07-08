<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-07 15:01:50
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-07 15:01:51
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/multilayer_graphene/subfields/aba-tlg/01_research_overview.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-07
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-07
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/aba-tlg/01_research_overview.md
 * @Description  : ABA 三层石墨烯量子霍尔效应 · 实验论文综述
-->
# 01 Research Overview / ABA 三层石墨烯 QHE · 实验论文综述

Last updated: 2026-07-07

> 系统整理 ABA（Bernal）堆叠三层石墨烯中量子霍尔效应（QHE）的实验研究，重点关注 2023–2025 年的分数量子霍尔效应（FQH）突破。
> 本综述为文献扫描（quick_scan），不生成 gap table 或 project candidates。

---

## 0. 为什么关注 ABA 三层石墨烯的 QHE？

ABA（Bernal）堆叠三层石墨烯是转角多层石墨烯研究的重要**实验 baseline**：

- **与转角体系的关键区别**：ABA TLG 无摩尔超晶格，其低能物理由本征的 monolayer-like 和 bilayer-like 能带构成。在垂直磁场下，两套朗道能级（LL）可以交叉杂化，产生丰富的量子霍尔相图。
- **与转角体系的关联**：转角三层体系（TMBG 等）中，摩尔平带在磁场下也会形成复杂的 LL 谱。理解非转角 ABA TLG 中多能带 LL 混合的基本物理，是理解和预测转角体系中 QHE 的前提。
- **2024–2025 年的实验爆发**：Aveek Bid 组（IISc Bangalore）和 Lei Wang 组（南京大学/HFML）在 ABA TLG 中发现了一系列新的 FQH 态，包括备受关注的 even-denominator 态（可能具有非阿贝尔激发），使 ABA TLG 的 QHE 成为独立于转角体系的活跃前沿。

---

## 1. 物理背景：ABA TLG 的朗道能级结构

### 1.1 零场能带

ABA 堆叠三层石墨烯的低能能带由两套子带组成：

- **Monolayer-like (ML) 带**：线性色散 $E \propto k$，类似于单层石墨烯的 Dirac 锥，有效速度 $v_F \approx 10^6$ m/s。
- **Bilayer-like (BL) 带**：二次色散 $E \propto k^2$，类似于 Bernal 双层石墨烯，有效质量 $m^* \approx 0.03m_e$。

两套能带在 K 点简并或接近简并（取决于层间耦合参数和位移场）。

### 1.2 磁场下的朗道能级

在垂直磁场 $B$ 下：
- ML 带的 LL：$E_N^{\text{ML}} = \pm v_F \sqrt{2e\hbar B |N|}$（$N=0,\pm1,\pm2,\ldots$），包括 $N=0$ 的零能 LL。
- BL 带的 LL：$E_N^{\text{BL}} \propto \pm \sqrt{N(N-1)}$，也具有 $N=0,1$ 的零能 LL。

两套 LL 可以随 $B$ 和位移场 $D$ 交叉杂化，产生可调的 LL 混合（LL mixing）。这种多能带 LL 结构是 ABA TLG 区别于单层和双层石墨烯的核心特征，也是其丰富 FQH 物理的起源。

---

## 2. 经典基准论文（2011–2019）

在进入近期 FQH 突破之前，以下是奠定了 ABA TLG QHE 实验基础的关键论文：

| 年份 | 论文 | 核心贡献 | 研究组 |
|---|---|---|---|
| 2011 | **Kumar et al., PRL 107, 126806** | 首次在 TLG 中观测到整数量子霍尔效应（IQHE），确认 ABA 和 ABC 堆叠的 LL 谱差异 | Goiran/Raquet (Toulouse) |
| 2012 | **Henriksen, Nandi & Eisenstein, PRX 2, 011004** | 双栅极 ABA TLG 中系统性 QHE 和半金属行为研究；位移场 $D$ 调控能带重叠和 LL 交叉 | Eisenstein (Caltech) |
| 2017 | **Datta et al., Nat. Commun. 8, 14518** | 高质量 ABA TLG 器件中强电子相互作用和多个量子霍尔铁磁相 | Deshmukh (TIFR) |
| 2019 | **Stepanov et al., arXiv:1901.02030** | "Quantum Parity Hall effect" — 在 ABA TLG 中观测到由层自由度（parity）导致的独特 QHE 平台序列 | Lau (Ohio State) |

### 关键结论（截至 2019 年）

- ABA TLG 的 IQHE 平台序列在低 $B$ 下表现为 monolayer-like（$\sigma_{xy} = \pm 2, \pm 6, \pm 10, \ldots$ 以 $e^2/h$ 为单位），在高 $B$ 下出现 bilayer-like 特征的混合。
- 位移场 $D$ 可以连续调谐 ML 和 BL 带的相对能量位置，驱动 LL 交叉和拓扑相变。
- 电子-电子相互作用在高质量器件中不可忽略，导致量子霍尔铁磁相和对称性破缺态。
- 但 **FQH 态**在 2019 年之前尚未在 ABA TLG 中被系统观测——这成为 2023–2025 年突破的背景。

---

## 3. 近期实验突破（2023–2025）

### 3.1 概述

2023 年底至 2025 年初，两个实验组——**Aveek Bid 组（IISc Bangalore）** 和 **Lei Wang 组（南京大学/HFML）**——几乎同时独立报道了 ABA TLG 中的分数量子霍尔效应。这是该体系实验研究的重大突破，主要发现包括：

- **Even-denominator FQH 态**（$\nu = 5/2, 7/2, 3/2, 9/2$ 等）：这些半填充态在 GaAs 的 $N=1$ LL 中被认为可能具有非阿贝尔激发（Moore-Read Pfaffian 或 anti-Pfaffian），在石墨烯体系的 $N=0$ LL 中出现令人意外。
- **位移场 $D$ 对 LL mixing 和 FQH 态的精确调控**：$D$ 打破镜像对称性 → 增强 LL mixing → 改变 FQH 态的稳定性和粒子-空穴对称性。
- **FQH 量子相变**：通过调谐 $B$ 和 $D$，可以实现不同 FQH 态之间的量子相变。

### 3.2 核心论文详解

---

#### [P1] Chen et al. (2023) — 首次观测 even/odd denominator FQH

> **Yiwei Chen, Yan Huang, Qingxin Li et al. (Lei Wang group)**
> "Tunable even- and odd-denominator fractional quantum Hall states in trilayer graphene"
> arXiv:2312.17204 (Dec 2023)

**核心发现**：
- 在 Bernal 堆叠 TLG 中观测到一系列 robust FQH 态，包括 even-denominator 态：$\nu = -9/2, -3/2, 3/2, 9/2$。
- 通过调节 $B$ 和 $D$，展示了这些半填充态和邻近 odd-denominator 态之间的量子相变——"此消彼长"（emerging and waning）的行为。

**物理机制**：
- TLG 的多带结构允许 LL 交叉和混合，混合强度可通过 $B$ 和 $D$ 外场调谐。
- Even-denominator 态的出现与特定 LL 轨道成分权重和 LL mixing 强度密切相关。

**与转角体系的关联**：
- 位移场 $D$ 调控 LL mixing 的机制，在原理上与 TDBG/TMBG 中 $D$ 调控拓扑相变类似。
- 这提示在转角多层体系中也可能通过外场调控 FQH 态的稳定性。

---

#### [P2] Kaur, Chanda et al. (2023→2024) — FQH 量子相变的普适性

> **Simrandeep Kaur, Tanima Chanda et al. (Aveek Bid group)**
> "Universality of Quantum Phase Transitions in the Integer and Fractional Quantum Hall Regimes"
> arXiv:2312.06194 → **Nat. Commun. 15, 8535 (2024)**

**核心发现**：
- 系统研究了 ABA TLG 中 IQH 和 FQH 态之间的量子相变，发现 IQH 和 FQH 相变共享相同的普适类。
- 通过 scaling analysis 提取了临界指数，与理论上预期的量子霍尔 Plateau-to-Plateau 相变普适类一致。

**与转角体系的关联**：
- 量子相变的普适 scaling 行为在转角体系中也可以研究（如 TDBG 中 Chern 数变化的拓扑相变）。
- ABA TLG 作为一个"干净"的多带 LL 系统，为理解转角体系中更复杂的相变提供了简化的理论 baseline。

---

#### [P3] Kaur, Singh et al. (2024) — 粒子-空穴对称性的外场调控

> **Simrandeep Kaur, Harsimran Singh et al. (Aveek Bid group)**
> "Controlling particle-hole symmetry of fractional quantum Hall states in trilayer graphene"
> arXiv:2411.18910 (Nov 2024, updated May 2025)

**核心发现**：
- 在 pristine（$D=0$）ABA TLG 中，odd-denominator FQH 态的激发能隙、朗道 g 因子、有效质量和无序展宽在粒子态和空穴共轭态之间**精确相等**——证明了体系具有严格的粒子-空穴对称性（PHS）。
- PHS 源于晶格镜像对称性（lattice mirror symmetry），它禁止了 LL mixing。
- 施加位移场 $D \neq 0$ → 打破镜像对称性 → 促进 ML 和 BL 带的 LL 杂化 → 增强 LL mixing 因子 $\eta$ → 激活三体相互作用 → **显式破缺 PHS**。
- PHS 破缺导致常规 FQH 态被完全去稳定化（destabilized）。

**关键物理区分**：
- ABA TLG 中的 PHS 破缺是**外在的**（extrinsic，由外场 $D$ 驱动），与单层/双层石墨烯最低 LL 中由相互作用内禀驱动的对称性破缺有本质区别。

**与转角体系的关联**：
- 转角体系中位移场 $D$ 同样可以打破层间对称性。Kaur et al. 的工作为理解 $D$ 如何通过 LL mixing 影响 FQH 态稳定性提供了一个清晰、可定量的实验范式。

---

#### [P4] Chanda, Kaur, Singh et al. (2025) — Even-denominator FQH 在 $N=0$ LL 中！

> **Tanima Chanda, Simrandeep Kaur, Harsimran Singh et al. (Aveek Bid group)**
> "Even denominator fractional quantum Hall states in the zeroth Landau level of monolayer-like band of ABA trilayer graphene"
> arXiv:2502.06245 (Feb 2025)

**这是目前 ABA TLG QHE 领域最新、最重磅的实验论文。**

**核心发现**：
- 在 ABA TLG 的 **$N=0$ 朗道能级**（zeroth LL）中观测到 even-denominator FQH 态：**$\nu = 5/2$ 和 $\nu = 7/2$**。
- 这些态出现在 monolayer-like 带和 bilayer-like 带的 LL 交叉处——两条具有不同 isospin 指标的 LL 在能量上重合时。
- Even-denominator 态两侧伴随有 **Levin-Halperin 子态**（daughter states）：$\nu = 7/13$ 和 $\nu = 9/17$——这是 Moore-Read 型非阿贝尔态的"指纹"信号。
- 远离半填充处，观测到标准的 **Jain 序列复合费米子态**。
- 随着 $B$ 增大，even-denominator 态和子态**增强**，而复合费米子态**减弱**。
- 位移场 $D$ 可以精细调谐 LL mixing，进而调控 even-denominator 态的稳定性。

**为什么 $N=0$ LL 中出现 even-denominator 态令人意外？**
- 传统上，even-denominator FQH 态（如 GaAs 中的 $\nu=5/2$）出现在 **$N=1$ LL** 中，因为 $N=1$ LL 的电子波函数具有特定的短程关联特征有利于 Moore-Read 态的形成。
- 在 $N=0$ LL（石墨烯的"相对论性"LL）中观测到 even-denominator 态是出乎预料的。
- 作者提出：ABA TLG 中**缺失空间反演对称性**（absence of inversion symmetry）引入了额外的 isospin 相互作用 → 增强 LL mixing → 软化库仑排斥的短程部分 → 稳定 even-denominator FQH 态。

**实验技术亮点**：
- 使用 hBN 封装的 dual-gated ABA TLG 器件
- 位移场 $D$ 作为独立调控参数（除了 $B$、载流子密度 $n$、温度 $T$ 之外）
- 高质量器件使 FQH 能隙 > 1 K，可在 dilution fridge 温度下清晰分辨

**开放问题**（论文自身提出）：
- Even-denominator 态的拓扑序到底是什么？（Pfaffian vs anti-Pfaffian vs PH-Pfaffian？）
- 非阿贝尔激发的直接实验验证仍待完成（如热导测量、干涉实验等）
- $N=0$ LL 中 Moore-Read 态的理论条件需要重新审视

**与转角体系的关联**：
- 这是目前最清晰的"非转角多层石墨烯中出现潜在非阿贝尔 FQH 态"的实验证据。
- 对于转角体系（如 TDBG 中的 Chern 绝缘体和 FQH），Chanda et al. 的工作提示：摩尔平带的 $C=0$ LL 中是否也可能出现类似的 even-denominator FQH 态？LL mixing 在摩尔体系中的角色如何？
- 位移场 $D$ 调控 LL mixing 的机制可以直接迁移到转角体系的实验设计中。

---

## 4. 相关论文（其他堆叠/构型的 FQH，供对比参考）

| 年份 | 论文 | 体系 | 与 ABA TLG 的关系 |
|---|---|---|---|
| 2024 | **Choi et al., Nature 639, 342 (2025)** — arXiv:2408.12584 | Rhombohedral (ABC) 三层石墨烯 + hBN 摩尔超晶格 | ABC TLG 中的超导和量子化反常霍尔效应；与 ABA TLG 的纯 QHE（磁场必需）形成对比 |
| 2023 | **Xia et al., Nature Phys. 21, 239 (2025)** — arXiv:2310.12204 | 螺旋三层石墨烯 (HTG) | 转角三层体系的拓扑平带 QHE；可与 ABA 的非转角 QHE 对比 |
| 2025 | **Dong et al., arXiv:2507.09908** | 转角多层中高 Chern 数平带的整数和分数 Chern 绝缘体 | $C>1$ 的分数 Chern 绝缘体；ABA TLG 中 $C=0$ LL 的 even-denom FQH 提供了有趣的对比 |

---

## 5. 主要实验组概览

| 研究组 | 所在机构 | 近年 ABA TLG QHE 方向 | 代表性论文 |
|---|---|---|---|
| **Aveek Bid** | IISc Bangalore | **最活跃**：FQH、PHS 破缺、量子相变普适性、even-denominator 态 | [P2][P3][P4] |
| **Lei Wang** | 南京大学 / HFML (合肥) | Even/odd denominator FQH、量子相变 | [P1] |
| **Chun Ning Lau** | Ohio State (现已转至其他机构) | 早期 ABA TLG QHE、Quantum Parity Hall | Stepanov 2019 |
| **J.P. Eisenstein** | Caltech | 经典双栅极 ABA TLG QHE 奠基工作 | Henriksen 2012 |
| **Mandar Deshmukh** | TIFR Mumbai | QH 铁磁相、强关联 | Datta 2017 |

---

## 6. 关键概念速查

| 概念 | 简要解释 | 在 ABA TLG 中的特殊性 |
|---|---|---|
| **Landau level mixing (LL mixing)** | 不同 LL 指标 $N$ 之间的量子相干混合，由 $\eta = E_C / \hbar\omega_c$ 参数化 | 可通过 $D$ 场和 $B$ 场独立调谐，因为有两套 LL（ML+BL）可交叉 |
| **Even-denominator FQH** | 半填充（$\nu = p/2$）处的 FQH 态，候选者为 Moore-Read Pfaffian 等非阿贝尔态 | 在 $N=0$ LL 中出现反常，可能与缺失反演对称性有关 |
| **粒子-空穴对称性 (PHS)** | $\nu \leftrightarrow 2-\nu$（或类似变换）下态的性质不变 | $D=0$ 时精确保持（镜像对称性），$D\neq0$ 时被外在破缺 |
| **位移场 (Displacement field $D$)** | 垂直电场打破层间电势对称性 | ABA TLG 中的核心调控参数，控制 ML/BL 带能量差和 LL mixing |
| **Levin-Halperin daughter states** | Moore-Read 态的"子态"序列，如 $\nu = 7/13, 9/17$ | 在 [P4] 中作为 even-denom FQH 的伴随信号出现 |
| **Isospin** | 谷（valley）+ 层（layer）+ 自旋自由度合称 | ABA TLG 中 ML 和 BL 带具有不同的 isospin 指标，LL 交叉时产生丰富的相图 |

---

## 7. 与转角三层体系 QHE 的关联总结

对于本 field pack 的核心关注对象（多层石墨烯：转角与非转角体系），ABA TLG QHE 实验提供了以下启示：

1. **位移场 $D$ 是一种通用调控手段**：无论是在 ABA TLG 还是在 TDBG/TMBG 中，$D$ 都能通过改变层间电势差来调控能带结构和 LL 混合。ABA TLG 实验提供了 $D$ 调控 FQH 稳定性的最清晰的定量范式。

2. **多带 LL 交叉是丰富关联物态的温床**：ABA TLG 中 ML 和 BL 带的 LL 交叉产生了 even-denominator FQH 态。转角体系中，摩尔平带的不同 $C$（Chern 数）子带之间的类似交叉也可能产生新颖的 FQH 态——目前这仍是开放前沿。

3. **$N=0$ LL 中的 even-denominator FQH 挑战了传统理论**：Chanda et al. (2025) 的发现表明，缺失反演对称性的多带 $N=0$ LL 可以稳定 Moore-Read 型态。转角体系的摩尔平带通常也具有复杂的对称性（或缺失某些对称性），这提示转角体系中可能存在类似甚至更丰富的非阿贝尔 FQH 物理。

4. **实验范式可迁移**：ABA TLG 实验中使用的高质量 hBN 封装 + dual-gate + dilution fridge 技术路线，与转角体系实验基本一致。这意味着 ABA TLG 的实验进展可以快速启发转角体系的实验设计。

---

## 8. NEEDS_VERIFICATION 标记

以下内容基于预印本信息，尚未经过同行评审或需要进一步确认：

| 内容 | 状态 |
|---|---|
| Chanda et al. (2025) 的 even-denom FQH 态是否为 Moore-Read 型 | NEEDS_VERIFICATION — 需要热导或干涉实验确认拓扑序 |
| Chen et al. (2023) 的论文是否已在期刊发表 | NEEDS_VERIFICATION — 截至 2026-07，未见正式期刊出版信息 |
| Kaur et al. (2024) 的 PHS 论文期刊状态 | NEEDS_VERIFICATION — v2 更新于 2025-05，待确认发表 |
| Stepanov et al. (2019) "Quantum Parity Hall" 是否正式发表 | NEEDS_VERIFICATION — arXiv 版本仍为 2019 年，未见期刊信息 |
| Lei Wang 组与 Aveek Bid 组的实验是否有合作/竞争关系 | UNKNOWN — 两组同期发表类似方向，关系待确认 |

---

## 9. 推荐下一步

1. **深入阅读 [P4] Chanda et al. (2025)**：这是当前最前沿的 ABA TLG QHE 实验，包含 even-denominator FQH 的全部关键数据和物理讨论。
2. **对比阅读 [P1] Chen et al. (2023) 和 [P4]**：两组独立观测到 even-denominator FQH，但具体 $\nu$ 序列和物理解释有差异，对比有助于理解全貌。
3. **扩展至 ABC (rhombohedral) TLG**：如果需要更全面地理解三层石墨烯 QHE，ABC TLG（具有平带和更强的关联效应）的实验进展也应追踪。
4. **与转角 TMBG/TDBG 的 QHE 计算交叉验证**：用户已有的 TBPM QHE 计算代码可以在 ABA TLG 上先做 benchmark（朗道能级谱、IQHE 平台），再推广到转角体系。
