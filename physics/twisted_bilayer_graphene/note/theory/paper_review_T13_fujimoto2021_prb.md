<!--
 * @Author       : AI 精读 (research_onboarding_skill, Phase 4) → 2026-09-08 按 5 块演绎结构重写
 * @Date         : 2026-08-06（初读）→ 2026-09-08（5 块重写 + 反向核对）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T13_fujimoto2021_prb.md
 * @Description  : T13: Fujimoto & Koshino 2021 — Moiré 边缘态与滑动陈数量子泵浦（理论；2026-09-08 按五块演绎结构重写：模型白箱/推导链/结论清单/假设-结论依赖图/接口）
-->

# Paper Review: Fujimoto & Koshino (2021) — TBG 的 Moiré 边缘态及其与量子泵浦的拓扑关系

| 字段 | 内容 |
|------|------|
| **编号** | T13 |
| **标题** | Moiré edge states in twisted bilayer graphene and their topological relation to quantum pumping |
| **作者** | Manato Fujimoto, Mikito Koshino |
| **期刊** | Physical Review B 103, 155410 (2021) |
| **DOI / arXiv** | 10.1103/PhysRevB.103.155410 / arXiv:2012.02537（⚠️ arXiv 号正文未出现，标外部来源） |
| **类型** | 理论 — 边缘态拓扑 / 体-边对应（紧束缚纳米带 + 滑动陈数，无实验数据） |
| **课题组** | Osaka University（Koshino group） |
| **PDF** | ✅ `reference/pdfs/Fujimoto和Koshino - 2021 - Moiré edge states in twisted bilayer graphene and their topological relation to quantum pumping.pdf`（正文 9 页 + 2 附录） |
| **精读日期** | 2026-08-06（初读）→ 2026-09-08（5 块重写 + 反向核对） |

> **结构说明**：按「理论论文演绎结构」五块记（`note/shared/method/theory_paper_reading.md` §3）。**全文无 ±**：数字统一 📜Q[~]。

---

## TL;DR

**本文想解决的理论问题**：TBG 存在一类**依赖 Moiré 图案、远离零能**的"Moiré 边缘态"——它们是否有拓扑起源？对应哪个体不变量（体陈数为零，无 QH/QVH 边缘态）？

**主结果**：① TBG 有两类边缘态——继承自单层的 zigzag 零能模 + 本文重点的 **Moiré 边缘态**（远离零能、强依赖 Moiré 图案边界截断）📜Q；② 层间滑动 $\lambda:0\to1$ 时边缘态**从一个能带转移到另一个能带**（跨越体能隙），**泵浦的边缘态数 = 能隙的滑动陈数**（sliding Chern number）📜Q；③ 滑动陈数是 $(k_i,\lambda_j)$ 空间的 Berry 曲率积分（对比 QH 的 $(k_x,k_y)$ 陈数），仅单方向动量积分、对每个 $k_y$ 定义且受隙保护 📜Q。

**结论/意义**：建立 Moiré 体系的**新体-边对应**——滑动陈数 ↔ Moiré 边缘态泵浦（Thouless 泵浦的 Moiré 版本）📜Q。⚠️ 全文为数值理论，作者用词 show / demonstrate / find；无实验实现层间滑动的方案。

---

## 1. 模型白箱（理想系统 + 假设清单）

### 1.1 哈密顿量（无自旋、每自旋）

**Moiré 晶格**：层 $l$ 旋转 $\mp\theta/2$（$l=1,2$），Moiré 基矢 $L_i^M=[R(\theta/2)-R(-\theta/2)]^{-1}a_i=\frac{1}{2\sin(\theta/2)}R(-\pi/2)a_i$（Eq. 1），晶格常数 $L_M=a/[2\sin(\theta/2)]$（Eq. 2）📜Q。

**层间滑动**：层 $l$ 平移 $a_i^{(l)}$ → Moiré 图案恰移 $\pm L_i^M$；任意位移 $\Delta x^{(l)}=\nu_1a_1^{(l)}+\nu_2a_2^{(l)}$ → $\Delta X=\pm(\nu_1L_1^M+\nu_2L_2^M)=\frac{\pm1}{2\sin(\theta/2)}R(-\pi/2\mp\theta/2)\Delta x^{(l)}$（Eq. 4）📜Q。$\theta\ll1$ 时 $\Delta X$ **几乎垂直于**滑动方向，放大 $[2\sin(\theta/2)]^{-1}\sim1/\theta$ 倍 📜Q。

