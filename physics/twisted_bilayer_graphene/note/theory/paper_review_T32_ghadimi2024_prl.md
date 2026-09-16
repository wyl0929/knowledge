<!--
 * @Author       : AI 精读（白箱演绎结构）
 * @Date         : 2026-08-11（初读）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T32_ghadimi2024_prl.md
 * @Description  : T32: Ghadimi, Mondal, Kim & Yang 2024 PRL — 零 Berry 曲率量子谷霍尔效应（2026-09-08 按 5 块演绎结构重写：模型白箱/推导链/结论清单/假设-结论依赖图/接口）
-->

# Paper Review: Ghadimi, Mondal, Kim & Yang (2024) — 无 Berry 曲率的量子谷霍尔效应

| 字段 | 内容 |
|------|------|
| **编号** | T32 |
| **标题** | Quantum Valley Hall Effect without Berry Curvature |
| **作者** | Rasoul Ghadimi, Chiranjit Mondal, Sunje Kim, Bohm-Jung Yang* |
| **期刊** | Physical Review Letters 133, 196603 (2024)（Received 2 Apr / published 7 Nov 2024）📜Q |
| **DOI / arXiv** | 10.1103/PhysRevLett.133.196603 / arXiv:2403.15050（⚠️ arXiv 号外部来源，正文未出现） |
| **类型** | 理论 — 零 Berry 曲率（ZBC）QVHE，由谷欧拉数（VEN）保护（紧束缚 + DFT，无实验数据） |
| **课题组** | Bohm-Jung Yang group（Seoul National Univ. CTP + Inst. Applied Physics） |
| **PDF** | ✅ `reference/pdfs/Ghadimi 等 - 2024 - Quantum Valley Hall Effect without Berry Curvature.pdf`（正文 7 页 + SM：TB 推导/边缘模/TBG/反铁磁/DW 稳定性/DFT） |
| **精读日期** | 2026-08-11（初读）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」的五块记（见 `note/shared/method/theory_paper_reading.md` §3）。理论论文无黑箱、无反推、无可辨识实验，故不用"四层变量表 + 判别表"。
> **共享知识引用**：valley Chern 数 / Berry 曲率 / 螺旋 vs 手征见 `[PHY-BERRY]`。⚠️ 本文核心是**谷欧拉数（VEN）**——欧拉曲率（非 Berry 曲率）的谷内积分，是"第二类拓扑"（Euler class）而非 Chern class，§2.3/§7 显式区分。

---

## TL;DR

**本文想解决的问题**：能否在 **Berry 曲率处处严格为零**（ZBC）的体系中仍有受拓扑保护的畴壁态？即：挑战"谷 Chern 数 ≠ 0 → 畴壁态"的标准范式，提出由**谷欧拉数（VEN）**保护的零 Berry 曲率 QVHE？

**主结果**（全文无实验数据，为对称性论证 + TB/DFT 数值）：① 时空反演 $I_{ST}$ 对称强制 Berry 曲率处处为零，但 2D 两条孤立能带仍可由整数**欧拉数 χ** 刻画（$E_c=\langle\nabla u_1|\times|\nabla u_2\rangle$ 的 BZ 积分）📜Q；② 构造 AA′ 堆叠双层 honeycomb 晶格模型（Eq. (1)）：层内 QVHE 的两层 VCN 反号，t⊥≠0 时总 Berry 曲率归零、但上下带各带**半整数欧拉数**，谷欧拉数 $\chi_\eta=\frac12\,\mathrm{sgn}(m\eta)$ → ZBC QVHE 📜Q；③ 当畴壁构型（DWC）保持 $M_y$ 镜面对称，或保持 $\Pi$ 手征 + $I'_{ST}=C_{2z}T$，两畴（VEN 反号）间的**螺旋畴壁态**受拓扑保护（$M_y$ 本征值相反 → 交叉稳定）📜Q；④ 候选体系 h-BAs、h-BP（DFT 确认螺旋 DW 模存在，$M_y$ 本征值相反），h-BN 因带隙过大/界面势突变而模被湮灭、但**加 E 场可恢复** 📜Q。

