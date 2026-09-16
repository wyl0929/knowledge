<!--
 * @Author       : AI 精读（白箱演绎结构）
 * @Date         : 2026-08-11（初读）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T28_mondal2023_prb.md
 * @Description  : T28: Mondal, Ghadimi & Yang 2023 PRB — 大转角 TBG 量子谷/子谷霍尔效应（2026-09-08 按 5 块演绎结构重写：模型白箱/推导链/结论清单/假设-结论依赖图/接口）
-->

# Paper Review: Mondal, Ghadimi & Yang (2023) — 大转角 TBG 的量子谷与子谷霍尔效应

| 字段 | 内容 |
|------|------|
| **编号** | T28 |
| **标题** | Quantum valley and subvalley Hall effect in large-angle twisted bilayer graphene |
| **作者** | Chiranjit Mondal, Rasoul Ghadimi, Bohm-Jung Yang* |
| **期刊** | Physical Review B 108, L121405(R) (2023)（Received 11 Jun / published 11 Sep 2023）📜Q |
| **DOI / arXiv** | 10.1103/PhysRevB.108.L121405 / arXiv:2306.02655（⚠️ arXiv 号外部来源，正文未出现） |
| **类型** | 理论 — 大转角 TBG 量子谷/子谷霍尔效应（连续模型 + 紧束缚 + DFT，无实验数据） |
| **课题组** | Bohm-Jung Yang group（Seoul National Univ. CTP + IBS-CES） |
| **PDF** | ✅ `reference/pdfs/Mondal 等 - 2023 - Quantum valley and subvalley Hall effect in large-angle twisted bilayer graphene.pdf`（正文 6 页 + SM：TB/DFT 细节） |
| **精读日期** | 2026-08-11（初读）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」的五块记（见 `note/shared/method/theory_paper_reading.md` §3）：**① 模型白箱 → ② 推导链 → ③ 结论清单（分层）→ ④ 假设-结论依赖图 → ⑤ 接口**。理论论文无黑箱、无反推、无可辨识实验，故不用"四层变量表 + 判别表"。
> **共享知识引用**：valley Chern 数 / Berry 曲率 / 体-边对应见 `[PHY-BERRY]`。⚠️ 本文子谷（subvalley）机制（Haldane/Semenoff 质量竞争）与 mTBG 的 AB/BA valley-Chern 畴壁是**两类**，§2.4/§7 显式对照。

---

## TL;DR

**本文想解决的问题**：大转角 TBG（commensurate 角 θc=38.21°）在层间耦合下是否仍承载拓扑谷霍尔物理？具体地，E 场能否在 EAB/EBA 开隙并产生谷 Chern 数差驱动的畴壁模，以及**层滑动**能否诱导"子谷"（subvalley）Dirac 锥与子谷霍尔效应——即把畴壁物理从 mTBG 小转角范式扩展到大转角？

**主结果**（全文无实验数据，均为理论推导 + DFT/TB 数值自洽）：① 大转角 commensurate 角 θc=38.21° 附近，SEO 构型分 EAB/EBA（Bernal 类），SEE 构型为 EAA（AA 类）；E 场在 EAB/EBA 打开拓扑隙、谷 Chern 数 $C_v=\eta\,\mathrm{sgn}(E)$（η=±1 谷指标）📜Q；② EAB-EBA 畴壁 $\Delta C_v=\pm2$ → **每谷 2 条反向传播畴壁模**；EAA 因 $C_{2z}T$ 对称 Berry 曲率恒零、$C_v=0$ 充当"真空"，EAB-EAA 畴壁 $\Delta C_v=\pm1$ → 1 条模 📜Q；③ 层滑动 d 使 EAB 的二次带接触劈成**子谷 Dirac 锥**，dx 与 E 场分别给**Haldane 质量**（两子谷反号）与 **Semenoff 质量**（两子谷同号）→ 子谷 Chern 数 ±1/2、子谷霍尔效应**无需真实 E 场**即存在 📜Q；④ 微小偏离 δθc 使局部结构扫过 EAA/EAB/EBA → 构成 **1D 畴壁导电网络**，在 δθc=0.05° 时 $L\sim740$ nm、$v_f\sim0.6\times10^6$ m/s、$T_x\approx7$ K，EAA 隙 ~5 meV（~58 K）→ 网络在 7–58 K 区间可现 **1D 非费米液体输运**（作者 "is expected to show"）📜Q。

