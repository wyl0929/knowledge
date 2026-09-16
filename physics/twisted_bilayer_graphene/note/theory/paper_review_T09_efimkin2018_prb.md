<!--
 * @Author       : AI 精读（白箱演绎结构）
 * @Date         : 2026-08-06（初读）→ 2026-09-02（4 块辨识结构，理论版）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T09_efimkin2018_prb.md
 * @Description  : T9: Efimkin & MacDonald 2018 PRB — 螺旋网络模型的系统理论（2026-09-08 按 5 块演绎结构重写：模型白箱/推导链/结论清单/假设-结论依赖图/接口）
-->

# Paper Review: Efimkin & MacDonald (2018) — 螺旋网络模型的系统理论

| 字段 | 内容 |
|------|------|
| **编号** | T9 |
| **标题** | Helical network model for twisted bilayer graphene |
| **作者** | Dmitry K. Efimkin, Allan H. MacDonald |
| **期刊** | Physical Review B 98, 035404 (2018)（Received 16 Mar 2018；published 2 Jul 2018 📜Q） |
| **DOI / arXiv** | 10.1103/PhysRevB.98.035404（正文页 1 出现 📜Q）/ arXiv:1803.06404（⚠️ 正文未出现，外部来源） |
| **类型** | 理论 — 螺旋网络系统理论 |
| **课题组** | Center for Complex Quantum Systems, The University of Texas at Austin 📜Q |
| **PDF / SI** | ✅ `reference/pdfs/Efimkin和MacDonald - 2018 - Helical network model for twisted bilayer graphene.pdf`（正文 6 页，无 SI） |
| **精读日期** | 2026-08-06（初读）→ 2026-09-02（4 块辨识结构）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」的五块记（见 `note/shared/method/theory_paper_reading.md` §3）：**① 模型白箱 → ② 推导链 → ③ 结论清单（分层）→ ④ 假设-结论依赖图 → ⑤ 接口**。理论论文无黑箱、无反推、无可辨识实验（是"白箱演绎"而非"黑箱溯因"），故不用"四层变量表 + 判别表"这套实验框架词汇（旧 4 块版已废弃）。
> **共享知识引用**：valley Chern / helical（chiral vs helical）见 `[PHY-BERRY]`；网络 miniband 驻波量子化 / Δn=4/A 见 `[PHY-MB]`；双栅静电学（位移场 2u）见 `[PHY-GATE]`。本文是 `[PHY-MB]` 网络 miniband 的"本文代入"母本之一（能带能标 $\varepsilon_L$、DoS 周期 $\varepsilon_L/3$）。阅读疑问见 `note/shared/method/mechanism_questions.md` `[METHOD-Q]`。

---

## TL;DR

**本文想解决的理论问题**：小扭角双层石墨烯（TBG）在有限层间位移场下，其低能电子结构能否被一个**唯象螺旋网络模型**完整捕获——电子局域在分隔近似 AB/BA 堆叠区的畴壁上，构成三角网络？

**主结果**：① 从 4-band $k\cdot p$ 连续模型投影到 2-band 子空间，畴壁 = Jackiw-Rebbi 零模（色散 $\varepsilon_p = v_\parallel p_\parallel$），局域谷陈数跨壁跳变 $C_{AB}-C_{BA}=2$ → 每 valley/spin 两条 helical 通道 📜Q；② AA 节点 3×3 幺正 S 矩阵（三角对称性约束，仅由角度 $\alpha$ 参数化）+ Bloch 定理 → 网络能带**无隙、含 Dirac 点**（$\Gamma,K,K'$，$v_D=v/2$ 独立于 $\alpha$）📜Q；③ 态密度 DoS 在能量上**周期性振荡**（每周 1 零点 + 1 van Hove 发散），DoS 周期 $\varepsilon_D=\varepsilon_L/3$，能带能标 $\varepsilon_L=2\pi\hbar v/L$（$\theta=0.245°$、$L\approx58$ nm 时 $\approx72$ meV 📜Q[~]）。

**结论/意义**：位移场下 TBG 的低能物理由唯象螺旋网络模型描述（摘要 "captured by a phenomenological helical network model" 📜Q）；模型给出 [43] 数值 DoS 峰的解释（作者措辞 "does seem to suggest" 📜Q）；**预言**强位移场下 magic angle 行为缺席（作者 "We predict" 📜Q）。⚠️ 全文为理论预言/解析，非已验证事实（网络连通性后被 T12 TZM 挑战，见 §5.3/§7）。

---

## 1. 模型白箱（理想系统 + 假设清单）

