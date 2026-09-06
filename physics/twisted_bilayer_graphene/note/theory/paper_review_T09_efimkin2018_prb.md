<!--
 * @Author       : AI 精读 (系统辨识式阅读法 → 三层分离整理)
 * @Date         : 2026-08-06（初读）→ 2026-09-02（按 4 块辨识结构重读）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T09_efimkin2018_prb.md
 * @Description  : T9: Efimkin & MacDonald 2018 — 螺旋网络模型的系统理论（纯 review，2026-09-02 按 4 块新架构整体重写）
-->

# Paper Review: Efimkin & MacDonald (2018) — 螺旋网络模型的系统理论

| 字段 | 内容 |
|------|------|
| **编号** | T9 |
| **标题** | Helical network model for twisted bilayer graphene |
| **作者** | Dmitry K. Efimkin, Allan H. MacDonald |
| **期刊** | Physical Review B 98, 035404 (2018)（Received 16 Mar 2018；published 2 Jul 2018 📜Q） |
| **DOI / arXiv** | DOI 10.1103/PhysRevB.98.035404（正文页 1 出现 📜Q）/ arXiv:1803.06404（⚠️ 正文未出现，外部来源） |
| **类型** | 理论 — 螺旋网络系统理论 |
| **课题组** | The Center for Complex Quantum Systems, The University of Texas at Austin 📜Q |
| **PDF / SI PDF** | ✅ reference/pdfs/Efimkin和MacDonald - 2018 - Helical network model for twisted bilayer graphene.pdf（正文 6 页，无 SI） |
| **精读日期** | 2026-08-06（初读）→ 2026-09-02（按 4 块新架构重读） |

> **共享知识引用**：valley Chern / helical（chiral vs helical）见 `[PHY-BERRY]`；网络 miniband 驻波量子化 / Δn=4/A 见 `[PHY-MB]`；双栅静电学（位移场 2u）见 `[PHY-GATE]`。本文是 `[PHY-MB]` 网络 miniband 的"本文代入"母本之一（能带能标 $\varepsilon_L$、DoS 周期 $\varepsilon_L/3$）。阅读疑问见 `note/shared/method/mechanism_questions.md` `[METHOD-Q]`。

---

## TL;DR

**本文想解决的问题**：小扭角双层石墨烯（TBG）在有限层间位移场下，其低能电子结构能否被一个**唯象螺旋网络模型**完整捕获——电子局域在分隔近似 AB/BA 堆叠区的畴壁上，构成三角网络？

**主结果**：① 从 4-band $k\cdot p$ 连续模型投影到 2-band 子空间，畴壁 = Jackiw-Rebbi 零模（色散 $\varepsilon_p = v p_\parallel$），谷陈数跨壁跳变 $\Delta C=2$ → 每 valley/spin 两条 helical 通道 📜Q；② AA 节点 3×3 幺正 S 矩阵（三角对称性约束，仅由角度 $\alpha$ 参数化）+ Bloch 定理 → 网络能带**无隙、含 Dirac 点**（$\Gamma,K,K'$，$v_D=v/2$ 独立于 $\alpha$）📜Q；③ 态密度 DoS 在能量上**周期性振荡**（每周 1 零点 + 1 van Hove 发散），DoS 周期 $\varepsilon_D=\varepsilon_L/3$，能带能标 $\varepsilon_L=2\pi\hbar v/L$（$\theta=0.245°$、$L\approx58$ nm 时 $\approx72$ meV 📜Q[~]）。

**结论/意义**：位移场下 TBG 的低能物理由唯象螺旋网络模型描述（摘要 "captured by a phenomenological helical network model" 📜Q）；模型给出 [43] 数值 DoS 峰的解释（作者措辞 "does seem to suggest" 📜Q）；**预言**强位移场下 magic angle 行为缺席（作者 "We predict" 📜Q）。

---

## 1. 系统辨识导览（判别表为全文唯一权威，机制细节见 [PHY-*]）

**黑箱三要素**：`{输入旋钮 θ / 2u / E | 输出观测量 网络能带 ε(q)、DoS ν(ε)、Dirac 点 | 声称结论 低能物理 = 螺旋网络模型}`

**四层变量图**（符号层一次钉死）：

