<!--
 * @Author       : paper-reading SKILL (deep literature reading)
 * @Date         : 2026-09-03
 * @Description  : E9: Hyunjin Kim et al. (2023) Nature — 魔角三层石墨烯中谷间相干序(Kekulé 序)的 STM 成像（4 块辨识结构）
-->

# Paper Review: Kim et al. (2023) — Imaging inter-valley coherent order in magic-angle twisted trilayer graphene

| 字段 | 内容 |
|------|------|
| **编号** | E9 |
| **标题** | Imaging inter-valley coherent order in magic-angle twisted trilayer graphene |
| **作者** | Hyunjin Kim, Youngjoon Choi, Étienne Lantagne-Hurtubise, Cyprian Lewandowski, Alex Thomson, Lingyuan Kong, Haoxin Zhou, Eli Baum, Yiran Zhang, Ludwig Holleis, Kenji Watanabe, Takashi Taniguchi, Andrea F. Young, Jason Alicea, Stevan Nadj-Perge |
| **期刊** | Nature 623, 942–948 (2023 年 11 月 30 日刊行；线上 2023-11-15) 📜Q(正文页眉) |
| **DOI / arXiv** | 10.1038/s41586-023-06663-8 / arXiv:2304.10586（⚠️ arXiv 号正文未出现，标外部来源） |
| **类型** | 实验 — 扫描隧道显微/谱学（STM/STS），Kekulé 序（谷间相干 IVC 序参量）实空间成像 |
| **课题组** | S. Nadj-Perge（Caltech，STM 主导）+ A. F. Young（UCSB，器件）+ J. Alicea（Caltech，理论） |
| **PDF / 文本** | ✅ PDF（references/exp/）；提取文本 /tmp/msTTG_txt/E9_kim2023.txt（正文+Methods+ED 图注，**不含 SI**） |
| **精读日期** | 2026-09-03 |

> **体系对应**：本文 "MATTG（twisted trilayer graphene，第二层扭 θ，第一、三层对齐）" = 本项目 msTTG 构型 (0°, θ, 0°)（镜面对称、交替扭转族）。主样品 θ = 1.60° ≈ TTG 魔角，低异质应变。全文为"外部资料核验通过"的单一来源事实层笔记；通用物理不在此复制（FRESH pack：暂无 [PHY-*] 锚点）。

---

## TL;DR

**本文想解决的问题**：MATTG（msTTG）在关联填充区的基态是否自发破缺对称性？若破缺，是哪一种谷间相干（inter-valley coherent, IVC）序、其空间调制波矢随填充与磁场的依赖如何，并与超导/赝隙现象有何关系？（"问题"句式：把"关联绝缘体基态是什么序"落到可成像判据上。）

**主结果**：低应变样品 A（|ε| ≈ 0.12%、θ = 1.60°）中，在约 −3 < ν < −2 与 2 < ν < 3（每 moiré 单胞约 2–3 个电子/空穴）📜Q(摘要) 观测到与隧穿谱中 correlated gap / 赝隙共存的石墨烯晶格原子级重构——Kekulé √3×√3 超胞（相对石墨烯倒格矢 1/√3、旋转 30°）📜Q(正文)；该序零磁场即有，36 nm×36 nm 大图自相关显示 moiré 尺度平移对称破缺，且 FT 提取的调制波矢 qKekulé 随空穴掺杂 ν = −2 → −2.5 单调增大、穿越 MBZ 边界附近的近公度点 g3/2 📜Q(正文+Fig.4 图注)，对磁场（0 → 8 T）几乎不变 📜Q(正文)。观测与理论提出的 **IKS（incommensurate Kekulé spiral）序**（含实测应变与 Hartree 修正的连续模型）预言一致 📜Q(正文+Methods)。

**结论/意义**（保留作者措辞强度）：作者结论为 "consistent with the theoretically proposed incommensurate Kekulé spiral order"（摘要）与 "indicate that superconductivity can emerge from an inter-valley coherent parent state"（摘要，最后一句）📜Q(摘要)；正文用 "suggests the presence of an IKS order"（Discussion）📜Q。全文无超导的直接测量——超导关联经由同组先前工作（ref 13 = Kim 2022 Nature 606；样本 C 同一区域，ED Fig. 9）📜Q(ED Fig.9 图注)。

---

## 1. 系统辨识导览（判别表为全文唯一权威）

**黑箱三要素**：`{VGate(V)、VBias(mV)、面外磁场 B(T)、温度 T(K)、样品(应变) | 原子分辨 dI/dV 图与 FT 峰强度、Kekulé 自相关图、提取波矢 qKekulé、dI/dV 谱(能隙) | MATTG 关联基态具 IVC(Kekulé) 序且为 moiré 平移对称破缺的 IKS 型序}`

**四层变量图**（符号层一次钉死）：

