<!--
 * @Author       : AI 精读（白箱演绎结构）
 * @Date         : 2026-08-06（初读）→ 2026-09-01（4 块辨识结构，理论版）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T12_tsim2020_prb.md
 * @Description  : T12: Tsim, Nam & Koshino 2020 PRB — 偏置 mTBG 的完美 1D 手征态（TZM 推翻网络图景；2026-09-08 按 5 块演绎结构重写：模型白箱/推导链/结论清单/假设-结论依赖图/接口）
-->

# Paper Review: Tsim, Nam & Koshino (2020) — 偏置 mTBG 的完美 1D 手征态（TZM）

| 字段 | 内容 |
|------|------|
| **编号** | T12 |
| **标题** | Perfect one-dimensional chiral states in biased twisted bilayer graphene |
| **作者** | Bonnie Tsim, Nguyen N. T. Nam, Mikito Koshino |
| **期刊** | Physical Review B 101, 125409 (2020)（Received 18 Jan 2020 / published 9 Mar 2020）📜Q |
| **DOI / arXiv** | 10.1103/PhysRevB.101.125409 📜Q / arXiv:2001.06257（⚠️ 正文未出现，标外部来源） |
| **类型** | 理论 — 连续模型 + 紧束缚（TZM 推翻网络图景） |
| **课题组** | Tsim（Manchester）+ Nam（AIST Sendai）+ Koshino（Osaka Univ.）📜Q |
| **PDF / SI** | ✅ `reference/pdfs/Tsim 等 - 2020 - Perfect one-dimensional chiral states in biased twisted bilayer graphene.pdf`（10 页，无 SI） |
| **精读日期** | 2026-08-06（初读）→ 2026-09-01（4 块辨识结构）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」的五块记（见 `note/shared/method/theory_paper_reading.md` §3）：**① 模型白箱 → ② 推导链 → ③ 结论清单（分层）→ ④ 假设-结论依赖图 → ⑤ 接口**。理论论文无黑箱、无反推、无可辨识实验（是"白箱演绎"而非"黑箱溯因"），故不用"四层变量表 + 判别表"这套实验框架词汇（旧 4 块版已废弃）。
> **共享知识引用**：通用物理（valley Chern / chiral vs helical、网络 miniband、Landauer-Büttiker 通道计数）已剥离到 `note/shared/physics/`，用锚点 `[PHY-BERRY] [PHY-MB] [PHY-LB]` 引用，不重复讲义。阅读疑问见 `note/shared/method/mechanism_questions.md` `[METHOD-Q]`。

---

## TL;DR

**本文想解决的问题**：小角 TBG 在强层间偏置下，AB/BA 畴壁上已知的拓扑通道究竟**形成 2D 渗流网络**（Efimkin-MacDonald 网络模型，入射模在节点分裂为多个出射模），还是**组成独立的 1D 链**？

**主结果**：① 拓扑通道**不形成渗流网络**，而是自组织为**三组独立的完美 1D 本征模**（topological zigzag mode, TZM），沿三个方向独立传播、从不杂化 📜Q（摘要）；② AA 节点散射是**置换型（确定性）**的——mode 1 恒散射到 mode 2（−120°），mode 2 恒散射到 mode 1（+120°）→ 三组独立 zigzag 模，无分束不杂化 📜Q（Sec. III）；③ 偏置产生**两个稀疏 1D 能量窗口**，被电荷中性点附近的**近扁平带簇**隔开 📜Q（Sec. II）。

**结论/意义**：这是网络模型的 **special case**——每个顶点散射矩阵唯一连接特定出入模；作者措辞 "do not actually form a percolating network, but instead … provide independent, perfect one-dimensional eigenmodes" 📜Q（摘要，理论演示非实验证明）。⚠️ 全文为理论预言/数值演示，非已验证事实（后续 T15/T29 承接修正，见 §5.3/§7）。

---

## 1. 模型白箱（理想系统 + 假设清单）

> 理论论文的研究对象是**白箱**——作者自写的理想模型，无需"反推内部"。本节只做两件事：**写下模型**（§1.1），**列出它成立的全部假设**（§1.3）。假设清单是本文一切结论的"前提集合"，§4 的依赖图据此展开。

