<!--
 * @Author       : AI 精读 (系统辨识式阅读法 → 三层分离整理)
 * @Date         : 2026-08-06（初读）→ 2026-09-01（按 4 块新架构重读）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T12_tsim2020_prb.md
 * @Description  : T12: Tsim, Nam & Koshino (2020) PRB — 偏置 mTBG 的完美 1D 手征态（TZM 推翻网络图景；4 块辨识结构）
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
| **课题组** | Koshino（Osaka Univ.）+ Nam（AIST Sendai）+ Tsim（Manchester）📜Q |
| **PDF / SI PDF** | ✅ reference/pdfs/Tsim 等 - 2020 - Perfect one-dimensional chiral states in biased twisted bilayer graphene.pdf（无 SI） |
| **精读日期** | 2026-08-06（初读）→ 2026-09-01（按 4 块新架构重读） |

> **共享知识引用**：通用物理（valley Chern / chiral vs helical、网络 miniband、Landauer-Büttiker 通道计数）已剥离到 `note/shared/physics/`，本 review 用锚点 `[PHY-BERRY] [PHY-MB] [PHY-LB]` 引用，不重复讲义。阅读疑问见 `note/shared/method/mechanism_questions.md` `[METHOD-Q]`。

---

## TL;DR

**本文想解决的问题**：小角 TBG 在强层间偏置下，AB/BA 畴壁上已知的拓扑通道究竟**形成 2D 渗流网络**（Efimkin-MacDonald 网络模型，入射模在节点分裂为多个出射模），还是**组成独立的 1D 链**？

**主结果**：① 拓扑通道**不形成渗流网络**，而是自组织为**三组独立的完美 1D 本征模**（topological zigzag mode, TZM），沿三个方向独立传播、从不杂化 📜Q（摘要）；② AA 节点散射是**置换型（确定性）**的——mode 1 恒散射到 mode 2（−120°），mode 2 恒散射到 mode 1（+120°）→ 三组独立 zigzag 模，无分束不杂化 📜Q（Sec. III）；③ 偏置产生**两个稀疏 1D 能量窗口**，被电荷中性点附近的**近扁平带簇**隔开 📜Q（Sec. II）。

**结论/意义**：这是网络模型的 **special case**——每个顶点散射矩阵唯一连接特定出入模；作者措辞 "do not actually form a percolating network, but instead … provide independent, perfect one-dimensional eigenmodes" 📜Q（摘要，理论演示非实验证明）。

---

## 1. 系统辨识导览（判别表为全文唯一权威）

**黑箱三要素**：`{输入旋钮 θ, Δ, u, E_F | 输出观测量 能带 E(k)、费米面拓扑、波函数空间分布、载流子密度 n_W | 声称结论 三组独立完美 1D 手征 zigzag 模，不形成渗流网络}`

**四层变量图**（符号层一次钉死）：

| 层 | 本文实例 |
|----|----------|
| **L1 旋钮 u** | $\theta$（扭角 1°→0.2°）、$\Delta$（层间偏置，±Δ/2，至 400 meV）、$u$（层间耦合，Fig. 5 从 0 增至真实值）、$E_F$（费米能，50/20 meV 截面） |
| **L2 导出量 x₁** | $\Delta K=\lvert\Delta K_j\rvert=4\pi\theta/(3a)$（moiré 动量偏移）、窗口宽度 $\sim u$、最大交叉能量 $\hbar v\Delta K/2$、$n_W=g_v g_s\,\Delta K/(4\pi\hbar v)$ |
| **L3 模型量 x₂** | $S$ 矩阵（置换型）、能带结构、DoS $D(E)$、费米面（开/闭）、态数 $2n_W$ |
| **固定参数（非旋钮）** | $a=2.46$ Å、$\hbar\upsilon/a=2.1354$ eV、$u=0.103$ eV（材料真实值）、$V_{pp\pi}^0\approx-2.7$ eV、$V_{pp\sigma}^0\approx0.48$ eV、$d_0\approx0.334$ nm、$a_0=a/\sqrt3\approx0.142$ nm、$r_0=0.184a$ |
| **反推量 θ̂** | 无（纯理论：全部量由旋钮直接计算，无从实验反推）——$n_W$ 是"到达 1D 窗口的预言载流子密度"（预测非反推）📜Q |
| **L4 观测量 y** | 能带 $E(k)$（三交叉平面、近直费米线）、波函数空间分布（1D 局域、绕过 AA）、1D 通道数→电导、AB 振荡有无（预言） |

