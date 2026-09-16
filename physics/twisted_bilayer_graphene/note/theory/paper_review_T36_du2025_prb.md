<!--
 * @Author       : AI 精读（白箱演绎结构）
 * @Date         : 2026-08-11（初读）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T36_du2025_prb.md
 * @Description  : T36: Du, Qi, Jiang & Xie 2025 PRB — 石墨烯 Josephson 结畴壁工程（2026-09-08 按 5 块演绎结构重写：模型白箱/推导链/结论清单/假设-结论依赖图/接口）
-->

# Paper Review: Du, Qi, Jiang & Xie (2025) — 石墨烯 Josephson 结中的畴壁工程

| 字段 | 内容 |
|------|------|
| **编号** | T36 |
| **标题** | Domain wall engineering in graphene-based Josephson junctions |
| **作者** | Xia'an Du, Junjie Qi, Hua Jiang*, X. C. Xie |
| **期刊** | Physical Review B 112, 184513 (2025)（Received 7 Sep / published 14 Nov 2025）📜Q |
| **DOI / arXiv** | 10.1103/PhysRevB.112.184513（⚠️ 摘要页印刷 "10.1103/2w2b-rq7l" 为模板占位符，按刊卷/文号标准 DOI 标注）/ arXiv:2509.02082（⚠️ 外部来源，正文未出现） |
| **类型** | 理论 — 石墨烯 Josephson 结畴壁工程（紧束缚 + Nambu BdG + Keldysh/Matsubara，无实验数据） |
| **课题组** | Hua Jiang（Fudan）/ X. C. Xie（Peking Univ.） |
| **PDF** | ✅ `reference/pdfs/Du 等 - 2025 - Domain wall engineering in graphene-based Josephson junctions.pdf`（正文 12 页） |
| **精读日期** | 2026-08-11（初读）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」的五块记（见 `note/shared/method/theory_paper_reading.md` §3）。理论论文无黑箱、无反推、无可辨识实验，故不用"四层变量表 + 判别表"。
> **共享知识引用**：拓扑 kink 态 / 谷 Chern 数见 `[PHY-BERRY]`；Josephson/Andreev/Fraunhofer 见 `[PHY-LB]`。⚠️ 本文是**超导畴壁工程**（非拓扑边缘输运主叙事），Scope Out 定位——仅需知道"存在"，§5.3 对标 T31。

---

## TL;DR

**本文想解决的问题**：把畴壁（DW）拓扑 kink 态作为超流通道引入石墨烯 Josephson 结，问：能否用 DW 的**数目、对称性、几何**三条策略调控临界电流对外场/相位的响应，从而超越"超流被限制在样品边缘"的传统拓扑 JJ 局限？

**主结果**（全文无实验数据，为紧束缚 + BdG + Keldysh/Matsubara 数值）：① **DW 数目工程**：$I_c$-$B$ 干涉图案随 DW 数从 AB 振荡连续演化到 Fraunhofer 衍射（0 DW → Fraunhofer、2 DW → 周期 ~3Φ₀ 的正弦、1 DW → 对 B 不敏感、NDW=19 → 类 Fraunhofer），复现 Barrier 2024（Nature 628, 741）观测，并给磁强计灵敏度增强的设计 📜Q；② **DW 对称性工程**：非对称（一 DW 倾斜）构型 + 磁场 → **理想 Josephson 二极管**，$I_c^+=0.405$ µA、$|I_c^-|=0.656$ µA、效率 η≈−24% 📜Q；③ **DW 几何工程**：交叉 DW（单交叉/双交叉环）实现**可控超流分流**，分流比由交叉角 α、磁场、超导相位差调控（α=0.2π 时 $I_2/I_1=0.895$、$I_3/I_1=0.100$、$I_4/I_1=0.005$）📜Q。