**结论/意义**：作者表态 "we propose a new type of valley-dependent topological phenomenon"——首次确立 ZBC QVHE 的**基本起源**为谷欧拉数，并把 QVHE 的拓扑保护判据从"Berry 曲率"扩展到"欧拉曲率"（Euler class）。⚠️ 全文为理论构造 + 第一性原理预言（"propose"），非实验证实。

---

## 1. 模型白箱（理想系统 + 假设清单）

### 1.1 模型：AA′ 堆叠双层 honeycomb 晶格的低能哈密顿量

**晶格**：AA′-stacked 双层 honeycomb 晶格（Fig. 1(a)），两谷 K/K′；层内最近邻跳迁 t1、层间 t⊥、交错子格势 m 📜Q。

**低能哈密顿量**（每谷，Eq. (1)）：

$$H_\eta(k_x,k_y)=v\eta k_x\,\sigma_x\tau_0+v k_y\,\sigma_y\tau_0+m\,\sigma_z\tau_z+t_\perp\,\sigma_0\tau_x$$

其中 $v=\frac{\sqrt3}{2}t_1$ 为费米速度、m 为交错子格势、t1/t⊥ 为层内/层间耦合、η=±1 标 K/K′ 谷、σi/τi 为子格/层 Pauli 矩阵 📜Q。

**对称性**：P 与 T 都是全体系对称，但每谷 $H_\eta$ 只在 $PT\equiv I_{ST}=\sigma_x\tau_x K$（时空反演，K 复共轭）下不变 📜Q。m 是 $I_{ST}$ 下唯一允许的质量项。$m=0$ 时 $H_\eta$ 还有两镜面 $M_y=\sigma_x$（y→−y）、$M_z=\tau_x$（z→−z）与两手征 $\Pi_0=\sigma_z\tau_z$、$\Pi=\sigma_z\tau_y$；$m\neq0$ 时仅 $\{H_\eta,\Pi\}=0$ 保持，$M_y,M_z,\Pi_0$ 全破 📜Q。

**能带演化**（Fig. 1(b)）：$m=t_\perp=0$ → 两层各一个简并 Dirac 锥；$m\neq0$ → 两锥质量反号 → Berry 曲率反号；$t_\perp\neq0$ → 耦合两锥 → **Berry 曲率处处为零**，但上下带各带**半整数欧拉数** → ZBC QVHE 📜Q。

### 1.2 参数分册（区分"作者设定" vs "推导所得"）

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | m（交错子格势，跨畴壁变号）、t⊥（层间耦合 0→非零）、谷 η=±1、畴壁构型（My 对称 / Π+IST） |
| **导出量（由旋钮+常数算出）** | 谷 Chern 数 $C_{\tau,\eta}=\frac12\,\mathrm{sgn}(m\eta\tau)$、欧拉曲率 $E_c$、欧拉数 χ、谷欧拉数 $\chi_\eta=\frac12\,\mathrm{sgn}(m\eta)$、$\Delta\chi_v^\eta=\mathrm{sgn}(m\eta)$ |
| **模型内部量（解的性质）** | 能带、欧拉曲率分布、螺旋 DW 模、$M_y$ 本征值 |
| **固定常数** | $t_1$（层内跳迁）、$v=\frac{\sqrt3}{2}t_1$、$m_0$（DW 质量幅度） |
| **预言量（可检验）** | h-BX / 大转角 TBG / 自旋体系中的螺旋 DW 模 |

> 无"反推量 θ̂"层——纯理论，参数为符号参数（全文无 eV/Å 数值旋钮）。**符号防混**：χ 是欧拉数（拓扑不变量），与 η（谷指标）、τ（层指标）不同文；$E_c$ 是欧拉曲率（非能量/非 E 场）；$I_{ST}$（时空反演）≠ $I'_{ST}=C_{2z}T$（畴壁时空反演）。

