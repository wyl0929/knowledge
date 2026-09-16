<!--
 * @Author       : AI 精读 (五块演绎结构重写)
 * @Date         : 2026-08-06（初读）→ 2026-08-11（Phase S 补充）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T07_vaezi2013_prx.md
 * @Description  : T7: Vaezi/Liang/Ngai/Yang/Kim 2013 — 栅控多层石墨烯倾斜晶界的拓扑边缘态（理论 — 紧束缚 + DFT + SPT 分类；2026-09-08 按 5 块演绎结构重写）
-->

# Paper Review: Vaezi, Liang, Ngai, Yang & Kim (2013) — 栅控多层石墨烯倾斜晶界的拓扑边缘态

| 字段 | 内容 |
|------|------|
| **编号** | T7 |
| **标题** | Topological Edge States at a Tilt Boundary in Gated Multilayer Graphene |
| **作者** | Abolhassan Vaezi, Yufeng Liang, Darryl H. Ngai, Li Yang, Eun-Ah Kim |
| **期刊** | Physical Review X 3, 021018 (2013) |
| **DOI** | 10.1103/PhysRevX.3.021018 |
| **类型** | 理论 — 倾斜晶界（tilt boundary）拓扑态（紧束缚 + DFT-LDA 第一性原理 + SPT 分类，无输运实验） |
| **课题组** | Kim（Cornell）/ Yang（Washington U. St. Louis） |
| **PDF** | ✅ `reference/pdfs/Vaezi 等 - 2013 - Topological Edge States at a Tilt Boundary in Gated Multilayer Graphene.pdf`（正文 9 页 + Appendix） |
| **精读日期** | 2026-08-06（初读）→ 2026-08-11（Phase S）→ 2026-09-08（5 块重写） |

> **结构说明**：按「理论论文演绎结构」五块记（`note/shared/method/theory_paper_reading.md` §3）。
> **共享知识引用**：谷 Chern 数 → `[PHY-BERRY]`；SPT 分类 → 本文特有（Wen 框架）。

---

## TL;DR

**本文想解决的理论问题**：近期成像的 AB-BA 倾斜晶界（tilt boundary，CVD/外延石墨烯天然结构缺陷）在栅控多层石墨烯中能否承载拓扑保护的无隙边缘态？其对称性保护分类是什么？

