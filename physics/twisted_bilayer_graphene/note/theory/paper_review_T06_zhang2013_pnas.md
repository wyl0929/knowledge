<!--
 * @Author       : AI 精读 (五块演绎结构重写)
 * @Date         : 2026-08-06（初读）→ 2026-08-11（Phase S 补充）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T06_zhang2013_pnas.md
 * @Description  : T6: Zhang/MacDonald/Mele 2013 — 谷 Chern 数与带隙双层石墨烯边界模（理论 — 畴壁拓扑统一分类；2026-09-08 按 5 块演绎结构重写）
-->

# Paper Review: Zhang, MacDonald & Mele (2013) — 带隙双层石墨烯中的谷 Chern 数与边界模

| 字段 | 内容 |
|------|------|
| **编号** | T6 |
| **标题** | Valley Chern numbers and boundary modes in gapped bilayer graphene |
| **作者** | Fan Zhang, Allan H. MacDonald, Eugene J. Mele |
| **期刊** | PNAS 110, 10546–10551 (2013) |
| **DOI** | 10.1073/pnas.1308853110 |
| **类型** | 理论 — 畴壁拓扑分类统一框架（4/2 带连续模型 + 晶格数值 + 量子几何论证，无实验数据） |
| **课题组** | Zhang（UPenn）/ MacDonald（UT Austin）/ Mele（UPenn） |
| **PDF** | ✅ `reference/pdfs/Zhang 等 - 2013 - Valley Chern numbers and boundary modes in gapped bilayer graphene.pdf`（正文 6 页） |
| **精读日期** | 2026-08-06（初读）→ 2026-08-11（Phase S）→ 2026-09-08（5 块重写） |

> **结构说明**：按「理论论文演绎结构」五块记（`note/shared/method/theory_paper_reading.md` §3）。
> **共享知识引用**：谷 Chern 数/Berry 曲率 → `[PHY-BERRY]`；通道计数 → `[PHY-LB]`。

---

## TL;DR

**本文想解决的理论问题**：带隙双层石墨烯（BLG）中三类畴壁——层间电场反转墙（EFW）、层堆叠反转墙（LSW，AB↔BA）、两者同时反转的补偿墙——各自束缚何种边界模？能否用统一的谷 Chern 数语言分类？

**主结果**：① EFW 与 LSW **拓扑等价**：两者谷 Chern 数变化都是 $\Delta N_\nu=2\nu$（跨越两种墙），都束缚一对谷投影手征模 📜Q；② LSW 的拓扑转变由四带哈密顿量参数空间中**有限动量能隙闭合**（$q_x=\pm\sqrt{\Delta^2+\gamma^2/4}$，$q_y=0$，锥形闭合）标记，并给出 $\Delta$-$\mu$ 平面相图（Fig. 1）📜Q；③ **补偿墙**（电场+堆叠同时反转）$\Delta N_\nu=0$ → 同谷内两对反向传播模杂化、谱完全开隙、边界模湮灭（即使连续模型亦然）📜Q。

**结论/意义**：为理解 BLG 谷投影拓扑态及其在谷间散射下的命运提供**统一框架**——是畴壁物理的"罗塞塔石碑"（EFW/LSW 等价 + 补偿墙对照）。⚠️ 全文为理论论证，作者用词 demonstrate / conclude / identify，非实验事实。

---

## 1. 模型白箱（理想系统 + 假设清单）

### 1.1 哈密顿量（4 带，归一化）

基 $\Psi=(\psi_{AT},\psi_{BT},\psi_{AB},\psi_{BB})$（T/B = 顶层/底层，A/B 子格）。低能区在 $K,K'$ 附近 $H(\nu K+q)$，$\nu=\pm1$ 标 K/K'。$\sigma$ 作用于层内子格，$\tau$ 作用于层。$H=H_0+H_{int}$ 📜Q：