### 1.3 显式假设清单（本文结论的前提集合）

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **$I_{ST}$（时空反演）对称**：强制 Berry 曲率处处为零、欧拉数可定义 | 模型 | 📜Q |
| A2 | **两条欧拉能带**：欧拉数是两带不变量；额外体能带只要不破坏半整数欧拉数即可 | 模型 | 📜Q（Discussion） |
| A3 | **单谷（谷间散射可忽略）**：VEN 按谷定义 | 模型 | 📜Q（类比 VCN） |
| A4 | **DWC 保持 $M_y$ 镜面，或 $\Pi$ 手征 + $I'_{ST}=C_{2z}T$** | 推导（保护条件） | 📜Q |
| A5 | **层间耦合足够小以保持带隙**（$M_y$ 表示 $\tilde M_y=\tau_z$ 不被破坏） | 推导 | 📜Q |

> 判别性扫轴：m 符号（跨 DW）、t⊥（0→非零）、材料（h-BAs/h-BP/h-BN 的带隙递增）、E 场（h-BN 恢复）——均为理论扫参。这些假设在 §4 逐一映射到"失效 → 结论崩塌"。

---

## 2. 推导链（演绎结构：顺论文顺序，每步"输入→输出→所用假设/定理→合法域"）

### 2.0 总览

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 前提定理层 | Introduction | QVHE（BC 积分）/ IST 欧拉带（refs 34–45,47） | ZBC 体系可有拓扑（欧拉数） | 欧拉类、脆弱拓扑 | IST（A1） |
| 模型层 | Model | AA′ 双层 + Eq.(1) | BC 归零 + 半整数欧拉数 | A1、A2 | 低能 |
| 推导层 | Topological invariant | 欧拉曲率积分 | $\chi_\eta=\frac12\,\mathrm{sgn}(m\eta)$ | Eq.(2) | 两带 |
| 推导层2 | Stability of helical DW | DWC + 对称保护 | 螺旋 DW 态（My 或 Π+IST 保护） | A4、A5 | DW |
| 边界层 | Materials + Discussion | h-BX / TBG / 无序 | 材料预言 + 稳健性 | DFT + 微扰 | — |

### 2.1 前提定理层（引言）

- QVHE：T 对称 + P 破缺体系两谷的 BC 非零，VCN = 谷内 BC 积分，跨畴壁计数 1D 手征金属态（refs 1–4）📜Q。
- $I_{ST}$ 对称：无 SOC 时是 T 与 P 的组合、有 SOC 时是 T 与 $C_{2z}$ 的组合（ref 46）→ 强制 BC 处处为零；但两条孤立带可由**整数欧拉数 χ** 刻画（ref 47）📜Q。带交叉点涡量 = 2χ；欧拉数变化伴随节点对产生/湮灭、非阿贝尔编织（refs 47–56）📜Q。欧拉数是 TBG 近平带的脆弱拓扑指标（refs 47,57–59）📜Q。
- 关键：纯欧拉带**不能**独自承载边界 in-gap 模，除非加额外对称（refs 47,60）——为 §2.4 的保护条件埋下伏笔 📜Q。

### 2.2 模型层：AA′ 双层 → ZBC QVHE

- $m=t_\perp=0$：两层各一简并 Dirac 锥；$m\neq0$：两锥质量反号 → BC 反号（Fig. 1(b2)）；$t_\perp\neq0$：耦合两 gapped Dirac 锥 → **BC 处处消失**、上下带各带半整数欧拉数（Fig. 1(b3),(b4)）📜Q。
- 机制：每层在退耦极限承载 QVHE，且上下层 VCN 反号 → 总体系 BC 处处为零、无 QVHE 预期；但螺旋 DW 态在 $t_\perp\neq0$、总 VCN 消失后仍存活 📜Q。

### 2.3 推导层：谷欧拉数（Topological invariant 节）

