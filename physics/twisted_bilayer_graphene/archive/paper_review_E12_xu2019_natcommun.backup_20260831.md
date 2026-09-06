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

> **"墙导电"的实验判据（排除法，即 Step 3 第一行「体 vs 墙」）**：D=0.5 V/nm 使畴区开隙 δ≈50 meV（本应绝缘，T≤50 K 高度绝缘，据 Bernal BLG ref 19 📜Q），但 NP 处 ρxx 却**随 T↓ 而↓**（金属性，液氦温降到几 kΩ，Fig. 1c）——与 Bernal BLG 相反 📜Q（正文 "MTG hosts a metallic system, in contrast to Bernal-stacked BLG and in agreement with the expected 1D transport along AB/BA walls"）。逻辑是**三层对照**：①**受控对照（系统间）**——Bernal BLG（无墙）+D → NP 绝缘 vs MTG（有墙）+D → NP 金属，唯一差异是墙；②**排除法（系统内）**——畴区已开隙绝缘 → 若仍有导电，通路只能在畴壁；③**温度反转内控（系统内）**——T>100 K 时畴区被热激活变导电 → 金属签名消失、ρxx 随 T↑ 而↓回到 Bernal 样（SI Note 4 "2D conductivity inside the Bernal-stacking regions overwhelmed the transport contribution from AB/BA walls"）→ 反证低温金属性确来自墙 📜Q。⚠️ 但此步（①②③合计）仍只确立"墙导电"这一**必要条件**，不单独证"1D/相干/拓扑"——作者用词 "in agreement with"（一致）而非"证明"；1D 维度性由后续 AB 振荡 + miniband 量化联合确立（见 §0 Step 3 注）。

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

### 3.3 测量（锁相 / 电阻率 / 两种去背景：Δρxx 减背景 vs d²ρ/dB²）

- 标准**低频锁相**：激励频率 6–30 Hz，电流 0.3 K 时 10 nA、高温 100 nA 📜Q（Methods）。
- **观测量**：纵向电阻率 $\rho_{xx}$、Hall 电阻率 $\rho_{xy}$（kΩ 量级）📜Q。AB 振荡是 $\rho_{xx}(B)$ 上"大平滑背景 + 小纹波"，故需去背景锐化，两种手段：
- **方法一：直接减单调背景 → Δρxx**（Fig. 1e、Fig. 2a inset）：$\Delta\rho_{xx}(B)=\rho_{xx}(B)-\rho_{xx}^{\text{monotonic}}(B)$——单条 trace 扣掉平滑磁阻背景、保留振荡残差，**单位仍 kΩ**、振幅可直接读（50 K 时 ~0.4 kΩ、2 K 时 >1 kΩ）📜Q（Fig. 1e caption "Same as d but a monotonic background is subtracted for clarity"）。
- **方法二：对 B 二阶导 → d²ρxx/dB²**（Fig. 1f、Fig. 2b、Fig. 3c、SI Fig. 2c/3）：密度**二维图**要"对每个 n 逐条减背景"不切实际 → 改用二阶导（参数无关、整图一次算），去掉平滑背景且**不移动振荡极值**（二阶导 −cos 与 cos 极值同位；一阶导会移 π/2，见 A.6）——代价是**单位变 kΩ/T²**、振幅不再直接对应电阻 📜Q（Fig. 1f caption "Instead of subtracting the magnetoresistance for each n as in e, we plot d²ρxx(B)/dB² which removes the smooth background without shifting positions of oscillations' extrema"）。
- **FFT 分析**：对 $\rho_{xx}(B)$ 曲线（如 Fig. 2a 主图，**非** Δρxx 插图）做 FFT，分离 ΔB、ΔB/2、ΔB/3 三个频率 📜Q（Fig. 2b inset 横轴 f、单位 T⁻¹；正文 "ρxx(B) curves for a given T were Fourier-transformed"）。⚠️ **FFT 峰高 ≠ 路径概率/占比**：峰高 = 该谐波的干涉振幅 $A_p\propto 2|t_1||t_2|\,e^{-pL/L_\phi}\times N_p$（$N_p$ 为 p 畴回路数），把**本征透射 × 退相干因子 × 回路计数**三者卷积在一起且随 T 变；论文只用峰高的**位置**（→ 面积 A/2A/3A）与**随 T 的衰减斜率**（→ 周长 3λ/4λ/5λ），不反推路径权重。

