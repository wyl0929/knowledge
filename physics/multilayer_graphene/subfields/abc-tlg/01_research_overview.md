<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-07 15:33:58
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-07 15:33:59
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/multilayer_graphene/subfields/abc-tlg/01_research_overview.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-07
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-07
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/abc-tlg/01_research_overview.md
 * @Description  : ABC 三层石墨烯（菱方堆叠）实验综述
-->
# 01 Research Overview / ABC 三层石墨烯 · 实验综述

Last updated: 2026-07-07

> 系统整理 ABC（rhombohedral）堆叠三层石墨烯（RTG）中的关联电子态实验进展，覆盖 2021–2025。
> 本综述为文献扫描（quick_scan），不生成 gap table 或 project candidates。

---

## 0. ABC vs ABA：为什么 stacking order 决定一切？

在进入实验综述之前，必须理解 ABC 和 ABA 三层石墨烯的本质差异。这个差异决定了为什么 ABA 的 QHE 物理以 FQH 为主，而 ABC 是超导和 Chern 绝缘体的乐园。

### 0.1 晶体结构

```
ABA (Bernal):        ABC (Rhombohedral):
  A — B                A — B
  B — A                C — A
  A — B                B — C
  (有镜像对称)          (无镜像对称，但有空间反演+平移的组合对称)
```

- **ABA**：层 1 和层 3 的碳原子在垂直投影下重合（类 Bernal 双层的外延）
- **ABC**：每层相对下一层平移一个 C-C 键长，三层碳原子在垂直投影下均不重合

### 0.2 低能能带色散

这是两者最关键的物理差异：

| 性质 | ABA（Bernal） | ABC（Rhombohedral） |
|---|---|---|
| 低能色散 | ML 带：$E \propto k$（线性） + BL 带：$E \propto k^2$（二次） | $E \propto k^3$（**三次**！） |
| 零场态密度 | $\propto$ 常数 + $\propto$ 常数 | $\propto k^{-2/3}$ → 发散 |
| 半金属/绝缘体 | 半金属（ML 和 BL 带重叠） | 半金属（能带接触在 K 点） |
| $D$ 场效应 | 调控 ML/BL 带相对位置 | 打开能隙 → 可调谐绝缘体 |
| 磁场下 LL | ML+BL 两套 LL 交叉 | $E_N \propto B^{3/2} N^{3/2}$ |
| hBN 对齐后 | 无摩尔效应 | 摩尔超晶格 → **平带 + 非零 Chern 数** |

**核心直觉**：ABC 的三次色散意味着费米能级附近的态密度极大（$\propto k^{-2/3}$），电子-电子相互作用天然更强。加上 hBN 对齐后的摩尔平带具有非零 Chern 数（$C=\pm 1, \pm 2, \pm 3$），使其成为在零磁场下实现 QAH 和 FQAH 的天然平台——这正是 2024–2025 年的核心突破方向。

---

## 1. 实验发现时间线

```
2021 Q2   Zhou et al. (UCSB) — ABC TLG 中首次发现超导！[E1]
           → Nature 598, 434 (2021) — 引爆整个 rhombohedral graphene 领域
2021 Q3–Q4 理论跟进：10+ 篇理论论文解释 SC 机制
2022       领域扩展至 Bernal 双层（Zhou et al., Science 375, 774）
2023 Q4   Arp et al. (UCSB) — ABC TLG 详细相图：quarter metal, IVC, SOC [E2]
           → Nature Phys. (2024)
2024 Q3   实验爆发期（三组同时）：
           • Patterson et al. (UCSB) — WSe₂ 邻近诱导 SOC 的 SC [E3]
           • Yang et al. (MIT/Long Ju) — SOC 对 SC 的影响 [E4]
           • Choi et al. (UCSB) — Rhombohedral 四层：QAH + SC 共存！[E5]
             → Nature 639, 342 (2025)
2024 Q4   Liu et al. (Weizmann) — STM 直接可视化 IVC 态 [E6]
2025       Yang et al. (MIT) — RTG 中创纪录的 Pauli 极限违反 [E7]
2026       Mayrhofer & Chubukov — 向列相变理论 [T1]（基于近期实验）
```

