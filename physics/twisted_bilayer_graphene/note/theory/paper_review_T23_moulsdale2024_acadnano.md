<!--
 * @Author       : AI 精读（白箱演绎结构）
 * @Date         : 2026-08-11（初读）→ 2026-09-02（4 块辨识结构，理论版）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T23_moulsdale2024_acadnano.md
 * @Description  : T23: Moulsdale, Enaldiev, Geim & Fal'ko 2024 Academia Nano — AB/BA 畴壁内非手征 1D 态（2026-09-08 按 5 块演绎结构重写：模型白箱/推导链/结论清单/假设-结论依赖图/接口）
-->

# Paper Review: Moulsdale et al. (2024) — AB/BA 畴壁内非手征 1D 态

| 字段 | 内容 |
|------|------|
| **编号** | T23 |
| **标题** | Non-chiral one-dimensional states inside AB/BA domain walls in bilayer graphene |
| **作者** | Christian Moulsdale, Vladimir V. Enaldiev, Andre K. Geim, Vladimir I. Fal'ko（⚠️ 第一作者 Moulsdale，非 Enaldiev） |
| **期刊** | Academia Nano: Science, Materials, Technology 2024;1（Received 2024-05-02 / Published 2024-07-24）📜Q |
| **DOI / arXiv** | 10.20935/AcadNano7267 / arXiv:2307.14293（⚠️ arXiv 号正文未出现，外部来源） |
| **类型** | 理论 — 畴壁非手征 1D 态（数值能带计算） |
| **课题组** | National Graphene Institute / University of Manchester（Geim & Fal'ko 组） |
| **PDF** | ✅ `reference/pdfs/Moulsdale 等 - 2024 - Non-chiral one-dimensional states inside ABBA domain walls in bilayer graphene.pdf`（8 页，无 SI） |
| **精读日期** | 2026-08-11（初读）→ 2026-09-02（4 块辨识结构）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」的五块记（见 `note/shared/method/theory_paper_reading.md` §3）：**① 模型白箱 → ② 推导链 → ③ 结论清单（分层）→ ④ 假设-结论依赖图 → ⑤ 接口**。理论论文无黑箱、无反推、无可辨识实验（是"白箱演绎"而非"黑箱溯因"），故不用"四层变量表 + 判别表"这套实验框架词汇（旧 4 块版已废弃）。
> **共享知识引用**：谷 Chern / 手征 vs 非手征拓扑畴壁态用锚点 `[PHY-BERRY]`；1D 通道计数 / 弹道输运 / 量子线用 `[PHY-LB]`。本文只写"本文代入"的数字，通用推导不复制。阅读疑问见 `note/shared/method/mechanism_questions.md` `[METHOD-Q]`。

---

## TL;DR

**本文想解决的问题**：AB/BA 畴壁的电子结构是否只有"谷锁定手征拓扑态"一种局域态？畴壁在低能能否还承载**非手征** 1D 态？

**主结果**：① 取决于畴壁宽度 w，AB/BA 边界**可以**承载非手征 1D 态——低能束缚于畴壁、高能（1D 带进入二维体连续谱处）变为准束缚态 📜Q（摘要）；② 非手征性来自 Δ=0 时 $\hat S=\tau_x\sigma_x$ 对称性（式 3）给出的 $\varepsilon(p_y)=\varepsilon(-p_y)$，即在每个谷内都存在反向传播模式 📜Q（§3）；③ 在有限磁场下，准束缚态经与朗道能级（LL）的杂化以"kink"（LL 色散的尖锐弯折）显现，且 kink 位置在 B=1 T 与 B=3 T 下对应同一 $\varepsilon(k_y)$（不随 B 缩放）——以此与 skipping 回旋轨道区分 📜Q（§4）。

**结论/意义**：畴壁的完整电子结构 = 手征（拓扑，来自谷 Chern ±2）+ 非手征（来自 $\hat S$ 对称性）两部分；非手征态有有限背散射长度但高质量样品低温下可弹道输运，通道数由费米能级调节 📜Q。作者用词 "we show / we notice / we expect"（展示/注意到/预期），非"已证实"。