| 层 | 本文实例 |
|----|----------|
| **L1 旋钮 u** | VGate（决定填充 ν）、VBias（隧穿偏压）、面外磁场 B（0/2/4/8 T）、温度 T（400 mK–7.5 K） |
| **L2 导出量 x₁** | 填充因子 ν（Landau fan 或满填充/CNP LDOS 特征标定，两法偏差 ≤5% 📜Q(Methods)）；扭角/异质应变（由 moiré 几何反推，θ̂ = 1.60°±0.01°，ε̂ 见 §4） |
| **L3 模型量 x₂** | 候选 IVC 基态族 {Kramers IVC, 时间反演对称 IVC (TRS-IVC), IKS}；理论最优波矢 qIKS 与可观测 qKekulé（两者相差连接 MBZ 中心 γ 与角点 κ 的动量平移）📜Q(正文 Fig.4h)；含 Hartree 修正（介电 εr = 30/15）的连续模型带结构；异质应变 ~0.1–0.2% 下单一波矢 qIKS 的谷间 nesting 失稳 📜Q(Discussion) |
| **固定参数（非旋钮）** | θ ≈ 1.60°（各样品 1.60°/1.59°/1.48°）；异质应变 ε 与应变角 φ（每样品一组，见 §4）；石墨烯晶格常数 0.246 nm 📜Q(正文) |
| **反推量 θ̂** | Kekulé 调制波矢 qKekulé（大小+方向，误差 ±0.12 nm⁻¹ 📜Q(Methods)）；Kekulé 峰相对强度（归一化于石墨烯峰） |
| **L4 观测量 y** | 原子分辨 topography/dI/dV 图；FT 谱中 Kekulé 峰位与位移；Kekulé 自相关图；隧穿谱 gap/赝隙；sash 特征；CNP 向列特征 |

**可辨识性判别表**（每条判别 = 判据 / 排除谁 / 确立谁）：

| 判别 | 判据（数据） | 排除谁 | 确立谁 |
|------|-------------|--------|--------|
| **D1** Kekulé 重构是电子学内禀序（非杂质/结构/针尖伪迹） | 原子分辨 dI/dV 出现晶格三重化图案，FT 有独立 Kekulé 峰组 📜Q(Fig.1)；图案对 VGate、VBias 强依赖：远带与 CNP 处完全消失、VBias 换号对比近反转 📜Q(正文+ED Fig.3)；高温随 gap 抑制而减弱 📜Q(正文+ED Fig.4)；每样品 ≥10 支微针尖重复 📜Q(Methods)；三个独立样品（A/B/C）均可门控重现 📜Q(Methods) | 杂质吸附、结构形变/位错、针尖状态伪迹 | Kekulé 型电子重构存在于关联填充区 |
| **D2** 序在零磁场即存在 → 排除 Kramers IVC | 零场下即有显著 Kekulé 峰 📜Q(正文)；Kramers IVC 理论预言仅在有限磁场下产生 LDOS Kekulé 峰 📜Q(正文, refs 25,26) | Kramers IVC（磁化密度波型） | 候选集收窄至零场 CDW 型：TRS-IVC 与 IKS |
| **D3** 序在 moiré 尺度破缺平移对称性 → 非均匀（公度）TRS-IVC | 相邻 AAA 位 Kekulé 图案反相（亮↔暗）📜Q(Fig.3b–g)；Kekulé 自相关呈沿 l1、l2 的条带、沿 l3 弱 📜Q(正文)；FT 峰相对公度 K₁=(G₁+G₂)/3 等位置的位移可由单一 qKekulé 统一解释 📜Q(正文+Methods)；qKekulé 一般与 moiré 失配（非公度）、随 VGate 单调演化 📜Q(正文) | 空间均匀的公度 Kekulé/TRS-IVC 基态 | moiré 平移对称破缺；与 IKS 族一致（近公度 lock-in 可能见 SI §9，正文明示 Fig.3 图案"very close to a commensurate modulation" 📜Q(Discussion)） |
| **D4** qKekulé 的填充/磁场依赖与 IKS 理论定量一致 | 理论（含实测异质应变、Hartree 未强烈反转情形）给出 qKekulé 随 ν=−2 空穴掺杂演化的趋势，与实验在双方误差内相符 📜Q(Discussion+Fig.4 图注)；qKekulé 几乎不随 B（2 T/8 T 仅方向微移）📜Q(正文)；背栅位移场（杂化平带与 Dirac 锥）几乎不改理论 qKekulé 📜Q(Discussion, SI Fig.6) | 强 Hartree 带反转（εr=15 情形）作为本样品主导图景；随 B 显著变化的序 | IKS 图景：平带结构（γ 与 κ/κ′ 极值位置、应变畸变、Hartree 反转程度）决定 qIKS |
| **D5** Kekulé 序与 (伪)隙、超导区的关系 | Kekulé 非零强度区与 gate 谱中 insulating gap/赝隙区重合 📜Q(正文+Fig.2j)；归一化 Kekulé 强度在赝隙区 ν≈−2.3~−2.5 最大、而非 ν=−2 绝缘相 📜Q(Discussion)；样本 C 同区先前已确立超导 📜Q(ED Fig.9) | "Kekulé 仅存在于 ν=−2 硬绝缘相"的图景 | IVC 序最强处在赝隙区；为 SC 源于 IVC 母态提供约束（作者措辞为 constraint/indicate，非证明 📜Q(Discussion)） |
| **D6**（次判别）sash 特征 + CNP 向列性 | FT 中卫星峰沿窄条带被抑制形成 sash，且非所有方向出现 → C3 对称破缺 📜Q(正文+ED Fig.7)；CNP（VGate=0 V）无晶格三重化但有键择优方向与 AAA 附近 dI/dV 空间演化，与理论 NSM（向列半金属）预言一致 📜Q(正文+ED Fig.10, ref 25) | 完整 C3 对称的简单电荷序 | IKS 基态附带的 C3 破缺痕迹；CNP 处向列半金属态 |

