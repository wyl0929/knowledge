<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-20 17:32:56
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-31 22:40:00
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/experiments/paper_review_E10_rickhaus2018_nanolett.md
 * @Description  : E10: Rickhaus et al. 2018 — mTBG 拓扑网络输运 FP+AB 振荡（2026-08-31 按 4 块模板重写：判别表置顶 + 前提限定 + 三层分离）
-->

# Paper Review: Rickhaus et al. (2018) — mTBG 拓扑网络输运的 FP+AB 振荡

| 字段 | 内容 |
|------|------|
| **编号** | E10 |
| **标题** | Transport Through a Network of Topological Channels in Twisted Bilayer Graphene |
| **作者** | Peter Rickhaus, John Wallbank, Sergey Slizovskiy, Riccardo Pisoni, Hiske Overweg, Yongjin Lee, Marius Eich, Ming-Hao Liu, Kenji Watanabe, Takashi Taniguchi, Thomas Ihn, Klaus Ensslin |
| **期刊** | Nano Letters 18, 6725–6730 (2018) |
| **DOI** | 10.1021/acs.nanolett.8b02387 |
| **arXiv** | 1802.07317 ⚠️ 正文未出现（外部书目来源，非本文验证） |
| **类型** | 实验 — 低温输运 |
| **课题组** | Ensslin group (ETH Zurich) |
| **PDF / SI** | ✅ reference/pdfs/Rickhaus 等 - 2018 - ...pdf（正文 6 页 + SI 19 页） |
| **DW.bib** | ✅ `rickhaus_transport_2018` |
| **精读日期** | 2026-08-06（初读）→ 2026-08-19（三问框架 + QC）→ 2026-08-28（重写）→ 2026-08-31（4 块模板重写） |

> **共享知识引用**：通用推导已剥离到 `note/shared/physics/` —— 静电学 `[PHY-GATE]`、FP/维度判据 `[PHY-FP]`、Hofstadter `[PHY-HOF]`、AB 干涉 `[PHY-AB]`、AB vs SdH 判别 `[PHY-SDH]`、Bohr-Sommerfeld 统一 `[PHY-MB]`、QVH 术语 `[PHY-BERRY]`。本 review 只写"本文代入"后的数值。

---

## TL;DR

**本文想解决的问题**：θ≈0.42° 的 mTBG 在大位移场 D 下，输运是否由 AB/BA 畴壁的**拓扑保护 1D 通道网络**承载（而非 2D 体态）？

**主结果**：顶栅 FP 腔内同时观测到**密度调谐的 FP 振荡**与**磁场调谐的 AB 振荡**，且 **0–8 T 持续存在**（8 T 时磁长 9 nm ≪ 任何器件尺寸）📜Q。周期反推：ΔB=0.37 T → A=11200 nm²；Δn_in=4.7×10¹⁰ cm⁻² → L_tot≈870 nm → 等效矩形 **408×27 nm²** ≈ 腔长 400 nm × λ√3/2=29 nm（相邻拓扑通道最短距离）→ 轨迹**环绕一排 AB/BA 区域**。

**结论/意义**：体电流沿拓扑保护 1D 通道流动；作者保守措辞 "good indications that electrons form coherent paths within a network of topological channels"、"hints at topological protection" 📜Q。这是 mTBG 畴壁网络**器件尺度相干输运的首个证据**（与 Huang 2018 的 STM 局域成像互补）。

---

## 1. 系统辨识导览（判别表为全文唯一权威）

**黑箱三要素**：`{Vtg, Vbg, B | G, dG/dn_in | 1D 拓扑网络通道}`。

**四层变量图**（符号层一次钉死）：

| 层 | Rickhaus 2018 实例 |
|----|--------------------|
| **L1 旋钮 u** | $V_{tg}$（顶栅 g1/g2/g3）、$V_{bg}$（石墨背栅）、$B$（0–8 T）；$T$ 固定 1.5 K（非扫描旋钮） |
| **L2 导出量 x₁** | $n_{in}$、$n_{out}$、$D$（栅压换算见 §3.2）、$\Delta$（$D$→$\Delta$，SI Eq. 10） |
| **L3 模型量 x₂** | $E_F$（$n$→$E_F$）、$k_F/k_x$（$n_{1D}$→$k_F$）、轨迹几何 $(A,L_{tot},\tilde L,\tilde w)$ |
| **固定参数（非旋钮）** | θ=0.42°（0.5° 目标）、λ=33 nm、d_top/d_bottom=27/45 nm、εhBN=3.2、L=200/300/400 nm、W=4.6 μm、a=0.246 nm、γ₁≈0.4 eV、d_m=0.33 nm、Λ≈1 |
| **反推量 θ̂** | A=11200 nm²（ΔB）、L_tot≈870 nm（Δn_in）、L̃×w̃=408×27 nm²、n₂≈0.8×10¹² cm⁻²、θ=0.42°（n₂ 标定） |
| **L4 观测量 y** | $G=dI/dV$（两端子 c1–c2）、$dG/dn_{in}$（数值导数）、$G(n_{in})$ 背景 |

