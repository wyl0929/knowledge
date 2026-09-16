<!--
 * @Author       : AI 精读 (paper-reading skill)
 * @Date         : 2026-08-11（初读）→ 2026-08-20（S-REV 机制重写）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T27_georgoulea2024_prb.md
 * @Description  : T27: Georgoulea, Caffrey & Power 2024 — 异质应变双层石墨烯中的 1D 拓扑通道（紧束缚 + 原子重构模型；2026-09-08 按 5 块演绎结构重写）
-->

# Paper Review: Georgoulea, Caffrey & Power (2024) — 异质应变 BLG 中的 1D 拓扑通道

| 字段 | 内容 |
|------|------|
| **编号** | T27 |
| **标题** | One-dimensional topological channels in heterostrained bilayer graphene |
| **作者** | Nina C. Georgoulea, Nuala M. Caffrey, Stephen R. Power |
| **期刊** | Physical Review B 109, 035403 (2024) |
| **DOI / arXiv** | 10.1103/PhysRevB.109.035403 / 2309.01467（⚠️ arXiv 号正文未出现，标外部来源） |
| **类型** | 理论 — 异质应变 BLG 的 1D 拓扑通道（紧束缚 + 唯象原子重构模型，无实验数据） |
| **课题组** | Georgoulea & Power (Trinity College Dublin / DCU)、Caffrey (UCD) |
| **PDF / SI** | ✅ `reference/pdfs/Georgoulea 等 - 2024 - One-dimensional topological channels in heterostrained bilayer graphene.pdf`（正文 10 页，无 SI） |
| **精读日期** | 2026-08-11（初读）→ 2026-08-20（机制修正）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」五块记。本文是**紧束缚 + 唯象重构白箱**——研究对象是异质应变 BLG 的紧束缚哈密顿量 + 界面锐度参数 $\alpha$ 的重构模型，结论是"均匀异质应变不足以产生通道、需重构"这一负结论 + 通道局域/层分布预言。

---

## TL;DR

**本文想解决的理论问题**：异质应变（heterostrain，上下层应变不同）产生的 1D moiré 图案中，AB/BA 畴之间的界面能否承载与扭角体系类似的**拓扑保护 1D 输运通道**？均匀异质应变够不够？

**主结果**：① **均匀异质应变单独不足以**在偏置 BLG 中产生 1D 拓扑通道——它给出连续变化的堆叠序、AB/BA 畴太小、界面太宽，偏压开不出清晰体隙/拓扑模 📜Q；② 需计入堆叠登记变化驱动的**面内原子重构**（展宽 Bernal 畴 + 锐化 AA/SP 界面，用单参数 $\alpha$ 的 sigmoid 模型 Eq. (6) 模拟）→ 稳健拓扑界面才出现 📜Q；③ 通道态高度局域于 **AA 或 SP 堆叠界面区**，且 AA 与 SP 模的**层/子格分布不同**（AA 模主层两子格对称、SP 模两层对称）📜Q。

**结论/意义**：异质应变是**调节（tune）**拓扑通道存在与分布的机制，与 twistronics 互补 📜Q。⚠️ 全文是紧束缚计算 + 唯象重构模型（"we show / we demonstrate / we expect"），非实验证实。

---

## 1. 模型白箱（紧束缚哈密顿量 + 重构模型）

### 1.1 哈密顿量（紧束缚 + Slater-Koster）

$$Ĥ = \sum_i \epsilon_i \hat c_i^\dagger \hat c_i - t(d)\sum_{\langle i,j\rangle}(\hat c_i^\dagger \hat c_j + \hat c_j^\dagger \hat c_i)\qquad(1)$$

层间偏压 $\Delta$ 通过格点能 $\epsilon_i=\pm\Delta/2$（符号由层决定）；跃迁 $t(d)$ 依赖距离矢量 $d=R_i-R_j$，用 Slater-Koster 参数（Eq. 2–4）：

$$-t(d)=V_{pp\pi}(d)\left[1-\left(\tfrac{d\cdot e_z}{d}\right)^2\right]+V_{pp\sigma}(d)\left(\tfrac{d\cdot e_z}{d}\right)^2,\quad V_{pp\pi}=V_{pp\pi}^0 e^{-(d-a_0)/r_0},\quad V_{pp\sigma}=V_{pp\sigma}^0 e^{-(d-d_0)/r_0}$$

参数：$V_{pp\pi}^0=-2.7$ eV、$V_{pp\sigma}^0=0.48$ eV、$a_0=1.42$ Å、$d_0=3.35$ Å、衰减长 $r_0=0.453$ Å、平面截断 $r_c=1.82$ Å（层内等效最近邻 TB，可处理 $\epsilon\sim0.25$ 应变与 dimer $\gamma_1$/skew $\gamma_3,\gamma_4$ 层间跃迁）📜Q。

