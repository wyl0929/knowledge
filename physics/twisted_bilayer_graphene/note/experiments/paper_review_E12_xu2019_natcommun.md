<!--
 * @Author       : AI 精读 (系统辨识式阅读法)
 * @Date         : 2026-08-06（初读）→ 2026-08-29（系统辨识重读）
 * @LastEditTime : 2026-08-29
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/experiments/paper_review_E12_xu2019_natcommun.md
 * @Description  : E12: Xu et al. 2019 — mTBG 三角网络 1D 态的巨幅 AB 振荡（按 15_case_study 系统辨识式阅读法重读）
-->

# Paper Review: Xu et al. (2019) — mTBG 三角网络 1D 态的巨幅 AB 振荡

| 字段 | 内容 |
|------|------|
| **编号** | E12 |
| **标题** | Giant oscillations in a triangular network of one-dimensional states in marginally twisted graphene |
| **作者** | S.G. Xu, A.I. Berdyugin, P. Kumaravadivel, F. Guinea, R. Krishna Kumar, D.A. Bandurin, S.V. Morozov, W. Kuang, B. Tsim, S. Liu, J.H. Edgar, I.V. Grigorieva, V.I. Fal'ko, M. Kim, A.K. Geim |
| **期刊** | Nature Communications 10, 4008 (2019) |
| **DOI** | 10.1038/s41467-019-11971-7 |
| **类型** | 实验 — 低温输运 |
| **课题组** | Geim group (Manchester) |
| **PDF** | ✅ reference/pdfs/Xu 等 - 2019 - ...pdf |
| **SI PDF** | ✅ reference/pdfs/Xu 等 - 2019 - SI of Giant oscillations...pdf（Supplementary Note 1–6 + Fig. S1–S6） |
| **DW.bib** | ❌ 待收录（⚡ 新发现） |
| **精读日期** | 2026-08-06（初读）→ 2026-08-29（系统辨识式重读） |

---

## TL;DR

在极小扭角 mTBG（θ≈0.10°，λ≈140 nm）双栅器件中，加位移场 D=0.5 V/nm 使 AB/BA 畴区开隙（δ≈50 meV）绝缘后，残存的**三角畴壁 1D 态网络**仍导电，并表现出两类"巨幅"相干振荡：① **随磁场 B 的 AB 振荡**（周期 ΔB=0.48 T，振幅达 ρ_xx 零场值的 ~50%、>1 kΩ，持续到 120 K）；② **随载流子密度 n 的 miniband 填充振荡**（Δn≈5×10¹⁰ cm⁻²，伴随 Hall 符号多次反转）。两条独立测量（ΔB→A 与 Δn→A）反推出同一个三角回路面积 A≈0.8–0.86×10⁻¹⁰ cm²，并与 FFT 谐波 ΔB、ΔB/2、ΔB/3（=1/2/3 个三角畴回路）自洽 → 判定载流子沿畴壁 1D 态网络的三角闭合回路做相干 AB 干涉。其"巨幅"（≈50% ρ_xx）远超 Rickhaus 2018 的弱振荡，是 T15（De Beule 2020）AB 散射理论的直接实验对标。

---

## §0 系统辨识速览（按 15_case_study 协议）

> 本 review 按 `systems_science/case/15_case_study_paper_reading_system_identification.md` 的"系统辨识式阅读法"重读。先把论文当作"输入旋钮→输出观测→反推内部结构"的辨识记录。

### Step 0 — 黑箱三要素

```
输入旋钮 u:  { Vtg(顶金属栅), Vbg(底石墨栅) → n, D ;  B(磁场);  T(温度) }
输出观测量 y: { ρxx(B,n,D,T),  ρxy(B,n,D,T),  d²ρxx/dB²,  FFT[ρxx(B)] }
声称结论 θ:  { 三角畴壁 1D 态网络承载相干 AB 干涉 + 隙内窄 miniband 序列 }
```

### Step 1 — 变量依赖图（四层，一次钉死）

| 层 | 含义 | Xu 2019 实例 |
|----|------|-------------|
| **L1 旋钮（u）** | 直接施加 | $V_{tg}$（顶金属栅）、$V_{bg}$（底**少层石墨**栅）、$B$（0–数 T）、$T$（0.3–120 K） |
| **L2 导出量（x₁）** | 由旋钮经静电/几何算出 | $n$（载流子密度）、$D$（层间位移场）、$\theta$（扭角）、$\lambda=a/[2\sin(\theta/2)]$、$\delta$（AB/BA 畴区能隙，$D$→$\delta$） |
| **L3 模型量（x₂）** | 由能带/几何算出 | $A=\frac{\sqrt3}{4}\lambda^2$（单三角回路面积）、$L=3\lambda,4\lambda,5\lambda$（回路周长）、$v_{DW}$（1D 态漂移速度）、$L_\phi(T)$（退相干长度）、$\varepsilon$（miniband 间隔） |
| **L4 观测量（y）** | 直接测量 | $\rho_{xx}$、$\rho_{xy}$、$d^2\rho_{xx}/dB^2$（高通滤波）、FFT 谱 |

> ⚠️ **本文与 E10 (Rickhaus) 的符号差异**：E10 测**电导** $G$ 及其 $dG/dn_{in}$；本文测**电阻率** $\rho_{xx}$ 及其 $d^2\rho_{xx}/dB^2$（对 B 二阶导）。且本文 $n$ **未分** $n_{in}/n_{out}$（正文只用单一 $n$），$D$ 与 $n$ 的显式栅压换算在 Supplementary Note 1 📜Q（原式见 §3.2）。SI 记石墨栅为下标 `gg`（graphite gate）：$C_{gg},V_{gg}$。

### Step 2 — 传递函数链（三层）