> **主结果 ↔ 判别表映射**：主结果①（Kekulé 重构存在于关联填充区）← {D1, D2}；主结果②（moiré 平移对称破缺、qKekulé 非公度且随掺杂演化）← {D3, D4}；主结果③（IVC 序最强在赝隙区、SC 可能从 IVC 母态涌现）← {D5}；佐证 ← {D6}。

> **[前提与限定]**（判别结论的适用范围）：
> - **噪声/扰动**：样品须"large, sufficiently clean and low-strained"📜Q(正文)——这是作者明确声明的前置条件；AFM 残留检查仅样品 A 干净（ED Fig. 2）📜Q(ED Fig.2 图注)；背景噪声数值正文未给；热展宽由 T=2 K 与 400 mK 数据界定，无定量 FWHM。
> - **判别性扫轴**：VGate 全程扫（−20 V … 9 V 展示，远带/CNP/关联区全覆盖）📜Q(Fig.2)；B 扫至 8 T（4 T 亦有谱，ED Fig.5）📜Q；T 扫 400 mK–7.5 K（5 K/7.5 K 谱，ED Fig.4）📜Q；**位移场/电场未被当作旋钮**（器件仅单背栅 graphite/hBN，无独立顶栅——可调性论点依赖他文 Park 2021/Hao 2021，本文只作引证）。
> - **候选集 M 边界**：只考虑 {Kramers IVC, TRS-IVC, IKS} 家族（动机：与 TBG 带结构/谱学相似，refs 25,26）📜Q(正文)；**集外候选未排除**：非 IVC 的电荷序/向列序+应变耦合组合未被逐个体排除（D3/D6 主要靠"与 IKS 预言方向一致"而非逐点否定）；单个低应变样品 A 承载全部大范围 FT 分析（>20 moiré 位），样品 B/C 只证 IVC 存在性 📜Q(Methods)。正文自我限定：Fig.3 图案近公度、lock-in 机制见 SI §9 📜Q(Discussion)。

三层标注：📜Q = 原文事实（附位置）｜推导｜📊F = 读图估算｜💭I = 推断。**不确定度（正交轴）**：[±] 原文误差棒 / [~] 原文无误差棒 / [读图] 图提取·色标值 / [相对] 仅相对量。所有数字经 pdftotext + grep 反向核对（见文末 pass）。

---

## 2. 结果与机制（按论文自身论证结构：Kekulé 成像 → 门压依赖 → moiré 平移破缺 → 波矢定量 → 讨论）

### 2.1 Kekulé 失真的实空间成像（Fig. 1）
- 在 AAA 位（三层碳原子对齐处）附近的高分辨成像显示蜂窝晶格（晶格常数 0.246 nm 📜Q[~](正文)）叠加更微弱的更大尺度原子调制；该调制在 dI/dV 空间图中比 topography 更明显，呈现清晰的**晶格三重化（lattice-tripling）图案** 📜Q(正文, Fig.1d,e)。
- 图案强度对 VBias 敏感，VBias 换号时对比度约反转（ED Fig. 3）📜Q(正文)；强 VGate/VBias/温度依赖 ⇒ 电子学起源，"rules out the possibility that the observed Kekulé peaks arise from impurities or structural deformations" 📜Q(正文)。
- FT 分析：六外峰=石墨烯倒格矢、六内峰=1/√3 石墨烯倒格矢旋转 30° ⇒ √3×√3 超胞旋转 30° 的 **Kekulé 失真** 📜Q(正文, Fig.1f)。物理语义：K/K′ 谷间相干散射导致布里渊区缩小（谷间相干 inter-valley coherence）📜Q(正文)。Kekulé 失真此前的已知宿主：金属原子修饰单层石墨烯（Gutiérrez 2016, ref 18）与量子霍尔区（refs 19,20）📜Q(正文)。

### 2.2 VGate 依赖：序存在的填充区间与 (伪)隙共存（Fig. 2 + ED Fig. 4/9）
- 远带（VGate=−20 V）与电荷中性点（VGate=0 V）附近 Kekulé 失真完全缺失；显著失真出现在 **−3 < ν < −2 与 2 < ν < 3** 📜Q(正文, Fig.2)。摘要措辞："over a filling range of about two to three electrons or holes per moiré unit cell"📜Q(摘要)。
- 归一化 Kekulé 峰强度（Kekulé 六峰和 / 石墨烯六峰和）的非零区与 gate 谱中 hosting **insulating gap 或 pseudogap** 的区域吻合（Fig. 2i,j；ED Fig. 9 为另一样品）📜Q(正文)。
- 强度近似在 VBias 匹配 (伪)隙伴随的 LDOS 峰时最大（ED Fig. 4）📜Q(正文)；温度升高、gap 被抑制时 Kekulé 可见度同步减弱（ED Fig. 4：5 K 时 ν=2 gap 存活而 ν≈−2 gap 大受抑制；7.5 K 时 ν=2 存活、ν≈−2 几乎消失）📜Q(ED Fig.4 图注)。
- 机制注记（D5）：Kekulé 序"何时出现"由费米能相对 (伪)隙位置决定——gap/(伪)隙与 IVC 序同现是本文判别"关联起源"的核心观测链。