$$
H_0=\nu q_x\sigma_x\tau_0+q_y\sigma_y\tau_0,\qquad H_{int}=\frac{\gamma}{2}(\sigma_x\tau_x-\sigma_y\tau_y)\quad(\text{AB})
$$

- AB 堆叠（顶层 A 与底层 B 杂化）取 $H_{int}=\gamma(\sigma_x\tau_x-\sigma_y\tau_y)/2$；BA 取 $H_{int}=\gamma(\sigma_x\tau_x+\sigma_y\tau_y)/2$ 📜Q。
- $\gamma=\gamma_1/(\hbar v)$（原文 OCR 为 "$\gamma=\gamma_1/Zv$"，"Z" 疑为 $\hbar$；"energies are normalized by $\hbar v$"），$\gamma_1$ 为最近邻层间跃迁、$v$ 为单层电子速度 📜Q。
- 层间电势差 $V$ 加 $\Delta\sigma_0\tau_z$，$\Delta=V/(2\hbar v)$ 📜Q。

**约化 2 带模型**（$\gamma\gg\Delta$，消去 ±γ 高能自由度；Eq. [1]）📜Q：

$$
\tilde H_\nu=g_\nu(q)\cdot\tilde\sigma,\qquad g_\nu(q)=\left(-\frac{q_x^2-q_y^2}{\gamma},\ \frac{2\nu q_x q_y}{\gamma},\ \Delta\right).
$$

**推广 4 带（含堆叠序参数 $\mu$）**（Eq. [3]）📜Q：

$$
H_{LSW}=\Delta\tau_z+\nu q_x\sigma_x+q_y\sigma_y+\frac{\gamma}{2}(\sigma_x\tau_x-\mu\sigma_y\tau_y),
$$

$\mu\to1(-1)$ 回到 AB（BA）。

### 1.2 参数分册

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | $\Delta$（层间势差）、$\mu$（堆叠序，AB↔BA）、$\gamma$（层间耦合）、$\nu$（谷） |
| **导出量（由旋钮+常数算出）** | Berry 曲率 $\Omega_\nu(q)$、谷 Chern 数 $N_\nu=-\nu\,\text{sgn}(\Delta)$、$\Delta N_\nu$ |
| **模型内部量（解的性质）** | 边界模色散、相图、能隙闭合位置 |
| **固定常数** | $\gamma_1$（层间跃迁）、$v$（单层速度）、晶格参数 $t=1,\gamma_1=0.3$（数值例） |
| **预言量（可检验）** | EFW/LSW 各 2 手征模、补偿墙无模、LSW 3 模（晶格）、Landauer $Ne^2/h$ |

> 无"反推量 θ̂"层。**符号防混**：本文 $N_\nu=-\nu\,\text{sgn}(\Delta)$，与 **T2 Li 2010 的 $N_\nu=\nu\,\text{sign}(\Delta)$ 符号约定相反**——跨论文引用必须带各自约定。

### 1.3 显式假设清单

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **谷守恒（无谷间散射）**：$\Omega_\nu$ 在单个谷内积分需谷是好量子数 | 推导 | 📜Q |
| A2 | **低能连续近似**（$q$ 小，$\Delta$ 小） | 模型 | 📜Q |
| A3 | **$\gamma\gg\Delta$**（约化到 2 带） | 推导 | 📜Q |
| A4 | **单粒子**（无相互作用） | 模型 | 💭I（原文未讨论关联） |
| A5 | **谷 Chern 数本身是近似**："the introduction of a valley Chern number in this context is approximate"（未把全 BZ 映到 $H_\nu$ 参数空间）；仅当 $\Delta$ 小且无谷间散射时 $\Delta N_\nu$ 可解释为拓扑量（"gluing together" 两积分） | 推导 | 📜Q |
| A6 | **相同规范下计算两侧 $\Delta N_\nu$**（要求边界处 $m_{-1;\nu;\pm}=m_{1;\nu;\pm}$） | 推导 | 📜Q |

