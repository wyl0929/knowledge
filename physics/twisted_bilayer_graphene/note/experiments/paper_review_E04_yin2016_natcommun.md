<!--
 * @Author       : AI 精读 (research_onboarding_skill Phase 4 → 2026-09-01 按 4 块新架构重读)
 * @Date         : 2026-08-11（初读）→ 2026-09-01（系统辨识重读，纯 review 化）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/experiments/paper_review_E04_yin2016_natcommun.md
 * @Description  : E4: Yin et al. (He group) 2016 — STM 直接成像双层石墨烯 AB–BA 畴壁拓扑边缘态（4 块辨识结构）
-->

# Paper Review: Yin et al. (2016) — STM 直接成像 BLG 畴壁拓扑边缘态

| 字段 | 内容 |
|------|------|
| **编号** | E4 |
| **标题** | Direct imaging of topological edge states at a bilayer graphene domain wall |
| **作者** | Long-Jing Yin\*, Hua Jiang\*, Jia-Bin Qiao & Lin He（\* 并列一作） |
| **期刊** | Nature Communications 7, 11760 (2016) |
| **DOI** | 10.1038/ncomms11760 |
| **类型** | 实验 — 低温 STM/STS 直接成像 + 紧束缚理论对标 |
| **课题组** | He group (Beijing Normal Univ.) + H. Jiang (Soochow Univ.) |
| **PDF / SI PDF** | ✅ reference/pdfs/Yin 等 - 2016 - ….pdf；SI ✅ 41467_2016_BFncomms11760_MOESM1433_ESM.pdf |
| **精读日期** | 2026-08-11（初读）→ 2026-09-01（系统辨识重读，4 块模板） |

> **共享知识引用**：本 review 用锚点 `[PHY-EF]`（费米能/CNP/band bending）引用通用物理；本文特有的"衬底诱导 gap + 质量型 LL 谱学"写在 §2/§9，不重复讲义。阅读疑问见 `note/shared/method/mechanism_questions.md` `[METHOD-Q]`。

---

## TL;DR

**本文想解决的问题**：AB–BA 畴壁被理论预言承载对称保护拓扑边缘态（零场存在），但此前只有输运间接证据（Ju 2015 / Li 2016），缺**实空间直接成像**——这些 1D 态到底在哪、空间分布如何？

**主结果**：① 首次 STM 直接成像：gap 内 LDOS 增强的 1D 导电通道**主要局域于畴壁两边缘**（不依赖能量，Fig 3a-c，30/40/300 mV）；② 畴壁结构为**近纯剪切孤子**（~85°），结构宽度 (8±1) nm；③ 衬底（石墨）破坏反演对称 → gap Eg=80±1 meV、m\*=(0.0454±0.0001)mₑ（无栅压）；④ 边缘态高场稳健（7.5 T，Fig 3g），FWHM 随 B 减小（SI Fig 11）。

**结论/意义**：作者称 "This provides **direct and compelling evidence** that the symmetry-protected topological edge states exist…"（强措辞 📜Q）；应用层 "may raise hopes of graphene-based electronics with ultra-low dissipation"（保留"may" 📜Q）。⚠️ 注意"拓扑性"由理论（Chern 数变，ref 12）+ 稳健性支撑，**非独立实验证明**（无输运/手征性/谷保护测量）。

---

## 1. 系统辨识导览（判别表为全文唯一权威）

**黑箱三要素**：`{输入旋钮：B(0–8 T)、sample bias Vb(=eE)、针尖位置 r | 输出观测量：STM 形貌 z(x,y)、dI/dV(x,y,E)∝LDOS | 声称结论：AB–BA 畴壁承载对称保护拓扑边缘态，局域于两边缘、高场稳健}`

**四层变量图**（符号层一次钉死）：