### 2.3 moiré 平移对称破缺（Fig. 3）
- ν=−2.3 处 36 nm×36 nm 大图覆盖 20 个 moiré AAA 位 📜Q(正文, Fig.3a)；取相邻 AAA 位（沿 l2）的 FT 滤波窗口比较：**Kekulé 图案亮/暗反相**，而石墨烯滤波图原子对齐精确一致 📜Q(Fig.3 图注+正文)。
- 方法升级为 **Kekulé 自相关图**：固定 ~1 nm×1 nm 小窗、以移动窗对 Kekulé 滤波图自相关，仅保留石墨烯原子自相关超阈值 0.5 的点（结论对阈值不敏感）📜Q(正文)。自相关图呈沿 l1、l2 的红-蓝条带，沿 l3 依赖弱 ⇒ 调制波矢 qKekulé **垂直于 l3**，大小约为 moiré 倒格矢的一半（该填充下）⇒ "near doubling of the moiré unit cell" 📜Q(正文)。

### 2.4 qKekulé 的定量提取与填充/磁场依赖（Fig. 4 + ED Fig. 5/6）
- 直接 FT：石墨烯倒格矢峰位被 moiré 卫星峰包围难以唯一定位（校准误差/同质应变）⇒ 用**高阶倒格矢峰**（簇更小）与 mG₁+nG₂ (m,n=−3…+3) 自洽性唯一确定 G₁、G₂（G₃=G₂−G₁）📜Q(正文+Methods, ED Fig.6)。
- 由 Gᵢ 计算公度 Kekulé 峰位 K₁=(G₁+G₂)/3、K₂=(G₂+G₃)/3、K₃=(G₃−G₁)/3：实测卫星峰不落在这些点，但三组峰的位移可由**单一波矢 qKekulé** 统一解释（K₁/K₂/K₃ 三个独立提取互相一致）📜Q(正文+Methods)。
- qKekulé 不随 VBias 变、随 VGate 单调演化，对不同图大小与 VBias 稳健 📜Q(正文+Methods)；空穴掺杂 ν=−2→−2.5 时 qKekulé 方向保持在 g3（误差内）而大小增大，**在近公度点 g3/2 附近穿越 MBZ 边界** 📜Q(正文, Fig.4l)。
- 磁场：2 T 与 8 T 下空间变化的 Kekulé 失真仍存，qKekulé 仅方向微移 📜Q(正文, ED Fig.5)；Landau fan 用于标定填充与确认序-能隙窗口（ED Fig.5a）📜Q(ED Fig.5 图注)。
- 理论对照（Fig. 4j,k）：K 谷价带顶在 ν=−2 的计算——小 Hartree 修正（εr=30，平带不反转）下理论 qKekulé 与实验相符；强 Hartree（εr=15，γ 点附近平带反转）不符 📜Q(Fig.4 图注+Discussion)。含实测应变的理论 qKekulé 在双方误差内与观测一致；演化在非反转区更显著；加入背栅位移场（平带与 Dirac 锥杂化）后理论 qKekulé 几乎不变（SI Fig.6）📜Q(Discussion)。

### 2.5 Discussion：IKS 识别、赝隙区序最强、超导关联
- −2 与 −2.5 之间关联态本质：缓慢调制、一般非公度、随掺杂变化的 Kekulé 图案 ⇒ **IKS 序** 📜Q(Discussion)。IKS 理论起源：小异质应变（~0.1–0.2%，与本样品同量级）下单一波矢 qIKS 的谷间 nesting 失稳 📜Q(Discussion, refs 3,4,27)。
- 序强度（归一化 Kekulé 强度）在**赝隙区 ν≈−2.3~−2.5 最大**，而非 ν=−2 绝缘相 📜Q(Discussion)。同填充范围还观察到：U→V 型隧穿谱演化（ref 13）、输运中 Ginzburg–Landau 相干长度突变与最大 Tc（refs 1,2）📜Q(Discussion) —— 作者把这些现象学与 IVC 序的链接称为 open challenge 📜Q。
- 附带对称性破缺证据：sash 特征（C3 破缺、与 ref 25 一致、ν≈−2 的 IKS 基态相容）📜Q(正文+ED Fig.7)；CNP 处无三重化但存在键择优 → 理论 NSM（向列半金属）基态（ED Fig.10）📜Q。

---

## 3. 实验方法

### 3.1 器件与样品
- 器件：石墨（gate）/hBN/TTG 堆叠；graphite 底栅（单栅，无顶栅结构）；PC 膜+PDMS 干法转移（60–100 °C），金覆 PDMS 翻转堆叠、Ti/Au(3/12 nm) e-beam、NMP 除 PC、金印章法（130 °C 压印）接电极与 gate 📜Q(Methods)。样品 A 用金印章法（表面最干净，AFM 无残留）；B/C 用先前 PDMS 翻转法（B 有残留）📜Q(Methods)。
- 三个样品参数（详见 §4 表）：A 主分析（θ=1.60°，低应变）；B 较大应变对照；C 同区先前确立超导的样品（ref 13）。
- 制备后无退火 📜Q(Methods)。室温先用导电 AFM（CAFM，~2.8 N/m 针尖、100 mV 偏压、gate 悬空）定位 ~9 nm moiré 波长区域 📜Q(Methods)。

