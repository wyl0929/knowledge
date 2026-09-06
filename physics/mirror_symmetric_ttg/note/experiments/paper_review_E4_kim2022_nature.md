<!--
 * @Author       : paper-reading SKILL (deep literature reading)
 * @Date         : 2026-09-04
 * @Description  : E4: Hyunjin Kim et al. (2022) Nature — 魔角三层石墨烯非常规超导的 STM 谱学证据（节点/无节点转变 + peak-dip-hump，4 块辨识结构）
-->

# Paper Review: Kim et al. (2022) — Evidence for unconventional superconductivity in twisted trilayer graphene

| 字段 | 内容 |
|------|------|
| **编号** | E4 |
| **标题** | Evidence for unconventional superconductivity in twisted trilayer graphene |
| **作者** | Hyunjin Kim, Youngjoon Choi, Cyprian Lewandowski, Alex Thomson, Yiran Zhang, Robert Polski, Kenji Watanabe, Takashi Taniguchi, Jason Alicea, Stevan Nadj-Perge（H.K. 与 Y.C. 共同第一作者） |
| **期刊** | Nature 606, 494–500 (2022)（Received 2021-09-20；Accepted 2022-04-01；Published online 2022-06-15）📜Q(正文页眉/页脚) |
| **DOI / arXiv** | 10.1038/s41586-022-04715-z（⚠️ 正文无 arXiv 号，标外部来源） |
| **类型** | 实验 — 扫描隧道显微/谱学（STM/STS）+ 点接触谱学（PCS） |
| **课题组** | S. Nadj-Perge（Caltech，STM 主导）+ J. Alicea（Caltech，理论 C.L./A.T.） |
| **PDF / 文本** | ✅ PDF（references/exp/）；提取文本 /tmp/msTTG_txt/E4_kim2022.txt（正文+Methods+ED 图注，**不含 SI**） |
| **精读日期** | 2026-09-04 |

> **体系对应**：本文 "MATTG（magic-angle twisted trilayer graphene，三层交替扭转、第一/三层对齐、中层转 θ）" = 本项目 msTTG 构型 (0°, θ, 0°)（镜面对称/交替扭转族）。全文为单一来源事实层笔记；通用物理不在此复制（FRESH pack：暂无 [PHY-*] 锚点）。阅读目的见文末「目的接口」（Q1 实验现象 + Q3 配对机制入口）。

---

## TL;DR

**本文想解决的问题**：MATTG（msTTG）在空穴掺杂关联区是否超导？若超导，其谱学证据（能隙、相干峰、温度/磁场响应）指向**常规还是非常规**超导？掺杂如何改变配对态（有无 gate 可调的节点/无节点转变），以及配对是否由玻色模强耦合驱动？（"问题"句式：把"msTTG 超导的配对机制是什么"落到可测的隧穿谱判据上。）

**主结果**：在密度窗约每 moiré 单胞 2–3 个空穴（−3 ≲ ν ≲ −2）📜Q(摘要) 内，隧穿电导在费米能处出现明显凹陷（谱隙），两侧伴对称相干峰；相干峰随温度升高至 2–2.5 K（≈输运最大 Tc）逐渐被抑制、随面外磁场（至 1 T）大幅减弱，点接触谱学独立观测到 Andreev 反射 📜Q(正文+Methods)。相干峰间距 2Δ 给出最大 Δ ≈ 1.6 meV（ν ≈ −2.4），对应 2Δ/kBTC ≈ 15–19（远大于 BCS 值 ~3.5）📜Q[~](正文)。谱形随掺杂从 **U 形**（−2.4 ≲ ν < −2.2）演化到 **V 形**（−3 ≲ ν ≲ −2.4），V 形谱可由**节点序参量**的 Dynes 公式拟合（例 Δ = 0.67 meV、Γ = 39 μeV 📜Q(Fig.3c 面板标注)），而各向同性 s-wave 拟合显著更差 📜Q(正文+ED Fig.9–11)；作者把这一转变解释为**共享节点序参量**的 gapped BEC → gapless BCS 转变 📜Q(正文)。同一掺杂窗还观测到 **peak–dip–hump** 结构，其玻色模能量 Ω 满足 Ω/2Δ 与 Δ 反相关且 ≤ 1，指向电子集体模（但不排除低能声子）📜Q(正文+Fig.4)。

**结论/意义**（保留作者措辞强度）：作者把四类签名列为超导"非常规性"证据——(1) 相干峰受温度/磁场抑制但 persist well beyond the BCS limit；(2) pseudogap-like 区（T* ≈ 7 K > Tc）；(3) dip–hump 结构；(4) 谱不能由 s-wave 拟合、而与 gate-tuned gapped BEC → gapless BCS（共享节点序参量）转变相容 📜Q(正文结论段)。措辞为 "provide unambiguous spectroscopic evidence of the unconventional nature of MATTG superconductivity"📜Q，但配对机制（电子集体模 vs 声子）明确未定论："Future theories addressing properties (1)–(4) will probably be needed to pinpoint the exact mechanism"📜Q。

---

## 1. 系统辨识导览（判别表为全文唯一权威）

**黑箱三要素**：`{VGate(填充 ν)、VBias、面外磁场 B(T)、温度 T(K)、样品(θ) | 归一化 dI/dV 谱（谱隙 Δ、相干峰、dip–hump）、Landau fan、PCS 零偏压电导 | MATTG 空穴掺杂 −3<ν<−2 区间存在非常规超导，且有 gate 可调的 gapped→nodal（U→V）转变}`

**四层变量图**（符号层一次钉死）：