```
L1 旋钮 ──[静电学: n=(Ctg·Vtg+Cbg·Vbg)/e, D=(Dtop−Dbottom)/2  💭I 背景]──→ L2 {n, D}
L2 {D,θ,λ} ──[能带: D→δ≈50meV;  λ→A=√3/4·λ²]──→ L3 {δ, A, L}
L3 {A,L} + B ──[输运: AB 干涉 ΔB=φ₀/A;  谐波 ΔB/2,ΔB/3;  T 衰减 e^(−L/Lφ)]──→ L4 {ρxx 振荡}
L2 {n} + 隙内 miniband ──[填充: Δn=4/A;  miniband 间隔 ε≈5meV]──→ L4 {ρxx(n), ρxy 反转}
```

### Step 3 — 可辨识性判别实验（含金量所在）

| 判别 | 判据（数据） | 排除谁 | 确立谁 |
|------|-------------|--------|--------|
| **体 vs 墙（边-体区分，存在性）** | D=0.5 V/nm 使畴区开隙 δ≈50 meV 绝缘，但 NP 处**仍金属性**（T↓ 时 ρxx↓ 到几 kΩ，Fig. 1c）——与 Bernal BLG 相反 📜Q | 畴区/体 2D 导电（已开隙绝缘） | 导电通路在 AB/BA 畴壁（1D 通道**存在**）——⚠️ 仅证"墙导电"，见下方注 |
| **AB vs SdH** | 低场 B 周期振荡，振幅达 50% 且**持续到 120 K**；到数 T 才被 SdH 淹没 | Shubnikov–de Haas（需低温、随 B 增强） | AB 干涉（低场、随 T 指数衰减但不需 LL 量子化）——机制判据详见附录 A.3 |
| **AB vs 介观涨落** | ρxx(n) 振荡**不随接触配置与 D 变化**（可复现） | 无序介观涨落（随机、不可复现） | 确定性 miniband 填充 |
| **谐波归属（1/2/3 畴）** | FFT 峰 ΔB、ΔB/2、ΔB/3；其 T 衰减斜率比 **~1 : 4/3 : 5/3** | 其他回路几何 | 1/2/3 个三角畴回路（L=3λ,4λ,5λ） |
| **ΔB 与 Δn 独立互验** | ΔB→A=0.86；Δn=4/A→A=0.80（两法一致） | 单一测量偶然 | 三角回路面积 A 唯一确定 |
| **Hall 反转 vs 现有模型** | ρxy 多次变号、平均 Hall 反号 | San-Jose 2013 / Efimkin 2018 现有模型（解释不了） | 需"skipping orbit"类比（开放问题，待理论） |

> **注（"1D 通道存在"是分层排除，非一步证成）**：论文对 1D 通道的论证是**分层排除**，单条观测各有其"可辨识"范围——①「体 vs 墙」先证**导电通路在墙不在体**（排除法：畴区开隙绝缘 + NP 金属性 → 只剩墙），这一步只确立"墙导电"这一**必要条件**；②「AB vs SdH」+「谐波归属」再证墙内通路**相干**且沿三角闭合回路；③「ΔB/Δn 互验」证回路的**量化几何**（miniband 网络）。因此"NP 金属性"单独**不能**证"1D/相干/拓扑"——作者用词正是 "in agreement with the expected 1D transport"（**一致**，非"证明"）📜Q；1D 维度性 + 相干性 + 拓扑性需上表其余行联合确立。⚠️ 正文此句引 Supplementary Note 5，但"金属性 NP 的温度依赖"实验佐证实为 SI Note 4（Fig. S4），Note 5 是 miniband 谱理论——正文引用略有错位，本 review 已据 SI 原文校正 💭I。

### Step 5 — 三层标注（全 review 统一）

📜Q = 原文直接陈述（附位置）｜推导 = 由原文原式合成的代数结论｜💭I = 背景/推断。本 review 所有数字均经 pdftotext 提取 + grep 反向核对。

---

## 1. 核心贡献

在极小扭角 MTG（θ≈0.1°）中发现：

1. **巨幅 AB 磁振荡** — 振幅达电阻的 **~50%**（>1 kΩ），持续到 **120 K（>100 K）** 📜Q（摘要 "reach in amplitude up to 50% of resistivity and persist to temperatures above 100 K"）
2. **密度振荡 + Hall 符号多次反转** — 揭示带隙内由 1D 态网络形成的**窄 miniband 序列**（间隔 ~5 meV）📜Q（摘要）
3. 把畴壁网络的输运信号从 Rickhaus 2018 的"弱振荡"推进到**"强可测、可做 FFT 谱学"**的阶段（振幅大 ~50% vs 弱，且到高温）💭I（对照，见 §7）

---

## 2. 物理机制

### 2.1 网络形成与"手征/螺旋"态（QVH 畴壁态，含术语辨析）

网络形成四步 📜Q（引言）：

1. 小 θ 下 tBLG 发生**应变伴随的晶格重构** → 出现亚微米 AB/BA 三角畴（Bernal 堆垛）📜Q（摘要/引言）
2. 加层间偏置（位移场 D）→ AB/BA 畴区**开隙 δ** → 畴区绝缘 📜Q（摘要 "interlayer bias is applied to open an energy gap inside the domain regions making them insulating"）
3. AB/BA 畴壁承载 **1D 态** → 形成**三角网络**，保持导电 📜Q（摘要）
4. 每条 AB/BA 畴壁两侧各有 **4 条（2 自旋 × 2 谷）无能隙 1D 态**；不同谷**反向传播**；在畴壁交汇处（堆垛变为 AA）劈裂 📜Q（正文 "there are four (2 spins and 2 valleys) gapless 1D states on each side. They propagate in opposite directions for different valleys and split apart at the superlattice's vertices where the stacking changes into AA"）