> 与 E12 符号差异：本文测**电导** $G$、$dG/dn_{in}$ 且密度分 $n_{in}/n_{out}$；E12 测**电阻率** $\rho_{xx},\rho_{xy}$、$d^2\rho/dB^2$ 且 $n$ 不分。

**可辨识性判别表**（唯一权威；机制判据细节见 [PHY-*]）：

| 判别 | 判据（数据） | 排除谁 | 确立谁 |
|------|-------------|--------|--------|
| **1D vs 2D** | FP 在 $n_{in}$ 上**等间距**（$k_F\propto n_{1D}\propto n_{in}$，1D）vs $\sqrt{n}$ 抛物线（2D）——摘要 "periodic in n (rather than √n)"，正文 "parabolic lines ... not observed" 📜Q | 2D 体态 | 1D 通道——推导见 [PHY-FP] |
| **AB vs 充电** | n-B 图**正负斜率并存**（Eq. 2 的 $\pm A$ 项 = 顺/逆时针环绕）vs 充电单斜率（refs 35,36 判据）📜Q | 单电子充电 | AB 干涉——交叉斜线见 [PHY-SDH] §4 |
| **QVH vs QH** | 振荡**从 QH 区连续到 B=0**（0→±3 T 连续，单 trace 到 8 T）→ 通道在 B=0 已存在 📜Q | QH 边缘通道（需 B） | QVH 畴壁态（B=0 已存在）——辨析见 [PHY-BERRY] |
| （弱）**固定通道数** | 背景 $G(n_{in})$ 平缓 → 通道数不随 $n_{in}$ 变 📜Q（Fig. 3C） | 随 $n_{in}$ 变化的体导电 | 固定数量 1D 通道 |

> **主结果 ↔ 判别表对应**：
> - 主结果① FP+AB 并存且 0–8 T 持续 ← {1D vs 2D, AB vs 充电, QVH vs QH}
> - 主结果② 路径几何 408×27 nm²（环绕一排 AB/BA）← {ΔB→A 与 Δn_in→L_tot 联合反推 + L/D 旋钮验证（§4.5）}
> - （前提）拓扑网络存在 ← 引言四步 + 判别 QVH vs QH
>
> **"1D 拓扑通道"是分层排除，非一步证成**：① 维度（1D vs 2D）；② 机制（AB vs 充电）；③ 拓扑性质（QVH vs QH）；④ 通道数（G 平缓，弱）。作者全程用 "good indications"、"hints at"（一致而非证明）📜Q。

> **[前提与限定]**（判别结论的适用范围）：
> - **噪声/扰动**：振荡振幅仅 **1–2%**（第二器件 5%）📜Q（SI S7）；Fig. 3B 已去平滑背景（"a smoothened background has been removed"）；无序与气泡（300 nm 栅倾斜 → 有效腔长偏小）📜Q（SI S1）；谷间散射来源未知（边缘粗糙度/杂质）📜Q（SI S7）；温度固定 1.5 K —— **无 T 依赖数据**（退相干 $L_\phi$ 未表征）。
> - **判别性扫轴**：固定 B 扫 $n_{in}$（FP）/ 固定 $n_{in}$ 扫 B（AB）/ 旋钮验证 L=200/300/400 nm 与 D 递减（§4.5）；B 上限 8 T（cryostat 最大场，"presumably beyond" 未测）📜Q。
> - **候选集 M 边界**：{2D 体态 FP, 单电子充电, QH 边缘通道, 其他轨迹几何} —— "环绕一排 AB/BA 的 1D 网络轨迹"在该集内唯一幸存；**非拓扑替代机制未完全排除**（正文只说 "hints at"）💭I；**网络 vs 独立通道未裁决**（原文未提出该区分，属后续 T9/T12/T15 之争）💭I。

三层标注：📜Q = 原文事实（附位置）｜💭I = 背景/推断。**不确定度（与证据分级正交）**：[±] 原文误差棒 / [读图] 读图估算 / [相对] 仅有相对量。⚠️ **本文全文数字无误差棒**（均以 =/≈ 给出，无 ±；ΔB=0.37 T 与 Δn_in 为作者自图提取）。所有数字经 pdftotext + grep 反向核对。

---

## 2. 结果与机制（按论文自身论证结构：网络 / 负对照 / 主发现）

