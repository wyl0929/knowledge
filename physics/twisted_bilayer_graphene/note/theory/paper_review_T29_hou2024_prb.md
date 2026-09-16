<!--
 * @Author       : AI 精读（白箱演绎结构）
 * @Date         : 2026-08-11（初读）→ 2026-09-02（4 块辨识结构，理论版）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T29_hou2024_prb.md
 * @Description  : T29: Hou, Yuan & Jiang 2024 PRB — 偏压 mTBG 的 1D 导电通道阵列（理论裁决 NQCP；2026-09-08 按 5 块演绎结构重写：模型白箱/推导链/结论清单/假设-结论依赖图/接口）
-->

# Paper Review: Hou, Yuan & Jiang (2024) — mTBG 中 1D 导电通道阵列

| 字段 | 内容 |
|------|------|
| **编号** | T29 |
| **标题** | Arrays of one-dimensional conducting channels in minimally twisted bilayer graphene |
| **作者** | Zhe Hou, Kai Yuan, Hua Jiang |
| **期刊** | Physical Review B 110, L161406 (2024)（Letter，received 20 Aug 2024 / published 15 Oct 2024）📜Q |
| **DOI / arXiv** | 10.1103/PhysRevB.110.L161406 / arXiv:2408.09843（⚠️ arXiv 号正文未出现，标外部来源） |
| **类型** | 理论 — 量子输运模拟（紧束缚 + NEGF）裁决 TZM vs 网络 |
| **课题组** | Hua Jiang 组（Fudan；一作 Zhe Hou，Nanjing Normal University） |
| **PDF / SI** | ✅ `reference/pdfs/Hou 等 - 2024 - Arrays of one-dimensional conducting channels in minimally twisted bilayer graphene.pdf`（正文 + SM §I–VII） |
| **精读日期** | 2026-08-11（初读）→ 2026-09-02（4 块辨识结构）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」的五块记（见 `note/shared/method/theory_paper_reading.md` §3）：**① 模型白箱 → ② 推导链 → ③ 结论清单（分层）→ ④ 假设-结论依赖图 → ⑤ 接口**。理论论文无黑箱、无反推、无可辨识实验（是"白箱演绎"而非"黑箱溯因"），故不用"四层变量表 + 判别表"这套实验框架词汇（旧 4 块版已废弃）。
> **共享知识引用**：量子化电导/通道计数见 `[PHY-LB]`；valley Chern/helical vs chiral 见 `[PHY-BERRY]`；网络 miniband 见 `[PHY-MB]`；AB/FP 干涉见 `[PHY-AB]`。本 review 只写"本文代入"的数字，不重复讲义。

---

## TL;DR

**本文想解决的问题**：极小扭角（minimally twisted）偏压 TBG 的畴壁拓扑螺旋态（THS）如何传播——是自组织为 **2D 三角网络**（在 AA 堆叠点被散射成三路），还是自组织为 **1D 拓扑锯齿模（TZM）** 独立传播？

**主结果**：用两端 TBG 纳米 flake 器件的紧束缚 + 非平衡格林函数（Landauer/Meir-Wingreen 形式）量子输运模拟，作者"show" THS 确实**自构 1D 畸变 TZM**、每条绕过 AA 堆叠点独立传播 📜Q。长 flake 上得到**近量子化电导平台（NQCP）**，值**接近 1、2、3（单位 2e²/h）**、非精确量子化 📜Q；算例 θ=0.82° 平台值 ~1.99（接近 2）📜Q。

**结论/意义**：这是 THS 存在 TZM 的"strong experimental sign"（作者措辞，是可检验预言而非已测事实）📜Q；裁决了十年的网络 vs TZM 之争，并在 2D 平台上实现 1D 通道阵列。

---

## 1. 模型白箱（理想系统 + 假设清单）

> 理论论文的研究对象是**白箱**——作者自写的理想模型，无需"反推内部"。本节只做两件事：**写下模型**（§1.1），**列出它成立的全部假设**（§1.3）。假设清单是本文一切结论的"前提集合"，§4 的依赖图据此展开。

### 1.1 器件模型 + 紧束缚哈密顿量 + NEGF

**器件模型**：底 = 未扭转单层 graphene nanoribbon（宽 N，以六角环数计），顶 = 扭转 graphene flake（长 L）；flat boundary 由刻蚀 [39,48,49] 或电栅控 [50,51] 实现；扭心 = 坐标原点 O（顶层相对逆时针转 θ）📜Q。两端 = 单层 graphene 引线。