> **"墙导电"的实验判据（排除法，即 Step 3 第一行「体 vs 墙」）**：D=0.5 V/nm 使畴区开隙 δ≈50 meV（本应绝缘，T≤50 K 高度绝缘，据 Bernal BLG ref 19 📜Q），但 NP 处 ρxx 却**随 T↓ 而↓**（金属性，液氦温降到几 kΩ，Fig. 1c）——与 Bernal BLG 相反 📜Q（正文 "MTG hosts a metallic system, in contrast to Bernal-stacked BLG and in agreement with the expected 1D transport along AB/BA walls"）。逻辑：畴区已开隙绝缘 → 若仍有导电，通路**只能在畴壁**。⚠️ 但此步只确立"墙导电"这一**必要条件**，不单独证"1D/相干/拓扑"——作者用词 "in agreement with"（一致）而非"证明"；1D 维度性由后续 AB 振荡 + miniband 量化联合确立（见 §0 Step 3 注）。

> ⚠️ **术语辨析**：摘要称 "chiral one-dimensional states"，但正文机制是**谷锁定反向传播**（helical，K/K′ 反向）——严格说是**量子谷霍尔（QVH）畴壁态**，不是"总电荷手征（chiral）"的 QH 边缘通道（后者需 B、净电荷 Chern 数）。同一术语 nuance 见 E10 review §2.1 辨析表 💭I。网络基本单元 = **等边三角形**，面积 $A=\frac{\sqrt3}{4}\lambda^2$ = 超晶格单胞（含 AB+BA 两畴）的一半 📜Q（正文 "The unit block for this 2D network is an equilateral triangle with the area A = √3/4 λ², half the size of the superlattice unit cell that includes both AB and BA domains"）。

### 2.2 巨幅 AB 振荡机制（核心，可辨识性判别）

**现象**：加 D 后，网络在所有器件中都表现出**随 B 周期**的强磁振荡；随 D 增大而发展，持续到 AB/BA 畴因掺杂或升温变导电为止（D=0.5 V/nm 时 |n| ≤ 5×10¹¹ cm⁻²、T ≤ 120 K）📜Q（正文 "The oscillations developed with increasing D and persisted until AB and BA domains became conductive..."）。

**机制 = 三角回路的 AB 干涉**：

- 电子沿畴壁网络的**闭合三角回路**传播，回路包围畴区面积 A；绕行相位随穿过 A 的磁通 $\Phi=BA$ 变化 → $\rho_{xx}$ 随 B 周期振荡，周期 $\Delta B=\phi_0/A$（$\phi_0=h/e$）📜Q（正文 "interference between electronic states propagating along, e.g., the red loop in Fig. 1a is expected to vary periodically with the magnetic flux piercing the domain area A"）。
- **高次谐波**：FFT 峰 $\Delta B$、$\Delta B/2$、$\Delta B/3$ = 分别包围 1、2、3 个三角畴的回路（面积 A、2A、3A）📜Q（正文 "twice and thrice larger areas... attributed to the loops such as those indicated by the blue and green arrows in Fig. 1a"）。
- **谐波归属的独立验证**：高次谐波随 T 衰减**更快**，衰减率比值 ~4/3、5/3 = 回路周长比 $L=3\lambda,4\lambda,5\lambda$；符合 $e^{-L/L_\phi}$ 退相干图像 📜Q（Fig. 2b + 正文 "decay rates ... followed the ratios L/Lϕ expected from the circumferences of the three involved loops (L = 3λ, 4λ, and 5λ)"）。
- **排除 SdH**：周期振荡持续到数 T 才被 SdH 淹没 📜Q（"persisted up to several Tesla where they became overwhelmed by Shubnikov-de Haas oscillations"）；且 AB 振荡能活到 120 K（SdH 在如此高温早已抹平）💭I（推断）——机制判据（几何相位 vs 朗道量子化、LK 热阻尼、B vs 1/B 周期）详见附录 A.3。

> **"巨幅"的来源**：振幅 ~50% ρ_xx(B=0) 意味着干涉环路几乎串联起了全部输运通道——不是背景上的一小纹波，而是主导输运的相干分量 📜Q（">1 kOhm... nearly ~50% of zero-B resistivity"）。这是与 E10 弱振荡的本质差别 💭I（对照）。

### 2.3 密度振荡（miniband 填充）机制

- 固定 D、扫 n（保持 AB/BA 畴绝缘的低掺杂区）：零场 $\rho_{xx}(n)$ 出现**振荡**，$\rho_{xy}(n)$ 在隙内**多次变号** 📜Q（Fig. 3 + 正文）。
- **排除介观涨落**：振荡对不同接触配置、不同 D 都**可复现**（不随机）📜Q（"It remained the same for measurements using different contact configurations and different D"）。
- **机制 = 隙内窄 miniband 的连续填充**：三角 1D 态网络形成 2D 超晶格 → 隙内出现一系列**窄 miniband**（refs 14,15 的网络模型）📜Q（"consecutive filling of electronic minibands formed by the triangular 2D lattice of 1D chiral states as suggested in refs. 14,15"）。每个 miniband 含电子/空穴型态 → 交替填充产生多个 NP（ρxy=0）与变号 ρxy 📜Q。
- **周期 Δn = 4/A**：每多填 1 个电子/畴区（四重简并：自旋×谷）→ 主周期 $\Delta n=4/A$ 📜Q（"The expected main periodicity Δn is given by 4/A which corresponds to one extra electron per AB or BA domain, taking into account the fourfold degeneracy"）。

### 2.4 Hall 符号反转机制（开放问题）

- 低温（0.3 K）隙内 ρxy 随 n、B 多次变号（Fig. 3b，±250 Ω）；50 K 下平均 Hall 响应**反号**（电子掺杂却呈空穴样，反之亦然，Fig. 3c，±3 kΩ）📜Q。
- 机制（作者定性类比，**非既有模型推导**）：借 QH 手征态的 **skipping orbit（跳跃轨道）**图像——电子沿 AB/BA 畴**内侧边界**环绕，方向与回旋轨道相反 → 小闭合回路的平均效应呈**空穴样** → 三角网络上的一群 skipping orbits 产生空穴样 Hall 📜Q（正文 "evoke an analogy with 1D chiral states in the quantum Hall effect... electrons would then circulate in the direction opposite to that for cyclotron orbits, that is, an average effect from such small closed loops would be hole-like"）。
- ⚠️ **作者明言**：该反转**不来自任何现有模型**（refs 14,15），类比需 miniband 能谱理论佐证 📜Q（"does not follow from any of the existing models... requires theoretical corroboration"）。

