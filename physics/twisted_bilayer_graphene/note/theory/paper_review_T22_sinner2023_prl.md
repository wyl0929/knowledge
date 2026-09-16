<!--
 * @Author       : AI 精读 (paper-reading skill)
 * @Date         : 2026-08-11（初读）→ 2026-08-20（S-REV 机制重写）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T22_sinner2023_prl.md
 * @Description  : T22: Sinner, Pantaleón & Guinea 2023 — 应变诱导扭角 moiré 晶格中的准 1D 通道（几何方法 + 连续模型；2026-09-08 按 5 块演绎结构重写）
-->

# Paper Review: Sinner, Pantaleón & Guinea (2023) — 应变诱导准 1D 通道

| 字段 | 内容 |
|------|------|
| **编号** | T22 |
| **标题** | Strain-Induced Quasi-1D Channels in Twisted Moiré Lattices |
| **作者** | Andreas Sinner, Pierre A. Pantaleón, Francisco Guinea |
| **期刊** | Physical Review Letters 131, 166402 (2023) |
| **DOI / arXiv** | 10.1103/PhysRevLett.131.166402 / 2210.07262（⚠️ arXiv 号正文未出现，标外部来源） |
| **类型** | 理论 — 应变诱导准 1D 通道（倒空间几何方法 + TBG 连续模型，无实验数据、无输运计算） |
| **课题组** | Sinner (IMDEA Nanoscience / U. Opole)、Pantaleón & Guinea (IMDEA Nanoscience / DIPC) |
| **PDF / SI** | ✅ `reference/pdfs/Sinner 等 - 2023 - Strain-Induced Quasi-1D Channels in Twisted Moiré Lattices.pdf`（正文 7 页 + Supplemental Material：可公度条件、电子结构、TBG 连续模型矢量势） |
| **精读日期** | 2026-08-11（初读）→ 2026-08-20（机制修正）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」五块记（`note/shared/method/theory_paper_reading.md` §3）：**① 模型白箱 → ② 推导链 → ③ 结论清单（分层）→ ④ 假设-结论依赖图 → ⑤ 接口**。本文是"几何白箱"——研究对象是倒空间变换矩阵 $T$（作者自写），"未知"在解的性质（临界应变、条纹方向、谱结构），故用参数分册 + 假设清单，不用实验框架词汇。

---

## TL;DR

**本文想解决的理论问题**：扭角双层 honeycomb 晶格中，应变与扭角如何相互作用，在什么临界条件下把 moiré 图案压成**近乎完美的一维条纹（准 1D 通道）**？能否给出只依赖几何量（扭角、应变、泊松比）的简单判据？

**主结果**：① 应变 + 扭角 → moiré 倒空间单胞（mBZ）**坍塌**（collapse），临界应变处 $\det T=0$（Eq. (4)，对任意晶格/任意应变类型普遍成立）📜Q；② 单轴异质应变下化为 $\epsilon_c=-(2/\sqrt\nu)\tan(\theta/2)$（Eq. (5)，与应变方向 $\phi$ 无关），线性化 $\epsilon_c\approx-\theta/\sqrt\nu$ 在 $\theta<10°$ 有效 📜Q；③ 坍塌后 1D 行为由两个通常不可公度的周期刻画，可在特定外力比（$-\epsilon_{yy}/\epsilon_{xx}=1/3$ 或 $1/12$）下退化为单一周期；为低角 TBG 与 TMD 中观测的 1D 通道复杂图案提供解释 📜Q。

**结论/意义**：纯几何方法（倒空间变换矩阵 $T$），给出临界应变与转角、泊松比的简单关系；**量测三个参数（转角/应变/泊松比）中任意两个即可定第三个**。⚠️ 全文是几何/能带论证，"channel"指几何条纹 + 关联的 1D 电子带，**无量子化电导/输运计算**，也不含拓扑不变量（Chern 等）论证（见 §3.4 显式声明）。

---

## 1. 模型白箱（几何变换矩阵 + 假设清单）

> 本文模型是**几何白箱**：作者自写的应变-转角倒空间变换，不反推自数据。§1.1 写几何定义，§1.2 参数分册，§1.3 假设清单。

