<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 22:02:11
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 22:02:14
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/experiments/paper_review_E10_rickhaus2018_nanolett.md
 * @Description  :
-->
<!--
 * @Author       : AI 精读 (research_onboarding_skill)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/note/experiments/paper_review_E10_rickhaus2018_nanolett.md
 * @Description  : E10: Rickhaus et al. 2018 — mTBG 拓扑网络输运 FP+AB 振荡
-->

# Paper Review: Rickhaus et al. (2018) — mTBG 拓扑网络输运的 FP+AB 振荡

| 字段 | 内容 |
|------|------|
| **编号** | E10 |
| **标题** | Transport Through a Network of Topological Channels in Twisted Bilayer Graphene |
| **作者** | Peter Rickhaus, John Wallbank, Sergey Slizovskiy, Riccardo Pisoni, Hiske Overweg, Yongjin Lee, Marius Eich, Ming-Hao Liu, Kenji Watanabe, Takashi Taniguchi, Thomas Ihn, Klaus Ensslin |
| **期刊** | Nano Letters 18, 6725–6730 (2018) |
| **DOI** | 10.1021/acs.nanolett.8b02387 |
| **arXiv** | 1802.07317 |
| **类型** | 实验 — 低温输运 |
| **课题组** | Ensslin group (ETH Zurich) |
| **PDF** | ✅ reference/pdfs/Rickhaus 等 - 2018 - ...pdf |
| **DW.bib** | ✅ `rickhaus_transport_2018` |
| **精读日期** | 2026-08-06 |
| **Phase S 重读** | 2026-08-19（三问框架 + QC 证据分级） |
| **arXiv** | 1802.07317 ⚠️ 正文未出现（外部书目来源，非本文验证） |

---

## 1. 核心贡献

首次在 mTBG 输运实验中同时观测到：

1. **Fabry-Pérot（FP）振荡** — 随载流子密度调谐 📜Q（摘要）
2. **Aharonov-Bohm（AB）振荡** — 随磁场调谐 📜Q（摘要）

最关键发现：振荡在 **0 到 8 T 垂直磁场下持续存在** 📜Q（摘要: "robust in magnetic fields ranging from 0 to 8 T"），与常规二维体系截然不同（二维体态轨迹被洛伦兹力弯折而抑制 FP 干涉）📜Q。从"磁场持续 + 密度线性间距"两点出发，证明体内电流主要沿**拓扑保护的一维通道**传播 📜Q（摘要: "The persistence in magnetic field and the linear spacing in density indicate that charge carriers in the bulk flow in topologically protected, one-dimensional channels"）。

## 2. 物理机制

### 2.1 拓扑网络的形成

1. tBLG 中 AB/BA 堆垛交替出现 → moiré 超晶格 📜Q（引言: "alternating regions of AB and BA stacking naturally exist and they form a superlattice"）
2. 外加大位移场 D → AB/BA 区域开隙并被耗尽 → 畴壁态形成网络 📜Q（引言: "The AB and BA regions can be depleted by applying large D and the emerging states form a network"）
3. 网络形成源于 AB/BA 堆垛区 valley Chern 数不同 📜Q（引言: "This network forms due to different valley Chern numbers in the AB and BA stacking regimes"）
4. 拓扑电流主要在**样品体内**流动 → 对边缘制备缺陷不敏感（对比 InAs/GaSb 系统）📜Q（引言）

### 2.2 扭角条件（重要修正）

- 早期理论：θ < 0.3° 才够 📜Q（引言，出自 ref [17] San-Jose & Prada）
- **本文实测：θ ≈ 0.42°（制备目标 0.5°）仍观察到此网络输运** — 晶格弹性形变稳定并扩大 AB/BA 区域，放宽了条件 📜Q（引言: "elastic deformations stabilize and enlarge the AB/BA regions and therefore relax this condition"，出自 ref [18] Andjelkovic et al. 2018）

### 2.3 为什么 FP 在磁场中持续存在？