**紧束缚哈密顿量**（pz 轨道，Eq. 5）：

$$
H=-\sum_{\langle i,j\rangle}t(R_i-R_j)|R_i\rangle\langle R_j|+\mathrm{H.c.}
$$

Slater-Koster 型跃迁（Eq. 6）：

$$
-t(d)=V_{pp\pi}\Big[1-\big(\tfrac{d\cdot e_z}{d}\big)^2\Big]+V_{pp\sigma}\big(\tfrac{d\cdot e_z}{d}\big)^2,\quad
V_{pp\pi}=V_{pp\pi}^0 e^{-(d-a_0)/\delta_0},\quad V_{pp\sigma}=V_{pp\sigma}^0 e^{-(d-d_0)/\delta_0}
$$

其中 $a=0.246$ nm（石墨烯晶格常数）、$a_0=a/\sqrt3\approx0.142$ nm（最近邻距离）、$d_0\approx0.335$ nm（层间距）、$\delta_0=0.184a$（跃迁衰减长度）；$V_{pp\pi}^0,V_{pp\sigma}^0$ 为跃迁积分（**原文未给显式数值**）；$d>3a$ 指数小、略去 📜Q。

**能标**：Moiré 能带折叠能 $E_M=\hbar v(2\pi/L_M)\sim(2\pi\hbar v/a)\theta$ 📜Q。

### 1.2 参数分册（区分"作者设定" vs "推导所得"）

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | 滑动参数 $\lambda\in[0,1]$（$\Delta x^{(2)}=\lambda(1/2,-1)$）、$k_y$（能带/滑动陈数的参量）、扭角 $\theta$ |
| **导出量（由旋钮+常数算出）** | $L_M=a/[2\sin(\theta/2)]$、$\Delta X=-(1/2)L_1^M+L_2^M$、$E_M\sim(2\pi\hbar v/a)\theta$、滑动陈数 $C_{ij}^{(l)}$、极化移动 $\Delta P$ |
| **模型内部量（解的性质）** | 纳米带能谱、Moiré 边缘态/zigzag 态、泵浦边缘态数、平带波函数 |
| **固定常数** | $a=0.246$ nm、$a_0\approx0.142$ nm、$d_0\approx0.335$ nm、$\delta_0=0.184a$、$V_{pp\pi}^0,V_{pp\sigma}^0$（未给数值）、$v$（能带速度） |
| **预言量（可检验）** | Moiré 边缘态随 $\lambda$ 的谱演化、泵浦数 = 滑动陈数 |

> **符号防混**：$a$（晶格常数 0.246 nm）≠ $a_0$（最近邻距离 0.142 nm）≠ $a_i^{(l)}$（层 $l$ 基矢）；$L_M$（Moiré 周期）≠ $L_i^M$（Moiré 基矢）。**无"反推量"层**。
> ⚠️ **QC 要点**：旧 review 写 "γ₀ = −2.6 eV, γ₁ = 0.34 eV"——**原文无此数值**（Slater-Koster 只给 $V_{pp\pi}^0,V_{pp\sigma}^0$ 符号、未给值），本次删除（见更正日志）。

### 1.3 显式假设清单

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **Slater-Koster 紧束缚**（pz 单轨道） | 模型 | 📜Q |
| A2 | **放大层间跃迁 2.52 倍**（$\theta=2.65°$ 模拟 $1.05°$）——低能能带由 $t_{inter}/E_M$ 决定 | 模型 | 📜Q |
| A3 | **面内弛豫纳入、面外弛豫忽略**（后者不改 Moiré 隙拓扑） | 模型 | 📜Q |
| A4 | **无自旋**（结果按"每自旋"报告） | 模型 | 📜Q |
| A5 | **边界近 armchair 截断**（抑制单层 zigzag 边缘态干扰） | 模型 | 📜Q |
| A6 | $d>3a$ 跃迁指数小、略去 | 模型 | 📜Q |
| A7 | **绝热滑动**（Thouless 泵浦，$\lambda$ 缓慢） | 推导 | 📜Q |

