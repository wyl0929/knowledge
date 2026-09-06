<!--
 * @Author       : AI 精读 (系统辨识式阅读法 → 三层分离整理)
 * @Date         : 2026-08-11（初读）→ 2026-08-19（QC 修正）→ 2026-09-01（按 4 块新架构重读）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/experiments/paper_review_E06_jiang2017_nanolett.md
 * @Description  : E6: Jiang, B.-Y. et al. (Basov group) 2017 — s-SNOM 等离激元在 AB/BA 畴壁处反射（4 块辨识结构重读；2026-09-01 按 4 块新架构重读）
-->

# Paper Review: Jiang, B.-Y. et al. (2017) — 等离激元被 AB/BA 畴壁的拓扑电子边界反射

| 字段 | 内容 |
|------|------|
| **编号** | E6 |
| **标题** | Plasmon reflections by topological electronic boundaries in bilayer graphene（⚠️ arXiv v1 标题为单数 "Plasmon reflection by…"，期刊版复数，正文 PDF 首行即 arXiv 版） |
| **作者** | Bor-Yuan Jiang¹†, Guangxin Ni¹†, Zachariah Addison², Jing K. Shi³, Xiaomeng Liu³, Frank Zhao³, Philip Kim³, E. J. Mele², D. N. Basov¹⁴, Michael M. Fogler¹（†并列一作；通讯 mfogler@ucsd.edu） |
| **期刊** | Nano Letters 17, 7252 (2017) |
| **DOI / arXiv** | 10.1021/acs.nanolett.7b03816（⚠️ 外部来源，arXiv 正文未出现）/ 1707.03980 |
| **类型** | 实验 + 理论 — s-SNOM 等离激元纳米成像 + 局域电导 Kubo 计算 |
| **课题组** | Basov group（UCSD / Columbia）+ Fogler（UCSD，理论）+ Mele（Penn）+ Kim（Harvard，制样） |
| **PDF / SI PDF** | ✅ `reference/pdfs/Jiang 等 - 2017 - Plasmon reflections …pdf`（22 页 arXiv v1，正文 1–14 页 + 附 Supplementary Material 15–22 页：式 S1–S13、Fig S1–S5）；⚠️ ACS 独立 SI 文件缺失（暂搁置） |
| **精读日期** | 2026-08-11（初读）→ 2026-08-19（QC 修正）→ 2026-09-01（4 块重读） |

> **共享知识引用**：通用物理已剥离到 `note/shared/physics/`，用锚点引用不重复讲义——散射/反射通道 `[PHY-QPI]`、拓扑手征模与 chiral/helical 术语 `[PHY-BERRY]`、局域能带/band bending/化学势 `[PHY-EF]`、背栅→密度 `[PHY-GATE]`。阅读疑问见 `note/shared/method/mechanism_questions.md` `[METHOD-Q]`。

---

## TL;DR

**本文想解决的问题**：红外频率下 AB/BA 畴壁对表面等离激元的反射，能否定量归因于束缚在畴壁上的电子态（拓扑手征模 + 常规波导模）对局域 ac 电导的增强？

**主结果**：① 两种壁给出两种驻波图样——拉伸壁由 1 峰过渡到 2 峰、剪切壁由 1 峰到 3 峰（Fig. 2a,b）；② 反射系数 r 拉伸壁幅值更大且近似纯虚数、剪切壁幅值更小且近似实数（Fig. 2e,f）📜Q；③ 拟合 s-SNOM 剖面与实验**定量一致**（摘要 "quantitative agreement"）📜Q。

**结论/意义**：畴壁反射探针的是一个**结构敏感的局域 ac 电导** σ⊥(x⊥)；拉伸壁额外承载常规束缚态（不穿隙）→ 与拓扑态一起增强 σ⊥。作者措辞 "proof of principle"——s-SNOM 可作 10-nm 尺度局域电子谱探针，而非"证明了拓扑"（见 §6）。

---

## 1. 系统辨识导览（判别表为全文唯一权威）

