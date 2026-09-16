<!--
 * @Author       : AI 精读 (research_onboarding_skill, Phase 4) → 2026-09-02 按 4 块新架构重读
 * @Date         : 2026-08-11（初读）→ 2026-09-02（4 块辨识结构重写）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T29_hou2024_prb.md
 * @Description  : T29: Hou, Yuan & Jiang 2024 — 偏压 mTBG 的 1D 导电通道阵列（理论裁决：NQCP 电导平台）
-->

# Paper Review: Hou, Yuan & Jiang (2024) — mTBG 中 1D 导电通道阵列

| 字段 | 内容 |
|------|------|
| **编号** | T29 |
| **标题** | Arrays of one-dimensional conducting channels in minimally twisted bilayer graphene |
| **作者** | Zhe Hou, Kai Yuan, Hua Jiang |
| **期刊** | Physical Review B 110, L161406 (2024)（Letter，received 20 Aug 2024 / published 15 Oct 2024） |
| **DOI / arXiv** | 10.1103/PhysRevB.110.L161406 / arXiv:2408.09843（⚠️ arXiv 号正文未出现，标外部来源） |
| **类型** | 理论 — 量子输运模拟（紧束缚 + NEGF）裁决 TZM vs 网络 |
| **课题组** | Hua Jiang 组（Fudan；一作 Zhe Hou，Nanjing Normal University） |
| **PDF / SI PDF** | ✅ reference/pdfs/Hou 等 - 2024 - Arrays of one-dimensional conducting channels in minimally twisted bilayer graphene.pdf（正文 + SM §I–VII） |
| **精读日期** | 2026-08-11（初读）→ 2026-09-02（4 块辨识结构重写） |

> **共享知识引用**：量子化电导/通道计数见 `[PHY-LB]`；valley Chern/helical vs chiral 见 `[PHY-BERRY]`；网络 miniband 见 `[PHY-MB]`；AB/FP 干涉见 `[PHY-AB]`。本 review 只写"本文代入"的数字，不重复讲义。

---

## TL;DR

**本文想解决的问题**：极小扭角（minimally twisted）偏压 TBG 的畴壁拓扑螺旋态（THS）如何传播——是自组织为 **2D 三角网络**（在 AA 堆叠点被散射成三路），还是自组织为 **1D 拓扑锯齿模（TZM）** 独立传播？

**主结果**：用两端 TBG 纳米 flake 器件的紧束缚 + 非平衡格林函数（Landauer/Meir-Wingreen 形式）量子输运模拟，作者"show" THS 确实**自构 1D 畸变 TZM**、每条绕过 AA 堆叠点独立传播 📜Q。长 flake 上得到**近量子化电导平台（NQCP）**，值**接近 1、2、3（单位 2e²/h）**、非精确量子化 📜Q；算例 θ=0.82° 平台值 ~1.99（接近 2）📜Q。

**结论/意义**：这是 THS 存在 TZM 的"strong experimental sign"（作者措辞，是可检验预言而非已测事实）📜Q；裁决了十年的网络 vs TZM 之争，并在 2D 平台上实现 1D 通道阵列。

---

## 1. 系统辨识导览（判别表为全文唯一权威）

**黑箱三要素**：`{输入旋钮: θ、层间偏压 Δ、费米能 E_F、扭转中心 (x₀,y₀)、器件尺寸 N/L/N_top、杂质参数 | 输出观测量: 两端微分电导 G（单位 G₀=2e²/h）、非平衡 LDOS ρ_NE(r) | 声称结论: THS 自构 1D 畸变 TZM、绕过 AA 点独立传播；NQCP 平台近 1/2/3}`

**四层变量表**（理论版，符号层一次钉死）：

