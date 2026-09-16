<!--
 * @Author       : AI 精读（白箱演绎结构）
 * @Date         : 2026-08-06（初读）→ 2026-09-02（4 块辨识结构，理论版）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T15_debeule2020_prl.md
 * @Description  : T15: De Beule, Dominguez & Recher 2020 PRL — mTBG 谷霍尔态网络的散射统一理论（2026-09-08 按 5 块演绎结构重写：模型白箱/推导链/结论清单/假设-结论依赖图/接口）
-->

# Paper Review: De Beule, Dominguez & Recher (2020) — mTBG 网络的 AB 振荡散射理论

| 字段 | 内容 |
|------|------|
| **编号** | T15 |
| **标题** | Aharonov-Bohm Oscillations in Minimally Twisted Bilayer Graphene |
| **作者** | C. De Beule, F. Dominguez, P. Recher |
| **期刊** | Physical Review Letters **125**, 096402 (2020)（Received 12 Mar 2020 / published 25 Aug 2020）📜Q |
| **DOI / arXiv** | 10.1103/PhysRevLett.125.096402 / arXiv:2005.05352（⚠️ arXiv 号正文未出现，外部来源） |
| **类型** | 理论 — 网络散射统一理论（唯象 S 矩阵） |
| **课题组** | Institute for Mathematical Physics, TU Braunschweig（De Beule, Dominguez）；Recher 兼 Laboratory for Emerging Nanometrology 📜Q |
| **PDF / SI** | ✅ `reference/pdfs/De Beule 等 - 2020 - Aharonov-Bohm Oscillations in Minimally Twisted Bilayer Graphene.pdf`（正文 6 页 + SI[39]） |
| **精读日期** | 2026-08-06（初读）→ 2026-09-02（4 块辨识结构）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」的五块记（见 `note/shared/method/theory_paper_reading.md` §3）：**① 模型白箱 → ② 推导链 → ③ 结论清单（分层）→ ④ 假设-结论依赖图 → ⑤ 接口**。理论论文无黑箱、无反推、无可辨识实验（是"白箱演绎"而非"黑箱溯因"），故不用"四层变量表 + 判别表"这套实验框架词汇（旧 4 块版已废弃）。
> **共享知识引用**：通用物理（AB 干涉/退相干、SdH/LK、Landauer-Büttiker 通道计数、网络 miniband、valley Chern）已剥离到 `note/shared/physics/`，用锚点 `[PHY-AB] [PHY-SDH] [PHY-LB] [PHY-MB] [PHY-BERRY]` 引用，不重复讲义。阅读疑问见 `note/shared/method/mechanism_questions.md` `[METHOD-Q]`。

---

## TL;DR

**本文想解决的问题**：极小扭角 mTBG 在层间偏压 U 下形成谷霍尔态三角网络；微观计算给出 1D 手征 ZZ 模，但现有网络理论（假设 AA 节点双通道去耦）无法复现，输运实验（AB 振荡）也与"去耦 1D 手征模"矛盾——**AA 节点处两通道到底耦不耦合？网络输运（尤其 AB 振荡）的输运理论是什么？** 📜Q（引言）

**主结果**：① **无前向散射时，对称性把网络模型压缩为单参数** $\phi\in[0,\pi/2]$（120° 偏转相位），$\phi$ 在 1D 手征 ZZ 模（$\phi=0$）与赝朗道能级 pLL（$\phi=\pi/2$）之间插值 📜Q；② **平行 ZZ 链耦合 → 准 1D 区间 → AB 振荡（能量无关、温度稳健）；不同方向 ZZ 耦合 → 2D 区间 → SdH 振荡（有限温度被抹平）** 📜Q；③ 由此 **统一** ZZ 模与 pLL，二者同源于网络 📜Q。

**结论/意义**（保留作者措辞强度）：作者称"provide for the first time a transport theory for the topological network in minimally twisted bilayer graphene under interlayer bias"、与 $\theta\sim0.1°$ 低场实验 "agree well" 📜Q。⚠️ 全为唯象散射理论结论，非第一性验证；"首次/统一"是作者断言。

---

## 1. 模型白箱（理想系统 + 假设清单）

> 理论论文的研究对象是**白箱**——作者自写的理想模型，无需"反推内部"。本节只做两件事：**写下模型**（§1.1），**列出它成立的全部假设**（§1.3）。假设清单是本文一切结论的"前提集合"，§4 的依赖图据此展开。