| 层 | Yin 2016 实例 |
|----|-------------|
| **L1 旋钮 u** | $B$（0–8 T）、sample bias $V_b$（STS 能量轴，图 2/3 横轴即 bias）、针尖位置 $r$（实空间扫描）；$T$=4.5 K 固定 |
| **L2 导出量 x₁** | $E=eV_b$（能量）、$E_g$（衬底诱导 gap，**非旋钮**）、CNP 偏移（AB/BA 差 ~15 meV） |
| **L3 模型量 x₂** | 畴壁宽度 $W$、$k_y$（y 向平移对称好量子数）、谷 $\xi=\pm$、Landau 指数 $n$、层极化 |
| **固定参数（非旋钮）** | 样品几何（剥离 BLG 解耦于石墨，扭转 10.0±0.5°）；理论 $t$=2.8 eV、$t_\perp$=0.4 eV、$D$=0.06 eV；$T$=4.5 K |
| **反推量 θ̂** | $E_g$=80±1 meV、$m^*$=(0.0454±0.0001)mₑ、$\|U\|$=77±3 meV（LL 拟合）；畴壁宽度 (8±1) nm、层间距离收缩 (1.5±0.5)%（原子像/2D-FFT） |
| **L4 观测量 y** | STM 形貌 $z(x,y)$、$dI/dV(\mathbf{r},E)$（STS 谱 + 能量固定 STS 图） |

> 与 E12（输运）根本差异：本文**无栅压**、无输运，旋钮只有 B / bias / 位置；gap 由衬底固定（~80 meV），不可调。E12 测 $\rho_{xx}$/$\rho_{xy}$，本文测 $dI/dV$（局域 LDOS）。

**可辨识性判别表**（唯一权威）：

| 判别 | 判据（数据） | 排除谁 | 确立谁 |
|------|-------------|--------|--------|
| **1D 结构 ≡ AB–BA 畴壁** | 原子分辨 STM 三角(AB)→类六角(中心)→三角(BA)（Fig 1c inset, 1e）+ 1D 结构强偏压依赖（SI Fig 3：高度 ~20/75/210 pm @ 400/100/30 mV）📜Q | graphene nanoripple / nanowrinkle（refs 27,28） | AB–BA 畴壁（层间平移完成 AB→BA） |
| **剪切 vs 拉伸孤子** | 边界法线与平移方向夹角 ~85° 📜Q | 拉伸孤子 | 近纯剪切孤子（ref 16） |
| **双层带隙 vs 单层无隙** | 质量型 Dirac LL（vs 单层质量型，SI Fig 1）+ Eq(1) 拟合 $E_g$=80±1 meV、$m^*$=0.0454 mₑ 📜Q | 单层石墨烯（质量型 Dirac 费米子） | 解耦 Bernal 双层 + 衬底破反演 → ~80 meV gap |
| **边缘态 vs 体态** | 隙内能量固定 STS 图（30/40/300 mV）1D 通道在**两边缘**（Fig 3a-c）；理论 $\rho(E,x)$ 顶层复现（Fig 3f）📜Q | 体态/均匀分布 | 1D 态局域于畴壁两边缘（不依赖能量） |
| **拓扑 vs 平凡束缚态** | 隙内 gapless 模不依赖畴壁类型/宽度（zigzag/armchair 计算，SI Fig 9）+ B 稳健到 8 T 📜Q | 平凡隙内束缚态（⚠️ 论文**未独立实验排除**） | 对称保护拓扑边缘态（理论 + 稳健性支撑） |
| **高场稳健** | 7.5 T STS 图（Fig 3g）+ FWHM 随 B 减小（SI Fig 11）📜Q | 磁场破坏的态 | 拓扑态 B 稳健 |

> **主结果 ↔ 判别表映射**：
> - 主结果① 1D 通道局域于两边缘 ← {边缘态 vs 体态}
> - 主结果② 结构 = AB–BA 剪切畴壁 ← {1D 结构 ≡ 畴壁, 剪切 vs 拉伸}
> - 主结果③ 衬底诱导 gap 80 meV ← {双层带隙 vs 单层无隙}
> - 主结果④ 拓扑性 + 高场稳健 ← {拓扑 vs 平凡束缚态, 高场稳健}
>
> **分层排除注**：「边缘态 vs 体态」证**存在 + 位置**（必要条件）；「拓扑 vs 平凡」靠**理论复现 + B 稳健性**，非一步证成——论文无手征性/谷保护/输运的独立测量，拓扑归属是"理论一致"而非"实验排除平凡"。