- **欧拉曲率**：$E_c(k)=\langle\nabla u_1(k)|\times|\nabla u_2(k)\rangle$（两实带非阿贝尔 Berry 曲率的 Pfaffian）📜Q。**欧拉数**（Eq. (2)）：$\chi=\frac{1}{2\pi}\int_{BZ}E_c(k)\,dk_x dk_y$ 📜Q。谷欧拉数：$\chi_\eta=\frac12\,\mathrm{sgn}(m\eta)$，跨畴壁变化 $\Delta\chi_v^\eta\equiv2\chi_\eta=\mathrm{sgn}(m\eta)$ 📜Q。
- **VCN vs VEN**：退耦极限每层 VCN $C_{\tau,\eta}=\frac12\,\mathrm{sgn}(m\eta\tau)$（τ=±1 层）；t⊥≠0 时每层 VCN ill-defined，唯 VEN 定义良好 📜Q。类比 QSH：两自旋通道 Chern 数反号叠加时，单自旋 Chern 数在 SOC 下 ill-defined、唯 Chern 数差 mod 2 定义良好（refs 63–67）📜Q。

### 2.4 推导层2：螺旋 DW 态的保护（Stability of helical DW states 节）

- **DWC**：$m\to m(y)$，$\lim_{|y|\to\infty}m(y)=\mathrm{sgn}(y)m_0$（$m_0>0$），DW 沿 x 方向；DW 哈密顿量（Eq. (3)）为 Eq. (1) 代 $k_y\to-i\partial_y$ 📜Q。
- **$M_y=\sigma_x$ 保护**：DWC 满足 $M_y$ → DW 是 $M_y$-不变 1D 空间；$M_y$ 变 m 符号 → 两畴欧拉数反号。退耦极限有效哈密顿 $H_{DW}^0=v_0 k_x\tau_z$，$M_y$ 在螺旋 DW 态空间表示为 $\tilde M_y=\tau_z$（禁止 $m_1\tau_x+m_2\tau_y$ 质量项）📜Q。两螺旋态 $M_y$ 本征值相反 → **交叉稳定** 📜Q。
- **$\Pi$ + $I'_{ST}=C_{2z}T$ 保护**：$I'_{ST}=\sigma_x K$（变 m 符号）强制 $m_2=0$；$\tilde\Pi=\tau_x$ 湮灭剩余 $m_1\tau_x$ → 交叉稳定（引 refs 85–87 的 Z₂ 0 维荷）📜Q。

### 2.5 边界层：材料实现 + 稳健性

- **h-BX（B=硼，X=As,P,N）**（Fig. 2）：h-BAs、h-BP 的 DFT 确认螺旋 DW 模存在、$M_y$ 本征值相反（Figs. 2(e),(f)）；h-BN **无**螺旋 DW 模（Fig. 2(g)），两原因：① 带隙递增 → K/K′ 波函数混合 → VEN ill-defined；② DW 处 on-site 势突变（∝ 子格势）→ 两谷螺旋模对湮灭 📜Q。**E 场可恢复** h-BN 的螺旋 DW 态（Fig. 3，TB 模型）📜Q。
- **其他候选**：大转角 TBG（refs 31,69–74，即 T28）、hexagonal 双层自旋体系、经典波系统（refs 22,25,26,90）📜Q。
- **无序稳健性**：$M_y$ 破缺（畴宽不等/垂直/侧向位移）下，只要畴宽足够大、失配在实验窗口内，DW 模仍稳（第一性原理）；局域无序破镜面 → 失去拓扑保护，但**无序强度大到等于带隙时仅开微小隙**（谱函数分析，refs 75–80）📜Q。

---

## 3. 结论清单（分层：定理 / 估算 / 预言）

### 3.1 定理式主张（数学/对称性论证的产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| BC 归零条件 | $I_{ST}$ 对称 → Berry 曲率处处为零 | A1 |
| 欧拉数定义 | 2D 两条孤立带由整数欧拉数 χ 刻画（Eq. (2)） | A1、A2 |
| 谷欧拉数 | $\chi_\eta=\frac12\,\mathrm{sgn}(m\eta)$；$\Delta\chi_v^\eta=\mathrm{sgn}(m\eta)$ | A1、A3 |
| 螺旋 DW 态保护 | VEN 反号两畴 +（My 或 Π+IST）→ 螺旋 DW 态 | A4、A5 |
| VCN↔VEN 类比 | 同 QSH 的 Chern↔Z₂ 类比：t⊥ 下 VCN ill-defined、VEN 定义良好 | $I_{ST}$ 存在 |

