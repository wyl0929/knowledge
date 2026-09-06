<!--
 * @Author       : AI 精读 (系统辨识式阅读法 → 三层分离整理)
 * @Date         : 2026-08-06（初读）→ 2026-09-02（4 块辨识结构重读）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T15_debeule2020_prl.md
 * @Description  : T15: De Beule, Dominguez & Recher (2020) — mTBG 谷霍尔态网络的散射统一理论（4 块辨识结构；理论论文，§3 为理论模型与方法）
-->

# Paper Review: De Beule, Dominguez & Recher (2020) — mTBG 网络的 AB 振荡散射理论

| 字段 | 内容 |
|------|------|
| **编号** | T15 |
| **标题** | Aharonov-Bohm Oscillations in Minimally Twisted Bilayer Graphene |
| **作者** | C. De Beule, F. Dominguez, P. Recher |
| **期刊** | Physical Review Letters **125**, 096402 (2020) |
| **DOI / arXiv** | 10.1103/PhysRevLett.125.096402 / arXiv:2005.05352（⚠️ arXiv 号正文未出现，外部来源） |
| **类型** | 理论 — 网络散射统一理论（唯象 S 矩阵） |
| **课题组** | Institute for Mathematical Physics, TU Braunschweig（De Beule, Dominguez）；Recher 兼 Laboratory for Emerging Nanometrology 📜Q |
| **PDF / SI PDF** | ✅ `reference/pdfs/De Beule 等 - 2020 - Aharonov-Bohm Oscillations in Minimally Twisted Bilayer Graphene.pdf`（正文 6 页 + SI[39]，SI 未随正文提取） |
| **精读日期** | 2026-08-06（初读）→ 2026-09-02（4 块辨识结构重读） |

> **共享知识引用**：通用物理（AB 干涉/退相干、SdH/LK、Landauer-Büttiker 通道计数、网络 miniband、valley Chern）已剥离到 `note/shared/physics/`，本 review 用锚点 `[PHY-AB] [PHY-SDH] [PHY-LB] [PHY-MB] [PHY-BERRY]` 引用，不重复讲义。阅读疑问见 `note/shared/method/mechanism_questions.md` `[METHOD-Q]`。

---

## TL;DR

**本文想解决的问题**：极小扭角 mTBG 在层间偏压 U 下形成谷霍尔态三角网络；微观计算给出 1D 手征 ZZ 模，但现有网络理论（假设 AA 节点双通道去耦）无法复现，输运实验（AB 振荡）也与"去耦 1D 手征模"矛盾——**AA 节点处两通道到底耦不耦合？网络输运（尤其 AB 振荡）的输运理论是什么？** 📜Q（引言）

**主结果**：① **无前向散射时，对称性把网络模型压缩为单参数** $\phi\in[0,\pi/2]$（120° 偏转相位），$\phi$ 在 1D 手征 ZZ 模（$\phi=0$）与赝朗道能级 pLL（$\phi=\pi/2$）之间插值 📜Q；② **平行 ZZ 链耦合 → 准 1D 区间 → AB 振荡（能量无关、温度稳健）；不同方向 ZZ 耦合 → 2D 区间 → SdH 振荡（有限温度被抹平）** 📜Q；③ 由此 **统一** ZZ 模与 pLL，二者同源于网络 📜Q。

**结论/意义**（保留作者措辞强度）：作者称"provide for the first time a transport theory for the topological network in minimally twisted bilayer graphene under interlayer bias"、与 $\theta\sim0.1°$ 低场实验 "agree well" 📜Q。⚠️ 全为唯象散射理论结论，非第一性验证；"首次/统一"是作者断言。

---

## 1. 系统辨识导览（判别表为全文唯一权威，机制细节见 [PHY-*]）

**黑箱三要素**：`{输入旋钮：φ、Pf1/Pf2/Pd、B、E、L/W | 输出观测量：网络色散 E(k)、磁电导 G(Φ)/G0、AB/SdH 振荡、温度依赖 | 声称结论：单参数 φ 统一 ZZ 模与 pLL；平行耦合→AB(稳健)、交叉耦合→SdH(抹平)}`

**四层变量图**（符号层一次钉死，理论版）：