| 层 | T29 实例 |
|----|----------|
| **L1 旋钮 u** | θ（扭角，0–1.2°）、Δ（层间偏压，−0.4–+0.4 eV）、E_F（费米能，±0.1 eV）、扭转中心 (x₀,y₀)、宽度 N、长度 L、顶层宽 N_top、杂质 (V₀, ξ, 位置) |
| **L2 导出量 x₁** | moiré 周期（由 θ 定；原文**未给 λ 数值**，仅定性"moiré period decreases with θ"）、commensurate 角 θ_com≈0.8168°（m=40, n=41）📜Q |
| **L3 模型量 x₂** | 紧束缚 H（Eq.1）、hopping t_ij（Slater-Koster Eq.2）、G(E_F)（NEGF Eq.3）、非平衡 LDOS ρ_NE（SI Eq.S5）、TZM 线性色散能窗（~150 meV）、valley Chern 差 ΔC_v=2 |
| **固定参数（非旋钮）** | a=1.418 Å、a_I=3.349 Å、γ₀=2.7 eV、γ₁=0.48 eV、q_π/a=q_σ/a_I=2.218 Å⁻¹、hopping 截断 r_c=3a 📜Q |
| **反推量 θ̂** | 无（纯理论，无反推实验量）；模型参考能 E_CNP≈0.79 eV（TBG 电荷中性点，Eq.3 定义基准）📜Q |
| **L4 观测量 y** | 可实验检验预言：NQCP 平台值（近 1/2/3 × 2e²/h）、100% valley 极化电流、AB 振荡"trivial origin" |

**可辨识性判别表**（理论论文 = 区分竞争图景/竞争模型，每条 = 判据 / 排除谁 / 确立谁）：

| 判别 | 判据（计算证据） | 排除谁 | 确立谁 |
|------|-----------------|--------|--------|
| **TZM vs 2D 网络**（传播图景） | 非平衡 LDOS ρ_NE：两条畸变、分离的 TZM 横跨 flake，被 AA 点排斥、平行 TZM"never couple in real space"（Fig.4a/b）；SI 能带本征态绕过所有 AA 点（Fig.S2b）📜Q | 2D 网络（AA 点散射成三路） | 1D 畸变 TZM 独立传播 |
| **NQCP vs 精确量子化** | 平台值"around 1.99"（非 2.00）、"around 0.999"（非 1.000）📜Q | 完美（无散射）TZM 的精确量子化 | 畸变 TZM → 近量子化平台（残余散射痕迹） |
| **bulk vs 边缘态** | 平台 1 与 3 共存（Fig.3b）→ 1D 通道必在 TBG 体内 📜Q | 边缘态解释 | bulk 1D 通道 |
| **观测振荡归属** | AB 振荡有 trivial origin（两 TZM + 接触围成轨迹）；1D 通道与 Rickhaus FP 振荡一致 [38] 📜Q | "观测振荡证 2D 网络"的解读 | 观测振荡"may not account for the 2D network model"[38,39] |

> **主结果 ↔ 判别表映射**（每条主结果由哪几条判别确立）：
> - 主结果① THS 自构 1D 畸变 TZM（绕过 AA 点独立传播）← {TZM vs 2D 网络}
> - 主结果② NQCP 平台近 1/2/3（非精确量子化）← {NQCP vs 精确量子化}
> - 主结果③ 1D 通道在 bulk（非边缘态）← {bulk vs 边缘态}
> - 主结果④ 已观测的 AB/FP 振荡不构成网络模型的证据 ← {观测振荡归属}
>
> **机制溯源五问（本文代入）**：① TZM 从何而来——AA 点散射规则（实线箭头→虚线箭头 −120°，虚线→实线 +120°，引 ref 40）使 THS 绕过 AA 点自组织 📜Q；② G 怎么定义——G₀≡2e²/h 单位下的两端微分电导，G(E_F)=(2e²/h)Tr[Γ_L G^r Γ_R G^a] 📜Q；③ ρ_NE 怎么提取——总 LDOS 减平衡 LDOS（Keldysh，SI Eq.S5）📜Q；④ 平台为何随 θ 变——θ 增→moiré 变窄→纵向 TZM 耦合增强→平台消失 📜Q；⑤ "近量子化"与"量子化"差在哪——平台值 ~1.99 而非 2.00（畸变 TZM 的弱散射痕迹）📜Q。