---

## 2. 核心实验论文详解

---

### [E1] Zhou et al., Nature 598, 434 (2021) — 开山之作

> **Haoxin Zhou, Tian Xie, Takashi Taniguchi, Kenji Watanabe, Andrea F. Young**
> "Superconductivity in rhombohedral trilayer graphene"
> arXiv:2106.07640 → Nature 598, 434 (2021)

**这是整个 rhombohedral graphene 领域的开创性论文。**

**核心发现**：
- 在 hBN 封装的 ABC TLG 双栅器件中，发现了两个独立的超导口袋（superconducting pockets）：SC1 和 SC2
- SC1：出现在 $n \approx -1.5 \times 10^{12}$ cm$^{-2}$（空穴掺杂），$T_c \approx 100$ mK
- SC2：出现在 $n \approx -2.3 \times 10^{12}$ cm$^{-2}$，$T_c \approx 50$ mK
- 超导仅出现在有限位移场 $D$ 范围内，暗示超导与对称性破缺的正常态密切相关

**物理意义**：
- 这是**首个在非转角（crystalline）石墨烯中发现的超导**——不需要魔角！
- ABC TLG 因此成为比 TBG 更简单、更可控的强关联平台
- 超导仅出现在 spin-polarized 和 valley-polarized 的正常态附近（quarter metal 或 half metal），提示配对机制与磁性涨落有关

**器件特征**：
- hBN 封装 → 迁移率 ~10⁵ cm²/Vs
- 双栅结构 → 独立调控 $n$ 和 $D$
- 无需精确转角控制 → 器件制备远比 TBG 简单

---

### [E2] Arp et al., Nature Phys. (2024) — 详细相图：quarter metal, IVC, SOC

> **Trevor Arp, Owen Sheekey, Haoxin Zhou et al. (Andrea Young group)**
> "Intervalley coherence and intrinsic spin-orbit coupling in rhombohedral trilayer graphene"
> arXiv:2310.03781 → Nature Physics (2024), DOI: 10.1038/s41567-024-02560-7

**核心发现**：
- 使用电子压缩率（compressibility）和局域磁强计（local magnetometry）对 ABC TLG 进行了前所未有的详细相图测绘
- 在 **quarter metal** 区域（仅一个 spin-valley flavor 被占据），发现了两种竞争的基态：
  - **Valley-imbalanced (VI) orbital ferromagnet**：谷极化态
  - **Intervalley coherent (IVC) state**：谷间相干态——两个谷的电子波函数形成宏观相干
- 通过对比 VI 和 IVC 相的面内自旋磁化率，**提取了石墨烯的内禀 SOC 强度**：$\lambda \approx 50$ μeV（hBN 封装器件）

**物理意义**：
- 首次在实验中确定了石墨烯的内禀 SOC 能量尺度——这对理解 spin-triplet 超导配对至关重要
- IVC 态的发现为超导配对对称性提供了关键约束：如果是 IVC 涨落介导的配对，则超导可能是 spin-triplet
- 相图显示 VI 和 IVC 之间存在微妙的竞争，解释了超导出现的狭窄参数窗口

---

### [E3] Patterson et al. (Aug 2024) — WSe₂ 邻近 SOC 诱导的超导和 spin canting

> **Caitlin L. Patterson, Owen I. Sheekey, Trevor B. Arp et al. (Andrea Young group)**
> "Superconductivity and spin canting in spin-orbit proximitized rhombohedral trilayer graphene"
> arXiv:2408.10190 (Aug 2024)

**核心发现**：
- 在 ABC TLG 上堆叠 WSe₂ 层（TMD 过渡金属硫族化合物），通过邻近效应引入强 SOC（~meV 量级，比内禀 SOC 大 10–100 倍）
- 邻近 SOC 显著改变了相图：**核化了一个新的超导口袋**
- 同时观察到 spin canting（自旋倾斜）现象——SOC 导致自旋不再严格平行于外磁场