### 1.1 连续模型与紧束缚哈密顿量

**连续模型**（Eq. 1，等价于 Bistritzer-MacDonald [1,6,39] 至一个规范变换 [42,43]）：

$$H_{\mathrm{TBG}}=\begin{pmatrix} H_1 & U^\dagger \\ U & H_2 \end{pmatrix},\qquad H_{1,2}=\begin{pmatrix} \mp\Delta/2 & -\upsilon\pi^\dagger \\ -\upsilon\pi & \mp\Delta/2 \end{pmatrix}$$

$H_{1,2}$ 为单层 Dirac 哈密顿量（含偏置 $\pm\Delta/2$，$\Delta$ = 垂直电场诱导的静电能移）📜Q；$\pi=\hbar(\xi k_x+ik_y)$，谷指标 $\xi=\pm1$ 区分 K/K′ 📜Q。层间耦合 $U=u\sum_{j=0,1,2}e^{i\Delta K_j\cdot r}\begin{pmatrix}1&e^{-i\frac{2\pi}{3}j}\\e^{i\frac{2\pi}{3}j}&1\end{pmatrix}$（Eq. 3），$u=0.103$ eV 📜Q[~]；$\Delta K_j$（Eq. 4）为两层原始 BZ 角位移，$|\Delta K_j|=4\pi\theta/(3a)$ 📜Q。**谷间耦合在小角可忽略，K/K′ 独立计算** 📜Q。

**紧束缚 + Slater-Koster**（Eqs. 6–9，Sec. III，用于晶格弛豫）：$H=-\sum_{i,j}t(R_i-R_j)|R_i\rangle\langle R_j|+\mathrm{H.c.}$，转移积分含 $V_{pp\pi}^0\approx-2.7$ eV（最近邻层内）、$V_{pp\sigma}^0\approx0.48$ eV（垂直最近邻）、$d_0\approx0.334$ nm（层间距）、$a_0=a/\sqrt3\approx0.142$ nm、衰减长度 $r_0=0.184a$（使次近邻层内耦合 $=0.1V_{pp\pi}^0$）、$d>3a$ 截断 📜Q[~]。弛豫原子位形取自先前工作（ref 50）📜Q。TB 中谷不区分 📜Q。

**变量含义表**：

| 符号 | 含义 | 值/定义 |
|---|---|---|
| $\theta$ | 扭角（扫 1°→0.2°） | 旋钮 |
| $\Delta$ | 层间偏置（±Δ/2，至 400 meV） | 旋钮 |
| $u$ | 层间耦合强度 | 0.103 eV 📜Q[~] |
| $\upsilon$ | 单层带速度（$\hbar\upsilon/a=2.1354$ eV） | 固定常数 📜Q[~] |
| $a$ | 晶格常数 | 2.46 Å 📜Q[~] |
| $\Delta K_j$ | moiré 动量偏移 | $|\Delta K_j|=4\pi\theta/(3a)$ |
| $E_F$ | 费米能截面 | 50 / 20 meV |
| $n_W$ | 1D 窗口载流子密度 | $g_vg_s\Delta K/(4\pi\hbar v)$ |

### 1.2 参数分册（替代旧"四层变量表"：区分"作者设定" vs "推导所得"）

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | $\theta$（扭角 1°→0.2°）、$\Delta$（偏置至 400 meV）、$u$（层间耦合，Fig. 5 从 0 增至真实值）、$E_F$（费米能） |
| **导出量（由旋钮+常数算出）** | $\Delta K=|\Delta K_j|=4\pi\theta/(3a)$、窗口宽度 $\sim u$、最大交叉能量 $\hbar v\Delta K/2$、$n_W=g_vg_s\Delta K/(4\pi\hbar v)$ |
| **模型内部量（解的性质）** | $S$ 矩阵（置换型）、能带结构、DoS $D(E)$、费米面（开/闭）、态数 $2n_W$ |
| **固定常数** | $a=2.46$ Å、$\hbar\upsilon/a=2.1354$ eV、$u=0.103$ eV、$V_{pp\pi}^0\approx-2.7$ eV、$V_{pp\sigma}^0\approx0.48$ eV、$d_0\approx0.334$ nm、$a_0\approx0.142$ nm、$r_0=0.184a$ |
| **预言量（可检验）** | 能带 $E(k)$（三交叉平面、近直费米线）、波函数空间分布（1D 局域、绕过 AA）、1D 通道数→电导、AB 振荡有无 |