| 层 | 本文实例 |
|----|----------|
| **L1 旋钮 u** | VGate（决定填充 ν）、VBias（隧穿偏压）、面外磁场 B（0→1 T 主序列；至 4 T/8 T 的 ED 数据）、温度 T（400 mK→7 K） |
| **L2 导出量 x₁** | 填充因子 ν（Landau fan 或满填充/CNP LDOS 抑制标定，两法偏差 ≤5% 📜Q(Methods)）；扭角 θ̂（由 moiré 波长反推，±0.01° 📜Q(Methods)）；能隙 Δ̂（相干峰间距一半 或 nodal fit）；玻色模能量 Ω̂ = Π̂ − Δ̂（dip–hump 位置减能隙） |
| **L3 模型量 x₂** | 候选序参量族 {各向同性 s-wave, s+id, d+id, nodal(d 波类)}；BEC vs BCS 图像（化学势 μ 在关联绝缘体能隙内 ↔ 在带内，模型取 μ = −0.2 meV 与 −1.2 meV 📜Q(Fig.3i,j 面板标注)）；玻色模来源 {电子集体模, 低能声子}；Hartree 修正带结构 |
| **固定参数（非旋钮）** | 石墨烯晶格常数 a = 0.246 nm；moiré 波长 LM ≈ 9 nm（θ = 1.5°）；石墨烯费米速度 vF = 1.14 × 10⁶ m/s（Fig.2i 读值）；样品 θ ≈ 1.5°（各数据集 1.42°–1.57°，见 §4） |
| **反推量 θ̂** | Δ(ν)（相干峰间距/2 或 nodal fit，误差棒 = 分辨率 0.1 meV + 拟合标准误差 📜Q(Fig.3 图注)）；Ω(ν) 与 Ω/2Δ；Tc ≈ 2–2.5 K、T* ≈ 7 K、Bc ≳ 1 T |
| **L4 观测量 y** | 归一化 dI/dV(VBias) 谱；相干峰幅度；零偏压电导；Landau fan（LDOS vs ν, B）；PCS dI/dV 零偏压增强（Andreev） |

**可辨识性判别表**（每条判别 = 判据 / 排除谁 / 确立谁）：

| 判别 | 判据（数据） | 排除谁 | 确立谁 |
|------|-------------|--------|--------|
| **D1** 相干峰来自超导（非关联绝缘体/量子点/杂质） | 对称相干峰 pinned 于 VBias = 0，出现在 −3 < ν < −2.2 📜Q(正文+Fig.3)；温度升高至 2–2.5 K 逐渐消失、零偏压电导回升 📜Q(正文+Fig.3d,e)；磁场至 1 T 相干峰大幅减弱 📜Q(正文+Fig.3g)；PCS 独立观测 Andreev 反射（零偏压增强仅出现在谱隙+相干峰共存区，且被磁场/温度抑制）📜Q(Methods+ED Fig.6)；相干峰落在输运超导填充范围 📜Q(正文) | 关联绝缘体（ν≈−2 附近 gap 非对称 + Coulomb diamonds + 量子点，ED Fig.4）；杂质/结构伪迹 | 谱学超导签名（gap + 相干峰） |
| **D2** 超导为强耦合/非常规（非弱耦合 BCS s-wave） | 2Δ/kBTC ≈ 15–19（Tc ≈ 2–2.5 K）远大于 BCS ~3.5；即使用 nodal fit 的较小 Δ 仍 2Δ/kBTC ≈ 10 📜Q[~](正文)；相干峰 persist well beyond the BCS limit、并有 pseudogap-like 区（T* ≈ 7 K > Tc）📜Q(正文结论段)；V 形谱不能由各向同性 s-wave 拟合 📜Q(ED Fig.9–11) | 弱耦合 BCS s-wave 超导 | 强耦合超导 + 非常规谱学性质 |
| **D3** gate 可调 gapped→nodal（U→V）转变 | U 形（−2.4 ≲ ν < −2.2）→ V 形（−3 ≲ ν ≲ −2.4）📜Q(正文+Fig.3a)；V 形谱用节点 Dynes 拟合、各向同性 s-wave 拟合显著更差（U 形区亦然，需 s+id/d+id 或 nodal）📜Q(正文+SI4 引用+ED Fig.9–11)；磁场对 V 形能隙抑制更高效 📜Q(正文+ED Fig.7)；BEC–BCS 模型（μ = −0.2 meV gapped ↔ μ = −1.2 meV nodal）定性复现 U/V 谱 📜Q(正文+Fig.3k,l) | 贯穿全区间的单一各向同性 s-wave 序参量；"两相都 fully gapped"的普通 BEC–BCS crossover 📜Q(正文) | 两个不同超导区 + gapped/gapless 转变；与共享节点序参量的 BEC→BCS 转变相容 |
| **D4** 强耦合玻色模（配对"胶水"） | peak–dip–hump 位于 Π = Δ + Ω 📜Q(正文)；正/负偏压 dip 对称且与填充无关 → 排除背景 DOS 内禀结构 📜Q(正文)；V 形区 Ω/2Δ 与 Δ 反相关且上界 ≤ 1 📜Q(正文+Fig.4c) | 背景态密度内禀 dip–hump；无玻色模的弱耦合图像 | 电子–玻色子强耦合；倾向电子集体模（但低能声子未排除）📜Q(正文+Methods) |

> **主结果 ↔ 判别表映射**：主结果①（谱学超导签名：gap+相干峰+Andreev）← {D1}；主结果②（强耦合/非常规：2Δ/kBTC、pseudogap、非 s-wave）← {D2}；主结果③（U→V gapped→nodal 转变 + BEC–BCS 图像）← {D3}；主结果④（peak–dip–hump 玻色模）← {D4}。
> **分层排除注**：D1 先证"存在超导"（vs 关联绝缘体/杂质）；D2 证"非常规/强耦合"（vs 弱耦合 BCS）；D3 证"序参量在掺杂下 gapped↔nodal 转变"（vs 单一 s-wave / 普通 crossover）；D4 证"有玻色模耦合"（vs 无胶水图像）。每步只证一层；配对机制（电子 vs 声子）作者明示未定论 📜Q。