### 3.2 估算（本文几乎纯符号，唯一"数值"是 $v=\frac{\sqrt3}{2}t_1$）

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| 费米速度 | $v=\frac{\sqrt3}{2}t_1$ | 最近邻跳迁 | 📜Q[~] |
| 半整数欧拉数 | 上下带各 1/2（χη=±1/2） | 两带 | 📜Q[~] |

> ⚠️ 全文无 eV/Å 数值参数（h-BX 的带隙只给"递增"趋势、未给绝对值）；不引入任何带隙数字（防脑补）。

### 3.3 预言（可检验性 → 见 §5.1）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| ZBC QVHE + VEN 保护螺旋 DW 态 | "we propose / dubbed"（理论构造）📜Q | 中——需 ZBC 材料实验 |
| h-BAs/h-BP 有螺旋 DW 模、h-BN 无（E 场可恢复） | "our DFT confirms / the helical DW modes are absent" 📜Q | 中——STM/ARPES |
| 大转角 TBG / 自旋体系 / 经典波系统可实现 | "we have identified / anticipate"（谨慎）📜Q | 弱——定性 |

### 3.4 内部验证（自洽核对，非"排除竞争解释"）

1. **解析 ↔ 数值互验**：Eq. (1) 的 χη=±1/2 预言 ↔ h-BX 欧拉曲率分布 + 半整数欧拉数（Fig. 2(b)–(d) 紫点 Dirac 点）📜Q。
2. **保护条件 ↔ 数值互验**：$M_y$ 本征值相反的螺旋 DW 模 ↔ DFT 确认（Figs. 2(e),(f)）📜Q。
3. **负对照**：h-BN 同对称条件却无螺旋 DW 模 → 归因带隙/界面势（排除"只要 VEN 反号必有模"的过强结论）📜Q。

### 3.5 概念区分（作者论证中的"分类"，非溯因排除）

| 区分 | 依据 | 结论 |
|---|---|---|
| Chern class vs Euler class | BC 积分（VCN）vs 欧拉曲率积分（VEN）📜Q | ZBC QVHE 属 Euler class |
| 螺旋 vs 手征 | 本文 DW 态是两反传播（helical）in-gap 态，非单向手征 📜Q | helical |
| VCN vs VEN | t⊥=0 时 VCN 定义良好；t⊥≠0 时唯 VEN 定义良好 📜Q | 类比 QSH Chern↔Z₂ |
| h-BAs/h-BP vs h-BN | 带隙小（VEN 良定义）vs 带隙大（VEN ill-defined + 界面势突变）📜Q | 材料筛选判据 |

> 注：这些是**概念/图景分类**（taxonomy），不是实验论文那种"数据排除竞争解释"（溯因排除）——理论论文没有后者。

---

## 4. 假设-结论依赖图（含金量所在）

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性（作者如何对待） |
|---|---|---|---|
| A1 $I_{ST}$ 对称 | 对称破缺（如 E 场、衬底） | BC 归零、欧拉数定义 | **致命**——ZBC QVHE 的根基 📜Q |
| A4 $M_y$ / Π+IST 保护 | 畴宽不等、位移失配、局域无序 | 螺旋 DW 态交叉的拓扑保护 | 作者证：畴宽足够大/失配在窗口内仍稳；无序强度达带隙仅开微小隙 📜Q |
| A2 两带欧拉数 | 额外体能带破坏半整数欧拉数 | 欧拉数（脆弱拓扑） | 作者论证 My 交叉在多带下仍由 My 保护 📜Q |
| A5 层间耦合小 | t⊥ 大到闭带隙 | $\tilde M_y=\tau_z$ 表示、VEN | 保护条件的前提 📜Q |
| A3 单谷 | 谷间散射 | VEN 按谷定义 | 类比 VCN，未展开 💭I |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（本文预言的实验靶标）

- h-BX（As/P）的螺旋 DW 模 + $M_y$ 本征值相反（Figs. 2(e),(f)）📜Q；
- h-BN 无模、E 场恢复（Fig. 3）📜Q；
- 大转角 TBG、hexagonal 双层自旋体系、经典波系统（声学/光子）📜Q。