### 2.1 网络图像与 QVH/QH 辨析

网络形成四步 📜Q（引言）：① tBLG 中 AB/BA 堆垛交替 → moiré 超晶格；② 大位移场 D 使 AB/BA 区开隙并耗尽 → 畴壁态成网；③ 网络源于 AB/BA 区 **valley Chern 数不同**；④ 拓扑电流主要在**体内**流动 → 对边缘制备缺陷不敏感（对比 InAs/GaSb）。

**扭角条件**（重要修正）📜Q（引言）：早期理论要求 θ<0.3°（ref 17 San-Jose & Prada）；**本文 θ≈0.42° 仍观测到网络输运** —— 弹性形变稳定并扩大 AB/BA 区域、放宽条件（ref 18 Andjelkovic）。

> **QVH 畴壁态 ≠ QH 边缘通道**（完整辨析表见 [PHY-BERRY]）："valley Chern 数不同"给出 QVH 畴壁态（B=0 已存在、谷锁定反向传播），不是文中所排除的 QH edge channels（需 B 的朗道能级）。文中 "not linked to the existence of Quantum Hall edge channels" 的逻辑 = 振荡从 QH 区连续到 B=0 📜Q。

### 2.2 Regime I（常规 n-p-n FP，负对照）

- 条件：$n_{in}\ll0$、$n_{out}\gg0$（双极 n-p-n）📜Q（Fig. 2A caption）；"displacement field can but does not have to be large" 📜Q。
- 2D FP 条件 $2L=j\cdot2\pi/k_F$、$k_F\approx\sqrt{n\pi}$ 📜Q；提取有效腔长 **550 nm** > 设计 400 nm（腔-体平滑过渡，ref 33 SI）📜Q。
- 振荡在 **B>0.5 T 消失**（Eq. 1: $2R_c=2\hbar k_F/eB>L$；SI S4: $R_c<2L$ 开始减弱、$R_c=L/2$ 完全消失）📜Q。

> ⚠️ regime I 的 2D（√n）标度是"声明 + 间接论证"，**无直接"周期随 n_in 变化"数据图**：只有 ① 2D FP 条件陈述；② Fig. 2A inset FFT（对 n_out 平均）提取单一周期 → L=550 nm；③ Fig. S4 展示随 **B** 消失（非随 n_in 的周期变化）。√n vs n 的对比实际在 **n-B 平面**做（2D 抛物线未现、1D 斜线现）📜Q。

### 2.3 Regime II（拓扑网络主导，主发现）

- 条件：小 $n_{in}<n_2$ + 大 $D$（AB/BA 被耗尽、超晶格对称性影响 B 行为）📜Q。
- n-B 图出现**交叉斜线共振**（正负斜率并存）📜Q（Fig. 3A）。
- **论证逻辑链**（正文 "In other two-dimensional systems..." 一段，7 步）：
  1. 现象：regime II 交叉斜线共振（Fig. 3A）；
  2. 候选：高场 B&n 共振在 2D 体系已知两种起源——单电子充电 vs AB 干涉（refs 35,36）；
  3. 判据：n-B 平面斜率符号——充电单斜率；AB 双斜率（Eq. 2 的 $\pm A$ 项 = 顺/逆时针环绕）；
  4. 判定：正负斜率并存 → 排除充电、确立 AB；
  5. 再排除：共振从 QH 区连续到零场 → 不绑定 QH 边缘通道；
  6. 强结论：AB 干涉持续到 B=0 → 载流子在所有 B 已在 1D 通道中；
  7. 弱佐证：$G(n_{in})$ 平缓 → 固定数量 1D 通道。
- 细节 📜Q：$2R_c\ge L$ 当 $B\lesssim0.4$ T —— 共振在 0.4 T 处既不消失也不突变；单 trace 到 **8 T**（"presumably beyond"，cryostat 上限）；8 T 时磁长 9 nm ≪ 器件尺寸。

### 2.4 两条维度判据（结论，推导见 [PHY-FP]）

1. **密度标度**：FP 在 $n_{in}$ 上等间距（1D）而非 √n（2D）📜Q。
2. **磁场标度**：振荡 8 T 仍持续 → 主导路径不是二维体轨道（2D 轨道在 $2R_c<L$ 消失），而是轨迹不受磁场影响的 1D 通道 📜Q。

---

## 3. 实验方法

### 3.1 器件