| 层 | T9 实例 |
|----|---------|
| **L1 旋钮 u** | $\theta$（扭角）、$2u$（层间位移场，栅压产生）、$E$（能谱变量，扫轴） |
| **L2 导出量 x₁** | $L=a_0/[2\sin(\theta/2)]$（moiré 周期）、$k_\theta=2k_D\sin(\theta/2)$（Dirac 点间距，$k_D=4\pi/3a_0$）、$\varepsilon_L=2\pi\hbar v/L$（网络能带能标）、$\delta_\pm(\mathbf{r})=(|T_{BA}|\pm|T_{AB}|)/2$（局域能隙）、$p_u=u/v$ |
| **L3 模型量 x₂** | $S$ 矩阵（$\alpha$ 参数化）、$U_q$（离散演化算子）、能带 $\varepsilon_{q}^{nm}$、valley Chern $C=\delta_-/|\delta_-|$、Dirac 速度 $v_D=v/2$、DoS $\nu(\varepsilon)$ |
| **固定参数（非旋钮）** | $a_0$（石墨烯晶格周期）、$v=10^6$ m/s（单层 Dirac 速度 📜Q[~]）、$w=400$ meV（杂化能标，引 [1] 📜Q[~]） |
| **反推量 θ̂** | $v_\parallel$（helical 态速度，由 $v_\parallel\approx\delta_+/p_u\approx 2wv/(3u)$ 估计 → $1.6\times10^6$ m/s 📜Q[~]） |
| **L4 观测量 y** | 网络能带 $\varepsilon(q)$（Fig. 1）、DoS $\nu(\varepsilon)$（Fig. 4）、Dirac 点位置/速度、DoS 周期 $\varepsilon_D$（可实验检验的预言） |

> ⚠️ 符号歧义：本文 `$k_D$` 出现**两个**含义——单层 BZ 角矢量 $k_D=4\pi/3a_0$（§II，定义 $k_\theta$）与网络 BZ 内 Dirac 点间距 $k_D=4\pi/3L$（§III 末）📜Q。二者别混淆（前者是单层晶格量，后者是 moiré 网络量）。

**可辨识性判别表**（理论版：每条判别 = 判据 / 排除谁[竞争图景] / 确立谁）：

| 判别 | 判据（推导/数据） | 排除谁 | 确立谁 |
|------|-------------|--------|--------|
| **helical 对 vs 单通道** | 局域谷陈数 $C=\delta_-/|\delta_-|$，跨畴壁 $C_{AB}-C_{BA}=2$ → 每 valley/spin 两条通道（反向传播、$T$ 连接两谷）📜Q（§II） | 单通道 / 非螺旋图景 | 谷锁定 helical 对 |
| **无隙 vs 有隙网络** | 判别式 $D=27+4\mathrm{tr}[U_q]^3+\mathrm{tr}[U_q^\dagger]^3-18|\mathrm{tr}[U_q]|^2-|\mathrm{tr}[U_q]|^4=0$ 在 $\Gamma,K,K'$ 对任意 $\alpha$ 成立（三角对称性）📜Q（§III） | 有隙网络能带 | 无隙 + Dirac 点（$v_D=v/2$ 独立于 $\alpha$） |
| **DoS 周期 = $\varepsilon_L/3$** | 三链对称 → DoS 周期为能带周期 $1/3$，每周 1 零点 + 1 van Hove 对数发散 📜Q（§III） | 无周期 / 任意周期 DoS | DoS 周期振荡谱（可实验检验） |
| **网络 vs 紧束缚** | 能量周期性来自网络模型离散演化算子相位，区别于标准紧束缚模型 📜Q（§III） | 标准紧束缚能带 | 网络模型特征能带 |
| **本文 regime vs [52]** | 需位移场 + 小扭角 vs 无位移场 + 大扭角近公度（[52] honeycomb 网络）📜Q（§IV） | 非螺旋 honeycomb 网络（不同 regime） | 位移场下 helical 网络 |
| **网络模型 vs 直接数值** | $\varepsilon_D\approx\varepsilon_L/3\approx20$ meV 与数值 [43] $\varepsilon_D\approx21$ meV 吻合（$\theta=0.2°$、$2u\approx180$ meV）📜Q（§IV） | 峰需全连续体数值才能解释 | 解析网络模型捕获 DoS 峰（"good agreement"/"does seem to suggest"） |

> **主结果 ↔ 判别表的对应**（每条主结果由哪几条判别确立）：
> - 主结果① 畴壁 helical 通道（$\Delta C=2$）← {helical 对 vs 单通道}
> - 主结果② 网络能带无隙含 Dirac ← {无隙 vs 有隙, 网络 vs 紧束缚}
> - 主结果③ DoS 周期振荡 ← {DoS 周期 = $\varepsilon_L/3$, 网络模型 vs 直接数值}
> - （前提）本文 regime 界定 ← {本文 regime vs [52]}
>
> **理论论文的"判别"性质**：本文不是排除实验竞争解释，而是①界定模型的**适用 regime**（位移场+小扭角，区别于 [52]）、②给出**模型自洽结果**（无隙/DoS 周期来自对称性）、③用**数值互验**（$\varepsilon_D\approx20$ vs 21 meV）确立模型捕获了 [43] 的峰。作者对数值互验的措辞是 "good agreement" / "does seem to suggest"（建议性，非"证明"）📜Q。