**结论/意义**：作者表态 "we propose three DW engineering strategies"、"establish a versatile platform for next-generation quantum devices"——把"畴壁工程"确立为石墨烯超导器件的新设计范式（磁强计/二极管/分流器）。⚠️ 全文为理论预言 + 数值（"we theoretically investigate / propose"），非实验证实；DW 起源（栅压/交错势）与 Barrier 2024（扭角堆垛畴界）不同但物理一致。

---

## 1. 模型白箱（理想系统 + 假设清单）

### 1.1 模型：Nambu 紧束缚 + 畴壁 staggered 势 + Keldysh 超流

**总哈密顿**（Eq. (1)）：$H=H_C+\sum_{l=L,R}H_l+H_T$——$H_C$ 中心区（含 DW）、$H_l$ 超导引线、$H_T$ 隧穿 📜Q。Nambu 表象含电子/空穴激发 📜Q。

**单层中心区**（Eq. (2)）：$H_C^{mono}=\sum\langle i,j\rangle\Psi_i^\dagger\begin{pmatrix}t_{ij}&0\\0&-t_{ij}^*\end{pmatrix}\Psi_j+H.c.+\sum_i\Psi_i^\dagger\begin{pmatrix}U_i&0\\0&-U_i\end{pmatrix}\Psi_i$，$t_{ij}$ 最近邻跳迁、$U_i$ on-site 势含 DW 结构信息 📜Q。**DW 构造**：单 DW 时，DW 上方 A(B) 子格 $U_i=+(-)V_{stag}$、下方 $U_i=-(+)V_{stag}$；$U_i$ 变号诱导拓扑保护 kink 态（引 ref 60）📜Q。

**超导引线**（Eq. (3)）：s 波，序参量 $\Delta e^{i\theta_l}$（θl 为引线 l 相位）；配对势 Δ=10 meV、on-site $U_S\approx-1.2$ eV、化学势 μ=0（此选择下引线对 Δ=0 保持金属、Δ≠0 变 s 波超导）📜Q。隧穿 $H_T$（Eq. (4)）📜Q。

**双层（Bernal）**：中心区加层间耦合（Eq. (5)）$H_C^{bi}=H_C^{mono,1}+H_C^{mono,2}+\sum\langle i_1,i_2\rangle\Psi_{i_1}^\dagger\begin{pmatrix}t_\perp&0\\0&-t_\perp\end{pmatrix}\Psi_{i_2}+H.c.$，$t_\perp=-0.4$ eV（仅垂直对齐原子）📜Q。DW 构造：层 1 上/下 $U_i=+(-)V_{stag}$、层 2 上/下 $U_i=-(+)V_{stag}$ 📜Q。

**磁场**：垂直场经 Peierls 替换 $t_{ij}=t e^{i\frac{e}{\hbar}\int A\cdot dl}$，规范 $A=(-yB,0,0)$，跳迁参数 $t=-2.75$ eV 📜Q。

**超流**（Eqs. (7),(8)）：Keldysh Green 函数 → 能量积分换 Matsubara 求和 $I=\frac{ieT}{\hbar}\sum_n\mathrm{Tr}[\tau_z(G_{CC}(i\omega_n)\Sigma(i\omega_n))^<-\cdots]$，Matsubara 频率 $\omega_n=(2n+1)\pi T$、$T=\Delta/10$、$k_B=1$ 📜Q。

### 1.2 参数分册（区分"作者设定" vs "推导所得"）

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | DW 数 $N_{DW}$、DW 排列（对称/倾斜）、交叉角 α、磁场 B、超导相位 θ、$V_{stag}$（±0.8/±1 eV） |
| **导出量（由旋钮+常数算出）** | 磁通量子 $\Phi_0=h/2e$、DW 间包围的磁通比例、Fourier 超流分布 $J_S(y)$ |
| **模型内部量（解的性质）** | $I_c$-$B$ 曲线、电流-相位关系、分流比 $I_k/I_1$、二极管效率 η |
| **固定常数** | $t=-2.75$ eV、$t_\perp=-0.4$ eV、Δ=10 meV、$U_S\approx-1.2$ eV、μ=0、$T=\Delta/10$ |
| **预言量（可检验）** | AB→Fraunhofer 演化、二极管 η≈−24%、分流比、磁强计分辨率 |