### 1.1 几何定义（倒空间变换矩阵 $T$）

单层倒格矢 $b_{1,2}=2\pi a^{-1}(1,\mp 1/\sqrt3)$（晶格常数 $a$，石墨烯 $a\approx2.46$ Å）→ 旋转得两层倒格矢 $G_i^{\uparrow,\downarrow}=R[\mp\theta/2]\,b_i$ → moiré 倒格矢 $g_i=G_i^\uparrow-G_i^\downarrow$。受应变变形后：

$$g̃_i = \tilde G_i^{\uparrow}-\tilde G_i^{\downarrow}=T b_i\qquad(1)$$

$$T = (1-E^{\uparrow})\,R[-\theta/2]-(1-E^{\downarrow})\,R[+\theta/2]\qquad(2)$$

其中 $E^l=\{\epsilon^l_{ij}\}$（$i,j=x,y$，层 $l=\uparrow,\downarrow$）为对称应变张量。单轴异质应变（力沿一方向）取 $E^\downarrow=-E^\uparrow=E/2$（引 ref 30）；应变张量由无量纲应变幅 $\epsilon$（相对晶格间距）、应变方向角 $\phi$、泊松比 $\nu$ 决定 📜Q。

**变量含义表**：

| 符号 | 含义 | 值/定义 |
|---|---|---|
| $\theta$ | 扭角（$\theta=0$ 即 AA 堆叠） | 旋钮 |
| $\epsilon$ | 无量纲应变幅（相对晶格间距） | 旋钮 |
| $\phi$ | 应变方向角 | 旋钮 |
| $x=\epsilon/\epsilon_c$ | 归一化应变参数（$0<x<1$） | 导出量 |
| $E^l$ | 层 $l$ 对称应变张量 | 输入 |
| $\nu$ | 单层泊松比 | 固定常数（石墨烯 $\approx0.16$，图用 $0.165$，TMD $\approx0.19$） |
| $a$ | 单层晶格常数 | 2.46 Å（石墨烯） |
| $b_{1,2}$ | 单层倒格矢 | $2\pi a^{-1}(1,\mp1/\sqrt3)$ |
| $k_0$ | 单层 Dirac 点动量 | $2\pi/(3a)$ |
| $T$ | 应变-转角变换矩阵（Eq. 2） | 核心几何量 |
| $g̃_i$ | 变形 moiré 倒格矢 | $T b_i$ |

> **结构要点**：① 扭角折进 $R[\mp\theta/2]$ 旋转；应变折进 $(1-E^l)$ 因子；二者**相减**给出变换 $T$——"扭角与应变的相互作用"即此矩阵的非退化性。② 本文限制"晶格间距 / moiré 单元长度 $\to0$"（小角度极限）；可比长度尺度（如黑磷上石墨烯的额外图案）明确不讨论 📜Q。

### 1.2 参数分册（替代"四层变量表"：区分"设定" vs "推导所得"）

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | $\theta$（扭角）、$\epsilon$（应变幅）、$\phi$（应变方向）、$\epsilon_{xx}/\epsilon_{yy}$（两垂直力分别施加时） |
| **导出量（由旋钮+常数算出）** | 临界应变 $\epsilon_c=-(2/\sqrt\nu)\tan(\theta/2)$（Eq. 5）、实空间矢量 $L_1,L_2$（Eq. 11–12）、单胞面积 $A_0$（Eq. 13）、单胞长 $L$（Eq. 14）、单胞宽 $W$（Eq. 15）、方向矢量 $s$（Eq. 9）与 $b$（Eq. 10）、$\tilde k_0=2k_0\sin(\theta/2)$ |
| **模型内部量（解的性质）** | 变形 mBZ 形状、Dirac 点位置、TBG 能带与 DOS |
| **固定常数** | $a\approx2.46$ Å、$\nu\approx0.16$（石墨烯）/ $0.165$（图）/ $\approx0.19$（TMD）、$k_0=2\pi/(3a)$ |
| **预言量（可检验）** | 临界应变处的 1D 条纹图案、条纹方向 $b$、通道周期（单一周期条件 Eq. 16–17） |