**可辨识性判别表**（唯一权威；理论论文 = 区分竞争图景/竞争模型，每条判别 = 判据 / 排除谁 / 确立谁）：

| 判别 | 判据（计算/论证） | 排除谁 | 确立谁 |
|------|------------------|--------|--------|
| **节点散射类型** | 波函数空间检验（Fig. 4 + 正文）：AA 顶点 mode 1 恒散射到 mode 2（−120°）、mode 2 恒散射到 mode 1（+120°）📜Q（Sec. III） | 渗流网络模型（"入射模一般分裂为两个或更多出射模" 📜Q，引言） | 置换型散射 → 三组独立 zigzag 模（网络模型的 special case）📜Q |
| **方向间是否杂化** | 能带由**三个互不杂化**的交叉平面组成、近直费米线（Fig. 2c/d）📜Q；k 空间矩阵元在六区 I–VI 边界近零 → 六区近解耦（Fig. 7 + pseudospin matching）📜Q | 2D 网络（不同方向通道在节点杂化） | 三方向 1D 模独立、完美 1D 通道 |
| **能谱结构** | 偏置产生两个**仅稀疏分布** 1D 模的能量窗口，被 CNP 附近**近扁平带簇**隔开（Fig. 2a）📜Q | 网络 miniband 连续填充谱 | TZM 稀疏 1D 谱 |
| **结构稳健性** | TB + 晶格弛豫下窗口与 TZM **仍存在**、波函数**更局域**于 AB-BA 边界（Fig. 3、Fig. 4）📜Q | 理想化刚性格子伪影 | TZM 是偏置 TBG 的 robust 特征 |

> **主结果 ↔ 判别表映射**：
> - 主结果① 三组独立完美 1D 手征 zigzag 模（TZM）← {节点散射类型, 方向间是否杂化}
> - 主结果② 两个稀疏 1D 能量窗口（被近扁平带簇隔开）← {能谱结构}
> - 主结果③ TZM 对晶格弛豫 robust ← {结构稳健性}
> - 主结果④ 起源（两带模型 open Fermi surface）← {方向间是否杂化（k 空间解耦）, 能谱结构}
>
> **分层排除注**（理论论文的模型判别链，非实验"存在性→相干→拓扑"分层）：① 节点散射矩阵形式（置换 vs 满矩阵）→ ② 方向间是否杂化（1D vs 2D）→ ③ 能谱（稀疏窗口 vs miniband 连续填充）。作者用对比式措辞 "do not actually form … but instead provide …"（摘要），是**理论演示**而非"证明"；末尾 "we found that these states never hybridize"（结论）📜Q。

> **[前提与限定]**（判别结论的适用范围）：
> - **近似/假设**：单粒子（无相互作用，未计算有限温/无序输运）💭I；Sec. II 连续模型假设刚性层，弛豫仅在 Sec. III 由 TB 引入 📜Q。
> - **判别性扫轴（旋钮范围）**：扫 $\theta$（1°, 0.5°, 0.3°, 0.2°）、扫 $\Delta$（至 400 meV）、扫 $u$（Fig. 5 从 0 到真实值）；截面 $E_F=50/20$ meV 📜Q。
> - **候选集 M 边界**：{渗流网络模型（Efimkin-MacDonald 2018）, 独立 1D 链（TZM）} —— 本文论证 TZM 在该集合内唯一幸存；**集外候选（相互作用关联态、有限温/强无序输运）原文未讨论、未排除** 💭I（封闭世界假设风险）。

三层标注：📜Q = 原文事实（附位置）｜推导 = 由原文公式合成｜📊F = 读图估算｜💭I = 推断。**不确定度（正交轴）**：[±] 原文误差棒 / [~] 原文以 =/≈ 给出但无误差棒 / [读图] 图提取 / [相对] 仅相对量。所有数字经 pdftotext + grep 反向核对。