> 无"反推量 θ̂"层——纯理论，参数为标准石墨烯/超导数值。**符号防混**：θ（超导相位差）≠ θ（扭角，本文无扭角）；Δ（超导配对势 10 meV）≠ ΔB（半高全宽磁通）；$U_S$（引线 on-site）≠ $U_i$（中心区 on-site 势）；α（交叉角）≠ 本文无其他 α。

### 1.3 显式假设清单（本文结论的前提集合）

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **Nambu BdG + s 波配对**描述超导 | 模型 | 📜Q |
| A2 | **拓扑 kink 态是超流通道**（$U_i$ 变号诱导） | 模型 | 📜Q（引 ref 60） |
| A3 | **单粒子 BdG**（无关联/无序） | 模型 | 💭I（原文未讨论关联） |
| A4 | **有限尺寸数值**（Nx=41–141、Ny=60–306） | 算例 | 📜Q |
| A5 | **kink 通道独立于材料细节**（单层↔双层相似 → 后续聚焦单层） | 推导 | 📜Q（"largely independent of the specific material details"） |
| A6 | **相相干 + Matsubara 求和**（$T=\Delta/10$、$k_B=1$） | 推导 | 📜Q |

> 判别性扫轴：$N_{DW}$（0–19）、B/Φ₀、α（0.2π/0.37π）、θ、$V_{stag}$——均为计算扫参。这些假设在 §4 逐一映射到"失效 → 结论崩塌"。

---

## 2. 推导链（演绎结构：顺论文顺序，每步"输入→输出→所用假设/定理→合法域"）

### 2.0 总览

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 前提定理层 | Introduction | 拓扑 JJ 边缘限制 + Barrier 2024（ref 29） | 畴壁工程动机 | kink 态（refs 23–26） | — |
| 模型层 | Sec II | Nambu 哈密顿 + DW | kink 态 = 超流通道 | A1、A2 | 单/双层 |
| 推导层 | Sec III-A 数目 | $I_c$-$B$ 数值 | AB→Fraunhofer 演化 + 幂律 | A3、A4 | 数值 |
| 推导层2 | Sec III-B/C 对称/几何 | 倾斜 DW / 交叉 DW | 二极管 + 分流 | A3、A4 | 数值 |
| 边界层 | Sec IV | 三策略汇总 | 器件设计原则 | — | — |

### 2.1 前提定理层（引言）

- 拓扑 JJ 超流被限制在边缘（ref 22）→ 临界电流与空间分布可调性受限；畴壁工程在体内构建拓扑通道（refs 23–26）是出路 📜Q。
- **Barrier 2024（ref 29）**：MTBG 拓扑 JJ，体内 0–10+ 条 DW，$I_c$-$B$ 图案随 DW 数变化——但缺理论框架（第一问）📜Q。MTBG 需高精度扭角控制、DW 数难预定（refs 30–33）→ 需替代 DW 方案（第二问）：双层石墨烯双栅电压写/擦 DW（refs 26,34–40）、单层石墨烯 staggered 子格势 DW（refs 42–47）📜Q。

### 2.2 模型层：Nambu 哈密顿 + 畴壁（Sec II）

- $H_C$（Eq. (2)）+ 超导引线（Eq. (3)）+ 隧穿（Eq. (4)）；双层加层间耦合（Eqs. (5),(6)）📜Q。
- DW 构造（$U_i$ 变号）→ kink 态（Fig. 1(b)/(d) 红曲线 = 体隙内导电通道）📜Q。
- 磁场经 Peierls 替换进跳迁项；超流经 Keldysh + Matsubara（Eqs. (7),(8)）📜Q。

