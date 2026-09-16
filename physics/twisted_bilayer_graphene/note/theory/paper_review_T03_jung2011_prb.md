<!--
 * @Author       : AI 精读 (五块演绎结构重写)
 * @Date         : 2026-08-06（初读）→ 2026-08-11（Phase S 补充）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T03_jung2011_prb.md
 * @Description  : T3: Jung/Zhang/Qiao/MacDonald 2011 — 多层石墨烯谷霍尔扭结态与边缘态（理论 — 紧束缚 + 连续模型；2026-09-08 按 5 块演绎结构重写）
-->

# Paper Review: Jung, Zhang, Qiao & MacDonald (2011) — 多层石墨烯中的谷霍尔扭结与边缘态

| 字段 | 内容 |
|------|------|
| **编号** | T3 |
| **标题** | Valley-Hall Kink and Edge States in Multilayer Graphene |
| **作者** | Jeil Jung, Fan Zhang, Zhenhua Qiao, Allan H. MacDonald |
| **期刊** | Physical Review B 84, 075418 (2011) |
| **DOI** | 10.1103/PhysRevB.84.075418 |
| **类型** | 理论 — π 轨道紧束缚 + 低能连续模型（无实验数据） |
| **课题组** | MacDonald 组（UT Austin） |
| **PDF** | ✅ `reference/pdfs/Jung 等 - 2011 - Valley-Hall kink and edge states in multilayer graphene.pdf`（正文 5 页） |
| **精读日期** | 2026-08-06（初读）→ 2026-08-11（Phase S）→ 2026-09-08（5 块重写） |

> **结构说明**：按「理论论文演绎结构」五块记（`note/shared/method/theory_paper_reading.md` §3）。
> **共享知识引用**：谷 Chern 数/谷霍尔电导 → `[PHY-BERRY]`；通道计数 → `[PHY-LB]`。

---

## TL;DR

**本文想解决的理论问题**：少层石墨烯中，紧束缚模型的**堆叠方式、界面结构、垂直外电场**如何影响 1D 边缘态与扭结态（kink state）——连续模型预言（谷 Chern 数差 → 界面模数）在多大程度上可靠？

**主结果**：① 多层 ABC（手征/菱方）堆叠石墨烯的谷 Chern 数 $C_{\tau_z}=N\,\tau_z\,\text{sgn}(\Delta)/2$（$\tau_z=\pm1$ 标 K/K'），谷霍尔电导 $\sigma_{xy}^{\tau_z}=N_3^e e^2/h$（$N_3^e$ 即谷 Chern 数）📜Q；② **边缘态**只在 zigzag 边缘出现（每谷 $[N/2]$ 条，armchair 边缘因两谷投影到同一动量而湮灭），而**扭结态**在电场反号内部界面上**与晶体取向无关**地出现（每谷 $N$ 条）📜Q；③ 电场反号处谷 Chern 数差 $2\times(N/2)=N$（= 层数），Fig. 3 紧束缚显示双层/三层/四层各 2/3/4 条扭结态分支 📜Q。

**结论/意义**：把 T1 Martin 2008 的双层结果推广到多层 ABC 石墨烯，确立"**内部畴壁比样品边缘更可靠地束缚拓扑态**"——这是后续畴壁实验（Ju 2015 等）选择内部畴壁而非边缘的理论依据。⚠️ 全文为理论计算，作者用词 find / conclude / expect，非实验事实。

---

## 1. 模型白箱（理想系统 + 假设清单）

### 1.1 哈密顿量

**(a) π 轨道紧束缚模型**（Eq. 1）📜Q：

$$
H=-\sum_{\langle i,j\rangle}\gamma_{i,j}\,c_i^\dagger c_j+\sum_i U_i\,c_i^\dagger c_i
$$

- 跃迁 $\gamma_{i,j}$：层内 $t=2.6$ eV、层间 $t_\perp=0.34$ eV 📜Q（**注意**：不是常见的 2.8/0.4 eV——旧版误写）。
- $U_i$ = 晶格位置依赖的外势（模拟电场与畴壁）。

**(b) ABC 堆叠 $N$ 层低能连续模型**（Eq. 2）📜Q：

$$
H_N=-t_\perp\begin{pmatrix}0 & \nu^{\dagger N}\\ \nu^{N} & 0\end{pmatrix}+\frac{\Delta}{2}\begin{pmatrix}1&0\\0&-1\end{pmatrix}
$$