层状结构（从下到上）📜Q（SI S1/S2）：p 掺杂硅片 → **石墨薄片（背栅 BG，兼屏蔽 SiO₂ 陷阱电荷）** → 底 hBN（45 nm）→ tBLG（单片连续）→ 顶 hBN（27 nm）→ Cr/Au 顶栅 g1/g2/g3 + 接触 c1–c4。顶栅定义 3 个腔 L=200/300/400 nm、W=4.6 μm（L≪W → 多并行通道同干涉条件）；g5/g6 未用。制备：撕裂-旋转-再拾取（θ 目标 0.5°；低温工艺防自发旋转）；⚠️ PC/PDMS 是转移聚合物，不在最终器件里；300 nm 栅倾斜 → 有效腔长偏小 📜Q（SI S1）。

### 3.2 静电学（推导见 [PHY-GATE]）

三条核心关系（正文原式）📜Q：

$$n_{in}=\frac{C_{tg}V_{tg}+C_{bg}V_{bg}}{e},\qquad C=\frac{\varepsilon_0\varepsilon_{hBN}}{d},\qquad D=\frac{D_{top}-D_{bottom}}{2},\; D_{top}=\frac{\varepsilon_r V_{TG}}{d_{top}}$$

本文数值：$C_{tg}/e\approx6.55\times10^{11}$、$C_{bg}/e\approx3.93\times10^{11}$ cm⁻²/V（d_top=27、d_bottom=45 nm、εhBN=3.2）→ 系数比 $C_{tg}/C_{bg}=45/27=1.67$（顶栅更"劲"）📜Q。**两个正交旋钮**：共模 → $n_{in}$、差模 → $D$，双栅独立调 $n_{in}$ 与 $D$。$n_{in}\approx0$ 时 $D=-(e/\varepsilon_0)n_{out}$ → $D=-0.8$ V/nm 对应 $n_{out}\approx4.4\times10^{12}$ cm⁻²。⚠️ 近似：平行板（忽略边缘场）、无量子电容修正（"simple approximation"）📜Q。

### 3.3 测量

温度 1.5 K、标准低频锁相 📜Q；**两端子**：交流电压对称加在 c1–c2 测电流，c3/c4 悬空 📜Q（SI S1）。$G=dI/dV_{sd}$（锁相微分电导，低偏压线性区）；**$dG/dn_{in}$** = $G$ 对腔密度的数值导数（⚠️ 与 $G=dI/dV_{sd}$ 是两个不同导数）📜Q。三种画法用途：$G(n_{in})$ 看背景平缓（判固定通道数）；$dG/dn_{in}(n_{in},n_{out})$ 看 FP（Fig. 2A）；$dG/dn_{in}(B)$ 看 AB（Fig. 3B，已去平滑背景）。为何画 $dG/dn$ = 高通滤波锐化纹波（见 [PHY-AB] §4）。

---

## 4. 关键数据

> ⚠️ 本文全文数字无 ±（原文以 =/≈ 给出，无误差棒）；ΔB 与 Δn_in 为作者自图提取。

### 4.1 Moiré 标定（n₂ 的定义，物理见 [PHY-HOF]）

| 参数 | 值 | 证据 |
|------|-----|------|
| 第一带充满密度 $|n_2|$ | ≈ 0.8×10¹² cm⁻²（= 8×10¹¹ cm⁻²） | 📜Q（正文 + SI S3） |
| 物理含义 | 第二个 Dirac 点：第一 moiré 子带填满 = 每 MUC 8 电子（自旋×谷×层） | 📜Q（SI S3） |
| 来源 | Hofstadter butterfly（$D=0$ 磁导图 $dG/dn_{out}$ 增强；2nd DP 扇出卫星 LLs，B>0.5 T 分形） | 📜Q（SI S3） |
| 几何关系 | $A_{MUC}=\sin60°\cdot\lambda^2$、$\lambda=a/(2\sin(\theta/2))$、$a=0.246$ nm；$n_2=8/A_{MUC}$ → θ=0.42° | 📜Q（SI S3） |
| 文中作用 | 标记 regime II 边界（$|n_{in}|<|n_2|$）；Fig. 2A 红虚线 | 📜Q |

> **有没有 n₁？没有。** 下标 "2" = 第二个 Dirac 点；主 DP 在 n=0 不给下标。⚠️ 区分 $n_{1D}$（1D 通道密度，SI Eq. 4）——不是 "n₁"。
> ⚠️ SI 文本指数笔误：SI S3 正文写 "n2 ≈ −0.8 × 10¹¹ cm⁻²"，指数应为 10¹²（与 Fig. S3B caption "n2 = −8 × 10¹¹ cm⁻²" 及正文 0.8×10¹² 一致）。
> **n_1D 换算**（SI Eq. 4）：$n_{1D}=n_{in}\cdot\lambda/(2\sqrt3)$（$N_{ch}=2\sqrt3/\lambda$，三方向网络）。**g=4 而非 8 的原因**：只有一个子带对 FP 主导贡献（SI: "Since only one of the bands leads to a dominant contribution to the FP resonances (see Fig. S10), the degeneracy is g = 4 (not g = 8)"）📜Q。