**几何**：单轴异质应变（1% 沿 armchair 方向加在层 L1"底"，L2 不应变）→ 严格 1D moiré 图案（Fig. 1 用夸张的 4% 示意）；堆叠调制不影响 zigzag 方向周期性 → 单胞 = 每层一条原子链；AA 起始，周期性要求总延伸为 $y_u=3a_0$ 的整数倍 → 应变取有理值 $\epsilon=M/N$，1% 对应 $M=1,N=100$、**804 碳原子**（43-nm 宽）📜Q。

**重构模型**（Eq. 5–6）：均匀应变给线性延伸 $\Delta y_{L1}(y_{0,L1})=\epsilon y_{0,L1}$（Eq. 5）；锐化界面用 sigmoid 和 $S_i(y_{0,L1})=\Delta Y_i/[1+e^{-(y_{0,L1}-y_{0,L1}^i)/(\alpha\Delta Y_i)}]$（Eq. 6，$i\in\{AA_1,SP,AA_2\}$，中心在 AA/SP 界面）——局域提高界面应变、锐化界面、AB/BA 区更均匀 📜Q。锐度参数 $\alpha$：小 $\alpha$=锐界面；$\Delta Y_{AA}=2a_0$、$\Delta Y_{SP}=a_0$（AA 界面位移是 SP 的两倍）📜Q。结构宽度 $\sim8\alpha\Delta Y$（96% 堆叠位移发生范围）📜Q。

### 1.2 参数分册

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | 异质应变 $\epsilon$（1% 主算例）、层间偏压 $\Delta$（$-200$/-400 meV）、界面锐度 $\alpha$（重构程度）、重构层选择（L1 或 L2） |
| **导出量** | 单胞原子数（804）、$\Delta E_4$（四带能窗）、结构宽度 $\sim8\alpha\Delta Y$（SP $\sim4.5$ nm、AA $\sim9.1$ nm @$\alpha=4$） |
| **模型内部量（解的性质）** | 能带结构、态的空间/层/子格分布、界面模传播方向 |
| **固定常数** | $V_{pp\pi}^0=-2.7$ eV、$V_{pp\sigma}^0=0.48$ eV、$a_0=1.42$ Å、$d_0=3.35$ Å、$r_0=0.453$ Å、$r_c=1.82$ Å |
| **预言量（可检验）** | AA/SP 界面拓扑通道的层/子格分布、$\Delta E_4$ 随 $\Delta,\alpha$ 的演化 |

> 无"反推量"层。**符号防混**：$\Delta$（层间偏压）≠ $\Delta Y_i$（堆叠位移）≠ $\Delta E_4$（四带能窗）；$\alpha$（界面锐度参数）≠ T22 的应变参数；$\epsilon$（异质应变）≠ 能级 $\varepsilon$。

### 1.3 显式假设清单

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **紧束缚（Slater-Koster）** + 平面截断 $r_c=1.82$ Å | 模型 | 📜Q |
| A2 | **无泊松收缩**（纯单轴，垂直方向不收缩）→ 严格 1D 图案 | 模型 | 📜Q |
| A3 | **单轴异质应变**（一层应变、一层不应变；或等效重构） | 模型 | 📜Q |
| A4 | **唯象重构模型**（sigmoid，单参数 $\alpha$，各界面独立）——$\alpha$ 大到界面合并时失效 | 推导 | 📜Q |
| A5 | **仅一层弛豫**（另一层因衬底/针尖保持均匀） | 推导 | 📜Q |
| A6 | **忽略面外变形与衬底细节** | 局限 | 📜Q |
| A7 | **单一 $\alpha$**（AA 与 SP 界面局部应变相同） | 简化 | 📜Q |

> 判别性扫轴：$\epsilon$（1%、4% 示意）、$\Delta$（$-200$/-400 meV）、$\alpha$（$3$–$11$，Fig. 5）、重构层（L1/L2，Fig. 6）📜Q。

---

## 2. 推导链（顺论文顺序）

### 2.0 总览

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 模型层 | Methods (Sec. II) | Slater-Koster TB | Ĥ（Eq. 1–4）、重构模型（Eq. 5–6） | A1–A3 | 局域应变 $\lesssim0.25$ |
| 推导层 | Electronic properties (Sec. III) | 1% 均匀异质应变 | 金属性、无清晰体隙/拓扑模 | A2 | — |
| 推导层 | Interface smoothness (Sec. IV) | 重构模型 $\alpha$ | 锐界面 → 体隙 + $\Delta E_4$ | A4–A5 | $\alpha$ 不合并 |
| 推导层 | Interface states (Sec. V) | $\alpha=9$、$\Delta=-400$ meV | AA/SP 界面拓扑通道 + 层分布 | 谷 Chern 数（引 ref 20） | — |