> **[前提与限定]**（判别结论的适用范围）：
> - **噪声/扰动**：零温 T=0（SI）📜Q；短程点杂质 V₀=2.5 eV、ξ≤a 免疫、大 ξ 且置于 TZM 路径上才破坏平台（SI Fig.S8）📜Q；强 e-e 关联未计入（只在魔角 ~1.05° 平带主导；本文 E_F 远离平带，TZM 能窗 ~150 meV ≫ U_c≈25 meV）📜Q。
> - **判别性扫轴**：扫 θ（0–1.2°）、E_F（±0.1 eV）、Δ（±0.4 eV）、L（长度）、N（宽度）、N_top（顶层边界）、扭转中心 y₀、杂质位置 y_im；均为零温静态计算。
> - **候选集 M 边界**：{2D 网络, 完美 TZM, 边缘态, 精确量子化} —— "畸变 TZM"在该集合内唯一自洽；**集外候选未排除**：无序系综平均、有限温、多体关联、零偏压网络（Δ=0 时 TZM 能窗不出现，见 SI Fig.S2）原文未系统处理。
>
> 三层标注：📜Q = 原文事实（附位置）｜推导｜📊F = 读图估算｜💭I = 推断。**不确定度（正交轴）**：[±] 原文误差棒 / [~] 原文以 =/≈ 给出但无误差棒 / [读图] 图提取 / [相对] 仅相对量。全文经 pdftotext + grep 反向核对。

---

## 2. 结果与机制（按论文论证结构：模型 → 电导行为 → 平台可调 → LDOS 佐证 → 稳健性）

### 2.1 THS → TZM 的自组织机制

偏压 mTBG 畴壁（AB/BA 堆叠区边界）存在 1D 拓扑螺旋态 THS，其起源 = 畴壁两侧每自旋谷 valley Chern 数之差 ΔC_v=2（引 refs 43,44）📜Q。每畴壁有两种 THS（Fig.1a 实线/虚线箭头），在 AA 堆叠区散射规则为：实线→虚线（−120°方向）、虚线→实线（+120°方向）（引 ref 40）📜Q。据此 THS 可自构 1D TZM。**本文新贡献**：量子输运模拟证明这些 THS 自构的是 **1D 畸变 TZM**（distorted TZM，Fig.1b 红曲线），"each bypassing the AA-stacking spots and propagating independently"（ref 40 的"完美"TZM 为黑曲线）📜Q。

> 术语辨析：标题/摘要称 THS = "topological **helical** states"；Fig.1 caption 又写每谷 "two **chiral** THSs"——单谷内手征、跨谷成 helical（QVH 畴壁态），与 [PHY-BERRY] 一致。本文"畸变 vs 完美"TZM 之别 = 是否严格沿 ±v_i 直线传播（ref 64 注：zigzag 模非严格沿 x 轴）📜Q。

### 2.2 电导平台 NQCP（核心结果）

- **平台 2**：长 flake（L=303a，θ=0.82°）平台值"around 1.99, close to the quantized value of 2"（Fig.2a 红色阴影区，θ 范围 0.76°<θ<0.91°）📜Q[~]。
- **平台机制**：θ=0.82° 时三排 AA 亮斑阵列沿纵向夹住两条 TZM（Fig.1c 巨箭头）→ 平台 2 📜Q。
- **非精确量子化**：作者措辞"nearly quantized"（近量子化）📜Q；平台值 ~1.99 而非 2.00——畸变 TZM 的残余散射痕迹（💭I，见判别表）。
- **θ 增大**：moiré 图案变窄、纵向 TZM 增多 → G 增大；但更大 θ 无新平台（moiré 周期减小、纵向 TZM 耦合增强）📜Q。

### 2.3 器件几何 / 宽度 / 长度 / 边界影响平台