---

## 2. 推导链（顺论文演绎顺序）

### 2.0 总览

| 层 | 论文内容 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 前提定理层 | 滑动陈数定义 | TBG Bloch 带 + $(k_i,\lambda_j)$ 空间 | $C_{ij}^{(l)}$（Eq. 8） | 体-边对应、Berry 曲率 | 隙内 |
| 模型层 | 纳米带紧束缚 | Slater-Koster + 2.52 放大 | $\theta=2.65°$→$1.05°$ 带结构 | A1–A6 | 5 单胞厚 |
| 推导层 | 滑动泵浦 | $\lambda:0\to1$ 谱演化 | 边缘态跨隙转移 | A7 | 每 $k_y$ 隙 |
| 边界层 | 体-边对应 | $C_{ij}^{(l)}$ + $\Delta P$ | 泵浦数 = 滑动陈数 | Eq. (9) | 隙不闭合 |

### 2.1 前提定理层：滑动陈数（Eq. 8）

- 层 $l$ 平移一个自身晶格周期 $a_i^{(l)}$ → 电子极化移动 $\Delta P=C_{i1}^{(l)}L_1^M+C_{i2}^{(l)}L_2^M$（Eq. 7，引 ref 35）📜Q。
- 滑动陈数 $C_{ij}^{(l)}=\frac{1}{2\pi}\int_0^1dk_j\int_0^1d\lambda_i\, i\sum_{n=\mathrm{occ}}\big(\langle\tfrac{\partial u}{\partial\lambda_i}|\tfrac{\partial u}{\partial k_j}\rangle-\langle\tfrac{\partial u}{\partial k_j}|\tfrac{\partial u}{\partial\lambda_i}\rangle\big)$（Eq. 8，$u=u_{nk}(\lambda_1,\lambda_2)$ 为 Bloch 本征态）📜Q。
- 低扭角下可对近解耦的 K、K′ 谷**分别定义**；时间反演对称性使两谷滑动陈数相等（附录 A）→ 总滑动陈数 = 单谷的两倍 📜Q。

### 2.2 模型层：纳米带紧束缚

- 目标魔角 $\theta=1.05°$（Moiré 单胞约 12000 原子，太贵）→ 改用 $\theta=2.65°$（少 10 倍原子）并**放大层间跃迁** $2.65°/1.05°\approx2.52$ 倍，因低能带由 $t_{inter}/E_M$ 决定而近似等价（除总能标外）；算后能量缩 $1/2.52$ 还原 📜Q（Fig. 3 对照验证）。
- 纳米带平行 y、垂直方向（x）5 个 Moiré 单胞厚、边界近 armchair 📜Q。
- 层 2 沿 y 滑动 $\Delta x^{(2)}=\lambda(1/2,-1)$（$0\le\lambda\le1$）→ Moiré 图案沿 x 移 $\Delta X=-(1/2)L_1^M+L_2^M$（恰一排 AA 点）📜Q。

### 2.3 推导层：边缘态泵浦（Fig. 4）

- $\lambda=0$ 有额外面内 $C_2$ 对称 → 上/下边界边缘态强制简并 📜Q。
- $\lambda:0\to1$：上边界两条边缘带从零能平带劈裂（正/负能两侧）→ 被吸收进激发导带/价带；同时下边界两条边缘带从激发带转入零能带 📜Q。
- 每自旋跨隙泵浦数：平带上方的隙为 **2**、第二个隙（约 0.8 eV）为 **4** 📜Q。
- 边缘态是时间反演算符的本征态（谷 K、K′ 混合）；边缘态出现与 AA 点穿过边界相关 📜Q。

### 2.4 边界层：体-边对应（Eq. 9）

