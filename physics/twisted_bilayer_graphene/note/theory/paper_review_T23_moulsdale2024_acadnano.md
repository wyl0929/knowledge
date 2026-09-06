<!--
 * @Author       : AI 精读 (系统辨识式阅读法 → 三层分离整理)
 * @Date         : 2026-08-11（初读）→ 2026-09-02（按 4 块新架构重读）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T23_moulsdale2024_acadnano.md
 * @Description  : T23: Moulsdale, Enaldiev, Geim & Fal'ko (2024) — AB/BA 畴壁内非手征 1D 态（4 块辨识结构理论版）
-->

# Paper Review: Moulsdale et al. (2024) — AB/BA 畴壁内非手征 1D 态

| 字段 | 内容 |
|------|------|
| **编号** | T23 |
| **标题** | Non-chiral one-dimensional states inside AB/BA domain walls in bilayer graphene |
| **作者** | C. Moulsdale, V.V. Enaldiev, A.K. Geim, V.I. Fal'ko（⚠️ 第一作者 Moulsdale，非 Enaldiev） |
| **期刊** | Academia Nano: Science, Materials, Technology 1 (2024) |
| **DOI / arXiv** | 10.20935/AcadNano7267 / 2307.14293（⚠️ arXiv 号正文未出现，外部来源） |
| **类型** | 理论 — 畴壁非手征 1D 态（数值能带计算） |
| **课题组** | Geim & Fal'ko group, National Graphene Institute / University of Manchester |
| **PDF** | ✅ reference/pdfs/Moulsdale 等 - 2024 - Non-chiral one-dimensional states inside ABBA domain walls in bilayer graphene.pdf |
| **精读日期** | 2026-08-11（初读）→ 2026-09-02（4 块新架构重读） |

> **共享知识引用**：谷 Chern / 手征 vs 非手征拓扑畴壁态用锚点 `[PHY-BERRY]`；1D 通道计数 / 弹道输运 / 量子线用 `[PHY-LB]`。本文只写"本文代入"的数字，通用推导不复制。阅读疑问见 `note/shared/method/mechanism_questions.md` `[METHOD-Q]`。

---

## TL;DR

**本文想解决的问题**：AB/BA 畴壁的电子结构是否只有"谷锁定手征拓扑态"一种局域态？畴壁在低能能否还承载**非手征** 1D 态？

**主结果**：① 取决于畴壁宽度 w，AB/BA 边界**可以**承载非手征 1D 态——低能束缚于畴壁、高能（1D 带进入二维体连续谱处）变为准束缚态 📜Q（摘要）；② 非手征性来自 Δ=0 时 Ŝ=τ_xσ_x 对称性（式 3）给出的 ε(p_y)=ε(−p_y)，即在每个谷内都存在反向传播模式 📜Q（§3）；③ 在有限磁场下，准束缚态经与朗道能级（LL）的杂化以"kink"（LL 色散的尖锐弯折）显现，且 kink 位置在 B=1 T 与 B=3 T 下对应同一 ε(k_y)（不随 B 缩放）——以此与 skipping 回旋轨道区分 📜Q（§4）。

**结论/意义**：畴壁的完整电子结构 = 手征（拓扑，来自谷 Chern ±2）+ 非手征（来自 Ŝ 对称性）两部分；非手征态有有限背散射长度但高质量样品低温下可弹道输运，通道数由费米能级调节 📜Q。作者用词 "we show / we notice / we expect"（展示/注意到/预期），非"已证实"。

---

## 1. 系统辨识导览（判别表为全文唯一权威）

**黑箱三要素**：`{输入旋钮：畴壁宽度 w、层间不对称势 Δ、磁场 B、波矢 k_y/能量 ε | 输出观测量：1D 带色散 ε(k_y)、minigap δ、费米波矢 k_F(n)、LL 谱 kink | 声称结论：畴壁承载非手征 1D 态，与手征拓扑态并存}`

**四层变量表**（符号层一次钉死）：

