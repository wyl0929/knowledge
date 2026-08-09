<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-21
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/abc-tlg/note_ll_valley_splitting_theory.md
 * @Description  : ABC TLG 高场 LL 谷分裂相关理论文献扫描
-->
# ABC TLG 高场 LL 谷分裂 · 相关理论文献扫描

Last updated: 2026-07-21

> Yin et al. ([PRL 122, 146802, 2019](https://doi.org/10.1103/PhysRevLett.122.146802)) 在 ABC TLG 中观测到 $\Delta_V \propto B$ 且随 LL 指数 $N$ 急剧衰减，称其 "beyond the description of any existed theory"。本扫描整理了 2019 年前后与此问题直接/间接相关的理论文献。
>
> **关键结论：2019 年后无直接解释该观测的理论论文。最近的直接相关理论来自 2011–2013，后续理论主要研究零场关联态。**
>
> ✅ 全部 7 篇文献已通过 arXiv 验证真实性并添加 DOI 链接 (2026-07-21 核实)。

---

## 一、2019 年前：最接近解释 LL 谷分裂的理论基础（3 篇）

### [T1] Shizuya — PRB 87, 085413 (2013)
> arXiv:[1212.0338](https://arxiv.org/abs/1212.0338) · DOI:[10.1103/PhysRevB.87.085413](https://doi.org/10.1103/PhysRevB.87.085413)
> "Orbital Lamb shift and mixing of the pseudo-zero-mode Landau levels in ABC-stacked trilayer graphene"

- **机制**：Coulomb 真空涨落 → **orbital Lamb shift** + pseudo-zero-mode LL 之间的混合
- **与实验关联**：解释了为什么低 $N$ LL 的劈裂更大——低 $N$ LL 波函数更局域 → Coulomb 涨落效应更强
- **不足**：未预测 $\Delta_V$ 的 $B$ 线性标度

### [T2] Côté, Rondeau, Gagnon & Barlas — PRB 86, 125422 (2012)
> arXiv:[1208.2237](https://arxiv.org/abs/1208.2237) · DOI:[10.1103/PhysRevB.86.125422](https://doi.org/10.1103/PhysRevB.86.125422)
> "Phase diagram of insulating crystal and quantum Hall states in ABC-stacked trilayer graphene"

- **方法**：Hartree-Fock，聚焦 $N=0$ triplet LL
- **核心**：Coulomb 交换相互作用 vs 单粒子 orbital splitting 的**竞争**→ 决定了基态是 QH 态还是电荷密度波
- **与实验关联**：定性解释了 $N=0$ LL 的劈裂增强来源于交换相互作用
- **不足**：仅覆盖 $N=0$，未系统处理 $N=1,2,\ldots$ 的 $\Delta_V(N)$ 衰减

### [T3] Barlas, Côté & Rondeau — PRL 109, 126804 (2012)
> arXiv:[1112.2729](https://arxiv.org/abs/1112.2729) · DOI:[10.1103/PhysRevLett.109.126804](https://doi.org/10.1103/PhysRevLett.109.126804)
> "Quantum Hall to charge-density-wave phase transitions in ABC-trilayer graphene"

- **方法**：Hartree-Fock，$n=0,1,2$ orbital triplet
- **核心**：单粒子 LL splitting 驱动 QH ↔ CDW 相变
- **与实验关联**：为理解 LL 指数 $N$ 如何影响基态选择提供了框架
- **不足**：主要关注相变临界条件，未直接计算 $\Delta_V(B,N)$

---

## 二、2019 年后：零场关联态相关理论（4 篇，间接相关）

> 这些论文研究 ABC/Rhombohedral graphene 中的谷极化、对称性破缺和关联态，但**均在零场或低场**，不直接解释高场 LL 的 $\Delta_V(B,N)$。

### [T4] Huang, Wolf, Qin, Wei, Blinov & MacDonald — PRB 107, L121405 (2023)
> arXiv:[2203.12723](https://arxiv.org/abs/2203.12723) · DOI:[10.1103/PhysRevB.107.L121405](https://doi.org/10.1103/PhysRevB.107.L121405)
> "Spin and Orbital Metallic Magnetism in Rhombohedral Trilayer Graphene"

- **方法**：平均场（Hund 型 valley-anisotropic 相互作用）
- **核心**：位移场下 ABC TLG 的破缺自旋/谷金属态——动量空间凝聚驱动谷极化
- **关联**：提供了"谷劈裂何以被 Hund 机制放大"的微观图像，但**非高场 LL**

### [T5] Das & Huang — PRB 109, L060409 (2024)
> arXiv:[2308.01996](https://arxiv.org/abs/2308.01996) · DOI:[10.1103/PhysRevB.109.L060409](https://doi.org/10.1103/PhysRevB.109.L060409)
> "Unconventional Metallic Magnetism: Non-analyticity and Sign-changing Behavior of Orbital Magnetization in ABC Trilayer Graphene"

- **方法**：Quarter metal 相中的轨道磁化计算
- **核心**：Berry curvature 和 Lifshitz 转变导致轨道磁化的非解析行为
- **关联**：揭示了谷劈裂与 orbital magnetic moment 的深层绑定关系，但**零场计算**

### [T6] Koh, Alicea & Lantagne-Hurtubise — PRB 109, 035113 (2024)
> arXiv:[2306.12486](https://arxiv.org/abs/2306.12486) · DOI:[10.1103/PhysRevB.109.035113](https://doi.org/10.1103/PhysRevB.109.035113)
> "Correlated Phases in Spin-Orbit-Coupled Rhombohedral Trilayer Graphene"

- **方法**：自洽 Hartree-Fock
- **核心**：SOC 下的 Stoner ferromagnet + IVC 相图
- **关联**：对 RTG 中 valley symmetry breaking 的微观机制提供了很强的参考，但**SOC 主导 + 零场**

### [T7] Vituri, Xiao, Pareek, Holder & Berg — PRB 111, 075103 (2025)
> arXiv:[2408.10309](https://arxiv.org/abs/2408.10309) · DOI:[10.1103/PhysRevB.111.075103](https://doi.org/10.1103/PhysRevB.111.075103)
> "Incommensurate inter-valley coherent states in ABC graphene: collective modes and superconductivity"

- **方法**：非限制 Hartree-Fock + 含时 Hartree-Fock (TDHF)
- **核心**：IVC 晶体/螺旋态的集体模式，软模介导超导
- **关联**：揭示了 valley coherence 和关联的微观动力学，但**零场 IVC 物理**

---

## 三、时间线总览

```
2011  Barlas et al.      — HF: QH ↔ CDW 相变  [T3]
2012  Côté et al.        — HF: N=0 triplet QH  [T2]
2012  Shizuya             — Orbital Lamb shift  [T1]
        ↓  三部曲是"最接近 LL 谷分裂解释"的理论
2019  ★ Yin et al. (PRL)  — 实验：Δ_V ∝ B, Δ_V(N) 衰减
        ↓  "beyond any existed theory"
2020–2023  ← 理论真空期（无人直接跟进解释）
        ↓
2022  Huang et al.        — 零场 Hund 金属磁性  [T4]
2023  Das & Huang          — 零场轨道磁化      [T5]
2023  Koh et al.          — 零场 SOC + HF       [T6]
2024  Vituri et al.       — 零场 IVC 集体模式  [T7]
        ↓  均在零场，未触及高场 LL
2026  至今：理论空白仍存在
```

---

## 四、对 TBPM/HF 计算的启示

理论空白 = 计算切入点：

1. **单粒子 TBPM 基准**：算出纯单粒子的 LL 谱 → 定量确认"单粒子无法解释 $\Delta_V(B,N)$"的差距有多大
2. **HF 修正**：在 TB 模型上加入 onsite Hubbard $U$ + 自洽 Hartree-Fock → 尝试首次复现 $\Delta_V(B,N)$
3. **最小可行目标**：先复现 $\Delta_V(N=0)$ 的 $B$ 标度，再扩展至 $N=1,2$

---

*笔记创建日期：2026-07-21 | arXiv 检索 + Scholar 检索*