> ⚠️ **背景的具体数值原文未给出（可复现性缺口）**：正文只给**相对量**——NP 处 ρxx "a few kOhms at liquid-helium T" 📜Q、AB 振幅 ">1 kOhm ≈ ~50% of zero-B resistivity"（2 K，Fig. 2a）📜Q。**未给**所减"单调背景"的绝对值、函数形式或拟合方法；Δρxx 的绝对值只能从图轴读图估算（📊F：50 K 时 Fig. 1d 的 ρxx ~ 4–8 kΩ、Fig. 1e 的 Δρxx ~ 0.4 kΩ），不可精确复现。可安全引用的是**相对关系**（振幅/零场电阻 ≈ 50%），而非背景的绝对 kΩ 值。

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

### 4.7 论文论证结构总览（三支柱 + 双轴墙/体判别）

> 全景版系统辨识：整篇论文的论点是一个——"mTBG 在 AB/BA 畴壁上有三角 1D 态网络，承载相干输运"。证据按"轴"分成三根支柱，缺一根都不构成完整可辨识。

| 支柱 | 轴 | 证什么 | 对应数据 |
|------|-----|--------|---------|
| **① 1D conductive network** | 密度/静电轴 | 墙**导电**（存在性） | Fig. 1c（D 开隙 + NP 金属性） |
| **② AB oscillations** | 磁轴 | 墙**相干**、沿**1D 回路** | Fig. 1d–f、Fig. 2 |
| **③ Minibands inside the gap** | 能量轴 | 墙网络**量子化**成 miniband 谱 | Fig. 3 |

**「AB vs SdH」是支柱②内部的判别，作用是"把振荡观测转化为对 1D 墙有利的证据"**：SdH = 2D 体（畴区）朗道量子化，AB = 1D 回路几何相位干涉——故"证 AB 非 SdH" ≈ "证振荡来自 1D 墙回路、而非 2D 体"。这一步不做，振荡反会被读成 2D 体证据、与 1D 墙主张矛盾。

**两条轴各自排除一次"体导电"（双轴墙/体判别）**：

```
密度轴（支柱①）:  D 开隙 + NP 金属性 → 导电不在体（畴）
磁轴（支柱②）:    振荡是 AB 非 SdH    → 振荡来自 1D 回路非 2D 体
                                         ↓
                             导电通路 = 1D 墙回路
```

**支柱②与③的分工与交叉验证**：

```
支柱② AB（磁轴）      → "墙上电子沿闭合三角回路相干干涉"（空间结构）
支柱③ Miniband（能量轴）→ "同一网络驻波量子化成离散 miniband"（能谱结构）
                          ↓ Δn→A = ΔB→A 两法反推同一三角回路面积
             主题: 三角 1D 墙网络承载相干 miniband 输运
```

**完整认定链**：存在性（①）→ 相干性 + 1D（②，含 AB-vs-SdH 与谐波几何）→ 谱量子化（③）→ 三根支柱合起来才是"1D 墙网络"的完整可辨识。

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

**AB 机制（几何相位 + 双路径干涉）**：电子波沿闭合环路分顺/逆时针两路传播后汇合，两路幅度 $t_1,t_2$，总透射是相干叠加：

$$T=|t_1+t_2|^2=\underbrace{|t_1|^2+|t_2|^2}_{\text{非相干背景}}+\underbrace{2|t_1||t_2|\cos\Delta\varphi}_{\text{干涉项}},\qquad \Delta\varphi=2\pi\frac{\Phi}{\Phi_0}+k(L_1-L_2)\quad(\Phi=BA,\ \Phi_0=h/e)$$