> 无"反推量 θ̂"层——理论论文不反推自数据（$n_W$ 是"到达 1D 窗口的预言载流子密度"，预测非反推）。

### 1.3 显式假设清单（本文结论的前提集合）

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **谷间耦合可忽略**（小角）→ K/K′ 独立计算 | 模型 | 📜Q |
| A2 | **单粒子**（无相互作用） | 模型 | 💭I（原文未讨论关联） |
| A3 | **连续模型刚性层**（Sec. II）；弛豫仅在 Sec. III 由 TB 引入 | 模型 | 📜Q |
| A4 | **弱耦合极限（$u\to0$）微扰起点** | 推导 | 📜Q |
| A5 | **两带模型**：大 $\Delta$ 下低能区由 layer 1 空穴带 + layer 2 电子带主导 | 推导 | 📜Q |
| A6 | $|\Delta K_j|\ll|k|$（层间矩阵元近似） | 推导（Eq. 11） | 📜Q |
| A7 | **长程杂质不混谷**（zigzag 纳米带类比） | 模型（无序讨论） | 📜Q |

> 判别性扫轴：$\theta$（1°, 0.5°, 0.3°, 0.2°）、$\Delta$（至 400 meV）、$u$（Fig. 5 从 0 到真实值）；截面 $E_F=50/20$ meV 📜Q。这些假设在 §4 逐一映射到"失效 → 结论崩塌"。

---

## 2. 推导链（演绎结构：顺论文顺序，每步"输入→输出→所用假设/定理→合法域"）

### 2.0 总览：论文六节是一条演绎链

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 前提定理层 | 引言 | 偏置下畴壁拓扑通道（已知）+ 网络模型图景 | 问题设定：渗流网络 vs 独立 1D 链 | refs 15,17–29 | — |
| 模型层 | II. Continuum model | 连续模型哈密顿量 | 两个能量窗口 + 1D 本征模 | A1–A3 | 小角、刚性层 |
| 推导层 | III. 波函数散射判定 | 波函数空间分布（Fig. 4） | 置换型散射 → 三组独立 zigzag 模 | 波函数检验 | — |
| 推导层2 | IV. 两带模型起源 | 弱耦合极限 + 两带模型 | 窗口起源 + 开费米面 + $n_W$ | A4–A6 | $u\to0$、大 $\Delta$ |
| 边界层 | III+IV+V. 弛豫与讨论 | 弛豫 TB + 无序讨论 | 弛豫稳健 + 无 AB 振荡预言 | A7 | — |

### 2.1 前提定理层（引言）：网络模型图景 vs 独立 1D 链

- **已知物理**：偏置使 AB/BA 畴区局域开隙 [22]，每条 AB-BA 边界出现**每条自旋-谷 sector 两条拓扑模** [23–29]；AB 与 BA 区单谷 Hall 电导分别为 $+e^2/h$ 与 $-e^2/h$ [30]，差 $2e^2/h$ → 每条边界每自旋每谷两条边界模 📜Q；K 与 K′ 两条模传播方向相反 📜Q。
- **问题设定**：网络模型 [38] 中入射模一般分裂为两个或更多出射模；但本文发现偏置 TBG 的拓扑模**不形成 2D 网络**，而是"拓扑通道段的**串联**（serial connection）"组成的独立 1D 本征模——网络模型的 **special case**（每个顶点散射矩阵唯一连接特定出入模）📜Q（引言 + Fig. 1b）。

### 2.2 模型层（II. Continuum model）：两个能量窗口