- 平带上方隙（每自旋、谷求和）：$C_{11}^{(1)}=C_{22}^{(1)}=2$、$C_{11}^{(2)}=C_{22}^{(2)}=-2$、余为 0 → 极化移动 $\Delta P=\frac12(C_{11}^{(2)}L_1^M+C_{12}^{(2)}L_2^M-C_{21}^{(2)}L_1^M+C_{22}^{(2)}L_2^M)=2\Delta X$（Eq. 9）→ **每自旋 2 电子**穿过每单位胞边界 ⟂x，与边缘态泵浦数一致 📜Q。
- 第二隙（约 0.8 eV）：$C=4$ → $\Delta P=4\Delta X$ 📜Q。
- **与 QHE 类比**：滑动陈数 = $(k_i,\lambda_j)$ 空间 Berry 曲率积分（vs QH 陈数 = $(k_x,k_y)$ 环面积分）；仅单方向动量积分，另一动量作参量；对每个 $k_y$ 定义、只要固定 $k_y$（任意 $k_x$）谱有隙即拓扑保护 📜Q。
- **稳健性**：泵浦数是拓扑不变量 → 对边缘无序稳健（滑动时体电子被推向边缘，必有 in-gap 边缘态吸收多余电子，与边缘细节无关）📜Q。

---

## 3. 结论清单（分层）

### 3.1 定理式主张（拓扑论证的产物，依赖 A7 绝热滑动）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 体-边对应 | 泵浦边缘态数 = 滑动陈数（$2$ / $4$ 两个隙） | A7（绝热）、隙不闭合 |
| 极化移动 | $\Delta P=2\Delta X$（平带上隙）、$4\Delta X$（第二隙） | A7、谷求和 ×2 |
| 拓扑保护范围 | 滑动陈数对每个 $k_y$ 定义、受隙保护 | 隙保持 |

### 3.2 估算（数值，非严格定理）

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| 魔角原子数 | $\sim12000$ 原子/Moiré 单胞（$\theta=1.05°$） | A2 | 📜Q[~] |
| 放大因子 | $2.65°/1.05°\approx2.52$ | A2 | 📜Q[~] |
| 纳米带厚度 | 5 个 Moiré 单胞 | A5 | 📜Q[~] |
| 第二隙位置 | $\sim0.8$ eV | — | 📜Q[~] |

### 3.3 预言（可检验性 → §5.1）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| Moiré 边缘态随 $\lambda$ 从平带跨隙转移到激发带 | "demonstrate / show"（数值构造）📜Q | 中——纳米带谱学/STM |
| 泵浦数 = 滑动陈数（体-边对应） | "shown to be equal / can be viewed as" 📜Q | 中——需层间滑动实验 |
| 其他超晶格（graphene/hBN、TMD 双层）同类泵浦 | "is expected" 📜Q | 弱——待未来工作 |

### 3.4 内部验证（自洽核对）

1. **参数放大互验**：$\theta=2.65°$（放大层间跃迁）vs $\theta=1.05°$ 原模型带结构定量一致（除能标 2.52 因子，Fig. 3）📜Q。
2. **体-边计数互验**：边缘态泵浦数（Fig. 4 标 "2"/"4"）与滑动陈数 $\Delta P$ 计算（Eq. 9）精确一致 📜Q。
3. **多角度稳健性**：$\theta=1.47°,2.65°,6.01°$（附录 B）Moiré 隙变窄、部分 $k_y$ 闭合，但隙内泵浦数不变（滑动陈数不变）📜Q。
4. **负对照**：单层已有隙是平庸的（层间耦合可连续关闭而不闭合隙）→ 无 Moiré 泵浦 📜Q。

### 3.5 概念区分（分类，非溯因排除）

| 区分 | 依据 | 结论 |
|---|---|---|
| zigzag 态 vs Moiré 边缘态 | 零能、继承单层、对 Moiré 不敏感 vs 远离零能、依赖 Moiré 截断 📜Q | 两类边缘态并存 |
| 滑动陈数 vs 常规陈数 | $(k_i,\lambda_j)$ 空间 vs $(k_x,k_y)$ 环面 📜Q | 两种体-边对应 |
| Moiré 泵浦 vs QHE 泵浦 | 边缘态转移随 $\lambda$（vs 随动量）📜Q | 机理类比 |

---