---

## 1. 模型白箱（理想系统 + 假设清单）

> 理论论文的研究对象是**白箱**——作者自写的理想模型，无需"反推内部"。本节只做两件事：**写下模型**（§1.1），**列出它成立的全部假设**（§1.3）。假设清单是本文一切结论的"前提集合"，§4 的依赖图据此展开。

### 1.1 模型：FKM 位移场 + SWM 4×4 哈密顿量

**晶格（Frenkel-Kontorova 模型）**：单条 AB/BA 畴壁用 FKM 描述为**部分螺位错**（partial screw dislocation），Burgers 矢量 $b=(0,a/\sqrt3)$ 沿臂椅方向，设边界条件于层间位移场 $u=(0,u_y(x))$（把 AB 连续变换到 BA 堆垛）📜Q（§2，Fig. 1）。位移场解（式 1）：$u_y(x)=\frac{2a}{\sqrt3\pi}\arctan e^{2x/w}$，畴壁全宽 $w=(a/\pi)\sqrt{\mu/6V}$ 📜Q。层间侧向偏移矢量 $r_0(x)=(0,a/\sqrt3+u_y(x))$ 📜Q。

**电子（SWM 型 4×4 哈密顿量，式 2）**：谷 $\xi=\pm$、层+子晶格基 $\Psi=(\psi_{At},\psi_{Bt},\psi_{Ab},\psi_{Bb})^T$：

$$H_\xi(r_0)=\begin{pmatrix} v\sigma_\xi p+\frac{\Delta}{2} & T_\xi(r_0)\\ T_\xi^\dagger(r_0) & v\sigma_\xi p-\frac{\Delta}{2} \end{pmatrix}+\begin{pmatrix} E_0(r_0)+E_1(r_0)\sigma_z & 0\\ 0 & E_0(r_0)-E_1(r_0)\sigma_z \end{pmatrix}$$

含谷依赖的 $T_\xi(r_0)$ 隧穿矩阵（$\gamma_1$、$v_3$、$v_4$ 项）与位置依赖对角项 $E_0(r_0)+E_1(r_0)\sigma_z$（$\Delta'$）📜Q（§3）。$\Delta$ = 层间不对称势（interlayer potential difference）；$E_{0,1}$ 计入二聚化/非二聚化子晶格能量差 $\Delta'\approx22$ meV（破缺 e-h 对称）📜Q。

**变量含义表**：

| 符号 | 含义 | 值/定义 |
|---|---|---|
| $w$ | 畴壁全宽（唯象参数） | $(a/\pi)\sqrt{\mu/6V}$，标称 ≈6 nm |
| $\Delta$ | 层间不对称势（**非**畴壁势阱深度） | 0–20 meV |
| $B$ | 面外磁场 | 0/1/3 T |
| $k_y,\varepsilon$ | 沿畴壁波矢 / 能量 | 旋钮 |
| $\gamma_1$ | 层间 hopping | ≈380 meV |
| $v,v_3,v_4$ | 费米速度 / trigonal warping 项 | $v\approx10^6$ m/s、$v_3\approx0.123v$、$v_4\approx0.045v$ |
| $\Delta'$ | 二聚化/非二聚化子晶格能量差 | ≈22 meV |
| $\delta$ | 非手征谱 minigap | 依赖 $w,\Delta$ |