### 4.2 Regime I（数据）

| 参数 | 值 | 证据 |
|------|-----|------|
| 有效腔长 | 550 nm（FFT 提取，> 设计 400 nm，腔-体平滑过渡） | 📜Q |
| 消失场 | B > 0.5 T（Fig. S4: $R_c<2L$ 减弱、$R_c=L/2$ 消失） | 📜Q |

### 4.3 Regime II（数据）

| 参数 | 值 | 证据 |
|------|-----|------|
| 交叉斜线 | 正负斜率并存，0→±3 T 连续 | 📜Q（Fig. 3A） |
| 2R_c=L 拐点 | B≲0.4 T（无消失、无突变） | 📜Q（正文） |
| 持续上限 | 8 T（cryostat 最大场，"presumably beyond"） | 📜Q |
| 振荡振幅 | **1–2%**（主器件 W=4.7 μm；第二器件 W=2 μm 为 5%） | 📜Q（SI S7） |
| 背景 G(n_in) | 平缓（固定数量 1D 通道） | 📜Q（Fig. 3C） |

### 4.4 周期 → 几何（提取链）

| 参数 | 值 | 证据 |
|------|-----|------|
| ΔB | 0.37 T（作者自 Fig. 3B 提取，无 ±） | 📜Q |
| A = φ₀/ΔB | 11200 nm² | 📜Q |
| moiré 单胞面积 | ≈950 nm²（A 大 1 个量级） | 📜Q |
| 顶栅腔面积 L·W | ≈2×10⁶ nm²（A 小 2 个量级）→ 路径在**腔内体区** | 📜Q |
| Δn_in | 4.7×10¹⁰ cm⁻² | 📜Q |
| L_tot = 2π/Δk_F = 8√3/(λΔn_in) | ≈870 nm | 📜Q |
| 等效矩形 L̃×w̃ | 408 nm × 27 nm | 📜Q |
| 对照 | 408 ≈ 设计 L=400；27 ≈ λ√3/2 = 29（相邻拓扑通道最短距离）→ **环绕一排 AB/BA** | 📜Q |

> ⚠️ 正文同时承认 "also other trajectories are possible"（AA 节点三方向谷守恒散射，无需谷间散射也可成环）；但长而窄 + 连接两腔界面 + $\tilde A/L\approx\lambda\sqrt3/2$、$L_{tot}-2L\approx2\lambda$ → **只此一类轨迹与数据一致** 📜Q。这是可观测性论证（A、L_tot 两条独立约束唯一确定轨迹类型）。

**统一驻波条件**（Eq. 2，推导见 [PHY-MB] §3）：$j=L_{tot}\dfrac{k_F}{2\pi}\pm A\dfrac{B}{\phi_0}$ —— FP（第一项，密度调谐）与 AB（第二项，磁场调谐）是**同一驻波条件在两个轴上的表现**。观测策略：固定 B 扫 $n_{in}$ → FP（提取 $L_{tot}$）；固定 $n_{in}$ 扫 B → AB（提取 $A$）→ 联合反推路径几何（等效矩形 408×27 nm²）📜Q。

### 4.5 旋钮验证（L 依赖 + D 依赖 + 第二器件）

- **L 依赖（Fig. 4A）**：L=200/300/400 nm，L 减小 → ΔB 与 Δn_in 都变"慢"（面积与周长都减小）📜Q。实线 = 任意 L 的 BS 量化（SI Eq. 6–8：$\Delta B=\phi_0/(\sqrt3/2\lambda\cdot L/\cos\alpha)$；$\Delta n_{in}=4\sqrt3/[\lambda(L/\cos\alpha+c\,w)]$；斜率 $\Delta n_{in}/\Delta B=6/[\phi_0(1+w/L)]$；经验因子 **c=1.2** 计入腔边缘费米速度变慢）📜Q；虚线 = 设计 L。300 nm 栅实测偏短（栅倾斜，SI S1）。
- **D 依赖（Fig. 4B/C）**：D 减小 → 共振边界收窄 📜Q。机制链：$D\downarrow$ → AB/BA 能隙 $\Delta\downarrow$（Fig. S9）→ 区域在更低 $n_{in}$ 被填充 → 费米面失去 1D 特征（费米速度涂抹，Fig. S10B）→ 退相干、图案涂抹（Fig. S10C）。红点 = 计算的涂抹边界，与数据吻合 📜Q。定量：$D=-0.8$ V/nm → Δ≈150 meV、干涉持续 −2.5<E_F<2.5 meV；$D=-0.3$ V/nm → Δ≈50 meV、−1<E_F<1 meV 📜Q（SI S9）。
- **第二器件（SI S5，弱多器件验证）**：θ=0.22°、L=600 nm；交叉斜线图案定性一致；对角线 = "环绕一排 moiré"预期周期 📜Q。