**结论/意义**：作者表态 "open up an alternative direction"、"can be generalized to many twisted bilayer systems (α-graphene, kagome bilayers)"——把 QVHE/畴壁物理从 mTBG 扩展到大转角、并引入**子谷自由度**作为新拓扑分类 📜Q。⚠️ 全文为理论预言/估算（作者 "we found / we study / can be tuned"），非实验证实。

---

## 1. 模型白箱（理想系统 + 假设清单）

> 理论论文的研究对象是**白箱**——作者自写的理想模型。本节只做两件事：**写下模型**（§1.1），**列出它成立的全部假设**（§1.3）。

### 1.1 模型：commensurate 大转角 TBG 的层间耦合 + 低能展开

**结构分类**（引 Refs. 28,29 Mele 2010/2012）：commensurate 角 TBG 按子格交换奇偶分为 SEO（子格交换奇，含 EAB/EBA 两种 Bernal 类堆垛）与 SEE（子格交换偶，仅 EAA 一种 AA 类堆垛）📜Q。EAA 由 EAB 经层平移 $d=\{0,2d_0\}$ 得到 📜Q。

**层内 Dirac**：$H_{1,2}=-i\nu(\sigma_x k_x+\sigma_y k_y)$，ν 为费米速度 📜Q。

**层间耦合**（θc=38.21°，Eq. (1)）：

$$H^{\alpha\beta}_{k,\tilde k}=\sum_{i=1}^{3} t_{k+G_i}\, e^{iG_i\cdot(\tau^\alpha+d)}\, e^{-i\tilde G_i\cdot\tau^\beta}$$

其中 α,β 为子格指标、$\tau^i$ 为子格位置、$G=\sum n_i b_i$、$\tilde G=\sum \tilde n_i \tilde b_i$ 为两层倒格矢、$t_{k+G}$ 为紧束缚跳迁的动量空间傅里叶系数（随 $|k+G|$ 快速衰减）。满足动量守恒且 $|t|$ 最大的三组 $(G,\tilde G)$：$(G_1,\tilde G_1)=(b_1,\tilde b_1+\tilde b_2)$、$(G_2,\tilde G_2)=(-2b_1-2b_2,-\tilde b_1-2\tilde b_2)$、$(G_3,\tilde G_3)=(-b_1+b_2,-2\tilde b_1)$ 📜Q。

**E 场**：$H_E=\mathrm{diag}(E,E,-E,-E)$ 📜Q。

**低能二阶展开**（EAB 附近、dy 方向，Eq. (2)）：

$$H_{0,d_y}(k_x,k_y)=\alpha(k_x^2-k_y^2)+m_1 d_y\sigma_x-2\alpha k_x k_y\sigma_y+(E+m_3 d_y k_y)\sigma_z$$

其中 α、$m_i$（i=0,1,2,3）为常数 📜Q。$E=0$ 时恢复 $C_2=\sigma_x$ 对称，在 $k_y=0$、$k_x=\pm k_0$（$k_0=m_1 d_y$）有 gapless 谱；$m_1>0$ 时仅 $d_y>0$ 有解 📜Q。

**子谷 Dirac 锥**：$H_{sv}=k_x\sigma_x+k_y\sigma_y$ 位于 $\pm k_0$；只有 $C_2$ 被 dx 平移或 E 场破坏才能开隙 📜Q。子谷质量（Eq. (3)）：

$$M_{sv}=(E\pm d_x k_0)\sigma_z$$

第一项来自 E（**Semenoff 类**，两子谷同号）、第二项来自 dx（**emergent E 场 / Haldane 类**，两子谷反号）📜Q。