> 理论论文的研究对象是**白箱**——作者自写的理想模型，无需"反推内部"。本节只做两件事：**写下模型**（§1.1），**列出它成立的全部假设**（§1.3）。假设清单是本文一切结论的"前提集合"，§4 的依赖图据此展开。

### 1.1 连续模型与投影（自 Bistritzer-MacDonald [20]）

**4-band 连续模型**（Eq. 1，valley $K$，子格 $\otimes$ 层空间 $\psi=\{\psi_{At},\psi_{Bt},\psi_{Ab},\psi_{Bb}\}$）：

$$H_0=\begin{pmatrix}v\sigma_t \mathbf p - u & T(\mathbf r)\\ T^\dagger(\mathbf r) & v\sigma_b \mathbf p + u\end{pmatrix}$$

$2u$ = 栅压产生的层间势差；$\sigma_{t(b)}$ = 上/下层各旋转 $\pm\theta/2$ 的泡利矩阵矢量；谱 valley 与 spin 独立，两谷由时间反演联系 📜Q。层间隧穿 $T(\mathbf r)=\frac{w}{3}\sum_{i=1}^3 e^{-i\mathbf k_i\cdot\mathbf r}T_i$（Eq. 2，$w$ = 杂化能标；$k_1=-k_\theta e_y$、$k_{2,3}=k_\theta(\pm\sqrt3 e_x+e_y)/2$；$k_\theta=2k_D\sin(\theta/2)$、$k_D=4\pi/3a_0$）📜Q。

**2-band 投影**（Eq. 3，大位移场 $\varepsilon_L\ll u\sim w$）：投影到上层导带 + 下层价带，隧穿分 $p$-波各向异性 $t_P(\varphi_p,\mathbf r)=[T_{BA}e^{-i\varphi_p}-T_{AB}e^{i\varphi_p}]/2$ 与各向同性 $t_S(\mathbf r)=-iT_d(\mathbf r)\sin(\theta/2)$（$\theta\ll1$ 时忽略，[49]）📜Q。

**变量含义表**：

| 符号 | 含义 | 值/定义 |
|---|---|---|
| $\theta$ | 扭角（小角 $\theta\ll1°$） | 旋钮 |
| $2u$ | 层间位移场（栅压产生） | 旋钮 |
| $L$ | moiré 周期 | $a_0/[2\sin(\theta/2)]$ |
| $k_D$ | 单层 BZ 角矢量 | $4\pi/3a_0$（⚠️ 网络 Dirac 点间距也用 $k_D=4\pi/3L$，双义见下） |
| $a_0$ | 单层 Bravais 周期 | 固定常数 |
| $w$ | 杂化能标（[1]） | 400 meV 📜Q[~] |
| $v$ | 单层 Dirac 速度 | $10^6$ m/s 📜Q[~] |
| $\varepsilon_L$ | 网络 miniband 能标 | $2\pi\hbar v/L$ |
| $\delta_\pm(\mathbf r)$ | 局域能隙最小/最大值 | $(|T_{BA}|\mp|T_{AB}|)/2$ |
| $v_\parallel$ | helical 态速度 | $\approx\delta_+/p_u\approx2wv/(3u)$ |
| $r_{\perp0}$ | 墙到 AB/BA 中心距离 | $L/2\sqrt3$ |
| $\alpha$ | 节点散射角度（唯一控制参数） | $0\le\alpha\le\alpha_M=\arccos[1/3]$ |

### 1.2 参数分册（替代旧"四层变量表"：区分"作者设定" vs "推导所得"）

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | $\theta$（扭角）、$2u$（位移场）、$E$（能谱变量） |
| **导出量（由旋钮+常数算出）** | $L=a_0/[2\sin(\theta/2)]$、$k_\theta=2k_D\sin(\theta/2)$、$\varepsilon_L=2\pi\hbar v/L$、$\delta_\pm=(|T_{BA}|\pm|T_{AB}|)/2$、$p_u=u/v$、$v_\parallel\approx\delta_+/p_u\approx2wv/(3u)$ |
| **模型内部量（解的性质）** | $S$ 矩阵（$\alpha$ 参数化）、$U_q$（离散演化算子）、能带 $\varepsilon_q^{nm}$、谷 Chern $C=\delta_-/|\delta_-|$、Dirac 速度 $v_D=v/2$、DoS $\nu(\varepsilon)$ |
| **固定常数** | $a_0$、$v=10^6$ m/s、$w=400$ meV（引 [1]） |
| **预言量（可检验）** | 网络能带 $\varepsilon(q)$（Fig. 1）、DoS $\nu(\varepsilon)$（Fig. 4）、Dirac 点位置/速度、DoS 周期 $\varepsilon_D$ |