### 3.2 STM 测量
- Unisoku USM-1300J STM/AFM，Pt/Ir 针尖；默认 T=2 K（除非注明 400 mK）；dI/dV 谱参数 VBias=100 mV、I=1 nA、锁相 Vmod=0.2–1 mV、f=973 Hz；实空间图用恒高模式 📜Q(Methods)。压电扫描器以 Pb(110) 标定并经碳原子间距验证；扭角不确定度 ±0.01° 📜Q(Methods)。所有特征经 ≥10 支不同微针尖确认 📜Q(Methods)。
- 填充因子标定：Landau fan 图 或（无磁场数据时）满填充/CNP 的 LDOS 抑制特征；两法偏差 ≤5% 📜Q(Methods)。

### 3.3 异质应变提取
- 由 moiré 晶格矢量 g₁、g₂（实为长度 l₁,l₂,l₃ 与方向）反推应变大小与方向；大均匀区（≥30 nm×30 nm、数十 moiré 位）取平均抑制压电蠕变 📜Q(Methods)。应变符号与层序绑定（中层逆时针转；A 样品中层受压应变，ε 为负）📜Q(Methods)。

### 3.4 图像分析（本文方法学核心）
- **FT 滤波**：以半径 3.5 nm⁻¹ 圆掩膜分别圈六 Kekulé 峰/六石墨烯峰，逆 FT 得滤波图 📜Q(正文+Methods)。
- **Kekulé 自相关**：两等大小窗元素乘并归一化（完全相同=1、完全反相=−1）；移动窗 1.2 nm（0.8–1.7 nm 内不敏感）；仅取石墨烯原子自相关 >0.5（局部极大）的点作图以对齐原子格 📜Q(正文+Methods)。
- **qKekulé 提取**：由高阶石墨烯峰定 G₁,G₂(G₃=G₂−G₁) → 公度 Kᵢ → 测最近卫星峰相对 Kᵢ 的位移（模 moiré 倒格矢 g 的等价类；选使 |qKekulé|<|g| 且随 gate 连续的分支）📜Q(Methods)。误差棒 = √2×0.09 nm⁻¹ = **0.12 nm⁻¹**（0.09 nm⁻¹ = Fig.4b–g 半像素）📜Q(Methods)。

---

## 4. 关键数据（提取链 + 验证链 + 不确定度标注）

### 4.1 样品/几何参数表

| 量 | 样品 A（主分析） | 样品 B（应变对照） | 样品 C（超导样） |
|---|---|---|---|
| 扭角 θ | 1.60°±0.01°（"magic angle of 1.60°"）📜Q[±](Methods)；主文 "θ=1.60°, close to the magic-angle value of TTG"📜Q[~] | 1.59°（ED Fig.8 图注）📜Q[~] | 1.48°（ED Fig.9 图注）📜Q[~] |
| 异质应变 | 大小 (0.12±0.04)%、ε=−(0.12±0.04)%、φ=(87±10)° 📜Q[±](Methods)；正文/Fig.1 "ϵ≈0.12%"📜Q[~] | ε=−(0.28±0.04)%、φ=(138±10)° 📜Q[±](Methods)；图注 0.28% 📜Q[~] | ε=−(0.11±0.04)%、φ=(60±10)° 📜Q[±](Methods)；**ED Fig.9 图注另写 ϵ=0.08%**（⚠️ 两处不一致，见更正日志） |
| moiré 波长（A） | l₁=8.98 nm、l₂=8.83 nm、l₃=8.60 nm 📜Q[~](图1b/3a 面板标注，txt 行 69–74) | ~9 nm（CAFM 导航目标）📜Q[~](Methods) | — |
| 石墨烯晶格常数 | 0.246 nm 📜Q[~](正文) | | |

### 4.2 序参量观测表

| 量 | 值 | 证据/不确定度 |
|---|---|---|
| Kekulé 存在填充区间 | −3 < ν < −2 与 2 < ν < 3（"约 2–3 个电子/空穴每 moiré 单胞"） | 📜Q[~](正文+摘要+Fig.2) |
| 序最强处 | 赝隙区 ν≈−2.3 ~ −2.5（非 ν=−2 绝缘相） | 📜Q[~](Discussion) |
| (伪)隙共存 | Kekulé 非零区 = gap/赝隙区；主文**未给 meV 数值**（SI 不在本次提取范围） | 📜Q（定性，正文）；⚠️ 能隙能量值 NEEDS_VERIFICATION(SI) |
| 磁场依赖 | B=0 即有序；2 T/8 T 仍存，qKekulé 方向仅微移；4 T 有谱（ED Fig.5） | 📜Q[~](正文+Fig.4i+ED Fig.5) |
| 温度依赖 | 400 mK 图（Fig.1d,e）；2 K 默认；5 K/7.5 K 谱：ν≈−2 侧 gap 被抑制、Kekulé 可见度随 gap 减弱 | 📜Q[~](图注) |
| 平移对称破缺 | ν=−2.3 处 qKekulé ⊥ l3、|qKekulé|≈½ moiré 倒格矢 ⇒ moiré 单胞近倍增 | 📜Q[~](正文, Fig.3h) |
| qKekulé 演化 | 空穴掺杂 −2→−2.5：方向沿 g3（误差内）、大小增大、近 g3/2 处穿越 MBZ 边界 | 📜Q[~](正文, Fig.4l) |
| qKekulé 误差 | 0.12 nm⁻¹ = √2×0.09 nm⁻¹ | 📜Q[~](Methods) |
| 大图/窗口参数 | 36×36 nm²（20 AAA 位）；42×42 nm²（ED Fig.7）；150×150 nm²（方法内验证）；自相关窗 1.2 nm（0.8–1.7 nm 不敏感）、阈值 0.5；FT 掩膜半径 3.5 nm⁻¹ | 📜Q[~](正文+Methods+ED 图注) |