---

## 2. 推导链（演绎结构：顺论文顺序）

### 2.0 总览

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 前提定理层 | Two-Band Continuum Formulation | 4 带 $H_0+H_{int}$ | $g_\nu(q)$、$\Omega_\nu(q)$、$N_\nu=-\nu\,\text{sgn}\Delta$ | Berry 曲率（refs 13,14） | 谷守恒 |
| 模型层 | Layer Stacking Walls | $H_{LSW}(\mu)$ | $\Delta N_\nu=2\nu$（LSW） | 大 $q$ 相位扭转、规范 | 相同规范 |
| 推导层 | Phase Diagram | $\Delta$-$\mu$ 平面 | 相边界 $\Delta=0$、$\mu=0$；补偿墙 | 能隙闭合分析 | 4 带 |
| 边界层 | Fragility + 晶格 | 紧束缚晶格 | LSW 3 模、判据 Eq. 12/13 | 谷间散射/短程 | 原子尺度 |

### 2.1 前提定理层：2 带连续模型

- **输入**：AB 堆叠 4 带 $H_0+H_{int}$；$\gamma\gg\Delta$ 时消去 ±γ 高能自由度 → 2 带 $\tilde H_\nu=g_\nu(q)\cdot\tilde\sigma$（Eq. [1]）📜Q。
- Berry 曲率（Eq. [2]）📜Q：

$$
\Omega_\nu(q)=\frac{-2\nu\gamma\Delta\,q^2}{(q^4+\gamma^2\Delta^2)^{3/2}}.
$$

- 因 $\nu$ 依赖，$\Omega_\nu$ 全 BZ 积分为零 → 总 Chern 数 $N=0$（时间反演要求）；但单谷积分精确定义 → **谷 Chern 数 $N_\nu=-\nu\,\text{sgn}(\Delta)=\pm1$** 📜Q。
- EFW 跨墙 $\Delta N_\nu=\pm2$ → 一对谷投影边缘模沿边界同向传播 📜Q。

### 2.2 模型层：LSW 的拓扑（4 带必需）

- LSW（$\Delta$ 恒定、堆叠 AB↔BA）改变 $H_{int}$ 并切换低能子空间轨道 → 需 4 带分析（或用大 $q$ 相位扭转 + 规范论证）📜Q。
- 大 $q$（$q\gg|\Delta|,\gamma$）深填充带态 $\Psi_{\mu\nu}(q)$（Eq. [5]）在 LSW 两侧由规范变换关联（Eq. [8]）：$\Psi_{\mu;\pm}\mapsto e^{i\mu\nu(1-\tau_z)\phi}\Psi_{\mu;\pm}$，每层相位扭转不同 📜Q。
- 谷 Chern 数变化 $\Delta N_\nu=2\nu+m_{-1;\nu;+}+m_{-1;\nu;-}-m_{1;\nu;+}-m_{1;\nu;-}$（Eq. [7]），$m_{\mu\nu;\pm}$ 为整体相位 $\alpha_{\mu\nu;\pm}$ 的整数绕数；同规范下 $m$ 抵消 → $\Delta N_\nu=2\nu$ 📜Q。
- EFW 由 $\Delta$ 反号分析，经 $H_{LSW}(-\Delta,\mu)=\tau_x H_{LSW}(\Delta,-\mu)\tau_x$（Eq. [9]）与规范变换（Eq. [10]）得同样 $\Delta N_\nu=2\mu\nu$ 📜Q。**EFW 与 LSW 的边界模共同拓扑起源**（Fig. 3）📜Q。
- 2 带约化后 $g_\nu(q)=(-(q_x^2-q_y^2)/\gamma,2\mu\nu q_xq_y/\gamma,\Delta)$，Berry 曲率 $\Omega_\nu(q)=-2\mu\nu\gamma\Delta q^2/(q^4+\gamma^2\Delta^2)^{3/2}$（Eq. [11]）单谷积分 $=-\mu\nu\,\text{sgn}(\Delta)$ 📜Q。