> **[前提与限定]**（判别结论的适用范围）：
> - **噪声/扰动**：单器件（多处不同 θ 区域数据点）；全部特征经 >10 支微针尖确认 📜Q(Methods)；零偏压漂移约 100 μV 需校正 📜Q(Methods)；能隙误差棒 = 实验分辨率 0.1 meV + 拟合标准误差 📜Q(Fig.3 图注)；基温 T = 400 mK（Pb(110) 标定，ED Fig.9a）。
> - **判别性扫轴**：VGate 全程扫（−15 → 15 V，ν = −4 → +4）；B 主序列 0 → 1 T（Fig.3g），ED 另至 4 T（谱隙持续 B ≳ 4 T，ED Fig.7f,g）、8 T（LL 分析，ED Fig.3）；T 扫 0.4 → 7 K（Fig.3d）；**位移场 D 未作为旋钮**（仅单石墨背栅，无顶栅——可调性论点依赖他文 Park 2021/Hao 2021，本文只引证，见 §7）。
> - **候选集 M 边界**：序参量只与 {各向同性 s-wave, s+id, d+id, nodal(d 波类)} 比对；配对机制在 {电子集体模, 低能声子} 间未定论（作者明说 "cannot rule out low-energy phonons"📜Q）；电子侧（+2 < ν < +3）能隙属 pseudogap 还是超导未定、需进一步研究（ED Fig.8 图注）；BEC–BCS 判读为**现象学模型**（Supplementary Information 5B），非第一性配对机制。

三层标注：📜Q = 原文事实（附位置）｜推导｜📊F = 读图估算｜💭I = 推断。**不确定度（正交轴）**：[±] 原文误差棒 / [~] 原文无误差棒 / [读图] 图提取·色标值 / [相对] 仅相对量。所有数字经 pdftotext + grep 反向核对（见文末 pass）。

---

## 2. 结果与机制（按论文自身论证结构：体系确认 → 超导谱学签名 → U→V 转变 → peak–dip–hump）

### 2.1 体系确认：mirror-symmetric A–tw–A 堆垛 + 关联 + 附加 Dirac 锥（Fig. 1–2）
- 三层石墨烯交替扭转 θ = 1.5°，形成单一 A–tw–A 构型（第一/三层对齐、中层转 θ）📜Q(正文)。moiré 波长 LM = a/(2 sin(θ/2)) ≈ 9 nm（a = 0.246 nm）📜Q[~](正文)；大尺度 topography 见条纹状畴界（相距约 100 nm，290 nm×80 nm 视场），作者归因于维持 A–tw–A 堆垛的原子重构 📜Q(正文+Fig.1b)。
- 关联信号：CNP 处两 VHS 分离相对 ν = ±4 满填充约 **fivefold** 增大 ⇒ 部分填充平带结构主要由电子关联决定（类比 MATBG）📜Q[~](正文)；伴随 flavour-symmetry-breaking cascade 相变 📜Q(正文+Fig.1f)。
- 附加 Dirac 锥：ν = ±4 处 LDOS 未被完全抑制、无量子点形成（区别于 MATBG），表明平带与远程色散带之间有 gapless 态 📜Q(正文+ED Fig.1)。Landau fan 从 ν = 0, ±4 及 ±1, ±2 发出；主 fan 序列从 ν = +4 为 +2, +6, …（ν = −4 为 −2, −6, …），Chern 数相对 MATBG 偏移 2，源于附加 Dirac 锥的第零 Landau 能级 📜Q[~](正文+Fig.2a)。有限场谱分辨 N = 0, ±1, ±2 … LL，由 LL 间距随场增大确认线性色散、得石墨烯费米速度 vF = 1.14 × 10⁶ m/s 📜Q[~](Fig.2i 读值)。
- Hartree 修正（band-flattening）：平带态权重局域于 AAA 位，Dirac 锥与 γ 点附近平带态更均匀（ED Fig.2）；静电掺杂产生 Hartree 势修正带结构并推动 Dirac 锥相对平带移动，Dirac 点位置落在 ±50 meV 内 📜Q[~](Methods)。实验谱（Fig.2e–h）与含 Hartree 修正的计算 DOS 吻合良好 📜Q(正文)。

### 2.2 超导谱学签名 near ν = −2（Fig. 3a–g）
- 掺杂范围 −3 ≲ ν ≲ −2 分两区：−2.1 < ν < −1.9 为关联绝缘体（关联诱导 gap + Coulomb diamonds + 近水平共振峰 → 量子点，ED Fig.4）；−3 < ν < −2.2 为超导区，隧穿电导极小被 pin 在费米能（VBias = 0）且两侧对称相干峰 📜Q(正文+Fig.3b,c)。
- 相干峰 = 超导第一线索：出现在输运超导填充范围、且 PCS 独立观测 Andreev 反射（Methods + ED Fig.6）📜Q(正文)。
- 温度依赖（Fig.3d–f）：相干峰随升温至 2–2.5 K（≈输运最大 Tc）逐渐消失；空穴侧相干峰在 Tc ≈ 2–2.5 K 完全消失、零偏压电导回升；受抑制零偏压 + 展宽电子侧相干峰存活至更高温，两者都在 T* ≈ 7 K 才被洗掉 📜Q[~](正文+Fig.3 图注)。相干峰消失后持续的谱隙抑制 → 解读为 pseudogap（类比铜氧化物/无序薄膜）📜Q(正文)。
- 磁场依赖（Fig.3g，ED Fig.7）：相干峰高度随 B 增大下降；1 T 时大幅减弱 ⇒ Bc ≳ 1 T（ν ≈ −2.4）📜Q[~](正文)。与输运 ξGL ≈ 12 nm 经朴素估计 Bc ≈ Φ₀/2πξGL² ≈ 2 T 相容 📜Q[~](正文+refs)。无相干峰的 LDOS 抑制持续到更高场（ED Fig.7f,g：B ≳ 4 T）。

