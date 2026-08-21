<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 22:02:08
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 22:02:12
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/experiments/paper_review_E09_huang2018_prl.md
 * @Description  :
-->
<!--
 * @Author       : AI 精读 (research_onboarding_skill)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/note/experiments/paper_review_E09_huang2018_prl.md
 * @Description  : E9: Huang et al. 2018 — STM 首次发现 mTBG 畴壁 TPH 态
-->

# Paper Review: Huang et al. (2018) — mTBG 拓扑螺旋态的 STM 发现

| 字段 | 内容 |
|------|------|
| **编号** | E9 |
| **标题** | Topologically Protected Helical States in Minimally Twisted Bilayer Graphene |
| **作者** | Shengqiang Huang, Kyounghwan Kim, Dmitry K. Efimkin, Timothy Lovorn, Takashi Taniguchi, Kenji Watanabe, Allan H. MacDonald, Emanuel Tutuc, Brian J. LeRoy |
| **期刊** | PRL 121, 037702 (2018) |
| **DOI** | 10.1103/PhysRevLett.121.037702 |
| **arXiv** | 1802.02999 |
| **类型** | 实验 — STM/STS |
| **课题组** | LeRoy group (Univ. Arizona) + MacDonald theory (UT Austin) |
| **PDF** | ✅ reference/pdfs/Huang 等 - 2018 - ...pdf |
| **DW.bib** | ✅ `huang_topologically_2018` |
| **精读日期** | 2026-08-06 |
| **Phase S 重读** | 2026-08-19（三问框架 + QC 证据分级） |

---

## 1. 核心贡献

**首次直接实验观测**极小扭角双层石墨烯（TBLG）畴壁网络上的**拓扑保护螺旋态（TPH states）** 📜Q（摘要: "demonstrate the emergence of TPH states on the domain wall network"）。通过 STM/STS：

- 观测到畴壁上增强的局域态密度（LDOS）📜Q
- 观测到 TPH 态特有的**双线（double-line）空间分布** 📜Q（摘要: "a double-line profile of the TPH states on the domain walls"）
- 证实 TPH 态仅在 AB/BA 区域被垂直电场打开能隙时才出现 📜Q（摘要: "only occurring when the AB and BA regions are gapped"）
- 展示了可控扭角制备超长莫尔周期（>50 nm）畴壁网络的方法 📜Q（摘要: "designer moiré crystals with wavelengths longer than 50 nm"）

## 2. 物理机制

### 2.1 TPH 态的形成条件

1. AB 与 BA 堆垛在外加垂直电场下开隙 → 产生大 Berry 曲率 📜Q（引言: "develop an energy gap and large Berry curvatures"）
2. 每谷 valley Chern number 量子化为 |C| = 1，符号依赖电场方向与堆垛构型 📜Q（引言: "quantized at unit magnitude with a sign that depends on both the sign of the electric field and the stacking configuration"）
3. AB 与 BA 在同一电场下 valley Chern number 符号相反 → 边界支持反向传播谷手征模 = TPH 态 📜Q（引言: "AB and BA stacked regions ... have opposite Chern numbers under a uniform electric field"）
4. **仅在 AB/BA 开隙时 TPH 态才出现**；电场近零时畴壁对比显著减弱 📜Q（Fig. 3c + 正文）

### 2.2 理论框架

- 低能连续模型（Bistritzer–MacDonald, ref [39]）📜Q
- 畴壁网络模型（San-Jose & Prada 2013 ref [10]; Efimkin & MacDonald 2018 ref [38]）📜Q
- 网络特征能标 $E_\lambda = \frac{2\pi\hbar v}{3\lambda} \approx 24\,\text{meV}$ 📜Q（正文原式；代入本文 λ=57.6 nm 与原文值一致）

### 2.3 两类能量特征

- $E \ll \Delta$（隙内）：畴壁螺旋态主导，网络干涉导致低能结构 📜Q（正文: "the only relevant degrees of freedom are helical states along the domain walls. Their interference results in the domain wall pattern band structure"）
- $E \gtrsim \Delta$（隙外）：高能 van Hove 特征，两个 saddle points 在 E ≈ ±250 meV 📜Q（正文 + Fig. 4 段: "±250 meV from the charge neutrality point"）

## 3. 实验方法

### 3.1 样品制备（sequential pickup）