### 4.3 验证链（互验/多器件/旋钮依赖）
1. **多针尖/多样品**：≥10 微针尖；A/B/C 三样品均见门控 Kekulé 重构（B、C 证存在性；大范围 FT 仅 A）📜Q(Methods)。
2. **多尺度互验**：qKekulé 对不同图大小与 VBias 一致；K₁/K₂/K₃ 三独立提取互符；实空间自相关（Fig.3）与 FT 提取（Fig.4）结论一致 📜Q(正文+Methods)。
3. **标定自洽**：高阶峰 mG₁+nG₂ 无其他长波图案 ⇒ Gᵢ 选择唯一 📜Q(Methods)。
4. **旋钮依赖**：VBias 换号对比反转、VGate 开关序、温度抑制序 ⇒ 电子起源（D1）📜Q。
5. **填充标定交叉**：Landau fan 与 LDOS 特征两法偏差 ≤5% 📜Q(Methods)。

---

## 5. 主要结论

1. MATTG（msTTG）在关联填充区（−3<ν<−2 与 2<ν<3）的基态伴随**原子级 Kekulé（√3×√3/30°）重构**，即谷间相干（IVC）序的直接实空间证据 📜Q。
2. 序在 **moiré 尺度破缺平移对称性**，调制波矢 qKekulé 一般非公度、随空穴掺杂（−2→−2.5）单调增大并在 g3/2 附近穿越 MBZ 边界、对磁场稳健（≤8 T）📜Q。
3. 观测与 **IKS（非公度 Kekulé 螺旋）序**理论预言一致（含实测异质应变、Hartree 非强反转情形）；零场即现的 Kekulé 峰排除 Kramers IVC 📜Q。
4. IVC 序强度在 **赝隙区最大**，作者据此主张超导可由 IVC 母态涌现（措辞强度：constrain / indicate，非证明）📜Q。

---

## 6. 局限与未解决

- **大范围定量分析仅单一样品（A）**：>20 moiré 位的 FT/IKS 判定只在低应变样品 A 完成；B/C 仅证 IVC 存在，无法独立检验 qKekulé–掺杂关系与应变依赖 📜Q(Methods)。样本量小 ⇒ D3/D4 的普适性有限（💭I）。
- **无位移场旋钮**：器件为单背栅，本文不能直接测电场可调性；"位移场几乎不改 qKekulé"仅来自理论（SI Fig.6）📜Q(Discussion)。
- **未直接测超导**：SC 关联经样本 C（同区 ref 13）外推，本文观测窗（ν、B、T）与 SC 窗的重叠是间接论证（"emergence from IVC parent state"是作者推断性结论）📜Q。
- **候选集封闭风险**：只与 IVC 家族 {Kramers, TRS-IVC, IKS} 比对；其他序（纯向列电荷序等）未逐个体证伪（正文对 CNP 另见 NSM，说明作者承认序谱系更宽）📜Q+💭I。
- **近公度模糊性**：Fig.3 图案接近公度调制，lock-in 机制仅 SI §9 讨论（本提取文本无 SI）⇒ 公度 vs 非公度的边界结论依赖 SI，NEEDS_VERIFICATION(SI) 📜Q(Discussion)。
- **能隙能量尺度缺失**：主文提取范围无 (伪)隙 meV 数值（仅图 2j 色标与"correlated gap/pseudogap"定性词），无法与热/磁场能量标度定量对比；需 SI。⚠️
- 应变在 IVC 序中的**因果角色**（nesting 需要 ~0.1–0.2% 应变）未做应变连续调谐实验（仅 B 样品 0.28% 对照组，属"更大应变仍见 IVC"）📜Q(Methods)+💭I。

---

## 7. 与其他工作的关系（跨论文对标，仅结构角色；数字均不出自他文）

- **同体系超导谱学/输运（上游实验）**：Kim 2022 Nature 606（ref 13，同组谱学证据、样本 C 同区）；Park 2021 Nature 590（ref 1）与 Hao 2021 Science 371（ref 2）——本文 Discussion 引其输运现象（GL 相干长度突变、最大 Tc 位置）与 IVC 序最强区衔接。Turkel 2022 Science（ref 14）为 MATTG 无序/结构研究。
- **TBG 侧 IVC 成像**：Nuckolls 2023 Nature（ref 15，TBG Kekulé/IVC 序成像）——本文明确提醒：因 moiré 单胞更小、应变与关联效应略有差别，两体系 Kekulé 细节与掺杂依赖的**直接对比需谨慎** 📜Q(Methods 末节)。
- **理论：IVC/IKS 族**：Kwan 2021 PRX（ref 3，IKS 序）与 Wagner 2022 PRL（ref 4，全局相图）——IKS 理论基础；Kang–Vafek 2019（ref 21）、Bultinck 2020（ref 22）、Lian 2021（ref 23，Kramers IVC 等）——被排除/备选成员；Christos–Sachdev–Scheurer 2022 PRX（ref 24，MATTG 专属理论，但作者称 MATTG 专门计算有限）；Wang 2022 DMRG（ref 27）。
- **STM 判据理论**：Hong–Soejima–Zaletel 2022 PRL（ref 25，STM 可观测判别、sash/C3、NSM 预言）与 Călugăru 2022 PRL（ref 26）——判别表判据的主要理论来源。
- **能带/魔角**：Khalaf 2019（ref 16，魔角层级）、Carr 2020（ref 17，夹层石墨烯的 Dirac 锥）——"flat band + 弥散 Dirac 锥"共存结构的出处（§9 相关）；Lopes dos Santos 2007（ref 28）、Bistritzer–MacDonald 2011（ref 29，连续模型）。
- **Kekulé 序其他宿主**：Gutiérrez 2016 Nat. Phys.（ref 18，单层+金属原子）；Liu 2022 Science 与 Coissard 2022 Nature（refs 19,20，量子霍尔石墨烯）——IVC 序的跨平台普遍性问题。
- **TBG 早期 STM**（refs 9–12：Kerelsky、Choi、Xie、Jiang）——此前方法只能做谱学+基本结构表征，本文把 STM 推进到对称性破缺序的判定。
- **层状石墨烯超导推广**：Zhang 2022 Science（ref 7）、Park 2022 Nat. Mater.（ref 8）——多层家族语境。