### 2.3 推导层：相图与补偿墙

- **相图**（Fig. 1）：$\Delta$-$\mu$ 平面，相边界在 $\mu$ 轴与 $\Delta$ 轴（$H_{LSW}$ 在 $E=0$ 能隙闭合处）。$\Delta=0,\mu=1$ 是 $q=0$ 二次带接触（无隙 BLG）；$\Delta\neq0,\mu=0$ 在**有限动量** $q_x=\pm\sqrt{\Delta^2+\gamma^2/4}$（$q_y=0$）锥形闭合（$\sigma_x$ 为运动常数）📜Q。四条边界分隔四个不同带隙相（Fig. 1）📜Q。
- 当 $\mu\neq\pm1$，原二次带接触分裂成一对线性 Dirac 奇点，各携原绕数的一半 📜Q。
- **补偿墙（c）**：层堆叠与电场同时反转 → 连接两个不同但 $\Delta N_\nu=0$ 的体态 → 同谷两对反向传播模杂化、谱完全开隙（Fig. 3 Lower）📜Q。

### 2.4 边界层：晶格计算（短程/谷间散射）

- **输入**：最简单 LSW 晶格模型（Fig. 5，底层连续、顶层沿 zigzag 断裂）；**输出**：均匀带隙 BLG 与 EFW 各有 2 条 zigzag 边缘平带（Fig. 6A/B），而 **LSW 每谷出现 3 条（非 2 条）无隙模**（Fig. 6C）📜Q。
- 第三条来自断裂层晶界线 $B_T^{LI}$/$A_T^{RI}$ 的平带（magenta），当跨墙隧穿 $t_c$ 大于电场隙时平带下推到价带 → 成为第三条无隙模（Fig. 7：$t_c=0,0.2,0.6,1$）📜Q。
- **判据**（Eq. 12/13）——原子突变 LSW 中"脆弱"无隙模数目的能标层级判据 📜Q：

$$
U_{loc}-\frac{V}{2}<-\frac{\Delta_{gap}}{2}\quad[12],\qquad U_{loc}+\frac{V}{2}\pm t_c<-\frac{\Delta_{gap}}{2}\quad[13],
$$

（$\Delta_{gap}/2$ = 电场诱导隙之半，$V$ 超临界值后饱和）。晶格参数数值例 $t=1$、$\gamma_1=0.3$、$V/2=0.25$（Fig. 5–7）📜Q。
- **谷间散射的命运**：谷在体内非好量子数 → 无良定义不变量；边界破坏谷 → 无良控物理后果；强短程散射可 preempt 单谷保护 → 畴壁模数目可为 0–4 中任意整数（视 Eq. 12/13）📜Q。

---

## 3. 结论清单（分层：定理 / 估算 / 预言）

### 3.1 定理式主张（拓扑/几何论证产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 谷 Chern 数 | $N_\nu=-\nu\,\text{sgn}(\Delta)=\pm1$ | A1、A3 |
| EFW 跨墙变化 | $\Delta N_\nu=\pm2$ | A1 |
| LSW 跨墙变化 | $\Delta N_\nu=2\nu$（= $2\mu\nu$ 一般式） | A1、A6 |
| EFW↔LSW 等价 | 两墙束缚同手征结构、同数目边界模（Fig. 3） | A1 |
| 补偿墙 | $\Delta N_\nu=0$ → 边界模开隙湮灭 | A1 |

### 3.2 估算（数值/近似，非严格定理）