- **连续模型对角化**：K/K′ 独立计算（A1），zone folding 用 moiré 倒格矢 $G_1=\Delta K_1-\Delta K_0$、$G_2=\Delta K_2-\Delta K_0$ 📜Q。
- **两个能量窗口**：偏置产生两个 **well-defined 能量窗口**，各含**稀疏分布**的完美 1D 本征模，被**电荷中性点附近的近扁平带簇**隔开 📜Q（摘要 + Sec. II）。窗口大小**不强烈依赖 $\Delta$**（θ=0.2° 增大 Δ 时仍见）📜Q。
- **三交叉平面**：K 谷能带由三个互不杂化的交叉平面组成（Fig. 2c），带速度沿 $(0,-1)$、$(\sqrt3/2,1/2)$、$(-\sqrt3/2,1/2)$ 三方向 → 近直费米线（Fig. 2d）📜Q。
- **赝朗道能级**：大偏置（$\Delta=400$ meV）下窗口上部出现平台型赝朗道能级（如 θ=0.3° 时 $50<|E|<100$ meV 的三条水平线，解释为赝规范场赝朗道能级，引 [17]）📜Q。

### 2.3 推导层（III）：置换型散射 → 三组独立 zigzag 模

- **波函数检验**（Fig. 4 + 正文）：在三角网格每个顶点（AA 区），"mode 1 is always scattered to mode 2 in the −120° direction, while mode 2 is always scattered to mode 1 in the +120° direction" → "we have three independent zigzag traveling modes" 📜Q。即 $S$ 矩阵是**置换型**（$S_{12}=S_{21}=1$ 型排列，非对角、非满矩阵），三方向模无分束、不杂化。

> ⚠️ **修正（沿袭 2026-08-20 S-REV）**：旧版写 "S 矩阵是对角的"——原文并非对角矩阵，而是**置换型**确定性散射（grep "120" ✓）。依据 `Phase_S/appendix_B_theory.md` §B.5 #13 + `cards.md` T12。

### 2.4 推导层2（IV）：两带模型解释窗口起源

- **弱耦合极限（$u\to0$）**：电子侧与空穴侧各开一隙（two gaps），随 $u$ 增至真实值成为两个窗口；1D 本征模**始终留在隙内**，阻止谱完全打开 📜Q（Fig. 5）。窗口宽度 $\sim u$（"obviously the order of u"）📜Q。
- **两带模型**：大 $\Delta$ 下低能区由 layer 1 空穴带 + layer 2 电子带主导，两反向锥以相对位移 $\Delta K_j$ 相交，交叉处 anticrossing 开隙 📜Q（Fig. 6a）。隙大小 ∝ 交叉线上 $U$ 矩阵元 $\langle k+\Delta K_j,+|U|k,-\rangle\approx iu\sin[\theta(k)-2\pi j/3]$（Eq. 11，$|k|>|\Delta K_j|$）📜Q。
- **费米面重构**：$u=0$ 时三个开费米面（120° 相隔）+ 三个闭 pocket；$u$ 增大后闭 pocket 因电子-空穴**良好 nesting** 被开隙、开费米面**保持无隙** → 解释 1D 模填充隙的起源 📜Q（Fig. 6c–e）。
- **大 $u$ 下仍解耦**（Fig. 7 + pseudospin matching）：k 空间矩阵元在六区 I–VI 边界处近零（单层本征态在 x 方向的 pseudospin $(1,1)$ 与 $(1,-1)$ 是 $U$ 的 $j=0$ 分量本征矢 → 不杂化）→ 六区近解耦，三方向 1D 模在大 $u$ 下仍独立 📜Q。
- **载流子密度 $n_W$**（Eq. 12）：两隙夹持的每面积态数 $=2n_W$，$n_W=g_vg_s\Delta K/(4\pi\hbar v)$，来自 $D(E)=g_vg_s\Delta/(2\pi\hbar^2 v^2)$（$|E|<\Delta/2$）× 最大交叉能量 $\hbar v\Delta K/2$ 📜Q。$\theta=0.3°$、$\Delta=200$ meV 时 $n_W=1.08\times10^{12}\,\mathrm{cm^{-2}}$ 📜Q[~]。

### 2.5 边界层（III+IV+V）：弛豫稳健 + 无序/AB 预言