---

## 8. 对后续研究的影响

- 确立 **STM 作为 moiré 关联态对称性破缺诊断工具**的方法模板：FT 滤波 + 自相关 + 高阶倒格矢标定的组合可移植到其他 moiré 体系（作者在 Methods 末明确呼吁在更广 moiré 平台检验 IVC）📜Q。
- 为理论提供**定量约束**：qKekulé(ν, B) 数据点与"Hartree 反转程度"判别（εr=30 vs 15）是后续多体计算的直接对标靶（见 §9）。
- 把"超导母态"问题具体化：作者主张 SC 从 IVC 母态涌现（abstract），把 MATTG/msTTG 的超导研究从"能谱+输运现象学"推向"确定对称性破缺序参量 + 配对共存"的理论议程 📜Q。
- 对 msTTG 项目：本文的 **θ=1.60°、ε、φ 与 qKekulé(ν,B)** 是复现"平带+Dirac 锥共存体系关联基态"的第一手对标数据；提示计算侧应检验：平带极值在 MBZ 的位置（γ vs κ）、应变导致的畸变、Hartree 项强弱如何移动 qIKS/qKekulé。

---

## 9. 理论模型映射（供计算对标：D→Δ、θ→λ→A、观测量↔……）

本文提供的理论↔实验对标接口（全部为正文/Methods 可 grep 的原文量）：

| 理论量 | 本文映射 | 对标建议（💭I 标注为建议） |
|---|---|---|
| 构型 | (0°, θ, 0°) msTTG，中层逆时针转；θ≈1.60°（TTG 魔角）📜Q | tbplas 建 (0,1.60°,0) 三单层 moiré 超胞 |
| 应变 | 样品 A：ε=−(0.12±0.04)%、φ=(87±10)°；理论 IKS 所需异质应变 ~0.1–0.2% 📜Q[±] | 计算中含 ε=0.12%、应变角 87° 的单轴异质应变（符号/方向影响 qIKS 方向）|
| 平带结构决定序 | 价带平带极小/极大在 MBZ 的 γ 与 κ、κ′；应变非普适畸变；Hartree 项可致 γ 点反转（εr=30 不反转 vs εr=15 反转）📜Q(Fig.4j,k) | 平带极值位置 + Hartree 强弱是判别 qKekulé 趋势的主控参数（💭I：可与自洽 Hartree 计算对照） |
| 序参量 | qIKS（nesting 单波矢，理论量）↔ qKekulé（LDOS/STM 观测量），相差连接 MBZ γ 与 κ 的动量平移 📜Q(Fig.4h) | 计算预言应输出 qKekulé 而非 qIKS，注意此平移关系 |
| 掺杂依赖 | 空穴 −2→−2.5：|qKekulé|↑、沿 g3、近 g3/2 穿越 MBZ 边界（Fig.4l 相对量）📜Q | 预言 |qKekulé|/|g3|(ν) 曲线与 0.5 附近行为 |
| 磁场 | qKekulé 对 B≤8 T 稳健（仅方向微移）📜Q | 零场基态即可；B 作为弱微扰 |
| 位移场/Dirac 锥杂化 | 背栅位移场使 TBG-like 平带与 Dirac 锥杂化，理论 qKekulé 几乎不变（SI Fig.6）📜Q(Discussion) | **对导师假说的直接接口**：若平带+Dirac 共存是可调性来源，本文理论提示该杂化不改 IKS 波矢——即序对杂化不敏感（强度/配对仍需他文，💭I） |
| 观测量 | LDOS Kekulé 峰（√3×√3 调制的 dI/dV）、自相关条带、sash（C3 破缺）、(伪)隙 | 计算 LDOS 调制周期、C3 各向异性；能隙 meV 值需 SI（⚠️ 本提取无） |

---

## 目的接口（随项目增删，不进入正文）