### 2.5 AB 振荡为何"周期在 B 完美、在 n 不完美"（讨论）

- 现象：miniband **在 B 上严格周期**（AB），**在 n 上不完全周期** 📜Q（讨论 "The reason why the minibands evolve periodically in B (Aharonov-Bohm oscillations) but not fully so in n"）。
- 原因：D 与有限 n **解除 AB/BA 简并** → 畴壁两侧 1D 态费米速度略不同 → AB/BA 干涉拍频；长回路再加随机性 📜Q（讨论段）。

### 2.6 Discussion 段三问（作者自设的三个问题/谜题）

论文 Discussion 段围绕**三个问题**展开（分别由 SI Note 4/5/6 支撑）：

| # | 问题 | 作者的解答 | 证据 |
|---|------|-----------|------|
| **1** | miniband 在 B 上严格周期（AB），在 n 上**不完全**周期 | D 与有限 n 解除 AB/BA 简并 → 畴壁两侧 1D 态费米速度略不同 → 拍频；长回路加随机性 | 📜Q（讨论段）；SI Note 5/6（Fig. S5c 速度发散） |
| **2** | AB 振荡活到 120 K，但 miniband 间隔仅 5 meV（>20 K 就热抹平）——表面矛盾 | Brown–Zak 类比：miniband 对 B **一致响应**（平均群速度变化）→ AB 能活过被热抹平的 miniband | 📜Q（讨论段引 ref 30）；SI Note 4 |
| **3** | 平均 Hall **反号**（电子掺杂→空穴样，反之亦然） | skipping-orbit 类比（电子沿畴内侧边界反向环绕 → 小闭合回路平均空穴样）；**不来自任何现有模型**，需理论佐证 | 📜Q（讨论段）；开放问题 |

> 顺带从问题 1 的驻波图像估 $\Delta E=2\varepsilon=10$ meV → $v_{DW}\approx10^6$ m/s ≈ Dirac 速度 → 暗示 AB/BA 畴壁**极其 sharp**。SI Note 6 给定量判据：sharp 畴壁要求宽度 $w<v/\sqrt{\gamma_1\delta}$，此时 $v_{DW}\approx v$；若 $w$ 大则 $v_{DW}$ 变小且出现抛物线型非拓扑通道 → 隙内 miniband 数 $M\approx\delta/(v_{DW}h/6\lambda)$ 变多。实验数得 $v_{DW}\approx v$ → 反证畴壁窄而 sharp 📜Q（SI Note 6）。

---

## 3. 实验方法

### 3.1 器件（层状结构 / 制备 / 几何）

- **制备**：tear-and-stack——单层石墨烯撕成两半，平行转移 + 小旋转叠合；名义 θ=0–0.1°；实测 ≤0.25° 📜Q（正文 "a monolayer graphene crystal was teared into two parts... rotated... nominally 0 to 0.1°... exhibited twist angles of ≤0.25°"）。
- **封装**：双 hBN 封装（提高质量）📜Q（"encapsulated in hexagonal boron nitride"）。
- **栅结构**：**双栅 Hall bar**——顶栅 = 标准金属膜电极；底栅 = **少层石墨**（降低电荷不均匀）📜Q（"The top gate was the standard metal-film electrode whereas the bottom gate was thin graphite, which further improved devices' electronic quality and reduced charge inhomogeneity"）。
- **加工**：电子束光刻 + 反应离子刻蚀成形 Hall bar 📜Q（Methods）。
- **样品统计**：4 个 MTG 器件，行为一致；主样品 θ≈0.10°（均匀性最高）📜Q（"Four MTG devices were studied in detail, all exhibiting similar behavior... θ ≈ 0.10°"）。

### 3.2 静电学（旋钮 → 导出量）

> 本文**正文未给出** $n$、$D$ 显式公式，只说"用顶/底栅施加位移场 D（Supplementary Note 1）" 📜Q；但 **SI Note 1 给出原式**（下式，SI 记石墨栅为 $C_{gg},V_{gg}$）：

$$n = \frac{1}{e}(C_{tg}V_{tg}+C_{gg}V_{gg}),\qquad D = \frac{1}{2\varepsilon_0}(C_{tg}V_{tg}-C_{gg}V_{gg})$$

- 电容由**独立 Hall 测量**标定 📜Q（SI Note 1 "The capacitances were found independently through Hall measurements"）。
- 测固定 D：联动调 $V_{tg},V_{gg}$（沿 SI Fig. S1b 的 D=const 线）扫 n 📜Q。
- 关键参数锚点（原文给）：$D=0.5$ V/nm → $\delta\approx50$ meV（引 ref 20 Zhang 2009）📜Q；"D = 0.5 V nm⁻¹ (achievable without a risk of damaging the devices)" 📜Q。

### 3.3 测量（锁相 / 电阻率 / d²ρ/dB² 高通滤波）

- 标准**低频锁相**：激励频率 6–30 Hz，电流 0.3 K 时 10 nA、高温 100 nA 📜Q（Methods）。
- **观测量**：纵向电阻率 $\rho_{xx}$、Hall 电阻率 $\rho_{xy}$（kΩ 量级）📜Q。
- **高通滤波 = 对 B 二阶导 $d^2\rho_{xx}/dB^2$**：去掉平滑磁阻背景、**不移动振荡极值位置**（与 E10 的 $dG/dn$ 同逻辑：微分=高频高通滤波，见本 review 附录 A.6）📜Q（Fig. 1f caption "we plot d²ρxx(B)/dB² which removes the smooth background without shifting positions of oscillations' extrema"）。
- **FFT 分析**：$\rho_{xx}(B)$ 曲线做 FFT，分离 ΔB、ΔB/2、ΔB/3 三个频率 📜Q（Fig. 2b）。