**物理意义**：
- WSe₂ 邻近 SOC 是调控 ABC TLG 关联物理的新"旋钮"
- 与 Long Ju 组（MIT）的独立工作 [E4] 形成互补，共同建立了 SOC-超导-磁性三者关系的实验图景
- 提示 SOC 可能是增强或调控超导 $T_c$ 的手段

---

### [E4] Yang et al. (Aug 2024) — SOC 对超导的影响（Long Ju 组）

> **Jixiang Yang, Xiaoyan Shi, Shenyong Ye et al. (Long Ju group, MIT)**
> "Impact of Spin-Orbit Coupling on Superconductivity in Rhombohedral Graphene"
> arXiv:2408.09906 → Nature Materials (2025, in press)

**核心发现**：
- 独立于 UCSB 组，系统研究了 WSe₂ 邻近 SOC 对 rhombohedral graphene（包括三层和四层）中超导的影响
- SOC 增强超导：在 WSe₂ 邻近的器件中，超导 $T_c$ 更高、超导区域更宽
- 提出了 SOC 通过 Ising 型自旋-轨道耦合稳定 spin-triplet 配对的机制

**与 UCSB 组的互补**：
- UCSB（Young）：聚焦精细相图（compressibility + magnetometry）
- MIT（Ju）：聚焦输运和超导对外场的响应
- 两组独立验证了 SOC 对超导的增强效应

---

### [E5] Choi et al., Nature 639, 342 (2025) — QAH + SC 共存！

> **Youngjoon Choi, Ysun Choi, Marco Valentini et al. (Andrea Young group)**
> "Superconductivity and quantized anomalous Hall in rhombohedral graphene"
> arXiv:2408.12584 → Nature 639, 342 (2025)

**虽然是四层（tetralayer）而非三层，但这是 rhombohedral graphene 系列中最具里程碑意义的论文——必须提及。**

**核心发现**：
- 在 hBN 对齐的 rhombohedral **四层**石墨烯中：
  - **$\nu = -1$ 处观测到量子反常霍尔效应（QAH）**：$R_{xy} = h/e^2$，零磁场下量子化
  - **$\nu \approx -3.5$ 处观测到超导**
  - **$\nu = 2/3$ 处观测到分数 Chern 绝缘体（FCI）**——也稳定在零磁场！
- 栅极电压可以**非易失性切换 QAH 的手征性**（chirality）→ 原则上可以实现可编程拓扑边缘态网络
- WSe₂ 邻近层可以核化新的超导口袋，同时保持 $\nu=-1$ QAH 态的拓扑不变

**为什么是四层而非三层**：
- 四层的 Chern 数更高（$|C|$ 可达 3 或 4），能隙更大，QAH 更 robust
- 但物理机制与三层相同：hBN 摩尔超晶格 + 强关联 → 陈平带 → QAH/SC

**对三层体系的启示**：
- 三层中也可能存在 QAH 和 FCI，但能隙更小、需要更低的温度和更干净的器件
- 2024–2025 年该领域的核心方向之一就是寻找三层中的 QAH/FCI

---

### [E6] Liu et al. (Nov 2024) — STM 直接可视化 IVC 态

> **Yiwen Liu, Ambikesh Gupta, Youngjoon Choi et al. (Weizmann + UCSB)**
> "Visualizing incommensurate inter-valley coherent states in rhombohedral trilayer graphene"
> arXiv:2411.11163 (Nov 2024)

**核心发现**：
- 使用 STM/STS 在实空间中直接成像了 ABC TLG 中的 IVC 态
- 发现 IVC 态表现为**非公度（incommensurate）的电荷密度调制**——波矢不由摩尔周期锁定，而由电子关联决定
- 证实了 Arp et al. [E2] 通过热力学测量间接推断的 IVC 态的存在

**物理意义**：
- 这是 IVC 态在石墨烯体系中的首次直接实空间观测
- 非公度特征提示 IVC 是纯粹的电子关联效应，而非摩尔势的外在驱动

---