- $-t_\perp$ = 层间跃迁；$\nu=\upsilon_F\pi/t_\perp$（无量纲算符，$\upsilon_F\sim c/300$ 单层费米速度）；$\pi=\hbar(k_x+ik_y\tau_z)$，$\tau_z=\pm1$ 标 K/K'；$(k_x,k_y)$ 从 Dirac 点量起的动量；$\Delta$ = 电场产生的层间势差。
- $\nu^{\dagger N}$、$\nu^{N}$ 为 $\nu$ 的 $N$ 次幂。Bloch 态主要局域在顶/底层（无垂直邻居的子格）。

### 1.2 参数分册

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | $N$（层数）、$\Delta$（层间势差）、堆叠（ABC/ABA）、边缘取向（zigzag/armchair）、$U_i$ 位形 |
| **导出量（由旋钮+常数算出）** | 谷 Chern 数 $C_{\tau_z}=N\,\tau_z\,\text{sgn}(\Delta)/2$、谷霍尔电导 $\sigma_{xy}^{\tau_z}=N_3^e e^2/h$、界面模数差 $n=N_3^{e,l}-N_3^{e,r}$ |
| **模型内部量（解的性质）** | 边缘态/kink 态能带、模数、传播方向 |
| **固定常数** | $t=2.6$ eV、$t_\perp=0.34$ eV、$\upsilon_F\sim c/300$ |
| **预言量（可检验）** | 边缘态 $[N/2]$ 条/谷、kink 态 $N$ 条/谷、armchair 无边缘态 |

> 无"反推量 θ̂"层。**符号防混**：$\nu$ 在 Eq. (2) 中是**无量纲算符** $\upsilon_F\pi/t_\perp$（不是谷指标——谷指标是 $\tau_z$）；谷 Chern 数用 $N_3^e$（"拓扑荷"记号，取义为 3D 无隙 Fermi 点拓扑荷 $N_3$ 的维度约化）📜Q。

### 1.3 显式假设清单

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **谷守恒（无谷间散射）**："robust to long range disorder ... as long as the system is free from valley scattering perturbations" | 模型 | 📜Q |
| A2 | **最近邻 π 轨道紧束缚**（无 γ3 三邻跃迁、无 γ4） | 模型 | 📜Q |
| A3 | **低能连续近似**（Bloch 态局域顶/底层、Berry 曲率尖峰在 $k=0$） | 模型 | 📜Q |
| A4 | **单粒子**（无相互作用） | 模型 | 💭I（原文未讨论关联） |
| A5 | **理想界面/均匀电场**（正文为无谷间散射理想界面；真实短程效应见 armchair gap 讨论） | 推导 | 📜Q |
| A6 | **谷 Chern 数对奇 $N$ 为半整数**（"for odd N this quantity is not an integer; we nevertheless refer to the values as Chern indices for convenience"） | 推导 | 📜Q |

---

## 2. 推导链（演绎结构：顺论文顺序）

### 2.0 总览

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 前提定理层 | II.A 谷霍尔效应 | ABC $N$ 层连续模型 | $C_{\tau_z}=N\tau_z\,\text{sgn}\Delta/2$ | 谷 Chern 数（refs 5,6,9,21） | 谷守恒 |
| 模型层 | II.B 均匀电场多层带 | 紧束缚 + 均匀 $\Delta$ | 边缘态 $[N/2]$/谷（zigzag），armchair 无 | A1、A2 | 均匀电场 |
| 推导层 | II.C kink 态 | 电场反号界面 | kink 态 $N$ 条/谷（两种取向） | 谷 Chern 数差 $2\times N/2=N$ | 谷守恒 |
| 边界层 | III 结论 | 厚度不同的界面、ABC/ABA 对照 | 界面电子结构依赖堆叠 | A2 | 短程物理 |

### 2.1 前提定理层：ABC $N$ 层的谷霍尔效应

- **输入**：ABC（菱方）堆叠 $N$ 层低能连续模型（Eq. 2）；**输出**：谷 Chern 数 $C_{\tau_z}=N\,\tau_z\,\text{sgn}(\Delta)/2$（把 Berry 曲率对 $(k_x,k_y)$ 积分并延拓到 ∞ 得到）📜Q。对奇 $N$ 为半整数（A6）。
- 谷霍尔电导：$\sigma_{xy}^{\tau_z}=N_3^e\, e^2/h$（$N_3^e$ = 谷 Chern 数"拓扑荷"记号）📜Q。
- **界面模数**：两个谷霍尔电导不同的体区之间，每谷 1D 通道数 = 谷 Chern 数差 $n=N_3^{e,l}-N_3^{e,r}$ 📜Q；电场反号时差 = $2\times(N/2)=N$（= 层数）📜Q（Fig. 1 上排示意）。
- **弹道输运**：每通道贡献 $e^2/h$ 双端电导 📜Q（$[PHY-LB]$）。