### 1.2 参数分册（替代旧"四层变量表"：区分"作者设定" vs "推导所得"）

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | $w$（畴壁宽度，唯象）、$\Delta$（层间不对称势 0–20 meV）、$B$（磁场 0/1/3 T）、$k_y$、$\varepsilon$ |
| **导出量（由旋钮+常数算出）** | $u_y(x)$（式 1）、$r_0(x)=(0,a/\sqrt3+u_y)$、minigap $\delta$ |
| **模型内部量（解的性质）** | 4×4 哈密顿量 $H_\xi(r_0)$（式 2）、非手征 1D 带色散 $\varepsilon(k_y)$、费米波矢 $k_F(n)$、LL 谱 |
| **固定常数** | $v\approx10^6$ m/s、$\gamma_1\approx380$ meV、$v_3\approx0.123v$、$v_4\approx0.045v$、$\Delta'\approx22$ meV、$a=0.246$ nm、$\mu=920$ eV/nm²、$V=0.0296$ eV/nm² |
| **预言量（可检验）** | LDOS/空间分布、$k_F(n)$ 正负不对称、$\delta(\Delta)$、LL kink |

> 无"反推量 θ̂"层——理论论文不反推自数据（$w$ 从 $a,\mu,V$ 代入式 1 得 ≈6 nm，是导出量非反推）。**符号防混**：$\Delta$（层间不对称势）≠ 畴壁势阱深度；$\Delta'$（二聚化/非二聚化子晶格能量差 ≈22 meV）≠ $\Delta$。

### 1.3 显式假设清单（本文结论的前提集合）

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **$w$ 唯象参数**（"no commonly established value for the DW width"，覆盖 6–14 nm） | 模型 | 📜Q |
| A2 | **单条、直臂椅取向、孤立畴壁**（FKM 部分螺位错） | 模型 | 📜Q |
| A3 | **SWM 型哈密顿量 + FKM 位移场**（单粒子、无相互作用） | 模型 | 📜Q |
| A4 | **纯数值能带计算**：无温度、无序、退相干建模 | 模型 | 📜Q（无序仅定性） |
| A5 | **磁场经 Peierls 替换进入**（Landau 规范 + 磁振子基展开） | 推导 | 📜Q |
| A6 | **能量窗 $-100\le\varepsilon\le100$ meV**（基尺寸 N 取到收敛） | 推导 | 📜Q |

> 判别性扫轴：$w=7,10,14$ nm × $\Delta=0,2,10,20$ meV（Fig. 2）× $B=0,1,3$ T × $\varepsilon\in[-100,100]$ meV。这些假设在 §4 逐一映射到"失效 → 结论崩塌"。

---

## 2. 推导链（演绎结构：顺论文顺序，每步"输入→输出→所用假设/定理→合法域"）

### 2.0 总览：论文是一条演绎链

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 前提定理层 | 引言 | 谷 Chern ±2 手征态（已知）+ 额外局域态动机 | 问题设定：畴壁能否承载非手征态 | refs 18,32,33 | — |
| 模型层 | FKM + 4×4 哈密顿量 | 位移场 + SWM 参数 | 能谱（两类态：散射连续谱 + DW 局域态） | A1–A3 | 单畴壁 |
| 推导层 | $\hat S$ 对称性 + $\Delta\neq0$ | 哈密顿量对称性 | 非手征性判据 + 手征态 + minigap | $\hat S=\tau_x\sigma_x$ | $\Delta=0$ |
| 边界层 | 磁场 LL 杂化 | LL 谱 + kink 追踪 | 准束缚态追踪 + B 无关性判别 | A5 | B=1/3 T |
| 应用层 | 讨论 | 非手征态输运含义 | 背散射/弹道/通道数/e-h 破缺 | — | — |

### 2.1 前提定理层（引言）：谷 Chern ±2 手征态 + 额外局域态动机

- **已知物理**：Bernal 堆叠面外电场开 interlayer-asymmetry 能隙；gapped BLG = "weak topological insulator"，谷 Chern 数 ±2 [18]，表现为 gap inversion line 周围的手征谷极化无隙模 [2,4,6] 📜Q。这些 partial dislocations 承载能隙内谷极化手征模 [18,26,27]；传播方向由谷指标定（反向谷反向）📜Q。
- **动机**：除手征态外，畴壁内还可能有其他局域态——delamination（两分离单层区间）[32] 或大扩展 crossover 区 [33] 暗示此类态丰富；这些额外态在每个谷内双向传播、可背散射，**质变整个 DW 网络性质** 📜Q（引言）。