- **晶格弛豫稳健**：TB + Slater-Koster 弛豫（AB/BA 畴扩宽）下：非弛豫 TB 与连续模型**定量一致**；弛豫后**定性特征不变**（窗口 + 完美 1D 模仍存在）；主要差别是中央赝朗道能级与 1D 模**完全杂化**、并入色散带，零能簇**更分散** 📜Q（Fig. 3）。弛豫下波函数更局域于 AB-BA 边界（Fig. 4）📜Q。
- **zigzag 纳米带类比**：偏置 TBG 的完美 1D 模是 zigzag 石墨烯纳米带"完美导电通道"的 2D 版本（每谷 $n$ 右行 + $n{+}1$ 左行模，另一谷 $n{+}1$ 右行 + $n$ 左行模；过量行模即使无序也是完美导电通道，只要杂质长程且不混谷）📜Q（ref 56）。
- **无序与 AB 预言**（Sec. V）：见 §3.3。

---

## 3. 结论清单（分层：定理 / 估算 / 预言）

> 理论论文的结论必须按**性质**分层，而非平铺。每条标：**依赖假设** + **可检验性**。

### 3.1 定理式主张（计算/论证的产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| TZM 不渗流 | 拓扑通道不形成渗流网络，而是三组独立完美 1D 本征模 | A1–A3 |
| 置换型散射 | AA 节点 mode 1↔mode 2（∓120°），无分束不杂化 | 波函数检验 |
| 方向间不杂化 | k 空间六区近解耦（pseudospin matching）→ 三方向模独立（大 $u$ 下仍成立） | A6 |
| 两个能量窗口 | 偏置产生两个稀疏 1D 窗口，被近扁平带簇隔开 | A3 |
| 窗口起源 | 两带模型（相交电子/空穴带）+ 开费米面解释 | A4–A5 |

### 3.2 估算（近似/算例，非严格定理）

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| $n_W$（θ=0.3°, Δ=200 meV） | $1.08\times10^{12}\,\mathrm{cm^{-2}}$ | Eq. (12) | 📜Q[~] |
| 窗口宽度 | $\sim u$（"order of u"） | A4 | 📜Q[~] |
| 赝朗道能级区间 | $50<|E|<100$ meV（θ=0.3°） | — | 📜Q[~] |
| 完美 1D 模条件 | 窗口由单层空穴带+另一层电子带主导 → $\Delta/2\gtrsim u$，即 $\Delta\gtrsim200$ meV | A5 | 📜Q[~] |

### 3.3 预言（可检验性 → 见 §5.1）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| 无 AB 振荡（TZM 完整形成时） | "we do not have the Aharonov-Bohm oscillation ... because the 1D eigenmodes do not enclose triangular domains" 📜Q | 中——磁输运实验 |
| 磁振荡出现在 TZM 未完整形成时 | "We expect that magnetic oscillations take place when the perfect 1D eigenmodes are not well formed" 📜Q | 中——对 AB 实验的预测性解释 |
| 弹道输运主导 | "the electronic transport must be dominated by the ballistic transport" 📜Q | 中 |
| 无序散射主要来自短程（几纳米） | "short-range disorder ... about a few nanometers" 📜Q | 弱——详细研究留待未来 |

### 3.4 内部验证（自洽核对，非"排除竞争解释"）

理论论文没有数据可辨识性，但有**一致性核对**，本文四处：

1. **连续↔TB 互验**：非弛豫 TB 能带与连续模型**定量一致** 📜Q（Fig. 3）。
2. **连续↔两带模型互验**：两带模型解析复现窗口起源（开隙位置、1D 模填充隙）📜Q（Fig. 5, 6）。
3. **k 空间解耦自检**：Fig. 7 矩阵元图 ↔ Fig. 6(e) 开费米面 ↔ Fig. 4 波函数层分布一致 📜Q。
4. **弛豫稳健自检**：弛豫前后定性特征不变（窗口 + TZM 存在）📜Q（Fig. 3, 4）。

### 3.5 概念区分（作者论证中的"分类"，非溯因排除）

| 区分 | 依据 | 结论 |
|---|---|---|
| 渗流网络 vs 独立 1D 链 | 网络模型入射模一般分裂多出射 vs 本文置换型散射（"special case of the network model"）📜Q | 偏置 TBG = TZM（special case） |
| 置换型 vs 对角 S 矩阵 | 原文 mode 1↔mode 2（∓120°），非对角 | 置换型（旧版"对角"已修正） |
| TZM vs zigzag 纳米带 | zigzag 纳米带"完美导电通道"的 2D 版本 📜Q（ref 56） | 2D 类比 |