### 2.3 U 形 → V 形能隙转变：gapped → nodal（Fig. 3b,c,h–l）
- 谱形从 U 形（−2.4 ≲ ν < −2.2）演化为 V 形（−3 ≲ ν ≲ −2.4）⇒ 两个不同超导区 📜Q(正文)。磁场对 V 形能隙的抑制比 U 形更高效（ED Fig.7）📜Q。
- V 形谱类似铜氧化物，可用带**节点序参量**的标准 Dynes 公式很好拟合（例 Fig.3c：Δ = 0.67 meV、Γ = 39 μeV）📜Q[~](正文+Fig.3c 面板标注)；U 形谱的增强抑制提示 fully gapped 超导态开始 📜Q(正文)。
- 序参量对称性判别：即使在 U 形区，各向同性 s-wave 拟合显著差于 s+nodal 混合或 d+id 序参量拟合（ED Fig.9–11，SI4）📜Q(正文)。
- 能隙幅度：相干峰间距 2Δ 给出最大 Δ ≈ 1.6 meV（ν ≈ −2.4），掺杂依赖与输运 Tc 相似（同在 ν ≈ −2.4 峰）📜Q[~](正文+Fig.3h)。nodal fit 的 Δ 比相干峰估计小 10–30% 📜Q[~](正文)。2Δ/kBTC ≈ 15–19（Tc ≈ 2–2.5 K）；即便用较小估计仍 ≈ 10，远大于 BCS ~3.5 ⇒ 强耦合 📜Q[~](正文)。测得谱隙给出自旋单态超导最大 Pauli 极限约 10 T 📜Q[~](正文)。
- BEC–BCS 解释（作者提出的另一种图像）：U→V 可理解为**共享节点序参量**的 BEC（化学势在关联绝缘体能隙内，fully gapped，Fig.3i,k）→ BCS（化学势进入带内，gapless nodal，Fig.3j,l）转变，而非两相都 gapped 的普通 BEC–BCS crossover 📜Q(正文+SI5B)。现象学模型（电子/空穴带 + 掺杂依赖带分离 + 节点配对，μ = −0.2 meV 与 −1.2 meV）定性复现 U/V 谱 📜Q(正文+Fig.3i,j,k,l)。

### 2.4 peak–dip–hump：玻色模耦合（Fig. 4）
- 相干峰邻接处观测到 dip–hump 特征，广掺杂范围持续；正/负偏压 dip 在能量上对称、与填充无关 ⇒ 排除背景态密度内禀结构 📜Q(正文+Fig.4a)。
- dip–hump 位置 Π = Δ + Ω（Ω = 玻色模能量），提取 Ω = Π − Δ 随掺杂变化且与 Δ 相关 📜Q(正文+Fig.4b)。V 形区 Ω/2Δ 与谱隙反相关（类铜氧化物/铁基），且上界 ≤ 1 📜Q(正文+Fig.4c)。Ω/2Δ ≤ 1 提示配对胶水来自电子自由度相关的集体模，但作者明确不排除低能声子 📜Q(正文+Methods)。U 形区 Ω/2Δ 无清晰反相关，或因 BEC 相提取真实序参量的困难 📜Q(正文)。

---

## 3. 实验方法

### 3.1 器件与样品
- PDMS 辅助 stack-and-flip：约 30 nm hBN + 单层石墨烯；PC/PDMS 印章在 90 °C 拾取 hBN、40 °C 撕裂并扭转石墨烯；PC 溶于 NMP、IPA 清洗；最终 PDMS 真空数日；转移至带石墨背栅 + 金电极的芯片，MATTG 经石墨片接电极 📜Q(Methods)。
- 器件为**单背栅**（graphite/hBN/TTG 堆叠），无顶栅 → 本文不做位移场 D 调控（可调性论点引证 refs 1,2）📜Q(Methods)。
- 多区域/多样品 θ：主文 1.51°（Fig.1f/3a）、1.46°（Fig.2c,d）；100×100 nm² 区域平均 θ = 1.48 ± 0.03°（Fig.2 图注）；其余数据集 1.42°–1.57°（ED Fig.6/7/8）。同一堆叠中另有 TBG 双层区（θ = 1.44°，ED Fig.1a）作对照。

### 3.2 STM/STS 测量
- Unisoku USM 1300J STM/AFM，Pt/Ir 针尖；所有特征 >10 支不同微针尖复现 📜Q(Methods)。默认 dI/dV 参数 VBias = 100 mV、I = 1 nA、锁相 Vmod = 0.2–1 mV、f = 973 Hz 📜Q(Methods)。压电扫描器以 Pb(110) 晶格标定、并经碳原子间距验证；扭角不确定度 ≈ ±0.01°（由 topography moiré 波长测定）📜Q(Methods)。

### 3.3 填充因子标定
- Landau fan 图（同前作）或满填充/CNP LDOS 抑制特征；两法偏差通常 ≤5% 📜Q(Methods)。