---

## 2. 结果与机制（按论文论证结构：网络→散射→能谱→起源→弛豫）

### 2.1 从渗流网络到独立 1D 模（散射矩阵置换型）

网络图景的前提 📜Q（引言）：偏置使 AB/BA 畴区局域开隙，每条 AB-BA 边界出现**每条自旋-谷 sector 两条拓扑模**（mode 1, 2）；AB 与 BA 区单谷 Hall 电导分别为 $+e^2/h$ 与 $-e^2/h$，差 $2e^2/h$ → 每条边界每自旋每谷两条边界模 📜Q；K 与 K′ 两条模传播方向相反 📜Q。

本文核心修正 📜Q（引言 + Sec. III）：网络模型中入射模一般分裂为多个出射模；但本文发现偏置 TBG 的拓扑模**不形成 2D 网络**，而是"拓扑通道段的**串联**"（serial connection）组成的独立 1D 本征模。这是网络模型的 **special case**——每个顶点散射矩阵**唯一连接特定出入模**。

**置换型散射的判定**（波函数检验，Fig. 4 + 正文）📜Q（Sec. III）：在三角网格的每个顶点（AA 区），"mode 1 is always scattered to mode 2 in the −120° direction, while mode 2 is always scattered to mode 1 in the +120° direction" → "we have three independent zigzag traveling modes"。即 $S$ 矩阵是**置换型**（$S_{12}=S_{21}=1$ 型排列，非对角、非满矩阵），三方向模无分束、不杂化。

> ⚠️ **修正（沿袭 2026-08-20 S-REV）**：旧版写 "S 矩阵是对角的"——原文并非对角矩阵，而是**置换型**确定性散射。原句见上（grep "120" ✓，/tmp/T12.txt 行 217–219）。依据 `Phase_S/appendix_B_theory.md` §B.5 #13 + `cards.md` T12。

### 2.2 两个 1D 能量窗口 + 近扁平带簇

偏置产生**两个 well-defined 能量窗口**，各含**稀疏分布**的完美 1D 本征模，被**电荷中性点附近的近扁平带簇**隔开 📜Q（摘要 + Sec. II）。窗口大小**不强烈依赖 Δ**（θ=0.2° 增大 Δ 时仍见）📜Q；窗口宽度是 $u$ 量级（"obviously the order of u"）📜Q（Sec. IV）。大偏置下（Δ=400 meV）窗口上部出现平台型**赝朗道能级**（如 θ=0.3° 时 50 meV < |E| < 100 meV 的三条水平线，解释为赝规范场赝朗道能级）📜Q（Sec. II）。

### 2.3 TZM 几何：绕过 AA 而非穿过

波函数取 1D 形式沿畴壁方向延伸、垂直方向不连通 📜Q（Fig. 4）；电子侧波幅主要集中于 layer 1、空穴侧集中于 layer 2 📜Q。弛豫下波函数**更局域**于 AB-BA 边界（AB/BA 畴区扩宽、波幅被限制在窄边界）📜Q。TZM 沿 AB/BA 畴壁传播、在 AA 点**绕过而非穿过**（zigzag 链）——三方向模彼此独立、从不交叉杂化 💭I（据 Fig. 1b + 正文散射描述）。

### 2.4 起源：弱耦合极限 + 两带模型

**弱耦合极限（u→0）**：电子侧与空穴侧各开一隙（two gaps），随 u 增至真实值成为两个窗口；1D 本征模**始终留在隙内**，阻止谱完全打开 📜Q（Fig. 5 + Sec. IV）。**两带模型**：大 Δ 下低能区由 layer 1 空穴带 + layer 2 电子带主导，两反向锥在动量空间以相对位移 $\Delta K_j$（j=0,1,2）相交，交叉处**anticrossing 开隙** 📜Q（Fig. 6a + Sec. IV）。隙大小 ∝ 交叉线上 $U$ 矩阵元 $\langle k+\Delta K_j, +|U|k, -\rangle \approx iu\,\sin[\theta(k)-2\pi j/3]$ 📜Q（Eq. 11）。