- 常规二维 FP：需满足 $2R_c \gtrsim L$ 📜Q（Eq. 1），B↑ 轨道弯折 → 干涉消失；本文 regime I 满足此式且振荡在 B > 0.5 T 消失 📜Q（正文 + Fig. S4）
- 本文 regime II：振荡持续到至少 8 T 📜Q —— 8 T 时磁长 9 nm ≪ 任何器件尺寸 📜Q（正文）→ 主导路径不是二维体轨道，而是轨迹不受磁场影响的一维通道 📜Q
- 正文明示：振荡在 8 T 仍存在 → "时间反演对称不能被打破，或存在其他保护对称性" → 提示拓扑保护 📜Q（正文: "time reversal symmetry cannot be broken or that there is another protective symmetry at play. This hints at topological protection"）

### 2.4 为什么是 1D 而非 2D？

FP 共振在密度上呈**等间距 Δn**（线性周期）📜Q（摘要: "periodic in n (rather than √n)"）——1D 有 $k_F \propto n_{1D}$，共振 $L_{tot} = 2\pi/\Delta k_F$ 等间距；若为 2D 则 $k_F \propto \sqrt{n}$（非等间距，磁导图应为抛物线），实验未见 📜Q（正文: "would lead to parabolic lines in the magnetoconductance map, which is not observed"）

## 3. 实验方法

### 3.1 器件参数

| 参数 | 值 | 证据 |
|------|-----|------|
| 扭角（制备目标） | θ = 0.5° | 📜Q（正文: "twisted by θ = 0.5°"） |
| 扭角（Hofstadter 实测） | θ = 0.42° | 📜Q（正文 + Fig. 1 caption） |
| moiré 周期 λ | 33 nm | 📜Q（Fig. 1 caption + 正文） |
| hBN 厚度 | d_top = 27 nm, d_bottom = 45 nm | 📜Q（正文） |
| hBN 介电常数 | ε_hBN = 3.2 | 📜Q（正文） |
| 顶栅腔长 L | 200, 300, 400 nm | 📜Q（正文 + Fig. 4 caption） |
| 器件宽度 W | 4.6 μm（L ≪ W → 多并行通道同干涉条件） | 📜Q（正文） |

### 3.2 栅控关系

- $n_{in} = (C_{tg}V_{tg} + C_{bg}V_{bg})/e$，$C_{tg} = \varepsilon_0\varepsilon_{hBN}/d_{top}$，$C_{bg} = \varepsilon_0\varepsilon_{hBN}/d_{bottom}$ 📜Q（正文原式）
- $D \approx (D_{top} - D_{bottom})/2$，$D_{top} = \varepsilon_r V_{TG}/d_{top}$ 📜Q（正文: "we use the simple approximation"）

### 3.3 测量

- 温度：1.5 K 📜Q（正文 + Fig. 2 caption）
- 方法：标准低频**锁相**技术测电导 📜Q（正文: "standard low-frequency lock-in technique at 1.5 K"——lock-in 有原文）
- 数据：差分电导 $dG/dn_{in}(n_{in}, n_{out})$ 📜Q（Fig. 2 caption）
- 分析：FFT（含 2D FFT）提取周期与特征尺度 📜Q（Fig. 4A: "2D fast Fourier transform"）

## 4. 关键数据

### 4.1 Moiré 标定

| 参数 | 值 | 证据 |
|------|-----|------|
| 第一带充满密度 |n₂| | ≈ 0.8 × 10¹² cm⁻² | 📜Q（正文，Hofstadter butterfly Fig. S3 提取） |

### 4.2 Regime I（常规 n-p-n FP）

- 条件：n_in ≪ 0, n_out ≫ 0 📜Q（Fig. 2A caption）
- 提取有效腔长 550 nm（> 设计 400 nm，归因于腔-体平滑过渡）📜Q（正文，细节见 SI of ref [33]）
- 振荡在 B > 0.5 T 时消失（符合 2D 轨道弯折图像，Eq. 1 成立）📜Q（正文 + Fig. S4）