> 注：这些是**概念/图景分类**（taxonomy），不是实验论文那种"数据排除竞争解释"（溯因排除）——理论论文没有后者。

---

## 4. 假设-结论依赖图（含金量所在）

> 理论论文三个月后最可能被引用的是"何时失效"，不是推导本身。本表把 §1.3 的每条假设映射到"失效方式 → 崩塌的结论 → 是否致命"。

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性（作者如何对待） |
|---|---|---|---|
| A3 连续模型刚性层 | 晶格弛豫/原子重构 | 能带定量、赝朗道能级 | 非致命——弛豫后 TZM 定性不变、波函数更局域（§2.5）📜Q |
| A1 谷间耦合可忽略 | 大角/谷间散射 | K/K′ 独立计算、谷锁定 | 致命——小角前提 📜Q |
| A4 弱耦合极限 | 大 $u$ 超出微扰 | 两带模型定量 | 局部——pseudospin matching 论证大 $u$ 下仍解耦（§2.4）📜Q |
| A5 两带模型 | 小 $\Delta$（不满足 $\Delta/2\gtrsim u$） | 窗口起源解释 | 局部——完美 1D 模条件 $\Delta\gtrsim200$ meV 📜Q |
| A2 单粒子 | 关联/相互作用 | TZM 图像 | 未处理 💭I |
| A7 长程杂质不混谷 | 短程无序 | 完美导电通道 | 作者明言短程无序是主要散射、详细研究留待未来 📜Q |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（本文预言的实验靶标）

- 能带 $E(k)$（三交叉平面、近直费米线）+ 波函数空间局域（1D 沿畴壁、绕过 AA）📜Q；
- 无 AB 振荡（TZM 完整形成时）；磁振荡出现在 TZM 未完整形成时（偏置不足或 $E_F$ 不在窗口）📜Q；
- 1D 通道数 → 电导平台（每谷每自旋每方向 1 条 TZM，计数见 [PHY-LB]）推导。

### 5.2 设计原则（TZM 完整形成条件）

大偏置 $\Delta\gtrsim200$ meV + $E_F$ 在 1D 窗口内（$|E_F|\lesssim u$）→ TZM 完整形成、弹道输运主导 📜Q。

### 5.3 后续文献修正（时间倒挂，💭I）

- **De Beule 2020（T15）**：散射统一理论（$\phi=0$=TZM / $\phi=\pi/2$=pLL 两极限），提供"网络 vs TZM"中间地带。
- **Hou 2024（T29, NQCP）**：量子输运裁决——TZM 成立、预言近量子化电导平台（NQCP 接近 1/2/3 × $2e^2/h$）。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 单粒子、无相互作用 | 全文未讨论关联/相互作用 | 💭I |
| 无序散射未详算 | "A detailed study of the disorder scattering will be left for future works" | 📜Q（Sec. V） |
| 有限温输运未计算 | 原文仅定性讨论弹道输运条件 | 💭I |
| 电导是否严格量子化未裁决 | 本文不给电导数值；后作 T29（Hou 2024）以 NQCP 补充 | 💭I（外部对标） |
| 相图边界未系统展开 | 不同 Δ/θ 的窗口边界仅示数算例（θ=0.2°–1°、Δ 至 400 meV） | 📜Q[~] |
| 无 AB 振荡是"预言"非实测 | 与已报道 AB 实验（refs 34–36）的对照是预测性解释 | 📜Q（Sec. V） |

---

## 7. 与其他工作的关系（跨论文对标放这里，不放正文）

| 工作 | 关系 |
|------|------|
| Efimkin & MacDonald 2018 (ref 18) | 网络模型——本文核心分歧：偏置 TBG 是其 special case（置换型散射）📜Q（引言） |
| Fleischmann et al. 2020 (ref 19) | 完美 nesting 费米面——本文结果与之**一致** 📜Q |
| Ramires & Lado 2018 (ref 17) | 赝朗道能级——本文 Fig. 2a 平台解释引用 📜Q（Sec. II） |
| San-Jose & Prada 2013 (ref 15) | 偏置下螺旋网络（前作图景）📜Q（引言） |
| Wakabayashi et al. 2007 (ref 56) | zigzag 纳米带完美导电通道——TZM 的 2D 类比 📜Q（Sec. IV） |
| Rickhaus 2018 (ref 34) / Yoo 2019 (ref 35) / Xu 2019 (ref 36) | 偏置小角 TBG 输运/STM 的显著 AB 振荡——本文预测 TZM 完整形成时**无 AB**，振荡出现在 TZM 未完整形成时 📜Q（Sec. V） |