> **[前提与限定]**（判别结论的适用范围）：
> - **噪声/扰动**：石墨衬底 → "ultra-low random potential fluctuations"（正文 📜Q）→ 高质量原子分辨像；无序势 near DW → 边缘态分布不对称（SI Fig 10）；热展宽 $k_BT$(4.5 K)≈0.4 meV ≪ gap 80 meV（谱分辨率不受限）。
> - **判别性扫轴**：能量轴 $V_b$（30/40/300 mV，跨隙）、磁场轴 $B$（0–8 T）、空间轴 $r$（cross-DW 扫描）。⚠️ **无栅压轴**（gap 固定不可调）。
> - **候选集 M 边界**：{nanoripple, nanowrinkle, 单层质量型, 体态/均匀态, 平凡束缚态} —— "AB–BA 畴壁拓扑边缘态"在**论文枚举的**该集合内唯一幸存；但拓扑性依赖理论（Vaezi 2013, ref 12）+ 稳健性佐证，集外候选（平凡隙内态、针尖诱导态）未显式排除（封闭世界假设风险）。

> 三层标注：📜Q = 原文事实（附位置）｜推导｜📊F = 读图估算｜💭I = 推断。**不确定度（正交轴）**：[±] 原文误差棒 / [~] 原文无误差棒 / [读图] 图·色标提取 / [相对] 仅相对量。所有数字经 pdftotext + grep 反向核对。

---

## 2. 结果与机制（按论文论证结构：结构识别 / 电子性质 / 边缘态成像 / B 稳健）

### 2.1 结构：AB–BA 畴壁的识别（排除褶皱 + 剪切分类）

- 样品是解耦于石墨衬底的剥离 BLG（顶层相对衬底扭转 10.0±0.5°，moiré 周期 1.4±0.1 nm，SI Fig 1）📜Q[±]。
- **识别**：原子分辨 STM 三角(AB)→类六角(畴壁中心)→三角(BA)转变（Fig 1c inset / 1e）📜Q。这是畴壁的直接原子指纹。
- **排除 nanoripple/nanowrinkle**：1D 结构高度强偏压依赖（~20 pm @ 400 mV → ~75 pm @ 100 mV → ~210 pm @ 30 mV，SI Fig 3）→ corrugation 主要来自 LDOS 而非几何褶皱 📜Q[~]。
- **剪切 vs 拉伸**：边界法线与层间平移方向夹角 ~85° → 近纯剪切孤子（ref 16）📜Q[~]。
- **宽度双法互验**：实测 (8±1) nm（Fig 1e caption）；层间距离在畴壁区收缩 (1.5±0.5)%（2D FFT，SI Fig 4）→ 换算一臂式方向层间平移宽度 ~9.0 nm，与实测一致 📜Q[±]。

> **机制溯源五问**（[METHOD-Q]）：
> 1. **从何而来**：gap 符号在 AB→BA 反号（谷 Chern 数变，ref 12）→ 畴壁处 gap 闭合-重开 → 隙内 gapless 模 📜Q。
> 2. **量怎么定义**："畴壁宽度"(8±1) nm 是**结构宽度**（原子像），≠ 边缘态局域宽度（后者 FWHM 随 B 减小，SI Fig 11）——易混点。
> 3. **怎么提取**：$E_g$、$m^*$ 从 LL 谱拟合 Eq(1)；$\|U\|$≈$E_g$（SI Fig 2）。
> 4. **为什么随 B 变/不变**：边缘态**能量**不随 B 变（隙内 gapless）；**空间 FWHM** 随 B 减小（磁约束，波函数尺度 $\sim\sqrt{2N}\,l_B$，正文 📜Q）。
> 5. **与邻近概念区分**：本文态 = 零场隙内边缘态（vs 体 LL 需 B、空间尺度 ~10 nm；vs QH 边缘通道需 B）——本文态 B=0 已存在 📜Q。