### 4.3 Regime II（拓扑网络主导）

- 条件：小 n_in（< |n₂|）+ 大 D（AB/BA 被耗尽、超晶格对称性影响 B 行为）📜Q（正文 + Fig. 2C）
- n-B 图出现交叉斜线共振（正负斜率并存 = 同一区域被顺/逆时针包围）📜Q（正文: "encircled both clock- and counterclockwise"）
- 共振从 QH 区连续演化到低场（0 到至少 ±3 T 连续，单独 trace 到 8 T）→ 与 QH 边缘通道无关 📜Q（正文 + Fig. 3A/B）
- 排除电子充电（Landau 能级充电）机制：正负斜率并存与充电效应不符 📜Q（正文引 ref [35] 判据）
- 背景电导平缓 → 参与输运的 1D 通道数量不随 n_in 变化 📜Q（Fig. 3C + 正文）

### 4.4 振荡周期提取（Bohr-Sommerfeld 条件 Eq. 2）

| 参数 | 值 | 证据 |
|------|-----|------|
| ΔB | 0.37 T（Fig. 3B 提取） | 📜Q |
| A = φ₀/ΔB | 11200 nm² | 📜Q |
| moiré 单胞面积 | ≈950 nm² | 📜Q |
| 顶栅腔面积 L·W | ≈2 × 10⁶ nm²（大 2 个量级） | 📜Q |
| Δn_in | 4.7 × 10¹⁰ cm⁻² | 📜Q |
| L_tot = 2π/Δk_F | ≈870 nm | 📜Q（n₁D 换算 $N_{ch} = 2/(\sqrt{3}\lambda)$，SI eq 4） |
| 等效长方形 | 408 nm × 27 nm | 📜Q（正文: "L̃ = 408 nm and width w̃ = 27 nm"） |
| 对照 | 408 nm ≈ 设计腔长 400 nm；27 nm ≈ λ√3/2 ≈ 29 nm（= 相邻拓扑通道最短距离） | 📜Q（正文） |

> 面积介于 moiré 单胞与顶栅腔之间 → 干涉路径位于腔内、环绕**一排 AB/BA 区域** 📜Q（正文: "This suggests that one row of AB/BA regions is encircled"）。⚠️ 正文同时承认 "also other trajectories are possible"（AA 节点三种谷守恒散射可能构成大而复杂路径）📜Q，但封闭轨迹的面积/长度约束 + 连接两腔界面要求 → 只此一类轨迹与数据一致 📜Q（正文: "this is the only kind of trajectory that is consistent"）。

### 4.5 顶栅长度依赖（Fig. 4A）

L = 200/300/400 nm 比较：L 减小 → 振荡在 ΔB 与 Δn_in 上变"慢"（即封闭面积与周长都减小）📜Q（正文: "become slower in both ΔB and Δnin for decreasing L"）；与"环绕一排 AB/BA 区域"模型（虚线=设计 L 预期，实线=任意 L 的 BS 量化）一致 📜Q（Fig. 4A caption）。

### 4.6 位移场依赖（Fig. 4B/C）

- D 减小 → 共振图案边界收窄（n_in 窗口收缩）📜Q（正文 + Fig. 4B: "The nin range where the interferences are observed is shrinking"）
- 机制：D 减小 → AB/BA 诱导 gap Δ 缩小（数值见 Fig. S9）→ 区域在更低 n_in 就被填充 → 费米面失去 1D 特征（费米速度向 1D 通道方向投影的涂抹，Fig. S10B）→ 退相干、干涉图案涂抹 📜Q（正文 + Fig. S10C）
- 理论预期的涂抹边界（红点）与实验数据良好吻合 📜Q（Fig. 4C caption）
- D = −1 V/nm 为 Fig. 4A 的固定条件 📜Q（Fig. 4A caption）

## 5. 主要结论

### 证明 1D 输运的证据链