### 3.4 点接触谱学（PCS）
- 大幅减小针尖–样品距离进入点接触区（针尖–样品电阻 10–100 kΩ），搜索 Andreev 反射：VBias = 0 mV 附近增强电导仅出现在 −3 < ν < −2.2、被面外磁场与升温抑制；ν ≈ −2 关联绝缘体区零偏压电导显著降低（相对 VBias = 1 mV）📜Q(Methods+ED Fig.6)。

### 3.5 零偏压校正
- 部分谱存在约 100 μV 量级的零偏压漂移（电子学漂移），校正为"电流为零处即真零偏压"📜Q(Methods)。

### 3.6 图像/谱分析
- 谱归一化：除以多项式背景（SI4）；Dynes 公式拟合同一并提到最小二乘/χ²（ED Fig.9–11 图注）；能隙误差棒 = 分辨率 0.1 meV + 拟合标准误差 📜Q(Fig.3 图注)。

---

## 4. 关键数据（提取链 + 验证链 + 不确定度标注）

### 4.1 能隙 / 温度 / 磁场参数表

| 量 | 值 | 证据/不确定度 |
|---|---|---|
| 最大能隙 Δ | ≈ 1.6 meV（ν ≈ −2.4，相干峰间距一半） | 📜Q[~](正文+Fig.3h) |
| 能隙误差棒 | 分辨率 0.1 meV + 拟合标准误差 | 📜Q[~](Fig.3 图注) |
| 2Δ/kBTC | ≈ 15–19（Tc ≈ 2–2.5 K）；用 nodal Δ 仍 ≈ 10；BCS 参考 ~3.5 | 📜Q[~](正文) |
| nodal Δ（nodal fit 相对相干峰） | 小 10–30% | 📜Q[~](正文) |
| Pauli 极限（自旋单态） | 约 10 T | 📜Q[~](正文) |
| Tc | ≈ 2–2.5 K（相干峰消失；输运最大 Tc） | 📜Q[~](正文) |
| T* | ≈ 7 K（零偏压电导回到隙外值的 90%） | 📜Q[~](正文+Fig.3e) |
| Bc | ≳ 1 T（ν ≈ −2.4，相干峰 1 T 大幅减弱） | 📜Q[~](正文) |
| Bc 朴素估计 | Φ₀/2πξGL² ≈ 2 T（ξGL ≈ 12 nm，输运 ref） | 📜Q[~](正文，推导) |
| 温度序列 | 0.4 / 2 / 3 / 4.5 / 5.6 / 7 K | 📜Q[~](Fig.3d 图注) |
| 磁场序列 | 0/100/200/300/400/600/800/1000 mT | 📜Q[~](Fig.3g 图注) |
| 谱隙持续场 | B ≳ 4 T（θ = 1.54° 区域，ED Fig.7f,g） | 📜Q[~](ED Fig.7 图注) |

### 4.2 Dynes 拟合参数表（ED Fig.9 面板标注，均 📜Q[~](ED Fig.9 图注)）

| 场景 | 参数 |
|---|---|
| V 形区节点拟合（Fig.3c, VGate = −9.1 V） | Δ = 0.67 meV、Γ = 39 μeV |
| V 形区节点拟合（VGate = −8.4 V 附近） | Δ = 1.44 meV（ED Fig.9h）；Δ = 1.26 meV（ED Fig.9k，VGate = −8.4 V） |
| U 形区 s+id 拟合 | Δs = 0.88 meV、Δd = 1.10 meV、Γ = 135 μeV（⚠️ 提取文本显示 "135 eV"，μ 疑被 pdftotext 丢失，见更正日志） |
| U 形区 d+id 拟合 | Δd1 = 0.85 meV、Δd2 = 1.35 meV、Γ = 135 μeV（同上 ⚠️） |
| Pb(110) 基温标定（双 gap） | Δ1 = 1.42 meV、Δ2 = 1.26 meV、Γ = 10 μeV |
| BEC/BCS 模型化学势（Fig.3i,j 面板标注） | μ = −0.2 meV（BEC）与 μ = −1.2 meV（BCS） |

### 4.3 样品 / 几何参数表

| 量 | 值 | 证据/不确定度 |
|---|---|---|
| 扭角 θ（主文数据） | 1.5°（正文）；1.51°（Fig.1f/3a）；1.46°（Fig.2c,d）；区域平均 1.48 ± 0.03°（100×100 nm²） | 📜Q[~](正文+Fig.2 图注)；[±] 用于 1.48 |
| 其他数据集 θ | 1.42°（ED Fig.6）、1.44°（TBG 区对照 + PCS，ED Fig.1/6）、1.45°（TTG 对照，ED Fig.1b）、1.54°（ED Fig.7）、1.57°（ED Fig.8） | 📜Q[~](ED 图注) |
| 扭角不确定度 | ±0.01° | 📜Q[~](Methods) |
| 石墨烯晶格常数 a | 0.246 nm | 📜Q[~](正文) |
| moiré 波长 LM | ≈ 9 nm | 📜Q[~](正文+Fig.1c) |
| 费米速度 vF | 1.14 × 10⁶ m/s | 📜Q[~](Fig.2i 读值) |
| 视场/尺度 | 290 nm×80 nm（畴界）；26 nm×26 nm（moiré）；scale bar 50/10/0.5 nm | 📜Q[~](Fig.1 图注) |
| 畴界间距 | ≈ 100 nm | 📜Q[~](正文) |