| 估算 | 值 | 证据 |
|---|---|---|
| LSW 能隙闭合位置 | $q_x=\pm\sqrt{\Delta^2+\gamma^2/4}$，$q_y=0$ | 📜Q[~] |
| 晶格参数 | $t=1$、$\gamma_1=0.3$、$V/2=0.25$（Fig. 5–7） | 📜Q[~] |
| 连续模型参数 | $\Delta=0.05$、$\gamma=0.1$（Fig. 2 caption） | 📜Q[~] |
| LSW 隧穿 | $t_c=0,0.2,0.6,1$（Fig. 7） | 📜Q[~] |
| LSW 无隙模数 | 每谷 3 条（晶格，非连续模型的 2） | 📜Q[~] |
| Landauer 电导 | 沿 LSW 无谷间散射可达 $Ne^2/h$（$N$ 每谷近完美透射通道数） | 📜Q[~] |

### 3.3 预言

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| STM 跨 LSW 时隙边缘 LDOS 的尖锐场诱导特征被色散畴壁模压制 | "should be suppressed" | 中——STM 可检 |
| 垂直电场下含单 LSW 样品的电导对样品取向/接触位置敏感 | "depends very sensitively on" | 中——输运可检 |

### 3.4 内部验证（自洽核对）

1. **4 带 ↔ 2 带互验**：LSW 用 4 带（大 $q$ 相位扭转）与 2 带约化（Eq. [11] 单谷积分 $=-\mu\nu\,\text{sgn}\Delta$）给出一致的 $\Delta N_\nu$ 变化 📜Q。
2. **连续 ↔ 晶格互验**：连续模型预言 LSW 每谷 2 模；晶格（无 $t_c$ 隧穿时，Fig. 7A）确给出 2 手征模 + 平带——平带是被连续模型漏掉的短程物理 📜Q。
3. **补偿墙负对照**：连续模型下补偿墙谱完全开隙（Fig. 3 Lower），与 EFW/LSW 的 2 模对照 📜Q。

### 3.5 概念区分（分类）

| 区分 | 依据 | 结论 |
|---|---|---|
| EFW vs LSW | $\Delta$ 反号 vs $\mu$ 反号 | 拓扑等价（$\Delta N_\nu=2\nu$），但 LSW 需 4 带才能看出 |
| 补偿墙 vs EFW/LSW | $\Delta N_\nu=0$ vs $2\nu$ | 补偿墙无保护模 |
| 谷 Chern 数（近似）vs 全 BZ Chern 数（严格） | 单谷非紧→紧映射 vs 全 BZ | 前者"approximate"，后者 $N=0$（TRS） |

---

## 4. 假设-结论依赖图（含金量所在）

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性 |
|---|---|---|---|
| A1 谷守恒 | 谷间散射（强短程/晶格尺度势） | 单谷保护被 preempt，畴壁模数 0–4 任意 | 作者明言"can be preempted entirely by sufficiently strong lattice-scale physics" 📜Q |
| A3 $\gamma\gg\Delta$ | 大 $\Delta$ | 2 带约化失效（需 4 带） | 边界明确 📜Q |
| A5 谷 Chern 数近似 | 谷非好量子数（体或边界） | 无良定义不变量/无良控物理后果 | "If [valley] is not [good quantum number] in the bulk, then there is no well defined topological invariant" 📜Q |
| A6 相同规范 | 边界两侧规范不一致 | $\Delta N_\nu$ 无意义 | 显式要求 $m_{-1;\nu;\pm}=m_{1;\nu;\pm}$ 📜Q |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（预言靶标）

- EFW/LSW 各 2 手征模、补偿墙无模（连续）；LSW 晶格 3 模（判据 Eq. 12/13）📜Q。
- STM 跨 LSW 的 LDOS 隙边缘特征被抑制；Landauer 电导 $Ne^2/h$（无谷间散射）📜Q。

### 5.2 设计原则

- **识别畴壁类型**：EFW 与 LSW 拓扑等价 → 可用统一框架；补偿墙无保护 → 非器件平台 📜Q。
- **谷是好量子数 + $\Delta$ 主导** 是畴壁模拓扑稳定的充要条件 📜Q（"gapless interface modes at a LSW are topologically stable when the potential difference between layers is the dominant energy scale and the valley index can be regarded as a good quantum number"）。