> 无"反推量"层——理论几何模型不反推自数据。**符号防混**：$\epsilon$（应变幅）≠ $\epsilon_c$（临界应变）；$\nu$（泊松比）≠ 填充因子（本文未用 $\nu$ 表填充）。

### 1.3 显式假设清单（本文结论的前提集合）

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **小扭角 $\theta$**（领先阶）；$\epsilon_c$ 线性化合法域 $\theta<10°$ | 几何/推导 | 📜Q |
| A2 | **单轴异质应变**：$E^\downarrow=-E^\uparrow=E/2$（力沿一方向） | 模型（Eq. 5 前提） | 📜Q |
| A3 | **应变方向 $\phi=0$**（沿 x 轴，"for simplicity but without loss of generality"） | 几何段（Eq. 6–15） | 📜Q |
| A4 | **单粒子**（无相互作用）——"We will not consider here the role of interactions … Luttinger liquid" | 电子谱 | 📜Q（ref 75 注） |
| A5 | **低能连续模型**（Dirac 描述，BM 连续模型） | 电子谱 | 📜Q |
| A6 | **晶格间距/moiré 单元长度 $\to0$**（Eq. (4) "can always be satisfied" 的前提）；可比长度尺度（黑磷上石墨烯）不讨论 | 几何 | 📜Q |
| A7 | **原子重构未显式建模**——仅指出 $x\ne1$ 时 moiré 晶格被重构（ref 40） | 几何边界 | 📜Q |

> 判别性扫轴：$\theta$ 轴（$3°\to0.2°$）、$\epsilon$ 轴（$0\to\epsilon_c$，Fig. 1/2）、$x=\epsilon/\epsilon_c\in\{0,0.25,0.5,1.3,1.4,1.5\}$（Fig. 1(g)）📜Q。这些假设在 §4 逐一映射到"失效 → 结论崩塌"。

---

## 2. 推导链（顺论文演绎顺序：每步"输入→输出→所用假设→合法域"）

### 2.0 总览：论文是一条几何→谱的演绎链

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 前提几何层 | Geometry of the deformed mBZ | $b_i$→旋转→$g_i$ | 变形 $g̃_i=Tb_i$（Eq. 1–2） | 旋转矩阵、应变张量 | — |
| 推导层（collapse） | Collapse of the mBZ | $g̃_i$ 共线 | $\det T=0$（Eq. 4）→ $\epsilon_c$（Eq. 5） | A2 | $\theta<10°$（线性化） |
| 几何结果层 | Geometry of deformed lattice | $K_i$ 角点 + $\epsilon=x\epsilon_c$ | $s,b$（Eq. 9–10）、$L_1,L_2$（Eq. 11–12）、$A_0,L,W$（Eq. 13–15） | A1、A3 | 小角度 |
| 其他应变组合 | Other strain combinations | $\epsilon_{yy}/\epsilon_{xx}$ 自由 | 可公度条件（Eq. 16–17）→ 单一周期 | — | — |
| 电子谱层 | Electronic spectrum/DOS | TBG 连续模型 | Dirac 点移动、Harper 方程类比、奇异谱 | A4、A5 | 单粒子 |

### 2.1 前提几何层：倒空间变形

- **输入**：单层倒格矢 $b_{1,2}$、扭角 $\theta$、应变张量 $E^l$。
- **输出**：变形 moiré 倒格矢 $g̃_i=Tb_i$（Eq. 1），变换矩阵 $T=(1-E^\uparrow)R[-\theta/2]-(1-E^\downarrow)R[+\theta/2]$（Eq. 2）📜Q。
- **所用**：旋转矩阵 $R[\mp\theta/2]$（两层各转 $\mp\theta/2$）、对称应变张量。无新假设。

### 2.2 推导层：mBZ 坍塌判据（本文核心）