## 4. 假设-结论依赖图（含金量所在）

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性 |
|---|---|---|---|
| A2（2.52 放大） | 高能带偏离 / $t_{inter}$ 非小 | $\theta=1.05°$ 定量还原 | 已用 Fig. 3 互验（定量一致）📜Q |
| A3（忽略面外弛豫） | 面外弛豫改变拓扑 | Moiré 隙拓扑 | 作者论证不改拓扑 📜Q |
| A7（绝热滑动） | 非绝热 / 层间摩擦 | 泵浦图景 | 未讨论实用实现 💭I |
| 隙不闭合 | 大角度部分 $k_y$ 闭合 | 滑动陈数定义 | 隙内仍成立（附录 B）📜Q |
| A4（无自旋） | 自旋轨道耦合 | 每自旋计数 | 未讨论 💭I |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（实验靶标）

- Moiré 边缘态谱随 $\lambda$ 的跨隙演化（纳米带谱学/STM）📜Q；
- 泵浦数 = 滑动陈数（需可控层间滑动的器件）📜Q；
- Moiré 边缘态对边界截断方式的高敏感性（区分于 zigzag 态）📜Q。

### 5.2 设计原则

层间滑动 → 电荷泵浦（Thouless 泵浦 Moiré 版）+ 边缘态可编程转移 💭I（本文 "can be viewed as / is expected"）。

### 5.3 后续文献修正（时间倒挂，💭I）

- **T12（Tsim 2020, TZM）**：同组互补——TZM 是畴壁内 1D 态，本文是 TBG 纳米带边界上的 Moiré 边缘态；两图景共享滑动陈数数学结构。
- **Fujimoto/Koschke/Koshino 2020 (ref 35)**：滑动陈数原始定义——本文是其体-边对应的直接实现。
- **与 QHE 体-边对应**（Hatsugai 1993, ref 4,5）：方法论祖先。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 无相互作用 | 仅无相互作用紧束缚 | 📜Q（单粒子模型） |
| 层间滑动实验难 | 未讨论可控滑动实现 | 💭I（原文 "left for future work"） |
| 仅魔角附近为主 | 主文 $\theta=1.05°$（附录扩展到 1.47–6.01°） | 📜Q |
| 无自旋 | 结果按每自旋报告 | 📜Q |
| 参数放大近似 | 2.52 放大依赖 $t_{inter}/E_M$ 标度 | 📜Q（A2） |

## 7. 与其他工作的关系（跨论文对标放这里）

| 工作 | 关系 |
|------|------|
| Fujimoto/Koschke/Koshino 2020 (ref 35) | 引用——滑动陈数定义来源 |
| Zhang/Gao/Xiao 2020 (ref 36)、Su/Lin 2020 (ref 37) | 引用——滑动陈数并行提出 |
| Fleischmann 2018 (ref 32)、Liu/Dai 2019 (ref 33) | 引用——Moiré 边缘态先导 |
| Landgraf 2013 / Morell 2014 等 (ref 28–31) | 引用——zigzag 零能边缘态 |
| Hatsugai 1993 (ref 4,5) / Thouless 1983 (ref 38) | 引用——QHE 体-边对应 / Thouless 泵浦祖先 |
| Nam & Koshino 2017 (ref 43) | 引用——面内弛豫（Moiré 隙来源） |

> ⚠️ Phase S 外部对标（**非本文引用**，时间倒挂 💭I）见 §5.3。

## 8. 对后续研究的影响

- 确立 **Moiré 体系的新体-边对应**（滑动陈数 ↔ 边缘态泵浦）📜Q。
- 把层间滑动映射为绝热泵浦、Berry 曲率在 $(k_y,\lambda)$ 空间——Moiré 拓扑的新范式 📜Q。
- 预言 graphene/hBN、TMD 双层等超晶格的 Moiré 泵浦（"left for future work"）📜Q。

## 9. 理论模型映射（供 TBPM 计算对标）

| 映射 | 说明 |
|------|------|
| Slater-Koster 跃迁 | Eq. (6)：$V_{pp\pi}=V_{pp\pi}^0 e^{-(d-a_0)/\delta_0}$、$V_{pp\sigma}=V_{pp\sigma}^0 e^{-(d-d_0)/\delta_0}$，$\delta_0=0.184a$，$d>3a$ 截断 📜Q |
| 纳米带几何 | 平行 y、x 向 5 Moiré 单胞、armchair 截断 📜Q |
| 滑动协议 | $\Delta x^{(2)}=\lambda(1/2,-1)$、$\lambda\in[0,1]$ → $\Delta X=-(1/2)L_1^M+L_2^M$ 📜Q |
| 滑动陈数 | Eq. (8) $(k_j,\lambda_i)$ 空间 Berry 曲率积分；$\Delta P$ Eq. (9) 📜Q |
| 能标还原 | $\theta=2.65°$ ×2.52 → $1.05°$，能量缩 $1/2.52$ 📜Q |