### 2.2 电子性质：衬底诱导 gap + 质量型 LL 谱学

- 衬底破坏顶层相邻双层反演对称 → 抛物带开 gap ~80 meV（正文 📜Q[~]）；两 Bernal 区 CNP 差 ~15 meV 📜Q[~]。
- 高场：Bernal 区呈现**质量型 Dirac 费米子** LL 量子化（Eq 1，$n=2,3,4\dots$）；最低两个 LL(0,1,±) 是层极化四重态，符号随 gate polarity（gap 符号）在 AB/BA 反号 📜Q。
- 拟合 Eq(1) → $E_g$=80±1 meV、$m^*$=(0.0454±0.0001)mₑ（Fig 2d,e caption）📜Q[±]；BA 区单独拟合 $m^*$=(0.045±0.001)mₑ、$\|U\|$=77±3 meV≈$E_g$（SI Fig 2）📜Q[±]。
- 畴壁处 LL "劈裂" 来自相邻 AB/BA 畴 **CNP 相对偏移**（~15 meV），非边缘态本身 📜Q（→ [PHY-EF] band bending）。

### 2.3 边缘态成像（核心发现）

- 能量固定 STS 图（reflects LDOS in real space）：0 T、bias 30/40/300 mV 下，隙内 1D 导电通道沿畴壁，**主要局域于两边缘**（Fig 3a-c），且"independent of the energy of the gapless edge states" 📜Q。
- 理论（zigzag/armchair TB）：隙内 gapless 模"irrespective of the type and width of the domain wall" 📜Q；顶层 $\rho(E,x)$ 复现两边缘增强（Fig 3f）📜Q。
- 结论措辞："This provides **direct and compelling evidence** that the symmetry-protected topological edge states exist…" 📜Q。
- 不对称（Fig 3a,b）可能来自 CNP 差 ~15 meV 或近畴壁无序势（SI Fig 10）📜Q。

### 2.4 高场稳健

- 7.5 T STS 图（Fig 3g，30 mV）仍稳健；"quite robust even in the highest magnetic field ~8 T" 📜Q。
- FWHM 随 B 增大而减小（SI Fig 11，无绝对值，仅趋势）📜Q[相对] → 可能进一步抑制沿畴壁散射。
- 与输运 ref 14（Li 2016）互证：边缘态拓扑特征对 B 稳健、背散射在 B 下被进一步抑制 📜Q。

---

## 3. 实验方法

### 3.1 器件
HOPG（ZYA 级，NT-MDT）胶带剥离 → 剥离 BLG/三层解耦于石墨（扭转 ~10°）📜Q。**无栅极**（💭I：全文无 gate/Vg/位移场描述；gap 由衬底诱导 📜Q）。UHV STM（UNISOKU USM-1500S，B≤8 T，~10⁻¹¹ Torr，恒流模式）📜Q。

### 3.2 静电学
无栅。gap 由衬底破反演诱导 ~80 meV（正文）；AB/BA 两区 CNP 差 ~15 meV → 畴壁 LL "劈裂"（→ [PHY-EF]）。理论层间化学势差项 $D$=0.06 eV（§9）。

### 3.3 测量
4.5 K；Pt(80%)Ir(20%) 蚀刻针尖；dI/dV 锁相 793 Hz、5 mV ac 调制（关反馈）；横向尺寸用石墨烯晶格 + Si(111)-(7×7) + Ag(111) 标定 📜Q。

---

## 4. 关键数据（提取链 + 验证链 + 不确定度标注）

### 4.1 结构
| 参数 | 值 | 证据 |
|------|-----|------|
| 畴壁宽度 | (8±1) nm | Fig 1e caption 📜Q[±] |
| 层间距离收缩 | (1.5±0.5)% | 正文 + SI Fig 4 📜Q[±] |
| 收缩换算宽度 | ~9.0 nm | 正文 📜Q[~] |
| 剪切角 | ~85° | 正文 📜Q[~] |
| 顶层 vs 衬底扭转 | 10.0±0.5° | SI Fig 1 📜Q[±] |
| moiré 周期 | 1.4±0.1 nm | SI Fig 1 📜Q[±] |
| 理论宽度（zigzag/armchair） | 8.52 / 8.40 nm | Methods 📜Q[~] |