### 2.3 推导层：DW 数目工程（Sec III-A）

- **0 DW**：中心区金属 → **Fraunhofer 衍射**，旁瓣特征宽 ~$\Phi_0=h/2e$（Figs. 2(a),(d)）📜Q。
- **1 DW**：无额外通道 → 干涉被抑制 → **$I_c$ 对 B 不敏感**（Figs. 2(b),(e)，ref 29 一致）📜Q。
- **2 DW**：通道间干涉 → 正弦振荡，周期 ~3Φ₀（总磁通的 1/3 被两 DW 包围 → 有效周期 Φ₀，ref 74）📜Q。
- **3 DW**：一个次级峰在 4Φ₀ 内；**5 DW**：三个次级峰在 6Φ₀ 内 → 每条附加 DW 贡献一个次级峰；**19 DW** → 类 Fraunhofer（Fig. 2(i)）📜Q。
- **Fourier 分析**：$I_c(\beta)=|\int_{-W/2}^{W/2}dy J_S(y)e^{i\beta y}|$（$\beta=2\pi BL/\Phi_0$）→ $J_S(y)$ 的峰数与位置与 DW 吻合 → 超流由 kink 态承载（Fig. 3）📜Q。
- **磁强计**：$\Delta B$（半高全宽）随 $N_{DW}$ 幂律，log-log 斜率 **−1.13**（vs ref 81 理论 −1.25）→ 增 $N_{DW}$ 提高分辨率（Fig. 4）📜Q。

### 2.4 推导层2：DW 对称性工程 → Josephson 二极管（Sec III-B）

- 两 DW、一条倾斜 → 破反演对称；+ 垂直场（已破时间反演）→ JDE 条件（refs 58,82）📜Q。
- 非对称超流分布（Fig. 5(b)）→ $I_c^+\neq|I_c^-|$；$I_c^+=\max_\theta I(\theta)$、$I_c^-=\min_\theta I(\theta)$ 📜Q。
- 最优场下 $\Delta I_c\sim0.25$ µA、$I_c^+=0.405$ µA、$|I_c^-|=0.656$ µA → 效率 $\eta=(I_c^+-|I_c^-|)/(I_c^++|I_c^-|)\approx-24\%$ 📜Q。

### 2.5 推导层2'：DW 几何工程 → 超流分流（Sec III-C）

- **单交叉**（两余弦 DW 交于角 α）：零场下 $I_k/I_1$（k=2,3,4）与相位 θ 无关；α=0.2π 时 $I_2/I_1=0.895$、$I_3/I_1=0.100$、$I_4/I_1=0.005$，满足守恒 $I_2/I_1+I_3/I_1+I_4/I_1=1$ 📜Q。小 α → 反射主导（$I_3/I_1\approx1$，DW 靠近增强层间跳迁）；大 α → 透射主导（$I_2/I_1\to1$）📜Q。
- **双交叉**（DW 环）：超流沿环两路径获不同相位（磁通 + 相位差）→ 干涉调分流；$I_1$（总注入）周期振荡、$I_2$（反射主导、窄交替条纹）、$I_3$（透射主导、宽条纹），由 $(B/\Phi_0,\theta)$ 调控（Fig. 7）📜Q。

---

## 3. 结论清单（分层：定理 / 估算 / 预言）

### 3.1 定理式主张（Nambu 模型/干涉论证的产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| kink 态 = 超流通道 | $U_i$ 变号 → 体隙内 kink 态载超流 | A2 |
| 干涉起源 | $I_c$-$B$ 图案 = DW 间磁通干涉（$J_S(y)$ Fourier 还原） | 相相干（A6） |
| 材料无关性 | 单层/双层 kink 态输运特征一致 | A5 |