> **[前提与限定]**（判别结论的适用范围）：
> - **近似假设**：局域近似（local approximation，动量积分在全动量空间而非 moiré BZ）📜Q；大位移场投影到 2-band 子空间（$\varepsilon_L\ll u\sim w$）📜Q；单通道/链（$\varepsilon_L\ll w\sim u$，$\varphi_I/\varphi_{II}$ 两 Dirac 锥动量分离 → 忽略其间散射）📜Q；唯象 S 矩阵（节点散射细节并入 $\alpha$，各向同性 $t_S$ 仅在节点附近重要 [49]）📜Q。
> - **适用范围**：$|\varepsilon|$ 低于 AB/BA 能隙（$|\varepsilon|\ll u,w$，helical 态为唯一低能自由度）📜Q；网络充分发育需波函数重叠 $|\psi_p(r_{\perp0})|^2/|\psi_p(0)|^2=\exp[-w/\varepsilon_L]\ll1$（$r_{\perp0}=L/2\sqrt3$）📜Q。
> - **候选模型集 M 边界**：{连续体数值 [43], 非螺旋网络 [52], 标准紧束缚} —— "helical 网络"在该集内确立；**集外候选**（无序、有限温度、非均匀应变、AA 堆叠区态、节点微观散射的完整解）原文未处理、未排除，须声明。

三层标注：📜Q = 原文事实（附位置）｜推导 = 由原文公式合成｜💭I = 推断。**不确定度（正交轴）**：[±] 原文误差棒 / [~] 原文以 ≈ 给出但无误差棒 / [读图] 图提取。本文为解析理论，**全文无误差棒**，所有数值参数标 📜Q[~]；精确恒等式（$\Delta C=2$、$v_D=v/2$ 等）标 📜Q。所有数字经 pdftotext + grep 反向核对。

---

## 2. 结果与机制（按论文三段：II 畴壁网络 / III 唯象网络模型 / IV 讨论）

### 2.1 畴壁网络：连续模型 → helical 通道（§II）

**起点**：valley $K$ 的 4-band $k\cdot p$ 连续模型（Eq. 1，sublattice $\otimes$ layer 空间 $\psi=\{\psi_{At},\psi_{Bt},\psi_{Ab},\psi_{Bb}\}$，$2u$ 为栅压产生的层间势差）📜Q。层间隧穿 $T(\mathbf{r})=\frac{w}{3}\sum_{i=1}^3 e^{-i\mathbf{k}_i\cdot\mathbf{r}}T_i$（Eq. 2，$w$ 为杂化能标）📜Q。

**2-band 投影**（大位移场 $\varepsilon_L\ll u\sim w$）：投影到上层导带 + 下层价带 2-band 子空间（Eq. 3），隧穿分为 $p$-波各向异性部分 $t_P(\varphi_p,\mathbf{r})=[T_{BA}e^{-i\varphi_p}-T_{AB}e^{i\varphi_p}]/2$ 与各向同性部分 $t_S(\mathbf{r})=-iT_d(\mathbf{r})\sin(\theta/2)$（$\theta\ll1$ 时忽略 [49]）📜Q。

**局域能隙各向异性**（Eq. 4）：$\Xi_p^2=\delta_-^2\cos^2[\varphi_p-\Theta]+\delta_+^2\sin^2[\varphi_p-\Theta]$，其中 $\delta_\pm(\mathbf{r})=(|T_{BA}|\pm|T_{AB}|)/2$，$\Theta(\mathbf{r})=(\arg[T_{BA}]-\arg[T_{AB}])/2$ 给出动量空间能隙极小方向 📜Q。**畴壁条件** $|T_{AB}|=|T_{BA}|\Rightarrow\delta_-=0$ → 能隙闭合 📜Q。

**谷陈数与通道数**：局域谷陈数 $C=\delta_-/|\delta_-|$（Eq. 5）；$\delta_-$ 跨壁变号 → 跨壁谷陈数差 $C_{AB}-C_{BA}=2$ → 每 valley/spin **两条** helical 通道（谷锁定反向传播）📜Q。

