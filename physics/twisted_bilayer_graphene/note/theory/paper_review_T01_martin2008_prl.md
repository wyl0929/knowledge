<!--
 * @Author       : AI 精读（白箱演绎结构）
 * @Date         : 2026-08-06（初读）→ 2026-09-02（4 块辨识结构，理论版）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T01_martin2008_prl.md
 * @Description  : T1: Martin/Blanter/Morpurgo 2008 PRL — 电场畴壁 (EFW) 拓扑零模首次预言（2026-09-08 按 5 块演绎结构重写：模型白箱/推导链/结论清单/假设-结论依赖图/接口）
-->

# Paper Review: Martin, Blanter & Morpurgo (2008) — 电场畴壁（EFW）拓扑零模首次预言

| 字段 | 内容 |
|------|------|
| **编号** | T1 |
| **标题** | Topological Confinement in Bilayer Graphene |
| **作者** | Ivar Martin, Ya. M. Blanter, A. F. Morpurgo |
| **期刊** | Physical Review Letters 100, 036804 (2008)（received 28 Sep 2007; published 23 Jan 2008） |
| **DOI / arXiv** | 10.1103/PhysRevLett.100.036804（正文无 arXiv 号） |
| **类型** | 理论 — 电场畴壁（EFW）拓扑零模首次预言（纯理论，无实验数据） |
| **课题组** | Los Alamos（Martin）+ Delft Kavli（Blanter、Morpurgo） |
| **PDF / SI** | ✅ `reference/pdfs/Martin 等 - 2008 - Topological Confinement in Bilayer Graphene.pdf`（4 页，无 SI） |
| **精读日期** | 2026-08-06（初读）→ 2026-09-02（4 块辨识结构）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」的五块记（见 `note/shared/method/theory_paper_reading.md` §3）：**① 模型白箱 → ② 推导链 → ③ 结论清单（分层）→ ④ 假设-结论依赖图 → ⑤ 接口**。理论论文无黑箱、无反推、无可辨识实验（是"白箱演绎"而非"黑箱溯因"），故不用"四层变量表 + 判别表"这套实验框架词汇（旧 4 块版已废弃）。
> **共享知识引用**：通用物理已剥离到 `note/shared/physics/`，用锚点 `[PHY-BERRY]`（chiral vs helical、valley Chern）、`[PHY-LB]`（Landauer-Büttiker 通道计数）、`[PHY-GATE]`（偏压↔栅压）引用，不重复讲义。阅读疑问见 `note/shared/method/mechanism_questions.md` `[METHOD-Q]`。

---

## TL;DR

**本文想解决的理论问题**：双层石墨烯（BLG）中，能否用**静电横向约束**（符号反转的层间偏压，即"电压扭结 voltage kink"）在畴壁上束缚出 1D 手征零模？这些零模的数目与拓扑性质由什么决定？

**主结果**：① 符号反转的层间偏压 V(x)（kink）使 BLG 体能隙（幅度 |V|）在畴壁处穿过零 → 束缚 1D 手征零模 📜Q（摘要）；② **每谷每自旋 2 条零模**（"two zero modes per kink per valley per spin"），数目由绝缘 BLG 态的**拓扑真空荷**（topological vacuum charge，N₃ = ±2）固定，且**不随 kink 宽度变化**（"regardless of the width"）📜Q；③ 同谷 2 条零模同向传播、K/K′ 谷反向传播（谷锁定）→ 可作**谷过滤/谷阀**（"may have implication for valleytronics"）📜Q；④ **拓扑约束 vs 普通约束**：只有反号偏压（kink）出零模；同极性偏压（φ = tanh²，普通约束）隙下有态但**无手征零模** 📜Q（Fig. 1/3）。

**结论/意义**：提出（propose/demonstrate）一种新的 1D 手征态——源自 BLG 手征准粒子（二次色散、粒子-空穴带零隙），而非 Dirac 费米子；强调其对 valleytronics 的用途（valley filter/valve 可用现有技术实现）📜Q。⚠️ 全文为理论预言/构造，作者用词 demonstrate / find / may have implication / can enable，**非已验证事实**（后续 T2 Li 2010、T6 Zhang 2013 承接，实验 Ju 2015/Li 2016 证实，见 §5.3/§7）。

---

## 1. 模型白箱（理想系统 + 假设清单）

> 理论论文的研究对象是**白箱**——作者自写的理想模型，无需"反推内部"。本节只做两件事：**写下模型**（§1.1），**列出它成立的全部假设**（§1.3）。假设清单是本文一切结论的"前提集合"，§4 的依赖图据此展开。

### 1.1 哈密顿量（单谷、自旋简并）

写在 $(A_1, B_1, A_2, B_2)$ 基（下标 = 子格、数字 = 层）下的 $4\times4$ 显式矩阵：