### [E7] Yang et al. (Oct 2025) — 创纪录的 Pauli 极限违反

> **Jixiang Yang, Omid Sharifi Sedeh, Chiho Yoon et al. (Long Ju group, MIT)**
> "Magnetic Field-Enhanced Graphene Superconductivity with Record Pauli-Limit Violation"
> arXiv:2510.10873 (Oct 2025)

**核心发现**：
- 在 WSe₂ 邻近的 rhombohedral 三层石墨烯中观测到**自旋极化的超导态（SC5）**
- 面内临界磁场 $B_{c2,\parallel}$ 远超 Pauli 顺磁极限——创石墨烯超导纪录
- 超导在某些磁场范围内被**增强**而非压制

**物理意义**：
- 强烈的 Pauli 极限违反是 spin-triplet 配对的决定性证据之一
- 磁场增强超导是 Ising 型 SOC 保护下的特征行为
- 进一步支持了 ABC TLG 中的超导是 spin-triplet 的理论图景

---

## 3. 关键理论跟进（2021–2023）

ABC TLG 实验发现后，理论界迅速跟进。以下是理解实验所需的关键理论参考：

| 论文 | 核心贡献 | 发表 |
|---|---|---|
| **Chou, Wu, Sau & Das Sarma** — arXiv:2106.13231 | 声学声子介导的超导机制；预言 SC 存在于特定 $n$-$D$ 窗口 | PRL 127, 187001 (2021) |
| **Szabo & Roy** — arXiv:2109.04466 | 平均场 + RG：quarter metal 正常态 + 超导相图 | PRB 105, L081407 (2022) |
| **Chatterjee, Wang, Berg & Zaletel** — arXiv:2109.00002 | IVC 涨落介导的超导配对理论 | Nat. Commun. 13, 6013 (2022) |
| **You & Vishwanath** — arXiv:2109.04669 | Kohn-Luttinger 机制 + IVC 配对 | 预印本 (2021) |
| **Qin, Huang, Wolf, Wei, Blinov & MacDonald** — arXiv:2203.09083 | fRG 研究：配对对称性和机制 | PRL 130, 146001 (2023) |
| **Jimeno-Pozo, Sainz-Cruz, Cea, Pantaleón & Guinea** — arXiv:2210.02915 | Kohn-Luttinger 超导 + SOC 增强 | PRB 107, L161106 (2023) |

### 理论共识与争议

**共识**：
- 超导配对对称性最有可能是 **spin-triplet, valley-singlet**（由 IVC 涨落介导）
- Quarter metal（或 isospin-polarized）正常态是超导的前提条件
- SOC（内禀或邻近）对稳定 spin-triplet 配对起关键作用

**争议**：
- 配对机制：声子 vs 电子关联（IVC 涨落）？→ 两种机制可能共存
- 具体的配对对称性（$p$-wave, $f$-wave？）→ 仍在争论中
- 超导 $T_c$ 的上限在哪里？能否达到液氮温区？→ 未知

---

## 4. 主要实验组概览

| 研究组 | 所在机构 | 核心方向 | 代表论文 |
|---|---|---|---|
| **Andrea F. Young** | UCSB | **绝对主导**：SC 发现、相图、IVC、SOC、QAH+FCI | [E1][E2][E3][E5][E6] |
| **Long Ju** | MIT | SOC 邻近效应、Pauli 极限违反、磁场增强 SC | [E4][E7] |
| **Haim Beidenkopf / Nurit Avraham** | Weizmann | STM 可视化 IVC 态 | [E6]（与 Young 合作） |

**UCSB Young 组的绝对主导地位**：从 2021 年的开山发现到 2025 年的 QAH+SC 共存，Young 组几乎单枪匹马定义了这个领域。这在凝聚态物理中相当罕见——通常一个突破性发现后会有多个组快速跟进，但 rhombohedral graphene 的高质量器件制备难度使 Young 组保持了长时间的领先。

---

## 5. ABC vs ABA 三层石墨烯：实验物理全景对比