磁矢势只给纯几何相位差 $2\pi\Phi/\Phi_0$（动态相位 $k(L_1-L_2)$ 与 B 无关）。扫 B → $\cos(2\pi BA/\Phi_0)$ 振荡 → 电导 $G=(e^2/h)T$ 振荡 → $\rho_{xx}\propto1/G$ 振荡，**B 轴上等间距**周期 $\Delta B=\Phi_0/A$。**关键分解**：非相干项 $|t_1|^2+|t_2|^2$ = 平滑"单调背景"，干涉项 $2|t_1||t_2|\cos\Delta\varphi$ = 振荡残差 $\Delta\rho_{xx}$（正是 §3.3/Fig. 1e 减背景后的量）；"巨幅 ~50%"意味着 $|t_1|\approx|t_2|$、干涉项与背景同量级，即环路几乎串联起全部输运通道。磁场只当"相位旋钮"，**不要求形成朗道能级**，B→0 即已存在；唯一条件是相位相干 $L_\phi(T)>L$，振幅 $\propto e^{-L/L_\phi}$（见 A.5）。

**SdH 机制（朗道量子化）**：强场下态密度劈成离散朗道能级，扫 B 时费米能级逐个穿过（填充因子 $\nu=n\Phi_0/(gB)$ 过整数）→ 电阻振荡，**1/B 轴上等间距** $\Delta(1/B)=g/(n\Phi_0)$。存在两个硬条件：

1. **量子迁移条件** $\omega_c\tau=\mu B\gg1$：$\mu\approx10^4$ cm²/V·s（正文 📜Q）→ B=1 T 时 $\omega_c\tau\approx1$，B<1 T 朗道能级根本分不开；
2. **热条件** $\hbar\omega_c\gg k_BT$——LK 公式给 SdH 振幅的**热阻尼因子** $R_T=X/\sinh X$（$X=2\pi^2k_BT/\hbar\omega_c$）；高温极限 $X\gg1$ 时 $R_T\approx2X\,e^{-X}$（**指数抹平**）。物理起源：费米-狄拉克分布的热展宽（宽度 $k_BT$）把间距 $\hbar\omega_c$ 的朗道能级抹糊，$R_T$ 正是 $-\partial f/\partial E$ 的傅里叶变换在振荡频率处的取值。完整 LK 振幅 $\propto R_T\,R_D\,R_S\,\cos(2\pi(F/B+\gamma))$（$R_D=e^{-\pi/\omega_c\tau_q}$ 为 Dingle 无序因子、$R_S=\cos(\pi g m^*/2m_0)$ 为自旋因子）。

**三条观测逐一排除 SdH**：

| 观测（正文 📜Q） | SdH 的要求 | 排除结论 |
|------|-----------|---------|
| 低场（~0.1–1 T）已振荡 | $\omega_c\tau=\mu B\approx1$（B=1 T）→ 朗道能级未分辨 | 低场无 SdH；AB 不需朗道量子化 |
| 振幅 ~50% ρxx | SdH 是背景小纹波（几个 %） | 50% = 干涉开关主输运通道 = AB |
| 持续到 120 K | $k_BT\approx10$ meV；B=1 T 时 $\hbar\omega_c\approx12$ meV（m*≈0.01 m₀）→ $X\approx17.5$，$R_T\sim e^{-17}\sim10^{-7}$ | 120 K 时 SdH 热抹平到百万分之一；AB 只要 $L_\phi>L$ |

**内交叉验证（作者自证）**：AB 振荡"持续到数 T 处才被 SdH 淹没" 📜Q——同一器件里两机制先后登场，低场 AB、高场 SdH 长出来盖掉它。若低场振荡本身是 SdH，应低场最弱、高场最强，而非反过来。

**最干净判据（B vs 1/B）**：AB 在 **B 轴**等间距（恒 ΔB=0.48 T）；SdH 在 **1/B 轴**等间距，换算回 B 轴 $\Delta B\approx B^2\Delta(1/B)$ 随 B 变密。画 $1/B$ 轴看是否等间距即教科书级判别（本文未逐字写出，💭I 背景补充，支持其归属）。⚠️ **两个限定使此判据严谨**：① 须跨**宽 B 范围**——SdH 在窄窗口可"看起来近似 B 周期"（若本文振荡是 SdH，周期应从 1 T 处 0.48 T 拉长到 4 T 处 ~7.7 T；实测 0.48 T 恒定 → 确凿 B 周期）；② 论文还**直接并排观测到 SdH**——AB 振荡"数 T 处才被 SdH 淹没" 📜Q，低场 AB（B 周期）与高场 SdH（1/B 周期）同台并存，是并列对照而非单一"B 周期"推断。此外"随 B 周期"只是 AB 的**必要条件**（排除 SdH 作主振荡），完整的 AB 认定靠 §0 Step 3 表各行**合取**（低场/高温/振幅 + 谐波几何 + ΔB/Δn 面积互验）。