### 2.2 模型层：均匀电场下的多层带（边缘态）

- 紧束缚带结构（Fig. 2）：ABC zigzag 三层/四层带中电场开能隙 + 边缘态；armchair 无边缘态（两谷投影同一动量 → 湮灭）📜Q。
- **边缘态数**：$[N/2]$ 条/谷（$[N/2]$ 为整数部分，ref 21 一致）——真空侧谷 Chern 数 $N_3^{e,vac}=0$，故边缘态由 $N/2-0$ 取整 📜Q。zigzag 中每谷 $[N/2]$ 条反向传播、局域在对边 📜Q。
- **ABC vs ABA 对照**：偏压 ABA 多层 zigzag 也有边缘态但模式更复杂；ABA 三层偏压增加体通道数（而 ABC 开能隙）📜Q。
- 计算参数：$\Delta/t=0.1$（层间势差）；四层用 $\Delta'=\Delta/3$（内层间距更小）📜Q。

### 2.3 推导层：kink 态（电场反号界面）

- **输入**：电场在带中心反号；**输出**：$N$ 条 kink 态/谷（zigzag 与 armchair 均有，Fig. 3 红支）📜Q。
- 双层/三层/四层 zigzag 与 armchair 各显示 2/3/4 条 kink 态分支（Fig. 3）📜Q。
- **传播方向**：kink 态在给定谷有确定传播方向；zigzag 中每谷还有 2 条简并的额外边缘态分支（速度与 kink 态相反）📜Q。
- **armchair 的 kink 态为何存活**：虽然 armchair 把 K/K' 投影到同一动量（无法从带结构标谷），但 kink 态仍 robust（Fig. 3 下排）——这是本文的"surprise"之一 📜Q。
- **尖锐势的 avoided crossing gap**：电场位形在空间尖锐变化时出现"barely visible gap"（类单层 staggered potential，ref 14），势变平滑时迅速缩小 📜Q。interface 态方程（Eq. 3）：$-V(x)u+K_N(\partial_x+k_y)^N v=\varepsilon u$，$K_N(\partial_x-k_y)^N u+V(x)v=\varepsilon v$，$K_N=-t_\perp(-i\upsilon_F\hbar/t_\perp)^N$ 📜Q。

### 2.4 边界层：厚度不同的界面 + 结论

- 三层/四层厚度不同的界面：界面电子结构依赖 ABC vs ABA 堆叠；"Bulk valley Hall effect values are also unreliable at the edge" 📜Q。
- 结论：kink 态对内部电场反号界面的 robust 是"surprise"；需确定无序与路径转弯下是否持续 📜Q。

---

## 3. 结论清单（分层：定理 / 估算 / 预言）

### 3.1 定理式主张（拓扑/连续模型论证产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 谷 Chern 数 | $C_{\tau_z}=N\,\tau_z\,\text{sgn}(\Delta)/2$（奇 $N$ 半整数） | A1、A3 |
| kink 态模数 | 电场反号界面每谷 $N$ 条（差 $2\times N/2=N$） | A1 |
| 边缘态模数 | zigzag 每谷 $[N/2]$ 条；armchair 无 | A1、A2 |
| 谷霍尔电导 | $\sigma_{xy}^{\tau_z}=N_3^e e^2/h$ | A1 |

### 3.2 估算（经验/数值，非严格定理）

| 估算 | 值 | 证据 |
|---|---|---|
| 计算参数 | $\Delta/t=0.1$；四层 $\Delta'=\Delta/3$ | 📜Q[~] |
| 层内/层间跃迁 | $t=2.6$ eV、$t_\perp=0.34$ eV | 📜Q[~] |
| kink 态分支数 | $N=2,3,4$ → 2/3/4 条（Fig. 3） | 📜Q[~] |
| armchair avoided gap | "barely visible"，随势平滑迅速缩小（未给具体数值） | 📜Q[~] |

> ⚠️ 本文**未**给出 armchair avoided gap 的定量数值（如 $0.0014t$ 是 **T4 Qiao 2011** 的数值，非本文）——不跨论文迁移。

