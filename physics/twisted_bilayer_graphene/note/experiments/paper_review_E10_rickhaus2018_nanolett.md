<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-20 17:32:56
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-28 23:40:55
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/experiments/paper_review_E10_rickhaus2018_nanolett.md
 * @Description  : E10: Rickhaus et al. 2018 — mTBG 拓扑网络输运 FP+AB 振荡（2026-08-28 重写：去重 + 归位 + 分层）
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
| **PDF** | ✅ reference/pdfs/Rickhaus 等 - 2018 - ...pdf |
| **SI PDF** | ✅ reference/pdfs/Rickhaus 等 - Supporting Information Transport through a Network of Topological Channels in Twisted Bilayer Graph.pdf（19 页） |
| **DW.bib** | ✅ `rickhaus_transport_2018` |
| **精读日期** | 2026-08-06（初读）→ 2026-08-19（三问框架 + QC 证据分级）→ 2026-08-28（重写） |

---

## TL;DR

在 mTBG（θ≈0.42°）顶栅腔体中，大位移场 $D$ 下观测到**同时随密度（FP）和磁场（AB）调谐的相干振荡**，且在 **0–8 T 持续**。据此判定：体电流沿 **AB/BA 畴壁的拓扑保护一维通道** 流动（而非 2D 体态）——判据两条：密度上**等间距**（$k_F\propto n$，1D 而非 $\sqrt n$）+ 磁场下**不消失**（轨迹不受洛伦兹力弯折）。

---

## 1. 核心贡献

首次在 mTBG 输运实验中同时观测到：

1. **Fabry-Pérot（FP）振荡** — 随载流子密度调谐 📜Q（摘要）
2. **Aharonov-Bohm（AB）振荡** — 随磁场调谐 📜Q（摘要）

最关键发现：振荡在 **0 到 8 T 垂直磁场下持续存在** 📜Q（摘要: "robust in magnetic fields ranging from 0 to 8 T"），与常规二维体系截然不同。从"磁场持续 + 密度线性间距"两点出发，证明体内电流主要沿**拓扑保护的一维通道**传播 📜Q（摘要: "The persistence in magnetic field and the linear spacing in density indicate that charge carriers in the bulk flow in topologically protected, one-dimensional channels"）。

## 2. 物理机制

### 2.1 拓扑网络（QVH 畴壁态）与 QVH/QH 辨析

网络形成四步：

1. tBLG 中 AB/BA 堆垛交替出现 → moiré 超晶格 📜Q（引言）
2. 外加大位移场 D → AB/BA 区域开隙并被耗尽 → 畴壁态形成网络 📜Q（引言）
3. 网络形成源于 AB/BA 堆垛区 **valley Chern 数不同** 📜Q（引言: "different valley Chern numbers in the AB and BA stacking regimes"）
4. 拓扑电流主要在**样品体内**流动 → 对边缘制备缺陷不敏感（对比 InAs/GaSb）📜Q（引言）

