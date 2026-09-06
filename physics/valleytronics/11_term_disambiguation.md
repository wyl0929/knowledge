<!--
Field: 量子谷霍尔效应与谷电子学（Quantum Valley Hall Effect & Valleytronics）
Mode: full_onboarding
Domain archetype: science_technical
Created date: 2026-09-02
-->

---
document_type: term_disambiguation
schema_version: v0.10-rc2
field: "量子谷霍尔效应与谷电子学（QVH / Valleytronics）"
last_updated: 2026-09-02
---

# 11 关键概念与边界说明

Last updated: 2026-09-02

## 概念边界契约 / Concept Boundary Contract

### 用户原始术语

"量子谷霍尔效应（QVH）"、"谷电子学（valleytronics）"。

### 规范工作范围

本 field pack 实际讨论的对象是**时间反演对称下、以"谷"（布里渊区两个不等价极值点 K / K′）为内部量子数的拓扑/输运现象**，具体分四层：

1. **谷陈数框架**：gapped 双层/多层石墨烯在破反演对称场下，单谷 Berry 曲率积分的整数拓扑不变量，及畴壁处谷陈数跳变如何束缚边界模。
2. **谷输运**：谷分辨的霍尔电导/谷电流，及其与"谷不守恒"这一软约束的张力。
3. **谷保护**：谷间（intervalley）背散射被动量失配抑制的机制、证据阶梯与"软保护"边界。
4. **泛化**：从 AB/BA 双层到 ABC/ABA 三层（rhombohedral trilayer）、再到单层/TMD 的谷物理推广。

### 上位概念、下位概念与相邻概念

- **上位概念**：拓扑物态（topological states of matter）、量子输运（quantum transport）、能带拓扑学（band topology / Berry 曲率）。
- **下位概念**：谷陈数（valley Chern number）、谷霍尔电导（valley Hall conductivity）、谷霍尔扭结态（valley-Hall kink state）、谷保护螺旋态（valley-protected helical state）、谷流/谷极化（valley current / valley polarization）。
- **相邻但不同的概念**：
  - 量子霍尔效应 QHE（总 $\sigma_{xy}$ 量子化，需破时间反演；QVH 总 $\sigma_{xy}=0$）
  - 量子自旋霍尔效应 QSHE（内部量子数=自旋，helical 边缘态；QVH 内部量子数=谷）
  - 量子反常霍尔效应 QAHE（零场手征，破时间反演）
  - 手征边缘态（chiral edge state，单向，破时间反演）
  - 拓扑绝缘体 / $\mathbb{Z}_2$ 不变量（QSHE 的对称性类别）

### 常见过度等同