### 2.2 模型层：FKM 位移场 → SWM 哈密顿量 → 能谱

- **FKM 位移场**（式 1）：$u_y(x)=\frac{2a}{\sqrt3\pi}\arctan e^{2x/w}$，$w=(a/\pi)\sqrt{\mu/6V}$；代入 $a=0.246$ nm、$\mu=920$ eV/nm²、$V=0.0296$ eV/nm² 得 $w\approx6$ nm 📜Q[~]。**w 无公认值**，覆盖 6–14 nm 作唯象参数 📜Q。
- **SWM 哈密顿量**（式 2）数值对角化，输出两类态：散布于 AB/BA 畴的散射态连续谱（灰色区）+ 能量在连续谱之外的 DW 局域态 📜Q（§3）。$\Delta=0$ 时谱仍被 $E_0$、$v_{3,4}$ 项破缺 e-h 对称，但谷简并保持 📜Q。

### 2.3 推导层：$\hat S$ 对称性 → 非手征性；$\Delta\neq0$ → 手征态 + minigap

- **非手征性判据**：$\Delta=0$ 时 $ŜH_\xi(p_x,p_y)Ŝ^+=H_\xi(p_x,-p_y)$，$\hat S=\tau_x\sigma_x$（式 3，$\tau_x$ 为层空间泡利矩阵）→ $\varepsilon(p_y)=\varepsilon(-p_y)$ 在两谷都成立 → 局域态在每个谷内支持**反向传播模式**，故为**非手征** 📜Q（§3）。
- **$\Delta\neq0$ 生成手征态**：层间不对称势 $\Delta$ 破缺双层反演对称，在能隙内生成**谷极化手征态对**（谷 Chern ±2 拓扑态）📜Q；同时改变非手征 1D 带色散——**手征与非手征带 merge 并 reconnect 色散线**，在更宽畴壁中发生在更高 $\Delta$；随 $\Delta$ 增大或 $w$ 减小，重连带边缘被推向体 BLG 的 $\pm\Delta/2$ 带边，从中间 $\Delta$ 的"重叠带"区过渡到高 $\Delta$ 的"gapful"对 📜Q（Fig. 2）。
- **minigap $\delta$**：取决于 $w$ 与 $\Delta$，非手征态谱可保持无能隙、或获得 minigap $\delta$ 📜Q（§5）；$\delta$ 随 $\Delta$ 画在 Fig. 5b（$\Delta$ 由面外位移场调控，ref 41），数值为图读值、正文未给 📜Q[读图]。

### 2.4 边界层：磁场 LL 杂化 → kink 追踪（B 无关性判别）

- **准束缚态**：1D 带进入体连续谱 → 畴壁局域态因衰变到 AB/BA 散射态而变 quasistationary 📜Q（§4）。
- **追踪方法**：面外磁场把 2D 连续谱离散成 LL 集 → 1D 带被稳定在体 LL 之间 → 与 LL 态**微扰杂化**，形成沿畴壁传播的态，表现为 LL 色散的尖锐弯折（kink）📜Q（§4）。Peierls 替换 $p\to(-i\hbar\partial_x,-i\hbar\partial_y-eBx)$ + Landau 规范磁振子基（式 4，$z=x/\lambda_B-k_y\lambda_B$）数值对角化 📜Q。
- **B 无关性判别**：沿最大漂移速度态追踪的 kink，在 B=1 T 与 B=3 T 下对应**同一** $\varepsilon(k_y)$（不随 B 缩放），而更高能色散特征随 B 缩放 → 后者归为畴内 skipping 回旋轨道 📜Q（Fig. 3/4）。旁证：此类 1D 态已在 AB/BA 畴壁 + 超导引线的量子输运中观测到（邻近效应维持到 5 T，ref 22 = Barrier 2024）📜Q（§4）。

### 2.5 应用层：实验含义（背散射 / 弹道 / 通道数 / e-h 破缺）