### 2.1 模型层：紧束缚 + 重构

- **输入**：Slater-Koster 参数 + 1% 异质应变几何。
- **输出**：Ĥ（Eq. 1）、有理应变 $\epsilon=M/N$（1% 给 $M=1,N=100$、804 原子单胞）、重构 sigmoid 模型（Eq. 5–6）📜Q。
- **方法定位**：对比 Frenkel-Kontorova，单参数 $\alpha$ 可连续调界面锐度，确定"何处发生转变" 📜Q。

### 2.2 推导层：均匀异质应变（负结论）

- **输入**：1% 均匀异质应变（无偏压、无重构）。
- **输出**：能带（Fig. 3(a)）复杂子带（804 原子大单胞 → 能带折叠）；投影到 AB/AA/SP 条（Fig. 3(b)–(d)）显示多数态分布多区域，仅低能高 $k$ 态局域于特定堆叠——来自**纯约束效应**（无隙）📜Q。
- **加偏压 $\Delta=-200$ meV**（Fig. 4）：**无清晰体隙、无拓扑模**——因堆叠序连续变化、完美 AB/BA 区极小 📜Q（对比晶界/锐偏压翻转处的成对手征边界模）📜Q。均匀异质应变**不足以**产生 1D 拓扑通道（摘要/正文核心负结论）📜Q。

### 2.3 推导层：界面锐度（重构）的作用

- **输入**：重构模型 $\alpha$（锐化 AA/SP 界面、展宽 AB/BA 畴、把应变从 AB/BA 区重分布到界面）。
- **输出**：$\alpha$ 减小（界面变锐）→ 费米面穿越带数减少，直到只剩两对（AA 与 SP 界面各一对、每谷 2 条 → 总共每谷 4 条谷保护拓扑模）📜Q。四带能窗 $\Delta E_4$（仅四条带存在）随界面变锐增大，**仅 $\alpha<11$ 打开**（Fig. 5 红虚线）📜Q。更小偏压需更锐界面；考察的 $\Delta$ 在实验可及范围内 📜Q。
- **能量代价**（Fig. 6）：破 AB 堆叠代价（红）+ 应变代价（蓝）→ 总能量（黑）；锐界面（小 $\alpha$）应变代价骤增（$\alpha\lesssim8$ 急剧上升）；总能量在宽 $\alpha$ 范围较平，$\alpha\lesssim8$ 陡增 📜Q。应变（未应变）层弛豫用 $\alpha\lesssim8$（10）时总能量略低于均匀应变；$−400$ meV 偏压可给 $\sim100$ meV 量级的 $\Delta E_4$ 能窗 📜Q。

### 2.4 推导层：界面态与层/子格分布

- **输入**：$\alpha=9$（应变层弛豫）、$\Delta=-400$ meV。
- **输出**（Fig. 7）：AB 区有隙；AA 与 SP 界面各承载 K 谷**一对单向传播**边界模（对谷反向）📜Q。与偏置 BLG 中 AB/BA 间**谷 Chern 数变化**产生的谷保护拓扑模一致（ref 20）📜Q。
- **AA vs SP 差异**：AA 模主权重在界面某一层、两子格对称、另一层子格分裂分布；SP 模两层/两子格更对称 📜Q。这些趋势对界面应变水平敏感，不同界面若应变不同则可能不出现 📜Q。
- **能量窗**：AA 与 SP 模观测窗略不同（高阶带 onset 不同）📜Q。

---

## 3. 结论清单（分层）

### 3.1 定理式主张（负结论 + 分类）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 均匀异质应变不足 | "a uniform heterostrain is not sufficient to create one-dimensional topological channels" | A2 |
| 重构必要性 | 展宽 Bernal 畴 + 锐化 AA/SP 界面是稳健拓扑界面的前提 | A4 |
| 界面模起源 | 谷 Chern 数变化（引 ref 20）→ 谷保护拓扑模 | 谷守恒（继承） |
| 通道分布 | AA 与 SP 界面模的层/子格分布不同 | A5 |

