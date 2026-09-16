<!--
 * @Author       : AI 精读 (五块演绎结构重写)
 * @Date         : 2026-08-06（初读）→ 2026-08-11（Phase S 补充）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T02_li2010_prb.md
 * @Description  : T2: Li/Morpurgo/Büttiker/Martin 2010 — 单谷体-边对应边际性（理论 — 拓扑分类严格性检验；2026-09-08 按 5 块演绎结构重写：模型白箱/推导链/结论清单/假设-结论依赖图/接口）
-->

# Paper Review: Li, Morpurgo, Büttiker & Martin (2010) — 单谷哈密顿量体-边对应的边际性

| 字段 | 内容 |
|------|------|
| **编号** | T2 |
| **标题** | Marginality of bulk-edge correspondence for single-valley Hamiltonians |
| **作者** | Jian Li, Alberto F. Morpurgo, Markus Büttiker, Ivar Martin |
| **期刊** | Physical Review B 82, 245404 (2010) |
| **DOI** | 10.1103/PhysRevB.82.245404 |
| **类型** | 理论 — 拓扑分类的严格性检验（连续模型解析解 + 紧束缚数值互验，无实验数据） |
| **课题组** | Li / Morpurgo / Büttiker（日内瓦大学）；Martin（Los Alamos 国家实验室） |
| **PDF** | ✅ `reference/pdfs/Li 等 - 2010 - Marginality of bulk-edge correspondence for single-valley Hamiltonians.pdf`（正文 7 页 + Appendix 边界条件推导） |
| **精读日期** | 2026-08-06（初读）→ 2026-08-11（Phase S）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」五块记（`note/shared/method/theory_paper_reading.md` §3）：**① 模型白箱 → ② 推导链 → ③ 结论清单（分层）→ ④ 假设-结论依赖图 → ⑤ 接口**。理论论文是"白箱演绎"（作者自写模型 + 解的性质），无黑箱/反推/可辨识实验。
> **共享知识引用**：Berry 相位/谷 Chern 数 → `note/shared/physics/` `[PHY-BERRY]`；通道计数 → `[PHY-LB]`。

---

## TL;DR

**本文想解决的理论问题**：带隙双层石墨烯（BLG）作为多谷原型系统，其**单个谷**的拓扑性质（非零"谷 Chern 数" $N_\nu=\pm1$）能否通过"天真推广"的体-边对应预言边缘零模数目？

**主结果**：① 谷特定霍尔电导与无隙边缘模数目之间的**精确对应一般不成立**——即使完全无谷间耦合，BLG-真空界面的零模数目仍**依赖边界条件**（四种 zigzag 终止分别给出每谷每自旋 1 / 1 / 2 / 0 条子能隙模）📜Q；② 非普适性源于单谷内**不存在良定义的拓扑不变量**（$N_\nu$ 是"边际"量，映射 $ĝ(k)$ 绕上半球两圈但不覆盖全球面）📜Q；③ 但 BLG-BLG 畴壁两侧之差 $N_\nu^l-N_\nu^r$ **是**良定义拓扑不变量（$|N_\nu^l-N_\nu^r|=2$，畴壁 2 条无隙态），这解释了 BLG-真空 vs BLG-BLG 界面的区别 📜Q。

**结论/意义**：单谷是"**边际拓扑绝缘体**"（marginal topological insulators）——其拓扑性质不能由一个不变量刻画，而须**逐个界面**分析是否存在决定边缘模数目的不变量。这是后续畴壁拓扑分类（T6 Zhang 2013 等）"$\Delta C_v$ 而非单侧 $C_v$"判据的严格基础。⚠️ 全文为理论论证，作者用词 find / show / conclude（数学构造），非实验事实。

---

## 1. 模型白箱（理想系统 + 假设清单）

### 1.1 哈密顿量（无量纲、单谷、自旋简并）

在基 $\Psi=(\psi_{B1},\psi_{A2},\psi_{B2},\psi_{A1})^T$ 下（$A(B)_{1(2)}$ 为下层/上层两子格，ref 19 符号），**无量纲** 4×4 矩阵 📜Q（Eq. 3）：

$$
H_\nu=\begin{pmatrix} H_1 & K_\nu\\ K_\nu & H_0\end{pmatrix},\quad
H_1=\sigma_x+\Delta\sigma_z,\quad H_0=-\Delta\sigma_z,\quad K_\nu=K_\nu^\dagger=\nu k_x\sigma_x+k_y\sigma_y .
$$