**黑箱三要素**：`{输入旋钮：Vg 背栅、固定 ω=890 cm⁻¹(≈λ 11.2 µm)、针尖位置 | 输出观测量：s-SNOM 近场振幅 s̄3 与相位 φ、垂直于壁的干涉条纹剖面 | 声称结论：畴壁反射源于拓扑手征模 + 常规束缚态增强局域 σ⊥}`

**四层变量图**（符号层一次钉死）：

| 层 | 本文实例 |
|----|---------|
| **L1 旋钮 u** | $V_g$（背栅）、$\omega$（固定 890 cm⁻¹）、针尖位置 $x_{tip}$ |
| **L2 导出量 x₁** | 载流子密度 $n$、化学势 $\mu$（拟合，见下） |
| **L3 模型量 x₂** | 堆叠序 $\delta(x_\perp)$、局域能带 $E(k_\parallel)$、局域 ac 电导 $\sigma_\perp(x_\perp)$、等离激元动量 $q_p$、波长/阻尼 $\lambda_p,\gamma$、反射系数 $r$、1D 态数 $N$ |
| **固定参数（非旋钮）** | $a=0.246$ nm、$\gamma_1=0.41$ eV、壁宽 $l$（拉伸 10.1 nm / 剪切 6.2 nm）、$\lambda=11.2$ µm、$T=300$ K（大气） |
| **反推量 θ̂** | $\mu$、$V_i$（层间偏压）、$\eta$（唯象阻尼）——三个拟合参数，由 s-SNOM 剖面反推 |
| **L4 观测量 y** | $s̄_3$（归一化近场振幅）、$\phi$（相位）、干涉条纹剖面 |

> 符号注意：$\sigma_\perp$ 是"垂直于壁方向的局域光学电导"，非霍尔电导；$V_i=V_{top}-V_{bot}$ 层间偏压；$x_\perp=y$（拉伸壁）/ $x_\perp=x$（剪切壁）。

**可辨识性判别表**（唯一权威）：

| 判别 | 判据（数据） | 排除谁 | 确立谁 |
|------|-------------|--------|--------|
| **拉伸 vs 剪切壁** | 两种驻波图样：拉伸 1→2 峰、剪切 1→3 峰（Fig. 2a,b）📜Q | 壁类型无关的单一图景 | 两种壁电子结构不同 |
| **反射来源 = 束缚态（非体连续）** | 计算的 $\sigma_\perp$：lattice（含束缚态）在壁处有峰 vs adiabatic（无束缚态）平坦（Fig. 3a）📜Q | 仅体连续（adiabatic 近似） | 束缚态增强局域 $\sigma_\perp$ |
| **拓扑态 vs 常规态** | 剪切壁 $V_i=0$ 无束缚态 → $\sigma_\perp$ 平坦；$V_i=\pm0.2$ V 开隙引入拓扑态 → 出现峰（Fig. 3c）📜Q | 常规束缚态是唯一来源 | 拓扑手征模是剪切壁反射的来源（[PHY-BERRY]） |
| **拉伸壁的常规束缚态** | 拉伸壁 $r$ 幅值大且近虚数、剪切壁 $r$ 幅值小且近实数（Fig. 2e,f caption）📜Q | 两壁等价的纯拓扑图景 | 拉伸壁额外承载常规束缚态（不穿隙） |
| **定量一致** | 拟合 s-SNOM 剖面复现实验、拟合参数随 $V_g$ 系统变化（Fig. 4 + SI Fig. S3/S4/S5；摘要 "quantitative agreement"）📜Q | 定性/唯象猜想 | s-SNOM 可作 10-nm 局域谱探针 |