$$
H=\begin{pmatrix}
-V(x)/2 & c\pi^\dagger & 0 & 0\\
c\pi & -V(x)/2 & t_\perp & 0\\
0 & t_\perp & V(x)/2 & c\pi^\dagger\\
0 & 0 & c\pi & V(x)/2
\end{pmatrix}\qquad(1)
$$

📜Q（原文 Eq. (1)；`pdftotext -layout` 复核各元素：对角 $(-V/2,-V/2,+V/2,+V/2)$、次对角 $(1,2)=(3,4)=c\pi^\dagger$、$(2,1)=(4,3)=c\pi$、层间耦合 $(2,3)=(3,2)=t_\perp$）。**只含单谷**（"we included here only one valley, assuming that V(x) is smooth enough not to cause intervalley transitions" 📜Q）。

**变量含义表**：

| 符号 | 含义 | 值/定义 |
|---|---|---|
| $V(x)$ | 层间偏压（可反号 = kink/antikink） | 旋钮 |
| $c$ | 费米速度（原文用 $c$，非 $v_F$） | 固定参数 |
| $\pi,\pi^\dagger$ | 动量升降算子 | $\pi=p_x+ip_y$，$\pi^\dagger=p_x-ip_y$ |
| $t_\perp$ | 层间耦合 | 固定参数（**全文无数值**，eV 单位数值未给） |
| $A_1,B_1,A_2,B_2$ | 下层两子格 $A_1,B_1$、上层两子格 $A_2,B_2$ | 基 |
| $a$ | 晶格常数（准经典动量以 $1/a$ 为单位） | 固定参数 |
| $\varphi(x)$ | 无量纲势（序参量） | $V(x)t_\perp a^2/(2c^2)$ |
| $\varphi_0$ | kink 幅度 | $\varphi(x)=\varphi_0\,\mathrm{sgn}\,x$ |
| $l$ | kink 宽度 | $\varphi(x)=\tanh(x/l)$ |
| $p_y$ | 沿畴壁动量 | 旋钮（扫色散） |

> **结构要点**：① 本文用 **$c$（非 $v_F$）**记费米速度，且准经典动量以逆晶格常数 $1/a$ 为单位（"momenta are measured in units of inverse lattice constant a" 📜Q）；② $V(x)$ 只出现在对角元 $\pm V/2$（上层 +、下层 −），偏压把粒子-空穴带打开、幅度 $|V|$ 的能隙 📜Q。

### 1.2 参数分册（替代旧"四层变量表"：区分"作者设定" vs "推导所得"）

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | $V(x)$（层间偏压，可反号）、$\varphi_0$（kink 幅度）、$l$（kink 宽度）、$p_y$（沿畴壁动量） |
| **导出量（由旋钮+常数算出）** | $\varphi(x)=V(x)t_\perp a^2/(2c^2)$、体能隙幅度 $\|V\|$、衰减长度 $\sim a/\sqrt{\varphi_0}$ |
| **模型内部量（解的性质）** | $H_{\rm qc}$（准经典 2-band 哈密顿量）、能谱 $E(p)$、零模色散 $\varepsilon(p_y)$、拓扑荷 $N_3/\tilde N_3$、波函数分量 $(u,v)$ |
| **固定常数** | $c$（费米速度）、$t_\perp$（层间耦合，无数值）、$a$（晶格常数）、valley 指标、自旋 |
| **预言量（可检验）** | 零模色散 $\varepsilon(p_y)$、每谷每自旋 2 条零模、谷锁定传播方向、谷阀开关行为、畴壁电荷密度 = 0 |

> 无"反推量 θ̂"层——理论论文不反推自数据。**符号防混**：$c$（费米速度）≠ 真空光速习惯用法；$\varphi_0$（kink 幅度）是**无量纲**序参量幅度，非能隙本身（能隙是 $|V|$）。

### 1.3 显式假设清单（本文结论的前提集合）

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **谷间解耦（谷守恒）**：$V(x)$ 足够平滑、不引起谷间跃迁 → 单谷处理合法 | 模型 | 📜Q |
| A2 | **自旋简并**：自旋作为整体 ×2（"per spin"），不进入矩阵 | 模型 | 📜Q |
| A3 | **$V\ll t_\perp$**（低能、恒栅压）：2-band 约化合法 | 推导 | 📜Q |
| A4 | **低能长波展开**：衰减长度 $\sim a/\sqrt{\varphi_0}$ 使解与长波展开自洽 | 推导 | 📜Q |
| A5 | **单粒子**（无多体/关联） | 模型 | 💭I（原文未讨论关联） |
| A6 | **反对称势 $\varphi(-x)=-\varphi(x)$**：使 $v(x)=u(-x)$、两波方程归并 | 推导（解析求解用） | 📜Q |
| A7 | **平滑无序仅定性**：无序只一句 "likely to influence transport in BLG with smooth potential disorder" | 模型 | 📜Q |

