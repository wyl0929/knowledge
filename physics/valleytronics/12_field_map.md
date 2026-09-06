<!--
Field: 量子谷霍尔效应与谷电子学（Quantum Valley Hall Effect & Valleytronics）
Mode: full_onboarding
Domain archetype: science_technical
Created date: 2026-09-02
-->

# 12 Field Map / 领域地图

Last updated: 2026-09-02

## 使用说明

本文件把谷电子学/QVH 拆成问题链、方法谱系、成熟度、核心假设和瓶颈，服务 gap table / frontier compass / project candidates。每个子方向不只列关键词，还说明研究问题、基本模型、典型证据、当前难点。

Field / 领域：量子谷霍尔效应与谷电子学（QVH / Valleytronics）

## 1. One-Sentence Field Definition / 一句话定义

### 一句话解释

谷电子学研究的是：如何把二维材料布里渊区里两个"镜像"的谷（K / K′）当成一个可编码、可输运、可探测的自由度——其中量子谷霍尔效应是"净霍尔电流为零、但谷分辨霍尔电流非零"的那支拓扑现象。

### 研究者版本

研究对象是时间反演对称下、以谷为内部量子数的能带拓扑与输运：输入 gapped 体系（破反演对称场/堆垛）的能带 Berry 曲率，输出谷陈数 $N_\nu$、谷霍尔电导 $\sigma_{xy}^V$、畴壁边界模与谷保护程度；评价方式是"谷陈数跳变能否束缚边界模、谷间背散射是否被抑制"。

## 2. Field Boundary / 领域边界

- **Studies / 研究什么**：谷陈数分类、谷输运（谷霍尔电导/谷流）、谷保护机制与证据、从双层到三层/TMD 的泛化。
- **Does not primarily study / 主要不研究什么**：总霍尔电导量子化（QHE）、自旋-轨道耦合自旋锁定（QSHE）、moiré 晶格重构与魔角关联态（TBG/强关联 platform）。
- **Adjacent fields / 相邻领域**：量子霍尔效应、量子自旋霍尔效应、twisted bilayer/multilayer graphene（平台）、强关联电子（tMBG 关联态）。
- **Common false equivalence / 常见错误等同**：QVH = QHE；helical = chiral；存在性 = 保护；谷保护 = 强保护（详见 `11_term_disambiguation.md`）。

## 3. Position in the Larger Chain / 在更大链条中的位置

```text
上游：二维材料 + 破反演对称场/堆垛（开隙）
  -> 抽象对象：单谷 Berry 曲率 / 谷陈数 N_ν
  -> 本领域核心环节：谷陈数跳变 → 畴壁边界模；谷间背散射抑制 → 谷保护
  -> 工具/实验/指标：STM LDOS、FT-STM QPI、谷霍尔输运、Kubo-Bastin
  -> 下游系统表现：谷流器件、谷阀、无耗散（软）输运通道
```

### 一句话解释

谷电子学是"从能带几何（Berry 曲率）到谷选择性输运"中间不可跳过的一层：不把它讲清楚，就无法判断"畴壁态是否真的受保护、器件能否用"。

### 为什么困难

这条链在四处会断：① 谷陈数不是严格拓扑不变量（依赖谷守恒近似，ZMM 2013 明言）；② 谷不守恒 → 谷霍尔电导无法严格量子化；③ 谷保护是软保护，原子缺陷即破坏；④ 保护证据的实验判定极难（级④抗无序量化输运未闭环）。

## 4. Subareas as Method Families / 子方向谱系

| Subarea | 人话解释 | Core question | Standard models | Common methods | Typical evidence | Maturity | Main trade-off |
|---|---|---|---|---|---|---|---|
| 谷陈数框架 | 谷陈数如何给畴壁态"编号" | 哪些畴壁有几条保护模 | 2/4 带连续模型、紧束缚 | Berry 曲率积分、Fukui-Hatsugai-Suzuki | ZMM 2013 分类、Martin 2008 零模 | mature | 单谷近似 vs 谷守恒破坏 |
| 谷输运 | 谷流怎么产生/检测 | 谷霍尔电导能否测到、能否量化 | valley Hall 输运、非局域/光学检测 | 输运测量、s-SNOM、纯谷流 | Ju 2015、Shimazaki 2015、Li 2016 | mature（双层）/ emerging（trilayer） | 谷分辨读出 vs 谷不守恒 |
| 谷保护 | 谷间背散射是否被抑制 | 保护成立条件、失效方式、实验判据 | 螺旋网络模型、QPI | FT-STM 散射空间判据 | Verbakel 2021 FFT | active frontier | 平滑势保护 vs 原子缺陷破坏 |
| 泛化 trilayer/TMD | 三层/TMD 的谷物理 | $C_v=\pm3$ 通道数、谷保护是否同样软 | chirally-stacked N 层、TMD 谷 Zeeman | 理论推演 + 实验待补 | Chen 2021、Phong 2026 | emerging | 层数/材料泛化 vs 证据缺失 |