**Jackiw-Rebbi 零模**：近壁展开 → 两个相同各向异性 Dirac 锥 + 空间依赖质量 $\delta_-(\mathbf{r}_\perp)$（Eq. 6）；$\delta_-$ 变号 → Jackiw-Rebbi 解（Eq. 8），色散 $\varepsilon_p=v p_\parallel$ 📜Q。网络充分发育判据见 §1 [前提与限定]。

### 2.2 唯象网络模型：S 矩阵 + Bloch 能带（§III）

**节点 S 矩阵**：三进三出 → 3×3 幺正 S 矩阵；对称性约束（前向 $|S_{11}|=|S_{22}|=|S_{33}|$，240° 偏转幅度相等）→ 由角度 $\alpha$（$0\le\alpha\le\alpha_M=\arccos[1/3]$）+ 6 个相位参数化（Eq. 9）📜Q。核心矩阵 $\bar S$ 前向元素为 $\cos(\alpha)e^{i\chi}$、偏转元素为 $\sin(\alpha)/\sqrt2$，$\chi=\arccos[\{3\cos^2(\alpha)-1\}/2\cos(\alpha)]$ 📜Q。电子流守恒 $P_f+2P_d=1$，前向概率 $P_f=\cos^2(\alpha)$、偏转概率 $P_d=\sin^2(\alpha)/2$，仅由 $\alpha$ 决定 📜Q。

**Bloch 能带方程**：$\psi_{out}=e^{-i\varphi_E}\hat S\psi_{in}$（$\varphi_E=\varepsilon L/\hbar v$ 为沿链传播的动力学相位）→ Bloch 定理 → $[\lambda-U_q]\bar\psi=0$，$\lambda=e^{i(\varphi_E-\varphi_T)}$ 📜Q。$U_q$（Eq. 10）是离散演化算子，3 个特征值 $\lambda_{nq}$（$n=-1,0,1$）→ 3 条能带，周期 $\varepsilon_L=2\pi\hbar v/L$：$\varepsilon_q^{nm}=\varepsilon_L(\arg\lambda_{nq}/2\pi+\varphi_T/2\pi+m)$（Eq. 11，$m$ 保证周期性）📜Q。$U_q$ 幺正且 $\det U_q=1$ → 特征值问题 $\lambda_q^3-\mathrm{tr}[U_q]\lambda_q^2+\mathrm{tr}[U_q^\dagger]\lambda_q-1=0$（Eq. 12），能谱只依赖 $\mathrm{tr}[U_q]$（Eq. 13）→ **只依赖 $\alpha$**（相位 $\Theta_1,\Theta_2$ 可经动量平移消除）📜Q。

**无隙与 Dirac 点**：判别式 $D=0$ 在 $\Gamma,K,K'$ 高对称点对任意 $\alpha$ 成立 → 无隙；Dirac 速度 $v_D=v/2$ 独立于 $\alpha$；Dirac 点间距 $k_D=4\pi/3L$ 📜Q。能量周期性是网络模型区别于标准紧束缚模型的**特征** 📜Q。图示取 $\alpha=1.1$（对应 $P_f\approx0.2$、$P_d\approx0.4$；偏转更可能来自数值 [14]）📜Q[~]。

### 2.3 态密度与对标（§III 末 + §IV）

**DoS**（每 valley/spin/Dirac 点，Fig. 4）：周期 $\varepsilon_D=\varepsilon_L/3$（为能带周期 $1/3$，反映单胞三链对称）；每周 1 零点（Dirac 点）+ 1 鞍点对数发散（van Hove）；标度 $\nu_L=3\pi/(\varepsilon_L L^2)$ 📜Q。

**数值互验** [43]：$\theta=0.2°$、$2u\approx180$ meV 时数值 DoS 峰间距 $\varepsilon_D\approx21$ meV；本文取 $v\approx v$ 近似得 $\varepsilon_D\approx\varepsilon_L/3\approx20$ meV，"good agreement" 📜Q[~]。

**实验对标** [42]：$\theta=0.245°$、$L\approx58$ nm → $\varepsilon_L=2\pi\hbar v/L\approx72$ meV，与位移场能隙 $\varepsilon_g\approx60$ meV 同量级 → 模型**不完全适用**（隙内仅观测到 1 个 DoS 峰）📜Q[~]。最大能隙 $\varepsilon_g\approx250$ meV（[53,54]）→ 模型广能量范围适用 📜Q[~]。

**能标估计**：$w=400$ meV（[1]）→ helical 态速度 $v_\parallel=1.6\times10^6$ m/s > 石墨烯 $v=10^6$ m/s；网络周期 $\varepsilon_L\approx115$ meV、DoS 周期 $\varepsilon_D\approx38$ meV 📜Q[~]。

