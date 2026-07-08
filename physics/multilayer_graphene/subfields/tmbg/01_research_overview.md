<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-12 14:23:19
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-12 14:23:19
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/tmbg/01_research_overview.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-12
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-12
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/tmbg/01_research_overview.md
 * @Description  : TMBG 研究综述 —— 从实验发现到理论现状
-->
# 01 Research Overview / TMBG · 研究综述

Last updated: 2026-06-12

> 深入综述 TMBG（Twisted Monolayer-Bilayer Graphene）的实验发现、理论进展和开放问题。
> 阅读前建议已读父 pack 的 `01_research_overview.md` 了解三层/多层体系的全局图景。

---

## 1. TMBG 在三层体系中的独特位置

在三层转角石墨烯的所有构型中，TMBG 占据了一个特殊的生态位：

- **比 TBG 丰富，但比 TDBG 简单**：只有 3 层而非 4 层，但已经有不对称的低能自由度
- **实验上最早实现的三层转角体系**：Chen et al. (2021) 和 Polshyn et al. (2020) 几乎同时报道
- **物理上介于 TBG 和单层石墨烯之间**：平带物理（TBG 遗产）+ 可调谐 Dirac 物理（单层遗产）

这使 TMBG 成为一个"最小不对称摩尔体系"的理想模型系统。

---

## 2. 实验发现时间线

```
2020  Q1  Polshyn et al. (UCSB) — TMBG 中关联绝缘态和 Chern 绝缘体的首次报道（Nature 588, 727）
     Q4
2021  Q1  Chen et al. (MIT) — 独立验证 TMBG 关联绝缘态（Nature Phys. 17, 374）
          He et al. — 自旋-谷极化的关联态（Nature Phys. 17, 26）
     Q2  Xu et al. — 位移场调控拓扑相变（Nature Nanotech. 16, 747）
     Q3  Shin et al. — 超导迹象报道（PRL 127, 047001）
     Q4  Siriviboon et al. — 位移场-填充因子联合相图（Nature 599, 593）
2022      理论相图的多组跟进
2023–24   领域重心逐渐转移到 TDBG（更干净的拓扑调控），TMBG 研究放缓
2025–现在  仍有理论空白（平带拓扑分类、无序效应、超导机制），计算切入窗口仍在
```

---

## 3. 关键实验发现详解

### 3.1 关联绝缘态（Chen 2021, Polshyn 2020）

**观测**：在 TMBG 的平带整数填充 ν = ±1, ±2, ±3 处，纵向电阻 $R_{xx}$ 出现峰值（> 100 kΩ），同时霍尔电阻 $R_{xy}$ 出现平台或符号反转。

**与 TBG 的关键差异**：
- TBG 的关联绝缘态在 ν = ±2 处最强（每摩尔单胞 2 个电子 → 填满一条平带）
- TMBG 在 ν = ±1 就已经出现强关联绝缘态
- 原因：单层侧的 Dirac 锥打破了层间等价对称性 → 平带的谷简并被部分解除 → 单条平带可被单独填充

**物理解释**：在 TMBG 中，三条平带（per spin per valley）不是等价的。外层的单层 Dirac 锥产生了一个"内置"的不对称性，使某些平带在能量上分离——类似于在内置了一个小的"位移场"。

### 3.2 Chern 绝缘体和拓扑（Polshyn 2020, Xu 2021）

**关键实验**：
- 外加垂直磁场 B，扫填充因子 ν 和位移场 D
- 在 ν = 1, 2, 3 处观测到量子化霍尔电阻 $R_{xy} = h/(\nu e^2)$，其中 Chern 数 C = ν
- 某些填充处的量子化霍尔态在有/无位移场时表现不同 → 位移场改变了平带的 Chern 数

**理论解释**：
- TMBG 的平带在有限 D 下携带非零 Chern 数（Liu, Khalaf et al., PRR 2021）
- 不对称构型（单层 vs 双层）使 Chern 数序列更复杂：不一定是简单的 (±2, 0, ∓2) 模式
- 实验上观测到的 Chern 数序列与连续模型计算定性一致

### 3.3 超导迹象（Shin 2021）

**观测**：
- 在 ν ≈ −2 附近，$R_{xx}$ 降到零（在最低温 ~30 mK 下）
- Tc ~ 2–3 K，与 TBG 超导的 Tc 范围重叠
- 超导穹顶在关联绝缘态（ν = −2）附近

**当前状态（suspected）**：
- 只有 Shin et al. (2021) 一篇明确报道了 TMBG 的超导
- 其他实验组（Chen, Polshyn, Siriviboon）主要关注绝缘态和拓扑，未明确报道超导
- 可能的原因：TMBG 超导对转角均匀性更敏感，或超导区域在参数空间中更窄
- **这是 field pack 标注的 suspected gap（G-E02）**

### 3.4 位移场联合相图（Siriviboon 2021）

Siriviboon et al. (Nature 599, 2021) 绘制了 TMBG 在 $(D, \nu)$ 二维参数空间中的完整输运相图：

**关键发现**：
- 关联绝缘态在 D = 0 附近最强，随 |D| 增大逐渐减弱
- 在某些 (D, ν) 区域，出现"半金属"行为（$R_{xx}$ 随温度降低而降低，不像绝缘态那样升高）
- 相图高度不对称于 D 的符号——这反映了 TMBG 天然的不对称性（单层在上 vs 双层在上）

---

## 4. 理论框架：从连续模型到紧束缚

### 4.1 连续模型（Bistritzer-MacDonald 推广）

Liu, Khalaf, Lee & Vishwanath (PRR 2021) 给出了 TMBG 的最完整连续模型处理。基本方案：