### 4.6 证据链汇总

**证明 1D 输运**：① FP 密度等间距（非 √n）；② n-B 图斜线（vs 2D 抛物线）；③ 背景电导平缓（固定数量 1D 通道）📜Q。

**证明拓扑保护**：① 仅大 D + 小 $n_{in}$ 出现（符合 valley Hall 网络条件）；② 0–8 T 持续（轨迹不受洛伦兹力弯折——"time reversal symmetry cannot be broken or there is another protective symmetry at play"）；③ 轨道尺度介于单胞与整腔之间（体内网络闭环，非边缘态）；④ D 依赖边界与理论费米速度涂抹一致（Fig. 4C 红点）📜Q。

---

## 5. 主要结论

1. mTBG 顶栅腔中 FP+AB 振荡并存且 0–8 T 持续 → 载流子沿 1D 通道流动 📜Q。
2. ΔB→A 与 Δn_in→L_tot 反推的（主导）路径长≈腔长、宽≈λ√3/2 → 环绕一排 AB/BA 区域；不同栅长下同类回路 📜Q。
3. 振荡密度范围对 D 的依赖与 AB/BA 区开隙一致 📜Q。
4. **作者保守定性**："good indications that electrons form coherent paths within a network of topological channels"；"hints at topological protection" —— 一致而非证明 📜Q。

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 路径几何非唯一性 | "also other trajectories are possible"，实验只提取主导尺度 | 📜Q（正文） |
| 网络 vs 独立 1D 链未裁决 | 数据不能区分"连通网络"（T9）与"独立 1D 通道间干涉"（T12/TZM） | 💭I（原文未提出该区分） |
| 无实空间成像 | 路径几何无法直接验证 | 💭I |
| 振幅弱 | 仅 1–2%（第二器件 5%）——干涉是背景上的小纹波（对比 E12 的 ~50%） | 📜Q（SI S7） |
| 无温度依赖数据 | 恒温 1.5 K → 退相干 $L_\phi$、热稳定性未表征 | 📜Q（方法节） |
| B 上限 | 8 T（cryostat 最大场），"presumably beyond" 未测 | 📜Q（正文） |
| 谷间散射来源未知 | 闭合 K–K′ 环的反射机制未明（边缘粗糙度/杂质，SI 电阻模型估 ~10 条 1D 通道在工作） | 📜Q（SI S7） |
| 非拓扑替代机制 | 未完全排除（正文只说 "hints at topological protection"） | 💭I |

## 7. 与其他工作的关系

| 工作 | 关系 |
|------|------|
| San-Jose & Prada 2013 (ref 17) | 螺旋网络理论预言 + θ<0.3° 条件来源 📜Q |
| Andjelkovic et al. 2018 (ref 18) | 弹性形变稳定/扩大 AB/BA 区域 → 放宽 θ 条件的依据 📜Q |
| Huang 2018 (ref 19) | STM 局域实空间证据 —— 本文提供互补的器件尺度输运证据 📜Q |
| Young & Kim 2009 / Rickhaus 2015 等 (ref 24,25,33,34) | 单层/双层石墨烯 2D FP 传统 —— 本文 regime I 复现、regime II 对照 📜Q |
| Li 2016 (ref 15) / Lee 2017 (ref 16) | 零场 BLG 拓扑通道早期实现 📜Q |

> ⚠️ **Phase S 外部对标（非本文引用）**：T9 Efimkin & MacDonald 2018（网络模型）、T12 Tsim/Nam/Koshino 2020（独立 1D 链）、T15 De Beule 2020（散射统一）——均为**后续**理论对本文的重新解释 💭I（来自 cards.md，原文未引）。

## 8. 对后续研究的影响

- 证明 moiré 拓扑网络不仅在局域探针下可见，**在器件尺度也支持相干量子输运** 📜Q（摘要）。
- 网络在磁场与无序下稳定体干涉 → 2D 网络优于单边缘通道，可做复杂 valleytronic 操作 💭I。
- 避开物理边缘 → 更干净的拓扑保护环境 📜Q。
- 推动 AA 节点散射与谷守恒规则的定量建模 💭I。

## 9. 理论模型映射（n_in ↔ E_F，D ↔ Δ）

（供 tbplas / Kubo-Bastin 对照；原文 SI Eq. 9/10/11、Fig. S8–S10。）

### 9.1 连续模型哈密顿量（SI Eq. 9）