**紧束缚哈密顿量**（Eq. 1，$p_z$ Wannier 基）：层内 on-site + hopping + 层间 hopping；层间偏压以 on-site 能 $(-1)^\alpha\Delta$ 计入（$\alpha=1/2$ = 顶/底层）📜Q。hopping 用 Slater-Koster（Eq. 2）：$V_{pp\pi}(r)=-\gamma_0 e^{(a-r)q_\pi/a}$、$V_{pp\sigma}(r)=\gamma_1 e^{(a_I-r)q_\sigma/a_I}$；面内 hopping 截断 $r_c=3a$（SI §I 验证 3a 合理）📜Q。

**输运公式**（Eq. 3，零温 NEGF）：
$$G(E_F)=\frac{2e^2}{h}\mathrm{Tr}[\Gamma_L G_C^r \Gamma_R G_C^a]$$
Landauer/Meir-Wingreen 形式，$G_0\equiv2e^2/h$，$E_F$ 相对 TBG 电荷中性点 $E_{\rm CNP}\approx0.79$ eV 📜Q。非平衡 LDOS $\rho_{\rm NE}=$ 总 LDOS − 平衡 LDOS（Keldysh，SI Eq.S5）📜Q。

**变量含义表**：

| 符号 | 含义 | 值/定义 |
|---|---|---|
| $\theta$ | 扭角 | 0–1.2°（算例 0.82°） |
| $\Delta$ | 层间偏压 | ±0.4 eV（算例 300 meV） |
| $E_F$ | 费米能 | ±0.1 eV |
| $N,L,N_{\rm top}$ | 器件宽度/长度/顶层宽 | N=121/209，L=303a/603a/123a |
| $G$ | 两端微分电导 | 单位 $G_0=2e^2/h$ |
| $\gamma_0,\gamma_1$ | 层内/层间 hopping | 2.7 eV / 0.48 eV |
| $a,a_I$ | 面内/层间最近邻距离 | 1.418 Å / 3.349 Å |

### 1.2 参数分册（替代旧"四层变量表"：区分"作者设定" vs "推导所得"）

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | $\theta$（扭角 0–1.2°）、$\Delta$（层间偏压）、$E_F$（费米能）、扭转中心 $(x_0,y_0)$、宽度 N、长度 L、顶层宽 $N_{\rm top}$、杂质 $(V_0,\xi,位置)$ |
| **导出量（由旋钮+常数算出）** | moiré 周期（由 θ 定，原文未给 λ 数值）、commensurate 角 $\theta_{\rm com}\approx0.8168°$（m=40,n=41） |
| **模型内部量（解的性质）** | 紧束缚 H（Eq.1）、hopping $t_{ij}$（Eq.2）、$G(E_F)$（Eq.3）、非平衡 LDOS $\rho_{\rm NE}$（SI Eq.S5）、TZM 线性色散能窗、valley Chern 差 $\Delta C_v=2$ |
| **固定常数** | $a=1.418$ Å、$a_I=3.349$ Å、$\gamma_0=2.7$ eV、$\gamma_1=0.48$ eV、$q_\pi/a=q_\sigma/a_I=2.218$ Å⁻¹、$r_c=3a$ |
| **预言量（可检验）** | NQCP 平台值（近 1/2/3 × 2e²/h）、100% valley 极化电流、AB 振荡"trivial origin" |

> 无"反推量 θ̂"层——理论论文不反推实验量（模型参考能 $E_{\rm CNP}\approx0.79$ eV 是 TBG 电荷中性点定义基准，非反推）。

### 1.3 显式假设清单（本文结论的前提集合）

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **零温 T=0**（SI） | 模型 | 📜Q |
| A2 | **单粒子紧束缚 + NEGF**（强 e-e 关联未计入；论证 $E_F$ 远离平带、$U_c\approx25$ meV ≪ 150 meV 能窗） | 模型 | 📜Q |
| A3 | **短程点杂质免疫**（$V_0=2.5$ eV、$\xi\le a$；大 $\xi$ 且置于 TZM 路径上才破坏平台） | 模型 | 📜Q(SI) |
| A4 | **有限两端器件几何**（flat boundary、扭心=原点） | 模型 | 📜Q |
| A5 | **偏压 $\Delta\neq0$**（Δ=0 时无 TZM 线性色散能窗，SI Fig.S2） | 推导 | 📜Q(SI) |
| A6 | **hopping 截断 $r_c=3a$**（SI §I 验证合理） | 推导 | 📜Q |