> ⚠️ Phase S 外部对标（**非本文引用**，时间倒挂，💭I）见 §5.3；引用关系依据 `cards.md` Q2 卡片与 `appendix_B_theory.md` §B.2。

---

## 8. 对后续研究的影响

- 给出**实验判别设计**：TZM 完整形成（大偏置 + $E_F$ 在窗口）→ 无 AB 振荡；观测到 AB → 提示 TZM 未完整形成（偏置不足或 $E_F$ 不在窗口）📜Q。
- 确立"**网络输运 vs 独立 1D 链输运**"的判别框架，为后续实验设计提供核心概念裁决标准 💭I。
- 留下开放问题：电导量子化程度（T29 承接）、无序/温度效应（未算）📜Q→💭I。
- 触发散射统一理论（T15）与 NQCP 裁决（T29）的谱系下游 💭I（外部对标）。

---

## 9. 理论模型映射（供 TBPM / Kubo-Bastin 对标）

| 映射 | 说明 |
|------|------|
| $\theta\to\Delta K=4\pi\theta/(3a)$ | 扭角→moiré 动量偏移→几何窗口 📜Q |
| $\Delta\to\pm\Delta/2$ | 层间偏置→两层 Dirac 能移 📜Q |
| $u\to$ 窗口宽度 | 层间耦合→窗口宽度 $\sim u$ 📜Q |
| 通道数→电导平台 | 每谷每自旋每方向 1 条 TZM；Landauer-Büttiker 计数见 [PHY-LB]（推导） |
| $n_W=1.08\times10^{12}\,\mathrm{cm^{-2}}$ | 到达 1D 窗口的预言载流子密度（θ=0.3°, Δ=200 meV）📜Q |
| 1D 模不围三角畴→无 AB | 与 E12 的 AB 振荡判别对照（TZM 完整 vs 未完整）📜Q |

> 与 TBPM/Kubo 对应：能带 E(k)、费米面、波函数局域可经 TB 直接复现；电导平台需 Landauer/Fisher-Lee 透射计算（有限器件）；AB 振荡为有限尺寸相干效应，bulk σxx 只给背景 💭I。

---

## Phase S 目的接口（三问引用式 + 增量价值）

- **Q1（edge state 如何表征）**：理论表征 = 能带 $E(k)$（三交叉平面、近直费米线）+ 波函数空间局域（1D 沿畴壁、绕过 AA）+ 通道计数（每谷每自旋每方向 1 条）——详见 §2/§3。
- **Q2（理论如何解释）**：本文 = 推翻网络图景的 TZM 理论；AA 节点置换型散射（mode 1↔mode 2 @ ±120°）→ 三组独立 zigzag 模、无分束不杂化 📜Q——详见 §2.3。
- **Q3（理论↔实验对应）**：预言 TZM 完整形成时**无 AB 振荡**；已报道 AB 振荡（Rickhaus/Yoo/Xu）= TZM 未完整形成（偏置不足或 $E_F$ 不在窗口）📜Q——详见 §3.3/§8。