### 5.2 设计原则（ZBC QVHE 材料三要素）

$I_{ST}$ 对称（BC 归零）+ 两反号 VCN 层叠（欧拉数半整数）+ DWC 保持 $M_y$ 或 Π+$C_{2z}T$（螺旋 DW 态保护）📜Q。

### 5.3 后续文献修正（时间倒挂，💭I）

- **T28 Mondal 2023（同组，前作）**：本文是其"EAA $C_{2z}T$ → BC 归零"思想的系统化（T28 的 EAA 正是本文 $I_{ST}$ 特例），并显式引用 T28 为候选体系（ref 31）💭I。
- 与 Euler class / 脆弱拓扑文献（refs 47–56 Ahn/Bouhon）构成拓扑分类的新轴线；尚无实验验证 💭I。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 玩具模型为主 | h-BX/TBG 应用是第一性原理预言，真实样品未验证 | 📜Q（"propose/anticipate"） |
| 拓扑保护强度 | 脆弱拓扑（Euler class）对对称性破缺的敏感度 vs Chern 情形未定量比较 | 💭I（旧版"对无序更敏感"已删——原文无此比较） |
| 单谷假设 | 谷间散射对 VEN 的影响未展开 | 💭I |
| 无定量实验信号 | 未给 STM/ARPES/输运的定量可测预言（只给"模存在/不存在"） | 📜Q（grep 无 LDOS/conductance 数字） |

## 7. 与其他工作的关系（跨论文对标放这里，不放正文）

| 工作 | 关系 |
|------|------|
| Ahn 2017–2019 / Bouhon 2020（refs 34–59） | **直接依赖**——IST 对称、欧拉类、脆弱拓扑、非阿贝尔编织的理论基础 📜Q |
| Zhao & Lu 2017（ref 34） | 引用——PT 对称实 Dirac 费米子 📜Q |
| Zhang/MacDonald/Mele 2013（ref 2）、Vaezi 2013（ref 3）、Jung 2011（ref 4） | 引用——QVHE 的 VCN 定义与畴壁模先驱 📜Q |
| Mondal/Ghadimi/Yang 2023（ref 31 = T28） | **同组前作**——大转角 TBG 的 EAA $C_{2z}T$ 零 Berry 曲率 📜Q |
| Kane-Mele QSH（refs 63–67） | 类比——VCN↔VEN 与 Chern↔Z₂ 的映射来源 📜Q |

> ⚠️ Phase S 外部对标（非本文引用，时间倒挂，💭I）见 §5.3。

## 8. 对后续研究的影响

- 把 QVHE 的拓扑保护判据从"谷 Chern 数（Berry 曲率）"扩展到"**谷欧拉数（欧拉曲率）**"——重写畴壁态的拓扑分类 📜Q。
- 提供"哪些实验畴壁态可能**不是**传统谷霍尔边缘态"的判据（ZBC QVHE 候选）📜Q。
- 与 T28 共同构成 Yang 组的"大转角 + 无 Berry 曲率拓扑"研究线 💭I。

## 9. 理论模型映射（供 TBPM / Kubo 计算对标）

| 映射 | 说明 |
|------|------|
| Eq. (1) 哈密顿 → TBPM | $H_\eta=v\eta k_x\sigma_x\tau_0+v k_y\sigma_y\tau_0+m\sigma_z\tau_z+t_\perp\sigma_0\tau_x$ 📜Q |
| m(y)=sgn(y)m0 → 畴壁 | DW 沿 x，$k_y\to-i\partial_y$（Eq. (3)）📜Q |
| 拓扑 ↔ 边缘态 | VEN 反号 + My/Π+IST → 螺旋 DW 模（可算 ribbon 能谱）📜Q |
| 材料 ↔ 参数 | h-BAs/h-BP（小带隙，VEN 良定义）/ h-BN（大带隙，模湮灭）📜Q |
| E 场 → h-BN 恢复 | 加 out-of-plane E 场可恢复螺旋 DW 态（Fig. 3）📜Q |