### 3.2 估算（数值算例，非严格定理）

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| 跳迁/耦合/隙 | $t=-2.75$ eV、$t_\perp=-0.4$ eV、Δ=10 meV、$U_S\approx-1.2$ eV | A1 | 📜Q[~] |
| 磁通量子 | $\Phi_0=h/2e$ | 定义 | 📜Q[~] |
| ΔB 幂律斜率 | −1.13（vs 理论 −1.25，ref 81） | A4 | 📜Q[~] |
| 二极管效率 | η≈−24%（$I_c^+=0.405$ µA、$|I_c^-|=0.656$ µA、$\Delta I_c\sim0.25$ µA） | A3、A4 | 📜Q[~] |
| 单交叉分流比 | $I_2/I_1=0.895$、$I_3/I_1=0.100$、$I_4/I_1=0.005$（α=0.2π） | A4 | 📜Q[~] |

### 3.3 预言（可检验性 → 见 §5.1）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| AB→Fraunhofer 连续演化（复现 Barrier 2024） | "reproducing experimental observations" 📜Q | 中——超导输运 |
| 理想 Josephson 二极管（η≈−24%） | "yields an ideal Josephson diode" 📜Q | 中——非互易输运 |
| 可控超流分流（α/B/θ 调） | "enable controllable supercurrent splitting" 📜Q | 中——多端超导 |

### 3.4 内部验证（自洽核对，非"排除竞争解释"）

1. **复现实验**：$N_{DW}=1$ 对 B 不敏感、$N_{DW}=2$ AB 振荡 ↔ Barrier 2024 观测（ref 29）一致 📜Q。
2. **单/双层互验**：单层与双层结果相似 → 材料无关（A5）、聚焦单层降成本 📜Q。
3. **Fourier ↔ DW 位置互验**：$J_S(y)$ 峰数/位置与 DW 吻合（Fig. 3）→ 超流由 kink 态承载 📜Q。
4. **幂律对标**：−1.13 vs 理论 −1.25（ref 81）接近 → 数值自洽 📜Q。

### 3.5 概念区分（作者论证中的"分类"，非溯因排除）

| 区分 | 依据 | 结论 |
|---|---|---|
| AB 振荡 vs Fraunhofer 衍射 | 通道干涉 vs 体金属连续传导 📜Q | 随 DW 数连续过渡 |
| 单层（交错势）vs 双层（栅压）DW | 起源不同，物理相同 📜Q | kink 态材料无关 |
| 反射主导 vs 透射主导 | 小 α（DW 近、层间跳迁强）vs 大 α 📜Q | 分流比机制 |
| 体 vs 边缘超流 | 本文 DW 在体内 vs 传统拓扑 JJ 边缘（ref 22）📜Q | 突破边缘限制 |

> 注：这些是**概念/图景分类**（taxonomy），不是实验论文那种"数据排除竞争解释"（溯因排除）——理论论文没有后者。

---

## 4. 假设-结论依赖图（含金量所在）

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性（作者如何对待） |
|---|---|---|---|
| A2 kink 态载超流 | DW 处无序/退相干破坏 kink 态 | 超流通道图景 | 未讨论无序 💭I |
| A3 单粒子 | 关联（虽石墨烯非魔角） | 定量 η、分流比 | 未讨论 💭I |
| A5 材料无关 | 双层 DW 构型复杂化 | 单层结论推广到双层的定量 | 作者证单/双层相似 📜Q |
| A4 有限尺寸 | 有限尺寸效应（Fig. 6(c) 涨落） | 分流比定量 | 作者明言涨落归有限尺寸 📜Q |
| A1 s 波 BdG | 非 s 波/拓扑超导 | 超流机制 | 未讨论 💭I |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（本文预言的实验靶标）

- $I_c$-$B$ 的 AB→Fraunhofer 演化（vs Barrier 2024）📜Q；
- Josephson 二极管非互易（$I_c^+\neq|I_c^-|$，η≈−24%）📜Q；
- 多端超流分流比（α/B/θ 调控）📜Q。