> 判别性扫轴：θ（0–1.2°）、E_F（±0.1 eV）、Δ（±0.4 eV）、L、N、N_top、扭转中心 y₀、杂质位置。这些假设在 §4 逐一映射到"失效 → 结论崩塌"。

---

## 2. 推导链（演绎结构：顺论文顺序，每步"输入→输出→所用假设/定理→合法域"）

### 2.0 总览：论文是一条演绎链

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 前提定理层 | 引言 | 偏压畴壁 THS + AA 散射规则（已知） | 问题设定：TZM vs 网络 | ΔC_v=2、refs 40,43,44 | — |
| 模型层 | 器件 + 哈密顿量 | 紧束缚 H + Slater-Koster hopping | 两端器件模型 | A2、A4 | 单粒子 |
| 推导层 | 输运 NEGF | NEGF Eq.3 | 电导 G(θ,E_F,Δ)、NQCP 平台 | A1、A5 | 零温零偏 |
| 边界层 | 几何/杂质/扭转中心 | 扫 N/L/扭心/杂质 | 平台 1/2/3 可调 + bulk 判别 + 稳健性 | A3 | — |
| 佐证层 | 非平衡 LDOS | Keldysh ρ_NE | 1D 本质实空间佐证 | — | — |

### 2.1 前提定理层（引言）：THS 起源 + AA 散射规则

- **THS 起源**：偏压 mTBG 畴壁（AB/BA 堆叠区边界）存在 1D 拓扑螺旋态 THS，其起源 = 畴壁两侧每自旋谷 valley Chern 数之差 $\Delta C_v=2$（引 refs 43,44）📜Q。每畴壁有两种 THS（Fig.1a 实线/虚线箭头）。
- **AA 散射规则**：实线→虚线（−120° 方向）、虚线→实线（+120° 方向）（引 ref 40）📜Q。据此 THS 可自构 1D TZM。

### 2.2 模型层：器件模型 + 紧束缚哈密顿量

- 底 = 未扭转单层 nanoribbon（宽 N）、顶 = 扭转 flake（长 L）；扭心=原点 📜Q。层间偏压以 on-site 能 $(-1)^\alpha\Delta$ 计入 📜Q。
- Slater-Koster hopping（Eq. 2）：$V_{pp\pi}(r)=-\gamma_0 e^{(a-r)q_\pi/a}$、$V_{pp\sigma}(r)=\gamma_1 e^{(a_I-r)q_\sigma/a_I}$；参数 $a=1.418$ Å、$a_I=3.349$ Å、$\gamma_0=2.7$ eV、$\gamma_1=0.48$ eV、$q_\pi/a=q_\sigma/a_I=2.218$ Å⁻¹、$r_c=3a$ 📜Q。

### 2.3 推导层：NEGF 输运 → NQCP 平台

- **输运公式**（Eq. 3）：$G(E_F)=\frac{2e^2}{h}\mathrm{Tr}[\Gamma_L G_C^r\Gamma_R G_C^a]$，$G_0\equiv2e^2/h$，$E_F$ 相对 $E_{\rm CNP}\approx0.79$ eV 📜Q。
- **平台 2（核心）**：长 flake（L=303a，θ=0.82°）平台值"around 1.99, close to the quantized value of 2"（Fig.2a，θ 范围 0.76°<θ<0.91°）📜Q[~]。机制：θ=0.82° 时三排 AA 亮斑阵列沿纵向夹住两条 TZM → 平台 2 📜Q。
- **非精确量子化**：作者措辞"nearly quantized"（近量子化）📜Q；平台值 ~1.99 而非 2.00——畸变 TZM 的残余散射痕迹（💭I）。
- **θ 增大**：moiré 变窄、纵向 TZM 增多 → G 增大；但更大 θ 无新平台（moiré 周期减小、纵向 TZM 耦合增强）📜Q。

### 2.4 边界层：几何/扭转中心/杂质 → 平台可调 + bulk 判别 + 稳健性