1. FP 共振在密度上呈线性等间距（非 √n 标度）📜Q（摘要 + 正文）
2. n-B 图共振线形态与 1D 通道模型一致（斜线 vs 2D 抛物线）📜Q（正文）
3. 背景电导平缓 → 固定数量 1D 通道参与输运 📜Q（Fig. 3C + 正文）

### 证明拓扑保护的证据链

1. 仅在大 D + 小 n_in 条件下出现 → 符合 valley Hall 网络形成条件 📜Q
2. 振荡 0–8 T 持续 → 轨迹不受洛伦兹力弯折 📜Q
3. 轨道尺度介于单胞与整腔之间 → 体内网络闭环，非边缘态 📜Q
4. D 依赖边界与理论费米速度涂抹一致（红点 vs 数据）📜Q（Fig. 4C）

### 作者最终定性（保守表述）

"good indications that electrons form coherent paths within a network of topological channels" 📜Q（结论段原文）——注意作者用"good indications"而非"prove"。

## 6. 局限与未解决的问题

| 局限 | 说明 | 证据 |
|------|------|------|
| 路径几何非唯一性 | "also other trajectories are possible"，实验只提取主导尺度 | 📜Q（正文） |
| 网络 vs 独立 1D 链未裁决 | 本文数据不能区分"连通网络"（T9）与"独立 1D 通道间干涉"（T12/TZM）——卡片同款局限 | 💭I（推断，Phase S 外部对标；原文仅承认轨迹非唯一） |
| 无实空间成像 | 路径几何无法直接验证 | 💭I（推断） |
| B 上限 | 仅到 8 T（低温恒温器最大场），"presumably beyond" 未测 | 📜Q（正文: "8 T was the maximum available field in our cryostat"） |
| 非拓扑替代机制 | 未完全排除所有非拓扑解释 | 💭I（推断，正文仅说 "hints at topological protection"） |
| 节点散射矩阵 | AA 节点谷间散射率与无序的定量关系未知 | 💭I（推断，SI 讨论 Fig. S7B 路径但无定量） |

## 7. 与其他工作的关系

| 工作 | 关系 |
|------|------|
| San-Jose & Prada 2013 (ref [17]) | 螺旋网络理论预言 + θ < 0.3° 条件来源 📜Q（引言引 [17]） |
| Andjelkovic et al. 2018 (ref [18]) | 弹性形变稳定/扩大 AB/BA 区域 → 放宽 θ 条件的理论依据 📜Q（引言引 [18]） |
| Huang 2018 (ref [19]) | STM 局域实空间证据（网络形成"as recently shown by STM measurements"）— 本文提供互补输运证据 📜Q |
| Young & Kim 2009 / Rickhaus 2015 等 (ref [24,25,33,34]) | 单层/双层石墨烯 2D FP 干涉传统 — 本文 regime I 复现、regime II 对照 📜Q |
| Li 2016 (ref [15]) / Lee 2017 (ref [16]) | 零场 BLG 拓扑通道的早期实现 📜Q（引言引 [15,16]） |

> ⚠️ **Phase S 外部对标（非本文引用）**：T9 Efimkin & MacDonald 2018 网络模型、T12 Tsim/Nam/Koshino 2020（独立 1D 链）、T15 De Beule 2020（散射统一）——均为后续理论对本文的重新解释 💭I（推断，来自 cards.md，原文未引）。

## 8. 对后续研究的影响

- 证明 moiré 拓扑网络不仅在局域探针下可见，**在器件尺度上也支持相干量子输运** 📜Q（摘要: "coherent electronic transport in a lattice of topologically protected states"）
- 网络在磁场与无序下稳定体干涉现象 → 二维网络优于单边缘通道，可做复杂 valleytronic 操作 💭I（推断，结论段支撑: "complex valleytronic operations"）
- 避开物理边缘 → 更干净的拓扑保护环境 📜Q（正文: "avoiding the physical edge leads to a better defined environment which improves topological protection"）
- 推动 AA 节点散射与谷守恒规则的定量建模 💭I（推断）

---