---

## 4. 关键数据

### 4.1 主样品与网络几何

| 参数 | 值 | 证据 |
|------|-----|------|
| 扭角 θ | ≈ 0.10°（主样品）；≤ 0.25°（全部） | 📜Q（正文） |
| moiré 周期 λ | ≈ 140 nm | 📜Q（"yields λ ≈ 140 nm or θ ≈ 0.10° ± 3%"） |
| 单三角回路面积 A | 0.86 ± 0.04 × 10⁻¹⁰ cm²（ΔB 反推） | 📜Q |
| 回路周长（1/2/3 谐波） | L = 3λ, 4λ, 5λ ≈ 420/560/700 nm | 📜Q |
| 迁移率（n≈10¹² cm⁻²） | ~10⁴ cm²/V·s | 📜Q（Fig. 1b caption） |

### 4.2 能隙与导电窗口

| 参数 | 值 | 证据 |
|------|-----|------|
| D=0.5 V/nm 时畴区能隙 δ | ~50 meV | 📜Q（引 ref 20） |
| 畴区绝缘掺杂范围 | \|n\| ≲ 3–5 × 10¹¹ cm⁻²（低于此才绝缘） | 📜Q（"n above ±3–5 × 10¹¹ cm⁻² to start populating the conduction and valence bands"） |
| 电荷中性点（NP）行为 | 金属性（T↓ 时 ρxx↓ 到几 kΩ） | 📜Q（Fig. 1c + 正文） |

### 4.3 AB 振荡

| 参数 | 值 | 证据 |
|------|-----|------|
| 主周期 ΔB | 0.48 ± 0.02 T | 📜Q |
| 面积 A（ΔB 反推） | 0.86 ± 0.04 × 10⁻¹⁰ cm² | 📜Q |
| 低温振幅 | >1 kΩ，~50% ρxx(B=0) | 📜Q |
| 温度上限 | 120 K（>100 K；D=0.5 V/nm） | 📜Q |
| T<50 K 增长 | 指数增长 | 📜Q（"grew exponentially"） |
| FFT 谐波 | ΔB、ΔB/2、ΔB/3 | 📜Q |
| 谐波 T 衰减斜率比 | ~1 : 4/3 : 5/3 | 📜Q（Fig. 2b caption） |
| 高场行为 | 数 T 处被 SdH 淹没 | 📜Q |

### 4.4 密度振荡与 miniband

| 参数 | 值 | 证据 |
|------|-----|------|
| 密度周期 Δn | 5 ± 0.5 × 10¹⁰ cm⁻² | 📜Q |
| 面积 A（Δn 反推） | 0.80 ± 0.09 × 10⁻¹⁰ cm² | 📜Q |
| 隙内振荡数 | ~10 个（\|n\| < 3 × 10¹¹ cm⁻²） | 📜Q |
| miniband 平均间隔 ε | ~5 meV | 📜Q |
| miniband 振荡消失温度 | >20 K | 📜Q（"completely disappear above 20 K"） |
| ΔE = 2ε（最小回路驻波能差） | 10 meV | 📜Q |
| DW 漂移速度 v_DW | ~10⁶ m/s（≈石墨烯 Dirac 速度） | 📜Q（推导见 A.4） |

### 4.5 Hall 效应

| 参数 | 值 | 证据 |
|------|-----|------|
| 0.3 K、B=40 mT 隙内 ρxy | ~±250 Ω | 📜Q（Fig. 3b caption） |
| 50 K 平均 Hall 响应 | ~±3 kΩ | 📜Q（Fig. 3c caption） |
| 反号方向 | 电子掺杂→空穴样（反之亦然） | 📜Q |

### 4.6 证据链汇总（可辨识性小结）

**证明 1D 网络相干输运**：① AB 振荡巨幅（~50% ρxx）；② FFT 谐波 1/2/3 畴回路 + 周长比衰减；③ 密度振荡 Δn=4/A 与 ΔB=φ₀/A 两法反推同一 A；④ 振荡可复现（排除介观涨落）📜Q。

**证明 miniband 谱结构**：密度振荡 + Hall 多次变号 → 隙内窄 miniband（ε≈5 meV）连续填充 📜Q。

**开放项**：Hall 平均反号无定量理论（skipping orbit 类比待佐证）📜Q。

---

## 5. 主要结论

1. 小扭角 MTG + 位移场 → AB/BA 畴壁**三角网络**支持相干 1D 输运；AB 振荡达 ρxx ~50%，远超常规 2D 体系 📜Q。
2. 磁振荡（ΔB→A）与密度振荡（Δn→A）**独立互验**，共同锁定三角回路面积 A ≈ 0.8–0.86×10⁻¹⁰ cm²，对应 λ≈140 nm、θ≈0.10° 📜Q。
3. 隙内存在由网络量子化产生的**多个窄 miniband**（间隔 ~5 meV），其电子/空穴型交替导致 Hall 符号反复反转，与常规 2D BLG 截然不同 📜Q。
4. 作者明确（保守）表态：Hall 反转"不来自任何现有模型"，需 miniband 能谱理论佐证 📜Q。

---

## 6. 局限与未解决的问题