### 5.2 设计原则（畴壁工程三策略）

数目（$N_{DW}$ 控 $I_c$-$B$ 图案与磁强计分辨率）+ 对称性（倾斜 DW 破反演 → 二极管）+ 几何（交叉角 α → 分流比）📜Q。

### 5.3 后续文献修正（时间倒挂，💭I）

- **Barrier 2024（ref 29）**：本文理论复现其观测（DW 数 → $I_c$-$B$ 图案）💭I。
- **T31 Kundu 2024**：同属"石墨烯超导畴壁"线——T31 网络散射（ZZ/PLL）vs 本文紧束缚 kink 态，互补 💭I。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 偏离核心叙事 | 超导畴壁（非拓扑边缘输运主叙事）——Scope Out | 💭I |
| 无无序/退相干 | kink 态对无序稳健性未测 | 💭I |
| 有限尺寸涨落 | 分流比曲线涨落归有限尺寸（Fig. 6(c)） | 📜Q |
| DW 起源与实验不同 | 栅压/交错势 vs Barrier 2024 扭角堆垛畴界（作者论证物理相同） | 📜Q |

## 7. 与其他工作的关系（跨论文对标放这里，不放正文）

| 工作 | 关系 |
|------|------|
| Barrier 2024 Nature 628, 741（ref 29） | **直接对标**——本文理论复现其 DW 数 → $I_c$-$B$ 图案观测 📜Q |
| Martin 2008（ref 23）、Ju 2015（ref 24）、Huang 2024（ref 26） | 引用——畴壁拓扑 kink 态先驱/栅压写擦 DW 📜Q |
| Zhang/MacDonald/Mele 2013（ref 32，间接） | 引用——valley Chern 畴壁模背景 📜Q |
| 二极管文献（refs 58,82–91） | 引用——JDE 的破反演+破时间反演条件与实验（NiTe2/InSb）📜Q |

> ⚠️ Phase S 外部对标（非本文引用，时间倒挂，💭I）见 §5.3。

## 8. 对后续研究的影响

- 确立**畴壁工程**（数目/对称性/几何）为石墨烯超导器件设计范式（磁强计/二极管/分流器）📜Q。
- 给 Barrier 2024 观测提供理论框架（AB→Fraunhofer 演化 + Fourier 还原）📜Q。
- 与 T31 共同构成"石墨烯超导畴壁"研究线（网络散射 vs 晶格 kink）💭I。

## 9. 理论模型映射（供 TBPM / 计算对标）

| 映射 | 说明 |
|------|------|
| Nambu 哈密顿 → 紧束缚 | Eq. (2)：$t=-2.75$ eV、$U_i=\pm V_{stag}$、Δ=10 meV、$U_S\approx-1.2$ eV 📜Q |
| DW → 势构型 | staggered 子格势变号（单层）/ 层间交错（双层）📜Q |
| 磁场 → Peierls | $A=(-yB,0,0)$、$t_{ij}=t e^{i\frac{e}{\hbar}\int A\cdot dl}$ 📜Q |
| 超流 → Keldysh/Matsubara | Eqs. (7),(8)：$\omega_n=(2n+1)\pi T$、$T=\Delta/10$ 📜Q |
| 分流 → 多端构型 | 单交叉（α）/ 双交叉环（B/θ 调）📜Q |

> 与 TBPM/Kubo 对应：本文是紧束缚 BdG + Keldysh/Matsubara，可对标计算"kink 态超流 + $I_c$-$B$ 干涉"；复现需实现 staggered 子格势 DW + 超导引线自能 + Matsubara 超流 💭I。⚠️ 属 Scope Out（超导畴壁，非拓扑边缘输运主叙事）。

---

## Phase S 目的接口（引用式，随项目增删）