*精读完成日期：2026-08-06（pdftotext 全文提取 + AI 精读） | 2026-08-19 三问框架重读 + QC 证据分级（pypdf 提取 → /tmp/rickhaus2018.txt → grep 反向核对）*

---

## Phase S 补充 (2026-08-19): 三问框架（Q1 表征 / Q2 理论复现 / Q3 对应）

### Q1: 实验如何表征边界态?

低温输运（1.5 K，低频锁相）📜Q。核心表征手段与判据：

- **FP 振荡（密度调谐）**：差分电导 dG/dn_in(n_in, n_out) 在 n_in 上等间距共振 📜Q；周期 Δn_in = 4.7×10¹⁰ cm⁻² 📜Q。**1D 标度判据**：n 线性周期（k_F ∝ n_1D）而非 √n（2D 体态）📜Q。
- **AB 振荡（磁场调谐）**：ΔB = 0.37 T → 面积 A = φ₀/ΔB = 11200 nm² 📜Q。交叉斜线共振（正负斜率并存 = 顺/逆时针包围）排除电子充电效应 📜Q。
- **高场持续判据**：0–8 T 振荡不消失（regime I 对照在 B > 0.5 T 消失）→ 轨迹不受洛伦兹力影响 → 1D 通道 📜Q。8 T 时磁长 9 nm ≪ 器件尺寸 📜Q。
- **边-体区分**：干涉面积 11200 nm² 介于 moiré 单胞（≈950 nm²）与顶栅腔（2×10⁶ nm²）之间 → 路径在**腔内环绕一排 AB/BA 区域**，非器件边缘态、非 QH 边缘通道（振荡从 QH 区连续演化到零场）📜Q。

> ✅ 与 cards.md E10 卡片核对：技术/可观测量/边-体区分/核心发现（FP+AB 双模、0–8 T 稳健）一致，无遗漏；卡片"局限"条（网络 vs 独立 1D 链）已并入 §6。

### Q2: 理论如何复现边界态?

本文**无新理论框架**，理论贡献为既有模型应用 + 定量化分析 📜Q（作者贡献: "J.W. calculated the band structure. S.S. and M.-H.L. helped to develop the theoretical understanding"）：

- **网络图像**：San-Jose & Prada 2013（ref [17]，θ<0.3° 条件）+ Andjelkovic 2018（ref [18]，弹性形变放宽条件）📜Q。
- **能带结构计算**：本文作者自算（位移场、能隙、费米速度，Fig. S9/S10；n₁D 换算 N_ch = 2/(√3λ)，SI eq 4）📜Q。
- **定量模型**：Bohr-Sommerfeld 共振条件 $L_{tot}k_F \pm A\frac{2\pi B}{\phi_0} = 2\pi j$（Eq. 2）📜Q；"环绕一排 AB/BA 区域"的矩形轨迹模型 → ΔB/Δn_in 对 L 的预期线（Fig. 4A 实线/虚线）📜Q。
- ⚠️ 复现方式：不是从哈密顿量导出畴壁态，而是把**拓扑网络假设 + BS 共振几何**映射到振荡数据 💭I（推断，综合）。

### Q3: 理论与实验如何对应?

| 理论预言 | 实验对应 | 证据 |
|------|------|------|
| 大 D 耗尽 AB/BA → 网络态出现 | 振荡仅在小 n_in + 大 D 出现（regime II） | 📜Q |
| 1D 通道 k_F ∝ n_1D → n 线性 FP 周期 | n-B 图斜线（非 2D 抛物线） | 📜Q |
| 环绕一排 AB/BA 区域：A ≈ L·√3λ/2，L_tot−2L ≈ 2λ | 提取 408×27 nm² ≈ 400 nm × 29 nm（λ√3/2） | 📜Q（正文原式） |
| 腔长 L 决定环路几何 | 三栅 L=200/300/400 nm 的 ΔB/Δn_in 与模型线一致 | 📜Q（Fig. 4A） |
| D 减小 → gap Δ 缩小 → 费米速度涂抹 → 退相干 | D 减小 → n_in 窗口收缩；红点（理论涂抹边界）与数据吻合 | 📜Q（Fig. 4B/C + S10） |
| regime I 为 2D 体 FP（2R_c ≳ L） | 有效腔长 550 nm、B>0.5 T 消失——作为 1D 结论的负对照 | 📜Q |