**预言**：强位移场下 magic angle 行为缺席（"We predict that magic angle behavior is absent at strong displacement fields" 📜Q）；能带弱依赖 $\theta$（除能标 $\varepsilon_L$ 外，网络发育良好时）📜Q。

---

## 3. 理论模型与方法（模型/哈密顿量/推导/计算方法）

### 3.1 连续模型与 2-band 投影
4-band $k\cdot p$（Eq. 1，自 Bistritzer & MacDonald [20]）→ 大位移场投影到 2-band（Eq. 3）。非常规步骤：隧穿分 $t_P$（$p$-波）/ $t_S$（各向同性，$\theta\ll1$ 忽略 [49]）。锚点：valley Chern / helical 见 `[PHY-BERRY]`。

### 3.2 局域能隙与 valley Chern
$\delta_\pm=(|T_{BA}|\pm|T_{AB}|)/2$（Eq. 4）；$C=\delta_-/|\delta_-|$（Eq. 5）；跨壁 $\Delta C=C_{AB}-C_{BA}=2$ 📜Q。

### 3.3 Jackiw-Rebbi 解
$\delta_-(\mathbf{r}_\perp)$ 变号 → Dirac Eq. (6) 的 Jackiw-Rebbi 零模，色散 $\varepsilon_p=v p_\parallel$（Eq. 7/8）📜Q。

### 3.4 网络 S 矩阵 + Bloch 能带方程
节点 3×3 幺正 S 矩阵（Eq. 9，$\alpha$ 参数化）→ 离散演化算子 $U_q$（Eq. 10）→ 特征值问题（Eq. 12）→ 能带（Eq. 11）。计算方法：**解析**（转移矩阵/离散演化算子法，与 Chalker-Coddington [45–47] 同类 📜Q）；无数值对角化。

---

## 4. 关键预言与数据（提取链 + 验证链 + 不确定度标注）

### 4.1 能标与参数表（全文无误差棒，标 📜Q[~]）

| 量 | 值 | 位置 | 证据 |
|----|-----|------|------|
| $\varepsilon_L$（$\theta=0.245°$） | $\approx72$ meV（$L\approx58$ nm） | §IV | 📜Q[~] |
| $\varepsilon_g$（实验 [42] 位移场能隙） | $\approx60$ meV | §IV | 📜Q[~] |
| $\varepsilon_g$（最大能隙 [53,54]） | $\approx250$ meV | §IV | 📜Q[~] |
| $w$（杂化能标，[1]） | $400$ meV | §IV | 📜Q[~] |
| $v_\parallel$（helical 态速度） | $1.6\times10^6$ m/s（$>v=10^6$ m/s） | §IV | 📜Q[~] |
| $\varepsilon_L$（$w=400$ meV） | $\approx115$ meV | §IV | 📜Q[~] |
| $\varepsilon_D$（$w=400$ meV） | $\approx38$ meV | §IV | 📜Q[~] |
| $\varepsilon_D$（数值 [43]，$\theta=0.2°$、$2u\approx180$ meV） | $\approx21$ meV | §IV | 📜Q[~] |
| $\varepsilon_D$（$v\approx v$ 近似） | $\approx\varepsilon_L/3\approx20$ meV | §IV | 📜Q[~] |
| $\alpha$（图示取值） | $1.1$（$P_f\approx0.2$、$P_d\approx0.4$） | §III | 📜Q[~] |
| $\alpha_M$（$\alpha$ 上限） | $\arccos[1/3]$ | §III | 📜Q |
| $C_{AB}-C_{BA}$ | $2$ | §II | 📜Q |
| $v_D$（网络 Dirac 速度） | $v/2$ | §III | 📜Q |
| $k_D$（网络 Dirac 点间距） | $4\pi/3L$ | §III | 📜Q |
| $r_{\perp0}$（墙到 AB/BA 中心） | $L/2\sqrt3$ | §II | 📜Q |

### 4.2 提取链（每列一条：观测量 → 反推量）

- **$\varepsilon_L$**：$\theta=0.245°\to L=a_0/[2\sin(\theta/2)]\approx58$ nm $\to\varepsilon_L=2\pi\hbar v/L\approx72$ meV 📜Q。
- **$\varepsilon_D$**：$\varepsilon_D=\varepsilon_L/3$（三链对称推导，原文明写 "three times smaller than the period of the network band structure" 📜Q）。
- **$v_\parallel$**：$v_\parallel\approx\delta_+/p_u\approx 2wv/(3u)$（Eq. 7）；$w=400$ meV → $1.6\times10^6$ m/s 📜Q。
- **$\Delta C=2$**：$C=\delta_-/|\delta_-|$，$\delta_-$ 跨壁变号 → $C_{AB}-C_{BA}=2$ 📜Q（推导）。

