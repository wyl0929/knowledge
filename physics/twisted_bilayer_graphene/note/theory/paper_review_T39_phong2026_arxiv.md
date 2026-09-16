<!--
 * @Author       : AI 精读 (research_onboarding_skill, Phase 4 → 五块演绎结构重写)
 * @Date         : 2026-08-11（初读）→ 2026-08-20（S-REV 反向核对）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T39_phong2026_arxiv.md
 * @Description  : T39: Phong et al. 2026 — 对称破缺菱方石墨烯畴壁谷阀（理论；2026-09-08 按 5 块演绎结构重写）
-->

# Paper Review: Phong et al. (2026) — 对称破缺菱方石墨烯畴壁谷阀

| 字段 | 内容 |
|------|------|
| **编号** | T39 |
| **标题** | Valley Valves at Domain Walls in Symmetry-Broken Rhombohedral Graphene |
| **作者** | Võ Tiến Phong¹²∗, Francisco Lobo³, Elsa Prada³, Pablo San-Jose³, Francisco Guinea⁴⁵†, Eugene Mele⁶‡ |
| **期刊** | arXiv:2606.14878v2 [cond-mat.mes-hall]（2026-06-24，正文 Dated June 26, 2026） |
| **DOI / arXiv** | arXiv 2606.14878（预印本，无 DOI） |
| **类型** | 理论 — 解析散射 + 对称性分类 + 微观数值（Green 函数 / Caroli-Fisher-Lee）+ BdG 超流 |
| **课题组** | Phong（FSU + NHMFL）/ Prada & San-Jose（ICMM-CSIC）/ Guinea（IMDEA + DIPC）/ Mele（UPenn） |
| **PDF / SI PDF** | ✅ `reference/pdfs/Phong 等 - 2026 - Valley Valves at Domain Walls in Symmetry-Broken Rhombohedral Graphene.pdf`（正文 7 页 + SI I–III：Kekulé 重构对称性分类 / 沿-跨畴壁输运 / 超导模型与超流） |
| **精读日期** | 2026-08-11（初读）→ 2026-08-20（S-REV 反向核对）→ 2026-09-08（五块重写） |

> **结构说明**：本篇按「理论论文演绎结构」五块记（见 `note/shared/method/theory_paper_reading.md` §3）。
> **⚠️ 标题解读**："Valley Valves"的"阀"指**谷间相互作用**——畴壁本身是**不可穿透势垒（两谷皆阻）**，跨壁传输须由谷间混合开启，故"阀"是谷间混合项，**非**单谷过滤（旧笔记"谷过滤效率∝N"为误读，已删）。
> **全文无 ±**：本文数字均为解析/数值设定参数，统一 📜Q[~]。
> **符号防混**：θ = 谷间耦合角度（在 τx,τy 空间旋转），**非**扭角（本文是菱方石墨烯，无扭角）。

---

## TL;DR

**本文想解决的理论问题**：对称破缺菱方多层石墨烯（垂直位移场极化出的**谷-自旋极化金属相**，可凝聚为**手征超导**）中的畴壁，在金属相与超导相分别如何影响输运？跨壁传输由什么介导？

**主结果**：① **谷畴壁是不可穿透势垒**——armchair 畴壁（任意宽度 w≲l）对电子传输完全阻隔（"impenetrable barriers"），即使臂椅方向谷动量投影重合、运动学允许谷混合也如此（解析：K′ 谷为旁观者 r_K′=t_K′=0，|r_K|²=1；N 层与数值 Green 函数均确认，含有限宽度与斜入射）📜Q；② **跨壁传输必须由谷间相互作用介导**——对称性分类给出普适谷间项 τxσ+、τyσ+（对所有 N 对称允许，作用于 A(1) 子格），微观数值模拟证实其使电子跨壁传输（透射率随耦合 m 增大、达共振单位透射/宽壁阈值开关）📜Q；③ **超导相 SNS′ 结**（连接相反手征 p+/p− 超导区）的**明显超流需谷间混合**——m=0 时超流密度被抑制到 ~0.02 nA/nm（但不精确为零，弱违反 Ambegaokar-Baratoff），m 增大则显著放大 📜Q。

**结论/意义**：谷间相互作用是"**阀**"（valve）——控制跨谷畴壁的输运；近期实验 [40] 在谷极化畴间观测到传输特征，强烈暗示谷间混合存在。⚠️ 全文为理论/数值结果（we show / we find = 数学/数值构造，非实验证实）。