### 4.4 验证链（互验/多手段/旋钮依赖）
1. **多手段互验**：STM 谱隙 + 相干峰（Fig.3）与 PCS Andreev 反射（ED Fig.6）独立确认超导；输运 Tc（refs 1,2）与谱学 Tc ≈ 2–2.5 K 一致 📜Q。
2. **多针尖复现**：全部特征 >10 支微针尖 📜Q(Methods)；多区域 θ（1.42°–1.57°）重复观测 gap/相干峰/dip–hump（ED Fig.6/7/8）📜Q。
3. **旋钮依赖**：温度（0.4→7 K）抑制相干峰、磁场（0→1 T）抑制相干峰、VGate 开关谱隙（仅 −3<ν<−2.2 有对称相干峰）⇒ 电子/超导起源（D1）📜Q。
4. **填充标定交叉**：Landau fan 与满填充/CNP 特征两法 ≤5% 📜Q(Methods)。
5. **序参量判别交叉**：同一数据用各向同性 s-wave vs nodal vs s+id/d+id 多模型拟合并报 χ² 对比（ED Fig.9–11），非单模型断言 📜Q(ED 图注)。

---

## 5. 主要结论

1. MATTG（msTTG）在 −3 < ν < −2（每单胞 2–3 空穴）呈现谱学超导签名：费米能处谱隙 + 对称相干峰 + 独立 Andreev 反射；相干峰随温度（至 2–2.5 K）与磁场（至 1 T）受抑制 📜Q。
2. 该超导是强耦合/非常规的：2Δ/kBTC ≈ 15–19 ≫ BCS、pseudogap-like 区（T* ≈ 7 K）、且谱不能由各向同性 s-wave 拟合 📜Q。
3. 掺杂驱动 U 形（gapped）→ V 形（nodal）转变，与共享节点序参量的 BEC→BCS 转变相容 📜Q。
4. peak–dip–hump 表明配对由玻色模强耦合驱动；Ω/2Δ ≤ 1 且与 Δ 反相关倾向电子集体模，但低能声子未排除 📜Q。
5. 作者总称四类签名构成 MATTG 超导非常规性的"unambiguous spectroscopic evidence"，但配对机制留待未来理论 📜Q(结论段措辞)。

---

## 6. 局限与未解决

- **单器件/单栅**：全部结论来自单一器件（多区域 θ），且无顶栅 → 本文不涉及位移场 D 可调性；"gate-tunable 转变"实为**掺杂（VGate）可调**，非 D 场可调 📜Q(Methods)+💭I。
- **配对机制未定论**：电子集体模 vs 低能声子（作者明说不能排除声子）；"pairing glue" 是从 Ω/2Δ ≤ 1 的间接论证，非直接证据 📜Q(正文+Methods)。
- **BEC–BCS 为现象学模型**：SI5B 的模型是构造性复现（电子/空穴带 + 掺杂依赖带分离 + 节点配对），非从第一性原理推导；作者也承认 U 形区 Ω/2Δ 无清晰反相关或因提取序参量困难 📜Q(正文)。
- **电子侧未定**：+2 < ν < +3 的能隙区无相干峰/dip–hump（ED Fig.8），作者推测为 pseudogap 但明说 "further investigation is needed to confirm this scenario" 📜Q(ED Fig.8 图注)。
- **SI 未纳入本次提取**：节点拟合细节、BEC–BCS 模型推导、s-wave/nodal 对比完整 χ² 表均在 SI（SI4/SI5B），本次提取范围仅正文+Methods+ED 图注 ⚠️ NEEDS_VERIFICATION(SI)。
- **能隙误差与 Δ 提取口径**：Δ 有"相干峰间距一半"与"nodal fit"两种口径（差 10–30%）；2Δ/kBTC 的数值范围（15–19 vs 10）依赖口径选择，报告引用时须注明口径 📜Q[~](正文)。
- **温度/磁场能量标度未交叉校准**：T* ≈ 7 K、Bc ≳ 1 T、Δ ≈ 1.6 meV 三者未给出定量换算关系（如 2Δ/kBT*），正文只作定性并存陈述 📜Q+💭I。

---

## 7. 与其他工作的关系（跨论文对标，仅结构角色；数字均不出自他文）

- **同体系输运超导（上游实验）**：Park & Cao 2021 Nature 590（ref 1）与 Hao 2021 Science 371（ref 2）——本文谱学 Tc ≈ 2–2.5 K、填充范围 −3<ν<−2、ξGL ≈ 12 nm 均与之对标，并把"输运观测超导"升级为"局域谱学证据" 📜Q。
- **同组前作（方法继承）**：Choi 系列 MATBG STM（ref 8 = Choi 2019 Nat. Phys. 15, 1174；ref 13 = Choi 2021 Nature 589, 536；ref 16 = Choi 2021 Nat. Phys. 17, 1375）——本文的 Landau fan 与填充标定方法继承之（"as in our previous studies on bilayers⁸,¹³,¹⁶"）📜Q(Methods)。⚠️ 注意：同组 PRX 前作 E3（Kim 2021 PRX 11, 041050，MATTG 谱学）**未被本文引用**（E4 收稿 2021-09-20，早于 E3 正式刊出，且本文方法引的是 MATBG 而非 TTG 前作）。
- **TBG 侧对标（关键）**：Oh 2021 Nature 600, 240（ref 5，"Evidence for unconventional superconductivity in twisted bilayer graphene"）——作者明示若干相似性（节点谱、巨 gap/Tc 比、pseudogap 对温度/磁场的反常鲁棒性）"suggest a common origin of superconductivity in bilayers and trilayers" 📜Q(正文)。⚠️ 本文标题与 Oh 2021 TBG 论文标题高度相似，勿混淆（本文为三层、Oh 为双层）。
- **理论对标**：Khalaf 2019 PRB 100, 085109（ref 3，魔角层级）、Li-Wu-MacDonald 2019（ref 4，single-twist 三层能带）、Carr 2020 Nano Lett.（ref 6，夹层 Dirac）——Dirac+flat 共存结构出处；Phong 2021 PRB 104, L121116（ref 15）与 Fischer 2022 npj（ref 14，= T11）——MATTG 带结构/超导理论；Christos-Sachdev-Scheurer 2022 PRX 12, 021018（ref 47，= T10）——关联绝缘体/半金属/超导三相理论，本文引其"平带与 Dirac 扇区非强耦合" 📜Q(Methods)。
- **玻色模判据**：Scalapino-Schrieffer-Wilkins 1966（ref 37）与 Carbotte 1990（ref 35）——dip–hump 能量 Π = Δ + Ω 判据；Yu 2009 / Anderson-Ong 2006 / Eschrig-Norman 2003（refs 38–40）——Ω/2Δ ≤ 1 → 电子集体模判据 📜Q。
- **pseudogap/BCS–BEC 谱系**：Eagles 1969（ref 18）与 Renner 1998（ref 19，BSCCO pseudogap）——pseudogap 解读；Botelho-Sá de Melo 2005（ref 23）与 Borkowski-de Melo 2001（ref 24）——d 波 Lifshitz/BCS→BEC 转变理论；Chen 2005 / Randeria-Taylor 2014（refs 25,26）——普通 BEC–BCS crossover 📜Q。