其中 $k=(k_x,k_y)$ 为**无量纲**波矢，谷指标 $\nu=\pm1$，$2|\Delta|$（$|\Delta|\ll1$）定义体能隙。**无量纲化**：能量以 $t_\perp$ 为单位、波矢以 $1/l_0\equiv 2t_\perp/(3ta)$ 为单位（$t_\perp$ 层间跃迁、$a$ 层内最近邻距离、$t$ 层内跃迁）📜Q（脚注 19）。激发谱 $E_{h,l}\approx\pm\sqrt{\Delta^2+(k^2+\varepsilon_{h,l})^2}$，$\varepsilon_h=1$、$\varepsilon_l=0$——高低能带分裂量级 1，低能带直接带隙 $2|\Delta|$ 📜Q。

**约化 2 分量模型**（$|E|,|\Delta|\ll1$，保留至 $E,\Delta$ 线性阶、略 $O(\Delta k^2),O(Ek^2)$）📜Q（Eq. 6）：

$$
H_\nu^{(2\times2)}=-g_\nu(k)\cdot\sigma,\qquad g_\nu(k)=\big(k_x^2-k_y^2,\ 2\nu k_x k_y,\ \Delta\big).
$$

> **符号防混**：本文 $g_\nu$ 的 $\nu$ 约定是 $g_\nu=(k_x^2-k_y^2,\ 2\nu k_xk_y,\ \Delta)$ 且 $N_\nu=\nu\,\text{sign}(\Delta)$；**与 T6 Zhang 2013 的约定相反**（后者 $g_\nu=(-(q_x^2-q_y^2)/\gamma,\ 2\nu q_x q_y/\gamma,\ \Delta)$ 且 $N_\nu=-\nu\,\text{sgn}(\Delta)$）。跨论文引用必须带各自约定，不能混用。

### 1.2 参数分册（区分"作者设定" vs "推导所得"）

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | $\nu$（谷）、$\Delta$（无量纲能隙，正比于层间电场）、$E$（能量，扫谱） |
| **导出量（由旋钮+常数算出）** | 谱 $E_{h,l}$、约化 $g_\nu(k)$、$N_\nu$、衰减指数 $\lambda_\pm$ |
| **模型内部量（解的性质）** | 子能隙边缘模数目、色散 $E(k_x)$、Berry 曲率 $B_k$ |
| **固定常数** | $t_\perp$、$t$、$a$（无量纲化用，正文**未给数值**——全文无 eV 数值） |
| **预言量（可检验）** | 边界条件依赖的零模数目、畴壁 $|N_\nu^l-N_\nu^r|=2$ |

> 无"反推量 θ̂"层。**关键**：本文完全无量纲，正文**不出现任何 eV/Å 数值**（$t_\perp$、$t$、$a$ 仅作为无量纲化标度出现，不代入数值）。

### 1.3 显式假设清单（本文结论的前提集合）

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **谷守恒（谷间解耦）**：边界不混合谷（"ideal edges that preserve the valley quantum number"） | 模型/推导 | 📜Q |
| A2 | **自旋简并**（自旋不进入矩阵，整体 ×2） | 模型 | 📜Q |
| A3 | **低能长波连续近似**（Bernal 堆叠紧束缚的低能约化，ref 18 McCann-Fal'ko） | 模型 | 📜Q |
| A4 | **$|E|,|\Delta|\ll1$ 且略去 $O(\Delta k^2),O(Ek^2)$**（约化到 2 分量） | 推导 | 📜Q |
| A5 | **单粒子**（非相互作用费米子，无多体） | 模型 | 📜Q（引言讨论"半导体电子结构分析"） |
| A6 | **边界条件由界面处概率流为零约束**（hard-wall；Appendix 推导） | 推导 | 📜Q |
| A7 | **完美界面**（正文只讨论不耦合谷的晶格边缘；无序边缘见 ref 12 另文） | 推导 | 📜Q |

---

## 2. 推导链（演绎结构：顺论文顺序）