> 判别性扫轴：kink 宽度 $l$（窄 $l=0.5$ / 宽 $l=4$，Fig. 3）扫"零模数目是否随宽度变"；$p_y$ 扫"色散与手征方向"；$\varphi_0$ 正负（kink vs antikink）扫"色散翻转"。这些假设在 §4 逐一映射到"失效 → 结论崩塌"。

---

## 2. 推导链（演绎结构：顺论文顺序，每步"输入→输出→所用假设/定理→合法域"）

### 2.0 总览：论文是一条演绎链，不是并列主题

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 前提定理层 | 引言（OP 类比） | 已知：OP 打开能隙、非平庸拓扑构型处零模重现 | 偏压 = 可调序参量 | Andreev 态/涡旋核/聚乙炔孤子/宇宙学膜类比 | — |
| 模型层 | 哈密顿量 + 约化 | 4×4 哈密顿量 + 参数 | 2-band 约化 → 能谱开隙 → 准经典 $H_{\rm qc}$ | A1–A3 | $V\ll t_\perp$、单谷 |
| 推导层 | 波方程求解 | $H_{\rm qc}$ + 具体 kink 构型 | 零模色散 $\varepsilon(p_y)$、数目、手征方向 | A6、阶跃/平滑 kink | 反对称势 |
| 拓扑论证层 | Topological considerations | 零模计数的经验结果 | 定理式主张：数目 = 拓扑真空荷 $N_3=\pm2$ | $\pi_3(S^3)$ winding | 单谷准经典 |
| 边界层 | 畴壁电荷 + 谷电子学 | 对称性 + 谷锁定 | 零电荷；谷过滤/谷阀 | 对称性、谷守恒 A1 | 谷守恒 |

### 2.1 前提定理层（引言）：偏压 = 可调序参量

- **类比框架**：凝聚态体系低能隙常由序参量（OP）打开（超导、CDW/SDW）；OP 的非平庸拓扑构型处零能费米子态重现（Andreev 束缚态、涡旋核态、聚乙炔孤子、宇宙学膜）📜Q（引言）。BLG 中**层间偏压 V 扮演 OP 的角色，且外部可调**（"plays a role analogous to an OP, but is externally tunable"）📜Q。
- **BLG 的独特性**：这些零模源自 BLG 手征准粒子（二次色散、粒子-空穴带零隙），**而非 Dirac 费米子**——与既有零模例子（Jackiw-Rebbi 等）的根本区别 📜Q（引言）。

### 2.2 模型层：哈密顿量 → 2-band 约化 → 能谱 → 准经典

- **4×4 哈密顿量**（Eq. 1）：作用在 $(A_1,B_1,A_2,B_2)$，只含单谷（A1）；"This Hamiltonian provides a good description of BLG as proven by recent experiments [13]" 📜Q。加偏压 $V$ 后粒子-空穴带间开隙幅度 $|V|$（ref 10）📜Q。
- **2-band 约化**（Eq. 2，$V\ll t_\perp$，ref 14）：剩余分量以 $A_1,B_2$ 为主 📜Q：
$$\tilde H=\begin{pmatrix}\tfrac{V}{2}\big(1-\tfrac{c^2 p^2}{t_\perp^2}\big) & -\tfrac{c^2}{t_\perp}\pi^{\dagger 2}\\ -\tfrac{c^2}{t_\perp}\pi^2 & -\tfrac{V}{2}\big(1-\tfrac{c^2 p^2}{t_\perp^2}\big)\end{pmatrix}$$
- **能谱开隙**（Eq. 3）：$E^2=\dfrac{V^2}{4}\Big(1-\dfrac{c^2 p^2}{t_\perp^2}\Big)^2+\dfrac{c^4 p^4}{t_\perp^2}$，有限偏压下谱有隙、**在圆 $cp=V/2$ 上达到最小 $|V|$** 📜Q；$V<t_\perp$ 时第一项 $p^2$ 修正可忽略 → $E^2=V^2/4+c^4p^4/t_\perp^2$ 📜Q。
- **准经典哈密顿量**（Eq. 4，实际求解用）：
$$H_{\rm qc}=-\varphi(x)\sigma_z-(p_x^2-p_y^2)\sigma_x+2p_xp_y\sigma_y,\qquad \varphi(x)=\frac{V(x)t_\perp a^2}{2c^2}$$
动量以 $1/a$ 为单位 📜Q。常数 $\varphi$ 下谱 $E=\pm\sqrt{\varphi^2+p^4}$，类似有非对角长程序的体系；栅压 $\varphi$ 扮演序参量角色 📜Q。