- **Q1（实验——msTTG 上观察到什么；本条聚焦 IVC/Kekulé 序成像证据）**：E9 给出序参量级成像证据：低应变样品（ε≈0.12%）中 Kekulé（√3×√3/30°）重构出现在 −3<ν<−2 与 2<ν<3，与隧穿 correlated gap/赝隙同现 📜Q；序零磁场即有（排除 Kramers IVC）、至 8 T 稳健、qKekulé 仅随空穴掺杂 −2→−2.5 单调增大（穿越近公度点 g3/2）、几乎不随 B 变 📜Q；随温度升高序随 (伪)隙一起被抑制（5 K/7.5 K 谱）📜Q。能隙 meV 数值不在本次主文提取范围（⚠️ SI）。→ 正文 §2.2/§2.4、§4.2 表。
- **Q3（证据强度：flat+Dirac 高可调 → 关联/超导链条）**：序参量成像把"关联态"从能谱特征升级为**确定的对称性破缺（IVC/IKS）序**，作者仅以 "indicate that superconductivity can emerge from an inter-valley coherent parent state"📜Q(摘要) 的弱措辞收尾——IVC 序最强在赝隙区而非 ν=−2 绝缘相，把 SC/赝隙同源于 IVC 母态设为待验证命题 📜Q(Discussion)；本篇自身不测超导（借 ref 13 样本 C 同区），故它对"flat+Dirac 共存→可调性→超导"因果链的贡献是**中间环节**（关联基态 = IVC 序），而非直接证据；且其理论部分显示位移场杂化几乎不改 qKekulé（SI Fig.6）📜Q，可调性→序→超导的传导路径仍未闭合。
- **增量价值**：相对同项目实验族笔记（E1 Hao/E2 Park 输运超导、E6 Li 谱学等），本篇补充的是**实空间序参量直接成像与 qKekulé 定量提取**——把"关联态"落实到具体对称性破缺（IVC/IKS、moiré 平移破缺、C3 破缺 sash），并提供 θ=1.60°/ε/φ 与 qKekulé(ν,B) 作为理论对标数值集；对假说检验，它提供了"IVC 母态"这一可计算的中间态概念。

---

## 反向核对 pass (2026-09-03)

对全部正文数字执行 pdftotext 提取文本 grep 核对（/tmp/msTTG_txt/E9_kim2023.txt），结果：

- ✅ 命中：1.60（3 次）/1.59/1.48；0.12/0.28/0.11/0.08（各 ≥1）；0.04（4 次，±0.04 共 4 处）；±0.01/± 10（3 次：87/138/60 各随 φ 出现）；0.246；l₁=8.98/l₂=8.83/l₃=8.60（图内标注）；36 nm/20 moiré/42 nm/150 nm；3.5 nm；1.2 nm/0.8–1.7 nm/1 nm×1 nm/阈值 0.5；0.09 nm、√2（"√2 × 0.09 nm⁻¹ = 0.12 nm⁻¹"）；2 T 和 8 T、4T、400 mK、5K、7.5K、2 K；−2.3（6 次）；973 Hz；0.2–1 mV；100 mV；1 nA；130 °C；60 °C；≤5%（"within 5%"）；−3 < ν < −2 与 2 < ν < 3；1/√3 与 30°；0.1−0.2%；g3/2；"two to three electrons"；Zenodo 10.5281/zenodo.8317363；Nature Vol 623 942 页眉。
- ✅ 措辞核对：Kramers IVC 排除句、IKS/TRS-IVC 候选句、qKekulé 沿 g3/穿越 MBZ 边界句、伪隙区 ν≈−2.3~−2.5 最大句、SC parent state 句、εr=30/15 句、位移场不改 qKekulé 句、"very close to a commensurate modulation"句均逐字存在于 txt。
- ⚠️ 降级/修正记录：见「更正日志」。

---

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-09-03 | 样品 C 应变两处来源不一致：Methods 写 ε=−(0.11±0.04)%、φ=(60±10)°，而 ED Fig.9 图注写 ϵ=0.08%——本笔记两处并列标注 📜Q 来源，不做归一；读者引用样品 C 应变时须注明出处（可能为不同测量区域/取整差异，💭I）。 |
| 2026-09-03 | 能隙能量（meV）：主文提取范围仅有 "correlated gap / (pseudo)gap" 定性表述与 Fig.2j 色标，**无 meV 数值**——本笔记不写任何能隙数值，标 NEEDS_VERIFICATION(SI)；避免从色标反推（色标为 dI/dV a.u.，非能量轴）。 |
| 2026-09-03 | moiré 波长 l₁/l₂/l₃（8.98/8.83/8.60 nm）为 Fig.1b/Fig.3a **面板标注**文本（非 caption 句），按 txt 可 grep 处理为 📜Q[~] 并注明图内标注来源；若视为"图读值"应降级 📊F[读图]（保守使用：仅作几何参照，不进核心结论）。 |
| 2026-09-03 | I1/I2/I3 与 g1/g2/g3、l1/l2/l3 符号易混：lᵢ 为实空间 moiré 波长方向、gᵢ 为对应倒格矢（gᵢ ⊥ lᵢ）；qKekulé 沿 g3、⊥ l3——笔记中严格区分，避免跨论文符号迁移。 |
| 2026-09-03 | "|qKekulé|/|g3| 数值范围(0.3–0.6 等)"未采用：Fig.4l 纵轴数值在 txt 中与相邻面板文本混淆，无法可靠归属，故只引用正文文字量（"≈½ moiré 倒格矢"、"穿越 g3/2"），不引轴读值。 |
| 2026-09-03 | 全文无 ± 声明补录：样品 A θ=1.60°±0.01°、应变 ±0.04%、φ ±10° 为 Methods 带误差棒数值 [±]；l₁/l₂/l₃、Kekulé 填充区间、qKekulé 演化趋势等为无误差棒表述 [~]；正文无 (伪)隙 ± 值。 |