1. **层 1（单层）**：标准 Dirac 哈密顿量 $H_1 = \hbar v_F \mathbf{k} \cdot \boldsymbol{\sigma}$，旋转 +θ/2
2. **层 2+3（AB 双层）**：4×4 双层哈密顿量，旋转 −θ/2
   - 包含层内最近邻跃迁 $\gamma_0 \approx 2.6$ eV
   - 层间 dimer 跃迁 $\gamma_1 \approx 0.36$ eV
   - 可选 trigonal warping $\gamma_3 \approx 0.3$ eV
3. **层间耦合（层 1↔层 2）**：BM 形式的摩尔倒格矢耦合
   - AA 堆叠处耦合能 $w_{AA} \approx 110$ meV
   - AB 堆叠处耦合能 $w_{AB} \approx 100$ meV
4. **层 2↔层 3 耦合**：AB 堆叠的固定层间耦合（无转角），用标准的 Slonczewski-Weiss-McClure (SWMcC) 参数

**推广后的魔角条件**：
- 有效耦合参数 $\tilde{\alpha} = w/(\hbar \tilde{v}_F k_\theta)$，其中 $\tilde{v}_F$ 是考虑到双层"有效 Dirac 速度"之后的等效速度
- TMBG 魔角 ≈ 1.0°–1.15°（具体取决于 $\gamma_1$, $\gamma_3$ 的取值）

### 4.2 紧束缚模型

构建 TMBG 紧束缚模型的挑战：
1. **超胞大小**：θ = 1.1° 时 a_M ≈ 13 nm，近公度超胞原子数 ~10⁴–10⁵
2. **层间耦合的截断**：层 1↔层 2 的转角耦合需要在实空间中截断（~5 Å 内才显著）
3. **双层内部耦合**：层 2↔层 3 的 AB 堆叠耦合用标准 SWMcC 参数即可

与 TBG 紧束缚相比，TMBG 多了一层，但物理上多出的复杂性主要在于：
- 不对称的层间耦合矩阵维度
- 位移场的实现（层 1 和层 2+3 之间的电势差）

### 4.3 位移场在紧束缚中的实现

这是父 pack gap G-T06 的直接体现。在紧束缚模型中，位移场 D 最简单的实现方式：
- 给层 1 的所有原子加一个 on-site 能 $+\Delta/2$
- 给层 2+3 的所有原子加一个 on-site 能 $-\Delta/2$
- 其中 $\Delta = e D d$，d 为层间距（~3.35 Å）

但这是过于简化的处理！**NEEDS_VERIFICATION**：
- AB 双层内部的电荷重分布可能导致层 2 和层 3 感受到的有效电势不同
- 弛豫效应（AA 区域层间距增大）会调制局域 D 的有效强度
- DFT 研究（G-T04 相关）可以给出更准确的有效 on-site 参数

---

## 5. TMBG 理论的开放问题

### 5.1 已较好解决的问题

| 问题 | 状态 | 关键文献 |
|---|---|---|
| TMBG 的连续模型能带结构 | ✅ 已解决 | Liu, Khalaf et al. (2021) |
| θ 和 D 对平带带宽的定性影响 | ✅ 已解决 | 同上 |
| Chern 数在有限 D 下非零的拓扑起源 | ✅ 已解决 | 同上 |

### 5.2 仍在争论的问题

| 问题 | 状态 | 说明 |
|---|---|---|
| TMBG 魔角的精确值 | `suspected 分歧` | 不同理论工作给出的魔角差 ~0.1°，弛豫效应使计算更复杂 |
| 超导配对对称性 | `speculation` | 几乎没有专门针对 TMBG 的微观配对理论 |
| ν = ±1 关联绝缘态的序参量 | `suspected` | 谷极化？自旋极化？层极化？组合？ |
| 转角无序对关联态的定量效应 | `weak` | 这是父 pack gap G-T02 在 TMBG 的具体化 |

### 5.3 几乎空白的问题（= 你的机会）

| 问题 | 为什么空白 | 你的优势 |
|---|---|---|
| TMBG 紧束缚能带 vs 连续模型的定量基准（G-M03） | 没人做过系统的大超胞 TB 收敛性测试 | TBPM 天然适合大体系 |
| TMBG 中无序对 Chern 数和平带的定量影响（G-T02） | 需要大体系无序平均，计算量大 | TBPM + MPI 并行 |
| TMBG 中位移场的微观紧束缚实现（G-T06） | 大多数人用连续模型，不碰 TB | 你有 TB 代码基础 |
| TMBG 的 TBPM DOS 基准数据（G-M02） | 社区缺乏公开基准 | 你的 TBPM 可以直接产出 |

---

## 6. TMBG 研究现状总结

```
实验状态：
  ✅ 关联绝缘态 — 多组确认
  ⚠️ 超导 — suspected，需更多验证
  ✅ 位移场拓扑调控 — 已确立
  ⚠️ 高精度 STM/STS — 数据有限

理论状态：
  ✅ 连续模型能带 — 已确立（Liu, Khalaf et al. 2021）
  ⚠️ 紧束缚基准 — 几乎空白
  ⚠️ 无序效应 — 几乎空白
  ❌ 超导微观机制 — 几乎空白

计算切入点（按优先级）：
  1. TMBG 紧束缚能带基准（验证连续模型，产出公开数据）
  2. 无序对 TMBG 平带的定量效应（独特的 TBPM 优势）
  3. 位移场的紧束缚微观建模
  4. TMBG 平带的完整拓扑分类
```

> 详细 gap 和项目卡片见 `20_gap_table.md` 和 `22_project_candidates.md`。