### 2.0 总览

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 前提定理层 | I 引言（Chern 数定义） | 2-band 有效模型 $H=\sum_k\Psi_k^\dagger[-g(k)\cdot\sigma+\varepsilon_k-\mu]\Psi_k$ | 体-边对应陈述；谷 Chern 数 $N_\nu$ | 体-边对应（refs 10,11） | 全 BZ 积分 |
| 模型层 | II 4-band→2-band | Bernal BLG 紧束缚 | $H_\nu$、约化 $g_\nu(k)$、$N_\nu=\nu\,\text{sign}\Delta$ | A3、A4 | $|E|,|\Delta|\ll1$ |
| 推导层 | II.B 边界条件解零模 | $H_\nu$ + 四种边界条件 | 边缘模数目 1/1/2/0 | A6、A1 | 谷守恒 |
| 边界/几何层 | III 讨论（Laughlin + 几何） | $N_\nu$ 的几何意义 | $N_\nu$ 非不变量；畴壁差是 | Laughlin 论证、Volovik 边际性 | 全 BZ |

### 2.1 前提定理层：Chern 数与体-边对应

- 对全隙 2-band 模型 $H=\sum_k\Psi_k^\dagger[-g(k)\cdot\sigma+\varepsilon_k-\mu]\Psi_k$，霍尔电导（单位 $e^2/h$，忽略自旋）等于占据带 Chern 数 $N=(1/4\pi)\int d^2k\,\hat g\cdot(\partial_{k_x}\hat g\times\partial_{k_y}\hat g)$，$\hat g=g/|g|$（Eq. 2，积分全 BZ）📜Q。拓扑非平凡 = $N\neq0$，其物理表现 = 边缘出现 $N$ 条无隙态（体-边对应）📜Q。
- 谷分解：全 BZ 积分 = 各谷贡献 $N_\nu$ 之和，可为零而个别 $N_\nu\neq0$ 📜Q（Fig. 1：$B_k$ 仅在 $K,K'$ 附近非零，两谷等反号贡献，全 BZ 积分为零）。

### 2.2 模型层：4-band → 2-band 约化

- **输入**：Bernal 堆叠 BLG 的紧束缚描述（ref 18）；**输出**：无量纲 $H_\nu$（Eq. 3）+ 约化 $g_\nu(k)$（Eq. 6）。
- 约化步骤：Schrödinger 方程 $H_\nu\Psi=E\Psi$ 改写（Eq. 4：高能分量 $\varphi=-(E+\sigma_x+\Delta\sigma_z)K_\nu\chi$），保留 $|E|,|\Delta|\ll1$ 的线性项，略 $O(\Delta k^2),O(Ek^2)$ → Eq. 6 📜Q。此约化"essentially identical to that used by McCann and Fal'ko"（ref 18）📜Q。
- **关键自洽**：4-band 与 2-band 算出的 $N_\nu=\nu\,\text{sign}(\Delta)$ **一致**，说明单谷拓扑性质完全来自低能带 📜Q（Sec. II.A）。

### 2.3 推导层：边界条件与零模数目

- **输入**：约化模型 + 具体边界条件（由界面概率流为零约束，Appendix 导出四类合法边界条件）；**输出**：零模色散与数目。
- 四种 zigzag 终止（Fig. 2，均不混合谷）给出**不同**子能隙模数 📜Q：

| 情形 | 边界条件（$y=0$） | 子能隙模/谷/自旋 |
|---|---|---|
| (a) | $\psi_{B2}=\psi_{B1}=0$（$A_1,A_2$ 子格终止于边缘） | **1** |
| (b) | $\psi_{A1}=\psi_{A2}=0$ | **1** |
| (c) | $\psi_{B2}=\psi_{A1}=0$ | **2**（同向传播的一对无隙模，Eq. 12/13） |
| (d) | $\psi_{B1}=\psi_{A2}=0$ | **0** |

- (a) 的 1 条零模恰是"单谷体-边对应若成立"的期望值 📜Q；但 (c) 的 2 条与 (d) 的 0 条证伪了普适对应。Fig. 3 给出 (a)/(c) 解析色散与紧束缚精确对角化的"excellent agreement" 📜Q。数值例 $\Delta=0.15$（Fig. 3 caption）📜Q。
- **结论**：$N_\nu=\pm1$ **不**唯一决定零模数目——体-边对应对单谷一般不成立 📜Q。

### 2.4 讨论层：Laughlin 论证为何失效 + 几何意义