### 2.3 推导层：波方程 → 反对称势简化 → 阶跃 kink 解析 → 平滑 kink 数值

- **波方程**（Eqs. 5–6）：$-\varphi u+(\partial_x+p_y)^2 v=\varepsilon u$、$\varphi v+(\partial_x-p_y)^2 u=\varepsilon v$——耦合二阶方程 📜Q。**反对称势** $\varphi(-x)=-\varphi(x)$ 下 $v(x)=u(-x)$ 使两方程归并为一个，两问题（$\Phi=\{u,u(-x)\}$ 与 $\Psi=\{v,-v(-x)\}$）可分离 📜Q。
- **阶跃 kink**（$\varphi(x)=\varphi_0\,\mathrm{sgn}\,x$）解析解：隙内态 $\propto e^{-\kappa x}$，在 $x=0$ 用波函数及其 1/2/3 阶导匹配（4 方程 4 未知、行列式 = 0）得零模色散（Eqs. 7–15）；**零能解在 $p_0=-\sqrt{\varphi_0}/2^{3/4}$**（$\varphi_0>0$）📜Q。同谷两解在 $\varepsilon\approx0$ 附近**负速度**（"This seems to imply time-reversal symmetry breaking"）；第二谷速度为正 → 对称性恢复；反 kink（$\varphi_0<0$）色散翻转 $\varepsilon(p_y)\to-\varepsilon(p_y)$ 📜Q。
- **平滑 kink**（$\varphi=\tanh(x/l)$）：Eqs. 5–6 用**有限差分法**数值解 📜Q。Fig. 2 示 $l=1$、$p_y=-1/2^{3/4}$ 的局域态，最低能量 $\varepsilon=0.1140$（远小于参考隙 $\varphi_0=1$），波函数轻微振荡衰减、满足 $v(x)=u(-x)$ 📜Q。
- **衰减长度**：拓扑约束态衰减长度 $\sim a/\sqrt{\varphi_0}$（低能），与长波展开 (4) 自洽；宽于 $a/\sqrt{\varphi_0}$ 的 kink 有定量偏离（数值解确实发现）📜Q。**只有色散细节依赖 kink 构型，零模存在本身是拓扑的**（"only the details of the zero mode dispersion ... depend on the exact profile"）📜Q。
- **关键结论（Fig. 3 caption）**：窄 kink（$l=0.5$）仅 2 支隙内态；宽 kink（$l=4$）隙边下出现更多低能态，但**任何宽度下都只有 2 条手征零模 per kink per valley per spin**（"regardless of the width"）📜Q。解析式 Eqs. (14)(15) 对窄 kink **"fits very well"** 📜Q。

### 2.4 拓扑论证层：$N_3$ 拓扑荷固定零模数目

- **$N_3$ 定义**：准经典 3D 动量-实空间 $(p,x)$ 中 Fermi 点 $(0,0,0)$ 的拓扑荷 $N_3$，由准经典 Green 函数 $G_{\rm qc}=(ip_0-H_{\rm qc})^{-1}$ 的 winding 给出（$\pi_3(S^3)$ 非平庸同伦群映射度）📜Q（Eq. 17）。
- **两个积分面选取**：(a) 无穷平面 $p_y=p_y^0$ → 等价于谱不对称函数差 $\eta(p_y^0)-\eta(-p_y^0)$；(b) 无穷平面 $x=x_0$ → $N_3$ = 左右两侧绝缘态**真空拓扑荷之差** $\tilde N_3(x_0)-\tilde N_3(-x_0)$ 📜Q。
- **结果**：$\tilde N_3(x_0)=\mathrm{sgn}\,\varphi(x_0)$，故 $N_3=\tilde N_3(x_0)-\tilde N_3(-x_0)=\pm2$，与"每谷每自旋 2 支跨零（负速度）"一致 📜Q。这就是摘要"零模支数由绝缘 BLG 态的拓扑真空荷固定"的论证。

### 2.5 边界层：畴壁零电荷 + 谷过滤/谷阀

- **畴壁电荷密度 = 0**：1D 孤子常携带有理/无理电荷；作者证明 BLG kink **反之**——利用对称性，kink 存在时密度与位置无关（正比于动量/能量截断的常数）→ 畴壁电荷密度为零（"contrary to this expectation the domain-wall charge density is zero"）📜Q。
- **谷过滤（valley filter）**：沿 kink 加电压差 → 只有一谷载流、另一谷被 "filtered out" 📜Q。
- **谷阀（valley valve）**：两个 filter 串联，同极性电流通过、反极性阻断 📜Q。
- **优势**：早期单层石墨烯谷过滤/阀方案依赖完美 zigzag 边缘（实现极难）；本文拓扑约束通道在样品内部远离边缘即可实现 → 大幅降低谷间散射 📜Q。开隙技术（栅电极开 BLG 能隙）"已被实验演示"（ref 22 Oostinga）📜Q；谷过滤的详细讨论 "will be presented elsewhere"（ref 23，未发表）📜Q。