### 1.2 参数分册（替代旧"四层变量表"：区分"作者设定" vs "推导所得"）

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | θ（θc=38.21° 主算例，另列 32.2°/43.17°/42.1°）、E 场、层间位移 d=(dx,dy)、偏离角 δθc |
| **导出量（由旋钮+常数算出）** | 谷 Chern 数 $C_v=\eta\,\mathrm{sgn}(E)$、$\Delta C_v$、子谷 Chern 数（±1/2）、$k_0=m_1 d_y$、网络长度 $L=l/[2\sin(\delta\theta_c/2)]$ |
| **模型内部量（解的性质）** | DFT/TB 能带、direct gap δg、子谷 Dirac 锥、Berry 曲率分布、畴壁模色散 |
| **固定常数** | ν（费米速度）、l（EAA/EAB 晶格常数）、Table I 的 (N, l, Δ) |
| **预言量（可检验）** | 畴壁/边缘模数、STM LDOS、dc 光学电导、非费米液体温度窗口 $T_x$ |

> 无"反推量 θ̂"层——纯理论论文，参数由紧束缚/DFT 自洽给出，非自实验反推。**符号防混**：η 是谷指标（±1），与 τ（层指标）不同文；$d_0$ 是结构位移单位（非子谷 Dirac 锥位移）；$k_0$ 是子谷锥位置（动量），非偏离角。

### 1.3 显式假设清单（本文结论的前提集合）

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **U(1) 谷守恒（无谷间散射）**：VCN/DW 模成立的前提 | 模型 | 📜Q（"without valley mixing"） |
| A2 | **单粒子图景**：非费米液体来自网络几何（1D 通道），非 e-e 关联 | 模型 | 💭I（原文未讨论关联） |
| A3 | **大转角下晶格弛豫可忽略**：EAA/EAB/EBA 能量差仅 0.14 meV/atom（对比小转角 AA/AB-BA 103 meV/atom） | 模型 | 📜Q |
| A4 | **局部结构近似**：incommensurate 结构局部仍像 commensurate 构型（可动量空间局部定义） | 推导 | 📜Q（"locally resembles"） |
| A5 | **低能二阶截断**：$H_{0,d_y}$ 只到动量二阶 | 推导 | 📜Q |
| A6 | **C2/C3z 对称约束**用于 subvalley 结构（quadratic band touching 由 C3z 强制） | 推导 | 📜Q |

> 判别性扫轴：θ（38.21°/32.2°/43.17°/42.1°）、E（±）、d=(dx,dy)、δθc（0.05°）——均为计算扫参。这些假设在 §4 逐一映射到"失效 → 结论崩塌"。

---

## 2. 推导链（演绎结构：顺论文顺序，每步"输入→输出→所用假设/定理→合法域"）

### 2.0 总览：论文是一条演绎链

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 前提定理层 | Introduction | QVHE（AB/BA，refs 30–43）+ SEO/SEE 分类（refs 28,29） | 大转角层间耦合仍有拓扑物理 | 谷 Chern 数、体-边对应 | U(1) 谷守恒（A1） |
| 模型层 | Structure and VCN | commensurate 哈密顿 + E 场 | EAB/EBA 开隙 + $C_v=\eta\,\mathrm{sgn}(E)$ | A1、A3 | θc=38.21° |
| 推导层 | Domain wall modes | VCN 差 → 畴壁 | ΔCv=±2/±1 → 2/1 条模 | 体-边对应 | 谷守恒 |
| 推导层2 | Incommensurate + subvalley | 层滑动 d + E 场 | 子谷 Dirac 锥 + Haldane/Semenoff 质量 | A4、A5、C2/C3z（A6） | 二阶展开 |
| 边界层 | Discussion | 弛豫能量差 + 网络输运 | 大转角稳定 + 非费米液体窗口 | A3、网络几何 | δθc 小 |

### 2.1 前提定理层（引言）：大转角仍有层间耦合拓扑

- 小转角 TBG：魔角平带 + 关联态（refs 1–17）📜Q。
- 大转角：早期预言层退耦（ref 22），但近期发现高阶拓扑（refs 23,24）、几何阻挫（ref 25）、平带（ref 25）、hypermagic 角（ref 26）、非平凡光学响应（ref 27）📜Q。低能带结构受层间耦合**高阶傅里叶分量**主导（refs 28,29）📜Q。
- SEO/SEE 分类：SEE=EAA（gapped + 晶格/高阶拓扑绝缘体）；SEO=EAB/EBA（Bernal 类，承载 QVHE，refs 30–43）📜Q。