- **宽度 N**：N 增大 → 平台出现在更小 θ（固定 θ 时 AA 斑数随 N 增）；要"完美嵌入两条纵向 TZM"需减小 θ 📜Q。平台质量随 θ 减小而改善（moiré 更大、TZM 分离、耦合消除）📜Q。更高平台 **4, 6, 8, …** 需更宽系统（作者预言）📜Q。
- **长度 L**：短 L 量子隧穿使 G 大，L 增则 G 快速降并饱和到平台 📜Q。中间长度（L=123a）除两条纵向 TZM 外还有 K′ 谷的 −v₂、−v₃ 模参与输运，但因垂直速度分量在边界被滤掉、不贡献电导（引 ref 64）📜Q。
- **边界/顶层宽度 N_top**（SI §VI）：N_top=N（非平直边界）→ 平台质量变差；NQCP of 2（扭心在原点）比 NQCP of 1（扭心在下边界）对边界更敏感（后者 θ 更小 + 单 TZM 无耦合）📜Q(SI)。

### 2.4 扭转中心位移调平台数（1/2/3 可调）

- **平台 1**：扭心移到 (0, −56√3a)，θ>0.34°，平台值"around 0.999, close to the quantized value 1"，两排 AA 阵列夹单条 TZM（Fig.3a）📜Q[~]。
- **平台 2 与 3 共存**：N=209、扭心 (0, −100√3a)≈(0, −246 Å)，θ=0.74° 处观察到 NQCP of 2 与 of 3（Fig.3b）📜Q。**平台 1 与 3 共存 → 1D 通道必在 bulk**，排除边缘态解释 📜Q。
- 平台值可经扭转中心的简单垂直位移微调到接近 1 或 3（抽象）📜Q；扭心下移的连续演化见 SI §III（Fig.S4/S5，每步 δy₀=−4√3a，NQCP of 1 在 y₀=−8√3a、0.66°≤θ≤0.72° 出现）📜Q(SI)。

### 2.5 非平衡 LDOS 佐证 1D 本质（Fig.4 + SI）

非平衡 LDOS ρ_NE(r)（Fig.4 底层层）显示：两条畸变、良好分离的 TZM 横跨 flake；**TZM 被 AA 斑排斥**；平行 TZM"never couple in real space"📜Q。SI Fig.S2(b) 能带本征态（Δ=0.3 eV）同样显示 TZM 绕过所有 AA 点、且电子型 TZM 波函数集中在顶层面 / 空穴型集中在底层面（layer 极化）📜Q(SI)。

### 2.6 E_F / Δ 依赖、layer/valley 极化与杂质稳健性

- **E_F/Δ 依赖**（Fig.2d/e）：NQCP 出现在正（负）偏压的空穴（电子）激发区；正偏压仅 K 谷态参与输运，反偏压谷指标反转为 K′ → 全可调、**100% valley 极化**电流 📜Q。空穴侧平台质量优于电子侧（electron-hole asymmetry）📜Q。
- **layer 极化**：TZM 波函数集中在底层层 → 与单层 graphene 引线接触更透明（解释平台只在特定极性出现）📜Q。
- **杂质**（SI §VII）：平台对缺陷型杂质（ξ≤a）免疫，只有大 ξ 且放在 TZM 传播路径上才破坏；TZM 展宽 ~75a 使其可绕开短程杂质 📜Q(SI)。对短程杂质的低散射率 → 1D 本质的又一佐证 📜Q。

---

## 3. 理论模型与方法（模型/哈密顿量/推导/计算方法）

### 3.1 器件模型
底 = 未扭转单层 graphene nanoribbon（宽 N，以六角环数计），顶 = 扭转 graphene flake（长 L）；flat boundary 由刻蚀 [39,48,49] 或电栅控 [50,51] 实现；扭心 = 坐标原点 O（顶层层相对逆时针转 θ）📜Q。两端 = 单层 graphene 引线。