---

## 3. 结论清单（分层：定理 / 估算 / 预言）

> 理论论文的结论必须按**性质**分层，而非平铺——"定理式主张"受假设限定、"估算"是近似、"预言"是待验证。每条标：**依赖假设** + **可检验性**。

### 3.1 定理式主张（数学/拓扑论证的产物，依赖 A1 谷守恒）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 零模数目 | 每谷每自旋 2 条零模，不随 kink 宽度变（"regardless of the width"） | A1（谷守恒） |
| 拓扑真空荷 | $N_3=\tilde N_3(x_0)-\tilde N_3(-x_0)=\pm2$，$\tilde N_3=\mathrm{sgn}\,\varphi$ | A1、单谷准经典 |
| 畴壁零电荷 | kink 存在时密度 x-无关常数 → 畴壁电荷密度 = 0 | 对称性（A6 类） |

⚠️ 本文**未**讨论量子化电导（如 $4e^2/h$）——零模的可测签名是零模色散与谷锁定方向，不引入电导平台数字（防跨论文迁移）。原文 grep "conductance / e²/h / quantized / 4e" 均无命中。

### 3.2 估算（近似/数值，非严格定理）

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| 衰减长度 | $\sim a/\sqrt{\varphi_0}$（低能，"of the order of"） | A4（长波展开） | 📜Q[~] |
| 零能解位置（阶跃 kink） | $p_0=-\sqrt{\varphi_0}/2^{3/4}$（$\varphi_0>0$） | 阶跃 kink、A6 | 📜Q[~] |
| 数值例能量 | $\varepsilon=0.1140$（$\varphi_0=1$，$l=1$，$p_y=-1/2^{3/4}$） | 平滑 kink tanh(x/1) | 📜Q[~] |
| 体能隙幅度 | $\|V\|$（最小值，圆 $cp=V/2$ 上） | — | 📜Q[~] |
| 简化谱（$V<t_\perp$） | $E^2=V^2/4+c^4p^4/t_\perp^2$ | A3 | 📜Q[~] |

> 全文数字均为无量纲（$\varepsilon$、$p_y$、$\varphi_0$、$l$ 以 $1/a$ 为单位），**无任何 eV 数值**（grep 数字+eV 无命中）。

### 3.3 预言（可检验性 → 见 §5.1）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| 谷过滤/谷阀（拓扑约束通道） | "may have implication / can enable / it should be possible to realize" 📜Q | 中——后续实验（Ju 2015/Li 2016） |
| 零模影响输运 | "These modes are likely to influence transport in BLG with smooth potential disorder" 📜Q | 弱——定性 |
| 零模源自 BLG 手征准粒子（非 Dirac） | "We demonstrate"（数学构造，非实验证实）📜Q | 中——理论构造 |

### 3.4 内部验证（自洽核对，非"排除竞争解释"）

理论论文没有数据可辨识性，但有**一致性核对**，本文四处：

1. **解析↔数值互验**：阶跃 kink 解析式（Eqs. 14–15）与窄 kink 数值解 "fits very well" 📜Q。
2. **拓扑荷↔零模计数互验**：$N_3=\pm2$ 与"每谷每自旋 2 支跨零（负速度）"一致 📜Q。
3. **对称性互验**：$v(x)=u(-x)$（Fig. 2 数值态）📜Q。
4. **衰减长度↔长波展开自洽**：$a/\sqrt{\varphi_0}$ 使解与展开 (4) 自洽 📜Q。

### 3.5 概念区分（作者论证中的"分类"，非溯因排除）

| 区分 | 依据 | 结论 |
|---|---|---|
| 拓扑约束 vs 普通约束 | 反号偏压 kink → 每谷每自旋 2 条手征零模（Fig. 3a–c）；同极性偏压 $\varphi=\tanh^2(x/4)$ → 隙下有态但**无手征零模**（Fig. 3d）📜Q | 只有符号反转偏压（拓扑约束）才出零模 |
| BLG 手征准粒子 vs Dirac 费米子 | 零模源自二次色散、粒子-空穴带零隙的 BLG 手征准粒子（"different from ... Dirac fermions"）📜Q | BLG 特有的手征零模 |
| 谷锁定（helical）vs 时间反演破缺（chiral） | 同谷 2 模负速度"似乎破缺 TR"，但第二谷速度为正 → 对称性恢复；零模有确定 $p_y S_y$ 符号（$S_y$=谷指标）📜Q | 谷锁定反向传播（helical，见 [PHY-BERRY]） |
| 零电荷 vs 分数电荷 | BLG kink 密度 x-无关 → 零电荷（"contrary to ... expectation"）📜Q | 与 1D 孤子（聚乙炔类）不同 |