**费米面重构**：u=0 时三个开费米面（120° 相隔）+ 三个闭 pocket；u 增大后闭 pocket 因电子-空穴**良好 nesting** 被开隙、开费米面**保持无隙** → 解释 1D 模填充隙的起源 📜Q（Fig. 6c–e）。**大 u 下仍解耦**：k 空间矩阵元图（Fig. 7）显示六区 I–VI 在边界处矩阵元近零（pseudospin matching：单层本征态在 x 方向的 pseudospin (1,1) 与 (1,−1) 是 $U$ 的 $j=0$ 分量本征矢 → 不杂化）→ 六区近解耦，三方向 1D 模在大 u 下仍独立 📜Q。**纳米带类比**：偏置 TBG 的完美 1D 模是 zigzag 石墨烯纳米带"完美导电通道"的 2D 版本（每谷 $n$ 右行 + $n{+}1$ 左行模，另一谷 $n{+}1$ 右行 + $n$ 左行模；过量行模即使无序也是完美导电通道，只要杂质长程且不混谷）📜Q（Sec. IV）。

**载流子密度 n_W** 📜Q（Sec. IV）：两隙夹持的每面积态数 = $2n_W$，其中 $n_W=g_v g_s\,\Delta K/(4\pi\hbar v)$（Eq. 12），来自 $D(E)=g_v g_s\,\Delta/(2\pi\hbar^2 v^2)$（$|E|<\Delta/2$）× 最大交叉能量 $\hbar v\Delta K/2$。$\theta=0.3°$、$\Delta=200$ meV 时 $n_W=1.08\times10^{12}\,\mathrm{cm^{-2}}$ 📜Q[~]——刻画"到达 1D 窗口的典型载流子密度"。

### 2.5 晶格弛豫：TZM 稳健

TB + Slater-Koster 晶格弛豫（AB/BA 畴扩宽）下：非弛豫 TB 与连续模型**定量一致**；弛豫后**定性特征不变**（窗口 + 完美 1D 模仍存在）；主要差别是中央赝朗道能级与 1D 模**完全杂化**、并入色散带，零能簇变得**更分散** 📜Q（Fig. 3 + Sec. III）。弛豫下波函数更局域于 AB-BA 边界（Fig. 4）📜Q。

---

## 3. 理论模型与方法

### 3.1 连续模型（Sec. II）
$$H_{\mathrm{TBG}}=\begin{pmatrix} H_1 & U^\dagger \\ U & H_2 \end{pmatrix},\qquad H_{1,2}=\begin{pmatrix} \mp\Delta/2 & -\upsilon\pi^\dagger \\ -\upsilon\pi & \mp\Delta/2 \end{pmatrix}$$
$H_{1,2}$ 为单层 Dirac 哈密顿量（含偏置 $\pm\Delta/2$，$\Delta$ = 垂直电场诱导的静电能移）📜Q；$\pi=\hbar(\xi k_x+ik_y)$，谷指标 $\xi=\pm1$ 区分 K/K′ 📜Q；$\upsilon$ 为单层石墨烯带速度，$\hbar\upsilon/a=2.1354$ eV、$a=2.46$ Å 📜Q[~]。$U$ 为 moiré 层间耦合（Eq. 3），强度 $u=0.103$ eV 📜Q[~]；$\Delta K_j$（Eq. 4）为两层原始布里渊区角位移，$|\Delta K_j|=4\pi\theta/(3a)$ 📜Q。谷间耦合在小角可忽略，K/K′ 独立计算 📜Q。

### 3.2 紧束缚 + 晶格弛豫（Sec. III）
$$H=-\sum_{i,j} t(R_i-R_j)|R_i\rangle\langle R_j|+\mathrm{H.c.}$$
Slater-Koster 型转移积分（Eq. 7–9）：$V_{pp\pi}^0\approx-2.7$ eV（最近邻层内）、$V_{pp\sigma}^0\approx0.48$ eV（垂直最近邻）、$d_0\approx0.334$ nm（层间距）、$a_0=a/\sqrt3\approx0.142$ nm、衰减长度 $r_0=0.184a$（使次近邻层内耦合 = $0.1 V_{pp\pi}^0$）、$d>3a$ 截断 📜Q[~]。弛豫原子位形取自先前工作（ref 50）📜Q。TB 中谷不区分 📜Q。