### 3.2 哈密顿量（Eq.1，p_z Wannier 基）
三层项：层内 on-site + hopping、层间 hopping；层间偏压以 on-site 能 (−1)^α Δ 计入（α=1/2 = 顶/底层）📜Q。hopping 用 Slater-Koster（Eq.2）：Vppπ(r)=−γ₀ e^{(a−r)q_π/a}、Vppσ(r)=γ₁ e^{(a_I−r)q_σ/a_I}；参数 a=1.418 Å、a_I=3.349 Å、γ₀=2.7 eV、γ₁=0.48 eV、q_π/a=q_σ/a_I=2.218 Å⁻¹，面内 hopping 截断 r_c=3a（SI §I 验证 3a 合理）📜Q。

### 3.3 输运公式（Eq.3，零温 NEGF）
$$G(E_F)=\frac{2e^2}{h}\mathrm{Tr}[\Gamma_L G_C^r \Gamma_R G_C^a]$$
即 Landauer/Meir-Wingreen 形式（SI 引 Meir-Wingreen "Landauer formula"），G₀≡2e²/h，E_F 相对 TBG 电荷中性点 E_CNP≈0.79 eV 📜Q。通道计数/自旋简并约定见 [PHY-LB]。

### 3.4 非平衡 LDOS（SI §IV，Eq.S1–S5）
ρ_NE = 总 LDOS − 平衡 LDOS；经 Keldysh 方程 G^< = G^r Σ^< G^a 与 T=0 化简，小偏压极限 ρ_NE ∝ (μ_L−μ_R)[G^r Γ_L G^a] 📜Q(SI)。用于实空间可视化"哪条模承载净电流"。

### 3.5 能带计算（SI §II）
周期性 TBG moiré 超晶格，commensurate 角 cos θ = (m²+4mn+n²)/2(m²+mn+n²)；θ=0.82° 用 m=40, n=41 → θ_com≈0.8168° 📜Q(SI)。Δ≥0.2 eV 时电子/空穴两侧出现线性色散 TZM 能窗（Δ=0 无）📜Q(SI)。

---

## 4. 关键预言与数据（提取链 + 验证链 + 不确定度标注）

### 4.1 平台值（NQCP）
| 量 | 值 | 证据 | 不确定度 |
|----|----|------|----------|
| NQCP 平台值（总述） | 接近 1、2、3（单位 2e²/h） | 📜Q（摘要） | [~]（作者"close to"） |
| 平台 2 具体值 | ~1.99（θ=0.82°，L=303a） | 📜Q（Fig.2a 正文） | [~]（"around"） |
| 平台 1 具体值 | ~0.999（θ>0.34°） | 📜Q（Fig.3a 正文） | [~]（"around"） |
| 平台 2 的 θ 范围 | 0.76°<θ<0.91° | 📜Q | [~] |
| 更高平台 | 4, 6, 8, …（更宽系统） | 📜Q（作者预言） | 预言 |
| 算例角 | θ=0.82° ↔ commensurate 0.8168°（m=40,n=41） | 📜Q | [~] |

### 4.2 能量/参数
| 量 | 值 | 证据 |
|----|----|------|
| TZM 线性色散能窗宽度 | ~150 meV（Δ=0.3 eV） | 📜Q（Discussion）[~] |
| 库仑能 U_c | ≈25 meV（平带区估计，引 refs 16,65） | 📜Q [~] |
| 层间偏压 | Δ=300 meV（=0.3 eV） | 📜Q |
| 费米能 | E_F=−70 meV（空穴窗中）、−50 meV、+60 meV | 📜Q |
| 电荷中性点 | E_CNP≈0.79 eV | 📜Q |
| TZM 能窗出现阈值 | Δ≥0.2 eV | 📜Q(SI Fig.S2) |
| 杂质 | V₀=2.5 eV，x_im≈500.05 Å，TZM 展宽 75a | 📜Q(SI) |

### 4.3 器件几何
N=121（主算例）、N=209（平台 3）；L=303a（平台 2）/ 603a（平台 1/3）/ 123a（中间长度对照）；扭心 (0,−56√3a)（平台 1）、(0,−100√3a)≈(0,−246 Å)（平台 3）📜Q。