> 注：这些是**概念/图景分类**（taxonomy），不是实验论文那种"数据排除竞争解释"（溯因排除）——理论论文没有后者。

---

## 4. 假设-结论依赖图（含金量所在）

> 理论论文三个月后最可能被引用的是"何时失效"，不是推导本身。本表把 §1.3 的每条假设映射到"失效方式 → 崩塌的结论 → 是否致命"。

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性（作者如何对待） |
|---|---|---|---|
| A1 谷守恒（$V(x)$ 平滑） | 原子尺度缺陷/谷间散射 | 零模谷锁定、谷过滤/谷阀 | **致命**——谷过滤/阀依赖谷锁定；作者强调通道远离边缘以降低谷间散射 📜Q |
| A3 $V\ll t_\perp$（2-band 约化） | $V\gtrsim t_\perp$ | 2-band 约化（Eq. 2）失效 | 局部——完整谱仍由 Eq. (3) 描述；约化仅用于推导层 📜Q |
| A4 低能长波展开 | 宽 kink（$>a/\sqrt{\varphi_0}$） | 定量偏离（非定性） | 非致命——零模数目（拓扑）不随宽度变 📜Q |
| A6 反对称势 | 非反对称 $\varphi(x)$ | $v(x)=u(-x)$ 对称性、解析可解性 | 非致命——平滑 kink 用数值解 📜Q |
| A5 单粒子 | 关联/强无序 | 零模图像、输运 | 未处理（无序仅一句定性 "likely to influence transport"）💭I |
| A2 自旋简并 | 自旋-轨道耦合 | 每谷每自旋计数 | 未处理（石墨烯 SOC 弱，原文未提）💭I |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（本文预言的实验靶标）

- 零模色散 $\varepsilon(p_y)$（Fig. 3）、每谷每自旋 2 条零模、谷锁定传播方向（$p_y S_y$ 符号）📜Q；
- 谷过滤/谷阀开关行为（同/反极性 → 通/断）📜Q；
- 畴壁电荷密度 = 0（与 1D 孤子对照）📜Q；
- 后续实验（Ju 2015、Li 2016）按此靶标证实偏压畴壁导电通道与谷极化输运（§5.3/§7）。

### 5.2 设计原则（"谷过滤/谷阀"二要素）

反号偏压 kink（拓扑约束）+ 远离样品边缘的平滑 1D 通道（降谷间散射）💭I（本文 "may have implication / can enable"）。

### 5.3 后续文献修正（时间倒挂，💭I）

- **Li/Morpurgo/Büttiker/Martin 2010（T2）**：直接继承/发展（后继理论，体-边对应边际性）。
- **Zhang/MacDonald/Mele 2013（T6）**：将本文零模置于 valley Chern 框架（"$\Delta C_v=2$" 是后世语言，本文未用）。
- **Ju 2015 Nature / Li 2016 Nat. Nanotech.**：实验证实偏压畴壁导电通道与谷极化输运（原文未引，💭I）。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| $V(x)$ 平滑假设 | 只处理单谷，假设 $V(x)$ 平滑到不引起谷间跃迁；尖锐势变化破坏谷守恒 | 📜Q |
| 2-band 模型适用域 | 仅 $V\ll t_\perp$ 合法；宽 kink（$>a/\sqrt{\varphi_0}$）有定量偏离 | 📜Q |
| 单粒子图像 | 无相互作用、无无序（无序仅一句 "likely to influence transport"） | 📜Q→💭I |
| 无输运量化 | 未计算电导/透射；$4e^2/h$ 为后世推演，非原文 | 💭I⚠️ |
| 谷过滤细节未展开 | "详细讨论 will be presented elsewhere"（ref 23 未发表） | 📜Q |
| 实验未验证（2008） | 开隙技术"已被演示"（ref 22），但畴壁零模当时未实验实现 | 📜Q |

---

## 7. 与其他工作的关系（跨论文对标放这里，不放正文）

| 工作 | 关系 |
|------|------|
| McCann & Fal'ko 2006 (ref 8) / McCann 2006 (ref 10) | BLG 2-band 模型 / 偏压开隙的来源 📜Q |
| Rycerz/Tworzydło/Beenakker 2007 (ref 12)、Recher 2007 (ref 21) | 早期单层石墨烯谷过滤/阀（依赖完美 zigzag 边缘）——本文批评其难实现 📜Q |
| Mañes/Guinea/Vozmediano 2007 (ref 14) | 2-band 约化依据 📜Q |
| Volovik（ref 20） | 拓扑荷 $N_3$（$\pi_3(S^3)$）方法的来源 📜Q |
| Oostinga 2007 (ref 22) | 栅电极开 BLG 能隙的已有实验 📜Q |