### 4.2 能隙与有效质量（LL 拟合 Eq(1)）
| 参数 | 值 | 证据 |
|------|-----|------|
| $E_g$ | 80±1 meV | Fig 2 caption 📜Q[±] |
| $m^*$ | (0.0454±0.0001)mₑ | Fig 2 caption 📜Q[±] |
| $m^*$（BA 区） | (0.045±0.001)mₑ | SI Fig 2 📜Q[±] |
| $\|U\|$（层间偏压） | 77±3 meV ≈ $E_g$ | SI Fig 2 📜Q[±] |
| CNP 差（AB/BA） | ~15 meV | 正文 📜Q[~] |

### 4.3 边缘态成像
- 0 T、30/40/300 mV 隙内 1D 通道在两边缘（Fig 3a-c）📜Q。
- 局域于两边缘、不依赖能量 📜Q。
- 7.5 T 稳健（Fig 3g，30 mV）📜Q。
- FWHM 随 B 减小（SI Fig 11，无绝对值）📜Q[相对]。

### 4.4 验证链（互验）
| 互验 | 两条独立证据 | 等级 |
|------|-------------|------|
| 畴壁宽度 | 原子像 (8±1) nm ↔ 收缩换算 ~9.0 nm | 一致 📜Q |
| 能隙 | $E_g$=80±1 meV（main）↔ $\|U\|$=77±3 meV（SI） | 一致 📜Q |
| 边缘态空间分布 | STS 图 ↔ 理论 $\rho(E,x)$（顶层） | 复现 📜Q |
| 高场稳健 | 本文 STM ↔ 输运 ref 14（Li 2016） | 互证 📜Q |

---

## 5. 主要结论

1. STM 首次直接成像 BLG AB–BA 畴壁拓扑边缘态：1D 通道主要局域于畴壁两边缘，不依赖能量 📜Q。
2. 畴壁 = 近纯剪切孤子（~85°），结构宽度 (8±1) nm（原子像与收缩换算互验）📜Q。
3. 衬底诱导 gap 80 meV（无栅压），$m^*$=0.0454 mₑ——质量型 Dirac 费米子谱学确立 📜Q。
4. 边缘态高场稳健（7.5 T），FWHM 随 B 减小 📜Q。
5. 作者强结论："direct and compelling evidence" 对称保护拓扑边缘态存在（⚠️ 拓扑归属靠理论 + 稳健性，非独立实验）📜Q。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 单条畴壁（非转角 mTBG 网络） | 未涉及 mTBG 畴壁网络 | 💭I（卡片） |
| 无栅压 | gap 固定由衬底诱导，不可调 | 💭I（原文无栅） |
| 拓扑性非独立实验证明 | 无输运/手征性/谷保护测量，未独立排除平凡隙内态 | 💭I |
| STM 局域测量 | 不代表宏观输运 | 💭I |
| 边缘态不对称来源未裁决 | CNP 差 ~15 meV vs 近畴壁无序势，两者未区分（SI Fig 10） | 📜Q |
| D→gap 换算未明示 | D=0.06 eV 与理论 gap 80 meV 的换算约定原文未给（§9） | 推导 |

---

## 7. 与其他工作的关系

| 工作 | 关系 |
|------|------|
| Martin 2008 (ref 8) | EFW 拓扑零模预言——本文畴壁的拓扑态理论起源 📜Q |
| Vaezi 2013 (ref 12) | AB–BA under uniform field ≡ gate-polarity DW；Chern 数变 → 本文 TB 计算的理论基（Eq 2 沿用）📜Q |
| Zhang/MacDonald/Mele 2013 (ref 10) | 谷 Chern 数边界态框架（本文引言引用）📜Q |
| Alden 2013 (ref 16) | 应变孤子——本文畴壁归类为"剪切孤子" 📜Q |
| Ju 2015 (ref 13) | 首次实验（s-SNOM + 输运）——本文补**直接成像** 📜Q |
| Li 2016 (ref 14) | EFW 输运——本文 ref 14，高场稳健互证 📜Q |
| Koshino 2013 (ref 30) | armchair 畴壁透射理论——本文 armchair 计算参照 📜Q |
| Huang 2018 (E9) | 后续：STM mTBG 螺旋态（双线 LDOS）——本文"两边缘"的先声（外部对标 💭I） |