### 3.3 推导链（两带模型 + 计数）
窗口起源的两带模型与 $n_W$ 公式见 §2.4；$n_W=g_v g_s\,\Delta K/(4\pi\hbar v)$、$D(E)=g_v g_s\,\Delta/(2\pi\hbar^2 v^2)$ 为原文 Eq. 12 及正文原式 📜Q。剩余通道计数（每谷每自旋每方向 1 条 TZM → 总通道数）见 [PHY-LB]。

---

## 4. 关键预言与数据（提取链 + 验证链 + 不确定度标注）

### 4.1 模型参数（全文无误差棒，理论计算 → 全部 [~]）
| 参数 | 值 | 来源等级 |
|------|-----|---------|
| 层间耦合 u | 0.103 eV | 📜Q[~]（Sec. II） |
| ħυ/a | 2.1354 eV | 📜Q[~]（Sec. II） |
| 晶格常数 a | 2.46 Å | 📜Q[~]（Sec. II） |
| 扭角扫描 θ | 1°, 0.5°, 0.3°, 0.2° | 📜Q[~]（Fig. 2a） |
| 偏置 Δ | 至 400 meV；两带模型算例 200 meV | 📜Q[~]（Fig. 2/4/5/6） |
| 费米能截面 E_F | 50 meV（Fig. 2d）；20 meV（Fig. 6c/d） | 📜Q[~] |
| n_W（θ=0.3°, Δ=200 meV） | 1.08 × 10¹² cm⁻² | 📜Q[~]（Sec. IV） |
| 赝朗道能级区间 | 50 meV < |E| < 100 meV（θ=0.3°） | 📜Q[~]（Sec. II） |
| Vppπ⁰ / Vppσ⁰ / d₀ / a₀ / r₀ | ≈−2.7 eV / ≈0.48 eV / ≈0.334 nm / ≈0.142 nm / 0.184a | 📜Q[~]（Sec. III） |
| 波函数算例扭角 θ | 0.55°（Fig. 4） | 📜Q[~] |

### 4.2 预言（作者措辞，标 📜Q，非已验证事实）
- **完美 1D 模条件**：要求能量窗口 $(|E_F|\lesssim u)$ 由单层空穴带 + 另一层电子带主导 → 条件 $\Delta/2 \gtrsim u$，即 $\Delta \gtrsim 200$ meV 📜Q[~]（Sec. V/结论）。
- **无 AB 振荡**：作者 "we do not have the Aharonov-Bohm oscillation in magnetic fields because the 1D eigenmodes do not enclose triangular domains" 📜Q（结论）。
- **弹道输运主导**：散射可忽略且 $E_F$ 在窗口内时，输运由 1D 本征模的弹道输运主导 📜Q（Sec. V）。
- **无序预言**：不同 1D 模杂化仅由 AB-BA 边界上 mode 1/2 的局域混合或 AA 角的不规则反射引起；主要散射来自**短程无序**（小于 AB-BA 边界与 AA 点局域结构，约几纳米）；moiré 尺度畸变不引起强混合；无序散射详细研究**留待未来** 📜Q（Sec. V）。
- **实验对 AB 振荡的解释**：作者 "we expect that magnetic oscillations take place when the perfect 1D eigenmodes are not well formed, e.g., because the bias is not large enough or the Fermi energy is not in the corresponding region" 📜Q（Sec. V）——这是对已报道 AB 振荡实验（refs 34–36）的**预测性解释**，非已验证。

### 4.3 验证链（本文内部互验）
| 支柱 | 互验内容 | 数据 |
|------|---------|------|
| 连续 ↔ TB | 非弛豫 TB 能带与连续模型**定量一致** | Fig. 3 |
| 连续 ↔ 两带模型 | 两带模型解析复现窗口起源（开隙位置、1D 模填充隙） | Fig. 5, 6 |
| k 空间解耦 | Fig. 7 矩阵元图 ↔ Fig. 6(e) 开费米面 ↔ Fig. 4 波函数层分布一致 | Fig. 4, 6, 7 |
| 弛豫稳健 | 弛豫前后定性特征不变（窗口 + TZM 存在） | Fig. 3, 4 |