### 4.3 验证链

- **数值互验**：$\varepsilon_D\approx\varepsilon_L/3\approx20$ meV vs 数值 [43] $\approx21$ meV（"good agreement" 📜Q[~]）——但作者注明 [43] 工况不完全在本文 regime，$v_\parallel$ 公式不适用、需取 $v\approx v$ 近似 📜Q。
- **$\alpha$ 独立鲁棒性**：Dirac 点位置/能量、$v_D$ 均独立于 $\alpha$ → 拓扑性质鲁棒（推导）。
- **对称性自检**：相位 $\varphi_T=\Theta_1=\Theta_2=(\pi-2\arcsin[3\sin\alpha/(2\sqrt2)])/3$ 保证节点 120° 旋转对称（离散旋转对称）📜Q。

---

## 5. 主要结论

1. 位移场下 TBG 的低能物理由唯象螺旋网络模型描述（电子局域在 AB/BA 畴壁）📜Q（摘要）。
2. 网络能带无隙、含 Dirac 点（$\Gamma,K,K'$，$v_D=v/2$），DoS 在能量上周期性振荡（每周 1 零点 + 1 van Hove 发散）📜Q（摘要 + §III）。
3. 网络能谱只依赖单参数 $\alpha$（前向/偏转散射概率分配）📜Q。
4. 模型提供 [43] 数值 DoS 峰的解释（"does seem to suggest" 📜Q）；与 [42] 实验不完全适用（仅 1 峰，因 $\varepsilon_L\approx72$ meV 与 $\varepsilon_g\approx60$ meV 同量级）📜Q。
5. **预言**：强位移场下 magic angle 行为缺席 📜Q（"We predict"）。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| AA 节点散射假设（网络连通） | 唯象 S 矩阵未从微观解出节点；**网络连通性**是核心假设，后被 T12 (TZM) 挑战 | 📜Q + 💭I（外部对标，见 §7） |
| 唯象参数 $\alpha$ 未从微观确定 | $\alpha$ 由节点散射细节决定，本文未算（引 [51] 复杂依赖） | 📜Q |
| 未计无序/温度/非均匀应变 | 模型为干净、零温、周期 moiré 极限 | 💭I |
| 未处理 AA 堆叠区态 | 只处理 AB/BA 畴壁态（$|\varepsilon|\ll u,w$ 外失效） | 📜Q（适用范围） |
| 与 [42] 实验不完全适用 | $\varepsilon_L\approx72$ meV vs $\varepsilon_g\approx60$ meV → 隙内仅 1 峰 | 📜Q |
| 同一链两通道散射被忽略 | 单通道/链近似（$\varepsilon_L\ll w\sim u$） | 📜Q |

---

## 7. 与其他工作的关系（跨论文对标放这里，不放正文）

| 工作 | 关系 |
|------|------|
| Bistritzer & MacDonald 2011 [20] | 4-band 连续模型来源（Eq. 1 起点）📜Q |
| San-Jose & Prada 2013 [43] | 网络模型发起者 + 数值 DoS 峰；本文解析化并解释其峰 📜Q |
| Chalker-Coddington [45] / Ho & Chalker [46] / Mkhitaryan & Raikh [47] | 方法论祖先（QH 网络模型、离散演化算子法）📜Q |
| Huang 2018 [42] | STM 观测畴壁网络（本文 motivation + 实验对标）📜Q |
| Rickhaus 2018 [55] | 磁输运网络 signature（可被本文模型处理，作者 "can be addressed theoretically"）📜Q |
| Pal, Spitz & Kindermann 2018 [52] | 非螺旋 honeycomb 网络（无位移场 + 大扭角近公度，不同 regime）📜Q |

> ⚠️ Phase S 外部对标（非本文引用）：**T12 (Tsim/Koshino/MacDonald, TZM)** 挑战网络连通性假设（AA 节点散射）；**T15 (De Beule 2020)** 用散射相位统一重释 AB 振荡——均为**后续**理论，时间倒挂，💭I。

---

## 8. 对后续研究的影响