| 层 | 本文实例 |
|----|----------|
| **L1 旋钮 u** | 畴壁宽度 $w$（唯象参数）、层间不对称势 $\Delta$（0–20 meV）、磁场 $B$（0/1/3 T）、波矢 $k_y$、能量 $\varepsilon$ |
| **L2 导出量 x₁** | 位移场 $u_y(x)$（式 1）、层间侧向偏移矢量 $r_0(x)=(0,a/\sqrt3+u_y)$、minigap $\delta$ |
| **L3 模型量 x₂** | 4×4 哈密顿量 $H_\xi(r_0)$（式 2）、非手征 1D 带色散 $\varepsilon(k_y)$、费米波矢 $k_F(n)$、LL 谱 |
| **固定参数（非旋钮）** | $v\approx10^6$ m/s、$\gamma_1\approx380$ meV、$v_3\approx0.123v$、$v_4\approx0.045v$、$\Delta'\approx22$ meV、晶格常数 $a=0.246$ nm（SWM 型参数） |
| **反推量 θ̂** | $w$（从 $a,\mu,V$ 代入式 1 得 $w\approx6$ nm；文献范围 6–14 nm） |
| **L4 观测量 y（可检验预言）** | LDOS/空间分布（Fig. 3 态局域在畴壁）、$k_F(n)$ 正负不对称（Fig. 5a）、$\delta(\Delta)$（Fig. 5b）、LL kink |

> 符号注意：本文 $\Delta$ = 层间不对称势（interlayer potential difference / interlayer-asymmetry gap），**不是**畴壁势阱深度；$\Delta'$ = 二聚化/非二聚化子晶格能量差（~22 meV），两者易混。

**可辨识性判别表**（理论版：每条判别 = 判据 / 排除谁[竞争图景] / 确立谁）：

| 判别 | 判据（论证/数据） | 排除谁 | 确立谁 |
|------|-------------|--------|--------|
| **手征 vs 非手征并存** | Δ=0 时 Ŝ 对称性（式 3）→ $\varepsilon(p_y)=\varepsilon(-p_y)$ 在两谷都成立 → 局域态支持反向传播模式 📜Q（§3） | 纯手征畴壁态图景（畴壁只承载谷锁定手征态） | 畴壁电子结构含**非手征** 1D 态（每个谷内双向传播） |
| **束缚态 vs 准束缚态** | 低能态能量在体连续谱之外（局域）；高能 1D 带穿入 2D 连续谱后变 quasistationary（逃逸到 AB/BA 畴）📜Q（摘要 + §4） | 非手征态仅存在于能隙内的图景 | 非手征态由束缚态连续过渡到准束缚态（共振） |
| **LL kink = 非手征态 vs skipping 轨道** | 最大漂移速度态追踪的 kink 在 B=1 T 与 B=3 T 对应**同一** ε(k_y)（不随 B 缩放）；更高能色散特征随 B 缩放 📜Q（§4，Fig. 3/4） | skipping 回旋轨道（位置随 B 缩放） | LL 谱中 kink = 非手征 1D 准束缚态（B 无关性判据） |
| **最小模型 vs 全模型（e-h 对称）** | 最小模型（$v_3=v_4=0,\Delta'=0$）给出 e-h 对称 DW 谱；全模型（$v_{3,4}>0$）破缺 e-h 对称（$k_F(n)$ 正负载流子密度不对称，Fig. 5a）📜Q（§5） | 理想 e-h 对称的 DW 谱 | 真实 BLG 的 DW 谱 e-h 对称破缺 |

> **主结果 ↔ 判别表的对应**：
> - 主结果① 非手征 1D 态存在（与手征并存）← {手征 vs 非手征并存}
> - 主结果② 束缚态 → 准束缚态过渡 ← {束缚态 vs 准束缚态}
> - 主结果③ 准束缚态经 LL 杂化追踪（B 无关 kink）← {LL kink vs skipping 轨道}
> - 主结果④ e-h 对称破缺 + minigap δ 依赖 w、Δ ← {最小 vs 全模型}

> **[前提与限定]**（判别结论的适用范围）：
> - **噪声/扰动**：纯数值能带计算，**未建模**热展宽、无序、退相干；无序仅以"残余无序散射低能 1D 态""非手征态有有限背散射长度"定性讨论 📜Q（§3/§5）。全文无误差棒（无 ±）。
> - **判别性扫轴**：$w=7,10,14$ nm × $\Delta=0,2,10,20$ meV（Fig. 2）与 $\Delta=0,20$ meV（Fig. 4）× $B=0,1,3$ T × $\varepsilon\in[-100,100]$ meV。$w$ 是唯象参数（原文："no commonly established value for the DW width"）📜Q。
> - **候选集 M 边界**：模型结构固定为 SWM 型 4×4 哈密顿量 + FKM 位移场（单条、直臂椅取向、孤立畴壁）；**未考虑**：其他畴壁取向、畴壁弯曲/无序网络、电子-电子相互作用、多畴壁耦合、有限温度。这些集外候选未排除（封闭世界假设）。