### 5.3 后续文献修正（时间倒挂，💭I）

- **T7 Vaezi 2013（PRX）**：本文 Note Added in Proof 引其为"complementary preprint"（ref 21），把 LSW 推广到 tilt boundary + SPT 分类。
- **T8 Jaskólski 2016（Nanoscale）**：本文"短程物理可 preempt 保护"的边界在真实缺陷（8-55）下的具体检验——发现拓扑态仍存活。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 谷 Chern 数是近似不变量 | 依赖谷守恒 + 小 $\Delta$ | 📜Q（"approximate"） |
| 短程物理非连续模型可及 | LSW 晶格出现 3 模（非 2） | 📜Q（"not captured in the continuum Hamiltonian"） |
| 单粒子 | 无相互作用 | 💭I |
| 谷间散射下模数不定 | 0–4 任意（视判据） | 📜Q |

## 7. 与其他工作的关系

| 工作 | 关系 |
|------|------|
| Martin, Blanter, Morpurgo 2008（ref 12，= T1） | 直接引用——EFW 束缚手征模的先驱（sharp EFW 解析解 + smooth $\Delta(r)$ 数值解）📜Q |
| Li et al. 2010（ref 15，= T2） | 引用——谷 Chern 数近似性（"marginal"）的先例 📜Q |
| Li et al. 2011 Nat. Phys.（ref 16） | 引用——子能隙电导拓扑起源 📜Q |
| Jung et al. 2011（ref 18，= T3） | 引用——多层谷霍尔 kink 态 📜Q |
| Qiao et al. 2011（ref 17，= T4） | 引用——$Ne^2/h$ 通道计数 📜Q |
| Vaezi et al. 2013（ref 21，= T7）/ Alden et al. 2013（ref 22） | Note Added in Proof——complementary preprint / 实验研究 📜Q |

## 8. 对后续研究的影响

- 建立"**谷 Chern 数统一分类**"——EFW/LSW 等价 + 补偿墙对照，成为后续所有畴壁实验（Ju 2015 LSW / Li 2016 EFW）的统一解释框架 📜Q→💭I。
- 揭示"连续模型漏掉短程物理"（LSW 3 模 vs 2 模）——为后续晶格/DFT 研究（T7/T8）设定问题 📜Q。

## 9. 理论模型映射（供计算对标）

| 映射 | 说明 |
|------|------|
| $g_\nu(q)=(-(q_x^2-q_y^2)/\gamma,2\nu q_xq_y/\gamma,\Delta)$ | cont.py 2 带模型 📜Q |
| $\Omega_\nu(q)=-2\nu\gamma\Delta q^2/(q^4+\gamma^2\Delta^2)^{3/2}$ | Berry 曲率（谷 Chern 数积分）📜Q |
| 晶格 $t=1,\gamma_1=0.3,V/2=0.25$、$t_c=0,0.2,0.6,1$ | tb.py LSW 复现参数锚点 📜Q |
| Eq. 12/13 判据 | 脆弱模数目的能标层级判据 📜Q |

---

## Phase S 目的接口（引用式，随项目增删）

- **Q1（edge state 如何表征）**：畴壁两侧 $\Delta N_\nu\neq0$ → 保护边界模；EFW/LSW 各 2 手征支/谷；补偿墙 $\Delta N_\nu=0$ → 无模 📜Q。
- **Q2（理论如何解释）**：谷 Chern 数统一分类——$\Delta N_\nu=2\nu$ 对 EFW/LSW 相同 → 支持同数边界模；晶格短程物理可增模（LSW 3 模）📜Q。
- **Q3（理论↔实验对应）**：三类畴壁明确预言——EFW/LSW 有通道、补偿壁无通道（可作对照）、模数随层数增加；为 Ju 2015 (EFW/LSW) 与后续实验提供统一框架 📜Q→💭I。