> **增量价值**：与 E12（实验，AB 振荡证实网络连通）形成**正面对照**——本文（理论）论证 TZM 完整时无 AB、E12 观察 AB = TZM 未完整形成的证据；对"网络 vs 独立 1D 链"的判别是本族笔记的核心概念裁决点。report.md 用其 TZM 结论（置换型散射）+ §3 预言（无 AB 条件、Δ≳200 meV、n_W 换算）。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` 提取正文到 `/tmp/T12.txt`（517 行），逐项 grep 核对：**全部数字/专名命中原文**——

| 数字/专名 | grep 命中位置 | 结论 |
|------|--------------|------|
| u=0.103 eV、ħυ/a=2.1354、a=2.46 Å | Sec. II | ✓ 📜Q[~] |
| θ=1°,0.5°,0.3°,0.2°；Δ 至 400 meV | Fig. 2a / Sec. II | ✓ 📜Q[~] |
| E_F=50 meV（Fig. 2d）、20 meV（Fig. 6c/d） | Fig. captions | ✓ 📜Q[~] |
| n_W=1.08×10¹² cm⁻²（θ=0.3°, Δ=200 meV） | Sec. IV | ✓ 📜Q[~] |
| Vppπ⁰≈−2.7、Vppσ⁰≈0.48、d₀≈0.334、a₀≈0.142、r₀=0.184a | Sec. III | ✓ 📜Q[~] |
| 50<|E|<100 meV（θ=0.3°）、θ=0.55°（Fig. 4） | Sec. II / Fig. 4 | ✓ 📜Q[~] |
| +e²/h、−e²/h、2e²/h | 引言 | ✓ 📜Q |
| |ΔK_j|=4πθ/(3a)、n_W=g_vg_sΔK/(4πħv)、D(E)=g_vg_sΔ/(2πħ²v²) | Sec. II/IV | ✓ 📜Q |
| ⟨k+ΔK_j,+|U|k,−⟩≈iu sin[θ(k)−2πj/3] | Eq. (11) | ✓ 📜Q |
| Δ/2≳u 即 Δ≳200 meV；|E_F|≲u | Sec. V | ✓ 📜Q |
| "a few nanometers"（短程无序） | Sec. V | ✓ 📜Q |
| "mode 1 ... −120° ... mode 2 ... +120°"、"three independent zigzag traveling modes" | Sec. III | ✓ 📜Q |
| "do not actually form a percolating network"、"special case of the network model" | 摘要/引言 | ✓ 📜Q |
| "these states never hybridize" | Conclusion | ✓ 📜Q |
| "we do not have the Aharonov-Bohm oscillation"、"do not enclose triangular domains" | Sec. V | ✓ 📜Q |

⚠️ 修正/降级：① S 矩阵"对角"→"置换型"（沿用 §B.5#13 修正，grep "120" ✓）。② arXiv:2001.06257 正文未出现 → 头部表已标"外部来源"。③ De Beule 2020 / Hou 2024 对标为**后续**工作（本文 2020 出版、引用列表无此二者）→ 标时间倒挂 💭I。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-06 | 初读（research_onboarding Phase 4 风格）：连续模型 + TB + 弛豫 + 两带模型起源；S 矩阵误记为"对角" |
| 2026-08-20 (S-REV) | **§3.2/§8 "S 矩阵对角"修正**：改为置换型确定性散射——原文非对角矩阵，而是 "mode 1 is always scattered to mode 2 in the −120° direction, while mode 2 is always scattered to mode 1 in the +120° direction"（grep "120" ✓）→ 三组独立 zigzag 模。依据 `Phase_S/appendix_B_theory.md` §B.5#13 + `cards.md` T12 |
| 2026-09-01 | **按 4 块辨识结构整体重写**：对齐 E12 结构/粒度/证据标注，§3 改为「理论模型与方法」；新增四层变量表、可辨识性判别表（网络 vs TZM 四条判别）、[前提与限定]、主结果↔判别映射、§9 理论模型映射、反向核对 pass；保留旧 📜Q 事实 |
| 2026-09-01 | **降级/删除无源内容**：① De Beule 2020 / Hou 2024 对标从旧 §5 移入 §7 并降级 💭I（时间倒挂、非本文引用）；② 旧 §2.1 "Rickhaus/Huang 实验支持网络图景"改为原文 "network probed by transport [34–36] / STM [37]"；③ 旧 §6 "未计算有限温输运""电导量子化未裁决"标 💭I |
| 2026-09-08 | **按 5 块演绎结构整体重写**（应用户要求）。旧 4 块版归档 `archive/paper_review_T12_tsim2020_prb.backup_20260908.md`。黑箱三要素/四层变量表/判别表/[前提与限定] → 拆为"模型白箱（连续模型+参数分册+7 条假设清单）"+"推导链（前提定理/模型/推导/边界四层）"+"结论清单（定理/估算/预言分层）"+"假设-结论依赖图"+"接口"；内部验证（§3.4）+ 概念区分（§3.5）取代判别表；删"反推量 θ̂"层。全部 📜Q 事实与数字无丢失。 |