> 全文无 ± 误差棒（理论计算）；数字均为 📜Q[~]（原文以 =/≈ 给出）；无读图提取的必要数字（未做色标读数）。

---

## 5. 主要结论（作者措辞，📜Q）

1. 偏置 TBG 在零能两侧 well-defined 能量窗口内出现**完美 1D 本征模**（"show that TBGs with an applied bias exhibit perfect 1D eigenmodes"）📜Q。
2. 这些态**从不杂化**、沿三方向沿 AB/BA 畴壁**独立传播**（"these states never hybridize and they propagate independently in three different directions"）📜Q。
3. AA 节点置换型散射 → 三组独立 zigzag 模，是网络模型的 **special case**（"a special case of the network model where the scattering matrix at each vertex exclusively connects the specific incoming and outgoing modes"）📜Q。
4. 窗口形成与态起源由**两带模型**（单层石墨烯相交电子/空穴带）解释，1D 模对应 moiré 层间杂化形成的**涌现开费米面** 📜Q。
5. 任意晶格畸变下波函数**更局域**于畴壁，TZM 保持 📜Q。

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
| Fleischmann et al. 2020 (ref 19) | 完美 nesting 费米面——本文结果与之**一致**（"The result is consistent with a recent work which predicts the perfect nesting"）📜Q |
| Ramires & Lado 2018 (ref 17) | 赝朗道能级——本文 Fig. 2a 平台解释引用 📜Q（Sec. II） |
| San-Jose & Prada 2013 (ref 15) | 偏置下螺旋网络（前作图景）📜Q（引言） |
| Wakabayashi et al. 2007 (ref 56) | zigzag 纳米带完美导电通道——TZM 的 2D 类比 📜Q（Sec. IV） |
| Rickhaus 2018 (ref 34) / Yoo 2019 (ref 35) / Xu 2019 (ref 36) | 偏置小角 TBG 输运/STM 观察到的显著 AB 振荡——本文预测：TZM 完整形成时应**无 AB**，振荡出现在 TZM 未完整形成时 📜Q（Sec. V） |

> ⚠️ **Phase S 外部对标（非本文引用，时间倒挂）💭I**：T15（De Beule et al. 2020 PRL，散射统一理论）与 T29（Hou 2024，NQCP 裁决）是**后续**工作，分别提供"网络 vs TZM 中间地带"与"近量子化电导"裁决；本文 2020 年出版，引用列表无此二者。旧 review §5 的"De Beule 对称性支持 TZM 不连通""Hou 量子输运裁决确认 TZM 胜出"均为卡片级综合，降级 💭I⚠️。

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
| $\theta\to\Delta K=4\pi\theta/(3a)$ | 扭角→moiré 动量偏移→几何窗口（非 λ 直接）📜Q |
| $\Delta\to\pm\Delta/2$ | 层间偏置→两层 Dirac 能移（直接旋钮）📜Q |
| $u\to$ 窗口宽度 | 层间耦合→窗口宽度 $\sim u$ 📜Q |
| 通道数→电导平台 | 每谷每自旋每方向 1 条 TZM；Landauer-Büttiker 计数见 [PHY-LB]（推导） |
| $n_W=1.08\times10^{12}\,\mathrm{cm^{-2}}$ | 到达 1D 窗口的预言载流子密度（θ=0.3°, Δ=200 meV）📜Q |
| 1D 模不围三角畴→无 AB | 与 E12 的 AB 振荡判别对照（TZM 完整 vs 未完整）📜Q |

> 与 TBPM/Kubo 对应：能带 E(k)、费米面、波函数局域可经 TB 直接复现；电导平台需 Landauer/Fisher-Lee 透射计算（有限器件）；AB 振荡为有限尺寸相干效应，bulk σxx 只给背景 💭I。

---

## Phase S 目的接口（三问引用式 + 增量价值）