- **模型化**：应变增大 → 实空间单胞被拉长/旋转趋向特定方向；倒空间 mBZ 被逐步压扁，直到临界值**坍塌**为一条线。坍塌 ⇔ 三个 $g̃_i$ 共线 ⇔ $Tb_i=\alpha_i s$（$i=1,2$，$s$ 待定，$\alpha_i$ 实）📜Q。
- **推导**：合并得 $T(b_1-\tfrac{\alpha_1}{\alpha_2}b_2)=0$（Eq. 3）；因 $b_i$ 线性无关，当且仅当 $\det T=0$（Eq. 4）📜Q。
- **单轴异质应变特化**：$\det T=0$ 化简为 $\epsilon_c=-\tfrac{2}{\sqrt\nu}\tan\tfrac\theta2$（Eq. 5），**与 $\phi$ 无关**；线性化 $\epsilon_c\approx-\theta/\sqrt\nu$ 对 $\theta<10°$ 合理 📜Q。**Eq. (4) 是普遍判据**（不假设具体晶格、不假设具体应变类型）；Eq. (5) 依赖 A2。
- **数值对照（作者自验）**：Eq. (5) 与实验定量吻合——Ref. [42] 报 $\epsilon=15\%$（$\theta=4°$），本文给 $\epsilon_c\approx17.5\%$；Ref. [66] 引 $\epsilon=8\%$（$\theta=2°$），本文预言 $\epsilon_c\approx8\%$（TMD $\nu\approx0.19$）📜Q。

### 2.3 几何结果层：实空间矢量与条纹方向

- 令 $\epsilon=x\epsilon_c$（$0<x<1$）。六角点 $K_i$（Eq. 6）→ 变形 mBZ 六角点 $\tilde K_i=TK_i$（Eq. 7）→ 显式 $\tilde K_1,\tilde K_{2,3}$（Eq. 8，$\tilde k_0=2k_0\sin(\theta/2)$）📜Q。
- 临界应变 $x=1$ 处所有 $\tilde K_i$ 都是 $s=(1/\sqrt\nu,\,1)$（Eq. 9）的倍数——**选定方向只依赖泊松比**；实空间单胞沿垂直方向 $b=(-\sqrt\nu,\,1)$（Eq. 10）📜Q。作者明言 Eq. (4)(5)(9)(10) 是"central results … valid for any twisted honeycomb lattice system"，只依赖几何。
- 实空间矢量 $L_1,L_2$（Eq. 11–12）长度在 $x\to1$ 处按 $1/|1-x|$ 发散；面积 $A_0=|L_1\times L_2|=\tfrac{3\sqrt3 a^2}{2\theta^2|1-x^2|}\sim1/|1-x|$（Eq. 13）、长 $L=\tfrac{3a\sqrt{1+\nu x^2}}{2\theta(1-x^2)}$（Eq. 14）均发散；**宽 $W=\tfrac{3a}{2\theta\sqrt{1+\nu x^2}}$ 在临界处保持有限**（Eq. 15）📜Q。
- **边界**：$x$ 大于或小于 1 时 moiré 晶格被重构（ref 40，A7）📜Q。

### 2.4 其他应变组合：可公度条件

- 两垂直力分别施加时 $\epsilon_{yy}/\epsilon_{xx}$ 不再由 $\nu$ 固定。周期可公度条件（Eq. 16）→ $-\epsilon_{yy}/\epsilon_{xx}=(m-n)^2/[3(m+n)^2]$（Eq. 17）📜Q。最简解 $m=0,n=1$ 给 $-\epsilon_{yy}/\epsilon_{xx}=1/3$，$m=3,n=1$ 给 $1/12$（Fig. 3(c)–(d)）→ 此时体系由**单一周期**决定，临界处图案退化为 1D 条纹（AA/AB/BA 条纹晶格，Fig. 1(c)(d)）📜Q。

### 2.5 电子谱层：连续模型 + Harper 方程类比

- 应变 TBG 中 Dirac 点不再位于 mBZ 角点（Fig. 2），随应变沿复杂轨迹移动（受变形 mBZ 几何与层间耦合共同影响）📜Q。
- 临界应变处电子波函数由 Eq. (16) 两个（通常不可公度）周期竞争决定；所得方程**类 Harper 方程**（ref 69，与磁场中晶格电子类比）📜Q。不可公度组合对应延展（色散）态 + 奇异谱（不同大小的 gap）（Fig. 3）📜Q。带宽速度与独立石墨烯层的费米速度相近（ref 75 注）📜Q。