**（B, n）二维图里的三种"线"签名**（SI Fig. 3 是横轴 B、纵轴 n、z 轴 $d^2\rho_{xx}/dB^2$ 的密度图；区分三种机制各自的几何形态）：

| 机制 | 共振条件 → n(B) | （B, n）图中的形态 |
|------|----------------|-------------------|
| **SdH（Landau fan）** | $\nu=\dfrac{n\Phi_0}{gB}=N\Rightarrow n=\dfrac{g}{\Phi_0}N B$ | **过原点的直线扇**（电子侧正斜率、空穴侧负斜率，从电荷中性点/带边扇出）；仅高 B + 低温 |
| **AB（1D 网络）** | $j=\dfrac{L k_F}{2\pi}\pm\dfrac{AB}{\Phi_0}$，$k_F\propto n$ | **交叉斜线（X 形，正负斜率并存于同一密度区）**，来自 $\pm$（顺/逆时针环绕）；低 B 即现 |
| **2D FP/AB（√n 标度）** | $k_F=\sqrt{\pi n}$ → $n\propto(j\mp AB/\Phi_0)^2$ | **抛物线**（n 是 B 的二次函数，顶点在 $j=\pm AB/\Phi_0$） |

> 结论：**SdH 是"直线扇"（Landau fan），不是抛物线**；"正负斜率"对 SdH 是电子/空穴两侧的扇、对 AB 是同区交叉的 X。**抛物线是 2D（√n）FP/AB 的签名**，本文密度图中未见 → 反过来佐证输运是 1D 而非 2D（与 E10 的 √n vs n 判别同一条线索）。⚠️ 注意此图中 **AB 与 SdH 都给直线**，单凭"是直线"不足以区分二者，须靠**形态**（扇 vs 交叉 X）+ **B 范围**（低场 vs 高场）+ **T 依赖** + **B vs 1/B 周期**联合判别。

### A.4 密度周期与 miniband 能标（Δn=4/A 推导 + Δn→A 与 ΔB→A 互验）

**密度振荡与 AB 振荡的关系**：两者是**同一回路驻波条件**在不同轴上的表现——$j=L k_F/2\pi\pm AB/\Phi_0$。固定 n 扫 B → AB 项 $2\pi BA/\Phi_0$ 周期变化 → **B 周期**（$\Delta B=\Phi_0/A$）；固定 B 扫 n → $k_F(n)$ 项变化 → 逐条填 miniband → **n 周期**（$\Delta n=4/A$）。论文明说密度振荡"conceptually similar to Aharonov-Bohm oscillations"（"changes in the global interference pattern with varying n and, hence, the Fermi wavelength"）📜Q。

**Δn = 4/A 的推导（域计数）**：moiré 单胞面积 $A_{\text{moiré}}=\tfrac{\sqrt3}{2}\lambda^2=2A$（含 AB+BA 两畴，各面积 $A=\tfrac{\sqrt3}{4}\lambda^2$）→ 畴密度 = 2 畴/单胞 ÷ 2A = **1/A 畴/cm²**。填一个 miniband = 每畴加 **1 个电子 ×（2 自旋 × 2 谷）= 4 重简并** → $\Delta n=4\times(1/A)=4/A$ 📜Q（正文 "one extra electron per AB or BA domain, taking into account the fourfold degeneracy"）。

$$\Delta n=\frac{4}{A};\qquad \Delta E=\frac{h v_{DW}}{L}\ (L=3\lambda)$$

**Δn→A 与 ΔB→A 的具体互验过程**：
1. 从 Fig. 3a/b 读 $\Delta n$（ρxx 峰间距 / ρxy 零点间距）= $5\pm0.5\times10^{10}$ cm⁻² 📜Q。
2. $A=4/\Delta n=4/(5\times10^{10})=0.80\pm0.09\times10^{-10}$ cm²（误差：$4/5.5\sim0.73$、$4/4.5\sim0.89$）📜Q。
3. 对比 AB 主周期：$A=\Phi_0/\Delta B=4.1357\times10^{-11}/0.48=0.86\pm0.04\times10^{-10}$ cm² 📜Q。
4. 再对比结构：$A=\tfrac{\sqrt3}{4}\lambda^2=\tfrac{\sqrt3}{4}(140\ \text{nm})^2=0.85\times10^{-10}$ cm²（θ=0.10°）。三法在误差内一致 → 交叉验证同一三角回路面积 ✅。