连续 (k·p) 模型（非晶格 tight-binding，但 on-site 概念对应）：

$$H_{T/B}=v\,\vec{p}\cdot\vec{\sigma}\pm\frac{\Delta}{2}\sigma_0$$

+/− 对应顶/底层，$\Delta$ 为栅诱导层间能移 📜Q（SI Eq. 9）→ **Δ 以 ±Δ/2 on-site 能移进入哈密顿量**（顶层 +Δ/2、底层 −Δ/2）。层间耦合 $H_{int}$：$w=110$ meV、$\Delta\vec K_j\approx4\pi\theta/(3a)(-\sin(2\pi j/3),\cos(2\pi j/3))$、$a=2.46$ Å；K′ 谷由 K 的 π 旋转得到 📜Q。能带结果（Fig. S8）：Δ=0/0.05/0.15 eV 对应 D=0/0.27/0.8 V/nm；三角电子/空穴口袋平边 → 六方向 1D 态；群速度可微斜（平行通道波函数重叠）📜Q。

### 9.2 D → Δ 的换算（SI Eq. 10）

$$\Delta=\frac{eD\,d_m}{1+\Lambda^2\ln\tfrac{4\gamma_1}{\Delta}}$$

（$d_m=0.33$ nm，$\Lambda\approx1$，$\gamma_1\approx0.4$ eV；实际画图用更精确公式，**屏蔽使 Δ 近似减半**）📜Q（SI S9A）。数值：$D=-0.3$ V/nm → Δ≈50 meV、$E_F\in[-1,1]$ meV；$D=-0.8$ V/nm → Δ≈150 meV、$E_F\in[-2.5,2.5]$ meV 📜Q。

### 9.3 n_in → 费米波矢（SI Eq. 11 + Fig. S10）

- 横向 DOS 投影 $\rho_{1D}(k_x)=\int\rho_{2D}(k_x,k_y)dk_y/(2\pi)$ → 两条快 1D 通道，主导通道在 $E_F$ 变号时切换（g=4 的依据）📜Q。
- 主导波矢 $k_x\sim n_{in}+c\cdot\text{sgn}(n)$（**线性**，S10B 虚线）📜Q；$|n_{in}|\gtrsim2\times10^{12}$ cm⁻²（Δ=150 meV）峰抹平 → FP 消失；n>2.5×10¹² 图案洗出，与实验一致 📜Q。
- 用 $k_x(n_{in})$ 画 FP 图案（Fig. S10C）→ **复现交叉斜线图案**（400 nm 栅）📜Q。

> **与实验量 G 的对应**（供 tbplas/Kubo 对照）：实验 $G=dI/dV$（两端子，器件量）与 Kubo-Bastin $\sigma_{xx},\sigma_{xy}$（体电导率，材料量）是同一线性响应的器件版 vs 材料版，$G=\sigma_{xx}\cdot W/L$（四端/扩散极限，需扣接触电阻；强场下两端子混入 $\sigma_{xy}$）。⚠️ 本文 FP/AB 振荡是**有限尺寸相干效应**，bulk $\sigma_{xx}$ 只给平滑背景——复现需有限器件透射（Landauer/Fisher-Lee）。变量对齐：$n\leftrightarrow E_F$（经 DOS 积分）、$D\leftrightarrow\Delta$（on-site）、$B$ 两者都有。💭I

---

## Phase S 补充：三问框架（引用式）

- **Q1（edge state 如何表征）**：低温输运（1.5 K 锁相），FP 振荡（$dG/dn_{in}$ 等间距，Δn_in=4.7×10¹⁰，1D 标度）+ AB 振荡（ΔB=0.37 T→A=11200 nm²，交叉斜线排除充电）+ 高场持续（0–8 T，轨迹不受洛伦兹力）+ 边-体区分（A 介于单胞 950 与腔 2×10⁶ nm² 之间 → 腔内环绕一排 AB/BA，非边缘态非 QH）——详见 §2.3/§4.4/§4.6。
- **Q2（理论如何解释）**：无新理论框架，理论贡献 = 既有模型应用 + 定量化（连续模型能带计算 SI Eq. 9/10 + BS 共振几何 Eq. 2）📜Q（作者贡献声明：J.W. 算能带、S.S./P.R. 推 SI Eq. 5/8、S.S. 算 Δ 与费米速度）——详见 §9。
- **Q3（理论↔实验对应）**：见下表（证据均 📜Q）：