### 4.4 验证链（理论论文 = 计算自洽互验）
- **平台值 ↔ 通道数互验**：~1.99 ↔ 两条纵向 TZM（AA 阵列夹两 TZM）；~0.999 ↔ 单 TZM；平台 3 ↔ 三条 v₁ TZM（SI Fig.S6 LDOS 佐证）📜Q。
- **bulk 通道判别**：平台 1 与 3 共存 → 排除边缘态 📜Q。
- **1D 本质三重佐证**：非平衡 LDOS 图案 + 短程杂质免疫 + AB 振荡 trivial origin 📜Q。
- **能带 vs 输运互验**：SI 能带 TZM 绕过 AA 点 ↔ 器件 Fig.4 实空间 TZM 被 AA 斑排斥 📜Q。

---

## 5. 主要结论（保留作者措辞强度）

1. THS 确实自构 1D 畸变 TZM、绕过 AA 点独立传播（作者 "show"）📜Q。
2. NQCP 平台值接近 1、2、3（单位 2e²/h）——"serves as a strong experimental sign for the existence of TZMs"（作者预言，非已测事实）📜Q。
3. 平台值可由扭转中心垂直位移微调到接近 1 或 3 📜Q。
4. 导电 TZM 全部 valley 极化 → 全可调 100% valley 极化电流（valleytronics 应用）📜Q。
5. "Our findings resolve recent debates on the THSs in biased minimally TBG"——作者自述裁决争议 📜Q。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 无直接电输运实验验证 | NQCP 平台是预言，尚待专门测量 | 📜Q（作者称"strong experimental sign"）/ 💭I |
| 零温 T=0 | 全文 T=0（SI）；有限温效应未算 | 📜Q(SI) |
| 强 e-e 关联未计入 | 作者论证 E_F 远离平带、U_c≈25 meV ≪ 150 meV 能窗，故可忽略 | 📜Q |
| 平台质量对边界/杂质敏感 | NQCP of 2 比 of 1 对纳米flake 边界更敏感；大 ξ 杂质在 TZM 路径上可破坏平台 | 📜Q(SI) |
| 零偏压行为未讨论 | 只处理偏压情形；Δ=0 时无 TZM 线性色散能窗（SI Fig.S2） | 📜Q(SI) + 推导 |
| 通道间耦合无定量参数 | 原文只有定性"coupling becomes stronger/gets eliminated"，**无 t_inter 数值**（旧版 t_inter≈0.05t 已删） | 💭I⚠️（cards.md） |

---

## 7. 与其他工作的关系（跨论文对标，核实自本文引用列表）

| 工作（本文 ref） | 关系 |
|------|------|
| San-Jose & Prada 2013 [28]、Efimkin & MacDonald 2018 [29]（及 [27,30–39]） | 2D 三角网络模型侧（"one THS scattered into three at AA point"）📜Q |
| Tsim, Nam & Koshino 2020 [40]（=T12）、Fleischmann 2020 [41]、De Beule 2020 [42]（=T15） | TZM 预言侧（band-structure + 单参数散射理论）；本文 = 其"完美 TZM"的"畸变 TZM"修正 📜Q |
| Hou et al. 2020 [45]（=T9，metallic network）、Hou 2020 [46]、You 2022 [47] | 网络侧量子输运模拟（topologically equivalent 单层模型）；本文与之"essentially distinct"因捕获了 AA/AB/BA 间平滑过渡 📜Q |
| Martin 2008 [43]、Vaezi 2014 [44] | THS 的 valley Chern 差 ΔC_v=2 来源 📜Q |
| Rickhaus 2018 [38] | FP 振荡观测；本文 1D 通道与之"consistent" 📜Q |
| **Xu 2019 [39]** | **AB 振荡观测；本文称"experimentally observed oscillations may not account for the 2D network model [38,39]"** 📜Q |

> ⚠️ **Phase S 外部对标（非本文原句，💭I）**：① "TZM(T12) 与网络(T9) 是耦合强度的两极限"——原文无此措辞，但原文确实以"纵向 TZM 耦合随 moiré 周期减小而增强"作为平台消失机制（§2.2/2.3）📜Q，故两极限框架是 review 层综合；② **修正附录 B.5**："与 Xu 2019 对标原文无"**有误**——Xu 2019 确在本文引用列表（ref [39]，引于正文 L67、L257），但本文并非"对标/统一解释"，而是主张 Xu/Rickhaus 的振荡"可能不解释为 2D 网络"。