**SI Note 5 讲了什么（miniband 谱的理论依据）**：① magic-angle 理论（两层只旋转、晶格不畸变）**不适用于** θ≪1°（应变大）；② 重构产生宏观 AB/BA 畴 + 原子级 sharp 畴壁（ref 10）；③ 层间偏置在畴区开隙 δ、在畴壁出 1D 态（ref 11）；④ 三角金属网络可用 ref 12（Efimkin & MacDonald 2018）模型描述为隙内"**次级 miniband 谱**"，miniband 在能量上近等间距（Fig. S6a）；⑤ 该模型**未计入带边费米速度变化**（Note 6）→ 偏离严格周期（Fig. S5c）；⑥ 实验表现：ρxx 在每个 miniband 间的 Dirac 中性点（DOS→0）出峰；ρxy 变号**比 ρxx 峰多一倍**（有效质量在中性点**和** van Hove 奇点都变号）📜Q——与 Fig. 3、SI Fig. 2 吻合。

ΔE=2ε=10 meV、L=3λ=420 nm → $v_{DW}=\Delta E\cdot L/h$=10 meV×420 nm/h≈10⁶ m/s ✓（正文）。

**Δn ∝ θ²（三器件定量验证）**：$\Delta n=4/A=16\theta^2/(\sqrt3 a^2)\propto\theta^2$。SI Note 2 三器件数据精确吻合：θ=0.10°→5、0.13°→8±1、0.24°→28±4（×10¹⁰ cm⁻²），比值 1:1.69:5.76 = θ² 之比 📜Q。

**miniband 数可定量计算**：$M\approx\delta/\varepsilon=\delta/(v_{DW}h/6\lambda)\approx50/5=10$，与 Fig. 3 实测 ~10 个吻合 📜Q（SI Note 6）。

**三机制对照（miniband ≠ 朗道/赝朗道）**：

| 机制 | 来源 | 间距 | ρxy |
|------|------|------|-----|
| 朗道能级 LL | 真磁场 B | $\hbar\omega_c\propto B$ | 单调阶梯、单侧恒号 |
| 赝朗道能级 | 应变赝磁场 | $\propto B_{ps}$ | 同上 |
| **本文 miniband** | **网络驻波（几何）** | $\varepsilon=h v_{DW}/L$ | **正负交替** |

**ρxy 正负震荡 vs LL 单调**：LL 电子区所有能级同属电子型带 → ρxy 恒正单调；miniband 每个含电子+空穴型态 → 载流子类型交替 → ρxy 正负交替（变号次数 = 2×ρxx 峰数：中性点 + van Hove 各变一次，SI Note 5）📜Q。

**miniband 周期 D 无关**：$\Delta n=4/A$、$n_j=4j/A$ 只含 λ 不含 D → Fig. 3a 峰位为竖直条纹不随 D 漂移；D 只定隙 δ（→M 个数）与可见度（阈值以上畴区绝缘充分，SI Note 2）📜Q。周期 D 无关 + Δn∝θ² + ρxy 正负交替三条合起来把"几何驻波量子化"钉死，排除静电（D）与朗道/赝朗道（B/应变）两种竞争解释 💭I（综合）。

**v_DW 的定义与提取**：$v_{DW}$ = 畴壁 1D 态的**群速度 = 费米速度**（线性色散 $E=\hbar v_{DW}k$ 的斜率，即电子沿墙传播的速度）——⚠️ 不是输运里 μE 的经典漂移速度，也不是 2D 石墨烯费米速度 $v$（虽然数值相近）。**提取链**（谱学反推，非第一性计算）：数 miniband（Fig. 3 隙内 ~10 个，δ=50 meV）→ $\varepsilon=\delta/M\approx5$ meV → 考虑 AB/BA 简并解除（谱加密一倍）$\Delta E=2\varepsilon=10$ meV → $v_{DW}=\Delta E\cdot L/h=2\varepsilon\cdot3\lambda/h\approx10^6$ m/s 📜Q。数值 ≈ 石墨烯 Dirac 速度 $v$ → 按 SI Note 6 判据（sharp 墙 $w<v/\sqrt{\gamma_1\delta}$ 时 $v_{DW}\approx v$；宽墙则 $v_{DW}$ 变小且现抛物线型非拓扑通道）**反证畴壁原子级 sharp** 📜Q。