---

## 3. 结论清单（分层：定理式主张 / 估算 / 预言）

> 每条标"依赖假设 + 可检验性"；保留作者动词强度。

### 3.1 定理式主张（几何论证产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 坍塌普遍判据 | $\det T=0$（Eq. 4），"does not assume any specific lattice … nor any specific type of the strain" | A6（长度比 $\to0$） |
| 临界应变公式 | $\epsilon_c=-(2/\sqrt\nu)\tan(\theta/2)$（Eq. 5），与 $\phi$ 无关 | A2（单轴异质应变） |
| 条纹方向 | $s=(1/\sqrt\nu,1)$、$b=(-\sqrt\nu,1)$，"depend on the geometry … only" | A2 |
| 参数闭合 | "suffices to measure only two of the parameters (twist angle, strain, or Poisson ratio); the third follows" | A2 |

### 3.2 估算（经验/近似）

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| 石墨烯临界应变 | $\epsilon_c\approx4.4\%$（$\theta=1°$，$\nu=0.165$） | Eq. (5) | 📜Q[~]（Fig. 2/3 caption） |
| TMD 临界应变 | $\epsilon_c\approx8\%$（$\theta=2°$，$\nu\approx0.19$） | Eq. (5) | 📜Q[~] |
| Ref. [42] 对照 | 本文 $\epsilon_c\approx17.5\%$ vs 实验 $15\%$（$\theta=4°$） | Eq. (5) | 📜Q[~] |
| 小角度门槛 | $\theta<0.2°$ 需 $<1.0\%$ 异质应变即可坍塌 mBZ | Eq. (5) 线性化 | 📜Q[~] |
| 线性化合法域 | $\theta<10°$ | A1 | 📜Q[~] |
| 单胞宽度 | $W=3a/[2\theta\sqrt{1+\nu x^2}]$ 临界处有限 | A1 | 📜Q[~] |

### 3.3 预言（待实验/后续验证）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| 为低角 TBG/TMD 观测的 1D 通道复杂图案提供解释 | "offer explanations / our results offer simple explanations" 📜Q | 中——条纹方向 $b$、临界应变值 vs 实验 |
| 电子谱类 Harper 方程 + 1D 准晶 | "suggesting similarities with the Harper equation and with one-dimensional quasicrystals" 📜Q | 弱——谱学定性 |
| 可推广到任意六角 moiré 图案及其他几何 | "can be applied to any hexagonal twisted moiré pattern and can be easily extended to other geometries" 📜Q | 中——材料普适性 |

### 3.4 内部验证 + "没写什么"（防跨论文迁移）

1. **数值对照**：Eq. (5) 预言（$17.5\%$、$8\%$）与实验（$15\%$、$8\%$）"impressive accuracy" 📜Q。
2. **⚠️ 本文未做**：无量子化电导（$4e^2/h$ 等）——**不引入**；无拓扑不变量（Chern/$Z_2$）论证；无输运计算；无"第三种畴壁机制"这一框架（这是 review 层综合，见 §5.3）。"channel" = 几何条纹 + 1D 电子带，非输运通道。

---

## 4. 假设-结论依赖图（含金量所在）

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性 |
|---|---|---|---|
| A2 单轴异质应变 | 两垂直力分别施加 | Eq. (5) 失效（但 Eq. (4) 仍成立）；方向 $s$ 依赖 $\epsilon_{yy}/\epsilon_{xx}$（Eq. 16–17 取代） | 部分——作者给出推广（§2.4） |
| A6 长度比 $\to0$（小角度） | 晶格间距与 moiré 长度可比 | Eq. (4) "can always be satisfied" 失效；黑磷上石墨烯额外图案 | 边界外——作者显式排除 📜Q |
| A1 小角度 | $\theta\gtrsim10°$ | $\epsilon_c$ 线性化 $\epsilon_c\approx-\theta/\sqrt\nu$ 失效（精确式 Eq. (5) 仍可用） | 轻微 |
| A4 单粒子 | 相互作用（Luttinger 液体） | 电子谱（Harper 类比、奇异谱）的定量形式 | 未处理——作者显式声明 📜Q（ref 75） |
| A7 无重构 | 原子重构（$x\ne1$ 已发生，ref 40） | 几何描述在 $x\ne1$ 的定量精度 | 边界——作者指出但未建模 |