> 无"反推量 θ̂"层——理论论文不反推自数据。**符号防混**：本文 `$k_D$` **双义**——单层 BZ 角矢量 $4\pi/3a_0$（§II，定义 $k_\theta$）与网络 BZ 内 Dirac 点间距 $4\pi/3L$（§III 末）📜Q；$\delta_-$（局域能隙最小）≠ 能隙本身，$\varepsilon_L$（能带能标）≠ $\varepsilon_D$（DoS 周期）。

### 1.3 显式假设清单（本文结论的前提集合）

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **局域近似（local approximation）**：动量积分在全动量空间而非 moiré BZ | 模型 | 📜Q |
| A2 | **大位移场投影**：$\varepsilon_L\ll u\sim w$（投影到 2-band 子空间） | 推导 | 📜Q |
| A3 | **单通道/链**：$\varepsilon_L\ll w\sim u$（两 Dirac 锥 $\varphi_I/\varphi_{II}$ 动量分离 → 忽略其间散射） | 推导 | 📜Q |
| A4 | **唯象 S 矩阵**：节点散射细节并入 $\alpha$；各向同性 $t_S$ 仅在节点附近重要（[49]） | 模型 | 📜Q |
| A5 | **适用范围**：$|\varepsilon|\ll u,w$（低于 AB/BA 能隙，helical 态为唯一低能自由度） | 模型 | 📜Q |
| A6 | **网络充分发育**：波函数重叠 $|\psi_p(r_{\perp0})|^2/|\psi_p(0)|^2=\exp[-w/\varepsilon_L]\ll1$ | 模型 | 📜Q |
| A7 | **谷/自旋独立**：谱 valley/spin 独立，两谷由时间反演联系 | 模型 | 📜Q |
| A8 | **干净、零温、周期 moiré**（无无序/温度/非均匀应变） | 模型 | 💭I（原文未处理） |

> 判别性扫轴：$\theta$（0.2° / 0.245°）、$2u$（≈180 meV / 大位移场）、$\alpha$（0–$\alpha_M$，图示 1.1）。这些假设在 §4 逐一映射到"失效 → 结论崩塌"。

---

## 2. 推导链（演绎结构：顺论文顺序，每步"输入→输出→所用假设/定理→合法域"）

### 2.0 总览：论文四节是一条演绎链

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 前提定理层 | 引言 | 偏压开隙 + valley Chern + 畴壁拓扑约束（已知） | 位移场下畴壁网络是低能自由度 | refs 3–9 | — |
| 模型层 | II. Domain wall network | 4-band 连续模型 + 参数 | 2-band 投影 → 局域能隙 → valley Chern → Jackiw-Rebbi 模 | A1–A2 | $\varepsilon_L\ll u\sim w$ |
| 推导层 | III. Phenomenological network model | 节点 S 矩阵 + Bloch | 网络能带无隙 + Dirac 点 + DoS 周期 | A3–A4、三角对称 | $|\varepsilon|\ll u,w$ |
| 边界层 | IV. Discussions | 模型预言 + 对标 | regime 界定 + 数值互验 + 实验对标 + 预言 | A5–A6 | — |

### 2.1 前提定理层（引言）：位移场开隙 + 畴壁拓扑约束

- **已知物理**：Bernal 堆叠（AB/BA）有 $2\pi$ Berry 相、二次带接触、位移场开隙；gapped 态有非平庸谷依赖 Chern 数，支持畴壁（位移场反号 [3–6] 或不同堆叠 [7–9]）上电子的拓扑约束 📜Q。畴壁 helical 对（两谷反向传播）已实验确认 [10–12] 📜Q。
- **动机**：错位石墨烯双层预期有三角晶格上的 helical 畴壁态网络 [20–41]，近期被 STM 观测 [42] 📜Q；畴壁处 LDOS 强能量依赖 + 隙内单峰 → 说明 helical 态沿网络干涉重要 📜Q。

### 2.2 模型层（II. Domain wall network）：连续模型 → helical 通道