### A.5 退相干与谐波衰减（AB 高温稳健）

**AB 振幅的退相干衰减 $e^{-L/L_\phi(T)}$（ref 27）及其推导**：

1. **相位相干长度** $L_\phi=v_F\tau_\phi$（$\tau_\phi$ 退相干时间，由非弹性散射 e-e/e-ph 决定）。相位被非弹性散射随机化是**泊松过程**（速率 $1/\tau_\phi$）：传播距离 $\ell$ 而不失相的概率 $P(\ell)=e^{-\ell/L_\phi}$。
2. **干涉项如何衰减**：AB 振荡来自两路（顺/逆时针）干涉项 $2|t_1||t_2|\cos\Delta\varphi$（见 A.3）。两路各走半环 $\sim L/2$，各带失相因子 $e^{-(L/2)/L_\phi}$，乘积得

$$2|t_1||t_2|\,e^{-L/L_\phi}\cos\Delta\varphi\quad\Rightarrow\quad\text{AB 振幅}\propto e^{-L/L_\phi}\ \ (L=\text{回路周长})$$

   第 $p$ 次谐波绕 $p$ 圈、周长 $pL$ → $e^{-pL/L_\phi}$，故高次谐波衰减更快。
3. **与数据对照**：L=3λ、4λ、5λ（1/2/3 个三角畴）→ 衰减斜率比 = 3λ:4λ:5λ = **1:4/3:5/3**，与 Fig. 2b 吻合 📜Q。$L_\phi(T)$ 随 T 升高而**变短**（非弹性散射增强），其具体幂次依赖退相干机制（e-e 散射 2D 扩散常给 $L_\phi\propto T^{-1/2}$ 等 💭I），论文未导出、只作现象学参量。

**退相干的物理（为什么非弹性散射会失相）**：相位相干丢失 = 电子的"走哪条路（which-path）"信息泄漏进环境。**非弹性散射**（e-e、e-ph）交换能量——① 电子能量/波矢改变 → 两路相位演化不同步 → 汇合时无固定相位差；② 更深层：散射出的声子/另一个电子**携带了"哪条路"的信息** → 电子与环境纠缠 → 对环境求迹后干涉项消失（which-path / 量子测量图景）。**弹性散射不失相**（静态无序只改方向、无能量交换、不漏路径信息）——这正是 AB 振荡能在扩散金属中存活的原因。$T=0$ 无声子、无 e-e 相空间 → $\tau_\phi\to\infty$；$T$↑ 散射增强 → $L_\phi\downarrow$ 💭I（背景）。

AB 振荡能活到 120 K，作者借 Brown–Zak 振荡（ref 30）类比解释：miniband 对 B 的**一致响应**（平均群速度变化）可抹平热展宽 💭I（背景）。

### A.6 高通滤波（Δρxx 减背景 vs d²ρ/dB²；为何二阶导不移极值）

**两种去背景的等价与差异**（对应 §3.3）：设 $\rho_{xx}(B)=\rho_{bg}(B)+A\cos(2\pi B/\Delta B+\varphi)$（$\rho_{bg}$ 为平滑单调背景）。

- **Δρxx（直接减背景）**：$\Delta\rho_{xx}=\rho_{xx}-\rho_{bg}=A\cos(\cdot)$——完整保留振荡**振幅与相位**（单位 kΩ），但需先拟合/选定背景 $\rho_{bg}(B)$，故适合单条 trace（Fig. 1e、2a inset）📜Q。
- **d²ρ/dB²（二阶导）**：$\dfrac{d^2\rho_{xx}}{dB^2}=\rho_{bg}''-A\!\left(\dfrac{2\pi}{\Delta B}\right)^2\cos(\cdot)$——只要 $\rho_{bg}''$ 小/平滑，就正比于 $-\cos$。**关键**：二阶导仍是 $\cos$ 而非 $\sin$，故极值与原始 $\rho_{xx}$ 振荡**同位**（不移动 extrema）；一阶导 $\propto-\sin$ 会把极值移 π/2（极值变零点）。这就是 Fig. 1f caption 强调 "without shifting positions of oscillations' extrema" 的原因 📜Q。代价：振幅被放大 $(2\pi/\Delta B)^2$ 倍且单位变 kΩ/T²，**不再直接对应电阻**。