| 方便说法 | 可能导致错误结论的原因 |
|---------|---------------------|
| "QVH = QHE" | QVH 总霍尔电导恒为 0（时间反演 $C_K+C_{K'}=0$），无 $\sigma_{xy}=\nu e^2/h$ 量子化平台；属谷电子学/畴壁态，不是量子霍尔。 |
| "谷霍尔电导量子化 = σ_xy 量子化" | 谷不守恒 → 谷分辨霍尔电导无法像总 σ_xy 那样严格量子化；它只在谷守恒近似下才有"量子化"意义。 |
| "helical = chiral" | helical = 谷/自旋锁定、反向传播（K 前进 K′ 后退）；chiral = 单一方向（需破时间反演）。helical 保护弱于 chiral。 |
| "STM/输运看到畴壁态 ⇒ 拓扑保护" | 存在性 ≠ 保护。STM LDOS、输运"有通道"是平衡/存在性陈述；"保护"是散射/动力学陈述。观测到形态一致是"必要+一致"，非充分。 |
| "谷保护 = 强保护（同 QHE）" | 谷保护靠动量失配，只挡平滑势，原子点缺陷即破坏；比 QHE 的手征保护脆弱得多。 |
| "valley Chern number = ±2（每谷）" | 每谷谷陈数幅度是 ±1（unit magnitude）；"2" 是畴壁两侧的**跳变** $\Delta C_v=\pm2$（或每谷 2 条边界模）。见下"谷陈数约定定稿"。 |

### 本包允许使用的表达

- **量子谷霍尔效应 (QVH)** / **谷电子学 (valleytronics)**：本 field 的核心对象。
- **谷陈数 (valley Chern number)**：指**单谷**的 Chern 数 $N_\nu=\pm1$（单位幅度）。需要区分"跳变"时写 $\Delta N_\nu=\pm2$。
- **谷霍尔电导 (valley Hall conductivity)**：$\sigma_{xy}^V$，谷分辨霍尔电导，仅在谷守恒近似下量子化。
- **谷保护 (valley protection)**：intervalley 背散射被动量失配抑制；默认是"软保护"。
- **螺旋态 (helical state)**：谷（或自旋）锁定反向传播的成对边缘/畴壁态。

### 本包禁止直接推出的结论

- 不能从"总 σ_xy=0 或存在谷霍尔信号"推出"有拓扑保护"。
- 不能从"STM 看到畴壁态 / 输运有通道"推出"谷保护成立"（需散射/谷分辨测量，见证据阶梯）。
- 不能把"谷霍尔电导"当成可严格量子化的总霍尔电导（谷不守恒）。
- 不能把 chirally stacked N 层石墨烯的 $C_K=N/2$（N 为奇数时为半整数）当真正的整数 Chern 数。

### 对下游研究判断的影响

- **field map**：必须把"谷陈数框架 → 谷输运 → 谷保护 → 泛化 trilayer/TMD"作为四个不同成熟度的层，前两层成熟、谷保护是 active frontier、trilayer 泛化是未闭环。
- **frontier compass**：谷保护的实验判定（目前仅 Verbakel 2021 FFT 一条间接证据）是真正边界；"存在霍尔信号 ⇒ 拓扑"是伪 gap。
- **gap table**：C_v 约定不一致本身已被本文件定稿（见下），不再作为 gap；TMBG 三层 $C_v=\pm3$ 的通道数对应仍保留为 gap。
- **project title / MVP success criteria**：凡涉及谷霍尔电导数值的 project，必须先解决"谷分辨"读出（是否把 Kubo-Bastin 分解到 K/K′），否则指标不成立。

### 核验状态

concept_status: source_checked（谷陈数约定已对照 Huang 2018 PRL 正文、Zhang-MacDonald-MeLe 2013 PNAS 原文、Verbakel 2021 PRB 原文定稿；trilayer 部分仍 NEEDS_VERIFICATION）

证据来源：Huang et al. PRL 121, 037702 (2018) 正文 "quantized at unit magnitude"；Zhang-MacDonald-MeLe PNAS 110, 10546 (2013) "valley Chern number $N_\nu=-\nu\,\mathrm{sgn}(\Delta)=\pm1$""changes by $\Delta N_\nu=\pm2$"；Verbakel et al. PRB 103, 165134 (2021) "$C_v=\pm1$（域）、$\Delta C_v=\pm2$（边界）"。三者经 pdftotext + grep 核对。

待核验事项：TMBG（ABC/ABA 三层）"$C_v=\pm3$"的确切约定与畴壁通道数对应 → Chen 2021 / Phong 2026 原文核（见 §7）。

---

## 0. 阅读说明

本文件比 `00_beginner_guide.md` 更严谨，但仍先解释概念再比较边界。它不是术语表，而是要帮助研究者理解：一个概念到底指什么、不指什么、和相邻概念为什么容易混、区别会怎样影响选题。

正文以中文为主，英文术语出现时附原文。

## 1. 核心概念：本领域到底指什么？

### 人话解释

石墨烯/双层石墨烯的电子结构在布里渊区有两个"谷"（K 和 K′），像两个镜像的极值点。如果加一个垂直电场把两层不对称地掰开（开一个能隙），这两个谷会各自带上一股"几何涡旋"——一个谷的电子倾向沿畴壁往一个方向走，另一个谷往反方向走，而且互不回头。这就是量子谷霍尔效应：**净霍尔电流为零，但谷分辨的霍尔电流不为零**，且这股谷流在平滑的扰动下很难被背散射打散。谷电子学就是想把这个"谷"当成一个可以编码、输运、探测的自由度。

### 正式定义或基本数学对象

gapped 双层石墨烯的单谷两带有效哈密顿量（Zhang-MacDonald-MeLe 2013）：

$$
\tilde H_\nu = \mathbf g_\nu(\mathbf q)\cdot\tilde{\boldsymbol\sigma},
\qquad
\mathbf g_\nu(\mathbf q)=\left(-\frac{q_x^2-q_y^2}{\gamma},\ \frac{2\nu q_x q_y}{\gamma},\ \Delta\right),
\qquad \gamma=\frac{t_\perp}{(\hbar v_F)^2}
$$

其中 $\nu=\pm1$ 是谷指标，$\Delta$ 是层间势差开出的能隙，$t_\perp$ 是层间耦合。单谷 Berry 曲率：

$$
\Omega_\nu(\mathbf q)=\mp\frac{2\nu\gamma\Delta\, q^2}{(q^4+\gamma^2\Delta^2)^{3/2}},
\qquad
\text{单谷谷陈数 } N_\nu = -\nu\,\mathrm{sgn}(\Delta)=\pm1
$$

时间反演使 $N_K+N_{K'}=0$，故总 Chern 数（总 $\sigma_{xy}$）为零；但**单谷谷陈数非零**，畴壁两侧谷陈数跳变 $\Delta N_\nu=\pm2$ 束缚出边界模。

### 包含哪些问题

- 谷陈数如何分类畴壁边界模（EFW / LSW / 补偿墙三类，ZMM 2013）。
- 谷霍尔电导 / 谷电流如何产生、检测（Shimazaki 2015、Su 2015 的纯谷流）。
- 谷保护是否成立、如何实验判定（Verbakel 2021 FFT）。
- 从双层到三层（ABC/ABA）到 TMD 的谷物理推广。

### 不包含哪些问题

- 总霍尔电导量子化的朗道量子化/分数态（属 QHE）。
- 自旋-轨道耦合驱动的自旋锁定边缘态与 $\mathbb{Z}_2$（属 QSHE）。
- moiré 晶格重构、魔角关联绝缘体/超导（属 TBG/强关联 platform field）。

### 一个贯穿例子中的位置

以 mTBG（极小扭角双层石墨烯）的 AB/BA 畴壁网络为例：

```text
上游：垂直电场开 AB/BA 能隙（[PHY-GATE]/[PHY-EF]）
  -> 本领域核心环节：AB/BA 谷陈数反号 → 畴壁束缚谷锁定螺旋态
  -> 相邻概念负责：无磁场（区别于 QHE 手征态需 B）
  -> 输出/判断：畴壁双线 LDOS（存在性，E9）+ FFT 无 intervalley 斑（谷保护，E13）
```

## 2. 必须掌握的重要概念

### 2.1 谷陈数（valley Chern number）

**先用人话说：** 谷陈数是"单个谷的能带绕一圈积累了多少几何相位"的整数。它不是一个谷两个谷一起算，而是**每个谷单独算**，两个谷符号相反、互相抵消。

**更正式地说：** 单谷占据带 Berry 曲率在布里渊区（或单谷区域）的积分。gapped 双层石墨烯 $N_\nu=-\nu\,\mathrm{sgn}(\Delta)=\pm1$（单位幅度）。畴壁两侧（AB vs BA，或 EFW 两侧）$N_\nu$ 反号，跳变 $\Delta N_\nu=\pm2$。

**它解决的问题：** 一个畴壁有没有、有几条受保护的边界模——边界模数目 = $|\Delta N_\nu|$（每谷每自旋）。

**它通常输入什么、输出什么：** 输入能带结构（含 $\Delta$ 的符号）；输出一个整数（每谷）+ 畴壁处的整数跳变。

**它与哪些概念容易混淆：** ① 与总 Chern 数（QHE 用，总 $\sigma_{xy}$ 量子化）混；② 与"每谷 2 条边界模"的"2"混——见 2.2 定稿。

**用贯穿例子说明：** mTBG 的 AB 区 $N_K=+1$、BA 区 $N_K=-1$（对谷 K），畴壁跳变 $\Delta N_K=+2$ → 谷 K 有 2 条前进模；谷 K′ 符号相反 → 2 条后退模。每谷每自旋 2 条 → 两自旋下两端口电导 $4e^2/h$。

**对选题判断的影响：** 任何"谷陈数数值计算"项目，先要决定算"每谷 $N_\nu$"还是"畴壁跳变 $\Delta N_\nu$"，两者差一倍（§2.2）。

### 2.2 谷陈数约定定稿（本次已核验，替代 §8.1 的待核问题）

**问题**：Huang 2018 正文说畴壁态的谷陈数 "accurately quantized at **unit magnitude**"（$|C|=1$，引 ZMM 2013），而 `[PHY-BERRY]` 笔记写 "AB/BA 有相反 $C_v=\pm2$"。二者差一倍。

**定稿（对照原始 PDF）**：

| 量 | 正确值 | 原始出处（pdftotext + grep 已核） |
|---|---|---|
| 单谷谷陈数 $N_\nu$ | $\pm1$（**unit magnitude**） | ZMM 2013 PNAS "$N_\nu=-\nu\,\mathrm{sgn}(\Delta)=\pm1$"；Huang 2018 "quantized at unit magnitude" |
| 畴壁两侧跳变 $\Delta N_\nu$ | $\pm2$ | ZMM 2013 "changes by $\Delta N_\nu=\pm2$"；Verbakel 2021 "$\Delta C_v=\pm2$" |
| 每谷每自旋边界模数 | 2（= $|\Delta N_\nu|$） | Martin 2008 "two zero modes per kink per valley per spin"；ZMM 2013 "每谷 2 条/自旋" |
| 两端口电导 | $4e^2/h$（2 模 × 2 自旋） | Verbakel 2021 正文 "4e²/h"（grep 命中） |

**结论**：`[PHY-BERRY]` 的 "$C_v=\pm2$" 是**把"畴壁跳变 $\Delta C_v=\pm2$"误标成了"单谷谷陈数"**。正确写法是：**每谷 $C_v=\pm1$（unit magnitude），畴壁跳变 $\Delta C_v=\pm2$，每谷每自旋 2 条模**。交接表 §8.1 里"每谷 1 条×2 谷×2 自旋=4 通道"的计数链条有误——正确链条是"每谷 2 条（来自 $\Delta C_v=2$）×2 谷 ×2 自旋 = 8 条螺旋模（4 前进 + 4 后退），净两端口电导 4e²/h"。**结论（$|C_v|=1$ 才对）是对的，中间通道计数（1 条/谷）是错的**。

**对下游的影响**：`[PHY-BERRY]` 笔记需回写修正（TBG field 的 `99_update_log.md` 记一条）；本 field 正文一律用"每谷 $C_v=\pm1$、$\Delta C_v=\pm2$、每谷 2 模"。

### 2.3 谷霍尔电导（valley Hall conductivity）

**先用人话说：** 谷霍尔电导是"只算一个谷贡献的那份横向电流"。因为两个谷方向相反，总横向电流是零；但把 K 谷和 K′ 谷分开看，各自有一股不抵消的横向流。

**更正式地说：** $\sigma_{xy}^{V}=N_\nu\, e^2/h$（谷守恒近似下），两个谷反号 $\sigma_{xy}^{K}=-\sigma_{xy}^{K'}$。总 $\sigma_{xy}=\sigma_{xy}^{K}+\sigma_{xy}^{K'}=0$。

**它解决的问题：** 谷流如何产生/检测，是谷电子学器件的核心指标。

**它通常输入什么、输出什么：** 输入能带 Berry 曲率；输出谷分辨横向电导。

**它与哪些概念容易混淆：** 与 QHE 的 $\sigma_{xy}=\nu e^2/h$ 混——后者是**总**电导且**严格**量子化；前者是谷分辨且**只在谷守恒近似下**才有"量子化"意义。

**用贯穿例子说明：** mTBG 畴壁态每谷 $N_\nu=\pm1$，但"谷霍尔电导"的量子化被 intervalley 散射（原子缺陷）破坏——这是"软保护"的直接体现。

**对选题判断的影响：** 数值算谷霍尔电导时，必须把 Kubo-Bastin/输运分解到 K/K′ 谷，且明确"谷不守恒 → 无严格量子化"这条边界（见 `16_metrics_and_benchmarks.md`）。

### 2.4 螺旋态 vs 手征态（helical vs chiral）

**先用人话说：** 螺旋态像两条对开的单行道——K 谷往东、K′ 谷往西，永不互相撞；手征态像一条单行道——所有电子都往一个方向。

**更正式地说：** helical = 谷（或自旋）锁定、反向传播的成对态，时间反演保护；chiral = 单一方向，破时间反演（需 B 或磁序）。helical 的背散射需要翻内部量子数（谷或自旋），chiral 根本不能背散射。

**它解决的问题：** 畴壁态"有没有背散射"的机制分类。

**它与哪些概念容易混淆：** 摘要常把 QVH 畴壁态叫 "chiral one-dimensional states"，但正文机制是谷锁定反向传播 = helical（[PHY-BERRY] 已注明此辨析）。

**用贯穿例子说明：** mTBG 畴壁态是 helical（K/K′ 反向），不是 QH 手征边缘通道（需 B）。

**对选题判断的影响：** 若把 helical 当 chiral，会误判"无耗散单行道"强度——helical 对原子缺陷脆弱，chiral 对无序鲁棒。

### 2.5 谷保护（valley protection）与"软保护"

**先用人话说：** 谷保护说的是"翻谷很难"，因为翻谷要额外补一大段动量（K 和 K′ 在倒空间隔得远）。平滑的势给不出这么大动量，所以谷守恒；但原子大小的缺陷是"白谱"，什么动量都提供得了，一出现就破坏谷守恒。

**更正式地说：** intervalley 背散射需要散射势提供 $|\Delta K|=\frac{4\pi}{3\sqrt3 a}\approx1.70$ Å⁻¹。平滑势 $V(q)$ 集中在 $q\approx0$ → $\langle K'|V|K\rangle=V(\Delta K)\approx0$ → 谷守恒。原子点缺陷 $V(q)$ 近似白谱 → intervalley 通道打开（[PHY-QPI] §3.1）。

**它解决的问题：** 谷保护成立的条件、失效方式、实验判据（FFT 无 intervalley 斑）。

**它与哪些概念容易混淆：** 与 QHE 的"强保护"混——QHE 手征态对任意不闭合体隙的扰动都稳；谷保护只挡平滑势，**单个原子缺陷即破坏**。

**用贯穿例子说明：** Verbakel 2021 用 FFT 三对照（pristine HOPG 无斑 / H 缺陷 HOPG 有斑 / TBG 网络无斑）证谷保护成立——但结论只对 defect-free 网络成立（作者自陈）。

**对选题判断的影响：** 任何"谷保护器件"提案必须把"缺陷密度"作为第一约束；谷保护不是免死金牌。

### 2.6 存在性 ≠ 拓扑保护（证据阶梯）

**先用人话说：** "看到态在畴壁上"和"这个态不怕背散射"是两件不同的事。前者是"它在那儿"，后者是"它不会被踢走"。

**更正式地说：** STM LDOS / 输运"有通道"是平衡/存在性陈述；"保护"是散射/动力学陈述。逻辑上"拓扑 ⇒ 长自由程/双线"（$P\Rightarrow Q$）推不出"观测到 $Q$ ⇒ 拓扑"（肯定后件谬误）。

**证据阶梯**（每级只证一层，[PHY-BERRY]）：

| 层级 | 证据 | 逻辑地位 | 实例 |
|------|------|---------|------|
| ① 存在性 | 隙内畴壁态（STM LDOS 增强）/ 有畴壁时导电 | 必要 | E9 Huang 2018；E1 Ju 2015 |
| ② 形态一致 | 双线、随电场开关、长自由程 | 一致（非排他） | E9；E1 |
| ③ 谷保护（机制） | intervalley 背散射被抑制（FFT 无 (√3×√3)R30° 斑） | 机制证据（强，仍间接） | E13 Verbakel 2021 |
| ④ 抗无序 + 量化输运 | 态在有缺陷/无序下存活、电导量化 | 最强（**严格未闭环**） | （待做） |

**对选题判断的影响：** 第④级是当前真边界（见 `20_gap_table.md` G-001 / `02_frontier_compass.md` B-001）。

## 3. 容易混淆的概念对比表

| 概念组 | 为什么容易混淆 | 最稳妥的一句话区别 | 如果混淆会怎样误导选题 |
|---|---|---|---|
| QVH vs QHE | 都带"霍尔效应"、都有拓扑边界态 | QVH 总 $\sigma_{xy}=0$ 无量子化平台；QHE 总 $\sigma_{xy}$ 严格量子化 | 把谷霍尔信号当量子霍尔平台，去算总 σ_xy 发现恒零 |
| QVH vs QSHE | 都是时间反演保护的螺旋态 | 内部量子数不同：QVH=谷，QSHE=自旋 | 误以为谷保护的失效方式和自旋保护一样（其实谷保护更脆弱） |
| helical vs chiral | 摘要常混叫 "chiral 1D states" | helical=谷/自旋锁定反向；chiral=单向 | 高估 helical 对无序的鲁棒性 |
| 谷霍尔电导 vs σ_xy | 都叫"霍尔电导" | 前者谷分辨、软量子化；后者总量子化 | 把软量子化的谷霍尔电导当精确平台 |
| 谷陈数 vs 畴壁跳变 | 都叫 "valley Chern number" | 每谷 $C_v=\pm1$；跳变 $\Delta C_v=\pm2$ | 通道数算错一倍 |

## 4. 最关键的概念对比展开

### 对比组 1：QVH 与 QHE（本 field 的第一条边界）

**为什么容易混淆**：都产生"拓扑保护的边界/畴壁输运通道"，实验上都能看到"边界态 + 无背散射"。

**输入/过程/输出不同**：QHE 的输入是强垂直磁场（破时间反演），输出是朗道能级 + 手征边缘态 + 总 $\sigma_{xy}=\nu e^2/h$ 平台；QVH 的输入是破反演对称的电场/堆垛（**保持**时间反演），输出是谷陈数反号的畴壁 + 螺旋态 + 总 $\sigma_{xy}=0$。

**同一例子中的分工**：mTBG 畴壁网络上，B=0 的畴壁态是 QVH（谷锁定螺旋）；若加 B，才叠加 QH 朗道物理（E16 Barrier 2024 是 QH 区 + 超导的相邻平台，不是 QVH 本体）。

**混淆的选题误判**：若把 QVH 当 QHE 去做"总霍尔电导量子化"计算/测量，会得到恒零结果，方向从一开始就错。

### 对比组 2：QVH 与 QSHE（同族不同内部量子数）

**为什么容易混淆**：两者都是时间反演保护的螺旋边缘态，$\mathbb{Z}_2$ 拓扑的教科书例子常把两者并列。

**输入/过程/输出不同**：QSHE 靠自旋-轨道耦合，螺旋态是"自旋↑前进、自旋↓后退"，背散射翻自旋（被磁性杂质破坏）；QVH 靠谷（动量空间），螺旋态是"K 前进、K′ 后退"，背散射翻谷（被原子缺陷破坏）。

**同一例子中的分工**：石墨烯本身 SOC 极弱（Kane-Mele 的 QSHE 无法在纯石墨烯实现）；而谷陈数是石墨烯的天然自由度（[PHY-QPI] 明确"谷保护软于自旋保护"）。

**混淆的选题误判**：把 QSHE 的 $\mathbb{Z}_2$ 不变量计算套到 QVH——QVH 的谷陈数是每谷的整数 Chern 数，不是 $\mathbb{Z}_2$ 奇偶性。

### 对比组 3：存在性证据 与 保护证据（选题判断上最危险的一组）

**为什么容易混淆**：论文摘要用 "demonstrate the emergence of topologically protected states" 这种措辞，读者容易把"看到了态"读成"证了保护"。

**输入/过程/输出不同**：存在性证据（STM LDOS 双线、输运有通道）的输入是平衡态谱，输出是"态在那儿"；保护证据（FFT 无 intervalley 斑、抗无序量化）的输入是散射/无序，输出是"背散射被抑制"。

**同一例子中的分工**：E9 Huang 2018 给存在性 + 形态一致（级①②），E13 Verbakel 2021 给谷保护机制（级③），级④抗无序量化输运至今未见闭合（实验与数值两侧均缺）。

**混淆的选题误判**：把"STM 看到畴壁态"当成"谷保护已证明"，进而跳过真正困难的级④，去设计一个地基不牢的"保护"器件。

## 5. 本领域术语树

```text
谷电子学 / QVH（时间反演保护，总 σ_xy=0）
  -> 谷陈数框架（单谷 N_ν=±1，畴壁 ΔN_ν=±2）
     -> 畴壁边界模（EFW / LSW 等价，补偿墙无模）
     -> 相邻：QHE（总 Chern 数，破时间反演）
  -> 谷输运（谷霍尔电导 σ_xy^V，谷流）
     -> 相邻：QSHE（自旋霍尔，内部量子数=自旋）
  -> 谷保护（intervalley 背散射抑制，软保护）
     -> 证据阶梯：存在性 -> 形态一致 -> 谷保护(FFT) -> 抗无序量化(未闭环)
  -> 泛化：双层 AB/BA -> 三层 ABC/ABA（每谷 3 模，待核）-> 单层/TMD
```

## 6. 与用户当前兴趣或研究路径的关系

- **最值得优先掌握**：2.2（谷陈数约定）——它直接决定任何谷陈数/谷霍尔电导数值计算的定义；2.5（软保护）——它决定项目能声称多强。
- **对 gap table 的影响**：级④抗无序量化是 G-001；TMBG 三层 $C_v=\pm3$ 对应关系是 G-002；谷分辨 Kubo-Bastin 读出是 G-003（工具层）。
- **对 project/MVP 的影响**：谷陈数/谷霍尔电导数值项目必须先通过"谷分辨读出"这关（见 `23_mvp_experiment_plan.md` 的 Operationalization Gate）。

## 7. 待核验内容

| 内容 | 为什么需要核验 | 推荐核验方式 | 状态 |
|---|---|---|---|
| TMBG（ABC/ABA 三层）"$C_v=\pm3$"的确切约定与畴壁通道数对应 | [PHY-BERRY] 写 $C_v=\pm3$，但 ZMM 2013 对 chirally-stacked N 层给 $C_K=N/2$（N=3 时半整数），且明言"ABA 三层上谷陈数无法定义" | Chen 2021 / Phong 2026 原文 pdftotext + grep | **半解决**（见 §7.1；"±3"是模数，谷陈数是 ±3/2） |
| 谷保护在 trilayer（ABC/ABA）是否同样"软" | 无直接实验；三层谷间散射动量失配是否仍成立 | 理论推演 + 文献检索 | NEEDS_VERIFICATION |
| tbplas/Kubo-Bastin 是否已能直接算谷分辨霍尔电导 | 决定谷霍尔电导 MVP 是改代码还是用现成能力 | code audit（QHE subfields/tbplas_conductivity） | NEEDS_VERIFICATION |
| Chen 2021（twisted monolayer–bilayer）的准确期刊/DOI | 交接表标"PRB"，PDF 文件名无期刊 | 查 arXiv/DOI | NEEDS_VERIFICATION |

### 7.1 三层谷陈数约定：半解决（2026-09-02）

**结论**：chirally-stacked N 层石墨烯的**单谷谷陈数 = $N/2$**，**每谷边界模数 = $N$**（二者差因子 2，同双层的"每谷 ±1 vs 每谷 2 模"）。

| 体系 | 单谷谷陈数 $C_v$（= 积分 Berry 曲率） | 每谷边界模数 $N$ |
|---|---|---|
| 单层 | $1/2$ | 1 |
| AB 双层 | $1$ | 2 |
| ABC 三层 | $3/2$ | 3 |

证据链：
1. 用户自推导 `reference/note.tex` §1：ABC 三层 $C_v=\frac32\xi\mu\,\mathrm{sgn}(\Delta)$（半整数），伪自旋表 J=1/2/3 → Berry phase $\pi/2\pi/3\pi$。
2. Zandvliet 2023 综述 Eq. 15：单层（含 SOC）每谷每自旋 $C_{\xi,s}=\pm\frac12$；双层 $C_K=-C_{K'}\approx V/|V|=\pm1$（📜Q）。
3. Zhang-Jung-Fiete-Niu-MacDonald 2011 PRL（T41）：chirally-stacked N 层 $C_K=N/2$ 出处。
4. **Chen 2021（tMBG 原文，θ=1.08°，pdftotext+grep 已核）**："the valley Chern number is $|C|=2$ and $|C|=1$ for the $D>0$ and $D<0$ sides, respectively"（导带）——即 tMBG 的谷陈数是 **|C|=2 与 |C|=1**，**不是 ±3**。
5. **Phong 2026（rhombohedral N 层，grep 已核）**：用 $k^N$ 色散两带模型，每谷有 $N$ 个（传播 + evanescent）模——与"每谷 $N$ 模"一致。

**对 [PHY-BERRY] 的最终裁决（升级）**：它写"tMBG $C_v=\pm3$"**没有原文支持**——Chen 2021 实测/计算的 tMBG 谷陈数是 $|C|=2,1$（随 D 符号），而"3"只可能来自 ABC（rhombohedral）三层的**每谷 3 模**（$N=3$）。真三层谷陈数（单谷积分）是 $\pm3/2$（半整数，故 ZMM 说"ABA 三层上无法定义"——半整数不是严格 Chern 数）。剩余待核：tMBG 的 $|C|=2,1$ 是"单谷积分"还是"两谷差"约定，需 Chen 2021 正文/方法节进一步确认（仍 NEEDS_VERIFICATION）。