| 层 | De Beule 2020 实例 |
|----|-------------------|
| **L1 旋钮 u** | $\phi\in[0,\pi/2]$（唯象偏转相位）、$P_{f1},P_{f2}$（前向散射概率）、$P_d$（偏转概率，$4P_d+P_f=1$ 约束）、$B$（磁场→Peierls 相位）、$E$（能量→动力学相位 $\lambda$）、$L,W$（条带几何） |
| **L2 导出量 x₁** | $l=a/[2\sin(\theta/2)]$（moiré 晶格常数）、$A=\sqrt3\,l^2/2$（moiré 单胞面积）、$\Phi=BA$（单胞磁通）、$\lambda=e^{iEl/\hbar v}$（动力学相位）、$\Phi_0=h/e$、$k_j=k\cdot l_j$ |
| **L3 模型量 x₂** | $S$ 矩阵（6×6）、网络能带（$[1_2\otimes M(k)]S$ 本征值相位）、色散 $E_{j,n}(k)$、透射 $T$、通道数 $N_i$ |
| **固定参数（非旋钮）** | $a$（石墨烯晶格常数）、$v$（谷霍尔态速度，两态相等）、$\gamma_\perp$（层间 hopping）、$\theta$（样品扭角→$l$） |
| **反推量 θ̂** | 无（本文不反推实验参数；$\phi$ 是唯象参数，未从微观模型导出 📜Q） |
| **L4 观测量 y** | 色散 $E(k)$、磁电导 $G(\Phi)/G_0$、AB/SdH 振荡、温度依赖（$T/T_l$） |

**可辨识性判别表**（理论版：每条判别 = 判据 / 排除谁[竞争图景] / 确立谁）：

| 判别 | 判据（原文） | 排除谁 | 确立谁 |
|------|-------------|--------|--------|
| **节点耦合 vs 去耦** | "In contrast to previous network models [23], we take into account scattering at the nodes between the two channels"；且无前向散射"impossible if the two valley Hall states are decoupled, as in this case there is a lower bound on forward scattering [23]" 📜Q | 去耦网络模型（Efimkin-MacDonald [23]） | AA 节点双通道散射的必要性（耦合是理解微观/实验一致的关键） |
| **ZZ vs pLL（φ 两极限）** | $\phi=0$→interchannel 偏转、$v/2$ 的 3 条独立 ZZ 链（Eq. 3）；$\phi=\pi/2$→intrachannel 偏转、局域化平带 = pLL 📜Q | ZZ 模与 pLL 是独立现象 | 单一散射结构的两个极限（"unifies these two phenomena" 📜Q） |
| **AB vs SdH（耦合类型→维度）** | 平行 ZZ 耦合（准 1D，$\phi=0$）→AB 振荡且能量无关→温度稳健；不同方向 ZZ 耦合（2D，$\phi\neq0$）→SdH（network Landau levels）温度抹平 📜Q | AB 与 SdH 同源/同机制 | 两种耦合机制 → 两种可实验甄别的振荡 |
| **AB 周期归属** | 共振在 $\Phi=\Phi_0/n$（$n$ 非零整数），主周期 = 每 moiré 单胞一磁通量子；准 1D 区间**不允许**环绕单 AB/BA 三角畴的路径 📜Q | 单三角畴回路解释（Ref[30] 的解读） | moiré 单胞回路 → 与 Xu 2019 的周期解读有分歧（→§7） |

> **主结果 ↔ 判别表的对应**（每条主结果由哪几条判别确立）：
> - 主结果① 单参数 φ 统一 ZZ↔pLL ← {ZZ vs pLL}
> - 主结果② AB(稳健) vs SdH(抹平) ← {AB vs SdH, AB 周期归属}
> - （前提）AA 节点双通道散射必要 ← {节点耦合 vs 去耦}
>
> **"统一"是作者的概括而非定理**：φ=0 / π/2 两极限的色散（Eq. 3 线性 vs 平带）是**解析导出的** 📜Q[推导]；"unifies these two phenomena, showing that both arise from the network"是结论段的定性断言 📜Q，本文未做微观参数（θ、U）→φ 的映射，故"统一"停在唯象层。

> **[前提与限定]**（判别结论的适用范围）：
> - **近似/扰动**：忽略 intervalley 散射（小扭角 moiré 缓变 📜Q）；磁场"sufficiently small"使 S 矩阵结构不变、只经 Peierls 相位进入 📜Q；两谷霍尔态速度相等 $v$ 📜Q；前向散射取同一 $P_d$（"different deflection probabilities lead to additional couplings, but these do not change our results qualitatively" 📜Q）；磁电导计算在**零温零偏**（Fig. 3/4，有限温度仅 Fig. 5 定性）📜Q；disorder（扭角/电荷密度涨落）会使 AB 共振展宽（SI[39] 提及）📜Q。
> - **判别性扫轴**：$\phi$（0→π/2，两极限）、$P_f$（0→…前向散射开启）、$\Phi=BA$（磁通轴）、$T/T_l$（热轴，仅 Fig. 5 定性三条曲线）。
> - **候选集 M 边界**：本文是理论，"竞争图景" = {去耦网络模型[23]、ZZ 模[27,28]、pLL[24]}——单一散射结构在该集内给出统一解释。**集外未排除**：$\phi$ 的微观来源（唯象）、晶格弛豫/无序对 S 矩阵的具体修正、intervalley 散射（声明忽略但未证安全）须显式声明。