**与 E10 的对照**：E10 用 $dG/dn$（对密度一阶导）锐化 FP 纹波；本文用 $d^2\rho/dB^2$（对磁场二阶导）锐化 AB 纹波——同一"微分=高通滤波"思想在磁轴上的版本。控制论语言：$\rho_{xx}$ 是原始输出，$\Delta\rho_{xx}$ / $d^2\rho_{xx}/dB^2$ 是两种高通预处理观测（延续 15_case_study §4.1 洞察）💭I。

### A.7 AB 电磁相位 vs Berry/valley 相位（与堆垛 / valley Chern 的关系）

> 澄清一个易混点：电子绕环一圈积累的是**两套独立的相位**，别混在一起。本节为教科书背景 💭I。

| 相位 | 来源 | 表达式 | 决定因素 | 是否依赖堆垛 / $C_v$ |
|------|------|--------|---------|---------------------|
| **AB（电磁规范）相位** | 磁矢势 $\mathbf A_{em}$ | $2\pi\dfrac{BA}{h/e}$ | 磁通 + 电荷 $e$ | **否**（普适） |
| **Berry（能带几何）相位** | 布洛赫波包 $\mathbf A_{Berry}$ | $\oint\mathbf A_{Berry}\cdot d\mathbf k=2\pi C_v$ | valley Chern 数 | **是** |

**结论**：① AB 振荡的**周期** $\Delta B=h/(eA)$ 来自电磁相位，是**拓扑无关的电荷-$e$ 普适效应**——即便一个无拓扑的普通金属环也有 $h/e$ 周期；② valley Chern 数的作用是**间接的、且在本系统的前一步**——(i) **让墙态存在**（AB/BA 有相反 $C_v=\pm2$ → 畴壁处 gap 反号 → 束缚 in-gap 1D 态）；(ii) **定墙态性质**（helical：K/K′ 反向、每侧 4 条=2 自旋×2 谷 → 决定"有无两条可干涉路径"与振幅）；(iii) **至多加一个常数 Berry 偏移**（移 $\cos$ 相位、**不改周期**）。

**实验自证**：论文用 $\Phi_0=h/e$ 反推 $A=0.86\times10^{-10}$ cm²，与 $\Delta n=4/A\to A=0.80$、$\theta\to\lambda=140$ nm 三方自洽 📜Q——若混入改变周期的 Berry/valley 相位，面积反推就对不上 → 证实这是**电荷-$e$ 电磁相位**。

**换堆垛（tMBG 的 ABC/ABA vs mTBG 的 AB/BA）会怎样**：

| 维度 | AB/BA（mTBG，Bernal 双层） | ABC/ABA（tMBG，rhombohedral 三层） |
|------|---------------------------|-----------------------------------|
| valley Chern 数 | $C_v=\pm2$ | $C_v=\pm3$ |
| AB 电磁周期 $\Delta B=h/eA$ | **相同** | **相同** |
| Berry 相位偏移 | $2\pi C_v$ 常数 | **不同常数**（只移相位不改周期） |
| 墙态通道数 / 手征性 | 4 条/侧，helical | 可能不同（$C_v$ 失配量不同 → 通道数/谷-手征结构变） |
| 振幅 / 可见度 | 由 $v_{DW}$、$L_\phi$、谷间散射定 | 可能不同 |