---

## Phase S 目的接口（引用式，随项目增删）

- **Q1（edge state 如何表征）**：给出 Moiré 边缘态谱特征——远离零能、强依赖边界截断、随 $\lambda$ 跨隙转移（区分 zigzag 零能态）📜Q；纳米带谱/STM 靶标。
- **Q2（理论如何解释）**：Moiré 边缘态 ↔ 滑动陈数泵浦的体-边对应（$(k_y,\lambda)$ 空间 Berry 曲率）📜Q。与 T12（TZM 畴壁态）互补而非同一概念。
- **Q3（理论↔实验对应）**：$\lambda$ ↔ 层间滑动位移、泵浦数（2/4）↔ 边缘态转移计数、MoIré 边缘态谱 ↔ 纳米带测量 📜Q。

> **增量价值**：与 T12（TZM 畴壁内 1D 态）分工——本文是 **TBG 纳米带边界上的 Moiré 边缘态**（非畴壁态），贡献滑动陈数体-边对应这一新拓扑原理。report 可用数字（均 📜Q）：$\theta=2.65°$、放大 2.52、5 单胞、泵浦数 2/4、$a=0.246$ nm、$a_0\approx0.142$ nm、$d_0\approx0.335$ nm。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` 提取正文到 `/tmp/T13.txt`，逐项 grep 核对：

| 数字/公式 | grep 命中位置 | 结论 |
|------|--------------|------|
| $a=0.246$ nm、$a_0\approx0.142$ nm、$d_0\approx0.335$ nm、$\delta_0=0.184a$ | §II B | ✓ 📜Q[~] |
| $\theta=2.65°$、$1.05°$、放大 2.52、~12000 原子 | §II B + Fig. 3 | ✓ |
| 5 个 Moiré 单胞厚 | §II A | ✓ |
| 滑动矢量 $\lambda(1/2,-1)$、$\Delta X=-(1/2)L_1^M+L_2^M$ | §II A | ✓ |
| 泵浦数 2（平带隙）、4（~0.8 eV） | Fig. 4 + §III B | ✓ |
| $C_{11}^{(1)}=C_{22}^{(1)}=2$、$C_{11}^{(2)}=C_{22}^{(2)}=-2$、$\Delta P=2\Delta X$、$4\Delta X$ | §III B Eq. (9) | ✓ |
| $\theta=1.47°,2.65°,6.01°$ | 附录 B | ✓ |
| $d>3a$ 截断 | §II B | ✓ |

⚠️ **修正/降级**：① **删除旧 review 无源参数 "γ₀ = −2.6 eV, γ₁ = 0.34 eV"**——原文全文 grep `2.6|0.34|γ0|γ1` 零命中（Slater-Koster 仅给 $V_{pp\pi}^0,V_{pp\sigma}^0$ 符号，未给数值），属"常识脑补参数"（陷阱②）；② 旧 review "AB 振荡的规范场解释" 已在此前（08-19）确认不存，本次保持无 AB 振荡表述；③ 其余数字重 grep 全命中。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-06 | 初读（research_onboarding Phase 4），叙事体 8 节。 |
| 2026-08-20 | S-REV：确认"AB 振荡的规范场解释"不存于本 review（grep 无 "Aharonov"），仅登记。 |
| 2026-09-08 | **按 5 块演绎结构整体重写**。旧叙事体归档 `archive/paper_review_T13_fujimoto2021_prb.backup_20260908.md`。 |
| 2026-09-08 | **QC 修正**：① 删除无源参数 γ₀=−2.6 eV / γ₁=0.34 eV（原文无此数值，常识脑补）；② 全文数字重 grep 全命中；③ 补参数分册 + 7 条假设清单 + 假设-结论依赖图。 |