---

## 8. 对后续研究的影响

- 确立 **STS + PCS 组合**作为 moiré 超导"存在性 + 非常规性"的谱学判据模板：相干峰 + Andreev 反射证存在性，U/V 谱形 + Dynes 拟合 + dip–hump 证非常规性；该方法直接移植到同组后续 E9（谷间相干序成像）📜Q+💭I。
- 把 msTTG 超导研究推进到**配对机制议程**：作者明列四类需未来理论解释的性质（properties 1–4），为理论侧提供定量靶（Δ(ν)、2Δ/kBTC、Ω(ν)、Ω/2Δ ≤ 1）📜Q(结论段)。
- 对 msTTG 项目：本文的 **θ = 1.51°、Δ ≈ 1.6 meV、Tc ≈ 2–2.5 K、T* ≈ 7 K、Bc ≳ 1 T、vF = 1.14×10⁶ m/s** 是复现"平带+Dirac 锥共存体系超导"的第一手对标数据；提示计算侧应检验：Dirac 锥与平带共存如何影响态密度/配对，以及掺杂（VGate）驱动的谱隙闭合行为 📜Q+💭I。
- **与导师假说的接口**：本文确认 msTTG 同时具备平带（VHS/cascade/关联）与附加 Dirac 锥（Landau fan/vF），并把超导定位为**强耦合非常规**；但**未直接检验"可调性→超导"链路**（无 D 场旋钮），该链路需 E1/E2（D 可调）与 T21（D 驱动半金属↔超导）补齐（见目的接口 Q3）。

---

## 9. 理论模型映射（供计算对标：D→Δ、θ→λ→A、观测量↔……）

| 理论量 | 本文映射 | 对标建议（💭I 标注为建议） |
|---|---|---|
| 构型 | (0°, θ, 0°) msTTG，中层转 θ；θ ≈ 1.5°（数据点 1.42°–1.57°）📜Q | tbplas 建 (0, 1.5°, 0) 三单层 moiré 超胞 |
| 平带 + Dirac 共存 | VHS（平带）+ 附加 Dirac 锥（Landau fan、Chern 偏移 2、vF = 1.14×10⁶ m/s）📜Q | 复现平带 DOS 峰与 Dirac 锥色散共存；Dirac 点相对平带 ±50 meV 📜Q |
| 掺杂旋钮 | VGate ↔ 填充 ν（标定 ≤5%）；**非位移场 D**（单背栅）📜Q | 若计算含 D 场扫描，需对照 E1/E2/T21，非本文 |
| 能隙 | Δ(ν) 峰 ≈ 1.6 meV @ ν ≈ −2.4；相干峰间距口径 vs nodal fit 差 10–30% 📜Q | 预言 gap(ν) 曲线与峰值位置 |
| 序参量 | 各向同性 s-wave 被排除；nodal / s+id / d+id 均可 📜Q | 计算应输出能隙对称性在 ν 空间的分区（gapped↔nodal 边界） |
| 玻色模 | dip–hump 能量 Π = Δ + Ω；Ω/2Δ ≤ 1 且 V 形区与 Δ 反相关 📜Q | 若算声子/集体模谱，对标 Ω(ν) 与 Ω/2Δ(Δ) 反相关关系 |
| 观测量 | 归一化 dI/dV 谱（U/V 形）、相干峰、零偏压电导、Landau fan、PCS Andreev | 计算 LDOS/DOS 的谱隙形状（U vs V）与掺杂演化 |

---

## 目的接口（随项目增删，不进入正文）