**一句话**：AB 振荡是拓扑无关的电荷-$e$ 效应——堆垛从 AB/BA 换成 ABC/ABA，环绕磁通的电磁相位 $2\pi BA/(h/e)$ 与周期**不变**；变的只是 valley Chern 数 $(\pm2\to\pm3)$ 所决定的**墙态结构**（存在性、通道数、helical vs chiral、振幅）与一个**常数 Berry 相位偏移**。valley Chern number 决定"这个环能否干净形成、有几条通道在干涉"，而不决定"每条通道绕一圈积累多少 AB 相位"。

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
| 2026-08-29 | §3.3 补全两种去背景手段：Δρxx（直接减单调背景，单位 kΩ、保振幅相位，用于单 trace Fig. 1e/2a-inset）vs d²ρxx/dB²（二阶导，单位 kΩ/T²、整图一次算，用于密度二维图 Fig. 1f 等）；A.6 补"为何二阶导不移极值（−cos 与 cos 同位，一阶导移 π/2）"的数学说明；§3.3 加 ⚠️ 注：背景具体数值/拟合方法原文未给（仅"a few kΩ"与"~50% zero-B"相对量），Δρxx 绝对值不可复现 |
| 2026-08-29 | A.3「AB 机制」扩为双路径干涉推导（$T=|t_1+t_2|^2$=非相干背景+干涉项；干涉项=Δρxx；"~50%"⇒|t₁|≈|t₂|）；新增 A.7「AB 电磁相位 vs Berry/valley 相位」辨析：AB 周期 $h/e$ 拓扑无关、$C_v$ 只决定墙态存在/性质/常数偏移，附 AB/BA($C_v=\pm2$) vs ABC/ABA($C_v=\pm3$) 对照表 |
| 2026-08-29 | A.3「最干净判据（B vs 1/B）」补两个限定：① 须宽 B 范围（SdH 窄窗可伪 B 周期；若本文是 SdH 周期应从 1 T 处 0.48 T→4 T 处 ~7.7 T，实测恒定 → B 周期）；② 论文并排观测到 SdH（"数 T 处被淹没"📜Q）= 并列对照；并强调"随 B 周期"只是必要条件，AB 认定靠 Step 3 各行合取 |
| 2026-08-29 | A.3 补「（B,n）二维图三种线签名」表：SdH=Landau fan（n∝B 过原点直线扇，非抛物线）；AB(1D)=交叉斜线 X；2D FP/AB(√n)=抛物线 n∝(j∓AB/Φ₀)²；并警示 AB 与 SdH 都给直线、须靠形态+B 范围+T+周期联合判别 |
| 2026-08-29 | A.3「热条件」补完整 LK 公式（$R_T=X/\sinh X$、高温极限 $2Xe^{-X}$、$R_D/R_S$ 因子、$-∂f/∂E$ 傅里叶变换物理起源）；A.5 补 $e^{-L/L_\phi}$ 退相干衰减推导（泊松失相 $e^{-\ell/L_\phi}$ + 两路乘积 + 谐波 $e^{-pL/L_\phi}$ → 1:4/3:5/3） |
| 2026-08-29 | A.5 补"为什么非弹性散射失相"（which-path 泄漏/能量交换 vs 弹性散射不失相）；§3.3 FFT 分析补 ⚠️：FFT 峰高 = 干涉振幅（本征透射×退相干×回路计数三者卷积，随 T 变），**不是**路径概率/占比，论文只取峰位置(→面积)与 T 衰减斜率(→周长) |
| 2026-08-29 | 新增 §4.7「论文论证结构总览」：三支柱（①墙导电②AB 相干③miniband 量子化）+ 双轴墙/体判别（密度轴/磁轴各排除一次体导电）+ 支柱②③交叉验证（Δn→A=ΔB→A）+ 完整认定链 |
| 2026-08-29 | A.4 扩写：密度振荡↔AB 振荡"同一驻波条件不同轴"关系；Δn=4/A 域计数推导（畴密度 1/A × 4 重简并）；Δn→A=0.80 与 ΔB→A=0.86 与 λ→A=0.85 三法互验步骤；SI Note 5 内容（Efimkin-MacDonald 模型 miniband 谱 + ρxy 变号比 ρxx 峰多一倍） |
| 2026-08-29 | A.4 再补：Δn∝θ² 三器件验证（1:1.69:5.76 = θ² 比）；M≈δ/ε 定量计算；LL/赝朗道/miniband 三机制对照表；ρxy 正负交替 vs LL 单调（电子/空穴型交替）；miniband 周期 D 无关（几何 vs 静电判别）；v_DW 定义（群速度=费米速度，非经典漂移速度）+ 谱学提取链（数 miniband→ε→ΔE→v_DW≈10⁶ m/s→sharp 墙反证） |