- 薄 h-BN（∼10–20 nm）作拾取层，从**同一片单层石墨烯**连续拾取两块 📜Q（正文: "sequential pickup, using a thin h-BN flake, of two graphene pieces from the same monolayer flake"）
- 半球形手柄衬底（覆 PVA）先拾 h-BN，再连续拾两块石墨烯；两块之间旋转手柄设定扭角（同源 → 晶格取向一致 → 扭角由旋转角直接决定）📜Q（正文 + Fig. 1a）
- 堆叠顺序：SiO₂/Si 衬底上 h-BN 在下、TBLG 在上（TBLG 直接暴露于 STM 探针）📜Q（正文: "placed on a SiO₂=Si substrate with the TBLG on top of h-BN"）；TBLG 与 h-BN 间扭角取大值以免 h-BN 影响电子性质 📜Q
- 电极：Cr 5 nm / Au 35 nm，EBL 定义，接触 TBLG 与硅背栅，控制电荷密度与层间偏压 📜Q
- 退火：高真空 350°C, 6 h 📜Q

> ⚠️ 注：「tear-and-stack」为社区惯称 💭I（推断），原文仅用 sequential pickup。

### 3.2 STM/STS 测量

- 温度：4.5 K，超高真空 📜Q
- 探针：电化学刻蚀 W tip 📜Q（tip 校准与可重复性见 SI [30]）
- 隧穿条件：I = 200 pA，稳定电压 V = +0.5 V 📜Q（Fig. 1c/d caption）
- STS 调制：3 mV @ 572 Hz 交流电压加在样品电压上测 dI/dV 📜Q（正文）；LDOS map 用 8 mV 📜Q（Fig. 3 caption）
- ⚠️ 「锁相」一词正文未出现，dI/dV 用锁相检测为 💭I（推断，标准做法）
- 背栅调控电荷密度与层间电场 📜Q

## 4. 关键数据

### 4.1 样品参数

| 参数 | 值 | 证据 |
|------|-----|------|
| 莫尔周期 λ | 57.6 ± 0.7 nm | 📜Q（正文 + Fig. 1c caption） |
| 扭角 θ | 0.245 ± 0.003° | 📜Q（正文） |
| 畴壁宽度 | 数 nm（several nanometer） | 📜Q（正文） |
| 莫尔周期下限 | > 50 nm（波长可控） | 📜Q（摘要/正文） |
| Fig. 1c scale bar | 80 nm | 📜Q（caption） |
| Fig. 3 scale bar | 50 nm | 📜Q（caption） |

### 4.2 STS 谱特征（Fig. 1d, Vg = +60 V）

- **AB 区**：−0.1 V 附近 dip（电场打开带隙）📜Q；+0.3 V 附近上升（导带第二子带）📜Q
- **畴壁**：无 −0.1 V dip；在电荷中性点两侧 ±0.25 V 出现对称双峰 📜Q
- **背栅依赖**（Fig. 2）：带隙宽度随 Vg 增大而增大，正大 Vg 时最大、随 Vg 减小而缩小 📜Q（正文）；扫描范围 −80 ~ +40 V 📊F（读图估算，Fig. 2 横轴）；gap 宽度约 10–70 meV 📊F（读图估算，Fig. 2c 纵轴）

### 4.3 空间 LDOS 成像（TPH 关键证据，Fig. 3）

- **Vg = +60 V，Vb = −0.11 V（带隙中心）**：畴壁网络亮、AB/BA 区暗（因 gap），呈**双线**分布 📜Q（Fig. 3a caption + 正文）
- **Vg = +60 V，Vb = −0.245 V（隙外）**：畴壁与区域对比显著下降 → TPH 态仅在 AB/BA 被 gapped 的能量处出现 📜Q（正文）
- **Vg = −50 V，Vb = 0.1 V（电场≈0）**：畴壁增强缺失 → "无隙则无 TPH" 📜Q（Fig. 3c caption + 正文: "where the electric field is negligibly small"）
- 双线空间分离此前已在孤立畴壁上报道，与螺旋态预言一致 📜Q（正文引用 ref [19] = Yin 2016, E4）

### 4.4 定量对比度分析（Fig. 4）

定义对比度 $C = [I(DW) - I(AB)] / I(AB)$ 📜Q（正文原式）：

- Vg = +60 V：C(V) 在 AB 带隙中心有主峰，AB 区导/价带边附近降到近零 📜Q（正文；带边由 FT-STS 确定，见 SI [30]）
- Vg = −50 V：中心峰消失，±0.25 V 两个高能峰仍可见 📜Q（正文: "since there is no electric field and no TPH states occur, but the two additional peaks are still visible"）
- 中央峰 FWHM 与 FWHM 范围内平均对比度均随 Vg 减小而下降 📜Q（Fig. 4c/d；误差棒为平均值的标准差）→ TPH 强度与 gap 大小相关 📜Q（正文）

## 5. 主要结论