### 子方向展开：谷陈数框架

**一句话解释：** 谷陈数是"每个谷单独算的几何相位整数"，它决定一个畴壁上有几条受保护的边界模。

**它在解决什么问题：** 把双层石墨烯三类畴壁（EFW/LSW/补偿墙）统一到"谷陈数跳变"这一把尺子上。

**基本模型 / 最小公式：**（ZMM 2013 两带模型）

$$
\Omega_\nu(\mathbf q)=\mp\frac{2\nu\gamma\Delta\, q^2}{(q^4+\gamma^2\Delta^2)^{3/2}},\qquad N_\nu=-\nu\,\mathrm{sgn}(\Delta)=\pm1,\qquad \Delta N_\nu=\pm2
$$

**大概怎么做：**

```text
输入：gapped 双层能带（Δ 符号随位置）
  -> 参数化：单谷两带有效哈密顿量
  -> 执行：Berry 曲率积分 / 紧束缚 Fukui 方法
  -> 指标：每谷 N_ν、畴壁跳变 ΔN_ν
  -> 结论：边界模数 = |ΔN_ν|（每谷每自旋）
```

**典型证据：** ZMM 2013 分类（EFW=LSW 拓扑等价、补偿墙无模）；Martin 2008 预言"two zero modes per kink per valley per spin"。

**为什么困难：** 谷陈数依赖谷守恒；armchair 边界、原子级尖锐缺陷可使其失效。

**和用户背景的关系：** tbplas + Kubo-Bastin 可直接对标谷陈数/边界模计算（见 `23_mvp_experiment_plan.md`）。

### 子方向展开：谷保护

**一句话解释：** 谷保护 = 翻谷需要补大动量，平滑势给不出、原子缺陷给得出。

**它在解决什么问题：** 畴壁态"会不会被背散射"的机制与实验判定。

**基本模型 / 最小公式：**（[PHY-QPI]）intervalley 散射需散射势提供 $|\Delta K|=\frac{4\pi}{3\sqrt3 a}\approx1.70$ Å⁻¹；平滑势 $V(q\approx0)$ 给不出 → 谷守恒；点缺陷白谱 → intervalley 打开。

**大概怎么做：**

```text
输入：原子分辨 STM 图
  -> 执行：2D FFT → q 空间功率谱
  -> 指标：(√3×√3)R30° 斑（|ΔK|≈1.70 Å⁻¹）有/无
  -> 结论：无斑 = intervalley 背散射被抑制 = 谷保护
```

**典型证据：** Verbakel 2021 三对照（pristine 无斑 / H 缺陷有斑 / TBG 网络无斑）。

**为什么困难：** 判据是"测量分辨率内无峰"，非绝对零；结论只对 defect-free 网络成立。

**和用户背景的关系：** FFT-STM 的 q 空间功率谱 = 实空间 LDOS 的 2D FFT，可由 TBPM 算 LDOS(r) 后 FFT 复现（[PHY-QPI] 已标）。

## 5. Conceptual Axes / 理解这个领域的坐标轴

### Axis 1：内部量子数（谷 vs 自旋 vs 总电荷）

```text
谷（QVH，时间反演，软保护）
  <->  自旋（QSHE，时间反演，软保护）
  <->  总电荷（QHE/QAHE，破时间反演，强保护）
```

- 左端适合：石墨烯/TMD 的天然谷自由度，无磁、无强 SOC。
- 右端适合：需量子化总 σ_xy 的计量/手征器件。
- 核心 trade-off：越靠"谷"端，器件越无需磁场/磁性，但保护越软。
- 用户应如何用这个轴读论文：先问"这篇的拓扑不变量是哪个内部量子数、保护有多强"。