| 局限 | 说明 | 证据 |
|------|------|------|
| Hall 反转无定量理论 | 仅 "skipping orbit" 类比，需 miniband 谱计算 | 📜Q（正文 "requires theoretical corroboration"） |
| 密度振荡非严格周期 | AB/BA 简并被 D 与有限 n 解除 → 速度失配拍频 + 长回路随机 | 📜Q（讨论段） |
| 高温分辨率有限 | miniband 间隔 ~5 meV → T>20 K 密度振荡热抹平 | 📜Q |
| 无实空间成像 | 路径几何由输运反推，非直接成像 | 💭I（推断） |
| 网络 vs 单通道尺度 | 哪个主导 AB 振荡未完全裁决（T15 后续散射理论才系统处理） | 💭I（推断，见 cards.md E12 局限） |

---

## 7. 与其他工作的关系

| 工作 | 关系 | 证据 |
|------|------|------|
| San-Jose & Prada 2013 (ref 14) | 螺旋网络理论——miniband 描述与 Δn=4/A 的来源 | 📜Q（正文引用） |
| Efimkin & MacDonald 2018 (ref 15) | 网络模型——miniband 填充图景 | 📜Q（正文引用） |
| Rickhaus 2018 (ref 16) | 首次 FP+AB 输运——本文 AB 信号**强得多**（~50% vs 弱）且到高温 | 📜Q（正文引用 ref 16） |
| Huang 2018 (ref 11) | STM 发现网络——本文提供器件尺度输运证据 | 📜Q（正文引用 ref 11） |
| Yoo 2019 (ref 12) | 重构畴壁网络结构基础（θ~0.1° 下） | 📜Q（正文引用 ref 12） |
| Zhang 2009 (ref 20) | BLG 能隙 δ(D) 标定（~50 meV @ 0.5 V/nm） | 📜Q（正文引用） |
| Krishna Kumar 2018 (ref 30) | Brown–Zak 振荡——解释 AB 振荡高温稳健的类比 | 📜Q（讨论段引用） |

> ⚠️ **Phase S 外部对标（非本文引用）**：T15 De Beule 2020（AB 散射统一理论）是**后续**理论对本文巨幅 AB 振荡的重新解释（散射相位参数解释对温度的稳健性）——本文（2019）不可能引用它 💭I（来自 cards.md，原文未引）。与 E10 相同："理论对标"是时间倒挂的后续重释，非本文自身理论框架。

---

## 8. 对后续研究的影响

- 把畴壁网络输运推进到**"强可测、可做 FFT 谱学 + 高温稳健"**阶段——AB 振荡 ~50% ρxx 且到 120 K，为干涉器件/传感提供平台 📜Q（摘要）。
- 提出可编程 1D 网络电子学的三参数协同调控（D、n、B）💭I（推断）。
- 两个**具体理论任务**留给后续：① Hall 平均反号与 miniband 能谱/曲率的关系；② AB/BA 不等价 + 速度失配 + 长回路 + 有限温退相干的统一输运模型（De Beule 2020 T15 承接）📜Q（正文开放问题）→ 💭I（对 T15 的承接为推断）。
- 证明**非 magic-angle 极限**也有独特强效应——重构网络态本身就是重要新物理平台 💭I（推断）。

---

## 9. 理论模型映射（供 tbplas / Kubo-Bastin 对照）

> 本文**无新理论框架**，理论贡献 = 既有网络模型（refs 14,15）应用 + 定量几何反推。作者贡献声明：V.I.F. 与 F.G. "provided the presented theory calculations" 📜Q（Author contributions）。

| 映射 | 说明 | 证据 |
|------|------|------|
| $D \to \delta$ | 位移场 → 畴区能隙（~50 meV @ 0.5 V/nm，引 ref 20） | 📜Q |
| $\theta \to \lambda \to A$ | 扭角 → moiré 周期 → 三角回路面积 $A=\sqrt3/4\,\lambda^2$ | 📜Q |
| $\Delta B = \phi_0/A$ | AB 主周期 ↔ 单回路面积 | 📜Q |
| $\Delta n = 4/A$ | 密度周期 ↔ 每畴一电子（四重简并） | 📜Q |
| $\Delta E = hv_{DW}/L$ | miniband 间隔 ↔ 最小回路驻波能量 → $v_{DW}$ | 📜Q |

> **与 TBPM/Kubo 的对应**（供理论复现，💭I）：实验 $\rho_{xx}$（两端子电阻率，器件量）与 Kubo-Bastin $\sigma_{xx},\sigma_{xy}$（体电导率，材料量）是同一线性响应的器件版/材料版；但 AB/密度振荡是**有限尺寸相干效应**，bulk $\sigma_{xx}$ 只给平滑背景——要复现需有限器件 Landauer/Fisher-Lee 透射计算（同 E10 §9 注记）。变量对齐：$n\leftrightarrow E_F$（经 DOS）、$D\leftrightarrow \Delta$（on-site）、$B$ 两者都有。

---

## 附录 A：推导与背景（💭I）

> ⚠️ 本附录为代数推导与背景知识（非 Xu 2019 原文陈述）；涉及本文的具体参数均复用正文 📜Q 证据，此处只做数值自洽性核算。

### A.1 moiré 周期与三角面积

$$\lambda=\frac{a}{2\sin(\theta/2)}\approx\frac{a}{\theta}\quad(a=0.246\ \text{nm});\qquad A=\frac{\sqrt3}{4}\lambda^2$$

数值：θ=0.10°=1.745×10⁻³ rad → λ≈141 nm；A=0.433×(141 nm)²=0.86×10⁻¹⁰ cm² ✓（与正文 0.86 一致）。

### A.2 AB 周期

$$\Delta B = \frac{\phi_0}{A}=\frac{h/e}{A}$$

$\phi_0=4.1357\times10^{-11}$ T·cm²；A=0.86×10⁻¹⁰ cm² → ΔB=0.48 T ✓（正文 0.48±0.02 T）。谐波 ΔB/2、ΔB/3 ↔ 面积 2A、3A（2、3 个三角畴）。

### A.3 AB vs SdH 判别机制（可辨识性，供 §0 Step 3 判别表 / §2.2 排除 SdH 的物理依据）