1. **TPH 态存在**：畴壁处隙内 LDOS 增强 + 双线空间分布 + 仅在开隙时显著 📜Q（Fig. 3 + 正文）
2. **多重一致性**：与连续模型 [39] 和网络模型 [10,38] 在能谱特征上相符 📜Q（正文: "The theoretical model captures all the principal observed features at energies E ≳ Δ"）
3. 畴壁网络可作拓扑通道"以无耗散方式输运电荷" 📜Q（正文: "transfer charge in a dissipationless manner"）；畴壁长度由扭角决定（制备时可控）→ **可设计的拓扑通道网络** 📜Q（正文末段）

## 6. 局限与未解决的问题

| 局限 | 说明 | 证据 |
|------|------|------|
| 仅局域谱学 | 全文无输运测量（无反散射长度、电导平台等量化） | 💭I（推断，事实为本文只做 STS） |
| 保护性未量化 | valley 混合、无序、边缘粗糙度的影响未系统研究 | 💭I（推断，原文未涉及） |
| 低能分辨率不足 | $E_\lambda \ll \Delta$ 条件 "not so well satisfied"，仅 −0.05 V 处一个网络峰可清晰分辨 | 📜Q（正文: "only the peak at −0.05 V in Fig. 1(d) is well resolved"） |
| 谷保护未直接验证 | 仅形态学（双线 + 电场开关）证据，无 valley 选择性散射实验 | 💭I（推断，卡片同款判断） |
| 高温稳健性未知 | 全部测量在 4.5 K | 💭I（推断） |
| 与强关联物理的关系 | 未涉及 magic-angle 关联态与拓扑态的竞争/耦合 | 💭I（推断） |

## 7. 与其他工作的关系

| 工作 | 关系 |
|------|------|
| San-Jose & Prada 2013 (ref [10]) | 理论预言 — 本文给出直接实验证据 📜Q（正文引用其图 2f 作 −50 V 对照） |
| Efimkin & MacDonald 2018 (ref [38]) | 畴壁网络能谱理论 — 本文 STS 谱与之一致 📜Q（正文引 [10,38]） |
| Martin et al. 2008 (ref [2]) | 电场畴壁拓扑束缚的原始预言 📜Q（引言引 [2]） |
| Ju et al. 2015 (ref [18]) | 均匀 BLG 畴壁输运实验 📜Q（引言引 [18]） |
| Yin et al. 2016 (ref [19]) | STM 观测 BLG 单条畴壁边缘态；**双线空间分离此前已在孤立畴壁报道** 📜Q（Fig. 3a 段正文引 [19]） |
| Li et al. 2016 (ref [16]) | split-gate 调控电场 → TPH 弹道输运 📜Q（引言引 [16,17]） |

## 8. 对后续研究的影响

- 将"拓扑界面态"从单条界面推进到**二维可工程化网络** 💭I（推断，正文末段支撑: "enabling controllable topological networks"）
- 方法学：证明扭角工程 + 局域探针可直接鉴别拓扑态 💭I（推断）
- 与 2018 年 magic-angle 热潮并行，开辟"非强关联拓扑网络"研究主线 💭I（推断，外部背景）
- 启示：畴壁长度 = f(θ) → 可按需设计拓扑通道网络 📜Q（正文: "The length of the domain walls depends on the twist angle ... which can be controlled during fabrication"）

---

*精读完成日期：2026-08-06（pdftotext 全文提取 + AI 精读） | 2026-08-19 三问框架重读 + QC 证据分级（pypdf 全文提取 → /tmp/huang2018.txt → grep 反向核对）*

---

## Phase S 补充 (2026-08-19): Q1/Q2/Q3 三问框架

### Q1: edge state 实验上如何表征?

低温 STM/STS 直接成像 mTBG 畴壁网络 📜Q（4.5 K, 超高真空）。

- **技术**：STM 形貌 + STS 点谱 + 空间 LDOS map 📜Q
- **核心可观测量**：LDOS 空间图——畴壁上的强隙内 LDOS 增强，呈特征双线（double-line）图案 📜Q（Fig. 3a: Vg=+60 V, Vb=−0.11 V）
- **关键对照（边-体区分）**：LDOS 增强仅在垂直电场打开 AB/BA 能隙时出现——移去电场（Vg=−50 V）或移出隙外能量（Vb=−0.245 V）时对比消失 📜Q（Fig. 3b/c）
- **定量化**：对比度 C = [I(DW)−I(AB)]/I(AB)，中央峰 FWHM 与平均对比度随 Vg 同步下降 → TPH 强度 ∝ gap 大小 📜Q（Fig. 4）
- 首次直接观测 mTBG 中 TPH 态 📜Q（摘要）。局限：未直接验证谷保护（仅形态学证据）💭I（与卡片一致）