### 3.3 预言

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| 不同厚度界面出现 kink 态（模式数 ∝ Berry 曲率积分差） | "suggest / should occur" | 中——紧束缚已验证界面依赖堆叠 |
| kink 态在无序与转弯下是否持续 | "It is important to determine if it persists..." | 中——T4 Qiao 2011 接续解答 |

### 3.4 内部验证（自洽核对）

1. **连续模型 ↔ 紧束缚互验**：连续模型预言（kink 态 $N$ 条/谷）与紧束缚带结构（Fig. 3）一致 📜Q。
2. **zigzag vs armchair 对照**：同一 kink 态在两种取向下都 robust，而边缘态只在 zigzag——区分"边缘态 vs kink 态"的关键对照 📜Q。

### 3.5 概念区分（分类）

| 区分 | 依据 | 结论 |
|---|---|---|
| 边缘态 vs 扭结态 | 位置（真空边界 vs 内部界面）+ 取向依赖 | kink 态取向无关，边缘态只 zigzag |
| 整数 vs 半整数谷 Chern 数 | $N$ 奇偶 | 奇 $N$ 半整数，模数取整 $[N/2]$ |
| ABC vs ABA | 堆叠 | ABC 开能隙有边缘态；ABA 模式复杂 |

---

## 4. 假设-结论依赖图（含金量所在）

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性 |
|---|---|---|---|
| A1 谷守恒 | 谷间散射 | 1D 态不再拓扑保护 | 作者明言"topologically protected **when valley mixing is neglected**" 📜Q |
| A5 理想界面 | 原子尺度尖锐势 | armchair kink 态开小 gap | 非致命，gap 随势平滑迅速缩小 📜Q |
| A2 最近邻 TB | 短程晶界效应 | 界面电子结构改变 | "连续模型 picture 可被界面原子尺度物理 invalidated"（不同厚度界面）📜Q |
| A3 低能连续 | 极低载流子密度/弱电场 | 谷 Chern 数 $=N/2$ 需修正 | "except possibly at very low carrier densities and weak electric fields" 📜Q |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（预言靶标）

- zigzag 带中 $[N/2]$ 边缘态 + $N$ 条 kink 态；armchair 无边缘态但 kink 态存活——可用纳米带紧束缚直接复现（本文已给 Fig. 2/3）📜Q。

### 5.2 设计原则

- **内部畴壁优于样品边缘**：畴壁态不依赖晶体取向（zigzag/armchair 均有），是更可靠的拓扑平台 📜Q。
- 多层 $N$ 层 → $N$ 条/谷通道 → 更大的谷霍尔电导（可作层数标度探针）📜Q→💭I。

### 5.3 后续文献修正（时间倒挂，💭I）

- **T4 Qiao 2011（Nano Lett）**：接续本文"kink 态在无序/转弯下是否持续"——NEGF 证明确实 robust（本批下一篇）。
- **T6 Zhang 2013 / T7 Vaezi 2013**：把 $N_3^e$（谷 Chern 数）语言推广到 LSW/tilt boundary。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 谷守恒前提 | 无谷间散射时保护才成立 | 📜Q |
| 最近邻 TB | 无 γ3/γ4（真实石墨烯有） | 📜Q（模型定义） |
| 无序/温度未处理 | kink 态输运是否存活留待后续 | 📜Q（"determine if it persists in the presence of disorder"） |
| 不同厚度界面仅定性 | "unreliable at the edge" 无定量 | 📜Q |

## 7. 与其他工作的关系

| 工作 | 关系 |
|------|------|
| Martin, Blanter, Morpurgo 2008（ref 5，= T1） | 直接引用——电场反号诱导 1D 态的先驱；本文是其多层推广 📜Q |
| Castro et al.（ref 10） | 引用——zigzag 双层带边缘态的最早数值研究 📜Q |
| Morpurgo et al.（ref 13） | 引用——识别为谷霍尔边缘态 📜Q |
| Li et al. 2010（ref 16，= T2） | 引用——边缘态存在依赖边缘形貌的最近分析 📜Q |
| Zhang, Jung, Fiete, Niu, MacDonald 2011（ref 21） | 引用——手征堆叠少层的量子霍尔/谷 Chern 数 $[N/2]$ 📜Q |
| Min & MacDonald 2008（ref 18） | 引用——连续模型来源 📜Q |

## 8. 对后续研究的影响