- **Q1（edge state 如何表征）**：理论表征 = 能带 E(k)（三交叉平面、近直费米线）+ 波函数空间局域（1D 沿畴壁、绕过 AA）+ 通道计数（每谷每自旋每方向 1 条）——详见 §2/§4。
- **Q2（理论如何解释）**：本文 = 推翻网络图景的 TZM 理论；AA 节点置换型散射（mode 1↔mode 2 @ ±120°）→ 三组独立 zigzag 模、无分束不杂化 📜Q——详见 §2.1。
- **Q3（理论↔实验对应）**：预言 TZM 完整形成时**无 AB 振荡**；已报道 AB 振荡（Rickhaus/Yoo/Xu）= TZM 未完整形成（偏置不足或 $E_F$ 不在窗口）📜Q——详见 §4.2/§8。

> **增量价值**：与 E12（实验，AB 振荡证实网络连通）形成**正面对照**——本文（理论）论证 TZM 完整时无 AB、E12 观察 AB = TZM 未完整形成的证据；对"网络 vs 独立 1D 链"的判别是本族笔记的核心概念裁决点。report.md 用其判别表（网络 vs TZM）+ §4 预言（无 AB 条件、Δ≳200 meV、n_W 换算）。

---

## 反向核对 pass (2026-09-01)

pdftotext 提取正文（/tmp/T12.txt，517 行），逐项 grep 核对：全部数字（u=0.103 eV / ħυ/a=2.1354 / a=2.46 Å / θ=1°,0.5°,0.3°,0.2° / Δ=400,200 meV / E_F=50,20 meV / n_W=1.08×10¹² / Vppπ⁰≈−2.7 / Vppσ⁰≈0.48 / d₀≈0.334 / a₀≈0.142 / r₀=0.184a / 50<|E|<100 meV / θ=0.55° / ±120° / Δ≳200 meV / |E_F|≲u / +e²/h,−e²/h,2e²/h / "a few nanometers"）均在原文命中。专名核对："three independent zigzag traveling modes"、"+120°/−120°"、pseudospin matching、regions I–VI、two-band model、serial connection、special case of the network 均命中。arXiv:2001.06257 正文未出现（仅 ref 21 的 arXiv:1904.12826），已标外部来源。

⚠️ 本次修订（相对旧版）：① S 矩阵"对角"→"置换型"（沿用 §B.5#13 修正，重核 grep "120" ✓）；② 旧 §5 的 De Beule/Hou 对标移入 §7 并降级 💭I（时间倒挂、非本文引用）；③ 旧 §2.1 "Rickhaus/Huang 似乎支持网络图景"→ 改为原文措辞 "network … experimentally probed by transport [34–36] and STM [37]"；④ 新增判别表（网络 vs TZM 四条）、四层变量表、[前提与限定]、§9 理论模型映射。

---

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-06 | 初读（research_onboarding Phase 4 风格）：连续模型 + TB + 弛豫 + 两带模型起源；S 矩阵误记为"对角" |
| 2026-08-20 (S-REV) | **§3.2/§8 "S 矩阵对角"修正**：改为置换型确定性散射——原文非对角矩阵，而是 "mode 1 is always scattered to mode 2 in the −120° direction, while mode 2 is always scattered to mode 1 in the +120° direction"（grep "120" ✓）→ 三组独立 zigzag 模。依据 `Phase_S/appendix_B_theory.md` §B.5#13 + `cards.md` T12 |
| 2026-09-01 | **按 4 块辨识结构整体重写**：对齐 E12 结构/粒度/证据标注，§3 改为「理论模型与方法」；新增四层变量表、可辨识性判别表（网络 vs TZM 四条判别）、[前提与限定]、主结果↔判别映射、§9 理论模型映射、反向核对 pass；保留旧 📜Q 事实 |
| 2026-09-01 | **降级/删除无源内容**：① De Beule 2020 / Hou 2024 对标从旧 §5「与其他工作」移入 §7 并降级 💭I（时间倒挂、非本文引用、引用列表无此二者）；② 旧 §2.1 "Rickhaus/Huang 实验支持网络图景"改为原文 "network probed by transport [34–36] / STM [37]"；③ 旧 §6 "未计算有限温输运""电导量子化未裁决"标 💭I（原文仅明言无序散射留待未来）；④ 全文数字补证据分级 + [~] 标注（理论计算无误差棒） |