- **Q1（实验——msTTG 上观察到什么；本条聚焦超导谱学证据）**：E4 给出局域谱学级的超导证据：在 −3<ν<−2（每单胞 2–3 空穴）出现费米能处谱隙 + 对称相干峰 + 独立 Andreev 反射；相干峰随温度（至 2–2.5 K）与磁场（至 1 T）受抑制，T* ≈ 7 K 处零偏压谱隙才完全消失（pseudogap-like）；最大 Δ ≈ 1.6 meV（2Δ/kBTC ≈ 15–19）；谱形 U→V 转变（gapped→nodal），peak–dip–hump 提示玻色模耦合 📜Q。→ 正文 §2.2/§2.3/§2.4、§4.1 表。
- **Q3（证据强度：flat+Dirac 高可调 → 超导链条）**：E4 对链条的贡献是**"超导侧"的中间环节**——它确认 msTTG 同时具备平带（关联）与 Dirac 锥（共存），并把超导定性为强耦合非常规（非弱耦合 BCS s-wave），为"配对机制"提供入口；但它**不直接检验可调性链路**：器件为单背栅、无位移场 D 旋钮，且"gate-tunable"仅指 VGate 掺杂（非 D 场）。因此 flat+Dirac→**可调性**→超导 的因果链需 E1/E2（D 可调超导）+ T21（D 驱动半金属↔超导）+ E13/E14（轻/重电子、双穹顶）接力，本文只闭合"超导存在且非常规"这一环 📜Q+💭I。
- **增量价值**：相对同项目实验族笔记（E1/E2 输运超导、E6 ARPES 能带、E9 谷间相干成像），本篇补充的是**超导的局域谱学定量判据**——Δ(ν)≈1.6 meV、2Δ/kBTC≈15–19、Tc≈2–2.5 K、T*≈7 K、Bc≳1 T、U→V(gapped→nodal) 转变、peak–dip–hump 玻色模 Ω/2Δ≤1；对假说检验，它提供"超导是非常规/强耦合"这一可计算的结论性事实，并把配对机制设为未决问题（供 Q2 理论 T10/T11/T20/R1 对标）。

---

## 反向核对 pass (2026-09-04)

对全部正文数字执行 pdftotext 提取文本 grep 核对（/tmp/msTTG_txt/E4_kim2022.txt），结果：

- ✅ 命中：1.5°/1.51°/1.46°/1.42°/1.44°/1.45°/1.54°/1.57°；1.48 ± 0.03°；±0.01°；0.246 nm；≈9 nm；≈100 nm/290 nm/80 nm/26 nm/10 nm/50 nm/0.5 nm；1.14 × 10⁶ m/s；1.6 meV；15–19；≈10；~3.5（"about 3.5"）；10–30%；≈10 T；≈12 nm；≈2 T；BC ≳ 1 T；2–2.5 K；T* ≈ 7 K；400 mK；0.4/2/3/4.5/5.6/7 K；0/100/200/300/400/600/800/1000 mT；750 mT；3 T；8 T；B ≳ 4 T；0.1 meV；0.67 meV；39 μeV；1.44/1.26/0.88/1.10/0.85/1.35 meV；1.42 meV；10 μeV；−0.2 meV/−1.2 meV（"µ = –0.2 meV"/"µ = –1.2 meV"，en-dash 编码）；±50 meV；5%；90%；100 mV/1 nA/0.2−1 mV/973 Hz；10−100 kΩ；100 μV；30 nm/90 °C/40 °C；−15 V→15 V（VGate 轴）；"two to three holes"；"Chern-number shift of 2"；"fivefold"；"unambiguous spectroscopic evidence"；properties (1)–(4) 句；"cannot rule out low-energy phonons"；BEC/BCS/Pauli/Dynes/Andreev/pseudogap/nodal/U-shaped/V-shaped 措辞均逐字存在。
- ⚠️ 降级/修正记录：见「更正日志」。

---

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-09-04 | **"135 eV" 单位疑云**：ED Fig.9e 图注提取文本显示 s+id/d+id 拟合 "Γ = 135 eV"（两处），而同级 Pb 标定写 "Γ = 10 μeV"、V 形节点拟合写 "Γ = 39 μeV"。物理上 135 eV 荒谬、135 μeV 与 0.85–1.35 meV 能隙同级合理 ⇒ 判为 pdftotext 丢失 μ 字符，本笔记写 "135 μeV" 并在 §4.2 标注 ⚠️；读者引用时以 PDF 原 caption 为准。 |
| 2026-09-04 | **负号/减号编码**：VGate 负值（−9.1 V、−7.8 V 等）与化学势（µ = –0.2/–1.2 meV）在提取文本中混用 en-dash（U+2013）/减号（U+2212），grep 用 ASCII '-' 不命中属编码差异、非内容缺失；正文引用值已在 read 输出核对存在。 |
| 2026-09-04 | **填充因子符号**：pdftotext 将 ν 渲染为 "v"（正文）与 "Q"（部分图），实为同一物理量 ν（filling factor）；笔记统一写 ν，避免与电压 V 混淆。 |
| 2026-09-04 | **vF = 1.14 × 10⁶ m/s** 为 Fig.2i 面板标注（"Vf = 1.14 × 10⁶ m s⁻¹"），按 txt 可 grep 处理为 📜Q[~] 并注明"读值/面板标注"；若视为图读值应降级 📊F[读图]。同理 Fig.3c 的 Δ=0.67 meV/Γ=39 μeV、Fig.3i,j 的 µ=−0.2/−1.2 meV 均为面板标注，已注"面板标注"来源。 |
| 2026-09-04 | **2Δ/kBTC 口径**：正文同时给 "≈15–19"（相干峰间距口径）与 "≈10"（nodal fit 口径，较相干峰小 10–30%），两处并列 📜Q，不做归一；报告引用时须注明口径（§4.1/§6 已标注）。 |
| 2026-09-04 | **SI 范围声明**：本次提取范围仅正文+Methods+ED 图注，**不含 SI**（SI1–5B：原子重构模拟、Dirac 锥细节、节点拟合、BEC–BCS 模型推导等）。笔记中所有 "SI4/SI5B" 提及仅作指针，不做内容引用；BEC–BCS 模型细节、完整 χ² 对比标 NEEDS_VERIFICATION(SI)。 |
| 2026-09-04 | **"gate-tunable" 措辞防歧义**：本文摘要/正文 "gate-tunable transition" 的旋钮是 VGate（静电掺杂），**非位移场 D**（器件单背栅、无顶栅）。目的接口 Q3 已显式区分，避免与 E1/E2 的 D 场可调性混淆。 |