- **Laughlin gedanken 论证为何不适用单谷**：Laughlin 论证依赖**电荷守恒**（绝热插磁通 $\varphi=2\pi$ 时 $k_x\to k_x+\varphi/L$，允许 $k_x$ 集合回到自身）；而**谷量子数在插磁通过程中不守恒**——谷被深入化学势以下的能带连接，谱流无法在单谷长波哈密顿量内描述 📜Q。故非零谷霍尔电导 $\sigma_H^v=N_\nu-N_{-\nu}$ 可与零模缺失并存 📜Q。
- **几何意义（边际性）**：$B_k=(1/4\pi)\hat g\cdot(\partial_{k_x}\hat g\times\partial_{k_y}\hat g)$ 是 $R^2$（非紧）→$S^2$（紧）映射的 Jacobian；BLG 在 $k^2\gg|\Delta|$ 处 $\hat g$ 落在赤道，积分收敛到 ±1 但 $\hat g$ **不覆盖全球面**（Fig. 4(a)(b)：绕上半球两圈）→ 非紧 $R^2$ 到紧 $S^2$ 的映射拓扑平凡 → $N_\nu$ **不是**良定义拓扑不变量 📜Q。此即 Volovik 对 massive Dirac 费米子的"marginal"分类 📜Q。
- **畴壁为何是良定义的**：$\Delta(x<0)<0$、$\Delta(x>0)>0$ 的畴壁，$k\to\infty$ 时两侧 $ĝ$ 纹理在赤道无缝连接、紧化同谷动量空间 → $N_\nu^l-N_\nu^r$ 是良定义拓扑不变量，$|N_\nu^l-N_\nu^r|=2$ 对应界面 2 条无隙态（Fig. 4(c)）📜Q。可推广到有隙单层石墨烯（ref 30）与 Kane-Mele 界面（ref 5）📜Q。

---

## 3. 结论清单（分层：定理 / 估算 / 预言）

### 3.1 定理式主张（数学/拓扑论证产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 谷 Chern 数 | $N_\nu=\nu\,\text{sign}(\Delta)$（4-band 与 2-band 一致） | A1、A3 |
| 单谷体-边对应不成立 | 零模数目依赖边界条件（1/1/2/0），非由 $N_\nu$ 唯一决定 | A1、A6 |
| $N_\nu$ 非不变量 | $ĝ$ 绕半球两圈不覆盖全球 → $N_\nu$ 是"边际"量 | 几何论证 |
| 畴壁差是不变量 | $N_\nu^l-N_\nu^r$ 良定义，$|N_\nu^l-N_\nu^r|=2$ → 畴壁 2 无隙态 | A1 |

> ⚠️ 本文**未**引入量子化电导平台数字（如 $4e^2/h$），也不讨论量子化谷霍尔电导的测量值——结论止于"零模数目"这一几何/谱学层面（防跨论文迁移，尤其注意 T8 才有 $2e^2/h$）。

### 3.2 估算（经验/近似，非严格定理）

| 估算 | 值 | 证据 |
|---|---|---|
| 边缘模衰减指数 | $\lambda_\pm^2=k_x^2-(\Delta^2+E^2)\pm i\sqrt{\Delta^2-E^2}$（Eq. 9，$R(\lambda_\pm)>0$） | 📜Q[~] |
| (a) 色散近似 | $E/\Delta=(1-4k_x^2)/(1+4k_x^2)$，$k_x<0$（Eq. 11） | 📜Q[~] |
| (c) 色散近似 | $E/\Delta=-\text{sgn}(k_x)(1-2k_x^2)/(1+2k_x^2)$（Eq. 13） | 📜Q[~] |
| 数值例 | $\Delta=0.15$（Fig. 3 对比用） | 📜Q[~] |

### 3.3 预言

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| 边际性可推广到其他多谷系统 | "likely to be not only characteristic of BLG but ... more general" | 中——后续体系（单层有隙、Kane-Mele 界面）已给出 |
| 无序边缘下体-边对应恢复（单 1D 通道/自旋，长局域化长度） | 引 ref 12（companion Nat. Phys. 论文） | 中——ref 12 已论证 |

### 3.4 内部验证（自洽核对）

1. **解析↔数值互验**：连续模型零模色散与紧束缚精确对角化"excellent agreement"（Fig. 3）📜Q。
2. **4-band↔2-band 互验**：两种模型算 $N_\nu$ 一致 → 拓扑性质来自低能带 📜Q。
3. **负对照**：畴壁（$|N_\nu^l-N_\nu^r|=2$）vs 真空界面（零模数目不定）——同一"拓扑荷"体系内两种界面的对照 📜Q。

### 3.5 概念区分（分类，非溯因排除）