- **无序敏感性对比**：拓扑态在能隙内形成、对两谷长程无序背散射受保护；而 1D 非手征态有**有限背散射长度** 📜Q（§3）。但最优异质结 [23] 低温（$T\to0$）下散射长度可超器件尺寸，实现**弹道输运**，1D 通道总数由费米能级调节 📜Q。
- **量子线图景**：有限长度畴壁段上，高能 1D 态"could act as"（可充当）与 2D 体**并联**的 1D 量子线 📜Q（§5）。
- **e-h 对称破缺**：真实系统（$v_{3,4}>0$，与 ref 39 一致）破缺 DW 态 e-h 对称，$k_F(n)$ 正负体载流子密度不对称（Fig. 5a）；**预期**（"we expect"）最小模型 [40] 的 e-h 对称谱在真实系统中被打破 📜Q（§5）。

---

## 3. 结论清单（分层：定理 / 估算 / 预言）

> 理论论文的结论必须按**性质**分层，而非平铺。每条标：**依赖假设** + **可检验性**。

### 3.1 定理式主张（数学/对称性论证的产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 非手征性判据 | $\Delta=0$ 时 $\hat S=\tau_x\sigma_x$ 对称性 → $\varepsilon(p_y)=\varepsilon(-p_y)$ 两谷成立 → 反向传播模式 | A2、A3 |
| 手征态生成 | $\Delta\neq0$ 破缺双层反演对称 → 能隙内谷极化手征态对（谷 Chern ±2） | A3 |

### 3.2 估算（数值算例，非严格定理）

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| 畴壁宽标称 | $w\approx6$ nm（$a=0.246$ nm、$\mu=920$、$V=0.0296$） | 式 (1) | 📜Q[~] |
| $w$ 文献范围 | $6<w<14$ nm；计算取 7/10/14 nm | — | 📜Q[~] |
| $\Delta$ 取值 | 0/2/10/20 meV（Fig. 2） | — | 📜Q |
| SWM 参数 | $\gamma_1\approx380$ meV、$v_3\approx0.123v$、$v_4\approx0.045v$、$\Delta'\approx22$ meV | — | 📜Q[~] |
| 能量窗 | $-100\le\varepsilon\le100$ meV | A6 | 📜Q |
| 邻近效应上限 | 5 T（ref 22） | — | 📜Q[~]（外部） |

### 3.3 预言（可检验性 → 见 §5.1）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| 畴壁承载非手征 1D 态（低能束缚、高能准束缚） | "we show"（计算展示）📜Q | 中——LDOS/输运 |
| 非手征态低温可弹道输运 | "can exceed ... realizing ballistic transport regime" 📜Q | 中——输运 |
| e-h 对称破缺（$k_F(n)$ 不对称） | "we expect" 📜Q | 中——Fig. 5a |
| 畴壁段可充当 1D 量子线 | "could act as" 📜Q | 弱——定性 |

### 3.4 内部验证（自洽核对，非"排除竞争解释"）

1. **B 无关性互验**：B=1 T 与 B=3 T 的 kink 对应同一 $\varepsilon(k_y)$ → 独立确证 kink 来自非手征 1D 态而非 skipping 轨道 📜Q（§4）。
2. **实验佐证**：与 Barrier 2024（ref 22）超导邻近效应观测（到 5 T）互为佐证 📜Q（§4）。

### 3.5 概念区分（作者论证中的"分类"，非溯因排除）

| 区分 | 依据 | 结论 |
|---|---|---|
| 手征 vs 非手征 | 手征 = 谷锁定单向传播（谷 Chern ±2）；非手征 = $\hat S$ 对称性 → 谷内双向传播 📜Q | 畴壁电子结构双组分 |
| 束缚态 vs 准束缚态 | 低能能量在体连续谱外（局域）vs 高能穿入连续谱（衰变、quasistationary）📜Q | 连续过渡 |
| LL kink vs skipping 轨道 | kink 位置 B 无关 vs skipping 位置随 B 缩放 📜Q | 非手征态 vs 畴内回旋轨道 |