> 对应方法本质：**振荡周期→几何反推**（ΔB→A，Δn_in→L_tot），与 E9（Huang 2018）的实空间 LDOS 直接成像互补——输运 vs 局域探针的 Q3 交叉验证 💭I（推断）。

---

### 附注（三问之外的附加问题）：Vg 与本样品的关系

- 本样品为**双栅**：石墨背栅 Vbg 调全局密度 n_out；顶栅 Vtg 调腔内密度 n_in 与位移场 D 📜Q（正文 + Fig. 1A）。
- 栅-密度换算：$n_{in} = (C_{tg}V_{tg} + C_{bg}V_{bg})/e$，C 由平行板模型（ε_hBN=3.2, d_top=27 nm, d_bottom=45 nm）📜Q。
- D 换算：$D ≈ (D_{top}−D_{bottom})/2$（"simple approximation"，作者明示近似）📜Q；D = −1 V/nm 为 Fig. 4A 条件 📜Q。
- 与 E9（Huang 2018）对照：E9 单背栅（电场 = 背栅 + tip bias + 功函数失配）；本文双栅可**独立**调 n_in 与 D，且无 tip 贡献（输运测量）💭I（推断，基于两文装置描述）。

---

## 反向核对 pass (2026-08-19)

pypdf 提取 → `/tmp/rickhaus2018.txt`（6 页）→ 逐项 grep 核对结果：

- ✅ θ=0.5° / θ=0.42° / λ=33 nm / d_top=27 nm / d_bottom=45 nm / ε=3.2 / L=200,300,400 nm / W=4.6 μm / |n₂|≈0.8×10¹² / 1.5 K / lock-in / 550 nm / 0.5 T / 9 nm / ΔB=0.37 T / A=11200 nm² / 950 nm² / 2×10⁶ nm² / Δn_in=4.7×10¹⁰ / L_tot≈870 nm / 408 nm / 27 nm / λ√3/2≈29 nm / D=−1 V/nm / 0–8 T / θ<0.3° —— 全部在原文找到
- ⚠️ 原文无：Efimkin & MacDonald 2018（本文理论引用实为 ref [17] San-Jose & Prada + ref [18] Andjelkovic 2018）→ 已修正；arXiv 1802.07317（正文无，标注外部来源）

---

## 更正日志 (2026-08-19)

| 原表述 | 问题 | 修正 |
|---|---|---|
| "Efimkin & MacDonald 2018 \| 理论框架 — 本文 D 触发机制与之一致" | 错误引用：原文未引 Efimkin & MacDonald（grep 证伪） | → 改为 ref [17] San-Jose & Prada + ref [18] Andjelkovic（弹性形变）；T9 移入"Phase S 外部对标"标注非原文引用 |
| "arXiv: 1802.07317" | 正文无法验证 | → 标注外部书目来源 |
| 全文数字无证据分级 | 违反 LITERATURE_QC_PROTOCOL | → 全部标 📜Q/📊F/💭I 并附位置 |
| "θ ≈ 0.42° 仍观察到此网络输运 — 晶格弹性形变放宽了条件" | 未注明 θ<0.3° 与弹性形变论点的原始出处 | → 标注 [17]/[18] |
| 4.5 节 "L 越小 → ΔB 与 Δn_in 越慢（更大尺度周期）" | 措辞歧义 | → 按原文 "slower in both ΔB and Δn_in" + "面积与周长都减小" 重写 |
| 6 局限表缺"网络 vs 独立 1D 链"（卡片同款） | 与 cards.md E10 不一致 | → 补入并标 💭I（T12/TZM 外部质疑） |
| 三问节缺失 | 用户明确三问框架（表征/复现/对应） | → 新增 Q1/Q2/Q3 节 + Vg 附注（三问之外） |