三层标注：📜Q = 原文事实（附位置）｜推导｜📊F = 读图估算｜💭I = 推断。**不确定度（正交轴）**：[±] 原文误差棒 / [~] 原文以 ≈ 给出无误差棒 / [读图] 图·色标提取 / [相对] 仅相对量。所有数字经 pdftotext + grep 反向核对。

---

## 2. 结果与机制（按论文论证结构：畴壁结构 / B=0 谱 / Δ≠0 谱 / B≠0 追踪 / 实验含义）

### 2.1 畴壁结构：Frenkel–Kontorova 模型（FKM）

单条 AB/BA 畴壁用 FKM 描述为**部分螺位错**（partial screw dislocation），Burgers 矢量 $b=(0,a/\sqrt3)$ 沿臂椅方向，设边界条件于层间位移场 $u=(0,u_y(x))$（把 AB 连续变换到 BA 堆垛）📜Q（§2，Fig. 1）。位移场解（式 1）$u_y(x)=\frac{2a}{\sqrt3\pi}\arctan e^{2x/w}$，其中畴壁全宽 $w=(a/\pi)\sqrt{\mu/6V}$ 📜Q（§2 式 1 与脚注 1）。代入 $a=0.246$ nm、$\mu=920$ eV/nm²、$V=0.0296$ eV/nm² 得 $w\approx6$ nm 📜Q（脚注 1）[~]。

> **w 无公认值**：原文明说 "no commonly established value for the DW width"，文献报道/讨论范围 $6\text{ nm}<w<14\text{ nm}$，故 w 作为唯象参数覆盖该范围 📜Q（§2）。数值计算取 $w=7,10,14$ nm（Fig. 2/4）📜Q。

### 2.2 B=0 谱与非手征态的起源（Δ=0 的 Ŝ 对称性）

哈密顿量（式 2，4×4、谷标记 $\xi=\pm$、层+子晶格基）在 Δ=0 时满足 $Ŝ H_\xi(p_x,p_y)Ŝ^+=H_\xi(p_x,-p_y)$，$Ŝ=\tau_x\sigma_x$（式 3），由此 $\varepsilon(p_y)=\varepsilon(-p_y)$ 在两谷都成立 → 局域态在每个谷内都支持**反向传播模式**，故为**非手征** 📜Q（§3）。能谱含两类态：散布于 AB/BA 畴的散射态连续谱（灰色区）+ 能量在连续谱之外的畴壁局域态 📜Q（§3）。

### 2.3 Δ≠0：手征态生成 + 非手征带重连（minigap δ）

层间不对称势 Δ 破缺双层反演对称：首先在能隙内生成**谷极化手征态对**（谷 Chern ±2 的拓扑态，见 [PHY-BERRY]）📜Q（§3/引言）；同时改变非手征 1D 带色散——**手征与非手征带 merge 并 reconnect 色散线**，在更宽的畴壁中发生在更高的 Δ；且随 Δ 增大或 w 减小，重连带边缘被推向体 BLG 的 ±Δ/2 带边，从中间 Δ 的"重叠带"区过渡到高 Δ 的"gapful"对 📜Q（§3，Fig. 2）。**取决于 w 与 Δ，非手征态谱可以保持无能隙，或获得 minigap δ** 📜Q（§5）。δ 随输入 Δ 的依赖画在 Fig. 5b（Δ 可由面外位移场调控，引 ref 41）；δ 数值为图中读值，正文未给具体数 📜Q [读图]。

### 2.4 B≠0：准束缚态的 LL 杂化追踪（kink 判别）

当 1D 带进入体连续谱，畴壁局域态因衰变到 AB/BA 散射态而变 quasistationary 📜Q（§4）。追踪方法：面外磁场把 2D 连续谱离散成 LL 集 → 1D 带被稳定在体 LL 之间的能量 → 与 LL 态**微扰杂化**，形成沿畴壁传播的态，表现为 LL 色散的尖锐弯折（kink）📜Q（§4）。判别：沿最大漂移速度态追踪的 kink，在 B=1 T 与 B=3 T 下对应同一 $\varepsilon(k_y)$（不随 B 缩放），而更高能色散特征随 B 缩放 → 后者归为畴内 skipping 回旋轨道 📜Q（§4，Fig. 3/4）。此法的旁证：此类 1D 态已在 AB/BA 畴壁 + 超导引线的量子输运中观测到（邻近效应维持到 5 T，引 ref 22 = Barrier 2024 Nature）📜Q（§4）。