> **⚠️ 概念辨析：量子谷霍尔（QVH）畴壁态 ≠ 量子霍尔（QH）边缘通道**（"valley Chern 数不同"给出的是前者，不是文中所排除的 QH edge channels）：
>
> | | QVH 畴壁态（=本文网络） | QH 边缘通道 |
> |---|---|---|
> | 拓扑不变量 | valley Chern 数 $C_v=(C_K-C_{K'})/2$（gapped BLG 中 $=\pm2$） | 总（电荷）Chern 数 $C=C_K+C_{K'}\neq0$ |
> | 打开条件 | 位移场 $D$ + AB/BA 堆垛差 | 垂直磁场 $B$（朗道能级） |
> | B=0 时 | ✅ 已存在（与 B 无关） | ❌ 不存在（需 B） |
> | 载流子 | K、K′ 谷**反向**传播（helical，谷锁定） | **手性**（chiral）单向 |
> | 净电荷霍尔电导 | 0（K 与 K′ 抵消） | 量子化 $e^2/h$ |
> | 位置 | AB/BA **畴壁**（体内） | 物理边缘 / 密度台阶 |
>
> 文中 "not linked to the existence of Quantum Hall edge channels" 的逻辑：振荡**从 QH 区连续到 B=0** → 通道在 B=0 已存在 → 只能是 QVH 网络，不能是 QH 边缘通道 📜Q。

### 2.2 扭角条件（重要修正）

- 早期理论：θ < 0.3° 才够 📜Q（引言，ref [17] San-Jose & Prada）
- **本文实测 θ ≈ 0.42°（目标 0.5°）仍观察到网络输运** — 晶格弹性形变稳定并扩大 AB/BA 区域，放宽条件 📜Q（引言，ref [18] Andjelkovic et al. 2018）

### 2.3 两个 regime 的定义与对比（总表）

| 维度 | Regime I（常规 n-p-n） | Regime II（拓扑网络） |
|------|------------------------|------------------------|
| $n_{in}$ | $n_{in}\ll 0$（大负，$>|n_2|$） | 小 $n_{in}<n_2$（$|n_{in}|<|n_2|\approx0.8\times10^{12}$ cm⁻²） |
| $n_{out}$ | $n_{out}\gg 0$（大正） | **大 $|n_{out}|$**（$D=\frac{e}{2\varepsilon_0}(n_{in}-2n_{out})$：小 $n_{in}$+大 $D$ ⟹ 大 $|n_{out}|$，如 $D=-0.8$ V/nm、$n_{in}\approx0$ → $n_{out}\approx4.4\times10^{12}$ cm⁻²） |
| $D$ | "can but does not have to be large"（非必要条件） | large $D$（$|D|\sim0.8$–1 V/nm，如 −0.8 V/nm → Δ≈150 meV） |
| 载流子类型 | 2D 体态（双极 n-p-n 结内） | 1D 拓扑畴壁通道（AB/BA 被耗尽） |
| 费米波矢标度 | $k_F\approx\sqrt{\pi n_{in}}$（2D 圆费米面） | $k_F\propto n_{1D}\propto n_{in}$（1D 线性） |
| 驻波条件 | $2L=j\cdot 2\pi/k_F$（2D FP） | $L_{tot}k_F\pm A\cdot 2\pi B/\phi_0=2\pi j$（1D FP+AB，Eq. 2） |
| 磁场行为 | B > 0.5 T 振荡消失（$2R_c\gtrsim L$ 破缺，Eq. 1） | 持续到至少 8 T（轨迹不受洛伦兹力影响） |
| n-B 图形态 | 常规 FP（单斜率） | 交叉斜线共振（正负斜率并存 = 顺/逆时针环绕） |
| 背景电导 | — | 平缓（固定数量 1D 通道） |
| 提取腔长 | 550 nm（> 设计 400 nm） | 等效 408 nm × 27 nm（≈ 设计 L × λ√3/2） |
| 角色 | **基准 / 负对照**（证明腔弹道、界面半透明） | **主要发现**（拓扑 1D 通道主导相干输运） |

📜Q 证据：$n_2$（正文 + Fig. S3）；regime I 条件（Fig. 2A caption: "nin ≪ 0 and nout ≫ 0"）；regime I 的 2D 标度与 D 非必要（正文: "$k_F\approx\sqrt{n\pi}$"、"The displacement field can but does not have to be large"）；regime II 条件（正文: "small nin < n2 and large D"）；B 行为（Eq. 1 + Fig. S4 + Fig. 3B）；D 值与 gap（Fig. S9B: D=−0.8 V/nm → 150 meV）。

### 2.4 两个维度判据（结论，推导见附录 A.2）

1. **密度标度**：FP 在 $n_{in}$ 上**等间距**（$k_F\propto n_{1D}$，1D）而非 $\sqrt{n}$（2D）📜Q（摘要 "periodic in n rather than √n"；正文 "would lead to parabolic lines in the magnetoconductance map, which is not observed"）
2. **磁场标度**：振荡在 8 T 仍持续 → 主导路径不是二维体轨道（$2R_c\gtrsim L$ 破缺即消失），而是轨迹不受磁场影响的 1D 通道 📜Q（正文 + Fig. S4 vs Fig. 3B）；8 T 时磁长 9 nm ≪ 器件尺寸 📜Q

## 3. 实验方法

### 3.1 器件（层状结构 / 几何 / 制备）

**层状结构（从下到上）**（SI Fig. S1/S2）：p 掺杂硅片（chip，含 SiO₂）→ **石墨薄片（背栅 BG，兼屏蔽 SiO₂ 陷阱电荷）** → 底 hBN（45 nm）→ **tBLG（活性通道，单片连续）** → 顶 hBN（27 nm）→ **Cr/Au 顶栅 g1/g2/g3** + Cr/Au 接触 c1–c4 📜Q。

- **几何**：顶栅定义 3 个腔 $L=200/300/400$ nm、$W=4.6$ μm（$L\ll W$ → 多并行通道同干涉条件）📜Q；g5/g6 未用。
- **制备**：机械解理 + 干法转移（撕裂一片石墨烯 → 旋转 0.5° 再拾取另一半 → 依次拾取底 hBN、石墨薄片 → 沉积到硅片）📜Q（SI Fig. S2）。
- ⚠️ **PC/PDMS 不是器件组成**：PDMS（印章）+ PC（聚碳酸酯粘附层）是**转移工艺聚合物**，只在 fabrication 中拾取/堆叠薄片，完成后被去除 📜Q（SI Fig. S2）。chip 就是硅片（不是 hBN+PC/PDMS）。

**n_in 与 n_out 的空间意义**：两者都是**同一片 tBLG 上、不同区域的载流子面密度**——顶栅正下方 = **腔区**（顶栅+背栅共同作用 → $n_{in}$）；顶栅之外 = **体区**（仅背栅 → $n_{out}$）。$n_{in}\neq n_{out}$ 在腔体边界形成密度突变 → p-n 结（半透明"腔镜"），FP 干涉靠它。

### 3.2 静电学（旋钮 → 导出量 → 读出）

**物理量一览**（$e$ 元电荷、$\varepsilon_0$ 真空介电常数隐式）：

| 符号 | 含义 | 值 / 单位 | 备注 |
|------|------|-----------|------|
| $V_{tg}$（$=V_{TG}$） | 顶栅电压（施加在 g1/g2/g3） | 可调，V | 文内两种写法混用 📜Q |
| $V_{bg}$ | 石墨背栅电压（全局） | 可调，V | 📜Q |
| $C_{tg}$, $C_{bg}$ | 顶/背栅**单位面积**电容 | F·m⁻² | 平行板模型 📜Q |
| $d_{top}$, $d_{bottom}$ | 上/下 hBN 厚度 | 27 / 45 nm | 📜Q |
| $\varepsilon_{hBN}$（$=\varepsilon_r$） | hBN 相对介电常数 | 3.2 | 文内两种记号 📜Q |
| $n_{in}$ | 腔区载流子密度 | 可调，cm⁻² | 两栅共同决定 |
| $n_{out}$ | 体区载流子密度 | 可调，cm⁻² | 仅背栅决定 📜Q |
| $D$ | 位移场 | 可调，V/nm | "简单近似"给出 📜Q |
| $D_{top}$, $D_{bottom}$ | 顶/背栅对位移场的贡献 | V/nm | $D_{bottom}$ 正文未单列 |

**三条核心关系**（正文原式）：

1. **密度—栅压**：$n_{in} = \dfrac{C_{tg}V_{tg} + C_{bg}V_{bg}}{e}$ 📜Q
2. **电容—厚度**（平行板模型）：$C_{tg} = \dfrac{\varepsilon_0\varepsilon_{hBN}}{d_{top}}$，$C_{bg} = \dfrac{\varepsilon_0\varepsilon_{hBN}}{d_{bottom}}$ 📜Q
3. **位移场—栅压**：$D = \dfrac{D_{top} - D_{bottom}}{2}$，$D_{top} = \dfrac{\varepsilon_r V_{TG}}{d_{top}}$ 📜Q（作者明示 "simple approximation"）

**物理依据**（为什么能这么写）：① 平行板电容充电 $n=CV/e$（$Q=CV$ 面密度版）；② 两栅静电感应**线性叠加**；③ 顶栅**局部**（只盖腔）、背栅**全局**（盖全器件）→ 腔外 $n_{out}=C_{bg}V_{bg}/e$ 只有背栅项 💭I。⚠️ 近似：平行板（忽略边缘场）、未含量子电容修正 📜Q（"parallel plate capacitor model" / "simple approximation"）。

**两个正交旋钮**：共模（$C_{tg}V_{tg}+C_{bg}V_{bg}$）→ $n_{in}$；差模（$(D_{top}-D_{bottom})/2$）→ $D$。双栅因此可**独立**调 $n_{in}$ 与 $D$。

> **两个代数结论（完整推导见附录 A.1）**：
> ① 轴映射：$n_{in}=\dfrac{C_{tg}}{e}V_{tg}+n_{out}$，即 $(n_{in},n_{out})$ 是 $(V_{tg},V_{bg})$ 的**线性剪切**（纵轴 $n_{out}$ = $V_{bg}$ 纯缩放 $3.93\times10^{11}$ cm⁻²/V；横轴 $n_{in}$ 含 $V_{tg}$ 缩放 $6.55\times10^{11}$ + $n_{out}$ 平移）。
> ② $D$ 用密度表达：$D=\dfrac{e}{2\varepsilon_0}(n_{in}-2n_{out})$ ⟺ $n_{out}=\dfrac{n_{in}}{2}-\dfrac{\varepsilon_0}{e}D$（常数 $D$ 为斜率 $1/2$ 直线族；$n_{in}\approx0$ 时 $D=-\dfrac{e}{\varepsilon_0}n_{out}$）。

### 3.3 测量（锁相 / 两端子 / G 与 dG/dn）

- 温度 1.5 K，标准低频**锁相**技术 📜Q（正文 + Fig. 2 caption）
- **两端子**：交流电压对称加在 c1–c2 间测电流，c3/c4 悬空 📜Q（SI: "An AC voltage bias is applied symmetrically between contacts c1 and c2 while measuring the resulting current. Contacts c3 and c4 are floating"）
- **G 是什么**：器件的（线性）电导 = $dI/dV_{sd}$（锁相直接测的微分电导，低偏压线性区 $G\approx I_{ac}/V_{ac}$）💭I（标准锁相背景）
- **dG/dn_in 是什么**：$G$ 对腔密度 $n_{in}$ 的（数值）导数 📜Q（Fig. 2 caption 称 "Differential conductance dG/dnin"）。注意与 $G=dI/dV_{sd}$ 是**两个不同的导数**（前者对源漏偏压，后者对密度）。
- **为何画 dG/dn_in**：FP/AB 振荡是"大而平滑背景 + 小纹波"，求导压低背景、放大振荡（周期不变）→ 纹波被"锐化"（推导见 A.2.4）。
- **三种画法用途**：$G(n_{in})$ 看背景平缓（判 1D 通道数不随 $n_{in}$ 变，Fig. 3C）；$dG/dn_{in}(n_{in},n_{out})$ 看 FP（Fig. 2A）；$dG/dn_{in}(B)$ 看 AB（Fig. 3B，已去平滑背景）📜Q。

## 4. 关键数据

### 4.1 Moiré 标定（n₂ 的定义）

| 参数 | 值 | 证据 |
|------|-----|------|
| 第一带充满密度 $|n_2|$ | ≈ 0.8 × 10¹² cm⁻²（= 8 × 10¹¹ cm⁻²） | 📜Q（正文 + Fig. S3） |
| 物理含义 | **第二个 Dirac 点（2nd DP）**：第一 moiré 子带填满 = 每 moiré 单胞 8 电子（自旋×谷×层 = 2×2×2） | 📜Q（SI Fig. S3） |
| 来源 | Hofstadter butterfly（Fig. S3B 中从 2nd DP 扇出的 LLs） | 📜Q |
| 几何关系 | $A_{MUC}=\sin60°\cdot\lambda^2$，$\lambda=a/(2\sin(\theta/2))$，$a=0.246$ nm；由 $n_2$ 反推 θ = 0.42° | 📜Q（SI Fig. S3） |
| 文中作用 | 标记 regime II 边界（$|n_{in}|<|n_2|$）；Fig. 2A 红色虚线 | 📜Q |

> **有没有 n₁？没有。** 下标 "2" 指"**第二个 Dirac 点**"（satellite DP），不是序列 n₁,n₂,n₃。第一个（主）Dirac 点在 $n=0$（电荷中性点），不给下标 📜Q（SI Fig. S3A）。⚠️ 区分 $n_{1D}$（1D 通道密度，SI Eq. 4）——不是 "n₁"。
>
> ⚠️ SI 指数笔误：Fig. S3 一处写 "θ = 0.42° from $n_2 \approx −0.8 \times 10^{11}$ cm⁻²"，指数应为 $10^{12}$（与正文 0.8×10¹² 及同段 "$n_2=-8\times10^{11}$" 一致）。

### 4.2 Regime I（常规 n-p-n FP，负对照）

- 条件：$n_{in}\ll 0$、$n_{out}\gg 0$ 📜Q（Fig. 2A caption）
- 提取有效腔长 550 nm（> 设计 400 nm，归因于腔-体平滑过渡；FFT 提取，细节见 ref [33] SI）📜Q
- 振荡在 B > 0.5 T 消失（符合 2D 轨道弯折，Eq. 1 成立）📜Q（正文 + Fig. S4）

> ⚠️ **regime I 的 2D（√n）标度是"声明 + 间接论证"，无直接"周期随 n_in 变化"数据图**：只有 ① 2D FP 条件 $2L=j\cdot2\pi/k_F$、$k_F\approx\sqrt{n\pi}$ 的陈述；② Fig. 2A inset FFT（对 $n_{out}$ 平均）提取单一周期 → L=550 nm；③ Fig. S4 展示**随 B 消失**（非随 n_in 的周期变化）。√n vs n 的实际对比在 n-B 平面（2D→抛物线未现、1D→斜线现）📜Q。

### 4.3 Regime II（拓扑网络主导，主发现）

- 条件：小 $n_{in}$（< $|n_2|$）+ 大 $D$（AB/BA 被耗尽、超晶格对称性影响 B 行为）📜Q（正文 + Fig. 2C）
- n-B 图出现**交叉斜线共振**（正负斜率并存 = 同一区域被顺/逆时针包围）📜Q（正文）
- 共振从 QH 区连续演化到低场（0 到 ±3 T 连续，单 trace 到 8 T）→ 与 QH 边缘通道无关 📜Q（正文 + Fig. 3A/B）
- 排除电子充电机制：正负斜率并存与充电（单斜率）不符 📜Q（正文引 ref [35] 判据）
- 背景电导平缓 → 参与输运的 1D 通道数不随 $n_{in}$ 变 📜Q（Fig. 3C + 正文）

> **论证逻辑链**（正文 "In other two-dimensional systems, resonances that depend on B and n at high magnetic fields …" 一段）：
> 1. **现象**：regime II 出现交叉斜线共振（正负斜率并存，Fig. 3A）。
> 2. **候选**：高场 B&n 共振在 2D 体系已知两种起源——单电子充电 vs AB 干涉（refs 35,36）。
> 3. **判据**：n-B 平面斜率符号——充电单斜率；AB 双斜率（Eq. 2 的 $\pm A$ 项 = 顺/逆时针环绕）。
> 4. **判定**：正负斜率并存 → 排除充电、确立 AB。
> 5. **再排除**：共振从 QH 区连续到零场 → 不绑定 QH 边缘通道。
> 6. **强结论**：AB 干涉持续到 B=0 → 载流子在所有 B 已在 1D 通道中。
> 7. **弱佐证**：$G(n_{in})$ 平缓 → 通道数不随 $n_{in}$ 变 → 固定数量 1D 通道。

### 4.4 周期 → 几何（Bohr-Sommerfeld 条件 Eq. 2）

| 参数 | 值 | 证据 |
|------|-----|------|
| ΔB | 0.37 T（Fig. 3B 提取） | 📜Q |
| A = φ₀/ΔB | 11200 nm² | 📜Q |
| moiré 单胞面积 | ≈950 nm² | 📜Q |
| 顶栅腔面积 L·W | ≈2 × 10⁶ nm²（大 2 个量级） | 📜Q |
| Δn_in | 4.7 × 10¹⁰ cm⁻² | 📜Q |
| L_tot = 2π/Δk_F | ≈870 nm | 📜Q（经 $n_{1D}$ 换算，SI Eq. 4） |
| 等效长方形 | 408 nm × 27 nm | 📜Q（正文） |
| 对照 | 408 nm ≈ 设计 L=400 nm；27 nm ≈ λ√3/2 ≈ 29 nm（相邻拓扑通道最短距离） | 📜Q |

> 面积介于 moiré 单胞与顶栅腔之间 → 干涉路径位于腔内、环绕**一排 AB/BA 区域** 📜Q（正文: "one row of AB/BA regions is encircled"）。⚠️ 正文同时承认 "also other trajectories are possible"（AA 节点三方向谷守恒散射），但长而窄 + 连接两腔界面 + $\tilde A/L\approx\lambda\sqrt3/2$、$L_{tot}-2L\approx2\lambda$ → 只此一类与数据一致 📜Q。

### 4.5 外部旋钮验证（L 依赖 + D 依赖）

**L 依赖（Fig. 4A）**：$L=200/300/400$ nm 比较，L 减小 → 振荡在 ΔB 与 Δn_in 上变"慢"（封闭面积与周长都减小）📜Q；与"环绕一排 AB/BA"模型一致（虚线=设计 L 预期，实线=任意 L 的 BS 量化）📜Q。

**D 依赖（Fig. 4B/C）**：D 减小 → 共振边界收窄（n_in 窗口收缩）📜Q。机制：$D\downarrow$ → AB/BA 能隙 $\Delta\downarrow$（Fig. S9）→ 区域在更低 $n_{in}$ 就被填充 → 费米面失去 1D 特征（费米速度涂抹，Fig. S10B）→ 退相干、图案涂抹（Fig. S10C）📜Q。理论涂抹边界（红点）与数据吻合 📜Q。D = −1 V/nm 为 Fig. 4A 固定条件 📜Q。

### 4.6 证据链汇总

**证明 1D 输运**：① FP 密度等间距（非 √n）；② n-B 图斜线（vs 2D 抛物线）；③ 背景电导平缓（固定数量 1D 通道）📜Q。

**证明拓扑保护**：① 仅大 D + 小 $n_{in}$ 出现（符合 valley Hall 网络条件）；② 0–8 T 持续（轨迹不受洛伦兹力弯折）；③ 轨道尺度介于单胞与整腔之间（体内网络闭环，非边缘态）；④ D 依赖边界与理论费米速度涂抹一致（Fig. 4C 红点）📜Q。

## 5. 主要结论

作者最终定性（保守表述）："good indications that electrons form coherent paths within a network of topological channels" 📜Q（结论段）——用 "good indications" 而非 "prove"。

## 6. 局限与未解决的问题

| 局限 | 说明 | 证据 |
|------|------|------|
| 路径几何非唯一性 | "also other trajectories are possible"，实验只提取主导尺度 | 📜Q（正文） |
| 网络 vs 独立 1D 链未裁决 | 数据不能区分"连通网络"（T9）与"独立 1D 通道间干涉"（T12/TZM） | 💭I（推断，原文仅承认轨迹非唯一） |
| 无实空间成像 | 路径几何无法直接验证 | 💭I（推断） |
| B 上限 | 仅到 8 T（恒温器最大场），"presumably beyond" 未测 | 📜Q（正文） |
| 非拓扑替代机制 | 未完全排除所有非拓扑解释（正文只说 "hints at topological protection"） | 💭I（推断） |
| 节点散射矩阵 | AA 节点谷间散射率与无序的定量关系未知 | 💭I（推断，SI Fig. S7B） |

## 7. 与其他工作的关系

| 工作 | 关系 |
|------|------|
| San-Jose & Prada 2013 (ref [17]) | 螺旋网络理论预言 + θ<0.3° 条件来源 📜Q |
| Andjelkovic et al. 2018 (ref [18]) | 弹性形变稳定/扩大 AB/BA 区域 → 放宽 θ 条件的依据 📜Q |
| Huang 2018 (ref [19]) | STM 局域实空间证据 — 本文提供互补输运证据 📜Q |
| Young & Kim 2009 / Rickhaus 2015 等 (ref [24,25,33,34]) | 单层/双层石墨烯 2D FP 传统 — 本文 regime I 复现、regime II 对照 📜Q |
| Li 2016 (ref [15]) / Lee 2017 (ref [16]) | 零场 BLG 拓扑通道早期实现 📜Q |

> ⚠️ **Phase S 外部对标（非本文引用）**：T9 Efimkin & MacDonald 2018 网络模型、T12 Tsim/Nam/Koshino 2020（独立 1D 链）、T15 De Beule 2020（散射统一）——均为后续理论对本文的重新解释 💭I（来自 cards.md，原文未引）。

## 8. 对后续研究的影响

- 证明 moiré 拓扑网络不仅在局域探针下可见，**在器件尺度也支持相干量子输运** 📜Q（摘要）
- 网络在磁场与无序下稳定体干涉 → 2D 网络优于单边缘通道，可做复杂 valleytronic 操作 💭I（推断）
- 避开物理边缘 → 更干净的拓扑保护环境 📜Q（正文）
- 推动 AA 节点散射与谷守恒规则的定量建模 💭I（推断）

## 9. 理论模型映射（n_in ↔ E_F，D ↔ Δ）

（供 tbplas / Kubo-Bastin 等理论计算对照实验用；原文 Eq. 9/10，Fig. S9/S10。）

### 9.1 连续模型哈密顿量（SI Eq. 9）

能带计算采用**连续 (k·p) 模型**（非晶格 tight-binding，但 on-site 概念对应），层内哈密顿量：

$$H_{T/B} = v\,\vec{p}\cdot\vec{\sigma} \pm \frac{\Delta}{2}\sigma_0$$

+/− 对应顶/底层（T/B），$\sigma_0$ 单位矩阵，$\Delta$ 为栅极诱导的**层间不对称能隙** 📜Q（SI Eq. 9: "the +/− sign is used for the T/B layer and Δ is the energy shift induced by the electrostatic gates"）。→ **Δ 以 ±Δ/2 on-site 能移进入哈密顿量**（顶层 +Δ/2、底层 −Δ/2，对角项 $\propto\sigma_0$，层内均匀、层间反号）——这是**层间**（interlayer）on-site 能差，不是"层内"。

### 9.2 D → Δ 的换算（SI Eq. 10）

$$D \;\xrightarrow{\text{Eq. 10}}\; \Delta = \frac{eD\,d_m}{1+\Lambda^2\ln\tfrac{4\gamma_1}{\Delta}}$$

（$d_m=0.33$ nm，$\Lambda\approx 1$，$\gamma_1\approx 0.4$ eV；实际画图用更精确公式，屏蔽使 Δ 近似减半）📜Q（SI Fig. S9A）。

| $D$ | 能隙 $\Delta$ | 干涉持续 $E_F$ 范围 |
|------|---------------|---------------------|
| −0.3 V/nm | ≈ 50 meV | −1 ~ +1 meV |
| −0.8 V/nm | ≈ 150 meV | −2.5 ~ +2.5 meV |

📜Q（SI Fig. S9B + 正文 Fig. 4c）。→ **正确链条**：$D$（位移场）→ $\Delta$（能隙，Eq. 10，含屏蔽）→ 层间 on-site 能差 $\pm\Delta/2$（Eq. 9）；$D$ 本身不是 on-site energy。

### 9.3 n_in → 费米能级 → 费米波矢

- $n_{in}$ 通过色散确定费米能级 $E_F$ 📜Q（SI Fig. S9B）
- 固定 $\Delta$ 下 $E_F$ 决定费米面形状（Fig. S10A：三角电子/空穴口袋平边 → 1D 拓扑通道）
- FP 相关量是主导 1D 波矢 $k_x$，与 $n_{in}$ **线性**相关 📜Q（SI Fig. S10B: "$k_x\sim n_{in}+c\cdot\text{sgn}(n)$"）
- 2D→1D 密度换算（SI Eq. 4）：$n_{1D}=n_{in}\cdot\dfrac{\lambda}{2\sqrt3}$（$N_{ch}=2\sqrt3/\lambda$），1D 费米波矢 $k_F=\dfrac{2\pi}{g}n_{1D}$ 📜Q

> **与实验量 G 的对应**（供 tbplas/Kubo 对照）：实验 $G=dI/dV$（两端子，器件量）与 Kubo-Bastin $\sigma_{xx},\sigma_{xy}$（体电导率，材料量）是**同一线性响应的器件版 vs 材料版**，关系 $G=\sigma_{xx}\cdot W/L$（四端/扩散极限，需扣除接触电阻；强场下两端子混入 $\sigma_{xy}$）。⚠️ 本文 FP/AB 振荡是**有限尺寸相干效应**，bulk $\sigma_{xx}$ 只给平滑背景、算不出振荡——要复现振荡需算有限器件透射（Landauer/Fisher-Lee）。变量对齐：$n\leftrightarrow E_F$（经 DOS 积分）、$D\leftrightarrow\Delta$（on-site）、$B$ 两者都有。💭I

---

## 附录 A：推导与背景（教科书 / 代数推导，💭I）

> ⚠️ 本附录为背景知识与代数推导（非 Rickhaus 2018 原文陈述）；涉及本文的具体参数均复用正文 📜Q 证据。

### A.1 静电学推导（Q=CV、叠加、位移场展开式、轴映射、D(n_in,n_out)）

**平行板电容充电**：栅压 $V$ 经介电层（厚度 $d$、$\varepsilon_{hBN}$）在石墨烯上感应面电荷密度 $CV$（$C=\varepsilon_0\varepsilon_{hBN}/d$），除以 $e$ 得 $n=CV/e$（$Q=CV$ 面密度版）。

**两栅叠加**：$n_{in}=(C_{tg}V_{tg}+C_{bg}V_{bg})/e$；**局部/全局几何**：腔外只背栅 → $n_{out}=C_{bg}V_{bg}/e$。

**位移场展开式**：由 $D=(D_{top}-D_{bottom})/2$、$D_{top}=\varepsilon_r V_{tg}/d_{top}=C_{tg}V_{tg}/\varepsilon_0$，得

$$D=\frac{C_{tg}V_{tg}-C_{bg}V_{bg}}{2\varepsilon_0}$$

（量纲 V/m，文中按 V/nm 报数。即双层石墨烯文献常用位移场形式。）

**用 $(n_{in},n_{out})$ 表达 $D$**：由 $C_{tg}V_{tg}=e(n_{in}-n_{out})$、$C_{bg}V_{bg}=e n_{out}$ 代入：

$$D=\frac{e}{2\varepsilon_0}(n_{in}-2n_{out})\;\Longleftrightarrow\; n_{out}=\frac{n_{in}}{2}-\frac{\varepsilon_0}{e}D$$

数值换算：$D\ (\text{V/nm})\approx 9.05\times10^{-14}\times(n_{in}-2n_{out})\ [\text{cm}^{-2}]$；$n_{in}\approx0$ 时 $D=-\dfrac{e}{\varepsilon_0}n_{out}$，故 $D=-0.8$ V/nm ⟹ $n_{out}\approx4.4\times10^{12}$ cm⁻²（≈ 5.5 $n_2$）。

**轴映射（线性剪切）**：$(n_{in},n_{out})$ 与 $(V_{tg},V_{bg})$ 之间是上三角（剪切）变换：

$$\begin{pmatrix}n_{in}\\n_{out}\end{pmatrix}=\frac{1}{e}\begin{pmatrix}C_{tg}&C_{bg}\\0&C_{bg}\end{pmatrix}\begin{pmatrix}V_{tg}\\V_{bg}\end{pmatrix},\qquad \frac{C_{tg}}{e}\approx6.55\times10^{11},\ \frac{C_{bg}}{e}\approx3.93\times10^{11}\ \text{cm}^{-2}/\text{V}$$

纵轴 $n_{out}$ = $V_{bg}$ 纯缩放；横轴 $n_{in}$ = $V_{tg}$ 缩放 + $n_{out}$ 平移。水平切线（$n_{out}$ 定）= 固定 $V_{bg}$ 扫 $V_{tg}$；竖直切线（$n_{in}$ 定）= 两栅联动补偿。系数比 $C_{tg}/C_{bg}=d_{bottom}/d_{top}=45/27=1.67$（顶栅更"劲"）。

### A.2 FP 振荡 + 维度判据推导（k_F ~ √n vs n）+ dG/dn 对应链条

**A.2.1 k 空间态密度**：$d$ 维自由电子气中每个 k 态占 $(2\pi)^d$，单位实空间体积、单位 k 空间体积的态数 $g/(2\pi)^d$（$g$ 简并度）。

**A.2.2 二维（圆费米面）**：$n=g\cdot\dfrac{\pi k_F^2}{(2\pi)^2}=\dfrac{g k_F^2}{4\pi}$ → $k_F=\sqrt{\dfrac{4\pi n}{g}}$；$g=4$（自旋×谷）→ $k_F=\sqrt{\pi n}$（即正文 $k_F\approx\sqrt{n\pi}$，与 SI "kF=√(4/g·nπ)" 一致）📜Q。

**A.2.3 一维（费米区间 $[-k_F,+k_F]$）**：$n_{1D}=g\cdot\dfrac{2k_F}{2\pi}=\dfrac{g k_F}{\pi}$ → $k_F=\dfrac{\pi n_{1D}}{g}$（线性）。

> ⚠️ 记号备注：本文 SI 写 $k_F=(2\pi/g)n_{1D}$（比标准 $\pi/g$ 大 2 倍）📜Q，是"费米点计数"或单方向密度约定差异 💭I；不影响 √n vs n 标度，且本文 SI Eq.4→Eq.5 在该约定下自洽。

**与实验量连接**：$n_{1D}=n_{in}\cdot\lambda/(2\sqrt3)$（SI Eq. 4，$N_{ch}=2\sqrt3/\lambda$）→ $k_F\propto n_{in}$（仍线性）。

**为什么"等间距 Δn"是 1D 指纹**：FP 条件 $L_{tot}k_F=2\pi j$ → $\Delta k_F=2\pi/L_{tot}$（常数）。1D：$dn_{1D}/dk_F=g/\pi$（常数）→ $\Delta n=2g/L_{tot}$（等间距）；2D：$dn/dk_F=gk_F/(2\pi)\propto k_F$ → $\Delta n\propto k_F$（非等间距，磁导图抛物线）。→ 实验等间距 $\Delta n_{in}=4.7\times10^{10}$ cm⁻² → 1D，排除 2D 📜Q。

**A.2.4 从 FP 条件到实验测到的 dG/dn_in（对应链条）**：
1. FP 条件在 $k_F$ 空间等间距：$\Delta k_F=\pi/L$（线性腔）或 $2\pi/L_{tot}$（闭环）。
2. $k_F(n)$ 搬共振到密度轴：$\Delta n=\dfrac{dn}{dk_F}\Delta k_F$（2D ∝ √n；1D 等间距）。
3. 电导振荡（FP 透射 Airy 函数）：$G(n)=G_{bg}(n)+\delta G\cos(2k_F L)$，密度轴周期 $\Delta n$。
4. 为何测 $dG/dn$：$\dfrac{dG}{dn}=\dfrac{dG_{bg}}{dn}-2L\dfrac{dk_F}{dn}\delta G\sin(2k_F L)$ —— 压低背景、放大振荡、周期不变 → 纹波锐化。
5. **结论**：Fig. 2A 测的 $\Delta n_{in}$ 就是 FP 密度周期；等间距→1D，非等间距→2D。

> ⚠️ **这里的 $n$ 是 $n_{in}$（腔密度），不是 $n_{out}$**：FP 干涉在腔内，$k_F$ 由腔内费米面决定。$n_{out}$ 只定腔镜反射率（幅度/可见度 + 有效腔长）与体区背景，**不定周期** —— 正因如此 Fig. 2A 的 FFT 才能"对 $n_{out}$ 平均"增强信号 📜Q。

### A.3 AB 振荡 + 交叉斜线（±斜率）

**AB 效应**：电子绕闭合环路一圈获相位 $\Delta\phi=\dfrac{e}{\hbar}\oint\mathbf A\cdot d\mathbf l=2\pi\dfrac{\Phi}{\Phi_0}$（$\Phi_0=h/e$）。顺/逆时针两条路径相位差随 $\Phi$ 线性变化 → 干涉。电导随 $B$ 周期振荡 $\Delta B=\Phi_0/A$。

**交叉斜线（正负两斜率）**：Bohr-Sommerfeld 条件 $j=L_{tot}\dfrac{k_F}{2\pi}\pm A\dfrac{B}{\phi_0}$ 的 $\pm$ 号 = 环路被顺/逆时针环绕。对固定 $j$ 解 $B$：

$$B=\frac{\phi_0}{\pm A}\left(j-\frac{L_{tot}k_F}{2\pi}\right)$$

→ 取 + 号得负斜率、取 − 号得正斜率（大小相同、符号相反）→ 两族斜线交叉成 X 形。充电机制只有单斜率 → 用"正负斜率并存"排除充电、确立 AB 📜Q。

### A.4 Hofstadter 蝴蝶

**物理实质**：2D 周期晶格 + 垂直磁场的布洛赫电子能谱，作为"每单胞磁通"的函数呈自相似分形（Hofstadter 1976）。核心无量纲参数 $\alpha=\Phi/\Phi_0=BA_{cell}/\Phi_0=A_{cell}/(2\pi l_B^2)$（$l_B=\sqrt{\hbar/eB}$ 磁长度）；$\alpha=p/q$ 有理 → 谱劈裂 $q$ 子带（Harper 方程），无理 → Cantor 集。

**为什么 moiré 让蝴蝶可见**：原子晶格 $A_{atom}\approx0.052$ nm² → $\alpha=1$ 需 $B\approx8\times10^4$ T（不可及）；moiré $A_{MUC}=(\sqrt3/2)\lambda^2\approx943$ nm² → $B_1=\Phi_0/A_{MUC}\approx4.4$ T（可及）。moiré 把有效晶格放大 $\approx2\times10^4$ 倍。

**本文测量与提取**（SI Fig. S3）：$D=0$ 下测磁导图 $G(n_{out},B)$，取 $dG/dn_{out}$ 增强 📜Q。观察：主 DP（$n=0$）扇出的主 LLs + 2nd DP（$\pm n_2$）扇出的卫星 LLs，$B>0.5$ T 分形。低场 Dirac LL $E_N\propto\pm\sqrt{NB}$ → $(n,B)$ 平面 $n_N\propto N\cdot B$ 直线族（每条 LL 简并度 $4B/\Phi_0$）💭I。提取：$n_2=8/A_{MUC}=8/((\sqrt3/2)\lambda^2)\approx0.8\times10^{12}$ cm⁻² → 反推 $\theta=0.42°$ 📜Q。蝴蝶（$D=0$）是**前置标定**，$n_2$ 兼作 regime II 密度边界。

### A.5 Bohr-Sommerfeld 统一条件

$$j=L_{tot}\frac{k_F}{2\pi}\;\pm\; A\frac{B}{\phi_0}$$

FP（第一项，密度调谐）与 AB（第二项，磁场调谐）是同一驻波条件在两个变量轴上的表现。观测策略：固定 B 扫 n → FP（提取 $L_{tot}\approx870$ nm）；固定 n 扫 B → AB（提取 $A$）→ 联合反推路径几何（等效矩形 408×27 nm²）📜Q。

---

## Phase S 补充：三问框架（2026-08-19）

### Q1: 实验如何表征边界态?

低温输运（1.5 K，低频锁相）📜Q。手段与判据：**FP 振荡**（$dG/dn_{in}$ 在 $n_{in}$ 上等间距，$\Delta n_{in}=4.7\times10^{10}$ cm⁻²，1D 标度）；**AB 振荡**（$\Delta B=0.37$ T → $A=11200$ nm²，交叉斜线排除充电）；**高场持续**（0–8 T，轨迹不受洛伦兹力）；**边-体区分**（$A$ 介于单胞 950 nm² 与腔 2×10⁶ nm² 之间 → 腔内环绕一排 AB/BA，非边缘态、非 QH 边缘通道）——详见 §4.3/4.4/4.6。

### Q2: 理论如何复现边界态?

本文**无新理论框架**，理论贡献为既有模型应用 + 定量化分析 📜Q（作者贡献声明）。网络图像（San-Jose & Prada 2013 + Andjelkovic 2018）；能带结构自算（Fig. S9/S10）；定量模型 = Bohr-Sommerfeld 条件 + "环绕一排 AB/BA"矩形轨迹（Fig. 4A 实线/虚线）。⚠️ 复现方式：不是从哈密顿量导出畴壁态，而是把"拓扑网络假设 + BS 共振几何"映射到振荡数据 💭I。——详见 §9 + 附录 A.5。

### Q3: 理论与实验如何对应?

| 理论预言 | 实验对应 | 证据 |
|------|------|------|
| 大 D 耗尽 AB/BA → 网络态出现 | 振荡仅在小 $n_{in}$ + 大 D 出现（regime II） | 📜Q |
| 1D 通道 $k_F\propto n_{1D}$ → n 线性周期 | n-B 图斜线（非 2D 抛物线） | 📜Q |
| 环绕一排 AB/BA：$A\approx L\cdot\lambda\sqrt3/2$，$L_{tot}-2L\approx2\lambda$ | 提取 408×27 nm² ≈ 400 nm × 29 nm | 📜Q |
| 腔长 L 决定环路几何 | 三栅 L=200/300/400 nm 的 ΔB/Δn_in 与模型线一致 | 📜Q（Fig. 4A） |
| D 减小 → gap 缩小 → 费米速度涂抹 → 退相干 | D 减小 → n_in 窗口收缩；红点与数据吻合 | 📜Q（Fig. 4B/C + S10） |
| regime I 为 2D 体 FP（$2R_c\gtrsim L$） | 550 nm、B>0.5 T 消失——负对照 | 📜Q |

> 对应方法本质：**振荡周期→几何反推**（ΔB→A，Δn_in→L_tot），与 E9（Huang 2018）实空间 LDOS 成像互补（输运 vs 局域探针）💭I。

---

## 反向核对 pass (2026-08-19)

pypdf 提取 → `/tmp/rickhaus2018.txt`（6 页）→ 逐项 grep 核对：

- ✅ θ=0.5° / θ=0.42° / λ=33 nm / d_top=27 nm / d_bottom=45 nm / ε=3.2 / L=200,300,400 nm / W=4.6 μm / |n₂|≈0.8×10¹² / 1.5 K / lock-in / 550 nm / 0.5 T / 9 nm / ΔB=0.37 T / A=11200 nm² / 950 nm² / 2×10⁶ nm² / Δn_in=4.7×10¹⁰ / L_tot≈870 nm / 408 nm / 27 nm / λ√3/2≈29 nm / D=−1 V/nm / 0–8 T / θ<0.3° —— 全部在原文找到。
- ⚠️ 原文无：Efimkin & MacDonald 2018（理论引用实为 ref [17] San-Jose & Prada + ref [18] Andjelkovic）；arXiv 1802.07317（正文无，外部书目来源）。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-19 | 修正错误引用（Efimkin & MacDonald → San-Jose & Prada + Andjelkovic）；arXiv 标注外部来源；全文加 📜Q/💭I 证据分级；补三问框架 |
| 2026-08-28 | 补 SI（测量两端子、Eq. 9/10、n₂=8/MUC、Hofstadter、n₁D 换算）；补 §3.2 静电学量纲链、§3.4 G/dG/dn、§3.5→§9 理论映射、§4.7→§2.3 regime 对比表、附录 A 推导 |
| 2026-08-28 | **整体重写**：去重 + 归位 + 分层（正文=原文事实 📜Q / 附录=推导 💭I / 文末=过程记录）；§3 实验方法瘦身，推导全部归入附录 A；§3.5 理论映射 → §9；§4.7 总表 → §2.3；Phase S 三问改引用式 |