> ⚠️ Phase S 外部对标（非本文引用）：本文"两边缘"空间分布 → Huang 2018 的双线 LDOS / Zheng 2022 Kagome 侧翼态的早期原型 💭I。

---

## 8. 对后续研究的影响

- 确立"能量固定 STS 图 + 原子分辨结构对照"为畴壁边缘态直接成像范式（后被 E9/E13/E14 沿用）📜Q→💭I。
- "两边缘"局域成为 mTBG 畴壁双线 LDOS（Huang 2018）的早期实验原形 💭I。
- 提供 TBPM 计算可**直接对标的 LDOS 数据**（§9）💭I。

---

## 9. 理论模型映射（供 TBPM / 紧束缚对标）

| 映射 | 说明 |
|------|------|
| 哈密顿量 | Eq(2)：$H=-t\sum_{l,\langle i,j\rangle}a^\dagger_{l,i}b_{l,j}+D\sum_{l,i}(-1)^l n_{l,i}-t_\perp\sum_i a^\dagger_{1,i}b_{2,i}+\mathrm{h.c.}$（AB 区；BA 区层间项换 $b^\dagger_{1,i}a_{2,i}$；畴壁区 $t_\perp=0$）📜Q |
| $t$, $t_\perp$ | 2.8 eV（层内）；0.4 eV（AB/BA 层间）；0（畴壁区，晶格失配近似）📜Q |
| **$D\to$ gap** | $D$=0.06 eV → Fig 3d caption "gap in the Bernal region of 80 meV" 📜Q；但按 TB 项 $\pm D(-1)^l$ 得层间化学势差 $2D$=0.12 eV → 隙 $2D$=120 meV（推导），**与 caption 80 meV 不符**；实验 $\|U\|$=77±3 meV≈$E_g$=80 meV。论文未给出 D 与 80 meV 的换算约定 → ⚠️ **NEEDS_VERIFICATION** |
| 畴壁宽度 $W$ | 理论 8.52/8.40 nm ≈ 实验 (8±1) nm 📜Q |
| 系统尺寸/边界 | zigzag 总宽 264 nm / armchair 156 nm，开放边界纳米带 📜Q |
| 观测量 | 顶层态密度 $\rho(E,x)=\sum_a|C_{l=1,a}(x)|^2\propto dI/dV(x,E)$（STS 主要探测顶层）📜Q |
| 求解 | y 向平移对称 → 部分傅里叶 → $H(k,l,x)$ 对角化 → 能带；固定 E 解本征模 → 空间分布判 kink/bulk 态 📜Q |

> 与 TBPM/Kubo 对应：本文模型是**小纳米带 TB**（156/264 nm 宽），TBPM 可直接复现 $\rho(E,x)$ 对标 dI/dV 图；但注意模型把畴壁区 $t_\perp$ 设 0（晶格失配近似）、且 $D\to$gap 换算存在上述不一致，对标前需先核对 Vaezi 2013 的约定 💭I。

---

## Phase S 目的接口（随项目增删，不进入正文）