> 三层标注：📜Q = 原文事实（附位置）｜推导 = 由原文公式合成｜💭I = 背景/推断。**不确定度（与证据分级正交）**：[±] 原文误差棒 / [~] 原文以 =/≈ 给出但无误差棒 / [读图] 图提取·色标值 / [相对] 仅相对量。所有数字经 pdftotext + grep 反向核对；⚠️ **pdftotext 丢失部首符号 √**（已用 `pdftotext -raw` 重提逐式核对，见文末反向核对 pass）。

---

## 2. 结果与机制（按论文论证：网络模型 → φ 两极限 → ZZ 耦合 → 磁输运）

### 2.1 网络模型与节点散射（动机）

网络四要素 📜Q（引言+图1）：① $\theta\sim0.1°$ 下晶格弛豫成 sharp 的三角 AB/BA 畴 [13–15]；② 层间偏压 U 在 AB/BA 畴区开隙，valley Chern 数 $N_K=-N_{K'}\approx\pm\operatorname{sgn}(U/\gamma_\perp)$（±对应 AB/BA）[16,17]；③ 每谷每自旋沿畴壁 2 条手征模、不同谷反向传播 [17–21]；④ 费米能调进隙内 → 低能激发全由谷霍尔态三角网络承载 [22–26]。

**核心矛盾** 📜Q（引言）：微观计算给出 1D 手征 ZZ 模 [27,28]（Fleischmann 2020 [27]、Tsim-Nam-Koshino 2020 [28]）；但"current network theories [23] cannot reproduce these results"，且输运实验的干涉振荡与"去耦 1D 手征模" incompatible [29,30]（Rickhaus 2018 [29]、Xu 2019 [30]）。

**本文的切入** 📜Q："In contrast to previous network models [23], we take into account scattering at the nodes between the two channels"——两谷霍尔态沿链路不混（无无序），但到 AA 区（层间偏压诱导的局域隙消失）没理由保持去耦。且无前向散射的构造"impossible if the two valley Hall states are decoupled"（去耦时有前向散射下界 [23]）。

### 2.2 φ 调控的 ZZ ↔ pLL 两极限

每个散射节点 **6 进 6 出**（2 通道 × 3 方向，Fig. 1b）📜Q。对称性约束（Eq. 1）：
$$C_3:\ S=C_3SC_3^{-1},\qquad C_2\mathcal T:\ S=S^t$$
$C_3$ 对入射模做循环置换 $(a_1,a'_1)\to(a_2,a'_2)\to(a_3,a'_3)\to(a_1,a'_1)$（出射同理）；$C_2$ 同时交换 A/B 子晶格与谷 📜Q。

**无前向散射时**，S 矩阵在幺正变换等价意义下由单参数 $\phi\in[0,\pi/2]$（120° intrachannel 偏转相位）决定（Eq. 2）📜Q：
$$S=\frac12\begin{pmatrix}S_{\phi,\phi}&S_{0,\pi}\\S_{\pi,0}&-S_{-\phi,-\phi}\end{pmatrix},\quad S_{\vartheta,\psi}=\begin{pmatrix}0&e^{i\vartheta}&e^{i\psi}\\e^{i\psi}&0&e^{i\vartheta}\\e^{i\vartheta}&e^{i\psi}&0\end{pmatrix}$$
$\phi$ 被作者明确处理为**唯象参数**（"which we treat as a phenomenological parameter" 📜Q）。

**两极限** 📜Q（正文+Fig. 1c/d）：
- $\phi=0$ → 只保留 interchannel 偏转，$a_+$ 逆时针、$a_-$ 顺时针 → **3 条独立手征 ZZ 链**，速度 $v/2$，线性色散 $E_{j,n}(k)=\frac{\hbar v}{2l}(2\pi n+k_j)$，$n\in\mathbb Z$（Eq. 3），能量周期 $\pi\hbar v/l$ 📜Q。
- $\phi=\pi/2$ → 只保留 intrachannel 偏转，$a_+$ 逆时针绕 BA 畴、$a_-$ 顺时针绕 AB 畴 → 局域化 → **每周期 $2\pi\hbar v/l$ 内 3 条双重简并平带** = pLL 📜Q。⚠️ 旧 review 误写"三重简并平带"，原文是"three doubly degenerate flatbands"（已更正）。

> 幺正变换（对称/反对称基）📜Q：$U=e^{-i\pi\sigma_y/4}e^{i\phi\sigma_z/2}\otimes\mathbb 1_3$，新基 $a_\pm=(a\,e^{i\phi/2}\mp a'\,e^{-i\phi/2})/\sqrt2$（出射同理）。这是把"两谷霍尔通道"旋转为"同一链路上的对称/反对称叠加"，使 $\phi$ 的物理（偏转 vs 前向的分配）显式化。

### 2.3 前向散射：平行 vs 交叉耦合（两个输运区间）

加入 intra/interchannel 前向散射（概率 $P_{f1},P_{f2}$），偏转取同一 $P_d$；流守恒 $4P_d+P_f=1$，$P_f=P_{f1}+P_{f2}$ 📜Q。新基下 S 矩阵（Eq. 4）：
$$USU^\dagger=\begin{pmatrix}S_1&S_2^\dagger\\S_2&-S_1^\dagger\end{pmatrix},\quad S_1=2i\sqrt{P_d}\sin\phi\,s_0+f\cos\phi\,\mathbb1_3,\quad S_2=2\sqrt{P_d}\cos\phi\,s_0+if\sin\phi\,\mathbb1_3,\quad f=\sqrt{P_{f2}}+i\sqrt{P_{f1}}$$
$[s_0]_{nm}=\delta_{n1}\delta_{3m}+\delta_{n2}\delta_{1m}+\delta_{n3}\delta_{2m}$；$S_1(S_2)$ = 新基下的 intrachannel(interchannel) 过程 $a_+\to b_+(b_-)$ 📜Q。

**两个耦合机制 → 两个输运区间** 📜Q（正文+Fig. 2）：
- **平行 ZZ 耦合（准 1D）**：$\phi=0$ 时仅 $S_1$ 通过 intrachannel 前向散射耦合**平行** ZZ 链，概率 $|f|^2=P_f$；网络解耦为 3 套独立准 1D 系统（Fig. 2a）。
- **交叉 ZZ 耦合（2D）**：一般 $\phi\neq0$ 时，不同方向 ZZ 链经**两个过程**耦合（Fig. 2d）：interchannel 前向散射（概率 $P_f\sin^2\phi$）+ counterclockwise(clockwise) intrachannel 偏转（概率 $4P_d\sin^2\phi$）→ 能带反交叉（Fig. 2e,f）→ 真 2D 逾渗系统。

> ⚠️ **旧 review 关键修正**：原文**并未**把 $P_{f1}$ 对应"平行耦合"、$P_{f2}$ 对应"交叉耦合"。$P_{f1}$（intrachannel 前向）与 $P_{f2}$（interchannel 前向）只经 $f=\sqrt{P_{f2}}+i\sqrt{P_{f1}}$ 进入，输运只依赖总量 $P_f=P_{f1}+P_{f2}$（Fig. 2b/2e/Fig. 5 均只出现 $P_f$ 组合）。**控制 AB vs SdH 的是 $\phi$（决定准 1D 还是 2D 区间），不是 $P_{f1}$ vs $P_{f2}$ 的拆分**（正文：两区间"characterized by the effective dimensionality" 📜Q）。

### 2.4 磁输运：AB vs SdH

磁场 $B=Be_z$ 垂直网络；设 B 足够小使 S 矩阵结构不变，只经 Peierls 相位进入（Landau 规范 $A=Bx\,e_y$；水平链路相位 0，上/下斜链路 $\Phi_\pm(m)=\mp\pi(m+1/2)\Phi/\Phi_0$）📜Q。$\Phi_0=h/e$，$\Phi=BA$ 为穿 moiré 单胞（含一 AB 一 BA 三角）的磁通，$A=\sqrt3\,l^2/2$ 📜Q。

零温零偏微分电导（Landauer-Büttiker，$G/G_0=N_iT$，$N_i=4W/(\sqrt3\,l)$，$G_0=4e^2/h$，Eq. 5）📜Q；透射 $T$ 用连接左右 lead 的转移矩阵算（两谷在 $W\gg L$ 极限下相同）📜Q。

- **准 1D 区间（φ=0）→ AB 振荡**：$l_3$ 分支（手征、全透射）给常数平台背景；前向散射开启后 $l_{1,2}$ 分支反向传播模贡献干涉 → AB 共振 📜Q。解析式（Eq. 6）$G/G_0\simeq(2+2P_f^{2L/l+1}[1+P_f(4P_d)^2F_L(\Phi)^2])W/(\sqrt3 l)$，$F_L(\Phi)=\sin[\pi(2L/l-1)\Phi/\Phi_0]/\sin(\pi\Phi/\Phi_0)$，峰宽 $\Delta\Phi=2\Phi_0/(2L/l-1)$；共振在 $\Phi=\Phi_0/n$（$n$ 非零整数，路径环绕 $n$ 倍 moiré 单胞）📜Q。**能量无关**（干涉路径等长、动力学相位抵消）→ **AB 共振温度稳健** 📜Q。
- **2D 区间（φ≠0）→ AB + SdH**：不同方向 ZZ 耦合 → SdH 振荡（"network Landau levels"，Fig. 5）；磁通周期性因加入单 AB/BA 三角路径而**加倍** 📜Q。有限温度下 SdH 被抹平，AB 主导 📜Q。

---

## 3. 理论模型与方法

### 3.1 对称性约束的 S 矩阵
$C_3$（$\pi/3$ 旋转，交换子晶格与谷）+ $C_2\mathcal T$（spinless 时间反演）是保谷对称性（小扭角下与扭心无关 [37,38]），给出 Eq. 1；无前向散射时压缩到单参数 $\phi\in[0,\pi/2]$（Eq. 2）📜Q。6 进 6 出 S 矩阵的对称性约束推导细节在 SI[39]。

### 3.2 Bloch 定理 + 网络能带
节点入射模与邻节点出射模以动力学相位 $\lambda=e^{iEl/\hbar v}$ 关联；Bloch 定理给出 $(a,a')^t=\lambda[1_2\otimes M(k)]S(a,a')^t$，$M(k)=\operatorname{diag}(e^{ik_3},e^{ik_1},e^{ik_2})$，$k_j=k\cdot l_j$，$l_3=-(l_1+l_2)$；能带 = $[1_2\otimes M(k)]S$ 本征值的相位 📜Q（引用 [23,41] 的约定）。⚠️ 旧 review 的"$\det[\mathbb1-\lambda M(k)S]=0$"是本征值条件的等价写法 [推导]。

### 3.3 幺正变换到对称/反对称基
$U=e^{-i\pi\sigma_y/4}e^{i\phi\sigma_z/2}\otimes\mathbb1_3$，$a_\pm=(a e^{i\phi/2}\mp a'e^{-i\phi/2})/\sqrt2$ 📜Q。变换后 S 矩阵分块为 $S_1$（intrachannel）/ $S_2$（interchannel），物理显式化（见 §2.3）。

### 3.4 磁输运计算
Landauer-Büttiker 零温零偏电导 + Peierls 相位（Landau 规范）+ 转移矩阵 📜Q。非常规步骤一行：磁电导 $G(\Phi)$ 由 Eq. 5/6 给出，温度依赖经 Fig. 5（$T/T_l$ 扫 0, 0.005, 0.01）定性展示（未见有限温解析式）。通道计数 $N_i=4W/(\sqrt3 l)$ 见 [PHY-LB]。

---

## 4. 关键预言与数据（提取链 + 验证链 + 不确定度标注）

> 本文是理论：下面"数据"= 文中给出的解析式与 Fig. 参数，均为作者模型预言，**不是实验测量**。数值多为 [~]（无误差棒）。

| 量 | 值 / 表达式 | 出处 | 分级 |
|----|-------------|------|------|
| 网络单参数 | $\phi\in[0,\pi/2]$ | 正文 Eq. 2 后 📜Q | [~] |
| ZZ 色散（φ=0） | $E_{j,n}(k)=\hbar v(2\pi n+k_j)/(2l)$，$n\in\mathbb Z$ | Eq. 3 📜Q | [~] |
| ZZ 能量周期 | $\pi\hbar v/l$ | 正文 📜Q | [~] |
| ZZ 速度 | $v/2$ | 正文 📜Q | [~] |
| pLL（φ=π/2） | 3 条双重简并平带 / 周期 $2\pi\hbar v/l$ | 正文 📜Q | [~] |
| 流守恒 | $4P_d+P_f=1$，$P_f=P_{f1}+P_{f2}$ | 正文 📜Q | [~] |
| 前向散射系数 | $f=\sqrt{P_{f2}}+i\sqrt{P_{f1}}$ | Eq. 4 📜Q | [~] |
| moiré 单胞面积 | $A=\sqrt3\,l^2/2$ | Fig. 3 caption 📜Q | [~] |
| 通道数 | $N_i=4W/(\sqrt3\,l)$；$G_0=4e^2/h$ | Eq. 5 📜Q | [~] |
| 磁电导（准 1D） | Eq. 6（含 $P_f,P_d,F_L(\Phi)$） | 正文 📜Q | [~] |
| AB 峰宽 | $\Delta\Phi=2\Phi_0/(2L/l-1)$ | 正文 📜Q | [~] |
| AB 共振条件 | $\Phi=\Phi_0/n$（$n$ 非零整数） | 正文 📜Q | [~] |
| 实验平台参考 | $h/8e^2\approx3.2$ kΩ（Ref[30] 平台） | 正文 📜Q | [~] |
| 温度标度 | $T_l=2\pi\hbar v/k_Bl\approx3400\,(\theta°)$ K | Fig. 5 caption 📜Q | [~] |
| 碳原子数 | moiré 单胞 $\sim10^4\,(\theta°)^{-2}$ | 引言 📜Q | [~] |

**Fig. 参数取值**（读自 caption，均为作者选取的演示值）📜Q [读图]：
- Fig. 2b：$\phi=0,\ P_{f1}=0,\ P_{f2}=0.04$（即 $P_f=0.04$）
- Fig. 2e/f：$\phi=0.2,\ P_{f1}=P_{f2}=0.02$（$P_f=0.04$）
- Fig. 3b：$L=10l,\ W\gg L$，扫 $\Phi=BA$
- Fig. 5：$\phi=0.2,\ P_{f1,2}=0.3,\ E_F=\pi\hbar v/6l$，扫 $T/T_l=0,\ 0.005,\ 0.01$

**验证链**（本文自洽性）：
- **色散极限互验**：φ=0（线性 $v/2$ ZZ 链）与 φ=π/2（平带 pLL）均由同一 Eq. 2 的 S 矩阵经幺正变换导出，两极限解析可控 📜Q[推导]。
- **AB 温度稳健的机制链**：准 1D 区间干涉路径等长 → 能量无关 → 温度稳健（这是**推导链**，非数值验证）📜Q[推导]。
- **与实验对标**：准 1D 区间的磁电导与 Ref[30] 磁阻"integer fractions of the main period + plateau slightly above $h/8e^2\approx3.2$ kΩ" 的定性特征一致 📜Q；但**主周期解读不同**（§7）。

> **不确定度总注**：本文无误差棒，全部数值 [~]（解析式/作者取值）或 [读图]（Fig. 参数）。$\phi$、$P_f$ 等是自由模型参数，非实测。

---

## 5. 主要结论

1. 无前向散射时，$C_3+C_2\mathcal T$ 对称性把谷霍尔态网络压缩为单参数 $\phi$，插值于 1D 手征 ZZ 模与赝朗道能级 pLL 之间 📜Q。
2. "our theory unifies these two phenomena, showing that both arise from the network"——ZZ 模与 pLL 是同一散射结构的两极限 📜Q（定性断言，停在唯象层）。
3. 平行 ZZ 耦合（准 1D）→ AB 振荡，能量无关、温度稳健；不同方向 ZZ 耦合（2D）→ SdH 振荡，有限温度抹平 📜Q。
4. 与 $\theta\sim0.1°$ 低场实验 "agree well"，"provide for the first time a transport theory for the topological network"（作者断言）📜Q。
5. 对 Ref[30]（Xu 2019）主周期给出重解释：准 1D 区间不允许单三角畴路径，主周期应对应 moiré 单胞 → 等价于把 Ref[30] 报告的扭角放大 $\sqrt2$ 倍 📜Q（→§7）。

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| $\phi$ 唯象 | "we treat as a phenomenological parameter"，未从微观模型（θ、U、弛豫）导出 | 📜Q |
| 无微观参数映射 | 未给出 θ、U → $\phi$、$v$ 的定量关系 | 💭I（本文未做） |
| 零温/弱场近似 | 磁电导在零温零偏；有限温度仅 Fig. 5 三条曲线定性 | 📜Q |
| disorder 仅定性 | 扭角/电荷密度涨落展宽 AB 共振（SI[39] 提及，未给定量） | 📜Q |
| intervalley 散射忽略 | 声明 moiré 缓变故忽略，未证其对结果安全 | 📜Q |
| 前向散射简化 | 取同一 $P_d$；"different deflection probabilities … do not change our results qualitatively" | 📜Q |
| 未做数值微观对照 | 与微观计算（ZZ 模 [27,28]）只定性一致，未做定量能谱对照 | 💭I |

## 7. 与其他工作的关系（跨论文对标，核实自本文引用列表）

| 工作 | 关系（本文视角） |
|------|-----------------|
| Efimkin & MacDonald 2018 ([23]) | "current network theories"——本文超越之：其假设 AA 节点双通道去耦，无法复现 ZZ 模；去耦时前向散射有下界 📜Q |
| Ramires & Lado 2018 ([24]) | pseudo-Landau levels 的来源（φ=π/2 极限对应 pLL[24]）📜Q |
| Fleischmann 2020 ([27]) / Tsim-Nam-Koshino 2020 ([28]) | ZZ 模来自微观计算；本文 φ=0 极限给出其散射理论框架 📜Q |
| Rickhaus 2018 ([29]) | 输运干涉振荡实验，与"去耦 1D 手征模" incompatible（本文动机之一）📜Q |
| **Xu 2019 ([30])** | AB 振荡实验；本文准 1D 区间磁电导与其定性特征一致，但**重解释主周期**（moiré 单胞 vs 单三角畴 → 扭角 ×$\sqrt2$）📜Q |

> ⚠️ **引用列表核对结论**：Rickhaus **确为 [29]**（Nano Lett. 18, 6725 (2018)）、Xu **确为 [30]**（Nat. Commun. 10, 4008 (2019)），两者均在本文参考文献列表 ✅。cards.md 的"直接解释 Xu 2019 巨幅 AB 振荡"是**卡片级综合 💭I⚠️**：原文是"exhibit the same qualitative features" + 主周期重解释，措辞强度低于"直接解释"。⚠️ 旧 review 的"De Beule/Dominguez/Recher 2021 (T18) Floquet 有效模型"**非本文内容**（本文 2020，未自引 T18），已降级为外部对标（未保留在正文）。

## 8. 对后续研究的影响

- 为 mTBG 谷霍尔态网络提供**首个输运理论**（作者自述），把 AB 与 SdH 振荡统一到同一散射框架 📜Q。
- 给出可实验甄别预言：平行耦合→温度稳健 AB；交叉耦合→温度敏感 SdH → 可作为 $\phi$ 取值（准 1D 还是 2D）的判据 💭I。
- 留下明确缺口：$\phi$ 的微观导出（θ、U、弛豫依赖）——是本文未闭合的唯象参数 📜Q→💭I。

## 9. 理论模型映射（供 TBPM/Kubo-Bastin 对标）

| 映射 | 说明 |
|------|------|
| $\theta\to l=a/[2\sin(\theta/2)]\to A=\sqrt3\,l^2/2$ | 扭角→moiré 晶格常数→网络单胞面积 📜Q |
| $\phi$（唯象）→ S 矩阵 | 可由 TBPM/紧束缚微观散射反推（本文未做，是开放任务）💭I |
| $B\to$ Peierls 相位 | $\Phi_\pm(m)=\mp\pi(m+1/2)\Phi/\Phi_0$（Landau 规范）📜Q |
| $E\to$ 动力学相位 | $\lambda=e^{iEl/\hbar v}$ 📜Q |
| 通道数 → 电导 | $N_i=4W/(\sqrt3 l)$，$G_0=4e^2/h$ 📜Q |
| 观测量 | $G(\Phi)/G_0$（器件量）；AB/SdH 振荡 |

> 与 TBPM/Kubo 对应：本文算的是**有限网络条带**的 Landauer 电导 $G(\Phi)$（转移矩阵），非 bulk $\sigma_{xx}$；复现需有限尺寸网络散射/转移矩阵计算，bulk Kubo 只给背景（同 E12 §9 注记）💭I。

---

## Phase S 目的接口（三问引用式）

- **Q1（edge state 如何表征）**：本文不直接表征，而是给**网络输运的散射模型**——AA 节点双通道 S 矩阵（6 进 6 出）+ 对称性约束 → 单参数 φ；φ=0 ↔ 1D 手征 ZZ 模、φ=π/2 ↔ pLL（见 §2.2）。
- **Q2（理论如何解释）**：核心 = 网络散射统一理论：无前向散射单参数 φ 插值 ZZ↔pLL；前向散射下平行耦合→AB（稳健）、交叉耦合→SdH（抹平）（见 §2.3/§2.4）📜Q。
- **Q3（理论↔实验对应）**：AB 振荡 ↔ 平行 ZZ 耦合（准 1D，φ=0）；SdH ↔ 交叉 ZZ 耦合（2D）；主周期 ↔ moiré 单胞（非单三角畴）→ 对 Xu 2019 扭角 ×$\sqrt2$ 重解释（见 §2.4/§7）📜Q。

> **增量价值**：这是 Q2 理论 8 篇里唯一给出**AA 节点散射的对称性约束解**（C3+C2T → 单参数 φ）并**统一 ZZ 模与 pLL**的论文；为"网络 vs TZM 之争"提供中间地带方案（散射相位连续插值）。比 TZM[28]/网络[23] 多的是"节点耦合"这一步，少的是"微观参数（θ、U）→φ"的定量映射。

## 反向核对 pass (2026-09-02)

`pdftotext -layout` 提取正文（6 页）+ 补充 `pdftotext -raw` 逐项 grep 核对：全部数字/符号（φ∈[0,π/2]、6 进 6 出、$l=a/[2\sin(\theta/2)]$、$N_K=-N_{K'}\approx\pm\operatorname{sgn}(U/\gamma_\perp)$、Eq. 1–6、$E_{j,n}(k)$、$v/2$、$\pi\hbar v/l$、$2\pi\hbar v/l$、3 条双重简并平带、$4P_d+P_f=1$、$f=\sqrt{P_{f2}}+i\sqrt{P_{f1}}$、$P_f\sin^2\phi$、$4P_d\sin^2\phi$、$\Phi_0=h/e$、$G_0=4e^2/h$、$N_i=4W/(\sqrt3 l)$、$h/8e^2\approx3.2$ kΩ、$T_l\approx3400(\theta°)$ K、$10^4(\theta°)^{-2}$、Fig. 参数 0.04/0.02/0.2/0.3/10l/0.005/0.01/$\pi\hbar v/6l$、$2L,2L+3l$、$\Delta\Phi=2\Phi_0/(2L/l-1)$、$\Phi=\Phi_0/n$）均在原文找到。

⚠️ **关键发现与降级**：
1. **pdftotext（默认/-layout）丢失部首符号 √**：`A=3l²/2`、`4W/3l`、`factor 2`、`a±=(...)/2`、`f=√Pf2+i√Pf1` 等处的 √3/√2 被吞。已用 `pdftotext -raw` 重提确认：$l_{1,2}=l(-1/2,\pm\sqrt3/2)$、$A=\sqrt3\,l^2/2$、$N_i=4W/(\sqrt3\,l)$、$a_\pm=(\dots)/\sqrt2$、$f=\sqrt{P_{f2}}+i\sqrt{P_{f1}}$、"factor $\sqrt2$"。此为本文件所有 √ 系数的来源依据。
2. **修正**「$P_{f1}$↔平行 / $P_{f2}$↔交叉」映射：原文无此对应，$P_{f1},P_{f2}$ 只经 $f=\sqrt{P_{f2}}+i\sqrt{P_{f1}}$（总 $P_f$）进入；控制 AB vs SdH 的是 $\phi$（§2.3）。
3. **修正**「φ=π/2 → 三重简并平带」→「3 条双重简并平带（每周期 $2\pi\hbar v/l$）」（§2.2）。
4. **删除**「Efimkin-MacDonald 网络态对应中间 φ」：无源；Efimkin-MacDonald[23] 是去耦网络模型（被超越），pLL 对应 Ramires-Lado[24]。
5. **删除**「Tsim & Koshino 发现 ZZ 模不形成连通网络」：本文未出现，原文只说 ZZ 模来自微观计算 [27,28]。
6. **删除/降级**「直接解释 Xu 2019 巨幅 AB 振荡」→「qualitative features 一致 + 主周期重解释（扭角×√2）」（§7）。
7. **删除**「De Beule 2021 (T18) Floquet 有效模型」：非本文内容。
8. **引用列表核实**：Rickhaus [29] ✅、Xu [30] ✅（均在列表）。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-06 | research_onboarding Phase 4 初读（旧 8 节格式 + Phase S Q2/Q3 补充） |
| 2026-09-02 | **4 块辨识结构整体重写**：对齐 E12 结构（TL;DR 问题句式 + 四层变量表 + 可辨识性判别表[理论版] + 三段结果 + 理论模型与方法 + 关键预言/数据 + 三问接口 + 反向核对 + 更正日志） |
| 2026-09-02 | **修正「Pf1↔平行/Pf2↔交叉」映射**：原文无此对应，$P_{f1},P_{f2}$ 只经 $f=\sqrt{P_{f2}}+i\sqrt{P_{f1}}$ 进入；控制 AB vs SdH 的是 φ（准 1D vs 2D 区间） |
| 2026-09-02 | **修正「三重简并平带」→「3 条双重简并平带」**（φ=π/2，每周期 $2\pi\hbar v/l$）；**删除**「Efimkin-MacDonald 网络态对应中间 φ」（pLL 对应 Ramires-Lado[24]） |
| 2026-09-02 | **删除无源/跨论文项**：「Tsim & Koshino 发现 ZZ 模不形成连通网络」、「De Beule 2021 (T18) Floquet」；**降级**「直接解释 Xu 2019」→「qualitative features 一致 + 主周期重解释（扭角×√2）」 |
| 2026-09-02 | **QC 记录 pdftotext 部首符号 √ 丢失**：用 `-raw` 重提逐式核对（$A=\sqrt3 l^2/2$、$N_i=4W/(\sqrt3 l)$、$a_\pm/\sqrt2$、$f=\sqrt{P_{f2}}+i\sqrt{P_{f1}}$、"factor √2"）；**核实引用列表**：Rickhaus [29] ✅、Xu [30] ✅ |