> **主结果 ↔ 判别表映射**：
> - 主结果① 两种驻波图样 ← {拉伸 vs 剪切壁, 拉伸壁的常规束缚态}
> - 主结果② r 的幅值/相位差异 ← {拉伸壁的常规束缚态, 拓扑态 vs 常规态}
> - 主结果③ 定量一致 + 可提取 µ/Vi/η ← {定量一致}
> - （前提）反射来源是束缚态增强局域 σ⊥ ← {反射来源 = 束缚态}
>
> **"拓扑手征模"的作用是分层证成的**：①「反射来源 = 束缚态」先证反射来自束缚态增强的 σ⊥（非体连续）；②「拓扑态 vs 常规态」用剪切壁 $V_i$ 开隙前后对照证拓扑态单独就能产生反射峰；③「拉伸壁的常规束缚态」证拉伸壁在拓扑态之外**额外**有常规态。作者摘要用 "due to topological chiral modes" 是**初始洞见**（"topological arguments give an important initial insight"），摘要末句明说"further microscopic analysis … proves necessary" 📜Q。

> **[前提与限定]**（判别结论的适用范围）：
> - **噪声/扰动**：$V_i$ 由衬底 **uncontrolled dopants** 决定（正文），故作为拟合参数而非独立测量 📜Q；全文 µ/Vi/η/λp **无 ± 误差棒**（只有离散拟合值，[~]）；$s̄_3$ 归一化到 $y=-200$ nm（拉伸）/ $x=-150$ nm（剪切）后取相对值（Fig. 2 caption）📜Q——绝对反射率/σ⊥ 绝对值原文未给，只可引相对量与定性幅值/相位。
> - **判别性扫轴**：扫 $V_g$（密度/化学势轴，60→−80 V 拉伸、30→−110 V 剪切）；$\omega$ 固定 890 cm⁻¹ 单频（未扫频）；$V_i$ 不扫（靠衬底 dopants 被动取值）。
> - **候选集 M 边界**：{仅体连续(adiabatic), 仅拓扑态, 仅常规态, 拓扑+常规} —— "束缚态增强 σ⊥"在该集合内唯一自洽；**集外候选未排除**：其他散射源（点缺陷、褶皱、应变梯度、样品边缘、其他畴壁）对反射的贡献原文未系统排除（封闭世界风险）。

三层标注：📜Q = 原文事实（附位置）｜推导｜📊F = 读图估算｜💭I = 推断。**不确定度（正交轴）**：[±] 原文误差棒（本文**全文无 ±**）/ [~] 原文以 =/≈ 给出无误差棒 / [读图] 图提取·色标值 / [相对] 仅相对量。所有数字经 pdftotext + grep 反向核对。

---

## 2. 结果与机制（按论文论证结构：壁电子结构 → 局域 σ⊥ → 反射与拟合 → 1D 等离激元展望）

### 2.1 壁的电子结构：拓扑手征模 + 常规波导模（Fig. 1）

- **结构起点**：畴壁是部分位错线，Burgers 矢量 $|\vec b|=a/\sqrt3$（非晶格常数 $a=0.246$ nm）📜Q（正文第 1 页）。壁角 $\alpha$：拉伸壁 $\alpha=0$（沿 zigzag $x$ 方向）、剪切壁 $\alpha=\pi/2$ 📜Q。
- **壁宽**：$l=6$–10 nm，由层间堆叠相互作用能与层内弹性应变竞争决定 📜Q（正文第 1 页）；模型输入取**拉伸 $l=10.1$ nm、剪切 $l=6.2$ nm**（SI 式 S4，引 ref 3 Alden 2013）📜Q。
- **拓扑手征模**：AB/BA 堆叠的满价带 valley-Chern 数差 2 → 畴壁必须承载**每自旋每谷 ≥2 条共向 1D 通道**（"minimum of two co-propagating 1D conducting channels per spin per valley"）📜Q（正文第 2 页）。忽略谷间散射时受保护，可承载**单向谷电流**（"unidirectional valley currents"）📜Q——即 K/K′ 反向传播的 helical 态（术语辨析见 [PHY-BERRY]：摘要称 "chiral"，机制是谷锁定反向的 QVH 畴壁态）。
- **常规波导模（仅拉伸壁）**：绝热近似下壁中点 ≈ SP（鞍点）堆叠，其无隙 Dirac 点投影到 $k_\parallel$ 产生**电子波导模**；有限宽度壁的量子限制给出**有限条** 1D 分支。其中只有 1 对（每自旋每谷）穿隙 = 拓扑手征模；其余波导模继承自 SP 带结构，**不穿隙**、传播方向几乎不随 $V_i$ 变 📜Q（正文第 3 页）。**剪切壁更窄 → 限制更强 → 波导模被推到带边、实际不可见，只剩穿隙的拓扑双线** 📜Q。