---

## 8. 对后续研究的影响

- 给出 TZM 的明确实验方案：两端 TBG 纳米flake 器件测 NQCP 平台（值近 1/2/3）——比精确量子化更易观测的定量靶 📜Q。
- 100% valley 极化电流 → valleytronics 潜在应用 📜Q。
- 在 2D 平台上实现 1D 导电通道阵列，提供 TBG 内禀拓扑态工程化路径（作者 "provides a way of engineering…"）📜Q。

---

## 9. 理论模型映射（供 TBPM/Kubo-Bastin 计算对标）

| 映射 | 说明 |
|------|------|
| θ → moiré 周期 → AA 阵列间距 | 扭角→moiré 周期→AA 斑阵列（原文**未给 λ 数值**，仅 θ_com=0.8168° commensurate）📜Q/💭I |
| Δ → THS 线性色散能窗 | 层间偏压→TZM 能窗（~150 meV @ Δ=0.3 eV；Δ≥0.2 eV 才出现）📜Q |
| 通道数 → 电导平台值 | 1/2/3 条纵向 TZM → 平台近 1/2/3 × 2e²/h（非精确）📜Q |
| NEGF G=(2e²/h)Tr[Γ_L G^r Γ_R G^a] ↔ Landauer/LB | 通道计数约定见 [PHY-LB] 📜Q |
| 平台 ~1.99 vs 2.00 → 畸变 TZM 弱散射 | TBPM/Kubo 若算出**精确**量子化 → 支持完美 TZM；**完全无平台** → 支持网络；**NQCP（近整数）** → 支持本文（💭I，同旧 note） |

> 与 TBPM/Kubo 对应：本文是有限两端器件的 Landauer/NEGF 透射计算，bulk σ_xx（Kubo）只给背景，复现 NQCP 需有限器件透射（同 E12 §9 注记）💭I。

---

## Phase S 目的接口（三问引用式 + 增量价值）

- **Q1（edge state 如何表征）**：本文用**两端微分电导 G(θ,E_F,Δ)** + **非平衡 LDOS ρ_NE(r)** 表征 TZM——平台数=纵向 TZM 数（近 1/2/3）、平台 1&3 共存判 bulk、LDOS 显示 1D 畸变通道。详见 §2/§4。
- **Q2（理论如何解释/复现）**：紧束缚 + NEGF（Landauer/Meir-Wingreen）量子输运；机制 = AA 点散射规则使 THS 自构 1D 畸变 TZM（vs 2D 网络）。详见 §3。
- **Q3（理论↔实验对应）**：NQCP 平台（近 1/2/3 × 2e²/h）为可检验预言；平台 ~1.99 @ θ=0.82°；1D 通道与 Rickhaus FP 振荡一致 [38]，观测 AB 振荡"may not account for the 2D network model"[38,39]。详见 §4/§7。

> **增量价值**：给 TZM vs 网络之争的裁决性**计算**证据（非平衡 LDOS + NQCP 平台），是 T12（完美 TZM）与 T9（网络）之间的"中间地带"定量靶（~1.99 @ 0.82°，非 2.00）。为项目 TBPM/Kubo 计算提供有限器件 NEGF 对标的 NQCP 判据（量子化 vs 无平台 vs 近量子化三分支）。

## 反向核对 pass (2026-09-02)