### Axis 2：证据强度（存在性 → 保护）

```text
① 存在性（STM LDOS） <-> ② 形态一致 <-> ③ 谷保护（FFT） <-> ④ 抗无序量化（未闭环）
```

- 左端：必要非充分，只能"态在那儿"。
- 右端：最强证据，但实验/计算至今未闭环。
- 核心 trade-off：越往右越难做、越有发表价值。
- 用户如何用：读 QVH 论文时把每条结论归到某一级，别把①③混成"已证保护"。

### Axis 3：平台（双层 → 三层 → TMD）

```text
双层 AB/BA（成熟） <-> 三层 ABC/ABA（emerging） <-> 单层/TMD（材料泛化）
```

- 左端：证据最全（E1–E14 几乎都在双层）。
- 右端：三层 $C_v=\pm3$ 待核、谷保护待证；TMD 另需谷-Zeeman/SOC。
- 核心 trade-off：越往右越新、越缺直接实验。

## 6. Core Assumptions / 核心假设

| Assumption | Used by whom | Why it matters | Failure mode | Evidence status |
|---|---|---|---|---|
| 谷守恒（无 intervalley 散射） | ZMM 2013 及几乎所有谷陈数分类 | 谷陈数/谷霍尔电导量子化的前提 | 原子缺陷/armchair 边界打开 intervalley → 谷陈数失义 | suspected（软保护，已证可被单缺陷破坏） |
| 畴壁两侧谷陈数反号 | AB/BA 畴壁、EFW | 边界模存在的依据 | 补偿墙 $\Delta N_v=0$ → 无模 | source_checked（ZMM 2013） |
| 三层 $C_v=\pm3$（每谷 3 模） | [PHY-BERRY]、交接表 | tMBG 畴壁通道数 | 若实为 $N/2$ 半整数约定 → 通道数/谷陈数措辞需改 | suspected（NEEDS_VERIFICATION，ZMM 明言 ABA 三层谷陈数难定义） |
| 谷保护在 trilayer 同样"软" | 无直接实验的外推 | tMBG 器件可行性 | 三层 intervalley 动量失配可能不同 | suspected（NEEDS_VERIFICATION） |

## 7. Known Bottlenecks / 已知瓶颈

| Bottleneck | 人话解释 | Affected subarea | Current workaround | Opportunity | Verification status |
|---|---|---|---|---|---|
| 谷不守恒 → 谷霍尔电导无法严格量子化 | 谷霍尔电导只在谷守恒近似下量子化 | 谷输运 | 用 FFT/非局域测"有/无"而非精确值 | 定量谷霍尔电导的数值基准 | source_checked |
| 谷保护实验判定难 | 级④抗无序量化输运未闭环 | 谷保护 | Verbakel 2021 FFT（级③，间接） | 抗无序量化输运的紧束缚/Kubo 数值 | suspected（G-001） |
| 谷分辨读出 | Kubo-Bastin 默认算总电导，未分解到 K/K′ | 谷输运、MVP | 需改代码投影到谷子空间 | 谷分辨 Kubo-Bastin 是直接缺口 | NEEDS_VERIFICATION（G-003） |
| trilayer 证据缺失 | tMBG 三层畴壁/谷保护无直接实验 | 泛化 trilayer/TMD | Chen 2021/Phong 2026 理论待核 | tMBG 谷陈数/谷保护数值对标 | NEEDS_VERIFICATION（G-002） |

## 8. What Not To Overclaim / 不要过度声称什么

| Risky claim | Why risky | Safer wording |
|---|---|---|
| "谷霍尔电导严格量子化" | 谷不守恒，无严格平台 | "在谷守恒近似下，谷霍尔电导取 $N_\nu e^2/h$" |
| "STM 看到畴壁态 = 证了拓扑保护" | 存在性 ≠ 保护（肯定后件谬误） | "观察到畴壁态存在 + 形态一致，是必要非充分证据" |
| "谷保护 = 无耗散" | 软保护，单缺陷即破坏 | "defect-free 且平滑势下 intervalley 背散射被抑制" |
| "三层 $C_v=\pm3$ 与双层同构" | ZMM 明言 ABA 三层谷陈数难定义、通道数对应待核 | "三层每谷预计 3 条模，但谷陈数约定需 Chen/Phong 原文核" |