### 3.2 估算

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| 算例应变 | 1%（主）、4%（示意） | A3 | 📜Q[~] |
| 单胞 | 804 原子（43 nm 宽）、$M=1,N=100$ | A2 | 📜Q[~] |
| 界面宽度 | SP $\sim4.5$ nm、AA $\sim9.1$ nm（$\alpha=4$；$\alpha=8$ 加倍）；结构宽 $\sim8\alpha\Delta Y$ | A4 | 📜Q[~] |
| 实验孤子宽 | CVD $6$–$11$ nm；双轴 $15$–$35$ nm；连续模型 $5.2/12$ nm | 引用 | 📜Q[~] |
| 临界锐度 | $\Delta E_4$ 仅 $\alpha<11$ 打开 | A4 | 📜Q[~] |
| 能窗 | $\sim100$ meV（$\Delta=-400$ meV、$\alpha=9$） | A4 | 📜Q[~] |

### 3.3 预言（待实验验证）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| 异质应变可调拓扑通道存在/分布 | "can be used as a mechanism to tune" 📜Q | 中——STM（LDOS）+ 输运 |
| AA/SP 界面模层/子格分布差异 | "exhibit differences in their layer and sublattice distribution" 📜Q | 中——层/子格分辨谱学 |
| 双轴/泊松收缩 → 2D 图案，AA 界面通道不再贡献 | "we expect" 📜Q | 弱——后续工作 |
| 绕开精确转角控制的平台 | "could potentially exhibit phenomena akin to those in tBLG" 📜Q | 弱——定性 |

### 3.4 内部验证 + "没写什么"

1. **负对照（核心）**：均匀异质应变 + 偏压 $\to$ 无体隙/拓扑模（Fig. 4）；加重构 $\to$ 出现（Fig. 5/7）——同一体系、同一偏压的锐度对照 📜Q。
2. **⚠️ 未做**：无输运计算（弹道极限之外未讨论）；无量子化电导数字；旧 review "≳0.05% 应变"无源已删（原文算例 1%/4%）。

---

## 4. 假设-结论依赖图

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性 |
|---|---|---|---|
| A2 无泊松收缩 | 泊松收缩/双轴应变 → 2D 图案 | 严格 1D 图案、通道几何 | 边界——作者预期 AA 界面通道不再贡献 |
| A4 唯象重构 | $\alpha$ 大到界面合并 | 重构模型失效 | 边界——作者显式声明 |
| A5 仅一层弛豫 | 两层同时弛豫 | 能量代价、最优 $\alpha$ | 部分（两层结果定性同，能量不同） |
| A1 TB 参数 | Slater-Koster 参数选择 | 具体带特征/所需偏压与弛豫 | 作者说不改变关键发现 |
| 谷守恒（继承） | 谷间散射 | 拓扑保护 | 基础（继承自 ref 20 图景） |

---

## 5. 接口（可检验性 / 设计原则 / 后续文献修正）

### 5.1 可检验性

AA/SP 界面局域态（STM LDOS，$20$ Å 条投影 Fig. 7）、$\Delta E_4$ 能窗、层/子格分布差异、临界 $\alpha$ 对应实验孤子宽（$6$–$11$ nm CVD、$15$–$35$ nm 双轴）📜Q。

### 5.2 设计原则

异质应变 $\epsilon$ 设 1D 图案 + 偏压 $\Delta$ 开隙 + 重构锐度 $\alpha$ 设界面——三旋钮调拓扑通道；避免精确转角控制 📜Q（作者 "circumventing some of the limitations associated with achieving precise twist angle control"）。

### 5.3 后续文献修正（时间倒挂，💭I）

- **T22 Sinner 2023（应变准 1D）**：本文给出其**电子拓扑后果**——均匀异质应变几何上可 1D 化（T22），但**拓扑通道需重构**（本文）💭I。
- **E8 Hsu 2020 / E18 Ouyang 2026（应变工程实验）**：异质应变畴壁的实验对标（⚠️ E18 晚于本文，时间倒挂）💭I。
- ⚠️ 旧 review "第四种机制"是 review 层分类（原文未作此计数）→ 移出正文。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 唯象重构（单参数 $\alpha$） | 非分子动力学/ab initio；各界面独立假设 | 📜Q |
| 忽略面外变形 | 可能降低总能/改局域化学活性 | 📜Q（引 ref 52） |
| 单一 $\alpha$ | AA 与 SP 界面局部应变相同 | 📜Q |
| 输运仅弹道极限 | 无散射/温度输运 | 💭I（旧 review 点，原文未做输运） |
| 实验异质应变难 | 需独立控上下层应变 | 📜Q（引言实验动机） |

## 7. 与其他工作的关系