> 本小节回答"为什么低场 + 50% 巨幅 + 120 K 存活就能判 AB 而非 SdH"。核心：两者机制本征不同——AB 是**几何相位**效应，SdH 是**朗道量子化**效应，故对 B、T 的依赖恰好相反。本节为教科书背景 💭I，涉及本文参数复用正文 📜Q 证据。

**AB 机制（几何相位）**：电子波沿闭合环路分顺/逆时针两路传播后汇合，磁矢势给纯几何相位差 $\Delta\phi=2\pi\Phi/\Phi_0$（$\Phi=BA$，$\Phi_0=h/e$）。电导 $\propto\cos(2\pi\Phi/\Phi_0)$ → **B 轴上等间距**周期 $\Delta B=\Phi_0/A$。磁场只当"相位旋钮"，**不要求形成朗道能级**，B→0 即已存在；唯一条件是相位相干 $L_\phi(T)>L$，振幅 $\propto e^{-L/L_\phi}$（见 A.5）。

**SdH 机制（朗道量子化）**：强场下态密度劈成离散朗道能级，扫 B 时费米能级逐个穿过（填充因子 $\nu=n\Phi_0/(gB)$ 过整数）→ 电阻振荡，**1/B 轴上等间距** $\Delta(1/B)=g/(n\Phi_0)$。存在两个硬条件：

1. **量子迁移条件** $\omega_c\tau=\mu B\gg1$：$\mu\approx10^4$ cm²/V·s（正文 📜Q）→ B=1 T 时 $\omega_c\tau\approx1$，B<1 T 朗道能级根本分不开；
2. **热条件** $\hbar\omega_c\gg k_BT$（LK 因子 $R_T=X/\sinh X$，$X=2\pi^2k_BT/\hbar\omega_c$）。

**三条观测逐一排除 SdH**：

| 观测（正文 📜Q） | SdH 的要求 | 排除结论 |
|------|-----------|---------|
| 低场（~0.1–1 T）已振荡 | $\omega_c\tau=\mu B\approx1$（B=1 T）→ 朗道能级未分辨 | 低场无 SdH；AB 不需朗道量子化 |
| 振幅 ~50% ρxx | SdH 是背景小纹波（几个 %） | 50% = 干涉开关主输运通道 = AB |
| 持续到 120 K | $k_BT\approx10$ meV；B=1 T 时 $\hbar\omega_c\approx12$ meV（m*≈0.01 m₀）→ $X\approx17.5$，$R_T\sim e^{-17}\sim10^{-7}$ | 120 K 时 SdH 热抹平到百万分之一；AB 只要 $L_\phi>L$ |

**内交叉验证（作者自证）**：AB 振荡"持续到数 T 处才被 SdH 淹没" 📜Q——同一器件里两机制先后登场，低场 AB、高场 SdH 长出来盖掉它。若低场振荡本身是 SdH，应低场最弱、高场最强，而非反过来。

**最干净判据（B vs 1/B）**：AB 在 **B 轴**等间距（恒 ΔB=0.48 T）；SdH 在 **1/B 轴**等间距，换算回 B 轴 $\Delta B\approx B^2\Delta(1/B)$ 随 B 变密。画 $1/B$ 轴看是否等间距即教科书级判别（本文未逐字写出，💭I 背景补充，支持其归属）。

### A.4 密度周期与 miniband 能标

$$\Delta n=\frac{4}{A};\qquad \Delta E=\frac{h v_{DW}}{L}\ (L=3\lambda)$$

数值：A=0.86×10⁻¹⁰ cm² → Δn=4.65×10¹⁰ cm⁻²（实测 5±0.5×10¹⁰，用 A=0.80 回代自洽）。ΔE=2ε=10 meV、L=3λ=420 nm → $v_{DW}=\Delta E\cdot L/h$=10 meV×420 nm/h≈10⁶ m/s ✓（正文）。

### A.5 退相干与谐波衰减（AB 高温稳健）

谐波振幅 $\propto e^{-L/L_\phi(T)}$（ref 27）。L=3λ、4λ、5λ → 衰减斜率比 ≈1:4/3:5/3，与 Fig. 2b 吻合 📜Q。AB 振荡能活到 120 K，作者借 Brown–Zak 振荡（ref 30）类比解释：miniband 对 B 的**一致响应**（平均群速度变化）可抹平热展宽 💭I（背景）。

### A.6 高通滤波（d²ρ/dB² vs E10 的 dG/dn）

E10 用 $dG/dn$（对密度求导）锐化 FP 纹波；本文用 $d^2\rho_{xx}/dB^2$（对磁场二阶导）锐化 AB 纹波——**同一"微分=高通滤波"操作在磁轴上的版本** 📜Q（Fig. 1f caption：去除平滑背景、不移动极值）。控制论语言：$\rho_{xx}$ 是原始输出，$d^2\rho_{xx}/dB^2$ 是经高通预处理的观测（延续 15_case_study §4.1 洞察）💭I。

---

## Phase S 补充：三问框架（2026-08-29）

### Q1: edge state 实验上如何表征?

低温输运（0.3 K，锁相 6–30 Hz/10 nA）📜Q。手段与判据：**巨幅 AB 振荡**（ΔB=0.48 T → A=0.86×10⁻¹⁰ cm²，振幅 ~50% ρxx，谐波 ΔB/2/3 = 1/2/3 三角畴回路，周长比 T 衰减）；**密度振荡**（Δn=5×10¹⁰ cm⁻² = 4/A，miniband 连续填充）；**Hall 多次反号**（miniband 电子/空穴型交替）；**边-体区分**（D 开隙使 AB/BA 畴绝缘后网络仍金属性导电 → 输运在畴壁不在畴体；振荡面积 = 三角畴回路，介于单胞与整器件之间）——详见 §2/§4。

### Q2: 理论如何复现边界态?