- **宽度 N**：N 增大 → 平台出现在更小 θ；平台质量随 θ 减小而改善 📜Q。更高平台 **4, 6, 8, …** 需更宽系统（作者预言）📜Q。
- **长度 L**：短 L 量子隧穿使 G 大，L 增则 G 快速降并饱和到平台 📜Q。
- **扭转中心调平台**：平台 1（扭心 (0,−56√3a)，θ>0.34°，"around 0.999"）；平台 2 与 3 共存（N=209、扭心 (0,−100√3a)≈(0,−246 Å)，θ=0.74°，Fig.3b）📜Q[~]。**平台 1 与 3 共存 → 1D 通道必在 bulk**，排除边缘态解释 📜Q。
- **杂质稳健性**（SI §VII）：平台对缺陷型杂质（ξ≤a）免疫，只有大 ξ 且放在 TZM 传播路径上才破坏；TZM 展宽 ~75a 使其可绕开短程杂质 📜Q(SI)。

### 2.5 佐证层：非平衡 LDOS + 极化 + 振荡归属

- **非平衡 LDOS**（Fig.4）：两条畸变、分离的 TZM 横跨 flake；TZM 被 AA 斑排斥；平行 TZM"never couple in real space"📜Q。SI Fig.S2(b) 能带本征态（Δ=0.3 eV）显示 TZM 绕过所有 AA 点、电子型 TZM 波函数集中顶层面/空穴型集中底层面（layer 极化）📜Q(SI)。
- **E_F/Δ 依赖**（Fig.2d/e）：NQCP 出现在正（负）偏压的空穴（电子）激发区；正偏压仅 K 谷态参与输运，反偏压谷反转为 K′ → **100% valley 极化**电流 📜Q。空穴侧平台质量优于电子侧（e-h asymmetry）📜Q。
- **振荡归属**：AB 振荡有 trivial origin（两 TZM + 接触围成轨迹）；1D 通道与 Rickhaus FP 振荡一致 [38] 📜Q；观测振荡"may not account for the 2D network model"[38,39] 📜Q。

---

## 3. 结论清单（分层：定理 / 估算 / 预言）

> 理论论文的结论必须按**性质**分层，而非平铺。每条标：**依赖假设** + **可检验性**。

### 3.1 定理式主张（数值计算/论证的产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| THS → 1D 畸变 TZM | 非平衡 LDOS：TZM 被 AA 斑排斥、平行 TZM 不耦（"never couple in real space"） | A2、A4 |
| bulk 通道判别 | 平台 1 与 3 共存 → 1D 通道在 bulk（非边缘态） | A4 |
| 100% valley 极化 | 正偏压仅 K 谷、反偏压仅 K′ 谷参与输运 | A5 |

### 3.2 估算（数值算例，非严格定理）

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| 平台 2 具体值 | ~1.99（θ=0.82°，L=303a） | A2 | 📜Q[~]（"around"） |
| 平台 1 具体值 | ~0.999（θ>0.34°） | A2 | 📜Q[~]（"around"） |
| 平台 2 的 θ 范围 | 0.76°<θ<0.91° | — | 📜Q[~] |
| commensurate 角 | $\theta_{\rm com}\approx0.8168°$（m=40,n=41） | SI | 📜Q[~] |
| TZM 能窗宽度 | ~150 meV（Δ=0.3 eV） | A5 | 📜Q[~] |
| 库仑能 | $U_c\approx25$ meV（平带区估计） | — | 📜Q[~] |
| 电荷中性点 | $E_{\rm CNP}\approx0.79$ eV | — | 📜Q[~] |
| TZM 能窗阈值 | Δ≥0.2 eV | SI | 📜Q(SI) |

### 3.3 预言（可检验性 → 见 §5.1）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| NQCP 平台近 1/2/3 = TZM 存在强信号 | "serves as a strong experimental sign"（预言）📜Q | 高——两端电导测量 |
| 更高平台 4, 6, 8, …（更宽系统） | 作者预言 📜Q | 中 |
| 100% valley 极化电流 | 作者预言 📜Q | 中——valleytronics |
| 裁决网络 vs TZM 之争 | "Our findings resolve recent debates"（作者自述）📜Q | 中——计算裁决 |

### 3.4 内部验证（自洽核对，非"排除竞争解释"）