---

## 1. 模型白箱（理想系统 + 假设清单）

### 1.1 连续模型（解析散射，正文 Eq. 1–7）

**畴壁与谷极化**（Fig. 1）：armchair 方向畴壁，谷极化 ετ(x) 沿 x 变化：ε_K(x)=ε− (x≤0)、ε_+(x>0)；ε_K′(x)=ε_+(x≤0)、ε_−(x>0)，0<ε−≤ε+（K 谷在 x<0、K′ 谷在 x>0）。

**单层自旋极化低能有效 Hamiltonian**（Eq. 1）：
$$
\hat H_{\tau_z}(x,k_y)=\hbar v_0(-i\partial_x,k_y)\cdot(\tau_z\sigma_x,\sigma_y)+\left(\varepsilon_K(x)\tau_+ + \varepsilon_{K'}(x)\tau_-\right)\sigma_z
$$
σ 作用子格、τ 作用谷空间，τ±=(τ₀±τ_z)/2；先取 ℏv₀=1。

**散射态**（Eq. 3–5）：入射 K 波在 x<0 含 K′ 谷贡献（ψ_A,K′/ψ_B,K′ 带 r_K′ e^{κx x} 指数衰减）。连续性要求下 r_K′=t_K′=0（只要 ε+≠ε−）→ **K′ 谷是旁观者**；入射 K 波完全反射回 K 谷（|r_K|²=1）📜Q。反射/透射系数 r_K、t_K（Eq. 5）显式给出。K 谷的**衰逝模在畴壁处仍携带沿壁电流**，即使 k_y=0：J_y∝(ε_++E)t†_K t_K，类似拓扑绝缘体边界态电流 📜Q。

**N 层推广**（Eq. 6–7）：最小两带模型含 k^N 色散（不含三角翘曲）：
$$
\hat H_{\tau_z}(x,k_y)=\begin{pmatrix}0&(-i\tau_z\partial_x-ik_y)^N\\(-i\tau_z\partial_x+ik_y)^N&0\end{pmatrix}+\left(\varepsilon_K(x)\tau_+ + \varepsilon_{K'}(x)\tau_-\right)\sigma_z
$$
波矢 $k_{\pm n}=\pm E^{1/N}\exp(i\varrho/N+2\pi ni/N)-k_y^2$ 开根（Eq. 7，ϱ∈{0,π}）。左侧 2 传播模（一入一出）+N−1 个可归一衰逝模，右侧 N 个衰逝模（全在 K 谷）；K′ 谷反转。边界处要求波函数及其前 N−1 阶导数连续 → **仍可用纯 K 谷波函数匹配** → 突变畴壁仍完全阻隔 📜Q。

### 1.2 微观模型（紧束缚 + 数值，正文 Eq. 8–9 + SI）

**紧束缚 Hamiltonian**：N 层菱方石墨烯，5 个碳原子跳跃参数 {γ₀,γ₁,γ₂,γ₃,γ₄}（SI Table SIV：γ₀=3100、γ₁=380、γ₂=−15、γ₃=−290、γ₄=−141，单位 meV）📜Q。位移场 = 逐层递增位能，相邻层能差 ∆，在电荷中性点开隙 ~∆(N−1)；∆ 符号约定使导带电子局域在第 1 层 A 子格。**谷极化**用 A(1) 子格上的 Haldane 型次近邻跳跃：
$$
\delta\hat H_{\tau_z}(\mathbf k)=\frac{2m_z}{3\sqrt3}\sum_{j=1}^3\sin[\mathbf k\cdot\mathbf a_j]\sigma_+
$$
（Eq. 8；a_{j+1}=a(cos[2πj/3],sin[2πj/3])，a 晶格常数）。**有限宽畴壁**：m_z(x<−w/2)=m_z、m_z(x>+w/2)=−m_z、m_z(|x|≤w/2)=−2m_z x/w；铁磁畴壁典型宽 w≲10 nm 📜Q。

**输运**：Caroli-Fisher-Lee 公式 $T(E,k_y)=\mathrm{tr}[\Gamma_L G_D\Gamma_R G_D^\dagger]$（Γ 为左右畴的能级宽度函数，G_D 为含自能的畴壁 Green 函数），y 方向周期 → k_y 好量子数 📜Q。

**谷间耦合**（Kekulé 重构）：√3×√3 超胞把 K、K′ 都映到折叠布里渊区中心 Γ̄。对称性分类（正文 Table I + SI Table SII）给出普适谷间项 **τxσ+、τyσ+**（对所有 N 对称允许，仅作用 A(1) 子格）。动量空间正规化：
$$
\delta\hat H_{intervalley}(\mathbf k)=m\left[h_x(\mathbf k)\cos\theta+h_y(\mathbf k)\sin\theta\right]
$$
（Eq. 9；h_x/h_y 为 3×3 矩阵、g(k)=Σᵢ e^{ik·aᵢ}，m 为耦合幅、θ 在 (τx,τy) 空间旋转）。谷间耦合只引入畴壁内部 📜Q。

**BdG 超导模型**（Eq. 10）：quarter-metal 配对 → 对动量 2K±≠0（Kekulé 尺度对密度波）；取 p+（K 谷）/p−（K′ 谷）序参量。BdG Hamiltonian 含 Δ̂SC(k)（3×3，配对仅 A(1) 子格），f(k)=(Δ_SC/2i)[e^{ik·a₁}+ωe^{ik·a₂}+ω†e^{ik·a₃}]、ω=e^{2πi/3}；投影到 K 谷 $\hat\Delta_{SC}(k)\approx 3\Delta_{SC}a(k_x+ik_y)/2$（p+ 相位绕数）📜Q。

### 1.3 参数分册（区分"作者设定" vs "推导所得"）

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | 谷间耦合幅 m、谷间角度 θ、畴壁宽 w、填充密度 n、化学势 µ |
| **固定/设定参数** | N=4（tetralayer，主算例）；∆=30 meV、m_z=10 meV；紧束缚 γ₀=3100/γ₁=380/γ₂=−15/γ₃=−290/γ₄=−141 meV；a=2.46 Å；∆SC=10 meV（Fig. 5）；T=0、η=10⁻⁴ meV |
| **导出量** | 能隙 ~∆(N−1)；|∆C|=2（跨结 Chern 数差）；m*（透射共振临界耦合，宽度依赖） |
| **模型内部量（解的性质）** | 透射率 T(E,k_y)、r_K/t_K、谱函数 A(E,k_y)、超流密度 J(ϕ)、Jc |
| **预言量** | 谷间混合是"阀"；m=0 超流 ~0.02 nA/nm 被抑制；SNS′ 明显超流需谷间混合 |

> **⚠️ 数值张力（反向核对发现）**：正文说"choose ∆SC so that the gap opening is about 1 meV（最佳 Tc~300 mK）"，但 Fig. 5 caption 给 ∆SC=10 meV。两处 📜Q 并存，属预印本内部张力，**不在笔记里调和**（详见反向核对 pass）。
> **符号防混**：θ（谷间耦合角，τx,τy 空间）≠ 扭角（本文无扭角）；m（谷间耦合幅）≠ m_z（谷极化质量/次近邻跳跃强度）≠ m*（透射共振临界值）；∆（位移场层间能差）≠ ∆SC（配对幅）≠ |∆C|（Chern 数差）；σ+（=(σ₀+σ_z)/2，A 子格投影）≠ σ_x/σ_y/σ_z（子格 Pauli）。

### 1.4 显式假设清单（本文结论的前提集合）

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **直畴壁**（armchair/zigzag 两极限，解析连续过渡到一般取向） | 模型 | 📜Q（引言） |
| A2 | **谷-自旋极化 quarter metal**：自旋全极化（聚焦谷自由度）；谷极化能标 ≪ 位移场隙 | 模型 | 📜Q |
| A3 | **两带 k^N 最小模型**（无三角翘曲）——解析部分 | 模型 | 📜Q（Eq. 6） |
| A4 | 0<ε−≤ε+（谷极化幅） | 模型 | 📜Q |
| A5 | **谷间耦合只局域在畴壁内** | 模型 | 📜Q |
| A6 | **p± 配对为假定**（基于对称性假定，**非自洽求解**） | 推导 | 📜Q |
| A7 | **超流计算**：突变相位剖面（无渐变相位）、T=0 | 推导 | 📜Q |
| A8 | 自旋翻转跨壁需额外机制，本文不处理 | 模型 | 📜Q（讨论） |

---

## 2. 推导链（演绎结构：顺论文顺序）

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 前提定理层 | Opacity of abrupt DW | 单层 + N 层模型 | 突变畴壁完全阻隔 | A1/A3/A4、连续性匹配 | 谷极化 |
| 推导层① | Finite-width DW | 紧束缚 + Caroli-Fisher-Lee | 数值确认 T=0（任意宽度/斜入射） | A2、TB 参数 | E 在对谷极化的谱区 |
| 推导层② | Intervalley-coupled DW | Kekulé 重构 + 对称性分类 | 谷间项 τxσ+、τyσ+ 使传输 | 对称性分类（C3/T） | m 有限 |
| 推导层③ | Models of chiral SC | BdG p± | 单位 Chern、单 Majorana 支 | A6 | 全隙 |
| 结论层 | Supercurrent (SNS′) | Eq. 11 超流公式 | m=0 抑制 ~0.02 nA/nm，m 增大放大 | A7、Ambegaokar-Baratoff | w=2 nm |

### 2.1 前提定理层：突变畴壁不可穿透（Eq. 1–7）

- **zigzag 方向**：动量守恒 → 两谷居动量分离能谷 → 完全阻隔（立即可见）📜Q。
- **armchair 方向**：投影谱把两谷映到相同晶体动量（谷混合运动学允许），但解析解（Eq. 3–5）给出 r_K′=t_K′=0（ε+≠ε−）→ 入射 K 波完全反射回 K 谷 |r_K|²=1 📜Q。类比 Weyl 半金属反向速度的透射阻隔（ref 73）。
- **N 层**（Eq. 6–7）：多衰逝模（左 N−1、右 N），但边界匹配仍可纯 K 谷完成 → 突变畴壁完全阻隔 📜Q。

### 2.2 推导层①：有限宽畴壁（微观 TB + Green 函数）

标准 N 层菱方 TB（γ₀–γ₄）+ 位移场（∆）+ Haldane 型谷极化（m_z，Eq. 8）→ 有限宽 w 畴壁（m_z 线性过渡）。Caroli-Fisher-Lee 透射 → **只要 E 在对谷极化的谱区，透射恒为零**（含 k_y=0 与 k_y≠0），验证有限宽度也不破坏阻隔 📜Q。

### 2.3 推导层②：谷间耦合开启传输（Kekulé + 对称性分类）

- 谷间耦合需 Kekulé 型 √3×√3 重构（K、K′ 折到 Γ̄）📜Q。
- 对称性分类（C3 旋转 + 自旋less TR）：普适谷间项 τxσ+、τyσ+（对所有 N 对称允许）📜Q。
- 数值（Fig. 3）：w≲10 nm 时 T 随 m 非线性增大（小 m 二次律）；临界 m*（宽度依赖）→ T→1（共振）；m>m* 振荡。宽壁 w=100 nm：阈值下近零、阈值上突跳到近 1（绝热演化）📜Q。θ 依赖弱；大 µ（两谷皆占）时 T 饱和于 2（两谷散射模）且谷间耦合反而引入散射降低 T 📜Q。

### 2.4 推导层③：手征超导（BdG + Chern + Majorana）

p± 配对（BdG，Eq. 10），$\hat\Delta_{SC}(k)\approx 3\Delta_{SC}a(k_x+ik_y)/2$。p± 全隙超导 generic 单位 Chern 数（数值非阿贝尔 Berry 曲率积分确认）→ 半无限平面边界处单条 Majorana 支穿越能隙 📜Q。

### 2.5 结论层：SNS′ 超流（Eq. 11）

超流 I(ϕ,k_y)=(e/ℏ)∫(dω/2π)n_F(ω)Re Tr[G[γ_z,ΣR]]、J(ϕ)=∫(dk_y/2π)I（Eq. 11）。几何：左 p+ SC（K 谷，相位固定）+ 右 p− SC（K′ 谷，相位可调），畴壁=正常金属宽 w=2 nm。CPR J(ϕ)≈Jc sin(ϕ+ϕ₀)。m≈0：超流密度 ~0.02 nA/nm（被抑制但不精确为零 → 弱违反 Ambegaokar-Baratoff）；m 增大 → 显著放大（与 Ambegaokar-Baratoff 定性一致）📜Q。|∆C|=2 → 两 Majorana 支（同号群速）局域于 NS 边界，CPR 振荡追踪这两支；超流主要来自 Γ̄ 点附近窄 k_y 窗 📜Q。

---

## 3. 结论清单（分层：定理式主张 / 估算 / 预言）

### 3.1 定理式主张（解析/对称性论证的产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 畴壁不可穿透 | armchair 畴壁（任意宽）完全阻隔；K′ 谷旁观者（r_K′=t_K′=0）、|r_K|²=1 | A1/A3/A4 |
| N 层不可穿透 | N 层仍可用纯 K 谷匹配边界 → 突变畴壁阻隔 | A3 |
| 谷间项普适 | τxσ+、τyσ+ 对所有 N 对称允许 | 对称性分类（C3/T） |
| 手征超导拓扑 | p± 全隙超导 unit Chern、单 Majorana 支；跨结 |∆C|=2 → 两 Majorana 支 | A6 |

### 3.2 估算（数值设定/解析判据）

| 估算 | 值 | 证据 |
|---|---|---|
| 主算例参数 | N=4、∆=30 meV、m_z=10 meV、n=5×10¹¹ cm⁻² | 📜Q[~] |
| 谷间耦合 | m=3 meV（Fig. 3/5）；w=2/5/10/100 nm | 📜Q[~] |
| 紧束缚参数 | γ₀=3100、γ₁=380、γ₂=−15、γ₃=−290、γ₄=−141 meV | 📜Q[~]（SI Table SIV） |
| 超流参数 | w=2 nm、T=0、η=10⁻⁴ meV、∆SC=10 meV | 📜Q[~]（Fig. 5） |
| m=0 超流密度 | ~0.02 nA/nm（抑制但非零） | 📜Q[~] |
| 物理能隙 | gap ~1 meV（Tc~300 mK） | 📜Q[~]（正文，与 ∆SC=10 meV 张力见 §1.3 ⚠️） |

### 3.3 预言/主张（保留作者动词强度）

| 预言 | 作者措辞 | 可检验性 |
|---|---|---|
| 谷间混合是"阀" | "they act as a valve to control transport" 📜Q | 中——谷分辨非局域输运 |
| 实验 [40] 传输特征 → 暗示谷间混合 | "strongly suggesting the presence of some form of intervalley mixing" 📜Q | 中 |
| 明显超流需谷间混合 | "we find that intervalley mixing is crucial for supporting an appreciable supercurrent" 📜Q | 中——SNS′ 结测量 |
| 谷间混合微观起源待解 | "poses an important problem" 📜Q | 弱 |

### 3.4 内部验证（自洽核对，非"排除竞争解释"）

1. **解析↔数值互验**：突变畴壁解析（|r_K|²=1）与有限宽 TB/Green 函数（T=0）一致，含斜入射 📜Q。
2. **极限对照**：大 µ（两谷皆占）时谷间耦合反而降低透射（vs quarter-metal 相增强透射）——谷间耦合作用的**符号依赖**对照 📜Q。
3. **超流↔透射对标**：超流放大与正常态透射透明度的增强定性一致（Ambegaokar-Baratoff）📜Q。

### 3.5 概念区分（分类，非溯因排除）

| 区分 | 依据 | 结论 |
|---|---|---|
| 谷阀 ≠ 谷过滤 | 畴壁两谷皆阻（不可穿透），非单谷过滤 | 标题"阀"指谷间相互作用 📜Q |
| zigzag vs armchair | 动量守恒 vs 解析阻隔 | 两极限均阻隔，解析连续 → 一般取向阻隔 📜Q |
| 正常态 vs 超导态 | 传输 vs 超流 | 两者都需谷间混合 📜Q |

---

## 4. 假设-结论依赖图（含金量所在）

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性 |
|---|---|---|---|
| A2 自旋全极化 | 自旋翻转跨壁 | 纯谷自由度描述失效 | 作者明说需额外机制（future study）📜Q |
| A1 直畴壁 | 强弯曲畴壁 | 解析/数值几何模型 | 中等（直壁近似描述 k_F⁻¹≲l≲R 区域）📜Q |
| A3 两带 k^N 无翘曲 | 三角翘曲显著 | 解析阻隔结论的定量细节 | 中等（微观 TB 已含翘曲，数值仍阻隔）📜Q |
| A5 谷间耦合仅局域畴壁 | 谷间耦合遍及体 | 传输图景 | 中等 |
| A6 p± 假定配对 | 实际配对对称性不同 | BdG/Chern/Majorana 结论 | 致命——作者明说"we do not solve for the pairing field self-consistently"📜Q |
| A7 突变相位剖面 | 相位渐变 | 超流定量 | 中等（作者明说 abrupt change 假设）📜Q |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性

- **谷分辨非局域输运**：检验谷畴壁的阻隔与谷间混合开启的传输 📜Q。
- **SNS′ 结超流**：检验明显超流需谷间混合（m=0 抑制 ~0.02 nA/nm vs m 增大放大）📜Q。
- **实验对标**：本文引 ref [40]（近期实验在谷极化畴间观测传输特征）作为谷间混合的间接证据 📜Q。

### 5.2 设计原则（谷阀工程）

谷间混合（原子尺度杂质/无序、注入电流非平衡效应、畴壁内的对称破缺相互作用）作"阀"控制跨壁输运 📜Q。Kekulé 重构是实现谷间混合的对称性途径。

### 5.3 后续文献修正（时间倒挂，💭I）

- **无**（2026 预印本）。
- 与 Phase S 的关系：本文把畴壁物理从 BLG（T1/T5/T6）扩展到**菱方多层 + 谷-自旋极化 quarter metal + 手征超导**；与 T38（BiSb 螺旋畴壁环）同属"畴壁 + 关联/超导"新方向，但体系（菱方石墨烯 vs BiSb）、机制（谷间混合阀 vs SC-pair 隧穿）不同。作者 San-Jose/Prada 即 T5 奠基作者 💭I。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 配对场非自洽 | p± 为对称性假定，未自洽求解 | 📜Q |
| 自旋翻转未处理 | 跨壁自旋翻转需额外机制（future study） | 📜Q |
| 谷间混合微观起源未解 | 实验谷间混合的来源（杂质/非平衡/相互作用）"poses an important problem" | 📜Q |
| ∆SC 数值张力 | 正文"gap ~1 meV" vs Fig. 5 "∆SC=10 meV" 未调和 | 📜Q（见 §1.3 ⚠️） |
| 畴壁宽度依赖未报告 | 超流对畴壁宽的依赖"reported in the future" | 📜Q |
| 预印本 | 未经同行评审 | — |

## 7. 与其他工作的关系（跨论文对标放这里，不放正文）

| 工作 | 关系 |
|------|------|
| ref [40]（实验） | **直接对标**——quarter-metal 手征超导 + 谷极化畴间传输特征 📜Q |
| refs 42–71 | 引用——菱方石墨烯相图/超导模型理论群 📜Q |
| refs 49/59/72 + 60 | 引用——p± 配对对称性的唯象/微观依据 📜Q |
| ref 73 | 引用——Weyl 半金属反向速度透射阻隔类比 📜Q |
| ref 74 | 引用——N 层边界匹配的显式计算 📜Q |

> ⚠️ 本文未引 Barrier 2024（E16）——旧笔记"与 Barrier 2024 互补"无源（继承 2026-08-20 结论）。

## 8. 对后续研究的影响

- 把"畴壁谷阀"概念从 BLG/谷 Chern 框架推广到**菱方多层 + quarter-metal + 手征超导**（交互作用对称性破缺体系）📜Q。
- 确立"谷间混合是跨谷畴壁输运的必要条件"这一通用判据——谷守恒破坏不再是缺陷而是**功能**（阀）📜Q。
- 为实验 [40] 的畴结构观测提供输运理论解释 📜Q。

## 9. 理论模型映射（供 TBPM / Kubo 计算对标）

| 映射 | 说明 |
|------|------|
| 紧束缚 → TBPM | N 层菱方 TB（γ₀=3100/γ₁=380/γ₂=−15/γ₃=−290/γ₄=−141 meV）+ 位移场（∆）+ Haldane 型 m_z（Eq. 8）——直接是 TBPM 输入 📜Q |
| 谷间耦合 → 局域势 | δĤ_intervalley=m[h_x cosθ+h_y sinθ]（Eq. 9），只局域畴壁——TBPM 可在畴壁加局域谷间项 📜Q |
| 透射 → Caroli-Fisher-Lee | T=tr[ΓL G ΓR G†]——与 Kubo/Fisher-Lee 输运接口 📜Q |
| 超流 → BdG | 3×3 Δ̂SC（Eq. 10）+ Eq. 11 超流公式——BdG 输运计算接口 📜Q |

> 本文无量子化电导（4e²/h）讨论；透射率 T（无量纲 0–2）而非电导平台。

---

## Phase S 目的接口（引用式，随项目增删）

- **Q1（edge state 如何表征）**：本文预言畴壁是**不可穿透势垒**（两谷皆阻），跨壁传输须谷间混合——为畴壁输运提供**负性判据**（无谷间混合则无传输）📜Q。
- **Q2（理论如何解释 edge state）**：本文把畴壁解释从"谷 Chern 数差 → 边缘态"（T5/T6）推进到"**谷极化畴壁 = 阻隔 + 谷间混合 = 阀**"——在对称破缺菱方多层体系中的新机制 📜Q。
- **Q3（理论↔实验对应）**：SNS′ 结超流（m=0 抑制 vs m 增大放大）+ 谷分辨非局域输运 ↔ 实验 [40] 的畴传输特征 📜Q。

> **增量价值**：对 Phase S 畴壁主线——把"谷间散射是缺陷（破坏谷保护，T5）"反转为"谷间混合是**功能阀**（开启跨壁输运，T39）"这一概念转折；且把畴壁平台扩展到菱方多层 + 手征超导。与 T5（San-Jose/Prada 2013）同作者系，是谷保护图景的**对偶**（谷守恒 vs 谷间混合）。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` → `/tmp/T39.txt`（+`-raw` → `/tmp/T39_raw.txt`），逐项 grep 核对，**全部数字/短语命中原文**：

| 数字/短语 | grep 位置 | 结论 |
|------|------|------|
| "impenetrable barriers"/"impenetrable boundaries" | 摘要 + 讨论 | ✓（2 命中） |
| "act as a valve"/"valley-valve" | 引言 + 讨论 | ✓ |
| "intervalley mixing" 多命中 | 摘要/正文 | ✓（旧笔记 grep "intervalley"=77） |
| ∆=30 meV、m_z=10 meV | 正文 Fig. 2 caption | ✓ |
| m=3 meV、w=5/10/100 nm、n=5×10¹¹ cm⁻² | Fig. 3 caption | ✓ |
| w=2 nm、T=0、η=10⁻⁴ meV、∆SC=10 meV | Fig. 5 caption | ✓ |
| 0.02 nA/nm | 讨论 | ✓ |
| 1 meV（gap）、300 mK（Tc） | 正文 Models of chiral SC | ✓ |
| γ₀=3100/γ₁=380/γ₂=−15/γ₃=−290/γ₄=−141 meV | SI Table SIV | ✓ |
| a=2.46 Å | SI S1 | ✓ |
| N=4（tetralayer） | 正文 | ✓ |
| |∆C|=2、unit Chern、single Majorana branch | 正文 | ✓ |
| "we do not solve for the pairing field self-consistently" | 正文 | ✓ |
| "Recent experiments [40] find transport signatures" | 讨论 | ✓ |

⚠️ **确认/降级**：① 旧版 "谷过滤效率接近 100%（∝N）/电场开关" 无源已删（继承 2026-08-20）——实际是两谷皆阻的势垒；② 旧版 "与 Barrier 2024 互补" 无源已删；③ **新发现数值张力**：正文"gap opening ~1 meV"（因 Tc~300 mK）vs Fig. 5 "∆SC=10 meV"——两处 📜Q 并存未调和，已在 §1.3 ⚠️ 标注，不在笔记里调和。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-20 | （S-REV）§1–§3/Q2 重写：旧版"谷过滤效率接近 100%（∝N）/电场开关"无源 → 改原文：谷畴壁为不可穿透势垒（两谷皆阻），跨壁传输须谷间相互作用介导（grep "impenetrable"=2）；SC 相 SNS′ 结超流需谷间混合。标题 "Valley Valves" 的"阀"指谷间相互作用，非单谷过滤。§3 删"与 Barrier 2024 互补"（跨论文迁移）。依据：appendix_B §B.5#32。 |
| 2026-09-08 | **按五块演绎结构整体重写**（应用户要求）。旧版归档 `archive/paper_review_T39_phong2026_arxiv.backup_20260908.md`。补全：模型白箱（Eq. 1–11 + 紧束缚参数 γ₀–γ₄ + 参数分册 + 8 条假设清单）、推导链 5 层、结论分层、假设-结论依赖图、接口、理论模型映射、Phase S 三问。**新增发现**：∆SC 数值张力（正文 gap~1 meV vs Fig.5 ∆SC=10 meV）标注；紧束缚参数 Table SIV 补齐。全部数字 grep 命中。 |