- 把 T1 双层结果推广到多层 ABC，给出"kink 态 = $N$ 条/谷、边缘态 = $[N/2]$ 条/谷"的层数标度律 📜Q。
- 确立"内部畴壁比边缘可靠"的实验设计原则——为 Ju 2015/Li 2016 选择内部畴壁提供理论先例 📜Q→💭I。

## 9. 理论模型映射（供计算对标）

| 映射 | 说明 |
|------|------|
| $C_{\tau_z}=N\tau_z\,\text{sgn}\Delta/2$ → tb.py 模数核对 | 畴壁模数 = 两侧差；边缘模数 $[N/2]$ 📜Q |
| Eq. (2) 连续模型 → cont.py | $H_N$ 两分量（顶/底层）+ $\nu^N$ 幂次耦合 📜Q |
| $\Delta/t=0.1$、$t=2.6$ eV、$t_\perp=0.34$ eV | TB 复现参数锚点 📜Q |

---

## Phase S 目的接口（引用式，随项目增删）

- **Q1（edge state 如何表征）**：zigzag 边缘态 $[N/2]$/谷 vs armchair 无；kink 态（内部电场反号界面）$N$ 条/谷且取向无关——kink 态是更稳健的探针 📜Q。
- **Q2（理论如何解释）**：谷 Chern 数 $N_3^e=N\tau_z\,\text{sgn}\Delta/2$ → 界面差 $N$（反号）或 $[N/2]$（真空）→ 对应 1D 通道数 📜Q。
- **Q3（理论↔实验对应）**：模式支数 = 层数 $N$ → 电导阶数可验证；内部畴壁不依赖晶体取向 → 实验应选畴壁而非边缘 📜Q→💭I。

> **增量价值**：T1 的多层推广 + "边缘 vs kink 区分"；与 T4 分工——本文是能带结构/模数分类，T4 是 NEGF 输运（无序/转弯 robust）。

## 反向核对 pass (2026-09-08)

`pdftotext -layout`+`-raw` 提取到 `/tmp/T03_layout.txt`/`T03_raw.txt`，逐项 grep 核对：

| 条目 | 命中位置 | 结论 |
|------|---------|------|
| $t=2.6$ eV、$t_\perp=0.34$ eV | Sec. II 紧束缚定义 | ✓ 📜Q |
| $C_{\tau_z}=N\,\tau_z\,\text{sgn}(\Delta)/2$ | Sec. II.A | ✓ 📜Q |
| $\sigma_{xy}^{\tau_z}=N_3^e e^2/h$、$n=N_3^{e,l}-N_3^{e,r}$ | Sec. II.A | ✓ 📜Q |
| 电场反号差 $2\times(N/2)=N$ | Sec. II.A | ✓ 📜Q |
| 边缘态 $[N/2]$/谷、armchair 无 | Sec. II.B / III | ✓ 📜Q |
| kink 态 2/3/4 条（$N=2,3,4$） | Fig. 3 caption | ✓ 📜Q |
| $\Delta/t=0.1$、四层 $\Delta'=\Delta/3$ | Sec. II.B | ✓ 📜Q |
| $K_N=-t_\perp(-i\upsilon_F\hbar/t_\perp)^N$、Eq. (3) | Sec. II.A | ✓ 📜Q |
| $\upsilon_F\sim c/300$ | Sec. II.A | ✓ 📜Q |

⚠️ **修正/降级（相对旧版）**：① 旧版"$t=2.8$ eV、$t_\perp=0.4$ eV"是常识脑补参数，原文为 $t=2.6$ eV、$t_\perp=0.34$ eV——已改。② 旧版"σ^v_xy = N e²/2h"与"每谷 N 条界面通道"部分正确但漏了"边缘态 $[N/2]$ vs kink 态 $N$"这一关键区分——已补。③ armchair avoided gap 无定量数值（旧版未写数值，正确），不引入 $0.0014t$（那是 T4 的）。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-06 | 初读（旧 5 节叙事版）。 |
| 2026-08-11 | Phase S 补充 Q2/Q3。 |
| 2026-09-08 | **按 5 块演绎结构整体重写**（应用户要求）。旧版归档 `archive/paper_review_T03_jung2011_prb.backup_20260908.md`。修正：① 紧束缚参数 $t=2.8$ eV/$t_\perp=0.4$ eV 常识脑补 → 改 $2.6$/$0.34$ eV；② 补"边缘态 $[N/2]$ vs kink 态 $N$"分层；③ 符号防混（$\nu$=无量纲算符 ≠ 谷指标 $\tau_z$；$N_3^e$=谷 Chern 数）。 |