> **增量价值**：T2 的"$\Delta N_\nu$ 判据"落实为 EFW/LSW/补偿墙三类畴壁的显式分类 + 相图 + 晶格判据；比 T2 多了 LSW 的 4 带规范论证与相图。

## 反向核对 pass (2026-09-08)

`pdftotext -layout`+`-raw` 提取到 `/tmp/T06_layout.txt`/`T06_raw.txt`，逐项 grep 核对：

| 条目 | 命中位置 | 结论 |
|------|---------|------|
| $H_0=\nu q_x\sigma_x\tau_0+q_y\sigma_y\tau_0$、$H_{int}=\gamma(\sigma_x\tau_x-\sigma_y\tau_y)/2$ | Two-Band 节 | ✓ 📜Q |
| $g_\nu=(-(q_x^2-q_y^2)/\gamma,2\nu q_xq_y/\gamma,\Delta)$ | Eq. [1] | ✓ 📜Q |
| $\Omega_\nu=-2\nu\gamma\Delta q^2/(q^4+\gamma^2\Delta^2)^{3/2}$ | Eq. [2] | ✓ 📜Q |
| $N_\nu=-\nu\,\text{sgn}(\Delta)=\pm1$、$\Delta N_\nu=\pm2$（EFW） | Two-Band 节 | ✓ 📜Q |
| $H_{LSW}$（Eq. [3]）、$\Delta N_\nu=2\nu$（Eq. [7]） | LSW 节 | ✓ 📜Q |
| 有限动量闭合 $q_x=\pm\sqrt{\Delta^2+\gamma^2/4}$ | Phase Diagram 节 | ✓ 📜Q |
| 补偿墙 $\Delta N_\nu=0$、谱开隙 | Phase Diagram / Fig. 3 | ✓ 📜Q |
| 晶格 $t=1,\gamma_1=0.3,V/2=0.25$；LSW 3 模；$t_c=0,0.2,0.6,1$ | Fig. 5–7 | ✓ 📜Q |
| $\Delta=0.05,\gamma=0.1$ | Fig. 2 caption | ✓ 📜Q |
| 判据 Eq. [12][13]、Landauer $Ne^2/h$ | Fragility / Discussion | ✓ 📜Q |

⚠️ **修正/降级（相对旧版，重大跨论文污染清理）**：① 旧版"DFT-LDA（3.1 nm 宽畴壁, 1.5 nm 域, 5 V/nm 电场）"**全部来自 T7 Vaezi 2013，本文无 DFT**——已删除。② 旧版"SPT 分类：Wen 的框架"**来自 T7，本文无 SPT/Wen**——已删除。③ 旧版"LSW 紧束缚（t=2.8 eV, t⊥=0.4 eV, V=0.5 eV, 200 晶胞）"参数错（本文为无量纲 $t=1,\gamma_1=0.3,V/2=0.25$）——已改。④ 旧版"$\gamma=t_\perp/(\hbar v_F)^2$"与原文 "$\gamma=\gamma_1/\hbar v$"不符——按原文（OCR 标注 $\hbar$）改写。⑤ 补 LSW 晶格"3 模（非 2）"这一关键结果（旧版误写"各 2 条"）。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-06 | 初读（旧 5 节叙事版）。 |
| 2026-08-11 | Phase S 补充 Q2/Q3。 |
| 2026-09-08 | **按 5 块演绎结构整体重写**（应用户要求）。旧版归档 `archive/paper_review_T06_zhang2013_pnas.backup_20260908.md`。重大修正（跨论文污染清理）：① 删除 DFT-LDA 段（T7 污染）；② 删除 SPT/Wen 分类（T7 污染）；③ LSW 紧束缚参数改无量纲 $t=1,\gamma_1=0.3,V/2=0.25$；④ 补 LSW 晶格"3 模"关键结果；⑤ 符号约定 $N_\nu=-\nu\,\text{sgn}\Delta$ 与 T2 的差异显式标注。 |