> 注：这些是**概念/图景分类**（taxonomy），不是实验论文那种"数据排除竞争解释"（溯因排除）——理论论文没有后者。

---

## 4. 假设-结论依赖图（含金量所在）

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性（作者如何对待） |
|---|---|---|---|
| A1 $w$ 唯象 | $w$ 取值不确定（6–14 nm） | 非手征态**存在性高度敏感于 $w$** | 致命缺口——作者明言 "highly sensitive to the DW width" 📜Q |
| A2 单条直臂椅畴壁 | 畴壁弯曲/网络/其他取向 | 色散定量 | 未处理（模型边界）💭I |
| A3 单粒子 SWM | 相互作用/多畴壁耦合 | 非手征态图像 | 未处理 💭I |
| A4 纯数值无温度无序 | 有限温/无序 | 输运定量、背散射长度 | 无序仅定性（"残余无序散射"）📜Q |
| $\Delta'$、$v_{3,4}$ 项 | 最小模型（$v_3=v_4=0,\Delta'=0$） | e-h 对称（真实系统破缺） | 作者显式声明真实系统 e-h 破缺 📜Q |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（本文预言的实验靶标）

- $k_F(n)$ 正负不对称（e-h 破缺，Fig. 5a）、$\delta(\Delta)$ 线性依赖（Fig. 5b）、LL 谱中 B 无关 kink（Fig. 3/4）📜Q；
- 与 Barrier 2024（ref 22）超导邻近效应到 5 T 的 1D 态观测对应 📜Q。

### 5.2 设计原则（非手征态出现条件）

取决于 $w$（畴壁宽度）与 $\Delta$（层间不对称势）——$w$ 越大非手征态越易出现；$\Delta$ 调控 minigap $\delta$（面外位移场，ref 41）📜Q。

### 5.3 后续文献修正（时间倒挂，💭I）

- **Barrier 2024 Nature（ref 22）**：实验佐证（1D 态超导邻近效应到 5 T）。
- 非手征态与手征态的**输运区分**需有限温度定量模型（本文未展开）。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| w 无公认值 | w 作唯象参数扫 6–14 nm；原文明言无公认值 | 📜Q（§2） |
| 纯数值、无温度/无序建模 | 无序仅定性（"残余无序散射"）；热展宽未建模 | 📜Q（§5）+ 💭I |
| minigap δ、k_F 无数值表 | 仅 Fig. 5 读图，正文未给具体值 | 📜Q [读图] |
| 模型结构受限 | 单条直臂椅畴壁、SWM 哈密顿量、无相互作用 | 💭I（模型边界） |
| 手征/非手征带耦合强度未量化 | 原文只描述 merge/reconnect 现象，未给耦合强度 | 💭I |
| 非手征态 vs 手征态输运区分 | 需有限温度定量模型（原文未展开） | 💭I |

---

## 7. 与其他工作的关系（跨论文对标放这里，不放正文）

| 工作 | 关系 |
|------|------|
| Zhang, MacDonald & Mele 2013 (ref 18) | 谷 Chern ±2、gapped BLG 手征边界模的理论基础 📜Q |
| Martin, Blanter & Morpurgo 2008 (ref 2) / Ju 2015 (ref 26) / Li 2016 (ref 6) | 拓扑受限 / 谷输运 / 栅控拓扑通道 📜Q |
| Barrier 2024 Nature (ref 22) | 实验佐证：AB/BA 畴壁 1D 态的超导邻近效应到 5 T 📜Q |
| Lane 2018 (ref 32, delamination) / Theil 2022 (ref 33, Volkov-Pankratov) | 先例：畴壁/界面内的额外局域态（非手征态存在的动机）📜Q |
| Alden 2013 (ref 23) | w 范围 6–14 nm 与"最优异质结"无序来源 📜Q |

> ⚠️ Phase S 外部对标（非本文引用）：旧 review 曾写"解释 Zheng 2022 (E14) STM 额外 LDOS 峰"——**原文引用列表无 Zheng 2022**（grep "Zheng" 无命中），此为 review 层综合，降级 💭I，已移出正文（见更正日志）。