- **4-band → 2-band 投影**（A2）：大位移场下投影到上层导带 + 下层价带，得 2-band 哈密顿量（Eq. 3）；隧穿分 $t_P$（$p$-波）/ $t_S$（各向同性，$\theta\ll1$ 忽略）📜Q。
- **局域能隙各向异性**（Eq. 4）：$\Xi_p^2=\delta_-^2\cos^2[\varphi_p-\Theta]+\delta_+^2\sin^2[\varphi_p-\Theta]$，能隙极小方向 $\varphi_{I}=\Theta$、$\varphi_{II}=\Theta+\pi$，$\Theta=(\arg[T_{BA}]-\arg[T_{AB}])/2$ 📜Q。**畴壁条件** $|T_{AB}|=|T_{BA}|\Rightarrow\delta_-=0$ → 能隙闭合 📜Q。
- **局域谷 Chern 数**（Eq. 5）：$C=\delta_-/|\delta_-|$；$\delta_-$ 跨壁变号 → 跨壁谷陈数差 $C_{AB}-C_{BA}=2$ → 每 valley/spin **两条** helical 通道 📜Q。
- **Jackiw-Rebbi 零模**：近壁展开 → 两个相同各向异性 Dirac 锥 + 空间依赖质量 $\delta_-(\mathbf r_\perp)$（Eq. 6）；$\delta_-$ 变号 → Jackiw-Rebbi 解（Eq. 8），色散 $\varepsilon_p=v_\parallel p_\parallel$ 📜Q。每个 Dirac 点携带半份谷 Chern $C_D=\delta_-/2|\delta_-|$，负责一条 helical 态 📜Q。速度 $v_\parallel\approx\delta_+/p_u\approx2wv/(3u)$、质量 $\delta_-\approx\sqrt3 w\sin(2\pi r_\perp/\sqrt3 L)$（Eq. 7）📜Q。

### 2.3 推导层（III. Phenomenological network model）：S 矩阵 → Bloch 能带 → 无隙 + DoS

- **节点 S 矩阵**（Eq. 9）：三进三出 → 3×3 幺正；对称性约束（前向 $|S_{11}|=|S_{22}|=|S_{33}|$、240° 偏转幅度相等）→ 由角度 $\alpha$（$0\le\alpha\le\alpha_M=\arccos[1/3]$）+ 6 个相位参数化 📜Q。核心矩阵 $\bar S$ 前向元素 $\cos(\alpha)e^{i\chi}$、偏转 $\sin(\alpha)/\sqrt2$，$\chi=\arccos[\{3\cos^2(\alpha)-1\}/2\cos(\alpha)]$ 📜Q。电子流守恒 $P_f+2P_d=1$，$P_f=\cos^2(\alpha)$、$P_d=\sin^2(\alpha)/2$，仅由 $\alpha$ 决定 📜Q。
- **Bloch 能带方程**：$\psi_{out}=e^{-i\varphi_E}\hat S\psi_{in}$（$\varphi_E=\varepsilon L/\hbar v$）→ Bloch 定理 → $[\lambda-U_q]\bar\psi=0$，$\lambda=e^{i(\varphi_E-\varphi_T)}$ 📜Q。$U_q$（Eq. 10）= 离散演化算子，3 个特征值 $\lambda_{nq}$（$n=-1,0,1$）→ 3 条能带，周期 $\varepsilon_L$：$\varepsilon_q^{nm}=\varepsilon_L(\arg\lambda_{nq}/2\pi+\varphi_T/2\pi+m)$（Eq. 11）📜Q。$U_q$ 幺正且 $\det U_q=1$ → $\lambda_q^3-\mathrm{tr}[U_q]\lambda_q^2+\mathrm{tr}[U_q^\dagger]\lambda_q-1=0$（Eq. 12），能谱只依赖 $\mathrm{tr}[U_q]$（Eq. 13）→ **只依赖 $\alpha$**（相位 $\Theta_1,\Theta_2$ 经动量平移消除）📜Q。
- **无隙与 Dirac 点**：判别式 $D=27+4\mathrm{tr}[U_q]^3+\mathrm{tr}[U_q^\dagger]^3-18|\mathrm{tr}[U_q]|^2-|\mathrm{tr}[U_q]|^4=0$ 在 $\Gamma,K,K'$ 高对称点对任意 $\alpha$ 成立 → 无隙；Dirac 速度 $v_D=v/2$ 独立于 $\alpha$；Dirac 点间距 $k_D=4\pi/3L$ 📜Q。能量周期性是网络模型区别于标准紧束缚模型的**特征** 📜Q。图示取 $\alpha=1.1$（$P_f\approx0.2$、$P_d\approx0.4$；偏转更可能来自数值 [14]）📜Q[~]。
- **DoS**（每 valley/spin/Dirac 点，Fig. 4）：周期 $\varepsilon_D=\varepsilon_L/3$（为能带周期 $1/3$，反映单胞三链对称，"three times smaller than the period of the network band structure" 📜Q）；每周 1 零点（Dirac 点）+ 1 鞍点对数发散（van Hove）；标度 $\nu_L=3\pi/(\varepsilon_L L^2)$ 📜Q。