| 维度 | ABA（Bernal） | ABC（Rhombohedral） |
|---|---|---|
| **核心物理** | 多带 LL 混合 → even-denom FQH | 三次色散 + hBN 摩尔平带 → SC + QAH |
| **关键调控参数** | $B$（磁场）+ $D$（位移场） | $n$（掺杂）+ $D$（位移场），$B=0$！ |
| **超导** | 无（至今未在 ABA TLG 中发现内禀 SC） | **有**：SC1、SC2、SC5 等多个口袋，$T_c \sim 100$–$300$ mK |
| **量子霍尔** | IQHE + FQH（需 $B \gtrsim 5$ T） | QAH（$B=0$）+ FCI（$B=0$！） |
| **hBN 对齐效应** | 无明显摩尔效应 | **关键**：hBN 摩尔超晶格打开拓扑平带 |
| **SOC 效应** | 不重要 | **重要**：内禀 SOC ~50 μeV，邻近 SOC 可至 meV |
| **器件制备难度** | 中等（需分辨 ABA vs ABC 畴） | 中等（需分辨 stacking + hBN 对齐） |
| **与转角体系关系** | 多带 LL 物理的 reference | 非转角的"魔角替代方案"——物理最接近 TBG |

---

## 6. 与转角三层体系（TMBG/TDBG）的关联

对于本 field pack 的核心关注对象，ABC TLG 实验提供了极为重要的参照：

1. **"最简单的摩尔量子材料"**：ABC TLG + hBN 对齐 = 一种无需精确控制转角就能实现平带 + 拓扑 + 关联的平台。这与 TMBG（需要精确转角 $\theta \approx 1.1^\circ$）形成鲜明对比。

2. **超导机制的普适性**：ABC TLG 和 TBG 的超导都出现在 isospin-polarized 正常态附近 → 提示关联诱导的配对机制可能是摩尔量子材料的普适特征，不依赖于转角。

3. **QAH/FCI 的实现路径**：ABC TLG 系列（尤其是四层）证明了 hBN 摩尔超晶格可以在零磁场下产生 QAH 和 FCI。这提示在 TDBG 等转角体系中，通过精心设计也可以实现零磁场下的拓扑态。

4. **SOC 作为通用调控手段**：ABC TLG 实验中 WSe₂ 邻近 SOC 的成功，为转角体系提供了直接的实验范式——在 TMBG/TDBG 上也尝试 SOC 邻近可能产生新物理。

5. **计算方法论启示**：ABC TLG 的紧束缚建模比转角体系简单得多（只需 6 个原子/原胞，无超大摩尔超晶格），是验证 TBPM QHE 计算代码的理想 testbed。

---

## 7. NEEDS_VERIFICATION 标记

| 内容 | 状态 |
|---|---|
| Zhou et al. (2021) SC1/SC2 的配对对称性是否为 spin-triplet | NEEDS_VERIFICATION — 相敏测量仍未完成 |
| ABC TLG 三层中是否存在零场 QAH/FCI | NEEDS_VERIFICATION — 四层已证实，三层待确认 |
| SC 的配对机制：声子 vs IVC 涨落的主导性 | NEEDS_VERIFICATION — 活跃争论中 |
| $T_c$ 是否能通过 SOC 工程提升到 > 1 K | NEEDS_VERIFICATION — 目前最高 ~300 mK |
| ABC TLG 的紧束缚参数（层间耦合 $\gamma_0, \gamma_1, \gamma_2, \gamma_3, \gamma_4$）是否需要修正 | NEEDS_VERIFICATION — 实验相图可用于约束 TB 参数 |

---

## 8. 推荐阅读路径

1. **入门**：[E1] Zhou et al., Nature 598, 434 (2021) — 开山论文，简短清晰
2. **理解相图**：[E2] Arp et al., Nature Phys. (2024) — 最详细的电子相图
3. **理解前景**：[E5] Choi et al., Nature 639, 342 (2025) — QAH+SC 共存，rhombohedral 系列的制高点
4. **与转角体系对比**：阅读父 pack 的 `01_research_overview.md`，比较 TBG/TMBG 与 ABC TLG 的异同