---

## 附录：FP 与 AB 振荡的物理基础与实验现象

> ⚠️ 本附录为教科书级背景知识整理 💭I（非 Rickhaus 2018 原文）；涉及本文的具体参数均已复用正文 📜Q 证据并标注章节号。

### A. Fabry-Pérot（FP）振荡

**物理基础**
- 光学原型：法布里-珀罗干涉仪——两片半透明镜面间的多次反射形成驻波。
- 电子输运类比：腔体两端的界面（载流子密度突变形成的半透明"镜面"，如 p-n 结边界）对电子波部分反射 → 往返路径干涉。
- 共振条件（构造干涉）：$2k_F L = 2\pi j$（$j$ 整数），即往返相位是 $2\pi$ 的整数倍；等价于腔长是电子半波长的整数倍（本文原文形式 $2L = j\cdot 2\pi/k_F$）。

**实验现象**
- 电导 $G$ 随密度 $n$（或栅压）**周期振荡**，峰间距由 $\Delta k_F$ 决定。
- **维度判据**：1D 通道 $k_F \propto n_{1D}$ → 峰**等间距**；2D 体态 $k_F \propto \sqrt{n}$ → 峰间距随 $n$ 增大。本文以此判定畴壁通道为 1D 📜Q（§2.4）。
- 二维体 FP 在磁场中轨迹被洛伦兹力弯折，$2R_c \gtrsim L$（Eq. 1）不满足时振荡消失。本文 regime I 即此类 2D FP：有效腔长 550 nm、B > 0.5 T 消失 📜Q（§4.2），作为 regime II 的负对照。

### B. Aharonov-Bohm（AB）振荡

**物理基础**
- AB 效应（Aharonov & Bohm, 1959）：矢势（而非场强本身）进入波函数相位。电子沿闭合环路绕行一圈获得相位 $\Delta\phi = \frac{e}{\hbar}\oint \mathbf{A}\cdot d\mathbf{l} = 2\pi\frac{\Phi}{\Phi_0}$，$\Phi$ 为环路包围磁通，$\Phi_0 = h/e$ 为磁通量子。
- 顺/逆时针两条绕行路径的相位差随 $\Phi$ 线性变化 → 干涉。

**实验现象**
- 电导随垂直磁场 $B$ **周期振荡**，周期 $\Delta B = \Phi_0/A$，$A$ 为闭合环路面积 → **测 ΔB 即可反推干涉环路面积**（振荡快 ↔ 面积大）。
- 本文：ΔB = 0.37 T → $A = 11200\ \text{nm}^2$，介于 moiré 单胞（≈950 nm²）与顶栅腔（2×10⁶ nm²）之间 → 路径在腔内环绕一排 AB/BA 区域 📜Q（§4.4）。
- **交叉斜线共振**：同一环路被顺/逆时针同时包绕（±A）→ n-B 图中正负斜率并存；而单电子充电效应只有单一斜率 → 用斜率符号排除 charging 机制、确立 AB 诠释 📜Q（§4.3）。

### C. 两者如何统一于本文

- 统一共振条件（本文 Eq. 2）：$L_{tot}k_F \pm A\,\frac{2\pi B}{\Phi_0} = 2\pi j$——FP（第一项，密度调谐）与 AB（第二项，磁场调谐）是同一 Bohr-Sommerfeld 驻波条件在两个变量轴上的表现。
- 观测策略：固定 B 扫 n → FP 振荡（提取 $L_{tot} \approx 870$ nm）；固定 n 扫 B → AB 振荡（提取 $A$）→ 联合反推干涉路径几何（等效矩形 408 × 27 nm²）📜Q（§4.4）。
- 物理图像：一个 1D 环路内的相干驻波，同时被电荷填充（$k_F$）与磁通（$\Phi$）两个"旋钮"调制。