### 2.4 边界层（IV. Discussions）：regime 界定 + 对标 + 预言

- **regime 界定**：本文 = 位移场 + 小扭角（helical）；[52] = 无位移场 + 大扭角近公度（honeycomb 非螺旋），不同 regime 📜Q。
- **数值互验 [43]**：$\theta=0.2°$、$2u\approx180$ meV 时数值 DoS 峰间距 $\varepsilon_D\approx21$ meV；本文取 $v_\parallel\approx v$ 近似得 $\varepsilon_D\approx\varepsilon_L/3\approx20$ meV，"good agreement" 📜Q[~]——作者注明 [43] 工况不完全在本文 regime，$v_\parallel$ 公式不适用 📜Q。
- **实验对标 [42]**：$\theta=0.245°$、$L\approx58$ nm → $\varepsilon_L\approx72$ meV，与位移场能隙 $\varepsilon_g\approx60$ meV 同量级 → 模型**不完全适用**（隙内仅 1 峰）📜Q[~]。最大能隙 $\varepsilon_g\approx250$ meV（[53,54]）→ 模型广能量范围适用 📜Q[~]。
- **能标估计**：$w=400$ meV → helical 态速度 $v_\parallel=1.6\times10^6$ m/s > 石墨烯 $v=10^6$ m/s；网络周期 $\varepsilon_L\approx115$ meV、DoS 周期 $\varepsilon_D\approx38$ meV 📜Q[~]。
- **预言**：强位移场下 magic angle 行为缺席（"We predict that magic angle behavior is absent at strong displacement fields" 📜Q）；能带弱依赖 $\theta$（除能标 $\varepsilon_L$ 外，网络发育良好时）📜Q。

---

## 3. 结论清单（分层：定理 / 估算 / 预言）

> 理论论文的结论必须按**性质**分层，而非平铺——"定理式主张"受假设限定、"估算"是近似、"预言"是待验证。每条标：**依赖假设** + **可检验性**。

### 3.1 定理式主张（数学/拓扑论证的产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 畴壁通道数 | 跨壁谷陈数差 $C_{AB}-C_{BA}=2$ → 每 valley/spin 两条 helical 通道 | A1（局域近似）、A7（谷守恒） |
| 网络能带无隙 | 判别式 $D=0$ 在 $\Gamma,K,K'$ 对任意 $\alpha$ 成立 → 无隙 + Dirac 点 | A3、A4、三角对称 |
| Dirac 速度 | $v_D=v/2$，独立于 $\alpha$ | 同上 |
| DoS 周期 | $\varepsilon_D=\varepsilon_L/3$（三链对称），每周 1 零点 + 1 van Hove 发散 | 三角对称 |

### 3.2 估算（近似/对标，非严格定理）

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| $\varepsilon_L$（$\theta=0.245°$） | $\approx72$ meV（$L\approx58$ nm） | — | 📜Q[~] |
| $\varepsilon_g$（实验 [42] 位移场能隙） | $\approx60$ meV | — | 📜Q[~] |
| $\varepsilon_g$（最大能隙 [53,54]） | $\approx250$ meV | — | 📜Q[~] |
| $v_\parallel$（helical 态速度） | $1.6\times10^6$ m/s（$>v=10^6$ m/s，$w=400$ meV） | Eq. (7) | 📜Q[~] |
| $\varepsilon_L$（$w=400$ meV） | $\approx115$ meV | — | 📜Q[~] |
| $\varepsilon_D$（$w=400$ meV） | $\approx38$ meV | — | 📜Q[~] |
| $\varepsilon_D$（数值 [43]，$\theta=0.2°$、$2u\approx180$ meV） | $\approx21$ meV | — | 📜Q[~] |
| $\varepsilon_D$（$v_\parallel\approx v$ 近似） | $\approx\varepsilon_L/3\approx20$ meV | A3 | 📜Q[~] |
| $\alpha$（图示取值） | $1.1$（$P_f\approx0.2$、$P_d\approx0.4$） | — | 📜Q[~] |

### 3.3 预言（可检验性 → 见 §5.1）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| 强位移场下 magic angle 行为缺席 | "We predict" 📜Q | 中——后续位移场下实验 |
| 低能物理由螺旋网络模型描述 | "We show"（数学构造）+ "captured by" 📜Q | 中——DoS 周期峰、磁输运 |
| 网络模型解释 [43] 数值 DoS 峰 | "does seem to suggest"（建议性）📜Q | 中——需进一步数值验证 |