### 2.2 局域 ac 电导 σ⊥ 的束缚态峰（Fig. 3）

- 用 4×4 Dirac 哈密顿 + 空间变化堆叠 $\delta(x_\perp)$（SI 式 S1–S4），$k_\perp\to-i\partial/\partial x_\perp$，Kubo 公式算非局域电导 $\Sigma(x_\perp,x'_\perp)$ 再积分局部化 $\sigma_\perp(x_\perp)\equiv\int\Sigma\,dx'_\perp$ 📜Q（正文第 4 页）。
- **对比**：lattice 法（含束缚态）的 Re σ⊥ 在拉伸壁处**远大于** adiabatic 法（无束缚态）——差别正来自束缚态 📜Q（Fig. 3a）。
- **剪切壁**：$V_i=0$ 时无束缚态 → σ⊥ 在壁处**相对平坦**；$V_i=\pm0.2$ V 开隙引入拓扑束缚态 → σ⊥ 不再平坦、Re σ⊥ 出峰；偏压符号不变 σ⊥（反号=交换谷）📜Q（Fig. 3b,c）。
- **拉伸壁**：$V_i=\pm0.1$ eV 时偏压符号改变常规束缚态的色散 → σ⊥ 显著不同 📜Q（Fig. 3d）。
- 计算参数：Fig. 3 为 $\mu=0.1$ eV、$\eta=0.1$、$\omega=890$ cm⁻¹ 📜Q；SI Fig. S1/S2 加 $T=300$ K、$V_i=0.1$ V/0，并把束缚态贡献与连续谱贡献分离 📜Q。

### 2.3 等离激元反射机制与剖面拟合（Fig. 2、4）

- **机制**：针尖发射等离激元径向传播 → 被畴壁反射 → 与入射波干涉成驻波，条纹周期 = **等离激元波长之半** 📜Q（正文第 3 页）。
- **反射系数定义**（一阶微扰）：$r=iq_\infty\int dx_\perp(\sigma_\perp(x_\perp)-\sigma_\infty)/\sigma_\infty$，正比于壁处相对背景的过量电导；壁宽 ≪ 等离激元波长 → 壁可视为 1D 散射体 📜Q（正文第 5 页）。
- **r 的壁型差异**：高 µ 时拉伸壁 $r$ **幅值大且近似虚数**、剪切壁 $r$ **幅值小且近似实数** 📜Q（Fig. 2e,f caption）→ 拉伸壁反射更强；r 的相位决定干涉图样在**拉伸壁处取极小、剪切壁处取极大** 📜Q（正文第 5 页）。
- **图样演化**：拉伸壁在 $V_g$ 接近 CNP 时仅一条几乎不可见的亮线，随 $V_g$ 降低演化为双条纹（1→2 峰）；剪切壁由单条纹演化为三条（1→3 峰）📜Q（Fig. 2a,b）；线剖面为沿壁 1 µm 长区段的平均 📜Q（Fig. 2 caption）。
- **拟合**：把 σ⊥ 转成等离激元动量 $q_p=2\pi/\lambda_p(1+i\gamma)$ 输入电磁求解器，调 µ、$V_i$、η 直到复现实验剖面；示例拉伸壁 $V_g=-80$ V、剪切壁 $V_g=-110$ V 📜Q（Fig. 4 caption）。**峰来自涉及束缚态的光学跃迁** 📜Q（Fig. 4 caption）。
- **可辨识性**：µ 增→λp 增且信号减弱；$V_i$ 变→壁处信号强度变；η 增→振荡整体幅度下降——三参数对剖面有可区分影响 → 可从拟合可靠确定 📜Q（SI Fig. S3）。

### 2.4 1D 等离激元展望（Fig. 5，正文 §"1D plasmons"）

- **障碍 = Landau 阻尼**（来自周围体连续谱）；需 $\mu$ 落在能隙内 + $\omega$ 足够小才可抑制；需顶栅（控 µ）+ 非 SiO₂ 衬底/栅介质（降无序）📜Q（正文第 6 页）。
- **1D 介电函数**（正文 Eq. (1) / SI 式 S13）：$\varepsilon_{1D}(k_\parallel,\omega)=\kappa-\frac{8e^2}{h}\ln\frac{A}{k_\parallel l}\sum_{j=1}^{N}\frac{k_\parallel^2|v_j|}{\omega^2-k_\parallel^2v_j^2}$，$N$ = 每自旋每谷 1D 态数、$v_j$ 群速度、$A\approx1$（SI 中 $A=2e^{-0.577}=1.12$）📜Q。
- **通道数 N**：剪切壁仅 $N=2$；拉伸壁 $N=2,4,6$（取决于 µ 与 $V_i$）📜Q（正文第 6 页）。等离激元群速度 $v_p\propto\sqrt N$（类比碳纳米管）📜Q。$N$ 以 2 为步长跳变 → λp 在特定 µ 处**锐变**（Fig. 5b 蓝线）📜Q。

---

## 3. 实验方法

### 3.1 器件
机械剥离石墨烯于 **285 nm SiO₂**/高掺 Si（全局背栅）上；光学衬度识别双层区；**shadow mask** 定义金属接触 📜Q（Methods）。⚠️ **单背栅、无顶栅**——只能调 $n$（与 µ），不能独立设定层间偏压 $V_i$（[PHY-GATE]）。

### 3.2 静电学
背栅 $V_g$ → 载流子密度与化学势；$\mu$ 作为拟合参数由 s-SNOM 剖面反推（非独立电容标定）。$V_i$ 由衬底 uncontrolled dopants 决定（正文第 5 页）📜Q。

### 3.3 测量
大气环境、AFM tapping 模式、红外 $\lambda=11.2$ µm、**pseudo-heterodyne** 检测提取近场散射振幅 s 与相位 φ、在 tapping 频率 **270 kHz** 的**三次谐波**解调去背景 📜Q（Methods）。观测量 = $s̄_3$（归一化）与 φ 剖面；反射系数 r 由剖面拟合提取。

---

## 4. 关键数据

### 4.1 实验参数（📜Q[~]，全文无 ±）
| 参数 | 值 | 位置 |
|------|-----|------|
| IR 波长 λ | 11.2 µm | Methods |
| 计算频率 ω | 890 cm⁻¹（≈ 11.2 µm） | Fig. 3 caption |
| 环境 | 大气、T=300 K（计算）、AFM tapping | Methods / SI Fig. S1 |
| 解调 | 三次谐波 270 kHz | Methods |
| 衬底/栅 | 285 nm SiO₂ / 高掺 Si 背栅 | Methods |

### 4.2 结构/能带参数（📜Q）
| 参数 | 值 | 位置 |
|------|-----|------|
| 晶格常数 a | 0.246 nm | 正文 |
| Burgers 矢量 \|b\| | $a/\sqrt3$ | 正文 |
| 层间耦合 γ₁ | 0.41 eV（正文）/ 0.4 eV（SI 式 S3） | 正文第 2 页 / SI |
| 壁宽 l | 6–10 nm（正文）；拉伸 10.1 nm、剪切 6.2 nm（SI 式 S4） | 正文第 1 页 / SI |
| valley-Chern 差 | 2（→ 每自旋每谷 ≥2 共向通道） | 正文第 2 页 |
| 1D 态数 N | 剪切 2；拉伸 2/4/6（随 µ、Vᵢ） | 正文第 6 页 |

### 4.3 反射系数与图样（📜Q，定性）
- r：拉伸壁幅值大、近似虚数；剪切壁幅值小、近似实数；拉伸壁反射更强 📜Q（Fig. 2e,f caption）。
- 干涉相位：拉伸壁处极小、剪切壁处极大 📜Q（正文第 5 页）。
- 图样演化：拉伸 1→2 峰、剪切 1→3 峰（$V_g$ 降低）📜Q（Fig. 2 caption）。

### 4.4 拟合参数（SI 原文表，📜Q[~]，离散值无误差棒）
| 壁 | $V_g$ (V) | $\mu$ (eV) | $V_i$ (V) | $\eta$ |
|----|-----------|-----------|-----------|--------|
| 拉伸 | 60, 0, −40, −80 | 0.17, 0.21, 0.25, 0.27 | 0.25, 0.2, −0.1, −0.2 | 0.2, 0.15, 0.1, 0.12 |
| 剪切 | 30, −20, −50, −80, −110 | 0.16, 0.21, 0.23, 0.24, 0.25 | 0.3, 0.35, 0.35, 0.35, 0.4 | 0.2, 0.2, 0.2, 0.2 |

> 来源：SI 正文（"for Vg = (60, 0, −40, −80) V are: µ = (0.17, …) eV, Vi = (…), η = (…)"）。⚠️ 这些是**拟合反推值**，非独立测量；无 ± 误差棒 [~]。

### 4.5 提取链与验证链
- **提取链**：s-SNOM 剖面 → 电磁求解器拟合 → 反推 {$\mu, V_i, \eta$} 与 {$\lambda_p,\gamma$ 剖面}；r 由 σ⊥ 剖面经一阶微扰公式算得。三参数可辨识依据 = SI Fig. S3（各参数对剖面有独立可区分影响）📜Q。
- **验证链**：① 两种壁不同图样 ↔ 电子结构差异（拉伸有/剪切无常规束缚态）；② 拟合参数随 $V_g$ 单调系统变化（µ 随 $V_g$ 降低而单调升高，拉伸/剪切两组器件一致，见 §4.4 表）；③ 拟合剖面与实验**定量一致**（摘要）📜Q。
- **未见**：无独立输运/STM 数据交叉验证 $V_i$、µ 的反推值；无反演唯一性检验。

---

## 5. 主要结论
1. AB/BA 畴壁对表面等离激元的反射源于束缚在壁上的态（拓扑手征模 + 拉伸壁常规波导模）增强局域 ac 电导 σ⊥ 📜Q。
2. 拉伸/剪切壁的电子结构差异直接导致两种驻波图样与 r 的幅值/相位差异——拉伸壁反射更强（r 大近虚数）📜Q。
3. 计算的等离激元干涉剖面与实验**定量一致**，可作为 s-SNOM 在 10-nm 尺度探局域电子特征的 proof of principle 📜Q。
4. 展望：畴壁可承载 1D 等离激元（N=2/4/6、$v_p\propto\sqrt N$），但受 Landau 阻尼限制，需顶栅 + 低无序衬底 📜Q。
5. 作者措辞强度：摘要 "due to topological chiral modes" 是初始洞见；摘要末句 "further microscopic analysis proves necessary to account quantitatively" —— 定量解释**需要**微观能带分析，拓扑论证只是起点 📜Q。

## 6. 局限与未解决
| 局限 | 说明 | 证据 |
|------|------|------|
| 单底栅 | 无顶栅 → 不能独立设 µ 与 $V_i$；$V_i$ 由衬底 uncontrolled dopants 定 | 📜Q（正文第 5 页） |
| $V_i$/µ/η 是拟合值 | 无独立测量交叉验证，无反演唯一性检验 | 📜Q（SI §3） |
| 全文无误差棒 | µ/Vi/η/λp 只给离散拟合值，r 只给幅值/相位定性 | 📜Q |
| 绝对反射率/σ⊥ 未给 | 只能引相对量与定性结论 | 📜Q（正文仅给相对剖面） |
| 单频 | 只在 ω=890 cm⁻¹ 成像，未扫频验证色散 | 📜Q（Methods/Fig. 3） |
| 未排除其他散射源 | 缺陷/褶皱/边缘/多壁散射对反射的贡献未系统排除 | 💭I |
| "拓扑"未直接证 | 反射归因拓扑态靠 $V_i$ 开隙对照（间接），非直接观测量子化/谷保护 | 💭I（[PHY-BERRY]） |

## 7. 与其他工作的关系
| 工作 | 关系 |
|------|------|
| Jiang, L. et al. 2016 (ref 9, Nat. Mater. 15, 840) | 前驱：首次 s-SNOM 见畴壁反射等离激元（"soliton-dependent plasmon reflection"），本文是其定量微观理论 + 壁型区分 📜Q |
| Zhang/Fogler 2016 (ref 24, PRL 117, 086801) | 方法前驱：bound 1D 态的 tunable plasmonic reflection，本文把非局域电导方法用到 BLG 畴壁 📜Q |
| Ju 2015 (ref 8) / Yin 2016 (ref 10) / Li, J. 2016 (ref 15) | 输运/STM 确立畴壁拓扑态——本文把"拓扑态存在"用于有限频率响应 📜Q |
| Koshino 2013 (ref 6) | 4×4 Dirac 模型 + AB-BA 畴界透射的模型来源（SI 式 S1 引 ref 1）📜Q |
| Shimazaki 2015 (ref 4 = SI ref 4) | 谷电流实验，本文 SI 计算中引为电导各向异性依据 📜Q |

> ⚠️ 本文是 **s-SNOM 光学探针**这一支，与输运支（E10/E12 AB/FP 振荡）、STM 支（E4/E9/E13/E14）互补：本文无输运、无 STM，只探测畴壁的**局域光学响应**。

## 8. 对后续研究的影响
- 提供"畴壁 = 等离激元反射体"的定量机制（局域 σ⊥ 增强）——s-SNOM 成为畴壁电子结构的非侵入探针 📜Q。
- 提出 s-SNOM 可推广到宽泛 vdW 异质结家族的电子边界 📜Q（摘要末句）。
- 提出畴壁 1D 等离激元（Luttinger 液体）研究方向，给出 N=2/4/6 与 $v_p\propto\sqrt N$ 预言 📜Q。
- 为 E1（Ju 2015 s-SNOM 成像）提供"成像→定量反射光谱"的升级路径 💭I。

## 9. 理论模型映射（供 tbplas / Kubo-Bastin 对照）
| 映射 | 说明 | 位置 |
|------|------|------|
| $\delta(x_\perp)=\frac2\pi\arctan e^{\pi x_\perp/l}+1$ | 堆叠序空间分布；l=10.1 nm（拉伸）/6.2 nm（剪切） | SI 式 S4 |
| 4×4 Dirac H | 基 $\{F A_t^K, F B_t^K, F A_b^K, F B_b^K\}$；$\gamma_1=0.4$ eV；$\delta=1,1.5,2$=AB,SP,BA | SI 式 S1–S3 |
| $\sigma_\perp(x_\perp)=\int\Sigma(x_\perp,x'_\perp)dx'_\perp$ | 非局域 Kubo → 局域电导 | 正文第 4 页 / SI 式 S7–S8 |
| $r=iq_\infty\int(\sigma_\perp-\sigma_\infty)/\sigma_\infty$ | 反射系数（一阶微扰） | 正文第 5 页 |
| $q_p=2\pi\sigma_\perp/(i\kappa\omega)=2\pi/\lambda_p(1+i\gamma)$ | 等离激元动量 ↔ 波长/阻尼 | 正文第 4–5 页 |
| $\varepsilon_{1D}(k_\parallel,\omega)$ | 1D 介电函数；$\omega^2=k_\parallel^2v_j^2$ 极点给 1D 等离激元色散 | 正文 Eq.(1) / SI 式 S13 |

> 对标：tbplas 可直接复现 Fig. 1 的壁电子结构（4×4 Dirac + 空间变化 δ）与 Fig. 3 的局域 Kubo 电导 σ⊥(x⊥)；s-SNOM 剖面还需电磁求解器（把 σ⊥→qp→干涉）。本文给的是**局域 σ⊥(x⊥) 剖面**，正是 Kubo-Bastin/局域响应能对标的对象 💭I。

---

## Phase S 目的接口（三问，引用式）

- **Q1（edge state 如何表征）**：s-SNOM 等离激元纳米成像——畴壁作为反射体，驻波条纹编码反射系数 r（幅值/相位）与壁型（拉伸 vs 剪切）；非侵入、室温大气、10-nm 尺度（§2/§4）。
- **Q2（理论如何解释）**：无新拓扑理论；用 4×4 Dirac + 空间变化堆叠 + Kubo 算局域 σ⊥，反射系数一阶微扰公式（§2.2/§2.3）📜Q。
- **Q3（理论↔实验对应）**：壁电子结构差异（拉伸有/剪切无常规束缚态）↔ 两种驻波图样与 r 差异；拟合剖面 ↔ 实验定量一致（§2.3/§4.4）📜Q。

> **增量价值**：本论文是 E1–E18 中**唯一**用 s-SNOM 把畴壁当作**等离激元反射体**定量研究的（补 E1 的成像式 s-SNOM 与 E4/E9 的 STM 谱学之外的"光学响应"维度）；report.md §2 的 s-SNOM 方法谱系用其"反射→局域 σ⊥"机制，§4 用其拉伸/剪切壁 r 差异作"畴壁电子结构可被光学区分"的证据。

## 反向核对 pass (2026-09-01)
pdftotext -layout 提取 22 页 arXiv v1（正文 1–14 页 + SI 15–22 页）→ grep 逐项核对，全部数字/专名命中：λ=11.2 µm、270 kHz 三次谐波、pseudo-heterodyne、tapping、285 nm SiO₂、shadow mask、890 cm⁻¹、100 cm⁻¹、a=0.246 nm、|b|=a/√3、γ₁=0.41 eV（正文）/0.4 eV（SI）、l=6–10 nm（正文）/10.1 nm、6.2 nm（SI S4）、N=2,4,6、quantitative agreement、10-nm scale、µ=0.1 eV、η=0.1、Vi=±0.2 V / ±0.1 eV、mostly imaginary / mostly real、one to two / one to three peaks、1 µm-long、y=−200 nm / x=−150 nm、拟合参数表（µ/Vi/η vs Vg）、A=2e^{−0.577}=1.12、Landau damping、zigzag/saddle point/waveguide modes、valley-Chern、co-propagating、unidirectional valley currents。⚠️ DOI 10.1021/acs.nanolett.7b03816 **不在 arXiv 正文中**（外部来源，已标 ⚠️）；期刊版标题复数 vs arXiv v1 单数（已标注）。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-19 | 原表述 λ~10.6 μm / 反射率 5–15% / λp 100–200 nm / 空间分辨 20 nm / "反射信号仅 D≠0 出现" / "仅探测单条畴壁" —— 原文无源或错（PDF 逐项 grep 无命中），已删；改为 11.2 µm、r 幅值/相位定性、Vg 依赖等 📜Q |
| 2026-09-01 | **4 块新架构整体重写**（对齐 E12 canonical）：新增 TL;DR 问题句式、四层变量表、可辨识性判别表（5 条）+ 主结果↔判别映射 + [前提与限定]、机制五问、§3–§9、目的接口、反向核对 pass |
| 2026-09-01 | **补 SI 内容**（旧 review 只基于正文）：arXiv v1 第 15–22 页含 SI（式 S1–S13、Fig S1–S5）——补入拟合参数表（µ/Vi/η vs Vg）、壁宽 l=10.1/6.2 nm（SI S4）、γ₁=0.4 eV（SI S3）、ε₁D 公式、A=1.12、三参数可辨识性（Fig S3）|
| 2026-09-01 | **措辞强度校正**：摘要 "due to topological chiral modes" 是初始洞见，摘要末句明说微观分析 necessary——TL;DR/§5/判别表补"分层证成"注与作者措辞强度 📜Q |
| 2026-09-01 | **DOI 标 ⚠️**：10.1021/acs.nanolett.7b03816 为外部来源（Semantic Scholar 按 arXiv 反查），arXiv 正文未出现；期刊版标题复数 "reflections" vs arXiv v1 单数 "reflection" 已标注 |