| 工作 | 关系 |
|------|------|
| Zhang, MacDonald & Mele 2013 (ref 20) | 引用——偏置 BLG AB/BA 谷 Chern 数、谷保护拓扑模（界面模起源）📜Q |
| San-Jose & Prada 2013 (ref 21) / Efimkin 2018 (ref 32) / Tsim 2020 (ref 34) / De Beule 2021 (ref 35) | 引用——tBLG 拓扑界面理论谱系 📜Q |
| Huder 2018 (ref 46) / Popov 2011 (ref 47) / Alden 2013 (ref 48) | 引用——应变孤子/畴壁实验与模型 📜Q |
| Georgoulea 2022 (ref 51，同组前作) | 引用——异质应变能量判据（$\gtrsim1\%$ 应变调制堆叠有利）📜Q |
| Choi 2010 / Van der Donck 2016 (refs 49,50) | 引用——纯单轴异质应变 1D moiré 图案 📜Q |

## 8. 对后续研究的影响

- 确立"**均匀异质应变不足以**产生拓扑通道、需重构"这一负结论，校正"应变直接给拓扑通道"的简化预期 📜Q。
- 给出"应变/偏压/锐度"三旋钮调拓扑通道的设计图景，补充 twistronics 📜Q。
- 留下双轴应变/泊松收缩的 2D 图案开放问题（作者正在研究）📜Q。

## 9. 理论模型映射（供计算对标）

| 映射 | 说明 |
|------|------|
| Slater-Koster TB（Eq. 1–4） | 直接可复现的紧束缚模型（参数全给） |
| 重构模型（Eq. 6） | 层依赖应变张量 → 输入 TBPM/TB 几何 |
| $\Delta E_4$ | 四带能窗 = 拓扑通道观测窗 → 输运/LDOS 对标 |
| 界面态层/子格分布 | AA vs SP 差异 → 层/子格分辨 LDOS 对标 |

## Phase S 目的接口（引用式）

- **Q1（edge state 如何表征）**：本文给**谱学特征**——AA/SP 界面局域态、层/子格分布差异、$\Delta E_4$ 能窗（$20$ Å 条投影，Fig. 7）📜Q。
- **Q2（理论如何解释）**：均匀异质应变 → 1D 图案但界面太宽无拓扑模；重构（展宽 Bernal 畴 + 锐化界面）→ 谷 Chern 数变化 → 谷保护拓扑界面模 📜Q。
- **Q3（理论↔实验对应）**：$\alpha$ ↔ 实验孤子宽（$6$–$11$ nm CVD）；$\Delta E_4$ ↔ STM/输运能窗；应变 $\epsilon$ ↔ 器件制备 📜Q。

> **增量价值**：与 T22 互补——T22 给几何 1D 化判据，本文给电子拓扑后果（重构必要性 + 界面态分布）。紧束缚参数完整，可直接供 TBPM 对标。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` 提取到 `/tmp/T27.txt`，grep 核对：**全部数字命中原文**——$V_{pp\pi}^0=-2.7$ eV、$V_{pp\sigma}^0=0.48$ eV、$a_0=1.42$ Å、$d_0=3.35$ Å、$r_0=0.453$ Å、$r_c=1.82$ Å、1%/4% 应变、804 原子、43-nm、$M=1,N=100$、$-200$/-400 meV、SP $\sim4.5$ nm、AA $\sim9.1$ nm、$\alpha=4/8/9/11$、$6$–$11$ nm、$15$–$35$ nm、$5.2/12$ nm、$\Delta Y_{AA}=2a_0$、$\Delta Y_{SP}=a_0$、$\sim100$ meV。

⚠️ 修正/降级：① arXiv 2309.01467 正文未出现 → 标"外部来源"；② 旧 review "异质应变 ≳0.05% 即产生通道"无源（grep `0.05`=0）→ 已删，改 1%/4% 算例；③ 旧 review "第三种机制"与 T22 重复计数 → 移出正文（review 层分类）；④ 未引入量子化电导/输运数字。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-11 | 初读（Phase 4 粗读）。 |
| 2026-08-20 | S-REV 机制重写：删旧版"≳0.05% 应变即产生通道"（无源）、"有效规范场/拓扑能隙反转"（不符）；改为原文（均匀异质应变单独不足，需重构→展宽 Bernal 畴+锐化 AA/SP 界面）。 |
| 2026-09-08 | **按 5 块演绎结构整体重写**（旧版归档 `archive/paper_review_T27_georgoulea2024_prb.backup_20260908.md`）：补参数分册/假设清单/推导链（TB→均匀应变负结论→重构→界面态）/结论分层/假设-结论依赖图/接口；补完整 Slater-Koster 参数与界面宽度数字；明确"均匀异质应变不足以"为核心负结论。 |