1. **平台值 ↔ 通道数互验**：~1.99 ↔ 两条纵向 TZM；~0.999 ↔ 单 TZM；平台 3 ↔ 三条 v₁ TZM（SI Fig.S6 LDOS 佐证）📜Q。
2. **bulk 通道判别**：平台 1 与 3 共存 → 排除边缘态 📜Q。
3. **1D 本质三重佐证**：非平衡 LDOS 图案 + 短程杂质免疫 + AB 振荡 trivial origin 📜Q。
4. **能带 vs 输运互验**：SI 能带 TZM 绕过 AA 点 ↔ 器件 Fig.4 实空间 TZM 被 AA 斑排斥 📜Q。

### 3.5 概念区分（作者论证中的"分类"，非溯因排除）

| 区分 | 依据 | 结论 |
|---|---|---|
| TZM vs 2D 网络 | 非平衡 LDOS：TZM 被 AA 点排斥、独立传播 vs AA 点散射成三路 📜Q | 1D 畸变 TZM |
| NQCP vs 精确量子化 | 平台值 ~1.99（非 2.00）、~0.999（非 1.000）📜Q | 近量子化（残余散射痕迹） |
| bulk vs 边缘态 | 平台 1 与 3 共存 → 1D 通道在体内 📜Q | bulk 1D 通道 |
| 畸变 vs 完美 TZM | 是否严格沿 ±v_i 直线传播（ref 64 注）📜Q | 本文 = 畸变 TZM |

> 注：这些是**概念/图景分类**（taxonomy），不是实验论文那种"数据排除竞争解释"（溯因排除）——理论论文没有后者。

---

## 4. 假设-结论依赖图（含金量所在）

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性（作者如何对待） |
|---|---|---|---|
| A1 零温 | 有限温 | NQCP 平台 | 适用域边界（未算有限温）📜Q(SI) |
| A2 单粒子（无 e-e） | 魔角平带关联 | TZM 图景 | 作者论证 E_F 远离平带、U_c≈25 meV ≪ 150 meV 能窗 📜Q |
| A3 短程杂质免疫 | 大 ξ 杂质在 TZM 路径上 | 平台破坏 | 作者明言大 ξ 杂质可破坏平台 📜Q(SI) |
| A4 有限两端器件几何 | 边界/顶层宽不理想 | 平台质量 | NQCP of 2 比 of 1 对边界更敏感 📜Q(SI) |
| A5 偏压 Δ≠0 | Δ=0 | TZM 能窗不出现 | Δ≥0.2 eV 阈值（SI Fig.S2）📜Q(SI) |
| 通道间耦合无定量 | 耦合增强（θ 增大） | 平台消失 | 仅定性"coupling becomes stronger"，无 t_inter 数值 💭I⚠️ |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（本文预言的实验靶标）

- NQCP 平台值（近 1/2/3 × 2e²/h）→ 两端 TBG 纳米 flake 器件电导测量 📜Q；
- 平台 ~1.99 @ θ=0.82°、~0.999 @ θ>0.34°（具体算例靶）📜Q；
- 100% valley 极化电流（valleytronics）📜Q。

### 5.2 设计原则（平台可调三要素）

$\theta$（设 moiré 周期/AA 阵列）+ 扭转中心垂直位移（微调平台数 1/2/3）+ $\Delta$（开 TZM 能窗，≥0.2 eV）📜Q。

### 5.3 后续文献修正（时间倒挂，💭I）

- **Xu 2019 (ref[39]) / Rickhaus 2018 (ref[38])**：本文主张其振荡"may not account for the 2D network model"——对"观测振荡证 2D 网络"解读的修正 📜Q。
- NQCP 平台尚待直接电输运实验验证（本文是预言）。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 无直接电输运实验验证 | NQCP 平台是预言，尚待专门测量 | 📜Q（"strong experimental sign"） |
| 零温 T=0 | 全文 T=0（SI）；有限温效应未算 | 📜Q(SI) |
| 强 e-e 关联未计入 | 论证 E_F 远离平带、U_c≈25 meV ≪ 150 meV 能窗 | 📜Q |
| 平台质量对边界/杂质敏感 | NQCP of 2 比 of 1 对边界更敏感；大 ξ 杂质可破坏平台 | 📜Q(SI) |
| 零偏压行为未讨论 | Δ=0 时无 TZM 线性色散能窗（SI Fig.S2） | 📜Q(SI) |
| 通道间耦合无定量参数 | 原文只有定性"coupling becomes stronger/gets eliminated"，无 t_inter 数值（旧版 t_inter≈0.05t 已删） | 💭I⚠️ |

---

## 7. 与其他工作的关系（跨论文对标放这里，不放正文）