### 2.2 模型层：E 场开隙 + VCN（"Structure and VCN" 节）

- **DFT 带结构**：EAB 在 E=0 时每谷 K/K′ 有 gapless **二次带接触**（Fig. 1(c)）；开 E 场 → 开隙（Fig. 1(d)）📜Q。Berry 曲率：gapped Dirac 锥是热点（Figs. 1(f),(g)）📜Q。
- **VCN**：$C_v=\eta\,\mathrm{sgn}(E)$（η=±1 谷指标，SM 有推导）；反转 E 场方向或换谷 → VCN 变号 📜Q。
- **EAA**：无论有无 E 场始终 gapped（Fig. 1(e)），但因 $C_{2z}T$ 对称（$C_{2z}:\{x,y,z\}\to\{-x,-y,z\}$）强制波函数为实 → Berry 曲率恒零 → $C_v=0$（引 refs 54–56）📜Q。

### 2.3 推导层：畴壁模（"Domain wall modes" 节）

- **计数规则**：$\Delta C_v=|C_v^A-C_v^B|$ = A/B 两区间的畴壁模数 📜Q。反谷 VCN 反号 → 畴壁/边缘模反向传播 📜Q。
- **EAB 带（Fig. 2(a)）**：两侧加相反 E 场 → 每谷 $\Delta C_v=\pm2$ → **每谷 2 条反向传播模**；边缘态由 EAB 与真空 VCN 差（$|C_v|=1$）解释 📜Q。
- **EAB-EBA 畴壁（Figs. 2(d)–(g)）**：$\Delta C_v=\pm2$ → 2 条 in-gap 模；平滑畴壁（缓慢滑层）也承载 2 条模（Fig. 2(f) 插图）→ 模不依赖畴壁具体化学细节、非常稳健 📜Q。
- **EAB-EAA 畴壁（Figs. 2(h)–(k)）**：EAA 的 $C_v=0$ → 等效"真空"；1 条模位于中心，仅 EAB 侧边缘承载边缘态（EAA 侧无）📜Q；平滑畴壁下模偏向 EAB 侧 📜Q。

### 2.4 推导层2：incommensurate 网络 + 子谷霍尔效应（核心）

- **网络结构**：从 θc 小偏离 δθc → 破坏大尺度 commensurability，但局部仍像由某位移 d 构造的 commensurate 构型（Fig. 3(a)）📜Q。沿垂直虚线 EAA→EAB→EBA：E=0 时 $\delta g$ 在 EAB 闭合（二次带接触）、再向 EBA 劈成**两个子谷 Dirac 锥**（受 C2 保护，在 EBA 合并回二次接触）📜Q。
- **子谷质量**（Eq. (3)）：E 场给 Semenoff 质量（同号）、dx 给 Haldane 质量（反号）→ **子谷 Chern 数反号**（如 dx>0 时 (+1/2,−1/2)，dx<0 时 (−1/2,+1/2)）📜Q。dx 符号反转 → 子谷 Chern 数变化 ±1 → **dx=0 处保护 2 条反向传播畴壁模**；**无真实 E 场**也能有子谷霍尔效应 📜Q。
- **E 场下的相变**：E 破坏 C2 → 两子谷锥都开隙；随 dx 增大，一锥保持 gapped、另一锥在 $|E|=|d_x k_0|$ 处经历 gap 闭合-重开 → 对应 1 条畴壁模（$\Delta C_v=1$）📜Q。相变**类比 Haldane 模型 + Semenoff 质量竞争**（ref 58）📜Q。
- **EAA 处**：两 gapped 子谷锥相遇、湮灭各自 Berry 曲率与子谷 Chern 数 📜Q。

### 2.5 边界层：弛豫稳定性 + 非费米液体（Discussion）