---

## 5. 接口（可检验性 / 设计原则 / 后续文献修正）

### 5.1 可检验性（预言靶标）

- 临界应变值 vs 实验：石墨烯 $\epsilon_c\approx4.4\%$（$\theta=1°$）、$17.5\%$（$\theta=4°$）、TMD $8\%$（$\theta=2°$）📜Q；
- 1D 条纹方向 $b=(-\sqrt\nu,1)$（由泊松比决定）📜Q；
- 通道周期：不可公度（一般）↔ 单一周期（$-\epsilon_{yy}/\epsilon_{xx}=1/3$ 或 $1/12$）📜Q。

### 5.2 设计原则

量测转角/应变/泊松比中任意两个即可定第三个（参数闭合）；调外力比 $\epsilon_{xx}/\epsilon_{yy}$ 把不可公度周期精调成单一周期 📜Q。

### 5.3 后续文献修正（时间倒挂，💭I）

- **T27 Georgoulea 2024（异质应变）**：指出"均匀异质应变**单独不足以**产生拓扑通道"，需原子重构——**部分修正/细化本文"应变→准 1D 条纹"图景**（本文不讨论重构对电子拓扑的影响）。
- **E8 Hsu 2020（应变工程实验）**、**E18 Ouyang 2026（应变畴壁谱学）**：应变畴壁的实验实现（⚠️ E18 晚于本文，时间倒挂）💭I。
- ⚠️ "第三种/第四种畴壁形成机制"、"无需栅压/纯机械手段"是 review 层综合框架，**原文未作此分类**（见 §3.4）💭I。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 无相互作用 | 显式排除；Luttinger 液体可能 | 📜Q（ref 75 注） |
| 无原子重构建模 | 仅指出 $x\ne1$ 被重构（ref 40） | 📜Q |
| 可比长度尺度未处理 | 黑磷上石墨烯图案 | 📜Q |
| 无输运/电导 | 通道是几何+谱概念，未算量子化电导 | 📜Q→💭I（"没写什么"） |
| 电子谱仅 $\theta=1°$ 算例 | 谱计算聚焦魔角附近，未系统扫角 | 📜Q |

## 7. 与其他工作的关系

| 工作 | 关系 |
|------|------|
| Bi, Yuan & Fu 2019 (ref 31) | 直接沿用——倒空间几何方法（"following the approach in [31]"）📜Q |
| Huder 2018 (ref 30) | 引用——单轴异质应变 $E^\downarrow=-E^\uparrow=E/2$ 简化 📜Q |
| Alden 2013 (ref 40) / Mendoza 2021 (ref 42) / Bai 2020 (ref 66) | 引用——1D 畴形成的实验观测与定量估算，本文 Eq. (5) 与之对照 📜Q |
| 单层应变矢量势文献 (refs 25, 32–37) | 引言背景——单层应变"类矢量势、不破坏时间反演"类比 📜Q |
| Harper 1955 (ref 69) | 引用——1D 极限电子方程类比 📜Q |

## 8. 对后续研究的影响

- 给出**几何闭合判据** $\det T=0$ + 临界应变 $\epsilon_c$（Eq. 4–5），为应变 moiré 的 1D 化提供可量测的普适判据 📜Q。
- 提出"应变 + 扭角 → mBZ 坍塌"这一纯几何视角，把应变效应从单层（矢量势类比）推进到扭角双层 📜Q。
- 留下"均匀应变↔原子重构"的张力——被 T27 细化（§5.3）💭I。

## 9. 理论模型映射（供计算对标）