| 工作（本文 ref） | 关系 |
|------|------|
| San-Jose & Prada 2013 [28]、Efimkin & MacDonald 2018 [29]（及 [27,30–39]） | 2D 三角网络模型侧（"one THS scattered into three at AA point"）📜Q |
| Tsim, Nam & Koshino 2020 [40]（=T12）、Fleischmann 2020 [41]、De Beule 2020 [42]（=T15） | TZM 预言侧（band-structure + 单参数散射理论）；本文 = 其"完美 TZM"的"畸变 TZM"修正 📜Q |
| Hou et al. 2020 [45] / Hou 2020 [46] / You 2022 [47] | 网络侧量子输运模拟；本文与之"essentially distinct"因捕获 AA/AB/BA 平滑过渡 📜Q |
| Martin 2008 [43]、Vaezi 2014 [44] | THS 的 valley Chern 差 ΔC_v=2 来源 📜Q |
| Rickhaus 2018 [38] | FP 振荡观测；本文 1D 通道与之"consistent" 📜Q |
| **Xu 2019 [39]** | AB 振荡观测；本文称"may not account for the 2D network model [38,39]" 📜Q |

> ⚠️ **Phase S 外部对标（非本文原句，💭I）**："TZM(T12) 与网络(T9) 是耦合强度的两极限"——原文无此措辞，但原文以"纵向 TZM 耦合随 moiré 周期减小而增强"作为平台消失机制（§2.3/2.4）📜Q，故两极限框架是 review 层综合。

---

## 8. 对后续研究的影响

- 给出 TZM 的明确实验方案：两端 TBG 纳米 flake 器件测 NQCP 平台（值近 1/2/3）——比精确量子化更易观测的定量靶 📜Q。
- 100% valley 极化电流 → valleytronics 潜在应用 📜Q。
- 在 2D 平台上实现 1D 导电通道阵列，提供 TBG 内禀拓扑态工程化路径（作者 "provides a way of engineering…"）📜Q。

---

## 9. 理论模型映射（供 TBPM / Kubo-Bastin 计算对标）

| 映射 | 说明 |
|------|------|
| θ → moiré 周期 → AA 阵列间距 | 扭角→moiré 周期→AA 斑阵列（原文未给 λ 数值，仅 θ_com=0.8168°）📜Q/💭I |
| Δ → THS 线性色散能窗 | 层间偏压→TZM 能窗（~150 meV @ Δ=0.3 eV；Δ≥0.2 eV 才出现）📜Q |
| 通道数 → 电导平台值 | 1/2/3 条纵向 TZM → 平台近 1/2/3 × 2e²/h（非精确）📜Q |
| NEGF G=(2e²/h)Tr[Γ_L G^r Γ_R G^a] ↔ Landauer/LB | 通道计数约定见 [PHY-LB] 📜Q |
| 平台 ~1.99 vs 2.00 → 畸变 TZM 弱散射 | TBPM/Kubo 精确量子化→完美 TZM；无平台→网络；NQCP→本文 💭I |

> 与 TBPM/Kubo 对应：本文是有限两端器件的 Landauer/NEGF 透射计算，bulk σ_xx（Kubo）只给背景，复现 NQCP 需有限器件透射 💭I。

---

## Phase S 目的接口（三问引用式 + 增量价值）

- **Q1（edge state 如何表征）**：本文用**两端微分电导 G(θ,E_F,Δ)** + **非平衡 LDOS ρ_NE(r)** 表征 TZM——平台数=纵向 TZM 数（近 1/2/3）、平台 1&3 共存判 bulk、LDOS 显示 1D 畸变通道。详见 §2/§3。
- **Q2（理论如何解释/复现）**：紧束缚 + NEGF（Landauer/Meir-Wingreen）量子输运；机制 = AA 点散射规则使 THS 自构 1D 畸变 TZM（vs 2D 网络）。详见 §1/§2。
- **Q3（理论↔实验对应）**：NQCP 平台（近 1/2/3 × 2e²/h）为可检验预言；平台 ~1.99 @ θ=0.82°；1D 通道与 Rickhaus FP 振荡一致 [38]，观测 AB 振荡"may not account for the 2D network model"[38,39]。详见 §3/§7。