- **弛豫对比**：小角度弛豫使 AA 收缩成拓扑点缺陷（ref 43）；大角度下 EAA/EAB/EBA 能量差（DFT）仅 **0.14 meV/atom**（对比 AA vs AB-BA 的 103 meV/atom）→ 三者皆为稳定局部结构、支撑所提 DW 态 📜Q。
- **非费米液体**：2D 导电畴壁网络在临界温度 $T_x\sim\hbar v_f/(k_B L)$ 以上可现 1D 非费米液体（引 ref 59）📜Q。δθc=0.05° → L∼740 nm、$v_f\sim0.6\times10^6$ m/s → $T_x\approx7$ K；EAA 隙 ~5 meV（~58 K）→ 网络在 **7 K 至 ~58 K** 区间预期现非费米液体输运（"is expected to show"）📜Q。
- **Table I**：θc → (N, l, Δ)：38.21°→(28, 6.46 Å, 5 meV)、32.2°→(52, 8.85 Å, 0.1 meV)、43.17°→(76, 10.7 Å, 0.2 meV)、42.1°→(124, 13.67 Å, 0.25 meV)——Δ 随 N、l 增大快速衰减 → 实验上更显著于少数小 N 的 θc 📜Q。

---

## 3. 结论清单（分层：定理 / 估算 / 预言）

> 理论论文的结论必须按**性质**分层，而非平铺。每条标：**依赖假设** + **可检验性**。

### 3.1 定理式主张（数学/对称性论证的产物，依赖 A1 谷守恒）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| VCN | $C_v=\eta\,\mathrm{sgn}(E)$（η=±1 谷指标） | A1（谷守恒） |
| EAA 无 Berry 曲率 | $C_{2z}T$ 强制波函数为实 → Berry 曲率恒零、$C_v=0$ | C2z T 对称 |
| 畴壁模数 | $\Delta C_v=\pm2$（EAB-EBA）→ 2 模；$\Delta C_v=\pm1$（EAB-EAA/真空）→ 1 模 | 体-边对应、A1 |
| 子谷 Chern 数 | 两子谷锥 ±1/2，dx 反号 → 符号互换 | C2 对称（A6） |
| 子谷霍尔效应 | 无真实 E 场即存在（dx 即 emergent E 场） | A4、A6 |

⚠️ 本文**未**讨论量子化电导（如 $4e^2/h$）——可测签名是 STM LDOS 与 dc 光学电导，不引入电导平台数字（防跨论文迁移）。

### 3.2 估算（数值算例/经验量，非严格定理）

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| 主算例转角 | θc=38.21°（另 32.2°/43.17°/42.1°） | commensurate 条件 | 📜Q[~] |
| 弛豫能量差 | EAA/EAB-EBA 0.14 meV/atom vs AA/AB-BA 103 meV/atom | DFT | 📜Q[~] |
| 网络非费米液体 | δθc=0.05°：L∼740 nm、vf∼0.6×10⁶ m/s、Tx≈7 K | 网络几何 | 📜Q[~] |
| EAA 隙 | ~5 meV（~58 K） | DFT/TB | 📜Q[~] |
| Table I 四组 (N,l,Δ) | 28/6.46 Å/5 meV；52/8.85 Å/0.1；76/10.7 Å/0.2；124/13.67 Å/0.25 | 紧束缚 | 📜Q[~] |

### 3.3 预言（可检验性 → 见 §5.1）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| 大转角 TBG 量子谷/子谷霍尔 + 畴壁模 | "we found / we study / can be tuned"（理论构造）📜Q | 中——STM LDOS + dc 光学电导 |
| 2D 畴壁网络 1D 非费米液体（7–58 K 窗口） | "is expected to show"（谨慎）📜Q | 中——输运测温 |
| 推广到 twisted α-graphene / kagome bilayers | "can be generalized to many twisted bilayer systems"📜Q | 弱——定性 |

### 3.4 内部验证（自洽核对，非"排除竞争解释"）