> ⚠️ Phase S 外部对标（**非本文引用**，时间倒挂，💭I）见 §5.3；引用关系依据 `cards.md` Q2 卡片与 `appendix_B_theory.md` §B.2。

---

## 8. 对后续研究的影响

- 开启 **EFW 拓扑态**研究线：把"拓扑约束 vs 普通约束"的本质区别立为可检验命题 📜Q。
- 提出**谷过滤/谷阀**的可实现方案（远离边缘、现有技术）📜Q——valleytronics 的早期理论基石。
- 留下后继任务：谷过滤的详细输运计算（ref 23）→ T2 承接；零模的 Chern 数语言 → T6 承接 💭I。

---

## 9. 理论模型映射（供 TBPM / Kubo 计算对标）

| 映射 | 说明 |
|------|------|
| $V(x)\to\varphi(x)=V(x)t_\perp a^2/(2c^2)$ | 层间偏压 → 无量纲序参量（栅压通过 $V$ 进入）📜Q |
| 开隙幅度 ↔ $\|V\|$ | 体绝缘能隙由偏压幅度定 📜Q |
| 零模数 ↔ $N_3=\pm2$ | 拓扑荷差 ↔ 每谷每自旋 2 条零模 📜Q |
| 谷锁定 ↔ $p_y S_y$ 符号 | K/K′ 反向传播（helical），chirality 方向 📜Q |
| 拓扑 vs 普通 → $\varphi=\mathrm{sgn}$ vs $\varphi=\tanh^2$ | 反号偏压 vs 同极性偏压 → 有无零模 📜Q |

> 与 TBPM/Kubo 对应：本文给的是单谷准经典解析/数值能谱，无器件透射。复现需在 kink 型 $V(x)$ 偏压下的 BLG 紧束缚/连续模型算 LDOS 与能谱（"零模 + 隙边态"结构）；输运量化（$4e^2/h$）需 Landauer/Fisher-Lee 透射，且必须显式处理谷间散射以检验"$V(x)$ 平滑"假设 💭I。

---

## Phase S 目的接口（引用式，随项目增删）

- **Q1（edge/domain-wall state 如何表征）**：本文无实验，纯理论预言——零模色散 $\varepsilon(p_y)$（Fig. 3）、每谷每自旋 2 条、谷锁定方向、衰减长度 $a/\sqrt{\varphi_0}$（§2/§3）。
- **Q2（理论如何解释 edge state）**：符号反转偏压 $V(x)$ → 体能隙（$|V|$）在畴壁处穿过零 → 束缚 1D 手征零模；数目由拓扑真空荷 $N_3=\pm2$ 固定（"two zero modes per kink per valley per spin" 📜Q）。⚠️ 未用 Chern/Z₂ 语言（grep 仅命中人名 Chernyak）；"$\Delta C_v=2$" 是 T6 后世语言 💭I（§2.4）。
- **Q3（理论↔实验对应）**：预言谷过滤/谷阀可开关通道；开隙技术已被 Oostinga 2007 演示；后续 Ju 2015/Li 2016 实验证实（原文未引，💭I）。（§2.5/§7）