---

## 8. 对后续研究的影响

- 把"畴壁电子结构"从纯手征拓扑图景补全为**手征（拓扑）+ 非手征（约束）双组分**——对解读畴壁 LDOS/输运有警示意义 📜Q。
- 给出可实验检验的预言：$k_F(n)$ 正负不对称（e-h 破缺）、$\delta(\Delta)$ 线性依赖、LL 谱中 B 无关 kink 📜Q（Fig. 5、§4）。
- 提示畴壁段可充当与 2D 体并联的 1D 量子线（作者 "could act as"）📜Q（§5）。

---

## 9. 理论模型映射（供 TBPM / Kubo 计算对标）

| 映射 | 说明 |
|------|------|
| $w\to$ 输入参数 | 畴壁宽度，扫 6–14 nm（计算取 7/10/14 nm）📜Q |
| $\Delta\to$ 层间不对称势 | 0–20 meV，对应面外位移场（ref 41）📜Q |
| SWM 参数 | $\gamma_1\approx380$ meV、$v_3\approx0.123v$、$v_4\approx0.045v$、$\Delta'\approx22$ meV、$v\approx10^6$ m/s 📜Q |
| $B\to$ Peierls 替换 | Landau 规范磁振子基展开（式 4）📜Q |
| 输出 ↔ 可算量 | 1D 带色散 $\varepsilon(k_y)$、minigap $\delta(\Delta)$、$k_F(n)$、LL 谱 kink ↔ LDOS 峰 / 电导通道 📜Q |

> 与 TBPM/Kubo 对应：本文是单畴壁连续模型能带计算；TBPM 复现需构造 AB/BA 畴壁（FKM 位移场）的紧束缚模型，核对畴壁局域 1D 带的 $\varepsilon(k_y)$ 与 LL kink 是否复现非手征态特征 💭I。

---

## Phase S 目的接口（三问引用式）

- **Q1（edge state 如何表征）**：本文明确定性表征——非手征 1D 态经 $\hat S$ 对称性（反向传播模式）定义，空间上局域于畴壁（Fig. 3 最大漂移速度态）；手征态经谷锁定单向传播定义。详见 §2.3。
- **Q2（理论如何复现）**：SWM 型 4×4 哈密顿量 + FKM 位移场（§1.1），输出 $\varepsilon(k_y)/\delta/k_F$/LL kink；非手征态的存在是计算预言，需实验核对 📜Q。
- **Q3（理论↔实验对应）**：对应 Barrier 2024（ref 22）超导邻近效应到 5 T 的 1D 态观测；可检验预言 = Fig. 5a $k_F(n)$ 不对称 + Fig. 5b $\delta(\Delta)$ + LL kink 📜Q。