1. **DFT ↔ 紧束缚互验**：EAB/EAA 带结构、VCN、Berry 曲率分布一致（Figs. 1,2）📜Q。
2. **解析 ↔ 数值互验**：Eq. (2)–(3) 低能展开的子谷锥结构与 Fig. 3 的 δg map、位置 a–h 的能带色散一致（如 EAB 二次接触、EBA 两 Dirac 锥）📜Q。
3. **计数自洽**：$\Delta C_v$ 预言模数 ↔ 数值 in-gap 模数逐一对应（2/1 模）📜Q。

### 3.5 概念区分（作者论证中的"分类"，非溯因排除）

| 区分 | 依据 | 结论 |
|---|---|---|
| SEO（EAB/EBA）vs SEE（EAA） | 子格交换奇/偶（refs 28,29）📜Q | Bernal 类（QVHE）vs AA 类（Cv=0） |
| Semenoff vs Haldane 质量 | E 场同号 vs dx 反号 📜Q | 子谷质量的两来源，竞争定拓扑相界 |
| valley vs subvalley | 谷 K/K′ vs 谷内二次接触劈出的子锥 📜Q | 子谷 = 新拓扑分类自由度 |
| 大转角 vs 小转角 | 大角度 E 场下 EAA/EAB/EBA 全 gapped vs 小角度 AA 在 E 场下仍 gapless 📜Q | 大转角是独立参数空间 |

> 注：这些是**概念/图景分类**（taxonomy），不是实验论文那种"数据排除竞争解释"（溯因排除）——理论论文没有后者。

---

## 4. 假设-结论依赖图（含金量所在）

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性（作者如何对待） |
|---|---|---|---|
| A1 谷守恒 | 原子尺度缺陷/谷间散射 | VCN 定义、畴壁模无耗散保护 | **弱保护**——作者未讨论，属 mTBG 通用风险（T5 已示"weak"）💭I |
| A3 弛豫可忽略 | 大角度弛豫发生 | EAA/EAB/EBA 稳定局部结构、DW 态 | 作者以 0.14 vs 103 meV/atom 论证**非致命**（大角度稳定）📜Q |
| A4 局部结构近似 | 结构变化尺度小于动量局域尺度 | incommensurate 网络图景 | 作者明言"局部结构环境可大到足以局部定义动量"📜Q |
| A5 二阶截断 | 高阶动量项显著 | 子谷锥的定量描述 | 低能近似固有边界 💭I |
| A2 单粒子 | 关联效应 | 非费米液体归属（本文归因网络几何非 e-e） | 未讨论 💭I |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（本文预言的实验靶标）

- **STM LDOS**：网络尺寸大于 STM 分辨率 → 畴壁网络可被 STM LDOS 直接成像 📜Q；
- **dc 光学电导**：作者建议 STM LDOS + dc 光学电导测量（引 ref 39 Yin 2016）📜Q；
- **非费米液体输运**：7–58 K 温度窗口的 1D 网络输运 📜Q。

### 5.2 设计原则（大转角畴壁工程）

大转角 commensurate 角（θc=38.21° 等，抑制弛豫）+ E 场（开隙定 $C_v=\eta\,\mathrm{sgn}(E)$）+ 层滑动 dx（emergent E 场，诱导子谷 Haldane 质量）+ 偏离 δθc（生成畴壁网络）📜Q。

### 5.3 后续文献修正（时间倒挂，💭I）

- **Ghadimi 2024（T32, 同组）**：把 T28 的 EAA $C_{2z}T$ 对称"Berry 曲率恒零"思想推广为**零 Berry 曲率 QVHE（谷欧拉数 VEN）**，并显式引用 T28 为"大转角 TBG 候选体系"（ref 31）💭I。
- **Li 2025（T35, Umklapp）**：大转角畴壁的另一机制（intervalley Umklapp + Jackiw–Rebbi），与本文"层滑动 Haldane 质量"并列为大转角畴壁物理的两个入口 💭I。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 无实验验证 | 全文为理论 + DFT/TB 数值，无 STM/输运实验数据 | 📜Q（无实验） |
| 谷守恒风险未讨论 | A1 是 VCN 成立前提，但作者未讨论原子缺陷破坏谷守恒的影响 | 💭I（对比 T5 显式讨论 weak 保护） |
| 非费米液体是引用结果 | 网络非费米液体机制引用 ref 59（Lee 2021），本文只代入 L/vf 数值 | 📜Q |
| 单粒子 + 网络几何 | 关联效应（大转角虽色散但非零）未纳入 | 💭I |
| 子谷退相干未知 | 子谷自由度的实验可分辨性/退相干未讨论 | 💭I（旧版遗留，原文未讨论） |