### 3.4 内部验证（自洽核对，非"排除竞争解释"）

理论论文没有数据可辨识性，但有**一致性核对**，本文三处：

1. **解析↔数值互验**：$\varepsilon_D\approx\varepsilon_L/3\approx20$ meV vs 数值 [43] $\approx21$ meV（"good agreement"）📜Q——但 [43] 工况不完全在本文 regime，$v_\parallel$ 公式不适用、需取 $v_\parallel\approx v$ 近似 📜Q。
2. **$\alpha$ 独立鲁棒性**：Dirac 点位置/能量、$v_D$ 均独立于 $\alpha$ → 拓扑性质鲁棒（推导）。
3. **对称性自检**：相位 $\varphi_T=\Theta_1=\Theta_2=(\pi-2\arcsin[3\sin\alpha/(2\sqrt2)])/3$ 保证节点 120° 离散旋转对称 📜Q。

### 3.5 概念区分（作者论证中的"分类"，非溯因排除）

| 区分 | 依据 | 结论 |
|---|---|---|
| 本文 regime vs [52] | 位移场 + 小扭角（helical）vs 无位移场 + 大扭角近公度（honeycomb 非螺旋）📜Q | 不同 regime 的网络模型 |
| 网络模型 vs 标准紧束缚模型 | 能量周期性来自网络离散演化算子相位，区别于标准紧束缚 📜Q | 网络模型特征能带 |
| helical vs chiral | 谷锁定反向传播（TR 连接两谷）vs 净手征（见 [PHY-BERRY]） | 本文是 helical |

> 注：这些是**概念/图景分类**（taxonomy），不是实验论文那种"数据排除竞争解释"（溯因排除）——理论论文没有后者。

---

## 4. 假设-结论依赖图（含金量所在）

> 理论论文三个月后最可能被引用的是"何时失效"，不是推导本身。本表把 §1.3 的每条假设映射到"失效方式 → 崩塌的结论 → 是否致命"。

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性（作者如何对待） |
|---|---|---|---|
| A4 唯象 S 矩阵（网络连通） | AA 节点微观散射非唯象 | 网络能带定量、$\alpha$ 值 | **致命**——网络连通性是核心假设，后被 T12 (TZM) 挑战（§5.3）📜Q+💭I |
| A3 单通道/链 | $\varepsilon_L\gtrsim w\sim u$ | 两 Dirac 锥散射不可忽略、单通道图景失效 | 局部——网络发育判据 A6 已界定 📜Q |
| A2 大位移场投影 | $\varepsilon_L\gtrsim u$ | 2-band 投影失效 | 局部——投影仅用于模型层，完整 4-band 仍有效 📜Q |
| A5 适用范围 $|\varepsilon|\ll u,w$ | 能量超出 AB/BA 能隙 | AA 堆叠区态进入、helical 非唯一自由度 | 致命——适用范围边界 📜Q |
| A6 网络充分发育 | 波函数重叠不可忽略（$w/\varepsilon_L$ 小） | 畴壁态交叠、网络图景失效 | 致命——发育判据 📜Q |
| A8 干净零温周期 moiré | 无序/温度/非均匀应变 | 能带/DoS 定量 | 未处理 💭I |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（本文预言的实验靶标）

- 网络能带 $\varepsilon(q)$（无隙 + Dirac 点 $v_D=v/2$）+ DoS $\nu(\varepsilon)$（周期振荡，$\varepsilon_D=\varepsilon_L/3\propto\theta$）📜Q；
- STM $dI/dV$ 多峰结构（DoS 周期峰）、磁输运网络 signature（[55]，作者 "can be addressed theoretically using the model developed in this work"）📜Q；
- 强位移场下无 magic angle（"We predict"）📜Q。

### 5.2 设计原则（网络模型适用 regime）

位移场（开隙 + 畴壁）+ 小扭角（$L$ 大、$\varepsilon_L$ 小、网络充分发育）→ 低能 = 螺旋网络；大位移场 $\varepsilon_L\ll u\sim w$ 📜Q。

### 5.3 后续文献修正（时间倒挂，💭I）

