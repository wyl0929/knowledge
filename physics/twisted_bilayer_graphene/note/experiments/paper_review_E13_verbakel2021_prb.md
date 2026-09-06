<!--
 * @Author       : AI 精读 (系统辨识式阅读法 → 三层分离整理)
 * @Date         : 2026-08-06（初读）→ 2026-09-01（按新方案 4 块模板重写）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/experiments/paper_review_E13_verbakel2021_prb.md
 * @Description  : E13: Verbakel et al. 2021 — 室温 FFT-STM 证明小角 TBG 畴壁 1D 态的谷保护（纯 review：QPI 物理已剥离到 note/shared/physics/）
-->

# Paper Review: Verbakel et al. (2021) — 室温 FFT-STM 证明畴壁 1D 态谷保护

| 字段 | 内容 |
|------|------|
| **编号** | E13 |
| **标题** | Valley-protected one-dimensional states in small-angle twisted bilayer graphene |
| **作者** | J.D. Verbakel, Q. Yao, K. Sotthewes, H.J.W. Zandvliet |
| **期刊** | Physical Review B **103**, 165134 (2021)（Editors' Suggestion） |
| **DOI / arXiv** | 10.1103/PhysRevB.103.165134 / [arXiv:2109.04128](https://arxiv.org/abs/2109.04128)（arXiv 号已核实；为**发表后补投**——收稿 2020-12、PRB 2021-04、arXiv 2021-09） |
| **类型** | 实验 — 室温 STM + FFT 散射分析（FT-STM / QPI） |
| **课题组** | Zandvliet group（Univ. Twente，Physics of Interfaces and Nanomaterials，MESA+） |
| **PDF** | ✅ reference/pdfs/Verbakel 等 - 2021 - ...pdf（5 页正文，无 SI） |
| **精读日期** | 2026-08-06（初读）→ 2026-09-01（按新方案重写） |

> **共享知识引用**：通用物理已剥离到 `note/shared/physics/`——谷 Chern / helical 机制见 `[PHY-BERRY]`；FT-STM / QPI / intervalley 散射判据见 `[PHY-QPI]`。本 review 只写"本文代入"的数字，不复制讲义。阅读疑问见 `note/shared/method/mechanism_questions.md` `[METHOD-Q]`。

---

## TL;DR

**本文想解决的问题**：小角 TBG 在垂直电场下形成的三角 1D 畴壁网络已被多篇实验"看见"，但其输运是否真如理论预言的 **valley-protected（谷间背散射被拓扑抑制）**，一直缺直接实验证据——弹道输运 ≠ 谷保护。

**主结果**：① **室温** STM 直接成像 θ=0.55° TBG 的三角网络（此前 Huang 2018 需 4.5 K）；② 对原子分辨图做 FFT 的三对照判据——缺陷-free 网络只有 1×1 斑、**(√3×√3)R30° intervalley 斑缺失**，而 H 缺陷 HOPG 出现该斑（阳性）→ 反向传播 1D 态的输运 **valley-protected**（谷保护的唯一直接实验证据）。

**结论/意义**：作者措辞 "convincing / compelling / solid experimental evidence"（📜Q 摘要/Conclusion）——1D 通道可跨多个 moiré 周期延伸，前提是两层 defect-free；单个缺陷即可局部破坏谷保护。

---

## 1. 系统辨识导览（判别表为全文唯一权威，机制细节见 [PHY-*]）

**黑箱三要素**：`{输入旋钮：样品偏压 V / 功函数差 Δφ / 背栅 V_g / 样品区选择 | 输出观测量：FFT 谱中 1×1 斑与 (√3×√3)R30° 斑的有/无 | 声称结论：1D 态输运 valley-protected}`

**四层变量图**（符号层一次钉死）：

| 层 | Verbakel 2021 实例 |
|----|-------------|
| **L1 旋钮 u** | 样品偏压 $V$、针尖-样品功函数差 $\Delta\varphi$、背栅 $V_g$（可选）、**样品区**（pristine HOPG / H-缺陷 HOPG / TBG 网络） |
| **L2 导出量 x₁** | 垂直电场 $E$（由 $V+\Delta\varphi+V_g$ 产生 → 破 AB/BA 反演对称 → 开隙） |
| **L3 模型量 x₂** | $C_v=\pm1$（AB/BA 域）、$\Delta C_v=\pm2$（边界）、$\vert b\vert=\frac{4\pi}{3a}\approx2.95$ Å⁻¹、$\vert\Delta K\vert=\frac{4\pi}{3\sqrt3 a}\approx1.70$ Å⁻¹ |
| **固定参数（非旋钮）** | $\theta=0.55°$、$\lambda=a/[2\sin(\theta/2)]$、自旋简并 2、室温（约 300 K） |
| **反推量 θ̂** | 「intervalley 散射**有/无**」二元判定——本文**无数值参数反推**（区别于 E12 的 $v_{DW}/L_\phi/\varepsilon$） |
| **L4 观测量 y** | FFT 谱：1×1 六角斑（有/无）、(√3×√3)R30° intervalley 斑（有/无） |

> 与 E12 的本质差异：E12 用输运（ρxx/ρxy/FFT 谱）反推几何与能谱数值；本文用**散射空间**二元判据证谷保护，全篇定性"有/无"、无误差棒、无定量比值。

**可辨识性判别表**（唯一权威；三对照实验，机制见 [PHY-QPI]）：

| 判别 | 判据（数据） | 排除谁 | 确立谁 |
|------|-------------|--------|--------|
| **D1 方法有效**（FFT 能分辨 intervalley） | H-缺陷 HOPG 的 FFT 出现 (√3×√3)R30° 斑（Fig. 3d），pristine HOPG 无该斑（Fig. 3b）📜Q | "FFT 对 intervalley 散射不敏感 / 仪器不可见" | (√3×√3)R30° 斑 = intervalley 散射的可靠指纹 |
| **D2 网络谷保护**（核心结论） | TBG 网络 AA 节点区原子分辨 FFT 只有 1×1 斑、无 (√3×√3)R30° 斑（Fig. 3f）📜Q | "网络内存在 intervalley backscattering（无谷保护）" | 1D 通道 + AA 节点输运 **valley-protected** |
| **D3 室温存在** | 室温 STM 直接成像三角网络（Fig. 1a，θ=0.55°）📜Q | "网络仅低温（4.5 K）存在" | 网络室温可观测（非低温特化） |

> **主结果 ↔ 判别表的对应**：
> - 主结果①（谷保护直接证据）← {D1 方法有效, D2 网络谷保护}
> - 主结果②（室温网络）← {D3 室温存在}（直接成像，非排除式判别）
> - （前提）1D 网络存在 ← Fig. 1a 直接成像（非判别）
>
> **分层排除注**：本文的辨识结构是"**方法自证 → 判据应用**"两层嵌套：D1 先证 FFT 指纹可靠（用缺陷石墨烯作阳性对照），D2 才把该指纹用于网络（实验组）。作者用词 "convincing / compelling evidence"（📜Q），未用 "prove"——判据是"测量分辨率内无 intervalley 斑"，非"绝对为零"。

> **[前提与限定]**（判别结论的适用范围）：
> - **噪声/扰动**：室温（散射空间分析不依赖能谱分辨率，但 STS 能谱热展宽大）；**必须缺陷-free**——本文专选无缺陷区，单个缺陷即可引入 intervalley 散射破坏判据（作者自陈，引 ref 18）；功函数差难控（依赖针尖几何）→ 电场未精确标定。
> - **判别性扫轴**：**无磁场/密度扫轴**；判据靠"空间三区域对照"（pristine / H-缺陷 / TBG）+ 能量轴（零偏压 STS 见 LDOS 增强，引 ref 28）。定性有/无，无定量比值、无误差棒。
> - **候选集 M 边界**：本文判的是**二元问题**（intervalley 散射有/无），非多模型竞争 → 封闭世界风险低；但三处边界必须声明：① "fully absent" 是测量分辨率内无峰，非绝对零；② 局域探针（STM）散射证据，非输运级非局域测量；③ 结论只对 **defect-free** 网络成立（有缺陷时谷保护被局部破坏，作者明确）。

三层标注：📜Q = 原文事实（附位置）｜推导｜📊F = 读图估算｜💭I = 推断。**不确定度（正交轴）**：[±] 原文误差棒 / [~] 原文无误差棒 / [读图] 图提取 / [相对] 仅相对量。本文无误差棒 → 全为定性"有/无"判据，标记 [~]。所有数字经 pdftotext + grep 反向核对。

---

## 2. 结果与机制（按论文：机制前提 / 三对照判据 / 适用边界）

### 2.1 室温网络与谷保护机制（前提结构）

**网络成像**：室温 STM 直接拍到 θ=0.55°（由 moiré 周期提取）TBG 的三角 1D 网络——畴壁为 link、AA 区为 node 📜Q（引言 Fig. 1a/b）。此前 Huang 2018 在 4.5 K 观测，本文把网络推进到非低温 📜Q（引言）。

**谷保护机制（理论前提，非本文新推导）**：垂直电场破 AB/BA 反演对称 → AB/BA 域各得 $C_v=\pm1$（符号依赖堆垛与场方向）→ AB/BA 边界 $\Delta C_v=\pm2$ → 每边界每谷 2 条拓扑保护 helical 通道；计入自旋 → 边界 1D 态总电导 4e²/h；畴壁电流 valley-polarized（K 与 K′ 反向传播）→ intervalley backscattering 被拓扑保护压制；AA 节点处 K 态有 3 个 valley-preserving 散射方向（6 中选 3）📜Q（引言 + Fig. 2a/b）。——机制分层见 [PHY-BERRY]（chiral/helical 辨析、$C_v$ 决定通道数）。

### 2.2 FFT 谷保护判据（核心发现，三对照）

判据原理：石墨烯 FFT 中 1×1 斑（$\vert b\vert\approx2.95$ Å⁻¹）对应晶格；缺陷诱导的 intervalley 散射产生 (√3×√3)R30° 斑（$\vert\Delta K\vert\approx1.70$ Å⁻¹）——机制见 [PHY-QPI]。三对照：

1. **基准（pristine HOPG）**：FFT 只有 1×1 六角斑 📜Q（Fig. 3b）。
2. **阳性（H 吸附 HOPG）**：FFT 出现 1×1 斑 **加** (√3×√3)R30° intervalley 斑 → 证明该斑确为 intervalley 散射指纹（D1）📜Q（Fig. 3d）。
3. **实验组（TBG 网络）**：AA 节点区原子分辨图（Fig. 3e）的 FFT 只有 1×1 斑、**无** (√3×√3)R30° 斑 → 1D 通道与 AA 节点处输运 valley-protected（D2）📜Q（Fig. 3f）。

> 关键逻辑：D1（阳性对照）与 D2（实验组）共用同一判据——若 intervalley 斑在缺陷石墨烯中清晰可见、在缺陷-free 网络中缺失，则"网络无 intervalley 散射"不是仪器灵敏度问题，而是谷保护的真实信号。这是本文论证的含金量所在（无阳性对照则"无峰"可被"看不见"解释掉）。

### 2.3 电场来源与缺陷鲁棒性（作者自设的适用边界）

- **STM 中电场来源**：样品-针尖偏压 $V$ + 针尖/样品功函数差 $\Delta\varphi$ +（可选）背栅 $V_g$，共同开 AB/BA 能隙 📜Q（Discussion）。功函数差难控（依赖针尖几何）；原文称 "a minor difference in work function of a few tens of eV" 已可产生可观电场（⚠️ 疑为 meV 量级笔误，功函数差物理上 ~0.1–1 eV 💭I）。小样品-针尖距离使零偏压下拓扑态仍可观测：STS 显示畴壁 LDOS 高于 AB/BA 域（引 ref 28，同组 Yao 2020）📜Q。
- **缺陷鲁棒性（作者自设的局限）**：单个晶格缺陷即可引入 intervalley 散射、局部破坏网络使其退回 gapped 相（引 ref 18）📜Q；H 原子退火可去除，但高温退火会致 TBG "untwist" 回 Bernal 堆垛 → **应避免退火** 📜Q（refs 9,29–31）；理论预言 H 优先吸附于 AA 区（ref 32）→ 可能整节点被消除（比单 link 破坏更严重）📜Q。→ 结论：器件化需极高晶体质量 + hBN capping 层防吸附 📜Q。

---

## 3. 实验方法

### 3.1 器件 / 样品
HOPG 样品（HQ Graphene），天然 Bernal 堆垛、表层频繁出现扭转畴 → 自然形成 TBG；本样品 θ=0.55° 📜Q（Methods）。⚠️ 是 HOPG 表层扭转（非 SiC 外延、非 tear-and-stack）——旧 bl-dw 笔记曾误作 "SiC 外延生长"，已更正。

### 3.2 静电学（电场来源，非双栅 n/D 换算）
电场 = 样品偏压 + 功函数差 + 背栅（无平行板电容标定；见 §2.3）。与 E12 的双栅 $n$/$D$ 换算（[PHY-GATE]）不同——本文电场未定量标定，只作"开隙"旋钮 📜Q。

### 3.3 测量（FFT-STM，非常规预处理）
Omicron STM1，电化学刻蚀 W 针尖，UHV 基底压强 3×10⁻¹¹ mbar，**室温** 📜Q（Methods）。对 STM 形貌图做 2D FFT → q 空间散射谱（FT-STM）；判据 = 检查 (√3×√3)R30° 斑有/无——机制见 [PHY-QPI]。偏压/电流：Fig. 1a 网络 400 mV/500 pA；Fig. 3a pristine −600 mV/1 nA；Fig. 3c H 缺陷 −500 mV/600 pA；Fig. 3e AA 节点 400 mV/500 pA 📜Q（各 caption）。

---

## 4. 关键数据（提取链 + 验证链 + 不确定度标注）

### 4.1 几何与谷 Chern 结构
| 参数 | 值 |
|------|-----|
| θ | 0.55°（由 moiré 周期提取）📜Q [~] |
| λ | 原文只给公式 λ=a/[2 sin(θ/2)]；代入 θ=0.55°、标准 a=0.246 nm → λ≈25.6 nm（**推导**，原文未给 λ 数值） |
| $C_v$（AB/BA 域） | ±1（符号依赖堆垛 + 场方向）📜Q |
| $\Delta C_v$（边界） | ±2 📜Q |
| 每边界通道 | 每谷 2 条 helical → 计入自旋 4 条 → 总电导 4e²/h 📜Q |

### 4.2 散射矢量
| 矢量 | 公式（原文） | 值 |
|------|-------------|-----|
| 1×1 倒易斑 $\vert b\vert$ | $4\pi/3a$ | ≈2.95 Å⁻¹ 📜Q [~] |
| intervalley 斑 $\vert\Delta K\vert$ | $4\pi/3\sqrt3\,a$ | ≈1.70 Å⁻¹ 📜Q [~] |

⚠️ "a" 定义（键长 1.42 Å vs 晶格常数 2.46 Å）的等价性见 [PHY-QPI] §2。

### 4.3 FFT 判据结果（三对照）
| 区域 | 1×1 斑 | (√3×√3)R30° 斑 | 含义 |
|------|:---:|:---:|------|
| pristine HOPG | ✅ | ❌ | 基准：无 intervalley |
| H-缺陷 HOPG | ✅ | ✅ | 阳性：intervalley 指纹可靠（D1） |
| TBG 网络（AA+畴壁） | ✅ | ❌ | intervalley 被抑制 = 谷保护（D2） |

### 4.4 验证链
三对照的嵌套结构 = 本文的模型验证（[PHY-QPI] §5）：**基准（无峰）→ 阳性（有峰，证方法敏感）→ 实验组（无峰，证谷保护）**。阳性对照是关键——它把"网络无峰"从"仪器看不见"升级为"真无 intervalley 散射"。⚠️ 全链是**定性**验证：无误差棒、无强度比、无多器件统计（单一样品）📜Q。

---

## 5. 主要结论
1. 室温下小角 TBG 三角 1D 网络存在（θ=0.55°），无需低温 STM 📜Q。
2. 缺陷-free 网络的 FFT 无 intervalley 散射斑 → 反向传播 1D 态输运 **valley-protected**——谷保护的首次直接实验证据 📜Q。
3. 1D 通道可跨多个 moiré 周期延伸，前提是两层 defect-free；单个缺陷即可局部破坏谷保护 📜Q。
4. 器件化要求极高晶体质量（+ hBN capping 防吸附、避免高温退火致 untwist）📜Q。

## 6. 局限与未解决
| 局限 | 说明 | 证据 |
|------|------|------|
| 局域探针证据 | STM 散射分析，非器件级非局域输运；长程输运长度/散射率未给 | 💭I |
| 定性判据 | "有/无"峰，无定量比值、无误差棒、单一样品 | 📜Q |
| 电场未标定 | 功函数差依赖针尖几何，可控性有限 | 📜Q |
| 无 B/密度扫轴 | 未测磁场/密度下谷保护的演化 | 💭I |
| 自然样品 | HOPG 表层自然扭转，"发现式"非可编程制备 | 📜Q |
| 缺陷-退化关系 | 单个缺陷破坏谷保护仅为理论讨论（ref 18），无受控缺陷实验 | 📜Q |
| 温度窗口 | 只证"室温可见"，上限/热稳定性未系统测试 | 💭I |

## 7. 与其他工作的关系
| 工作 | 关系 |
|------|------|
| Huang 2018（ref 14, E9） | 4.5 K 首次 STM 发现网络（LDOS 双线）——本文补"谷保护"关键环节 + 推进到室温 📜Q |
| San-Jose & Prada 2013（ref 18, T5）/ Efimkin & MacDonald 2018（ref 20, T9）/ Tsim & Koshino 2020（ref 19, T12）/ Zhang-MacDonald-Mele 2013（ref 17, T6） | valley Chern 机制理论来源——本文给出直接实验呼应 📜Q |
| Rickhaus 2018（ref 15, E10）/ Xu 2019（ref 16, E12） | 输运证明弹道/相干——本文补"弹道 ≠ 谷保护"的显微证据 📜Q |
| Rutter 2007（ref 24）/ Dutreix 2019（ref 25） | QPI / intervalley 散射的 FFT 方法学先例 📜Q |
| Yao 2020（ref 28，同组） | 零偏压 STS 畴壁 LDOS 增强（本文电场来源的前置证据）📜Q |

## 8. 对后续研究的影响
- FFT-STM 成为"谷保护是否成立"的快速诊断工具（有/无 intervalley 斑）💭I。
- 室温可观测 → 降低 valleytronic 网络器件对低温的依赖 💭I。
- "超低缺陷密度"是谷保护实用化前提 → 推动高质量 TBG 制备 + hBN capping 📜Q。
- 留下待定量闭环：缺陷类型/浓度 → intervalley 散射 → 器件性能的定量图谱；STM 散射证据 ↔ 多端输运量测（非局域、长度/温度依赖）的一一对应 💭I。

## 9. 理论模型映射（供计算对标）
| 映射 | 说明 |
|------|------|
| 电场 → 开隙 → $C_v$ | 垂直电场破 AB/BA 反演对称 → $C_v=\pm1$、边界 $\Delta C_v=\pm2$ 📜Q |
| $\theta\to\lambda$ | λ=a/[2 sin(θ/2)]，θ=0.55°→λ≈25.6 nm（推导）📜Q |
| 判据 ↔ FFT 斑 | intervalley 散射 ↔ (√3×√3)R30° 斑有无；$\vert b\vert$=2.95、$\vert\Delta K\vert$=1.70 Å⁻¹ 📜Q |
| 通道计数 | 每边界每谷 2 helical + 自旋 2 → 4e²/h 📜Q |

> 与 TBPM/Kubo 对应：FFT-STM 的 q 空间功率谱 = 实空间 LDOS 的 2D FFT，可由 TBPM 计算 LDOS(r) 后 FFT 复现；intervalley 斑有无对应"谷间散射通道是否被激发"，可作谷保护 benchmark（同 bl-dw 旧笔记 §10 的判断，保留）💭I。

---

## 目的接口（Phase S 三问，随项目增删，不进入正文）

- **Q1（edge state 如何表征）**：原子分辨 STM + FFT 散射分析。核心可观测量 = FFT 中 intervalley 散射峰 (√3×√3)R30° 的**缺失**（散射空间判据）——直接证明谷间背散射被抑制 = 谷保护。三对照（pristine 基准 / H 缺陷阳性 / TBG 网络实验组）锁定判据可靠性。见 §2.2 / §4.3。
- **Q2（理论如何解释）**：无新理论，直接引用 valley Chern 机制（San-Jose & Prada / Efimkin & MacDonald / Tsim & Koshino / Zhang-MacDonald-Mele）——电场开隙 → $C_v=\pm1$ → 边界 $\Delta C_v=\pm2$ → 2 条/谷 helical 通道 → intervalley backscattering 被拓扑压制。见 §2.1。
- **Q3（理论↔实验对应）**：理论预言"intervalley backscattering 被抑制" ↔ 实验"网络 FFT 无 (√3×√3)R30° 斑"（而缺陷石墨烯有）——谷保护的直接对应。见 §2.2。

> **增量价值**：E13 是谷保护的**唯一直接实验证据**（Q1 的定论性工作，plan.md §2.2 / cards.md 定位）。与同族笔记的分工：E9 只"看见网络形貌"（未证谷保护）、E10/E12 证弹道/相干（弹道 ≠ 谷保护）、本文补上"谷选择性散射"这一环并把网络推进到室温。report.md §2（Q1 表征）取用其判别表与 §4.3 三对照表；比 E10/E12 多的维度 = 散射空间谷选择性（FT-STM），少的 = 输运/能谱数值（本文无定量反推）。

## 反向核对 pass (2026-09-01)
pdftotext 提取 5 页正文，逐项 grep 核对：θ=0.55° / 4e²/h / ΔC_v=±2 / |b|=2.95 / |ΔK|=1.70 / (√3×√3)R30° / 3×10⁻¹¹ mbar / 各偏压-电流（400 mV 500 pA、−600 mV 1 nA、−500 mV 600 pA）/ "few tens of eV" / "fully absent" / "convincing" / "compelling" 均在原文找到。⚠️ 无源数字清理：旧笔记"谷内/谷间强度比 ≫ 1"、"能隙 > k_B T≈26 meV" 为无源推断 → 删除或降级；"SiC 外延生长" → 更正为 HOPG。λ≈25.6 nm 标注为推导（原文未给数值）。

## 更正日志
| 日期 | 条目 |
|------|------|
| 2026-09-01 | 按新方案（三层分离 4 块模板 + QC v1.1）整体重写：判别表化（三对照 D1/D2/D3）+ [前提与限定] 块 + 主结果↔判别映射 |
| 2026-09-01 | 三层分离：FT-STM / QPI / intervalley 散射通用物理剥离到 `note/shared/physics/08_qpi_intervalley.md`（[PHY-QPI]）；valley Chern 机制引用既有 [PHY-BERRY] |
| 2026-09-01 | QC 更正（vs 旧 bl-dw 笔记）：① "SiC 外延生长" → **HOPG 表层扭转**（原文 Methods 明示，全 PDF 无 SiC）；② 删"谷内/谷间强度比 ≫1"无源数字 → 定性"有/无"判据；③ 删"能隙>k_B T≈26 meV"脑补；④ arXiv 2109.04128 经 arxiv.org 检索核实（发表后补投，非 registry 笔误）；⑤ θ 从 "<1°" 精确到 0.55° |