| 理论预言 | 实验对应 |
|------|------|
| 大 D 耗尽 AB/BA → 网络态出现 | 振荡仅在小 $n_{in}$ + 大 D 出现（regime II） |
| 1D 通道 $k_F\propto n_{1D}$ → n 线性周期 | n-B 图斜线（非 2D 抛物线） |
| 环绕一排 AB/BA：$A\approx L\cdot\lambda\sqrt3/2$、$L_{tot}-2L\approx2\lambda$ | 提取 408×27 nm² ≈ 400 nm × 29 nm |
| 腔长 L 决定环路几何 | 三栅 L=200/300/400 nm 的 ΔB/Δn_in 与模型线一致（Fig. 4A） |
| D 减小 → gap 缩小 → 费米速度涂抹 → 退相干 | D 减小 → n_in 窗口收缩；红点与数据吻合（Fig. 4B/C） |
| regime I 为 2D 体 FP（$2R_c\gtrsim L$） | 550 nm、B>0.5 T 消失——负对照 |

> **增量价值**：与 E12（Xu 2019）分工——E10 是**首个** FP+AB 器件尺度观测（2018），独有"双轴同腔"（FP+AB 同一器件）+ 几何反推（408×27）+ 四旋钮验证（L/D/B/n）；但振幅弱（1–2% vs E12 ~50%）、无密度振荡/Hall 谱学、无温度依赖。report.md §2 用其 0–8 T 持续 + 维度判据与 QVH/QH（B=0）判别；§4 用其与 San-Jose→Efimkin 网络模型的映射链。与 E9（Huang 2018）实空间 LDOS 成像互补（输运 vs 局域探针）💭I。

---

## 反向核对 pass (2026-08-31, 重写时全量复核)

pdftotext 提取正文（6 页）+ SI（19 页）→ 逐项 grep 核对：

- ✅ 正文：θ=0.5°(目标)/0.42°(实测)/λ=33 nm/d_top=27/d_bottom=45/εhBN=3.2/L=200,300,400/W=4.6 μm/|n₂|≈0.8×10¹²/1.5 K/lock-in/550 nm/0.5 T/0.4 T/8 T/9 nm/ΔB=0.37 T/A=11200 nm²/950 nm²/2×10⁶ nm²/Δn_in=4.7×10¹⁰/L_tot≈870 nm/408 nm/27 nm/λ√3/2=29 nm/D=−1 V/nm/"good indications"/"hints at"/"presumably beyond" —— 全部在原文找到。
- ✅ SI：n_in 公式/SI Eq. 1–8（BS、ΔB、L_tot、Δn_in、斜率、c=1.2、α 取向）/Eq. 9（±Δ/2）/Eq. 10（d_m=0.33 nm、Λ≈1、γ₁≈0.4 eV，屏蔽减半）/Eq. 11（ρ_1D 投影）/n₂=8/MUC/g=4 依据/第二器件 θ=0.22°、L=600 nm/振幅 1–2% vs 5%/300 nm 栅倾斜/Δ=50、150 meV 与 E_F 窗口 —— 全部在原文找到。
- ⚠️ **全文数字无 ±**（原文以 =/≈ 给出，无误差棒）；ΔB=0.37 T、Δn_in 为作者自图提取 → 进 report 时须注明。
- ⚠️ SI 文本指数笔误："n2 ≈ −0.8 × 10¹¹ cm⁻²" 应为 10¹²（与 caption、正文一致）。
- ⚠️ 原文无：Efimkin & MacDonald 2018（理论引用实为 ref 17 San-Jose & Prada + ref 18 Andjelkovic）；arXiv 1802.07317（外部书目来源）。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-19 | 修正错误引用（Efimkin & MacDonald → San-Jose & Prada + Andjelkovic）；arXiv 标注外部来源；全文加 📜Q/💭I 证据分级；补三问框架 |
| 2026-08-28 | 补 SI（两端子、Eq. 9/10、n₂=8/MUC、Hofstadter、n₁D 换算）；补静电学量纲链、G/dG/dn、理论映射、regime 对比表、附录 A 推导 |
| 2026-08-28 | **整体重写**：去重 + 归位 + 分层（正文=事实/附录=推导/文末=过程记录） |
| 2026-08-31 | **4 块模板重写**：① 新增 §1 系统辨识导览（黑箱三要素 + 四层变量表含"固定参数/反推量" + 判别表置顶 + 主结果↔判别映射 + [前提与限定] 块）；② TL;DR 改问题句式；③ 通用推导剥离到 shared（[PHY-GATE]/[PHY-FP]/[PHY-HOF]，AB/SdH/BS/QVH 改锚点引用），附录 A 撤销；④ 补振幅 1–2%、第二器件 θ=0.22°、c=1.2、E_F 窗口等 SI 细节；⑤ 不确定度标注轴启用（全文无 ± 声明 + ΔB 自图提取标注）；⑥ 接口补"增量价值"行；⑦ 反向核对 pass 全量复核更新 |