| 区分 | 依据 | 结论 |
|---|---|---|
| 全 BZ Chern 数 vs 单谷 $N_\nu$ | 前者是紧流形上的不变量，后者非紧→紧映射拓扑平凡 | 前者良定义，后者"边际" |
| BLG-真空 vs BLG-BLG 界面 | 前者 $N_\nu$ 不决定零模，后者 $N_\nu^l-N_\nu^r$ 良定义 | 两类界面保护程度不同 |
| 电荷 vs 谷量子数 | 电荷在插磁通中守恒，谷不守恒 | Laughlin 论证只适用电荷 |

---

## 4. 假设-结论依赖图（含金量所在）

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性 |
|---|---|---|---|
| A1 谷守恒 | 短程无序/谷间散射 | 单谷零模耦合、开输运能隙（"opening of a transport gap"） | 作者显式声明零模对短程无序不 robust，对长程谷内无序 stable 📜Q |
| A7 完美界面 | 边缘无序 | 单谷体-边对应**恢复**（1 条 1D 通道/自旋） | 反直觉：无序反而恢复普适对应（引 ref 12）📜Q |
| A4 小 $E,\Delta$ | 偏离低能 | 2-band 约化失效 | 仅影响约化，不影响 4-band 结论 |
| A3 长波近似 | 需全 BZ 描述（插磁通谱流） | 单谷内无法描述谱流 → 必须全 BZ | 这是 $N_\nu$ 边际性的**根因**，非"失效"而是边界 📜Q |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（本文预言的靶标）

- 四种 zigzag 边缘的零模数目（1/1/2/0）可用紧束缚/连续模型复现（本文已自证）；实验上理想边缘的谷守恒在真实器件难实现（短程无序谷间散射），故**真空边缘不是可靠探针**，**畴壁才是** 📜Q。

### 5.2 设计原则

- 计算畴壁态数目用**两侧谷 Chern 数之差** $\Delta N_\nu$，而非单侧 $N_\nu$——这是后续 T6 Zhang 2013 统一分类与 DW 项目超胞建模（cont.py/tb.py）的直接判据 📜Q→💭I。

### 5.3 后续文献修正（时间倒挂，💭I）

- **T6 Zhang 2013（PNAS）**：把"$\Delta N_\nu$"语言落实为 EFW/LSW 的 $\Delta N_\nu=2\nu$ 统一分类（本文 §2.4 畴壁论证的直接延续）。
- **T3 Jung 2011**：多层 ABC 石墨烯中 kink 态（$N$ 支/谷），沿用"内部界面比真空边缘可靠"的结论。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 只讨论理想（谷守恒）边缘 | 真实边缘有谷间散射（正文只引 ref 12 处理无序边缘） | 📜Q |
| 非相互作用 | 单粒子图像 | 📜Q（引言定位） |
| 全无量纲 | 无材料参数数值，量化需另代入 $t_\perp,t,a$ | 📜Q（脚注 19） |
| 未讨论量子化电导 | 结论止于零模数目，不引入 $e^2/h$ 平台 | 💭I（显式声明未出现） |

## 7. 与其他工作的关系

| 工作 | 关系 |
|------|------|
| Martin, Blanter, Morpurgo 2008（ref 14，= T1） | 直接引用——畴壁 $|N_\nu^l-N_\nu^r|=2$ 的先驱（"Δ changes sign across the domain wall"）📜Q |
| Li, Martin, Büttiker, Morpurgo 2010 Nat. Phys.（ref 12） | companion 论文——无序边缘下体-边对应恢复、单 1D 通道/自旋 📜Q |
| McCann & Fal'ko 2006（ref 18） | 引用——4-band→2-band 约化步骤来源 📜Q |
| Brey & Fertig 2006（ref 24） | 引用——单层石墨烯边界条件处理的先例 📜Q |
| Yao, Yang, Niu 2009（ref 29） | 引用——动量依赖质量项可大幅改变无隙模（边际性的例子）📜Q |
| Semenoff, Semenoff, Zhou 2008（ref 30）/ Kane-Mele（ref 5） | 引用——边际性可推广到有隙单层与 Kane-Mele 界面 📜Q |

## 8. 对后续研究的影响

- 确立"**单谷 $N_\nu$ 非不变量、畴壁差 $\Delta N_\nu$ 是**"这一拓扑分类基础——后续所有畴壁拓扑理论（T3/T6/T7）的逻辑起点 📜Q。
- 用 Laughlin 论证的"谷不守恒"机制解释了"非零谷霍尔电导但无边缘模"这一看似矛盾的结果 📜Q。

## 9. 理论模型映射（供计算对标）