> **增量价值**：这是 EFW 拓扑态的**原始预言**（时序上先于所有畴壁实验/后继理论），为 T1 之后的 T2–T15 提供"拓扑约束 vs 普通约束"这一判别母题；report 取用 §2.4（真空荷论证）与 §3.1（每谷每自旋 2 条零模）作为 EFW 机制源点。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` 提取正文到 `/tmp/T01.txt`（359 行），逐项 grep 核对：**全部数字/公式命中原文**——

| 数字 | grep 命中位置 | 结论 |
|------|--------------|------|
| two such modes (per spin) | 摘要后正文 | ✓ 📜Q |
| two (chiral) zero modes per kink per valley per spin regardless of the width | Fig. 3 caption | ✓ 📜Q |
| topological vacuum charge | 摘要 | ✓ 📜Q |
| $N_3=\tilde N_3(x_0)-\tilde N_3(-x_0)=\pm2$；$\tilde N_3=\mathrm{sgn}\,\varphi$ | Topological considerations 节 | ✓ 📜Q |
| gap of magnitude $\|V\|$；minimum $\|V\|$ on circle $cp=V/2$ | 引言/能谱段 | ✓ 📜Q |
| $E^2=V^2/4+c^4p^4/t_\perp^2$（$V<t_\perp$） | 能谱段 | ✓ 📜Q |
| $\varepsilon=0.1140$（$\varphi_0=1$，$l=1$，$p_y=-1/2^{3/4}$） | Numerical solution 段 | ✓ 📜Q |
| $p_0=-\sqrt{\varphi_0}/2^{3/4}$ | Step kink 段 | ✓ 📜Q |
| decay length of order $a/\sqrt{\varphi_0}$ | Step kink 段 | ✓ 📜Q |
| $l=0.5$、$l=4$ | Fig. 3 caption | ✓ 📜Q |
| $\varphi=\tanh(x/l)$、$\varphi=\tanh^2(x/4)$ | Fig. 2/3 caption | ✓ 📜Q |
| "fits very well for the narrow kink" | Fig. 3 caption 后正文 | ✓ 📜Q |
| "plays a role analogous to an OP, but is externally tunable" | 引言 | ✓ 📜Q |
| "smooth enough not to cause intervalley transitions" | 模型段 | ✓ 📜Q |
| "contrary to this expectation the domain-wall charge density is zero" | Charge of the kink 节 | ✓ 📜Q |
| "may have implication for valleytronics" / "valley filters and valves" | 摘要后正文 | ✓ 📜Q |

⚠️ 修正/降级：① 全文无 eV 数值（grep 数字+eV 无命中），$t_\perp$ 无数值——旧稿 "约 0.4 eV" 为常识脑补，已删除。② 原文未出现 "conductance / e²/h / quantized / 4e"——$4e^2/h$ 为后世推演，显式声明"不引入"。③ 原文未用 "Chern"（grep 仅命中致谢人名 Chernyak）与 "闭合-重开/相变"（grep "phase transition/closing/reopening"=0）——均已标后世语言 💭I。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-20 | **§3 实验签名 4e²/h**：加注 💭I⚠️——原文未出现该字符串（grep "4e"=0），系推演。依据: appendix_B §B.5#9 |
| 2026-08-20 | **Q2 拓扑不变量语言**：删除 "Z₂ / ΔC_v=2"——原文未用 Chern/Z₂ 语言（grep "Chern" 仅命中致谢人名 Chernyak），改以 "topological vacuum charge" + "two zero modes per kink per valley per spin" 📜Q；ΔC_v 标注为 T6 (2013) 后世语言 💭I。依据: §B.5#9 + cards.md T1 |
| 2026-09-02 | **按 4 块辨识结构新架构整体重写（理论适配）**：TL;DR 问题句式 + 四层变量表（理论版）+ 可辨识性判别表（区分竞争图景）+ [前提与限定] + 理论模型映射（§9）；§3 由"实验方法"改为"理论模型与方法" |
| 2026-09-02 | **修正 2-band 哈密顿量**：旧稿对角元 `V/2 − c²p²/t⊥` 漏 (1−c²p²/t⊥²) 结构（漏 V/2 因子、分母 t⊥ 误为 t⊥），按 Eq. 2 修正为 (V/2)(1−c²p²/t⊥²)；补 Eq. 3 全谱 E²=(V²/4)(1−c²p²/t⊥²)²+c⁴p⁴/t⊥² 与简化式 E²=V²/4+c⁴p⁴/t⊥² 的区分 |
| 2026-09-02 | **删除 t⊥ ≈ 0.4 eV**：原文无任何以 eV 为单位的能量数值（grep 数字+eV 无命中；t⊥ 全文无数字），旧稿 "约 0.4 eV" 为常识脑补 → 删除 |
| 2026-09-02 | **"V=0 闭合-重开 → 拓扑相变"标注 💭I**：原文未用该措辞（grep "phase transition/closing/reopening"=0），只说隙 |V|、偏压"类比 OP"、Ñ₃=sgn φ；保留为后世重述并显式标注 |
| 2026-09-02 | **4e²/h 通道计数修正**：旧稿 "两谷×两模×e²/h" 漏自旋、误计谷；正确为每谷 2 模×2 自旋=4 通道（谷过滤选单谷）→ 4e²/h，仍标 💭I⚠️[推导] |
| 2026-09-08 | **按 5 块演绎结构整体重写**（应用户要求；方法论 §4.0 定位：理论论文是"白箱演绎"非"黑箱溯因"）。旧 4 块版归档 `archive/paper_review_T01_martin2008_prl.backup_20260908.md`。黑箱三要素/四层变量表/判别表/[前提与限定] → 拆为"模型白箱（哈密顿量+参数分册+假设清单）"+"推导链（五层演绎）"+"结论清单（定理/估算/预言分层）"+"假设-结论依赖图"+"接口"；内部验证（§3.4）+ 概念区分（§3.5）取代判别表。全部 📜Q 事实与数字无丢失，22 项数字/公式 grep 复核全命中。 |