本文**无新理论**，理论贡献 = 既有网络模型（San-Jose & Prada 2013 ref 14 + Efimkin & MacDonald 2018 ref 15）应用 + 定量几何反推（ΔB→A、Δn→A、ΔE→v_DW）📜Q。⚠️ 复现方式不是从哈密顿量导出畴壁态，而是把"三角网络假设 + AB/miniband 定量关系"映射到振荡数据 💭I。Hall 反转作者明言"不来自任何现有模型"，留待后续 💭I。

### Q3: 理论与实验如何对应?

| 理论预言 | 实验对应 | 证据 |
|------|------|------|
| D 开隙使 AB/BA 畴绝缘、网络导电 | NP 处金属性（T↓ ρxx↓），畴区 \|n\|<3–5×10¹¹ 绝缘 | 📜Q |
| 三角回路 AB 干涉 ΔB=φ₀/A | ΔB=0.48 T → A=0.86×10⁻¹⁰ cm² | 📜Q |
| 1/2/3 畴回路 → 谐波 | FFT 峰 ΔB、ΔB/2、ΔB/3 + 周长比衰减 | 📜Q |
| miniband 填充 Δn=4/A | Δn=5×10¹⁰ cm⁻² → A=0.80×10⁻¹⁰ cm² | 📜Q |
| miniband 间隔 ε | ε≈5 meV（10 个隙内振荡 / δ≈50 meV） | 📜Q |
| 现有模型（refs 14,15）解释 Hall | **失败**（平均 Hall 反号）→ 需 skipping-orbit 类比 + 新理论 | 📜Q |

---

## 反向核对 pass (2026-08-29)

pdftotext 提取 → `/tmp/xu2019.txt`（5 页）→ 逐项 grep 核对：

- ✅ θ≈0.10° / θ≤0.25° / 名义 0–0.1° / λ≈140 nm / A=√3/4 λ² / ΔB=0.48±0.02 T / A=0.86±0.04×10⁻¹⁰ / δ≈50 meV / D=0.5 V/nm / ~50% / >1 kΩ / >100 K / 120 K / |n|≤5×10¹¹ / ±3–5×10¹¹ / Δn=5±0.5×10¹⁰ / A=0.80±0.09×10⁻¹⁰ / 4/A / 四重简并 / ~10 oscillations / |n|<3×10¹¹ / ε≈5 meV / 2ε=10 meV / v_DW≈10⁶ m/s / L=3λ,4λ,5λ / 4/3、5/3 / ~10⁴ cm²/V·s / lock-in 6–30 Hz / 10 nA / 100 nA / 4 devices / four (2 spins and 2 valleys) / ±250 Ω / ±3 kΩ / 40 mT / 20 K / skipping orbit —— 全部在原文找到。
- ✅ **SI PDF 已收录并核对**（`/tmp/xu2019_SI.txt`，Supplementary Note 1–6）：$n=\tfrac1e(C_{tg}V_{tg}+C_{gg}V_{gg})$、$D=\tfrac{1}{2\varepsilon_0}(C_{tg}V_{tg}-C_{gg}V_{gg})$、电容经独立 Hall 标定（Note 1）；θ 双法独立确定——Δn→θ=0.104°±0.006°、ΔB→θ=0.10°±0.002°（Note 2）；Sharp 畴壁判据 $w<v/\sqrt{\gamma_1\delta}$、$M\approx\delta/(v_{DW}h/6\lambda)$、$v_{DW}\approx v$（Note 6）——均已入正文。
- ⚠️ 原文无：T15 De Beule 2020（后续理论，原文不可能引用）→ 已标 💭I 外部对标。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-29 | **按 15_case_study 系统辨识式阅读法整体重写**：补 §0 系统辨识速览（黑箱三要素 + 四层变量图 + 传递函数链 + 可辨识性判别表）；8 节模板补齐（原 review 仅 8 节骨架但缺 TL;DR/§9/附录/三问/反向核对）；全文加 📜Q/推导/💭I 证据分级；补 AB 振荡完整机制（谐波归属 + 周长比 T 衰减 + ΔB/Δn 独立互验 + 排除 SdH/介观涨落）；补 d²ρ/dB² 高通滤波洞察；修正旧版 "n 振荡非严格周期" 归因（明确 AB/BA 简并解除 + 长回路）；标注 SI PDF 缺失与静电学公式的 💭I 边界 |
| 2026-08-29 | 补附录 A.3「AB vs SdH 判别机制」：几何相位 vs 朗道量子化机制对比、ω_cτ 与 LK 热阻尼定量估算、B vs 1/B 周期判据、作者"数 T 处被 SdH 淹没"的内交叉验证；原 A.3/A.4/A.5 顺延为 A.4/A.5/A.6，同步修正正文两处附录交叉引用 |
| 2026-08-29 | **SI PDF 收录后回补**：SI 状态 ❌→✅；§3.2 静电学原式 💭I→📜Q（SI Note 1：$n=\tfrac1e(C_{tg}V_{tg}+C_{gg}V_{gg})$、$D=\tfrac{1}{2\varepsilon_0}(C_{tg}V_{tg}-C_{gg}V_{gg})$，电容独立 Hall 标定）；删除 §6「SI 未收录」局限；新增 §2.6「Discussion 段三问」清单（B/n 周期不对称 / 高温稳健矛盾 / Hall 反号）并标注 SI Note 4/5/6 支撑；补 SI Note 2 双法 θ 互验与 Note 6 sharp 畴壁判据 |
| 2026-08-29 | Step 3 判别表补「体 vs 墙（边-体区分，存在性）」行 + 分层排除注（"NP 金属性"只证墙导电=必要条件，1D/相干/拓扑由 AB+miniband 联合确立）；§2.1 补"墙导电排除法"判据段；校正正文"metallic at NP 引 Supplementary Note 5"的引用错位（实验佐证实为 SI Note 4，Note 5 为 miniband 谱理论）💭I |