### 1.1 网络散射模型（S 矩阵）

**网络四要素** 📜Q（引言+Fig. 1）：① $\theta\sim0.1°$ 下晶格弛豫成 sharp 的三角 AB/BA 畴 [13–15]；② 层间偏压 U 在 AB/BA 畴区开隙，谷 Chern 数 $N_K=-N_{K'}\approx\pm\mathrm{sgn}(U/\gamma_\perp)$（± 对应 AB/BA，$\gamma_\perp$ 为层间 hopping）[16,17]；③ 每谷每自旋沿畴壁 2 条手征模、不同谷反向传播 [17–21]；④ 费米能调进隙内 → 低能激发全由谷霍尔态三角网络承载 [22–26]。

每个散射节点 **6 进 6 出**（2 通道 × 3 方向，Fig. 1b）📜Q。对称性约束（Eq. 1）：
$$C_3:\ S=C_3SC_3^{-1},\qquad C_2\mathcal T:\ S=S^t$$
$C_3$（$2\pi/3$ 旋转，交换子晶格与谷）对入射模做循环置换 $(a_1,a'_1)\to(a_2,a'_2)\to(a_3,a'_3)\to(a_1,a'_1)$；$C_2\mathcal T$（spinless 时间反演）是保谷对称性（小扭角下与扭心无关 [37,38]）📜Q。

**无前向散射时**，S 矩阵在幺正变换等价意义下由单参数 $\phi\in[0,\pi/2]$（120° intrachannel 偏转相位）决定（Eq. 2）📜Q：
$$S=\frac12\begin{pmatrix}S_{\phi,\phi}&S_{0,\pi}\\S_{\pi,0}&-S_{-\phi,-\phi}\end{pmatrix},\quad S_{\vartheta,\psi}=\begin{pmatrix}0&e^{i\vartheta}&e^{i\psi}\\e^{i\psi}&0&e^{i\vartheta}\\e^{i\vartheta}&e^{i\psi}&0\end{pmatrix}$$
$\phi$ 被作者明确处理为**唯象参数**（"which we treat as a phenomenological parameter" 📜Q）。

**变量含义表**：

| 符号 | 含义 | 值/定义 |
|---|---|---|
| $\phi$ | 120° 偏转相位（唯象，唯一控制参数） | $[0,\pi/2]$ |
| $P_{f1},P_{f2}$ | intra/interchannel 前向散射概率 | 只经 $f=\sqrt{P_{f2}}+i\sqrt{P_{f1}}$ 进入 |
| $P_d$ | 偏转概率 | $4P_d+P_f=1$，$P_f=P_{f1}+P_{f2}$ |
| $l$ | moiré 晶格常数 | $a/[2\sin(\theta/2)]$ |
| $A$ | moiré 单胞面积（含一 AB 一 BA 三角） | $\sqrt3\,l^2/2$ |
| $\lambda$ | 动力学相位 | $e^{iEl/\hbar v}$ |
| $\Phi$ | 穿 moiré 单胞磁通 | $BA$，$\Phi_0=h/e$ |
| $v$ | 谷霍尔态速度（两态相等） | 固定参数 |

### 1.2 参数分册（替代旧"四层变量表"：区分"作者设定" vs "推导所得"）

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | $\phi$（唯象偏转相位）、$P_{f1},P_{f2},P_d$（散射概率）、$B$（磁场→Peierls 相位）、$E$（能量→动力学相位）、$L,W$（条带几何） |
| **导出量（由旋钮+常数算出）** | $l=a/[2\sin(\theta/2)]$、$A=\sqrt3 l^2/2$、$\Phi=BA$、$\lambda=e^{iEl/\hbar v}$、$k_j=k\cdot l_j$ |
| **模型内部量（解的性质）** | $S$ 矩阵（6×6）、网络能带（$[1_2\otimes M(k)]S$ 本征值相位）、色散 $E_{j,n}(k)$、透射 $T$、通道数 $N_i$ |
| **固定常数** | $a$（晶格常数）、$v$（谷霍尔态速度）、$\gamma_\perp$（层间 hopping）、$\theta$（样品扭角→$l$） |
| **预言量（可检验）** | 色散 $E(k)$、磁电导 $G(\Phi)/G_0$、AB/SdH 振荡、温度依赖 |

> 无"反推量 θ̂"层——本文不反推实验参数（$\phi$ 是唯象参数，未从微观模型导出 📜Q）。

### 1.3 显式假设清单（本文结论的前提集合）

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **忽略 intervalley 散射**（小扭角 moiré 缓变） | 模型 | 📜Q |
| A2 | **磁场"sufficiently small"**：S 矩阵结构不变，只经 Peierls 相位进入 | 推导 | 📜Q |
| A3 | **两谷霍尔态速度相等 $v$** | 模型 | 📜Q |
| A4 | **偏转取同一 $P_d$**（不同偏转概率只加额外耦合、不质变） | 推导 | 📜Q |
| A5 | **零温零偏磁电导**（有限温度仅 Fig. 5 定性） | 推导 | 📜Q |
| A6 | **无前向散射起点**（网络几何使偏转重叠大于前向） | 推导 | 📜Q |
| A7 | **disorder（扭角/电荷密度涨落）展宽 AB 共振**（SI[39] 定性） | 模型 | 📜Q |

> 判别性扫轴：$\phi$（0→π/2 两极限）、$P_f$（前向散射开启）、$\Phi=BA$（磁通轴）、$T/T_l$（热轴，Fig. 5）。这些假设在 §4 逐一映射到"失效 → 结论崩塌"。

---

## 2. 推导链（演绎结构：顺论文顺序，每步"输入→输出→所用假设/定理→合法域"）

### 2.0 总览：论文是一条演绎链

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 前提定理层 | 引言（矛盾） | 微观 ZZ 模 + 网络理论 + 输运实验 | 问题设定：AA 节点耦合 | refs 23,27–30 | — |
| 模型层 | Network model | 6×6 S 矩阵 + 对称性 | 单参数 $\phi$（Eq. 2） | A1、$C_3$+$C_2\mathcal T$ | 无前向散射（A6） |
| 推导层 | 色散两极限 | S 矩阵 + 幺正变换 | $\phi=0$→ZZ / $\phi=\pi/2$→pLL | 幺正变换 $U$ | — |
| 推导层2 | 前向散射耦合 | 加 $P_{f1},P_{f2},P_d$ | 准 1D vs 2D 两区间 | A3、A4、流守恒 | — |
| 边界层 | Magnetotransport | Peierls 相位 + Landauer | AB（稳健）vs SdH（抹平） | A2、A5 | 零温零偏、弱场 |

### 2.1 前提定理层（引言）：核心矛盾

- **微观计算**给出 1D 手征 ZZ 模 [27,28]（Fleischmann 2020、Tsim-Nam-Koshino 2020）；但"current network theories [23] cannot reproduce these results"，且输运实验的干涉振荡与"去耦 1D 手征模" incompatible [29,30]（Rickhaus 2018、Xu 2019）📜Q。
- **本文切入**：两谷霍尔态沿链路不混（无无序），但到 AA 区（层间偏压诱导的局域隙消失）没理由保持去耦；且无前向散射的构造"impossible if the two valley Hall states are decoupled"（去耦时有前向散射下界 [23]）📜Q。

### 2.2 模型层：对称性压缩到单参数 $\phi$

- 6 进 6 出 S 矩阵受 $C_3$（循环置换）+ $C_2\mathcal T$（$S=S^t$）约束（Eq. 1）📜Q；无前向散射时压缩到单参数 $\phi\in[0,\pi/2]$（Eq. 2）📜Q。
- **幺正变换**（对称/反对称基）：$U=e^{-i\pi\sigma_y/4}e^{i\phi\sigma_z/2}\otimes\mathbb 1_3$，$a_\pm=(a e^{i\phi/2}\mp a' e^{-i\phi/2})/\sqrt2$（出射同理）——把"两谷霍尔通道"旋转为"同一链路上的对称/反对称叠加"，使 $\phi$ 的物理（偏转 vs 前向分配）显式化 📜Q。

### 2.3 推导层：色散两极限（$\phi=0$ vs $\phi=\pi/2$）

- **$\phi=0$** → 只保留 interchannel 偏转，$a_+$ 逆时针、$a_-$ 顺时针 → **3 条独立手征 ZZ 链**，速度 $v/2$，线性色散 $E_{j,n}(k)=\frac{\hbar v}{2l}(2\pi n+k_j)$，$n\in\mathbb Z$（Eq. 3），能量周期 $\pi\hbar v/l$ 📜Q。
- **$\phi=\pi/2$** → 只保留 intrachannel 偏转，$a_+$ 逆时针绕 BA 畴、$a_-$ 顺时针绕 AB 畴 → 局域化 → **每周期 $2\pi\hbar v/l$ 内 3 条双重简并平带** = pLL 📜Q。（⚠️ 旧 review 误写"三重简并"，原文"three doubly degenerate flatbands"。）

### 2.4 推导层2：前向散射 → 两个输运区间

- 加入 intra/interchannel 前向散射（$P_{f1},P_{f2}$），偏转取同一 $P_d$；流守恒 $4P_d+P_f=1$，$P_f=P_{f1}+P_{f2}$ 📜Q。新基下（Eq. 4）：$USU^\dagger=\begin{pmatrix}S_1&S_2^\dagger\\S_2&-S_1^\dagger\end{pmatrix}$，$S_1=2i\sqrt{P_d}\sin\phi\,s_0+f\cos\phi\,\mathbb1_3$、$S_2=2\sqrt{P_d}\cos\phi\,s_0+if\sin\phi\,\mathbb1_3$、$f=\sqrt{P_{f2}}+i\sqrt{P_{f1}}$ 📜Q。
- **平行 ZZ 耦合（准 1D）**：$\phi=0$ 时仅 $S_1$ 通过 intrachannel 前向散射耦合**平行** ZZ 链（概率 $|f|^2=P_f$）→ 网络解耦为 3 套独立准 1D 系统（Fig. 2a）📜Q。
- **交叉 ZZ 耦合（2D）**：一般 $\phi\neq0$ 时不同方向 ZZ 链经**两个过程**耦合（Fig. 2d）：interchannel 前向散射（$P_f\sin^2\phi$）+ intrachannel 偏转（$4P_d\sin^2\phi$）→ 能带反交叉（Fig. 2e,f）→ 真 2D 逾渗系统 📜Q。

> ⚠️ **关键修正（沿袭 2026-09-02）**：原文**并未**把 $P_{f1}$ 对应"平行耦合"、$P_{f2}$ 对应"交叉耦合"。$P_{f1},P_{f2}$ 只经 $f=\sqrt{P_{f2}}+i\sqrt{P_{f1}}$（总 $P_f$）进入；**控制 AB vs SdH 的是 $\phi$（决定准 1D 还是 2D 区间），不是 $P_{f1}$ vs $P_{f2}$ 的拆分**（正文：两区间"characterized by the effective dimensionality" 📜Q）。

### 2.5 边界层：磁输运 AB vs SdH

- **Peierls 相位**（Landau 规范 $A=Bx e_y$）：水平链路相位 0，上/下斜链路 $\Phi_\pm(m)=\mp\pi(m+1/2)\Phi/\Phi_0$ 📜Q；$\Phi_0=h/e$，$\Phi=BA$，$A=\sqrt3\,l^2/2$ 📜Q。
- **零温零偏微分电导**（Landauer-Büttiker，$G/G_0=N_iT$，$N_i=4W/(\sqrt3\,l)$，$G_0=4e^2/h$，Eq. 5）；透射 $T$ 用连接左右 lead 的转移矩阵算（两谷在 $W\gg L$ 极限下相同）📜Q。
- **准 1D 区间（φ=0）→ AB 振荡**：$l_3$ 分支（手征、全透射）给常数平台背景；前向散射开启后 $l_{1,2}$ 分支反向传播模贡献干涉 → AB 共振。解析式（Eq. 6）$G/G_0\simeq(2+2P_f^{2L/l+1}[1+P_f(4P_d)^2F_L(\Phi)^2])W/(\sqrt3 l)$，$F_L(\Phi)=\sin[\pi(2L/l-1)\Phi/\Phi_0]/\sin(\pi\Phi/\Phi_0)$，峰宽 $\Delta\Phi=2\Phi_0/(2L/l-1)$；共振在 $\Phi=\Phi_0/n$（$n$ 非零整数）📜Q。**能量无关**（干涉路径等长、动力学相位抵消）→ **AB 共振温度稳健** 📜Q。
- **2D 区间（φ≠0）→ AB + SdH**：不同方向 ZZ 耦合 → SdH 振荡（"network Landau levels"，Fig. 5）；磁通周期性因加入单 AB/BA 三角路径而**加倍** 📜Q。有限温度下 SdH 被抹平，AB 主导 📜Q。

---

## 3. 结论清单（分层：定理 / 估算 / 预言）

> 理论论文的结论必须按**性质**分层，而非平铺。每条标：**依赖假设** + **可检验性**。

### 3.1 定理式主张（数学/对称性论证的产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 单参数压缩 | 无前向散射时 $C_3+C_2\mathcal T$ 把网络压为单参数 $\phi\in[0,\pi/2]$ | A1、A6、$C_3$+$C_2\mathcal T$ |
| ZZ 极限 | $\phi=0$ → 3 条独立手征 ZZ 链（速度 $v/2$，色散 Eq. 3） | 幺正变换 $U$ |
| pLL 极限 | $\phi=\pi/2$ → 3 条双重简并平带（每周期 $2\pi\hbar v/l$） | 同上 |
| AB 温度稳健 | 准 1D 区间干涉路径等长 → 能量无关 → 温度稳健 | A2、A5 |

### 3.2 估算（近似/解析式，非严格定理）

| 估算 | 值/表达式 | 依赖假设 | 证据 |
|---|---|---|---|
| ZZ 色散 | $E_{j,n}(k)=\hbar v(2\pi n+k_j)/(2l)$ | Eq. (3) | 📜Q[~] |
| ZZ 能量周期 | $\pi\hbar v/l$；速度 $v/2$ | — | 📜Q[~] |
| moiré 单胞面积 | $A=\sqrt3 l^2/2$；通道数 $N_i=4W/(\sqrt3 l)$；$G_0=4e^2/h$ | — | 📜Q[~] |
| AB 峰宽 | $\Delta\Phi=2\Phi_0/(2L/l-1)$；共振 $\Phi=\Phi_0/n$ | Eq. (6) | 📜Q[~] |
| 实验平台参考 | $h/8e^2\approx3.2$ kΩ（Ref[30] 平台） | — | 📜Q[~] |
| 温度标度 | $T_l=2\pi\hbar v/k_Bl\approx3400(\theta°)$ K | — | 📜Q[~] |
| 碳原子数 | moiré 单胞 $\sim10^4(\theta°)^{-2}$ | 引言 | 📜Q[~] |

### 3.3 预言（可检验性 → 见 §5.1）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| 平行耦合→温度稳健 AB；交叉耦合→温度敏感 SdH | "we find / we show"（推导结果）📜Q | 中——磁输运 + 温度依赖 |
| 统一 ZZ 模与 pLL | "our theory unifies these two phenomena"（定性断言）📜Q | 弱——唯象层 |
| 首个网络输运理论 | "provide for the first time a transport theory" 📜Q | 中——作者断言 |
| 与 θ∼0.1° 低场实验一致 | "agree well" 📜Q | 中——定性特征一致 |

### 3.4 内部验证（自洽核对，非"排除竞争解释"）

1. **色散极限互验**：$\phi=0$（线性 $v/2$ ZZ 链）与 $\phi=\pi/2$（平带 pLL）均由同一 Eq. 2 的 S 矩阵经幺正变换导出，两极限解析可控 📜Q[推导]。
2. **AB 温度稳健的机制链**：准 1D 区间干涉路径等长 → 能量无关 → 温度稳健（推导链，非数值验证）📜Q[推导]。
3. **与实验对标**：准 1D 区间磁电导与 Ref[30] 磁阻"integer fractions of the main period + plateau slightly above $h/8e^2\approx3.2$ kΩ" 定性特征一致 📜Q；但**主周期解读不同**（§3.5/§5.3）。

### 3.5 概念区分（作者论证中的"分类"，非溯因排除）

| 区分 | 依据 | 结论 |
|---|---|---|
| 节点耦合 vs 去耦 | "In contrast to previous network models [23], we take into account scattering at the nodes between the two channels" 📜Q | 耦合是理解微观/实验一致的关键 |
| ZZ vs pLL（φ 两极限） | $\phi=0$→ZZ / $\phi=\pi/2$→pLL，同一散射结构 📜Q | "unifies these two phenomena" |
| AB vs SdH（维度） | 平行耦合（准 1D）→AB；交叉耦合（2D）→SdH 📜Q | 有效维度决定振荡类型 |

> 注：这些是**概念/图景分类**（taxonomy），不是实验论文那种"数据排除竞争解释"（溯因排除）——理论论文没有后者。

---

## 4. 假设-结论依赖图（含金量所在）

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性（作者如何对待） |
|---|---|---|---|
| $\phi$ 唯象（无微观来源） | θ、U、弛豫未映射到 $\phi$ | "统一"停在唯象层 | **致命缺口**——作者明言 "phenomenological parameter" 📜Q |
| A1 忽略 intervalley 散射 | 大角/谷间散射 | 谷锁定、单参数压缩 | 声明忽略但未证安全 📜Q |
| A2 弱场近似 | 磁场足够大改变 S 矩阵 | AB 共振定量 | 适用域边界 📜Q |
| A3 两谷速度相等 | 速度不等 | 转移矩阵、$G$ 定量 | 假设 📜Q |
| A4 同一 $P_d$ | 不同偏转概率 | 额外耦合（不质变） | 作者声称不质变 📜Q |
| A5 零温零偏 | 有限温/有限偏压 | SdH 被抹平（Fig. 5 定性） | 适用域边界 📜Q |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（本文预言的实验靶标）

- 平行耦合（准 1D）→ 温度稳健 AB 振荡；交叉耦合（2D）→ 温度敏感 SdH → 可作 $\phi$ 取值（准 1D 还是 2D）的判据 💭I；
- AB 主周期 = 每 moiré 单胞一磁通量子（非单三角畴）📜Q。

### 5.2 设计原则（$\phi$ 作为控制参数）

$\phi$ 连续插值 ZZ（$\phi=0$）↔ pLL（$\phi=\pi/2$），控制网络的**有效维度**（准 1D vs 2D）→ 决定磁输运振荡类型 📜Q。

### 5.3 后续文献修正（时间倒挂，💭I）

- **Xu 2019 (Ref[30]) 主周期重解释**：准 1D 区间不允许单三角畴路径 → 主周期对应 moiré 单胞 → 等价于把 Ref[30] 报告的扭角放大 $\sqrt2$ 倍 📜Q。
- **Hou 2024（T29, NQCP）**：量子输运裁决（独立通道 + 近量子化平台），对本散射框架的延续。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| $\phi$ 唯象 | "we treat as a phenomenological parameter"，未从微观模型（θ、U、弛豫）导出 | 📜Q |
| 无微观参数映射 | 未给出 θ、U → $\phi$、$v$ 的定量关系 | 💭I（本文未做） |
| 零温/弱场近似 | 磁电导在零温零偏；有限温度仅 Fig. 5 三条曲线定性 | 📜Q |
| disorder 仅定性 | 扭角/电荷密度涨落展宽 AB 共振（SI[39] 提及，未给定量） | 📜Q |
| intervalley 散射忽略 | 声明 moiré 缓变故忽略，未证其对结果安全 | 📜Q |
| 前向散射简化 | 取同一 $P_d$；"do not change our results qualitatively" | 📜Q |
| 未做数值微观对照 | 与微观计算（ZZ 模 [27,28]）只定性一致，未做定量能谱对照 | 💭I |

---

## 7. 与其他工作的关系（跨论文对标放这里，不放正文）

| 工作 | 关系（本文视角） |
|------|-----------------|
| Efimkin & MacDonald 2018 ([23]) | "current network theories"——本文超越之：其假设 AA 节点双通道去耦，无法复现 ZZ 模；去耦时前向散射有下界 📜Q |
| Ramires & Lado 2018 ([24]) | pseudo-Landau levels 的来源（φ=π/2 极限对应 pLL[24]）📜Q |
| Fleischmann 2020 ([27]) / Tsim-Nam-Koshino 2020 ([28]) | ZZ 模来自微观计算；本文 φ=0 极限给出其散射理论框架 📜Q |
| Rickhaus 2018 ([29]) | 输运干涉振荡实验，与"去耦 1D 手征模" incompatible（本文动机之一）📜Q |
| **Xu 2019 ([30])** | AB 振荡实验；本文准 1D 区间磁电导与其定性特征一致，但**重解释主周期**（moiré 单胞 vs 单三角畴 → 扭角 ×$\sqrt2$）📜Q |

> ⚠️ **引用列表核对结论**：Rickhaus **确为 [29]**、Xu **确为 [30]**，两者均在本文参考文献列表 ✅。⚠️ Phase S 外部对标（非本文引用，时间倒挂 💭I）见 §5.3。

---

## 8. 对后续研究的影响

- 为 mTBG 谷霍尔态网络提供**首个输运理论**（作者自述），把 AB 与 SdH 振荡统一到同一散射框架 📜Q。
- 给出可实验甄别预言：平行耦合→温度稳健 AB；交叉耦合→温度敏感 SdH → 可作 $\phi$ 取值的判据 💭I。
- 留下明确缺口：$\phi$ 的微观导出（θ、U、弛豫依赖）——是本文未闭合的唯象参数 📜Q→💭I。

---

## 9. 理论模型映射（供 TBPM / Kubo-Bastin 对标）

| 映射 | 说明 |
|------|------|
| $\theta\to l=a/[2\sin(\theta/2)]\to A=\sqrt3 l^2/2$ | 扭角→moiré 晶格常数→网络单胞面积 📜Q |
| $\phi$（唯象）→ S 矩阵 | 可由 TBPM/紧束缚微观散射反推（本文未做，是开放任务）💭I |
| $B\to$ Peierls 相位 | $\Phi_\pm(m)=\mp\pi(m+1/2)\Phi/\Phi_0$（Landau 规范）📜Q |
| $E\to$ 动力学相位 | $\lambda=e^{iEl/\hbar v}$ 📜Q |
| 通道数 → 电导 | $N_i=4W/(\sqrt3 l)$，$G_0=4e^2/h$ 📜Q |
| 观测量 | $G(\Phi)/G_0$（器件量）；AB/SdH 振荡 |

> 与 TBPM/Kubo 对应：本文算的是**有限网络条带**的 Landauer 电导 $G(\Phi)$（转移矩阵），非 bulk $\sigma_{xx}$；复现需有限尺寸网络散射/转移矩阵计算，bulk Kubo 只给背景 💭I。

---

## Phase S 目的接口（三问引用式）

- **Q1（edge state 如何表征）**：本文不直接表征，而是给**网络输运的散射模型**——AA 节点双通道 S 矩阵（6 进 6 出）+ 对称性约束 → 单参数 φ；φ=0 ↔ 1D 手征 ZZ 模、φ=π/2 ↔ pLL（见 §2.2/§2.3）。
- **Q2（理论如何解释）**：核心 = 网络散射统一理论：无前向散射单参数 φ 插值 ZZ↔pLL；前向散射下平行耦合→AB（稳健）、交叉耦合→SdH（抹平）（见 §2.4/§2.5）📜Q。
- **Q3（理论↔实验对应）**：AB 振荡 ↔ 平行 ZZ 耦合（准 1D，φ=0）；SdH ↔ 交叉 ZZ 耦合（2D）；主周期 ↔ moiré 单胞（非单三角畴）→ 对 Xu 2019 扭角 ×$\sqrt2$ 重解释（见 §2.5/§5.3）📜Q。

> **增量价值**：这是 Q2 理论 8 篇里唯一给出**AA 节点散射的对称性约束解**（C3+C2T → 单参数 φ）并**统一 ZZ 模与 pLL**的论文；为"网络 vs TZM 之争"提供中间地带方案（散射相位连续插值）。比 TZM[28]/网络[23] 多的是"节点耦合"这一步，少的是"微观参数（θ、U）→φ"的定量映射。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` 提取正文（6 页）+ `pdftotext -raw` 复核，逐项 grep 核对：**全部数字/符号命中原文**——

| 数字/符号 | grep 命中位置 | 结论 |
|------|--------------|------|
| φ∈[0,π/2]、6 进 6 出 | Network model 节 | ✓ 📜Q |
| $l=a/[2\sin(\theta/2)]$、$l_{1,2}=l(-1/2,\pm\sqrt3/2)$ | Network model 节 | ✓ 📜Q |
| $N_K=-N_{K'}\approx\pm\mathrm{sgn}(U/\gamma_\perp)$ | 引言 | ✓ 📜Q |
| $C_3:S=C_3SC_3^{-1}$、$C_2\mathcal T:S=S^t$ | Eq. (1) | ✓ 📜Q |
| Eq. (2) S 矩阵、$S_{\vartheta,\psi}$ | Eq. (2) | ✓ 📜Q |
| $E_{j,n}(k)=\hbar v(2\pi n+k_j)/(2l)$、$v/2$、$\pi\hbar v/l$ | Eq. (3) | ✓ 📜Q |
| 3 条双重简并平带、$2\pi\hbar v/l$ | Network model 节 | ✓ 📜Q |
| $U=e^{-i\pi\sigma_y/4}e^{i\phi\sigma_z/2}\otimes1_3$、$a_\pm/\sqrt2$ | Network model 节 | ✓ 📜Q |
| $4P_d+P_f=1$、$f=\sqrt{P_{f2}}+i\sqrt{P_{f1}}$ | Coupling 节/Eq. (4) | ✓ 📜Q |
| $P_f\sin^2\phi$、$4P_d\sin^2\phi$ | Coupling 节 | ✓ 📜Q |
| $\Phi_0=h/e$、$G_0=4e^2/h$、$N_i=4W/(\sqrt3 l)$ | Magnetotransport/Eq. (5) | ✓ 📜Q |
| Eq. (6)、$F_L(\Phi)$、$\Delta\Phi=2\Phi_0/(2L/l-1)$、$\Phi=\Phi_0/n$ | Magnetotransport 节 | ✓ 📜Q |
| $h/8e^2\approx3.2$ kΩ、$T_l\approx3400(\theta°)$ K、$10^4(\theta°)^{-2}$ | 正文/Fig. 5 | ✓ 📜Q |
| Fig. 参数 0.04/0.02/0.2/0.3/10l/0.005/0.01/$\pi\hbar v/6l$ | Fig. captions | ✓ 📜Q[读图] |
| "unifies these two phenomena"、"provide for the first time a transport theory" | Conclusion | ✓ 📜Q |
| "agree well"、twist angle ×√2 | Conclusion/正文 | ✓ 📜Q |

⚠️ 修正/降级：① pdftotext（-layout）丢失部首符号 √，已用 `-raw` 重提确认（$A=\sqrt3 l^2/2$、$N_i=4W/(\sqrt3 l)$、$a_\pm/\sqrt2$、$f=\sqrt{P_{f2}}+i\sqrt{P_{f1}}$）。② 修正「$P_{f1}$↔平行/$P_{f2}$↔交叉」映射（原文无此对应，控制 AB vs SdH 的是 $\phi$）。③ 修正「三重简并平带」→「3 条双重简并平带」。④ arXiv:2005.05352 正文未出现 → 头部表已标外部来源。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-06 | research_onboarding Phase 4 初读（旧 8 节格式 + Phase S Q2/Q3 补充） |
| 2026-09-02 | **4 块辨识结构整体重写**：TL;DR 问题句式 + 四层变量表 + 可辨识性判别表[理论版] + 三段结果 + 理论模型与方法 + 关键预言/数据 + 三问接口 + 反向核对 + 更正日志 |
| 2026-09-02 | **修正「Pf1↔平行/Pf2↔交叉」映射**：原文无此对应，$P_{f1},P_{f2}$ 只经 $f=\sqrt{P_{f2}}+i\sqrt{P_{f1}}$ 进入；控制 AB vs SdH 的是 φ（准 1D vs 2D 区间） |
| 2026-09-02 | **修正「三重简并平带」→「3 条双重简并平带」**（φ=π/2，每周期 $2\pi\hbar v/l$）；**删除**「Efimkin-MacDonald 网络态对应中间 φ」（pLL 对应 Ramires-Lado[24]） |
| 2026-09-02 | **删除无源/跨论文项**：「Tsim & Koshino 发现 ZZ 模不形成连通网络」、「De Beule 2021 (T18) Floquet」；**降级**「直接解释 Xu 2019」→「qualitative features 一致 + 主周期重解释（扭角×√2）」 |
| 2026-09-08 | **按 5 块演绎结构整体重写**（应用户要求）。旧 4 块版归档 `archive/paper_review_T15_debeule2020_prl.backup_20260908.md`。黑箱三要素/四层变量表/判别表/[前提与限定] → 拆为"模型白箱（S 矩阵+参数分册+7 条假设清单）"+"推导链（前提定理/模型/推导/边界四层）"+"结论清单（定理/估算/预言分层）"+"假设-结论依赖图"+"接口"；内部验证（§3.4）+ 概念区分（§3.5）取代判别表；删"反推量 θ̂"层。全部 📜Q 事实与数字无丢失。 |