- **Q1（edge state 如何表征）**：STM/STS 直接成像——能量固定 STS 图（LDOS 实空间）+ 原子分辨结构对照 + 边-体区分（隙内 1D 通道在两边缘 vs AB/BA gapped 谱）+ 高场稳健（§2/§4）。
- **Q2（理论如何解释）**：无新理论——Vaezi 2013 谷 Chern 数变 + 小纳米带 TB（Eq 2）；gap 符号反号 → 畴壁 gapless 模（§2.1/§9）。
- **Q3（理论↔实验对应）**：结构（原子像↔剪切孤子）、gap（LL 拟合 80 meV↔衬底诱导）、空间分布（STS 图↔$\rho(E,x)$ 顶层）、稳健性（B 稳健↔拓扑保护）（§4.4）。
- **增量价值**：本文是"畴壁拓扑边缘态存在性"的**直接成像基准**——E1 Ju 2015（s-SNOM+输运）缺实空间 LDOS，本文补齐；比同组 E5（Rh 箔，gap 170 meV）衬底更干净（石墨，gap 80 meV）且带原子分辨畴壁结构。report §2.1（STM 表征谱系）取用其"能量固定 STS 图 + 边-体区分"范式与 §4 数字。

---

## 反向核对 pass (2026-09-01)

pdftotext 提取正文 + SI，逐项 grep 核对：全部数字（80±1 meV / 0.0454±0.0001 mₑ / 0.045±0.001 mₑ / 77±3 meV / (8±1) nm / (1.5±0.5)% / ~9.0 nm / ~85° / ~15 meV / 10.0±0.5° / 1.4±0.1 nm / ~7° / 20/75/210 pm / 2.8 eV / 0.4 eV / 0.06 eV / 264/156/8.52/8.40 nm / 4.5 K / 793 Hz / 5 mV / 8 T / 10⁻¹¹ Torr / 30/40/300 mV / 7.5 T / 0.4 V·0.25 nA / 80×80 nm / LL(0,1,±) / zigzag / armchair / shear soliton / Chern）均在原文找到；"direct and compelling evidence""mainly located at the two edges""robust…~8 T"逐字核对（正文行号见上）。

⚠️ 本次修订关键点：① 确认"无栅极"（全文无 gate/Vg，gap 由衬底诱导）；② 保留并**精确化**旧注的 D→gap 疑问（D=0.06 eV 按 TB 项得隙 2D=120 meV，与 caption 80 meV 不符 → NEEDS_VERIFICATION）；③ 明确"拓扑性非独立实验证明"（无输运/手征性/谷保护测量，正文无 "chiral/quantized/4e²/h"）。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-18 | 态局域宽度 ~3-5 nm → 无源数字（幻觉）→ "局域于畴壁两边缘；畴壁结构宽度 (8±1) nm" |
| 2026-08-18 | 石墨局域底栅 → 与原文不符（石墨是衬底，非栅极）→ "石墨衬底，无栅极" |
| 2026-08-18 | 栅压依赖性 / 栅压范围 ~20V → 跨论文混淆（Vg 数据属 Huang 2018 E9）→ 删除，改为"衬底诱导 gap 不可调" |
| 2026-08-18 | LDOS 增强 5-10× → 无源数字（原文未给倍数）→ 删除倍数，标注 📜Q |
| 2026-08-18 | FWHM ~13±2 nm / 3-5 nm → 图读值未标注 → 13±2 保留并标 📊F 读图估算 |
| 2026-09-01 | **按 4 块新架构整体重写**（对齐 E12 canonical）：旧 IMRaD 结构 → 黑箱三要素 + 四层变量表 + 判别表置顶 + [前提与限定] + 主结果↔判别映射 + 提取链/验证链；全文补 📜Q/[±]/[~]/[相对] 分级 |
| 2026-09-01 | **FWHM ~13±2 nm 删除**（正文/SI 均无此绝对值；SI Fig 11 仅给趋势，正文只述"FWHM decreases with B"）→ 降级为 [相对] 定性趋势，不再列数值 |
| 2026-09-01 | **D→gap 疑问精确化**：旧注"若每层 ±D 则 U=2D=120 meV，若 U=D 则 60 meV" 修正为"TB 项 ±D(-1)^l → 层间化学势差 2D=0.12 eV → 隙 2D=120 meV，与 caption 80 meV 不符"；标注 NEEDS_VERIFICATION（推导，非 📜Q） |
| 2026-09-01 | **拓扑性归属澄清**：全文补"拓扑性非独立实验证明（无输运/手征性/谷保护测量）"；"chiral" 仅见于 SI Fig 9 标题，正文用 "symmetry-protected topological gapless mode" |