- 定义 mTBG 畴壁网络的**基准理论语言**：螺旋网络 = 拓扑畴壁态 + AA 节点 S 矩阵 + Bloch 能带 📜Q→💭I。
- 给出可实验检验预言：DoS 周期峰（$\varepsilon_D=\varepsilon_L/3\propto\theta$）↔ STM $dI/dV$ 多峰结构、磁输运网络 signature 📜Q。
- 留下核心开放问题：节点散射（$\alpha$）微观来源、网络连通性——T12/T15 承接修正 💭I。
- 预言强位移场下无 magic angle → 划定网络模型的 regime 边界 📜Q（predict）。

---

## 9. 理论模型映射（供 TBPM / Kubo-Bastin 计算对标）

| 映射 | 说明 |
|------|------|
| $\theta\to L\to\varepsilon_L$ | 扭角→moiré 周期 $L=a_0/[2\sin(\theta/2)]$→能带能标 $\varepsilon_L=2\pi\hbar v/L$ 📜Q |
| $2u\to\delta_\pm$ | 位移场→局域能隙 $\delta_\pm=(|T_{BA}|\pm|T_{AB}|)/2$；畴壁 $|T_{AB}|=|T_{BA}|\to\delta_-=0$ 📜Q |
| $\alpha\to S\to$ 能带 | 节点散射角度→3×3 S 矩阵→$U_q$→能带 $\varepsilon_q^{nm}$ 📜Q |
| $\varepsilon_L\to\varepsilon_D$ | 能带能标→DoS 周期 $\varepsilon_D=\varepsilon_L/3$ 📜Q |
| $v_\parallel\to$ 通道速度 | helical 态色散速度 $\approx2wv/(3u)$（Eq. 7）📜Q |
| $C=\delta_-/|\delta_-|$ ↔ 局域 valley Chern | TBPM 可算局域 valley Chern，验证跨壁 $\Delta C=2$ 📜Q |

> 与 TBPM/Kubo 对应：本文是**低能有效理论**（$|\varepsilon|\ll u,w$），TBPM 需在相同大位移场 regime 对比其局域能隙、畴壁色散与 DoS 周期；节点散射 $\alpha$ 在本文是唯象参数，TBPM 可从节点实空间剖面微观提取（补本文之缺）💭I。

---

## Phase S 目的接口（三问引用式）

- **Q1（edge state 如何表征）**：本文是理论——表征方式 = 能带 $\varepsilon(q)$（无隙 + Dirac 点 $v_D=v/2$）+ DoS $\nu(\varepsilon)$（周期振荡）+ 色散 $\varepsilon_p=v p_\parallel$；实验可验 = STM $dI/dV$ 多峰（$\varepsilon_D\propto\theta$）、磁输运 network signature 📜Q（§2/§4/§8）。
- **Q2（理论如何复现）**：本文即螺旋网络系统理论——连续模型→2-band 投影→Jackiw-Rebbi 模→AA 节点 S 矩阵→Bloch 能带；能谱只依赖 $\alpha$，DoS 周期 $\varepsilon_L/3$ 📜Q（§2/§3）。
- **Q3（理论↔实验对应）**：数值 [43] $\varepsilon_D\approx21$ meV ↔ 本文 $\approx20$ meV（"good agreement"）；实验 [42] $\varepsilon_L\approx72$ meV vs $\varepsilon_g\approx60$ meV（不完全适用，仅 1 峰）📜Q（§2.3/§4）。

> **增量价值**：本文是 `[PHY-MB]` 网络 miniband 的**解析母本**（能带能标 $\varepsilon_L=2\pi\hbar v/L$ + DoS 周期 $\varepsilon_L/3$），与 E12（实验 Δn=4/A、v_DW 提取）互为"理论解析 ↔ 实验反推"两端；report.md 理论侧引用其 $\Delta C=2$、$\varepsilon_L$、$\varepsilon_D=\varepsilon_L/3$ 与"强位移场无 magic angle"预言。比 E12 多的是：网络能带的**闭式色散**与 S 矩阵参数化；少的是：无实空间/输运数据（纯理论）。

---

## 反向核对 pass (2026-09-02)

pdftotext 提取正文（/tmp/T09.txt，424 行），逐项 grep 核对全部数字与专名：$\varepsilon_L$=72 meV、$L$=58 nm、$\theta$=0.245°、$\varepsilon_g$=60/250 meV、$w$=400 meV、$v_\parallel$=1.6×10⁶ m/s、$v$=10⁶ m/s、115/38 meV、21/20 meV、$2u$=180 meV、$\theta$=0.2°、$\alpha$=1.1、$P_f$=0.2、$P_d$=0.4、$\alpha_M$=arccos[1/3]、$C_{AB}-C_{BA}=2$、$v_D=v/2$、$k_D=4\pi/3L$、$r_{\perp0}=L/2\sqrt3$、$\delta_\pm=(|T_{BA}|\pm|T_{AB}|)/2$、$\varepsilon_D=\varepsilon_L/3$、"one zero and one divergence per period"、"captured by a phenomenological helical network model"、"We predict that magic angle behavior is absent" 等——**全部在原文找到** ✓。