| 映射 | 说明 |
|------|------|
| $H_\nu\to$ cont.py 超胞 | 无量纲 4-band BLG + 边界条件 → 可复现 1/1/2/0 零模数目 📜Q |
| 畴壁 $\Delta(x)$ 反号 → 界面模 | $|N_\nu^l-N_\nu^r|=2$ 对应 2 无隙态，供 tb.py 畴壁态计数对标 📜Q |
| $g_\nu(k)$ 几何 → Berry 曲率 | 自洽反推核对（映射是否覆盖球面）📜Q |

---

## Phase S 目的接口（引用式，随项目增删）

- **Q1（edge state 如何表征）**：本文给出**否定性**结论——BLG 真空边缘的零模数目依赖边界条件（1/1/2/0），**不是**可靠拓扑探针；可靠探针是畴壁（$\Delta N_\nu$ 良定义）📜Q。
- **Q2（理论如何解释）**：单谷体-边对应边际性 = $N_\nu$ 非紧→紧映射拓扑平凡、谷在插磁通中不守恒；畴壁差 $\Delta N_\nu$ 才是良定义拓扑量 📜Q。
- **Q3（理论↔实验对应）**：不要依赖样品边缘输运验证拓扑，应聚焦畴壁输运——为 Ju 2015、Li 2016 等选择畴壁而非边缘提供理论基础 📜Q→💭I。

> **增量价值**：为 T1 Martin 2008 提供"为何真空边缘不可靠、畴壁可靠"的严格拓扑论证；与 T6 Zhang 2013 分工——本文是"边际性 + 判据来源"，T6 是"EFW/LSW 统一分类 + 相图"。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` + `-raw` 提取到 `/tmp/T02_layout.txt`/`T02_raw.txt`，逐项 grep 核对：

| 条目 | 命中位置 | 结论 |
|------|---------|------|
| $H_1=\sigma_x+\Delta\sigma_z$、$H_0=-\Delta\sigma_z$、$K_\nu=\nu k_x\sigma_x+k_y\sigma_y$ | Eq. (3) | ✓ 📜Q |
| $g_\nu=(k_x^2-k_y^2, 2\nu k_xk_y, \Delta)$、$N_\nu=\nu\,\text{sign}(\Delta)$ | Sec. II.A | ✓ 📜Q |
| 无量纲化 $t_\perp$、$1/l_0=2t_\perp/(3ta)$ | 脚注 19 | ✓ 📜Q |
| 四种 zigzag 边界条件 + 模数 1/1/2/0 | Fig. 2 caption + Sec. II.B | ✓ 📜Q |
| $\Delta=0.15$ | Fig. 3 caption | ✓ 📜Q |
| $\sigma_H^v=N_\nu-N_{-\nu}$、$|N_\nu^l-N_\nu^r|=2$ | Sec. III | ✓ 📜Q |
| "marginal"（Volovik）、绕半球两圈不覆盖全球 | Sec. III | ✓ 📜Q |
| 无序边缘恢复体-边对应（单 1D 通道/自旋） | 脚注 13 / 结论 | ✓ 📜Q |

⚠️ **修正/降级（相对旧版）**：① 旧版"$N_\nu=-\nu\,\text{sgn}(\Delta)$"与"$g_\nu=(-(k_x^2-k_y^2)/2m,-\nu\,2k_xk_y/2m,\Delta)$"是 **T6 Zhang 2013 的约定污染**（含 $-2m$ 分母），本文实为 $N_\nu=\nu\,\text{sign}(\Delta)$、$g_\nu=(k_x^2-k_y^2,2\nu k_xk_y,\Delta)$（无量纲、无 $2m$）——已改。② 旧版四种 zigzag 边缘的"exposed 子格"标注（(a) B1-A2 等）与原文 Fig. 2 相反，已改为直接记录边界条件。③ 全文无 eV 数值（无量纲化），不引入 $t_\perp\approx0.4$ eV 等常识参数。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-06 | 初读（旧 5 节叙事版）。 |
| 2026-08-11 | Phase S 补充 Q2/Q3。 |
| 2026-09-08 | **按 5 块演绎结构整体重写**（应用户要求）。旧版归档 `archive/paper_review_T02_li2010_prb.backup_20260908.md`。修正：① $N_\nu$ 符号约定污染（T6 约定误植，改回 $\nu\,\text{sign}(\Delta)$）；② 四种 zigzag 边缘 exposed 子格标注反向（改记边界条件）；③ 明确"全文无 eV 数值、无量纲化"，删除任何 $t_\perp\approx0.4$ eV 脑补。 |