- **Q1（edge state 如何表征）**：本文是理论，无实验表征；预言 = $I_c$-$B$ 图案（AB/Fraunhofer）+ 二极管非互易 + 分流比 📜Q（§2.3–2.5）。
- **Q2（理论如何解释）**：DW kink 态 = 体内超流通道；数目/对称性/几何三策略调控 $I_c$ 对外场/相位响应 📜Q。
- **Q3（理论↔实验对应）**：$N_{DW}$ ↔ Barrier 2024 观测；非互易 ↔ Josephson 二极管实验；分流比 ↔ 多端超导器件 📜Q。

> **增量价值**：Scope Out 定位——超导畴壁需独立调研；提供 Barrier 2024 的理论框架 + 与 T31 的分工（晶格 kink vs 网络散射）。旧版无源"$I_c(\phi)$ 锯齿形、ZBCP、Majorana 信号"（grep "sawtooth"=0、"ZBCP"=0）已删。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` 提取正文到 `/tmp/T36.txt`（760 行），逐项 grep 核对：**全部数字/专名命中原文**——

| 数字/专名 | grep 命中位置 | 结论 |
|------|--------------|------|
| t=−2.75 eV、t⊥=−0.4 eV | Sec II | ✓ 📜Q[~] |
| Δ=10 meV、US≈−1.2 eV、μ=0 | Sec II | ✓ 📜Q[~] |
| Vstag=±0.8 eV（3 处）、±1 eV（3 处） | Fig. captions | ✓ 📜Q[~] |
| Φ0=h/2e | Sec III-A | ✓ 📜Q |
| 斜率 −1.13（2 处）、理论 −1.25 | Sec III-A | ✓ 📜Q[~] |
| ΔIc~0.25 µA、Ic+=0.405 µA、|Ic−|=0.656 µA、η≈−24%（2 处） | Sec III-B | ✓ 📜Q[~] |
| I2/I1=0.895、I3/I1=0.100、I4/I1=0.005、α=0.2π、α=0.37π | Sec III-C | ✓ 📜Q[~] |
| Fraunhofer（10 处）、diode（21+1 处）、Aharonov-Bohm（2 处）、kink state（19 处） | 全文 | ✓ 📜Q |
| Nx=61/41/101/141、Ny=80/84/60/160/306/168 | Fig. captions | ✓ 📜Q[~] |

⚠️ 修正/降级：① **DOI 异常**：摘要页印刷 "10.1103/2w2b-rq7l" 为模板占位符（非标准 DOI），头部表按刊卷 PRB 112, 184513 标标准 DOI 并注明。② arXiv:2509.02082 正文未出现 → 头部表已标"外部来源"。③ 旧版"$I_c(\phi)$ 锯齿形、ZBCP、Majorana 信号"无源（grep "sawtooth"=0、"ZBCP"=0，Majorana 仅引言动机 grep=2）→ 已删，改为三条 DW 工程策略。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-20 | **§1–§3 重写**：旧版 "$I_c(\phi)$ 锯齿形、ZBCP/Majorana 信号" 无源（grep "sawtooth"=0、"ZBCP"=0；Majorana 仅为引言动机 grep=2）→ 改为原文三条 DW 工程策略: (i) 数目工程 AB→Fraunhofer（复现 Barrier 2024 Nature 628, 741）(ii) 对称性工程 → Josephson 二极管 (iii) 几何工程 → 超流分流。依据 §B.5#29。 |
| 2026-09-08 | **按 5 块演绎结构整体重写**（应用户要求）。旧叙事版归档 `archive/paper_review_T36_du2025_prb.backup_20260908.md`。新增：模型白箱（Nambu 哈密顿 Eqs.(1)–(8) + 参数分册 + 6 条假设清单）、推导链（前提定理/模型/数目/对称/几何五层）、结论清单（定理/估算/预言分层）、假设-结论依赖图、接口。全部 📜Q 事实与数字无丢失；DOI 模板占位符异常已标注。 |