### 2.5 实验含义（背散射 / 弹道 / 通道数 / 量子线）

- **与手征态的无序敏感性对比**：拓扑态在能隙内形成、对两谷长程无序的背散射受保护；而 1D 非手征态有**有限背散射长度** 📜Q（§3）。但对当今最优质石墨烯异质结 [ref 23]，低温（T→0）下散射长度可超过器件尺寸，实现**弹道输运**区，1D 通道总数由费米能级调节 📜Q（§3）。
- **量子线图景**：尽管高能 1D 态衰变到 2D 体（残余无序散射低能 1D 态所致），在有限长度畴壁段上，它们"could act as"（可充当）一条与 2D 体**并联**的 1D 量子线 📜Q（§5，作者措辞）。
- **e-h 对称破缺**：真实系统（$v_{3,4}>0$，与 ref 39 早前报道一致）破缺 DW 态电子-空穴对称，体现为 $k_F(n)$ 在正负体载流子密度下不对称（Fig. 5a）📜Q（§5）。**预期**（"we expect"）最小模型 [ref 40，$v_3=v_4=0,\Delta'=0$] 给出的 e-h 对称谱在真实系统中被打破 📜Q（§5）。

---

## 3. 理论模型与方法

### 3.1 模型（FKM → 4×4 哈密顿量）
- **晶格**：FKM 位移场（式 1）→ 层间侧向偏移矢量 $r_0(x)=(0,a/\sqrt3+u_y(x))$ 描述跨畴壁的堆垛变化，从 AA 堆垛起算 📜Q（§2）。
- **电子**：SWM 型 4×4 哈密顿量（式 2），谷 $\xi=\pm$、层+子晶格基 $\Psi=(\psi_{At},\psi_{Bt},\psi_{Ab},\psi_{Bb})^T$；含谷依赖的 $T_\xi(r_0)$ 隧穿矩阵（$\gamma_1$、$v_3$、$v_4$ 项）与位置依赖对角项 $E_0(r_0)+E_1(r_0)\sigma_z$（$\Delta'$）📜Q（§3）。
- **参数**（全部 📜Q[~]，§3/脚注 1）：$v\approx10^6$ m/s、$\gamma_1\approx380$ meV、$v_3\approx0.123v$、$v_4\approx0.045v$、$\Delta'\approx22$ meV、$a=0.246$ nm、$\mu=920$ eV/nm²、$V=0.0296$ eV/nm²。

### 3.2 磁场（Peierls + Landau 规范 + 磁振子基）
磁场经 Peierls 替换 $p\to(-i\hbar\partial_x,\,-i\hbar\partial_y-eBx)$ 进入式 2；用 Landau 规范下的磁振子态基（式 4，$z=x/\lambda_B-k_y\lambda_B$，Hermite 多项式）展开子晶格分量；对稠密 $k_y$ 集数值对角化，基尺寸 N 取到保证 $\varepsilon\in[-100,100]$ meV 内收敛 📜Q（§4）。

### 3.3 准束缚态提取
B=0 局域态色散（Fig. 2 黑点）→ 用 B=1 T 最大漂移速度态的 kink 外推进连续谱 → 在 B=3 T 谱上复验 kink 对应同一 ε(k_y)（B 无关性）→ 组合成跨越"真局域 + 准静态"两区间的完整色散（Fig. 4 橙线）📜Q（§4）。

> 非手征性判据、谷 Chern 手征态、量子线通道计数等通用推导见 [PHY-BERRY] / [PHY-LB]，此处不复制。

---

## 4. 关键预言与数据（提取链 + 验证链 + 不确定度标注）

| 量 | 值 | 证据 | 不确定度 |
|----|-----|------|---------|
| 畴壁宽 $w$ 定义 | $w=(a/\pi)\sqrt{\mu/6V}$ | 📜Q（§2 式 1） | 公式 |
| $w$（代入标称值） | $\approx6$ nm | 📜Q（脚注 1） | [~] |
| $w$ 文献范围 | $6\text{ nm}<w<14\text{ nm}$ | 📜Q（§2） | [~]（原文 "range as"） |
| 计算取 $w$ | 7, 10, 14 nm | 📜Q（Fig. 2/4 caption） | 确定值 |
| 计算取 $\Delta$ | 0, 2, 10, 20 meV（Fig. 2）；0, 20 meV（Fig. 4） | 📜Q（caption） | 确定值 |
| $B$ | 0, 1, 3 T | 📜Q（Fig. 3/4 caption） | 确定值 |
| 能量窗 | $-100\le\varepsilon\le100$ meV | 📜Q（§4） | 确定值 |
| 邻近效应上限 | 5 T（引 ref 22） | 📜Q（§4） | 外部文献 [~] |
| minigap $\delta$ | 依赖 $w,\Delta$，数值在 Fig. 5b | 📜Q（§5） | [读图]（正文无数值） |
| $k_F(n)$ | 正负 $n$ 不对称（Fig. 5a） | 📜Q（§5） | [读图]（相对量） |
| 谷 Chern | ±2 | 📜Q（引言） | 确定值 |

**提取链**：
- $w$：$a,\mu,V\to$（式 1）$\to w\approx6$ nm；唯象上覆盖 6–14 nm 📜Q。
- $k_F(n)$：$B=0$ 色散点 + Fig. 4 橙线插值色散 → 非手征 1D 带的费米波矢 vs 体载流子密度 📜Q（Fig. 5a caption）。
- $\delta(\Delta)$：Fig. 2 非手征谱 minigap → 对每个 w 画 $\delta$ vs $\Delta$，对非零 δ 点做线性拟合（Fig. 5b 空符号 + 虚线）📜Q（§5）。

**验证链**：B=1 T 与 B=3 T 的 kink 对应同一 ε(k_y)（B 无关性）→ 独立确证 kink 来自非手征 1D 态而非 skipping 轨道 📜Q（§4）；与 Barrier 2024（ref 22）超导邻近效应观测互为实验佐证 📜Q（§4）。

---

## 5. 主要结论

1. 畴壁除谷极化手征拓扑态外，还（取决于宽度）承载**非手征 1D 态**：低能束缚、高能准束缚 📜Q（摘要，作者 "we show"）。
2. 非手征性来自 Δ=0 的 Ŝ 对称性（式 3）——每个谷内双向传播，与手征态的谷锁定单向传播判然不同 📜Q（§3）。
3. 手征 + 非手征带可共存并 merge/reconnect；非手征谱可保持无能隙或获得 minigap δ（依赖 w、Δ）📜Q（§3/§5）。
4. 非手征态有有限背散射长度（非拓扑保护），但最优异质结低温下可弹道输运，通道数由费米能级调节 📜Q（§3）。
5. 真实系统（$v_{3,4}>0$）破缺 DW 态电子-空穴对称 📜Q（§5，作者 "we expect"）。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| w 无公认值 | w 作唯象参数扫 6–14 nm；原文明言无公认值 | 📜Q（§2） |
| 纯数值、无温度/无序建模 | 无序仅定性（"残余无序散射"）；热展宽未建模 | 📜Q（§5）+ 💭I |
| minigap δ、k_F 无数值表 | 仅 Fig. 5 读图，正文未给具体值 | 📜Q [读图] |
| 模型结构受限 | 单条直臂椅畴壁、SWM 哈密顿量、无相互作用 | 💭I（M 边界） |
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
| 输出 ↔ 可算量 | 1D 带色散 ε(k_y)、minigap δ(Δ)、k_F(n)、LL 谱 kink ↔ LDOS 峰 / 电导通道 📜Q |

> 与 TBPM/Kubo 对应：本文是单畴壁连续模型能带计算；TBPM 复现需构造 AB/BA 畴壁（FKM 位移场）的紧束缚模型，核对畴壁局域 1D 带的 ε(k_y) 与 LL kink 是否复现非手征态特征 💭I。

---

## Phase S 目的接口（引用式）

- **Q1（edge state 如何表征）**：本文明确定性表征——非手征 1D 态经 Ŝ 对称性（反向传播模式）定义，空间上局域于畴壁（Fig. 3 最大漂移速度态）；手征态经谷锁定单向传播定义。详见 §2.2/§2.3。
- **Q2（理论如何复现）**：SWM 型 4×4 哈密顿量 + FKM 位移场（§3），输出 ε(k_y)/δ/k_F/LL kink；非手征态的存在是计算预言，需实验核对 📜Q。
- **Q3（理论↔实验对应）**：对应 Barrier 2024（ref 22）超导邻近效应到 5 T 的 1D 态观测；可检验预言 = Fig. 5a k_F(n) 不对称 + Fig. 5b δ(Δ) + LL kink 📜Q。

> **增量价值**：补充纯拓扑畴壁图景——畴壁完整电子结构含非手征（约束）+ 手征（拓扑）两部分；非手征态对无序无拓扑保护但低温可弹道。report 侧可用其"手征 vs 非手征"判别（Ŝ 对称性判据）与 Fig. 5 可检验预言；⚠️ 不可引用旧 review 的"势阱深 10–20 meV"（无源）。

## 反向核对 pass (2026-09-02)

pdftotext 提取 `/tmp/T23.txt`（511 行，正文 8 页，无 SI），逐项 grep 核对：
- ✅ 全部数字（$a=0.246$、$\mu=920$、$V=0.0296$、$w\approx6$ nm、6–14 nm、7/10/14 nm、0/2/10/20 meV、$\gamma_1\approx380$、$v_3\approx0.123v$、$v_4\approx0.045v$、$\Delta'\approx22$、$v\approx10^6$、B=1/3 T、±100 meV、5 T、谷 Chern ±2）均 grep 命中原文。
- ✅ 作者/期刊/DOI 与 citation 块一致（Moulsdale 第一作者；Academia Nano 2024;1；10.20935/AcadNano7267）。
- ⚠️ **arXiv 2307.14293 正文未出现**（grep "2307/arxiv" 仅命中 ref 33 的 arXiv.2203.16079）→ 标外部来源。
- ⚠️ **grep "Zheng" 无命中** → "解释 E14" 降级 💭I 移出正文。
- ⚠️ **grep "V_DW / scalar potential / potential well / electrostatic" 均无命中** → 旧 review 的"有效标量势 V_DW(x) 势阱""静电束缚"降级为 review 层推断，正文改为原文措辞（FKM 位移场 + 位置依赖 E0,1(r0) 项 + Ŝ 对称性判据）。
- ⚠️ **grep "peak/single/double/sides" 无手征双线 vs 非手征单峰的空间分布表述** → 该对比降级 💭I；正文只保留原文 📜Q（"highest drift velocity state strongly localized at the DW"，Fig. 3）。
- ⚠️ **旧 review "栅压切换非手征态开/关"无源** → 原文为"通道数由费米能级调节""minigap δ 由位移场调控"（ref 41），已按原文改写。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-11 | 初读（research_onboarding Phase 4 风格），标题误写 "Enaldiev, Moulsdale... (2023)" |
| 2026-08-19 | 修正①：旧版 "V_DW 势阱深 10–20 meV" 无源——原文 10/20 meV 是层间不对称势 Δ 的取值系列 Δ=0,2,10,20 meV，非势阱深度（appendix_B #6） |
| 2026-08-19 | 修正②：旧版 "解释 Zheng 2022 (E14) STM 额外 LDOS 峰" 无源——原文引用列表无 Zheng 2022（grep "Zheng" 无命中），降级 💭I（appendix_B #18） |
| 2026-09-02 | **4 块新架构整体重写**：按 spec 输出结构（TL;DR + 系统辨识导览 + 结果机制 + 理论模型与方法 + 关键预言 + 结论 + 局限 + 关系 + 影响 + 模型映射 + 目的接口 + 反向核对 + 更正日志）；补四层变量表、理论版判别表、[前提与限定]、主结果↔判别映射 |
| 2026-09-02 | 修正③：作者顺序（Moulsdale 第一作者）、年份 2024、期刊 Academia Nano 2024;1、DOI 10.20935/AcadNano7267（appendix_B #17）；arXiv 2307.14293 标外部来源 |
| 2026-09-02 | 修正④：grep 核实旧 review 无源表述——"标量势 V_DW(x) 势阱""静电束缚""双线 vs 单峰空间分布"均原文无命中 → 降级 💭I 并按原文措辞改写（FKM 位移场 + E0,1(r0) + Ŝ 对称性）；"栅压切换开/关"改为原文"通道数由费米能级调节 + minigap δ 由位移场调控" |
| 2026-09-02 | 新增 📜Q 事实：Ŝ 对称性判据（式 3）、LL kink 的 B 无关性判别、merge/reconnect 带重连、e-h 对称破缺（k_F(n) 不对称）、Barrier 2024 5 T 邻近效应、FKM 参数表 |