- **Tsim 2020（T12, TZM）**：推翻"连通网络"——AA 节点确定性散射、不渗流，部分修正本文网络图景。
- **De Beule 2020（T15）**：用散射相位统一重释（$\phi=0$=TZM / $\phi=\pi/2$=pLL 两极限）。
- **Hou 2024（T29, NQCP）**：裁决为独立 1D 通道 + 近量子化平台。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| AA 节点散射假设（网络连通） | 唯象 S 矩阵未从微观解出节点；网络连通性是核心假设，后被 T12 (TZM) 挑战 | 📜Q + 💭I |
| 唯象参数 $\alpha$ 未从微观确定 | $\alpha$ 由节点散射细节决定，本文未算（引 [51] 复杂依赖） | 📜Q |
| 未计无序/温度/非均匀应变 | 模型为干净、零温、周期 moiré 极限 | 💭I |
| 未处理 AA 堆叠区态 | 只处理 AB/BA 畴壁态（$|\varepsilon|\ll u,w$ 外失效） | 📜Q |
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
| Rickhaus 2018 [55] | 磁输运网络 signature（可被本文模型处理）📜Q |
| Pal, Spitz & Kindermann 2018 [52] | 非螺旋 honeycomb 网络（无位移场 + 大扭角近公度，不同 regime）📜Q |

> ⚠️ Phase S 外部对标（**非本文引用**，时间倒挂，💭I）见 §5.3；引用关系依据 `cards.md` Q2 卡片与 `appendix_B_theory.md` §B.2。

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

- **Q1（edge state 如何表征）**：本文是理论——表征方式 = 能带 $\varepsilon(q)$（无隙 + Dirac 点 $v_D=v/2$）+ DoS $\nu(\varepsilon)$（周期振荡）+ 色散 $\varepsilon_p=v_\parallel p_\parallel$；实验可验 = STM $dI/dV$ 多峰（$\varepsilon_D\propto\theta$）、磁输运 network signature 📜Q（§2/§3/§8）。
- **Q2（理论如何复现）**：本文即螺旋网络系统理论——连续模型→2-band 投影→Jackiw-Rebbi 模→AA 节点 S 矩阵→Bloch 能带；能谱只依赖 $\alpha$，DoS 周期 $\varepsilon_L/3$ 📜Q（§2/§3）。
- **Q3（理论↔实验对应）**：数值 [43] $\varepsilon_D\approx21$ meV ↔ 本文 $\approx20$ meV（"good agreement"）；实验 [42] $\varepsilon_L\approx72$ meV vs $\varepsilon_g\approx60$ meV（不完全适用，仅 1 峰）📜Q（§2.4/§3）。