**主结果**：① 紧束缚（$t=2.8$ eV、$t_\perp=0.4$ eV、$\Delta=0.5$ eV）+ DFT-LDA（3.1 nm 宽畴壁、1.5 nm 宽域、5 V/nm）双线证实 AB-BA 倾斜晶界承载**无隙边缘态**（每谷每自旋 2 条；DFT 显示两条 1D Dirac 色散 $K_1,K_2$，应变致其能量分裂）📜Q；② 倾斜晶界 = 谷 Chern 数 $C_K=-C_{K'}=(N/2)\,\text{sgn}(t_\perp\Delta)$ 反号的界面 → $\Delta C_K=N\,\text{sgn}(t_\perp\Delta)$ → 每谷 $N$ 条螺旋边缘态 📜Q；③ 用 Wen 的 SPT 框架把 QVH（量子谷霍尔）识别为**Z 型 SPT**（由时间反演 + 无谷混合 + $U(1)_c$ 电荷守恒保护），给出对称性改变下的相变表（LAF = Z₂ 而非 Z）📜Q。

**结论/意义**：把"结构性拓扑缺陷承载拓扑态"从理论兴趣推进为**首个具体可实现实例**，并可能解释带隙 BLG 的亚隙电导之谜（倾斜晶界网络 → 2D variable-range hopping $R(T)\propto\exp(T_0/T)^{1/3}$）。⚠️ 全文为理论预言，作者用词 show / predict / propose / expect，非实验验证。

---

## 1. 模型白箱（理想系统 + 假设清单）

### 1.1 哈密顿量

**(a) 紧束缚**（AB 堆叠区，Eq. 1）📜Q：

$$
H_{AB}=-t\sum_{i=1}^{2}\sum_{m,n}a_{m,n}^{(i)\dagger}\left(b_{m,n}^{(i)}+b_{m-1,n}^{(i)}+b_{m,n-1}^{(i)}\right)+\Delta\sum_{i=1}^{2}\sum_{m,n}(-1)^i\left(a_{m,n}^{(i)\dagger}a_{m,n}^{(i)}+b_{m,n}^{(i)\dagger}b_{m,n}^{(i)}\right)-t_\perp\sum_{m,n}a_{m,n}^{(1)\dagger}b_{m,n}^{(2)}+\text{H.c.}
$$

- $i=1,2$ 层指标；$t$、$t_\perp$ 层内/层间最近邻跃迁；$\Delta$ = 栅压导致的两层化学势差；$(m,n)$ 双位单胞位置。BA 区仅层间项换成 $-t_\perp\sum b_{m,n}^{(1)\dagger}a_{m,n}^{(2)}+\text{H.c.}$ 📜Q。
- 参数：$t=2.8$ eV、$t_\perp=0.4$ eV、$\Delta=0.5$ eV；系统 200 单胞（每方向 PBC，每域 100 单胞宽，两条 sharp tilt boundaries）📜Q。

**(b) 低能有效哈密顿量**（K 谷，AB/BA 双层，Eq. 2）📜Q：

$$
H_K^{AB-BA}=v_F k_x(\pm\sigma_x\tau_0)+v_F k_y(\sigma_y\tau_0)-\frac{\Delta}{2}(\sigma_0\tau_z)\pm\frac{t_\perp}{2}(\sigma_x\tau_x)\mp\frac{t_\perp}{2}(\sigma_y\tau_y),
$$

- $v_F=3ta/2$；$\sigma_i$ 作用于子格、$\tau_i$ 作用于层；± 对应 AB/BA。$H_{K'}(k_x,k_y)=H_K(-k_x,k_y)$ 📜Q。
- **AB↔BA 等价**：$\sigma_0\tau_x\,H_K^{AB}(\Delta)\,\sigma_0\tau_x=H_K^{BA}(-\Delta)$（Eq. 3）——BA = AB 加相反栅极性 📜Q。

### 1.2 参数分册

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | $\Delta$（层间势差）、$t_\perp$、$\vec b$ vs $\vec t$ 夹角（0°–90°）、畴壁宽度 |
| **导出量（由旋钮+常数算出）** | 谷 Chern 数 $C_K=(N/2)\,\text{sgn}(t_\perp\Delta)$、$\Delta C_K=N\,\text{sgn}(t_\perp\Delta)$、$v_F=3ta/2$ |
| **模型内部量（解的性质）** | 边缘态能带、$K_1,K_2$ Dirac 点分裂、SPT 分类（Z/Z₂/…） |
| **固定常数** | $t=2.8$ eV、$t_\perp=0.4$ eV（紧束缚）；$a$（原子间距，$|\vec b|=a$） |
| **预言量（可检验）** | 无隙边缘态、谷过滤、$R(T)\propto\exp(T_0/T)^{1/3}$、各向异性 $R_{13}\gg R_{24}$ |

> 无"反推量 θ̂"层。**符号防混**：$\Delta$ = 两层化学势差（= 栅压势差），**不是**能隙本身（能隙由 $\Delta$ 与 $t_\perp$ 共同打开）；$\vec b$（Burgers 矢量，$|\vec b|=a$）≠ 磁通量。

### 1.3 显式假设清单

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **无谷混合（no-valley mixing）**：SPT 保护三对称之一 | 模型/推导 | 📜Q |
| A2 | **时间反演 T 保持** | 模型/推导 | 📜Q |
| A3 | **电子数守恒 $U(1)_c$**（+ 谷极化守恒 $U(1)_v$） | 模型/推导 | 📜Q |
| A4 | **单粒子**（SPT 是非相互作用费米子分类；关联仅在边缘作 Luttinger 液体提及） | 模型 | 📜Q（Sec. II 末尾） |
| A5 | **spin-degenerate**（正文主结论"spin-degenerate tilt boundaries"；自旋作为动力学自由度见 Table II） | 模型 | 📜Q |
| A6 | **DFT-LDA**（局部密度近似） | 推导 | 📜Q |
| A7 | **微扰论 Berry 曲率积分延拓到 ∞**（线性色散延拓） | 推导 | 📜Q |

---

## 2. 推导链（演绎结构：顺论文顺序）

### 2.0 总览

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 前提定理层 | I 引言（背景 + 亚隙之谜） | 栅极带隙 BLG、亚隙电导、tilt boundary 成像 | 问题设定 | 实验背景（refs 1–8） | — |
| 模型层 | II 双层倾斜晶界（TB + DFT） | 紧束缚 + DFT-LDA | 无隙边缘态、$K_1,K_2$ 分裂 | A1–A6 | 谷守恒 |
| 推导层 | III SPT 分类 | 低能有效理论 + Wen 框架 | Z 型 SPT、相变表 | A1–A3、A7 | 对称性保护 |
| 边界层 | IV 实验关联 | 倾斜晶界网络 | $R(T)\propto\exp(T_0/T)^{1/3}$、四类实验 | 变程跳跃（refs 36,37） | 低温 |

### 2.1 模型层：紧束缚 + DFT 证实边缘态

- **紧束缚**：$t=2.8$ eV、$t_\perp=0.4$ eV、$\Delta=0.5$ eV、200 单胞系统 → K 与 K' 谷**每谷每自旋 2 条**边缘态；右/左行模在两条边缘空间分离 → 天然谷过滤（Fig. 2(c)）📜Q。
- **DFT-LDA**：周期超胞两条 tilt boundary（Burgers 矢量同 TB），畴壁 3.1 nm 宽、域 1.5 nm 宽、5 V/nm 电场，弛豫至力 <0.5 eV/nm → 两条无隙 1D Dirac 色散（$K_1,K_2$ 点）；压缩应变抬高、拉伸应变降低 Dirac 点能量；此分裂在更宽畴壁下可忽略 📜Q。
- **谷过滤机制**：$K_1$ 态局域在压缩应变层、$K_2$ 在拉伸应变层（与电场方向无关）→ 层选择性接触 = 谷过滤 📜Q。
- **关联注**：宽畴壁下边缘态前向散射主导 → Luttinger 液体行为（ref 24）📜Q。

### 2.2 推导层：AB↔BA 映射 + SPT 分类

- **AB↔BA 等价于栅极性反号**（Eq. 3）→ tilt boundary（AB-BA）等价于 Martin et al.（ref 13，= T1）的结构均匀双层栅极性畴壁 📜Q。
- **谷 Chern 数**（Eq. 4）：$C_K=-C_{K'}=(N/2)\,\text{sgn}(t_\perp\Delta)$；tilt boundary 处符号反转 → $\Delta C_K=-\Delta C_{K'}=N\,\text{sgn}(t_\perp\Delta)$ → 每谷 $N$ 条螺旋边缘态（只要两谷仍区分）📜Q。
- **SPT 分类（Wen 框架）**：三步（找同对称无隙 Dirac 哈密顿量 → Majorana 基写对称量与守恒量 → 找反易质量矩阵空间）。对 chiral 多层：Clifford 代数 Cliff(3,2)，质量矩阵空间 $\pi_0(C_M)=\mathbb Z$ → **Z 型 SPT**（QVH，三对称齐备时）📜Q。
- **对称性改变 → 相变**（Table I 无自旋 / Table II 含自旋）：破 T → Z⊕Z（intravalley QAH）；加谷间散射 → Z（intervalley QAH）；破 $U(1)_c$ → TSC；**LAF 相 = Z₂**（自旋-谷 Chern 数 $C_{SV}$ mod 2，每谷奇数模）；QSH = Z（多重时间反演算符）📜Q。
- 谷间散射（破坏 $U(1)_v$）是唯一通向无边缘态平凡相的路径 📜Q；但大动量转移一般需细调（除非单胞放大或短程无序如空位）📜Q。

### 2.3 边界层：实验关联与亚隙之谜

- **任意 $\vec b$-$\vec t$ 夹角**：armchair 型（$\vec b\parallel\vec t$）边缘态开小 gap（armchair 放大单胞、K/K' 投影重合，类 ref 20）；但 zigzag 型（$\vec b\perp\vec t$）无隙。观察到的倾斜晶界宽（5–20 nm）→ 预期几乎所有直 tilt boundary 近无隙（除小夹角）📜Q。
- **亚隙之谜**：倾斜晶界弯曲时有无隙/小 gap 分段 → 传输靠 gap 区间跳跃 → 2D 网络给出 $R(T)\propto\exp(T_0/T)^{1/3}$（refs 36,37），与 Oostinga/Yan-Fuhrer 低温电阻一致 📜Q。
- **四类实验预言**：(1) 四端输运 $R_{13}\gg R_{24}$（各向异性）；(2) STS（晶界无隙、远处隙）；(3) 热电势成像（晶界网络中态密度）；(4) 扫描 SQUID（边缘流磁场成像）📜Q。

---

## 3. 结论清单（分层：定理 / 估算 / 预言）

### 3.1 定理式主张（拓扑/对称性论证产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 谷 Chern 数 | $C_K=-C_{K'}=(N/2)\,\text{sgn}(t_\perp\Delta)$ | A1、A7 |
| tilt boundary 谷 Chern 数跳变 | $\Delta C_K=N\,\text{sgn}(t_\perp\Delta)$ → 每谷 $N$ 条螺旋边缘态 | A1 |
| SPT 分类 | chiral 多层 = Z 型 SPT（QVH，三对称齐备） | A1、A2、A3 |
| LAF 相 | Z₂（$C_{SV}$ mod 2，每谷奇数模） | A1、A2 |

### 3.2 估算（数值/近似，非严格定理）

| 估算 | 值 | 证据 |
|---|---|---|
| 紧束缚参数 | $t=2.8$ eV、$t_\perp=0.4$ eV、$\Delta=0.5$ eV | 📜Q[~] |
| 系统大小 | 200 单胞/方向，每域 100 单胞 | 📜Q[~] |
| DFT 几何 | 3.1 nm 畴壁、1.5 nm 域、5 V/nm、力 <0.5 eV/nm | 📜Q[~] |
| 亚隙之谜背景 | 光学隙大至 250 meV（ref 3） | 📜Q[~] |
| 典型畴壁宽 | 5–20 nm（Fig. 1 caption） | 📜Q[~] |
| 边缘态数 | 每谷每自旋 2 条（$N=2$） | 📜Q[~] |

### 3.3 预言

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| tilt boundary = 首个承载拓扑无隙模的结构缺陷 | "We predict ... to be the first ..." | 中——需输运/STS/SQUID |
| 亚隙电导之谜的解释 | "may explain the long-standing puzzle" | 中——需与实验温依赖对照 |
| 网络 $R(T)\propto\exp(T_0/T)^{1/3}$ | "would yield ... consistent with observed" | 中 |
| 四类实验可测 | "We propose ... to test our proposal" | 中——可设计实验 |

### 3.4 内部验证（自洽核对）

1. **TB ↔ DFT 互验**：紧束缚预言无隙边缘态，DFT-LDA（含应变与有限宽度）独立证实 → 对长程扰动（畴壁宽度、键长变化、应变）robust 📜Q。
2. **低能有效理论 ↔ 微观计算**：Eq. (4) 谷 Chern 数跳变（$N$ 条/谷）与 Sec. II 的"每谷每自旋 2 条"（$N=2$）自洽 📜Q。
3. **连续 ↔ SPT**：AB↔BA 映射（Eq. 3）+ 谷 Chern 数（Eq. 4）+ Wen 分类（Z）三线一致指向 QVH 边缘态 📜Q。

### 3.5 概念区分（分类）

| 区分 | 依据 | 结论 |
|---|---|---|
| zigzag vs armchair tilt boundary | $\vec b\perp\vec t$ vs $\vec b\parallel\vec t$ | 前者无隙，后者开小 gap |
| QVH（Z）vs LAF（Z₂）vs QSH（Z） | 对称性（Table I/II） | 三类不同 SPT |
| 谷保护（弱）vs 对称保护（SPT） | 三对称 vs 谷间散射 | 后者是本文的严格化语言 |

---

## 4. 假设-结论依赖图（含金量所在）

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性 |
|---|---|---|---|
| A1 无谷混合 | 谷间散射（破坏 $U(1)_v$） | 唯一通向无边缘态平凡相的路径 | 作者明言"the only way to arrive at a trivial phase without edge states" 📜Q |
| A1 谷间散射（短程如空位） | 空位破坏 A-B 子格对称 | 边缘态被破坏 | 但大动量转移需细调，罕见 → 预期多数 tilt boundary 有边缘态 📜Q |
| A2 破 T | 磁场 | QVH → intravalley QAH（Z⊕Z） | 相变（相变需闭重开能隙）📜Q |
| A5 自旋动力学 | LAF 相 | Z → Z₂ | 每谷奇数模（Velasco 2012 观测到闭重开）📜Q |
| A4 单粒子 | 强关联 | 边缘态 → Luttinger 液体（非平凡相变，宽畴壁下前向散射主导） | 仅改变边缘态性质非存在性 📜Q |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（预言靶标）

- 四端输运各向异性 $R_{13}\gg R_{24}$；STS 晶界无隙/远处隙；热电势成像网络；扫描 SQUID 边缘流 📜Q。

### 5.2 设计原则

- **结构性缺陷 = 拓扑导线**：CVD/外延石墨烯天然 tilt boundary 无需额外图案化 📜Q。
- **层选择性接触 = 谷过滤**（$K_1$ 压缩层/$K_2$ 拉伸层）📜Q。
- **SPT 分类**给出器件设计的对称性边界：破坏哪些对称 → 相变到哪类态 📜Q。

### 5.3 后续文献修正（时间倒挂，💭I）

- **T8 Jaskólski 2016（Nanoscale）**：本文"空位/短程无序破坏边缘态"的边界在 8-55 缺陷下被检验——拓扑态仍存活（部分推翻"缺陷必杀死"直觉）。
- **T6 Zhang 2013（PNAS）**：本文 Note added 引为 complementary preprint（ref 45），二者 LSW/tilt boundary 互补。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 谷守恒前提 | armchair 型、强短程杂质使保护失效 | 📜Q |
| 紧束缚/DFT 的"脆弱模" | 局域应变 + 平带带来额外结构 | 📜Q |
| 强关联仅简提 | Luttinger 液体仅在文末提及 | 📜Q |
| 三层（$N=3$）无 DFT 验证 | 仅 Eq. (4) 推广，未做 DFT | 📜Q（Eq. 4 为一般 $N$） |
| 任意 $\vec b$-$\vec t$ 夹角微观研究未完成 | "will be presented in the future"（ref 34） | 📜Q |

## 7. 与其他工作的关系

| 工作 | 关系 |
|------|------|
| Oostinga et al. 2008（ref 1）/ Yan & Fuhrer 2010（ref 5） | 引用——亚隙电导之谜的实验来源 📜Q |
| Martin, Blanter, Morpurgo 2008（ref 13，= T1） | 直接引用——栅极性畴壁边缘态先驱；tilt boundary 映射对象 📜Q |
| Jung et al. 2011（ref 20，= T3） | 引用——谷霍尔 kink 态/armchair 小 gap 📜Q |
| Xiao, Yao, Niu 2007（ref 12） | 引用——谷霍尔电导/谷 Chern 数 📜Q |
| Zhang, Jung, Fiete, Niu, MacDonald 2011（ref 28） | 引用——chiral 多层 $C_K=(N/2)\text{sgn}(t_\perp\Delta)$ 📜Q |
| Wen 2012（ref 17） | 引用——SPT 分类框架（本文首次用于具体体系）📜Q |
| Alden et al. 2013（ref 6）等 | 引用——tilt boundary 成像实验 📜Q |

## 8. 对后续研究的影响

- 把畴壁拓扑态从"理想堆叠界面"推广到"**真实结构缺陷（tilt boundary）**"——CVD 石墨烯天然晶界即拓扑通道 📜Q。
- 首次把 Wen SPT 分类应用于具体 2D 体系，给出对称性-相变完整表（QVH/QAH/LAF/QSH/TSC）📜Q。
- 提出"亚隙电导 = 倾斜晶界网络"假说，为后续输运实验设定靶标 📜Q。

## 9. 理论模型映射（供计算对标）

| 映射 | 说明 |
|------|------|
| $C_K=-C_{K'}=(N/2)\,\text{sgn}(t_\perp\Delta)$ | cont.py 谷 Chern 数 📜Q |
| $t=2.8$ eV、$t_\perp=0.4$ eV、$\Delta=0.5$ eV、200 单胞 | tb.py tilt boundary 复现参数锚点 📜Q |
| DFT 几何 3.1 nm/1.5 nm/5 V/nm | 第一性原理对标（若做 DFT）📜Q |
| SPT 分类表（Table I/II） | 对称性-相变地图 📜Q |

---

## Phase S 目的接口（引用式，随项目增删）

- **Q1（edge state 如何表征）**：tilt boundary（AB-BA 晶界）承载拓扑边缘态，每谷每自旋 2 条（$N=2$），右/左行空间分离（谷过滤）；$K_1$（压缩层）/$K_2$（拉伸层）📜Q。
- **Q2（理论如何解释）**：晶界两侧谷 Chern 数 $C_K=(N/2)\,\text{sgn}(t_\perp\Delta)$ 反号 → $\Delta C_K=N\,\text{sgn}(t_\perp\Delta)$ → 每谷 $N$ 条螺旋模；SPT 分类为 Z 型 QVH 📜Q。
- **Q3（理论↔实验对应）**：CVD/外延石墨烯天然晶界即拓扑通道（无需栅压图案化）；四类实验（四端/STS/热电势/SQUID）可验证 📜Q→💭I。

> **增量价值**：T6 的 LSW 连续分类 → T7 的真实 tilt boundary（TB+DFT）+ SPT 严格化；比 T6 多了 DFT 验证与对称性相变表，是"理想模型 → 实际缺陷"的关键推广。

## 反向核对 pass (2026-09-08)

`pdftotext -layout`+`-raw` 提取到 `/tmp/T07_layout.txt`/`T07_raw.txt`，逐项 grep 核对：

| 条目 | 命中位置 | 结论 |
|------|---------|------|
| $t=2.8$ eV、$t_\perp=0.4$ eV、$\Delta=0.5$ eV | Sec. II.A | ✓ 📜Q |
| 200 单胞、每域 100 单胞 | Sec. II.A | ✓ 📜Q |
| 3.1 nm 畴壁、1.5 nm 域、5 V/nm、力 <0.5 eV/nm | Sec. II.B | ✓ 📜Q |
| $C_K=-C_{K'}=(N/2)\,\text{sgn}(t_\perp\Delta)$（Eq. 4） | Sec. III | ✓ 📜Q |
| $\Delta C_K=-\Delta C_{K'}=N\,\text{sgn}(t_\perp\Delta)$ | Sec. III | ✓ 📜Q |
| $v_F=3ta/2$、Eq. (2)(3) | Sec. III | ✓ 📜Q |
| 每谷每自旋 2 条边缘态（$N=2$） | Sec. II.A / III | ✓ 📜Q |
| Z 型 SPT、Cliff(3,2)、LAF=Z₂、QSH=Z | Sec. III / Table I/II | ✓ 📜Q |
| $R(T)\propto\exp(T_0/T)^{1/3}$ | Sec. IV | ✓ 📜Q |
| 250 meV 光学隙（ref 3）、5–20 nm 畴壁宽 | I / Fig. 1 | ✓ 📜Q |

⚠️ **修正/降级（相对旧版）**：① 旧版"armchair-like tilt boundary → 谷投影重叠 → 明显开隙"表述过强——原文是 armchair 型（$\vec b\parallel\vec t$）边缘态开**小** gap（"gap magnitude ... will be small when the tilt boundary is spread over a finite width"），且 zigzag 型无隙——已按原文措辞。② 旧版"网络电导远低于 e²/h（趋于 variable-range-hopping）"——原文是 $R(T)\propto\exp(T_0/T)^{1/3}$（2D variable-range-hopping 温依赖），未给"远低于 e²/h"这一具体数值——已改。③ 本文数值（t=2.8/t⊥=0.4/Δ=0.5/3.1 nm 等）与旧版一致，保留。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-06 | 初读（旧 5 节叙事版）。 |
| 2026-08-11 | Phase S 补充 Q2/Q3。 |
| 2026-09-08 | **按 5 块演绎结构整体重写**（应用户要求）。旧版归档 `archive/paper_review_T07_vaezi2013_prx.backup_20260908.md`。修正：① armchair 型 tilt boundary 措辞（"明显开隙"→"小 gap，随畴壁展宽减小"）；② 删除"网络电导远低于 e²/h"无源表述，改为 $R(T)\propto\exp(T_0/T)^{1/3}$；③ 补 SPT 分类表（Table I/II）与 LAF=Z₂ 细节。 |