## 7. 与其他工作的关系（跨论文对标放这里，不放正文）

| 工作 | 关系 |
|------|------|
| Mele 2010/2012（refs 28,29） | **直接依赖**——SEO/SEE 分类、大转角高阶傅里叶耦合 📜Q |
| 高阶拓扑 TBG（refs 23,24 Kindermann 2015 / Park 2019） | 引用——EAA 的晶格/高阶拓扑绝缘体背景 📜Q |
| AB/BA BLG QVHE（refs 30–43，含 Martin 2008/Jung 2011/Vaezi 2013） | 引用——QVHE 与畴壁模的先驱，本文把其机制移植到大转角 📜Q |
| Haldane 1988（ref 58）/ Semenoff 1984（ref 57） | 引用——子谷 Haldane/Semenoff 质量的类比来源 📜Q |
| Alden 2013（ref 43） | 引用——小角度弛豫使 AA 收缩成点缺陷的对照 📜Q |
| Lee/Oshikawa/Cho 2021（ref 59） | 引用——2D 网络非费米液体的理论来源 📜Q |

> ⚠️ Phase S 外部对标（非本文引用，时间倒挂，💭I）见 §5.3。

## 8. 对后续研究的影响

- 把 QVHE/畴壁物理从 mTBG 小转角扩展到**大转角 commensurate 角**——"大转角 + 子谷"成为新参数空间 📜Q。
- 引入**子谷（subvalley）**自由度作为谷内二次带接触劈出的新拓扑分类（±1/2 子谷 Chern 数）📜Q。
- 提供可测签名（STM LDOS + dc 光学电导 + 非费米液体窗口），为大转角输运实验给理论靶标 📜Q。
- 与 T32（ZBC QVHE）、T35（Umklapp）共同构成"大转角畴壁物理"集群 💭I。

## 9. 理论模型映射（供 TBPM / Kubo 计算对标）

| 映射 | 说明 |
|------|------|
| θc → moiré 超胞 | 38.21° → N=28 atoms、l=6.46 Å（Table I）📜Q |
| E → 谷隙 | $C_v=\eta\,\mathrm{sgn}(E)$，EAB/EBA 开隙 📜Q |
| 层滑动 d → 子谷质量 | dx → Haldane 质量（反号）、E → Semenoff 质量（同号）📜Q |
| δθc → 网络周期 | $L=l/[2\sin(\delta\theta_c/2)]$，δθc=0.05° → L∼740 nm 📜Q |
| 畴壁 → 界面构型 | EAB-EBA（ΔCv=2）/ EAB-EAA（ΔCv=1）ribbon 📜Q |
| 非费米液体 → 输运对标 | Tx≈7 K（~58 K 上限），TBPM 需 <meV 分辨率 + 有限温输运 💭I |

> 与 TBPM/Kubo 对应：本文紧束缚 + DFT 是 TBPM 直接上游（同一 $H^{\alpha\beta}_{k,\tilde k}$ 层间耦合）；复现"EAB-EBA 2 模 / EAB-EAA 1 模"需算畴壁 ribbon 能谱与 LDOS 空间分布 💭I。

---

## Phase S 目的接口（引用式，随项目增删）

- **Q1（edge state 如何表征）**：本文是理论，无实验表征；预言 = 畴壁 in-gap 模（每谷 2 条 EAB-EBA / 1 条 EAB-EAA）+ STM LDOS + dc 光学电导 📜Q（§2.3/§5.1）。
- **Q2（理论如何解释）**：大转角 EAB/EBA 在 E 场下开隙、$C_v=\eta\,\mathrm{sgn}(E)$ → 畴壁模由 VCN 差计数；层滑动 dx 诱导子谷 Haldane 质量 → 子谷霍尔效应（无需真实 E 场）📜Q（§2.2–2.4）。
- **Q3（理论↔实验对应）**：δθc ↔ 网络周期（0.05°→740 nm）；E 场 ↔ 谷隙/畴壁；非费米液体窗口（7–58 K）↔ 输运测温；STM LDOS ↔ 网络成像 📜Q。