> **增量价值**：本文是 `[PHY-MB]` 网络 miniband 的**解析母本**（能带能标 $\varepsilon_L=2\pi\hbar v/L$ + DoS 周期 $\varepsilon_L/3$），与 E12（实验 Δn=4/A、v_DW 提取）互为"理论解析 ↔ 实验反推"两端；report.md 理论侧引用其 $C_{AB}-C_{BA}=2$、$\varepsilon_L$、$\varepsilon_D=\varepsilon_L/3$ 与"强位移场无 magic angle"预言。比 E12 多的是：网络能带的**闭式色散**与 S 矩阵参数化；少的是：无实空间/输运数据（纯理论）。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` 提取正文到 `/tmp/T09.txt`（424 行），逐项 grep 核对：**全部数字/公式命中原文**——

| 数字 | grep 命中位置 | 结论 |
|------|--------------|------|
| $\varepsilon_L=2\pi\hbar v/L$ | §II | ✓ 📜Q |
| $L=a_0/[2\sin(\theta/2)]$、$k_D=4\pi/3a_0$ | §II | ✓ 📜Q |
| $C=\delta_-/|\delta_-|$、$C_{AB}-C_{BA}=2$ | §II | ✓ 📜Q |
| $\delta_\pm=(|T_{BA}|\pm|T_{AB}|)/2$ | §II | ✓ 📜Q |
| $v_\parallel\approx\delta_+/p_u\approx2wv/(3u)$ | Eq. (7) | ✓ 📜Q |
| $r_{\perp0}=L/2\sqrt3$、$\exp[-w/\varepsilon_L]$ | §II | ✓ 📜Q |
| $\alpha_M=\arccos[1/3]$、$P_f=\cos^2\alpha$、$P_d=\sin^2\alpha/2$、$P_f+2P_d=1$ | §III | ✓ 📜Q |
| $\chi=\arccos[\{3\cos^2\alpha-1\}/2\cos\alpha]$ | Eq. (9) | ✓ 📜Q |
| $\varepsilon_q^{nm}=\varepsilon_L(\arg\lambda_{nq}/2\pi+\varphi_T/2\pi+m)$ | Eq. (11) | ✓ 📜Q |
| $\lambda^3-\mathrm{tr}[U_q]\lambda^2+\mathrm{tr}[U_q^\dagger]\lambda-1=0$ | Eq. (12) | ✓ 📜Q |
| $D=27+4\mathrm{tr}[U_q]^3+\mathrm{tr}[U_q^\dagger]^3-18|\mathrm{tr}[U_q]|^2-|\mathrm{tr}[U_q]|^4=0$ | §III | ✓ 📜Q |
| $v_D=v/2$、$k_D=4\pi/3L$ | §III | ✓ 📜Q |
| $\varepsilon_D=\varepsilon_L/3$、$\nu_L=3\pi/(\varepsilon_L L^2)$ | §III/Fig.4 | ✓ 📜Q |
| $\alpha=1.1$、$P_f\approx0.2$、$P_d\approx0.4$ | §III | ✓ 📜Q |
| $\theta=0.2°$、$2u\approx180$ meV、$\varepsilon_D\approx21$ meV、$\approx20$ meV | §IV | ✓ 📜Q[~] |
| $\theta=0.245°$、$L\approx58$ nm、$\varepsilon_L\approx72$ meV、$\varepsilon_g\approx60$ meV | §IV | ✓ 📜Q[~] |
| $\varepsilon_g\approx250$ meV、$w=400$ meV、$v_\parallel=1.6\times10^6$ m/s、$v=10^6$ m/s、$\varepsilon_L\approx115$ meV、$\varepsilon_D\approx38$ meV | §IV | ✓ 📜Q[~] |
| "captured by a phenomenological helical network model"、"one zero and one divergence per period" | 摘要 | ✓ 📜Q |
| "We predict that magic angle behavior is absent" | §IV | ✓ 📜Q |

⚠️ 修正/降级：① arXiv:1803.06404 正文未出现 → 头部表已标"外部来源"。② 旧版 S 矩阵 $\begin{pmatrix}0&t&r\\r&0&t\\t&r&0\end{pmatrix}$、能带方程 $\cos(qL)=(1-2|t|^2)/2|t|^2$、"$\alpha=|t/r|$"、适用条件 "$|E|<\delta_+$" 均 grep 不到原文 → 已改为原文 Eq. 9/11/12、散射角度定义、$|\varepsilon|\ll u,w$（见更正日志）。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-06 | 初读（research_onboarding Phase 4 风格）：一句话总结 + 背景 + 方法模型 + 核心结果 + 公式速查 |
| 2026-08-20 | **能标公式修正（S-REV，§B.5#1）**：旧版 "DoS 周期 $\sim2\pi\hbar v/L$" 符号混乱 → 拆为能带能标 $\varepsilon_L=2\pi\hbar v/L$（$\theta=0.245°$、$L\approx58$ nm 时 ≈72 meV 📜Q，grep "72 meV"/"58 nm" ✓）与 DoS 周期 $\varepsilon_D=\varepsilon_L/3$（≈20 meV 📜Q）两个量；卡片旧版 "$E_\lambda=2\pi\hbar v/3\lambda$" 同源错误（实为 DoS 周期），已改 |
| 2026-09-02 | **按 4 块辨识结构整体重写**：头部字段表 + TL;DR 问题句式 + §1 系统辨识导览（黑箱三要素 + 四层变量表 + 理论版判别表 6 条 + [前提与限定]）+ §2 按论文三段 + §3 理论模型与方法 + §4 关键预言与数据 + §5–§9 + Phase S 接口 + 反向核对 pass |
| 2026-09-02 | **无源内容修正**：S 矩阵、能带方程、"$\alpha=|t/r|$"、适用条件 "$|E|<\delta_+$" 均 grep 不到原文 → 分别改为原文 Eq. 9（$\bar S$，$P_f=\cos^2\alpha/P_d=\sin^2\alpha/2$）、Eq. 11/12（$U_q$ 特征值问题）、散射角度定义、$|\varepsilon|\ll u,w$ + "below AB-BA gaps"；arXiv 号正文未出现 → 标外部来源 |
| 2026-09-08 | **按 5 块演绎结构整体重写**（应用户要求）。旧 4 块版归档 `archive/paper_review_T09_efimkin2018_prb.backup_20260908.md`。黑箱三要素/四层变量表/判别表/[前提与限定] → 拆为"模型白箱（连续模型+参数分册+8 条假设清单）"+"推导链（前提定理/模型/推导/边界四层）"+"结论清单（定理/估算/预言分层）"+"假设-结论依赖图"+"接口"；内部验证（§3.4）+ 概念区分（§3.5）取代判别表；删"反推量 θ̂"层（$v_\parallel$ 归入导出量+估算）。全部 📜Q 事实与数字无丢失。 |