> **增量价值**：给 TZM vs 网络之争的裁决性**计算**证据（非平衡 LDOS + NQCP 平台），是 T12（完美 TZM）与 T9（网络）之间的"中间地带"定量靶（~1.99 @ 0.82°，非 2.00）。为项目 TBPM/Kubo 计算提供有限器件 NEGF 对标的 NQCP 判据（量子化 vs 无平台 vs 近量子化三分支）。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` 提取正文（/tmp/T29.txt, 421 行）+ SI，逐项 grep 核对：**全部数字/专名命中原文**——

| 数字/专名 | grep 命中位置 | 结论 |
|------|--------------|------|
| 平台 1.99 / 0.999 / 近 1,2,3 / 2e²/h / G₀≡2e²/h | 正文 | ✓ 📜Q[~] |
| θ=0.82°、θ_com≈0.8168°（m=40,n=41）、0.76°<θ<0.91°、θ>0.34° | 正文/SI | ✓ 📜Q[~] |
| a=1.418 Å / a_I=3.349 Å / γ₀=2.7 eV / γ₁=0.48 eV / 2.218 Å⁻¹ / r_c=3a | 正文 | ✓ 📜Q |
| E_CNP≈0.79 eV、Δ=300 meV、E_F=−70/−50/+60 meV | 正文 | ✓ 📜Q |
| TZM 能窗 ~150 meV、U_c≈25 meV、杂质 V₀=2.5 eV / x_im≈500.05 Å / 展宽 75a、Δ≥0.2 eV | Discussion/SI | ✓ 📜Q[~] |
| N=121/209、L=303a/603a/123a、扭心 (0,−56√3a)/(0,−100√3a)≈(0,−246 Å) | 正文/SI | ✓ 📜Q |
| 4,6,8,…、100% valley 极化、ΔC_v=2、−120°/+120° | 正文 | ✓ 📜Q |
| Rickhaus 2018=ref[38]、Xu 2019=ref[39] | 引用列表 | ✓ 📜Q |
| "strong experimental sign for the existence of TZMs" | 正文 | ✓ 📜Q |

⚠️ 修正/降级：① arXiv:2408.09843 正文未出现 → 头部表已标"外部来源"。② 三处旧无源数字仍确认不存在：grep "0.05"=0、"0.1 eV"=0、"0.8"（作 0.8–0.95 系数）=0 → 旧版 t_inter≈0.05t、G≈0.8–0.95×N、平台宽度~0.1 eV 已删除。③ Xu 2019 确在本文引用列表（ref[39]）——本文主张其振荡"may not account for the 2D network model"（附录 B.5 旧记"与 Xu 对标原文无"有误，已更正）。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-20 (S-REV) | **删除三处无源数字**："t_inter≈0.05t"（grep "0.05"=0）、"G≈0.8–0.95×N·2e²/h"、"平台宽度~0.1 eV"（grep "0.1 eV"=0）→ 改为原文 "nearly quantized conductance plateau ... close to 1, 2, and 3 (in units of 2e²/h)" 与 θ=0.82° 算例平台接近 2 📜Q。依据：§B.5#3 + cards.md T29 |
| 2026-08-20 (S-REV) | **"通道间弱耦合"标注 💭I⚠️**：原文未给耦合参数，该定性为 review 层综合。依据：cards.md T29 |
| 2026-09-02 | **按 4 块辨识结构整体重写**：TL;DR 问题句式 + 系统辨识导览（黑箱三要素/四层变量表/判别表/[前提与限定]）+ 结果与机制 + 理论模型与方法 + 关键预言与数据 + 目的接口 + 反向核对 pass |
| 2026-09-02 | **更正 Xu 2019 引用（新发现）**：附录 B.5 旧记"与 Xu 2019 对标原文无"有误——Xu 2019 确在引用列表（ref[39]，正文 L67/L257），本文主张其振荡"may not account for the 2D network model"[38,39] |
| 2026-09-08 | **按 5 块演绎结构整体重写**（应用户要求）。旧 4 块版归档 `archive/paper_review_T29_hou2024_prb.backup_20260908.md`。黑箱三要素/四层变量表/判别表/[前提与限定] → 拆为"模型白箱（器件+紧束缚+NEGF+参数分册+6 条假设清单）"+"推导链（前提定理/模型/推导/边界/佐证五层）"+"结论清单（定理/估算/预言分层）"+"假设-结论依赖图"+"接口"；内部验证（§3.4）+ 概念区分（§3.5）取代判别表；删"反推量 θ̂"层。全部 📜Q 事实与数字无丢失。 |