> **增量价值**：与 T35（Umklapp）互补——本文是**层间耦合高阶傅里叶分量 + 层滑动 Haldane 质量**驱动的大转角畴壁，T35 是**intervalley Umklapp + Jackiw–Rebbi**驱动；供大转角 TBPM 双机制对标。纠正旧版三处无源（"~6°/~10°"转角列表、"~1 nm vs ~5 nm"边缘宽度、"圆偏振光读出"均已删）。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` 提取正文到 `/tmp/T28.txt`（407 行），逐项 grep 核对：**全部数字/专名命中原文**——

| 数字/专名 | grep 命中位置 | 结论 |
|------|--------------|------|
| θc=38.21°（9 处）、32.2°、43.17°、42.1° | 全文 + Table I | ✓ 📜Q[~] |
| Cv = η sgn(E) | "Structure and VCN" 节 | ✓ 📜Q |
| ΔCv=±2（EAB-EBA）、±1（EAB-EAA/真空） | Domain wall modes 节 | ✓ 📜Q |
| d={0,2d0}、Haldane=9、Semenoff=9 | 正文 | ✓ 📜Q |
| Msv=(E±dx k0)σz（Eq. 3）、k0=m1 dy | Incommensurate 节 | ✓ 📜Q |
| 子谷 Chern ±1/2 | 正文 | ✓ 📜Q |
| 103 meV/atom vs 0.14 meV/atom | Discussion | ✓ 📜Q[~] |
| L∼740 nm、vf∼0.6×10⁶ m/s、Tx≈7 K、58 K | Discussion | ✓ 📜Q[~] |
| EAA gap ~5 meV | Discussion | ✓ 📜Q[~] |
| Table I (28/6.46/5)、(52/8.85/0.1)、(76/10.7/0.2)、(124/13.67/0.25) | Table I | ✓ 📜Q[~] |
| non-Fermi（4 处）、δθc=0.05° | Discussion | ✓ 📜Q |

⚠️ 修正/降级：① arXiv:2306.02655 正文未出现 → 头部表已标"外部来源"。② 未引入 $4e^2/h$（本文未出现该量）。③ 旧版无源"~6°/~10°"转角列表、"~1 nm vs ~5 nm"边缘宽度、"圆偏振光读出"（grep "circular"=0）已删。④ Table I 的 5/0.1/0.2/0.25 meV 为带隙 Δ 值，非"子谷质量"，已在 §1.2 符号分册钉死。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-20 | **删除转角列表**："~5-15°"、"(~6°, ~10°)" 无源 → 改为原文算例 θc=38.21°（grep "38.21"=9），微小偏离产生 1D 畴壁网络。依据 §B.5#34。 |
| 2026-08-20 | **删除 "~1 nm vs ~5 nm"、"圆偏振光读出"**：均无源（grep "circular"=0）。依据 §B.5#34。 |
| 2026-08-20 | **补充 Haldane/Semenoff 子谷质量、非费米液体、电场/层滑动调控**：原文验证（grep "Haldane"=9、"Semenoff"=9、"non-Fermi"=4）。 |
| 2026-09-08 | **按 5 块演绎结构整体重写**（应用户要求；方法论：理论论文是"白箱演绎"非"黑箱溯因"）。旧叙事版归档 `archive/paper_review_T28_mondal2023_prb.backup_20260908.md`。新增：模型白箱（commensurate 哈密顿量 Eq.(1)+(2)+(3) + 参数分册 + 6 条假设清单）、推导链（前提定理/模型/推导/边界四层）、结论清单（定理/估算/预言分层）、假设-结论依赖图、接口（可检验性/设计原则/T32-T35 后续修正）。全部 📜Q 事实与数字无丢失。 |