⚠️ 本次修订发现并修正的**无源内容**（旧 review 中非原文、本次降级/改写）：
1. 旧 §3.3 S 矩阵 $S=\begin{pmatrix}0&t&r\\r&0&t\\t&r&0\end{pmatrix}$（$|t|^2+|r|^2=1$）**非原文**——原文 $\bar S$（Eq. 9）前向元素 $\cos(\alpha)e^{i\chi}\ne0$、偏转 $\sin(\alpha)/\sqrt2$，且流守恒为 $P_f+2P_d=1$。→ 改为原文 Eq. 9。
2. 旧 §4.1 能带方程 $\cos(q_n^0 L_\parallel)=(1-2|t|^2)/(2|t|^2)$ **非原文**——原文为 $U_q$ 特征值问题 $\lambda^3-\mathrm{tr}[U_q]\lambda^2+\mathrm{tr}[U_q^\dagger]\lambda-1=0$（Eq. 12）+ $\varepsilon_q^{nm}=\varepsilon_L(\arg\lambda_{nq}/2\pi+\varphi_T/2\pi+m)$（Eq. 11）。→ 改为原文 Eq. 11/12。
3. 任务/旧版 "$\alpha=|t/r|$" **非原文**——原文 $\alpha$ 为散射角度（$P_f=\cos^2\alpha$、$P_d=\sin^2\alpha/2$），与 $|t/r|$ 无对应。→ 改为原文定义。
4. 旧 §4.3 适用条件 "$|E|<\delta_+$" **非原文表述**——原文为 $|\varepsilon|\ll u,w$（helical 态唯一自由度）+ "below the AB and BA gaps"。$\delta_+$ 是局域能隙最大值（Eq. 4），非适用条件本身。→ 改为原文条件。
5. arXiv:1803.06404 正文未出现 → 标 ⚠️ 外部来源。

---

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-06 | 初读（research_onboarding Phase 4 风格）：一句话总结 + 背景 + 方法模型 + 核心结果 + 公式速查 |
| 2026-08-20 | **能标公式修正（S-REV，§B.5#1）**：旧版 "DoS 周期 $\sim2\pi\hbar v/L$" 符号混乱 → 拆为能带能标 $\varepsilon_L=2\pi\hbar v/L$（$\theta=0.245°$、$L\approx58$ nm 时 ≈72 meV 📜Q，grep "72 meV"/"58 nm" ✓）与 DoS 周期 $D=\varepsilon_L/3$（≈20 meV 📜Q）两个量；卡片旧版 "$E_\lambda=2\pi\hbar v/3\lambda$" 同源错误（实为 DoS 周期），已改 |
| 2026-09-02 | **按 4 块辨识结构整体重写**：头部字段表 + TL;DR 问题句式 + §1 系统辨识导览（黑箱三要素 + 四层变量表 + 理论版判别表 6 条 + 主结果↔判别映射 + [前提与限定]）+ §2 按论文三段（II 畴壁/III 网络模型/IV 讨论）+ §3 理论模型与方法 + §4 关键预言与数据（提取链/验证链/不确定度 📜Q[~]）+ §5–§9 + Phase S 接口 + 反向核对 pass；全文 📜Q/推导/💭I 分级 + 不确定度标注 |
| 2026-09-02 | **无源内容修正**：S 矩阵（旧 $\begin{pmatrix}0&t&r\\r&0&t\\t&r&0\end{pmatrix}$）、能带方程（旧 $\cos(qL)=(1-2|t|^2)/2|t|^2$）、"$\alpha=|t/r|$"、适用条件 "$|E|<\delta_+$" 均 grep 不到原文 → 分别改为原文 Eq. 9（$\bar S$，$P_f=\cos^2\alpha/P_d=\sin^2\alpha/2$）、Eq. 11/12（$U_q$ 特征值问题）、散射角度定义、$|\varepsilon|\ll u,w$ + "below AB-BA gaps"；arXiv 号正文未出现 → 标外部来源 |
| 2026-09-02 | **符号歧义标注**：本文 `$k_D$` 双义（单层 $4\pi/3a_0$ vs 网络 Dirac 间距 $4\pi/3L$），§1 变量表显式标注；理论"预言"全部用作者措辞（"We predict"/"does seem to suggest"）并标 📜Q |