pdftotext 提取正文（/tmp/T29.txt, 421 行）+ SI（/tmp/T29_SI.txt, 517 行），逐项 grep 核对：
- ✅ 平台值 1.99 / 0.999 / 近 1,2,3 / 2e²/h / G₀≡2e²/h 均在正文找到（L129/L244/L30–31/L98/L113）。
- ✅ θ=0.82°（L137,187,275）、θ_com≈0.8168°（m=40,n=41，SI L98）、0.76°<θ<0.91°（L125–127）、θ>0.34°（L244–245）。
- ✅ 参数 a=1.418 Å / a_I=3.349 Å / γ₀=2.7 eV / γ₁=0.48 eV / 2.218 Å⁻¹ / r_c=3a（L86–91）；E_CNP≈0.79 eV（L103）；Δ=300 meV（L118）；E_F=−70/−50/+60 meV（L119,235,186）。
- ✅ TZM 能窗 ~150 meV（L273）、U_c≈25 meV（L274）、杂质 V₀=2.5 eV / x_im≈500.05 Å / 展宽 75a（SI L447,453,458）、Δ≥0.2 eV 阈值（SI L135）。
- ✅ 器件几何 N=121/209、L=303a/603a/123a、扭心 (0,−56√3a)/(0,−100√3a)≈(0,−246 Å)（L187,190,233,235,237,241；SI L362）。
- ✅ 4,6,8,…（L208–209）、100% valley 极化（L212）、ΔC_v=2（L59–60）、−120°/+120°（L48–49）。
- ✅ Rickhaus 2018=ref[38]（L258–259）、Xu 2019=ref[39]（L382–387，引于 L67/L257）。
- ⚠️ **新发现并修正**：附录 B.5 "与 Xu 2019 对标原文无"**有误**——Xu 2019 确在本文引用列表（ref [39]），本文明确主张其（与 Rickhaus 的）振荡"may not account for the 2D network model"；已在 §7 更正。
- ✅ 三处旧无源数字仍确认不存在：grep "0.05"=0、"0.1 eV"=0、"0.8"（作为 0.8–0.95 系数）=0（"0.8"仅出现为坐标轴刻度）。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-20 (S-REV) | **§2/§3 删除三处无源数字**："t_inter≈0.05t"（grep "0.05"=0）、"G≈0.8–0.95×N·2e²/h"、"平台宽度~0.1 eV"（grep "0.1 eV"=0）→ 改为原文可验证表述："nearly quantized conductance plateau with its value close to 1, 2, and 3 (in units of 2e²/h)"（grep ✓）与 θ=0.82° 算例平台接近 2 📜Q；TZM 绕过 AA 点独立传播 📜Q。依据：§B.5#3 + cards.md T29。 |
| 2026-08-20 (S-REV) | **"通道间弱耦合"标注 💭I⚠️**：原文未给耦合参数，该定性为 review 层综合。依据：cards.md T29。 |
| 2026-09-02 | **按 4 块辨识结构整体重写**：TL;DR 问题句式 + §1 系统辨识导览（黑箱三要素/四层变量表/判别表置顶/主结果↔判别映射/[前提与限定]）+ §2 结果与机制 + §3 理论模型与方法（理论版）+ §4 关键预言与数据（提取链+验证链+不确定度标注）+ §5–§9 + 目的接口 + 反向核对 pass。全部数字标证据分级 + [~] 不确定度，经 grep 反向核对。 |
| 2026-09-02 | **更正 Xu 2019 引用（新发现）**：附录 B.5 旧记"与 Xu 2019 对标原文无"有误——Xu 2019 确在本文引用列表（ref [39]，正文 L67/L257），本文主张其振荡"may not account for the 2D network model"[38,39]。§7 已改。 |
| 2026-09-02 | **补 SI 方法细节与参数表**（§3/§4）：Slater-Koster 参数（a/a_I/γ₀/γ₁/q 衰减/r_c=3a）、NEGF Eq.3、非平衡 LDOS Eq.S5、commensurate 角 θ_com≈0.8168°、Δ≥0.2 eV 阈值、杂质参数（V₀=2.5 eV/75a 展宽）、边界效应（SI §VI）。 |
| 2026-09-02 | **旧"局限"修正**：删除旧 note "弱耦合参数 t_inter 由拟合决定"（原文无 t_inter，见上文）；"零偏压未讨论"补 SI 依据（Δ=0 无 TZM 能窗）；"通道间耦合两极限（TZM/网络）"降级 💭I 移入 §7。 |