| 映射 | 说明 |
|------|------|
| 应变张量 → $T$ → $g̃_i$ | 输入 $(\theta,\epsilon,\phi,\nu)$ 得变形 moiré 倒格矢（Eq. 1–2），TBPM 应变模块可直接复用 |
| $\epsilon_c$ → 相图 | $(\theta,\epsilon)$ 平面内 $|\epsilon|<\epsilon_c$ 为 2D moiré、$=\epsilon_c$ 为 1D 条纹；TBPM 可扫 |
| 条纹方向 $b$ → 几何 | 通道取向由泊松比决定（Eq. 10），非应变主轴 💭I（作者只说"material dependent parameters"） |
| 电子谱 → DOS/能带 | 临界处类 Harper 谱（奇异/延展），对应 TBPM 的 DOS 结构 |

## Phase S 目的接口（引用式，随项目增删）

- **Q1（edge state 如何表征）**：本文不直接给输运表征——预言的是**几何 1D 条纹**（方向 $b$、周期可公度条件）与**类 Harper 电子谱**（奇异谱 + 延展态）📜Q；无电导/拓扑不变量（见 §3.4）。
- **Q2（理论如何解释）**：应变 + 扭角 → 倒空间单胞坍塌（$\det T=0$）→ 准 1D 条纹；临界应变 $\epsilon_c=-(2/\sqrt\nu)\tan(\theta/2)$ 只依赖几何量 📜Q。是"非栅压/非堆垛"的应变路径（💭I，原文未作此分类）。
- **Q3（理论↔实验对应）**：$\epsilon_c$ ↔ 实验临界应变（$17.5\%$ vs $15\%$；$8\%$ vs $8\%$）📜Q；条纹方向 ↔ STM 图案；单一周期条件 ↔ 外力比 $\epsilon_{xx}/\epsilon_{yy}$ 📜Q。

> **增量价值**：与 T27 分工——本文给**几何判据**（$\det T=0$、$\epsilon_c$），T27 给**电子拓扑后果**（重构→拓扑界面态）。本文可直接供 TBPM 应变模块的几何输入（Eq. 1–2）。

## 反向核对 pass (2026-09-08)

`pdftotext -layout/-raw` 提取到 `/tmp/T22.txt`，逐项 grep 核对：**全部数字命中原文**——$a\approx2.46$ Å、$\nu\approx0.16/0.165/0.19$、$\epsilon_c\approx4.4\%$（Fig. 2/3 caption）、$8\%$（TMD）、$17.5\%$ vs $15\%$、$<1.0\%$（$\theta<0.2°$）、$\theta<10°$ 线性化、$k_0=2\pi/(3a)$、$1/3$ 与 $1/12$（Eq. 17）、$\theta=3°$（Fig. 1）、$\theta=1°$（Fig. 2/3）。

⚠️ 修正/降级：① arXiv 2210.07262 正文未出现（正文仅含引文 arXiv 号）→ 头部表标"外部来源"；② 旧 review "层内单轴应变（类矢量势）"表述与原文不符——"矢量势类比"是**单层**应变引言背景，本文实际机制是**单轴异质应变**（$E^\downarrow=-E^\uparrow=E/2$）；③ 旧 review "通道间耦合指数衰减/隔离度可控""通道方向由应变主轴决定"原文均无 → 删除；④ 未引入 $4e^2/h$（本文无电导）。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-11 | 初读（Phase 4 粗读）。 |
| 2026-08-20 | S-REV 机制重写：删旧版"非均匀应变梯度→赝磁场/应变梯度≳0.1%/nm/赝磁场~100T"（无源）；改为原文机制（单轴应变类矢量势+转角→倒空间单胞坍塌→1D 条纹）；补 $\epsilon_c\approx4.4\%/8\%$。 |
| 2026-09-08 | **按 5 块演绎结构整体重写**（旧版归档 `archive/paper_review_T22_sinner2023_prl.backup_20260908.md`）：补头部表格/参数分册/假设清单/推导链/结论分层/假设-结论依赖图/接口；修正"类矢量势"为引言背景、"单轴应变"细化为"单轴异质应变"；删除无源"通道耦合指数衰减""方向由应变主轴决定"；显式声明不引入电导/拓扑不变量。 |