> 与 TBPM/Kubo 对应：本文是低能两带有效模型（Eq. (1)），可直接离散化做 ribbon 计算；复现"螺旋 DW 态 + My 本征值相反"需算 DW 能谱与波函数空间分布 💭I。

---

## Phase S 目的接口（引用式，随项目增删）

- **Q1（edge state 如何表征）**：本文是理论，无实验表征；预言 = 螺旋 DW 态（两反传播）+ $M_y$ 本征值相反（Figs. 2(e),(f)）📜Q。
- **Q2（理论如何解释）**：ZBC QVHE = 谷欧拉数（欧拉曲率谷内积分）保护，**非** Berry 曲率；挑战"谷陈数 ≠ 0 是拓扑保护必要条件" 📜Q（§2.3–2.4）。
- **Q3（理论↔实验对应）**：候选 h-BX（As/P）、大转角 TBG；h-BN 无模但 E 场可恢复；供重新审视已有 BLG 畴壁实验的拓扑解释 📜Q。

> **增量价值**：提供畴壁态的**第二类拓扑判据**（Euler class vs Chern class），供计算对标"零 Berry 曲率畴壁"；纠正旧版"量子度规 gij 产生边界态"（不符，实为谷欧拉数）与"对无序更敏感"（无源）两处。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` 提取正文到 `/tmp/T32.txt`（487 行），逐项 grep 核对：**全部数字/专名命中原文**——

| 数字/专名 | grep 命中位置 | 结论 |
|------|--------------|------|
| v=(√3/2)t1 | Eq. (1) 附近 | ✓ 📜Q |
| Cτ,η = 1/2 sgn(mητ) | Topological invariant 节 | ✓ 📜Q |
| χη = 1/2 sgn(mη)、Δχvη = sgn(mη) | Topological invariant 节 | ✓ 📜Q |
| χ = (1/2π)∫Ec dkx dky（Eq. 2） | Topological invariant 节 | ✓ 📜Q |
| IST = σxτxK、My=σx、Mz=τx、Π0=σzτz、Π=σzτy | Model 节 | ✓ 📜Q |
| h-BAs/h-BP/h-BN、h-BX (X=As,P,N) | Hexagonal bilayer materials 节 | ✓ 📜Q |
| Euler（36 处）、space-time inversion、helical | 全文 | ✓ 📜Q |
| "the helical DW modes are absent"（h-BN） | Materials 节 | ✓ 📜Q |

⚠️ 修正/降级：① arXiv:2403.15050 正文未出现 → 头部表已标"外部来源"。② 旧版"量子度规 gij 产生边界态"不符 → 实为谷欧拉数 VEN（Euler 曲率谷内积分，$I_{ST}$ 保护）。③ 旧版"边缘态对无序鲁棒性显著弱于 Chern 边缘态"为 review 层 💭I、原文未作此比较 → 删除。④ 全文无 eV/Å 数值参数（grep "eV"=0、"Å"=0 于正文旋钮处），§3.2 已声明不引入带隙数字。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-20 | **重写 §1–§3/Q2**：旧版"量子度规 gij 产生边界态"不符 → 原文为谷欧拉数 VEN（Euler 曲率谷内积分、$I_{ST}$ 时空反演对称）保护的 ZBC QVHE（grep "Euler"=36）；候选 h-BX (X=As,P)、大转角 TBG。依据 §B.5#26。 |
| 2026-08-20 | **§3 "对无序更敏感" 标注 💭I**：原文未作与 Chern 边缘态的直接比较。依据 QC 规则。 |
| 2026-09-08 | **按 5 块演绎结构整体重写**（应用户要求）。旧叙事版归档 `archive/paper_review_T32_ghadimi2024_prl.backup_20260908.md`。新增：模型白箱（Eq.(1) 哈密顿量 + 对称性 + 参数分册 + 5 条假设清单）、推导链（前提定理/模型/推导/材料边界四层）、结论清单（定理/估算/预言分层）、假设-结论依赖图、接口。全部 📜Q 事实无丢失，旧版两处无源/不符已删除。 |