> **增量价值**：补充纯拓扑畴壁图景——畴壁完整电子结构含非手征（约束）+ 手征（拓扑）两部分；非手征态对无序无拓扑保护但低温可弹道。report 侧可用其"手征 vs 非手征"判别（$\hat S$ 对称性判据）与 Fig. 5 可检验预言；⚠️ 不可引用旧 review 的"势阱深 10–20 meV"（无源）。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` 提取正文到 `/tmp/T23.txt`（511 行），逐项 grep 核对：**全部数字/专名命中原文**——

| 数字/专名 | grep 命中位置 | 结论 |
|------|--------------|------|
| $a=0.246$ nm、$\mu=920$ eV/nm²、$V=0.0296$ eV/nm²、$w\approx6$ nm | §2 脚注 1 | ✓ 📜Q[~] |
| $6<w<14$ nm、7/10/14 nm | §2 / Fig. 2 caption | ✓ 📜Q |
| $\Delta=0,2,10,20$ meV | Fig. 2 caption | ✓ 📜Q |
| $\gamma_1\approx380$ meV、$v_3\approx0.123v$、$v_4\approx0.045v$、$\Delta'\approx22$ meV、$v\approx10^6$ m/s | §3 | ✓ 📜Q[~] |
| $u_y(x)=\frac{2a}{\sqrt3\pi}\arctan e^{2x/w}$、$w=(a/\pi)\sqrt{\mu/6V}$ | §2 式 (1) | ✓ 📜Q |
| $ŜH_\xi(p_x,p_y)Ŝ^+=H_\xi(p_x,-p_y)$、$Ŝ=\tau_x\sigma_x$ | §3 式 (3) | ✓ 📜Q |
| $\varepsilon(p_y)=\varepsilon(-p_y)$、counter-propagating、non-chiral | §3 | ✓ 📜Q |
| B=1/3 T、±100 meV、5 T | Fig. 3/4 caption / §4 | ✓ 📜Q |
| 谷 Chern ±2 | 引言 | ✓ 📜Q |
| "could act as a 1D quantum wire"、"we expect ... electron-hole symmetry ... broken" | §5 | ✓ 📜Q |
| Peierls $p\to(-i\hbar\partial_x,-i\hbar\partial_y-eBx)$、$z=x/\lambda_B-k_y\lambda_B$ | §4 式 (4) | ✓ 📜Q |

⚠️ 修正/降级：① arXiv:2307.14293 正文未出现 → 头部表已标"外部来源"。② grep "Zheng" 无命中 → "解释 E14" 降级 💭I 移出正文。③ grep "V_DW/scalar potential/potential well/electrostatic" 均无命中 → 旧 review 的"势阱深 10–20 meV""静电束缚"降级，改为原文措辞（FKM 位移场 + $\Delta$ 取值 + $\hat S$ 对称性）。④ 旧 review "栅压切换开/关"无源 → 原文为"通道数由费米能级调节 + minigap δ 由位移场调控"。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-11 | 初读（research_onboarding Phase 4 风格），标题误写 "Enaldiev, Moulsdale... (2023)" |
| 2026-08-19 | 修正①：旧版 "V_DW 势阱深 10–20 meV" 无源——原文 10/20 meV 是层间不对称势 Δ 的取值系列 Δ=0,2,10,20 meV，非势阱深度（appendix_B #6） |
| 2026-08-19 | 修正②：旧版 "解释 Zheng 2022 (E14) STM 额外 LDOS 峰" 无源——原文引用列表无 Zheng 2022（grep "Zheng" 无命中），降级 💭I（appendix_B #18） |
| 2026-09-02 | **4 块新架构整体重写**：按 spec 输出结构；补四层变量表、理论版判别表、[前提与限定]、主结果↔判别映射 |
| 2026-09-02 | 修正③：作者顺序（Moulsdale 第一作者）、年份 2024、期刊 Academia Nano 2024;1、DOI 10.20935/AcadNano7267；arXiv 2307.14293 标外部来源 |
| 2026-09-02 | 修正④：grep 核实旧 review 无源表述——"标量势 V_DW(x) 势阱""静电束缚""双线 vs 单峰空间分布"均原文无命中 → 降级 💭I 并按原文措辞改写（FKM 位移场 + E0,1(r0) + Ŝ 对称性）；"栅压切换开/关"改为原文"通道数由费米能级调节 + minigap δ 由位移场调控" |
| 2026-09-08 | **按 5 块演绎结构整体重写**（应用户要求）。旧 4 块版归档 `archive/paper_review_T23_moulsdale2024_acadnano.backup_20260908.md`。黑箱三要素/四层变量表/判别表/[前提与限定] → 拆为"模型白箱（FKM+SWM 哈密顿量+参数分册+6 条假设清单）"+"推导链（前提定理/模型/推导/边界/应用五层）"+"结论清单（定理/估算/预言分层）"+"假设-结论依赖图"+"接口"；内部验证（§3.4）+ 概念区分（§3.5）取代判别表；删"反推量 θ̂"层（w 归入导出量）。全部 📜Q 事实与数字无丢失。 |