> ✅ 与 cards.md E9 卡片逐条核对一致：技术/可观测量/边体区分/核心发现/理论框架/局限，无遗漏。

### Q2: Vg（背栅）与 sample bias 的关系?

- **Vg = 硅背栅电压**：控制电荷密度 + 层间电压偏置 📜Q（正文: "silicon back gate ... for control of the charge density and interlayer voltage bias"）
- **sample bias = 针尖-样品直流偏压**：STS 的能量轴（Fig. 1d 横轴 "Sample voltage (V)"）📜Q
- **关键关系**：层间破反演电场有三个贡献 = 背栅 + tip bias + 针尖与 TBLG 功函数失配；后两者使"零电场点"对应的 Vg 发生偏移 📜Q（正文: "The electric field has contributions from the back gate voltage, the tip bias, and the work function mismatch"）→ 因此 gap 在**正大 Vg** 区最大（而非 Vg=0 处）📜Q（正文）
- **本文出现的 Vg 集合**：+60 V（Fig. 1d / 3a / 3b / 4a）；−50 V（Fig. 3c / 4b，电场≈0 📜Q 正文）；扫描 −80 ~ +40 V（Fig. 2）📊F（读图估算）

### Q3: Vg 与 AB 能隙 Δ 的关系?

- **Δ(Vg) 单调**：gap 在正大 Vg 最大，随 Vg 减小而缩小 📜Q（正文: "The band gap is largest at large positive back gate voltages, while it diminishes as the back gate voltage decreases"）
- **数值**：gap 宽度约 10–70 meV（Fig. 2c 纵轴）📊F（读图估算）；误差棒为谱拟合不确定性 📜Q（Fig. 2 caption）
- **负 Vg 区**：AB 区 dI/dV 最小值保持恒定（gap 未打开），而畴壁最小值随 Vg 增大（DOS 因 TPH 态出现而增强）📜Q（Fig. 2d + 正文）
- **gap 提取方法**：见 SI [30]，正文未给公式 📜Q
- **TPH 强度 ↔ Δ 关联**：对比度中央峰 FWHM 与平均对比度均随 Vg（即 Δ）减小而下降 📜Q（Fig. 4c/d）
- ⚠️ **归位声明**：E4（Yin 2016）曾被误装的"Vg 依赖 gap"数据即本节内容，属本文（Huang 2018）——E4 无栅压、gap 80 meV 由石墨衬底诱导。本文是 Q1 中 Vg→Δ 数据的唯一正确出处。

---

## 反向核对 pass (2026-08-19)

pypdf 提取 → `/tmp/huang2018.txt`（6 页）→ 逐项 grep 核对结果：

- ✅ 57.6 ± 0.7 nm / 0.245 ± 0.003° / >50 nm / 24 meV / 10–20 nm h-BN / Cr 5 nm / Au 35 nm / 350°C 6h / 4.5 K / 200 pA / +0.5 V / 3 mV 572 Hz / 8 mV / −0.1 V / +0.3 V / ±0.25 V / ±250 meV / −0.05 V / +60 V / −0.11 V / −0.245 V / −50 V / 0.1 V / −80~+40 V / 80 nm / 50 nm / several nanometer width / dissipationless / sequential pickup / same lattice orientation / polyvinyl alcohol —— 全部在原文找到
- ⚠️ 原文无：lock-in（"锁相"）→ 已降级 💭I；tear-and-stack → 已标注为惯称

---

## 更正日志 (2026-08-19)

| 原表述 | 问题 | 修正 |
|---|---|---|
| "STS 锁相调制" | 正文无 lock-in 字样（grep 证伪） | → "3 mV @ 572 Hz ac 电压测 dI/dV"；锁相标 💭I |
| "样品制备（tear-and-stack / sequential pickup）" | tear-and-stack 原文未出现 | → 仅 sequential pickup，tear-and-stack 标注为社区惯称 💭I |
| "Vg = −50 V（近零电场）：畴壁增强缺失" | 缺 sample voltage 0.1 V（Fig. 3c caption） | → 补 Vb = 0.1 V |
| "带隙宽度十几到数十 meV 量级" | 无证据标注 | → 标 📊F 读图估算（Fig. 2c 纵轴 10–70 meV） |
| 全文数字无证据分级 | 违反 LITERATURE_QC_PROTOCOL | → 全部标 📜Q/📊F/💭I 并附位置 |
| 缺 Q2/Q3 节 | 三问框架不完整（E4 样板含 Q1/Q2/Q3） | → 新增 Q2（Vg↔sample bias）与 Q3（Vg↔Δ），Vg 数据归位本文 |
| 局限表各条无分级 | 推断性条目混入事实层 | → 逐条标 💭I/📜Q |
