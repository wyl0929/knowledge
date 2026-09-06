<!--
 * @Author       : msTTG project agent (deep-reading, paper-reading SKILL v1.0)
 * @Date         : 2026-09-03
 * @Description  : E13: Pierce et al. (2025) Nature Physics — 轻/重电子可调相互作用（局域压缩率 SET，msTTG 单栅器件；4 块辨识结构）
 -->

# Paper Review: Pierce et al. (2025) — Tunable interplay between light and heavy electrons in twisted trilayer graphene

| 字段 | 内容 |
|------|------|
| **编号** | E13 |
| **标题** | Tunable interplay between light and heavy electrons in twisted trilayer graphene |
| **作者** | Andrew T. Pierce¹, Yonglong Xie¹, Jeong Min Park², Zhuozhen Cai¹, Kenji Watanabe⁴, Takashi Taniguchi⁵, Pablo Jarillo-Herrero², Amir Yacoby¹（¹Harvard；²MIT；⁴⁵NIMS；共同一作：Pierce/Xie/Park；Pierce 现 Cornell，Xie 现 Rice） |
| **期刊** | **Nature Physics 21, 1237–1242 (2025)**（received 18 Dec 2023；accepted 28 May 2025；published online 26 June 2025）⚠️ registry 曾误记为 "Nature 2024"，实为 Nature Physics 2025（见更正日志） |
| **DOI / arXiv** | 10.1038/s41567-025-02956-z / arXiv:2401.12284（⚠️ arXiv 号来自项目注册信息，正文未出现 → 外部来源） |
| **类型** | 实验 — 扫描单电子晶体管（scanning single-electron transistor, SET）局域压缩率（local compressibility dµ/dn）+ 局域离散电荷传感（discrete charge sensing） |
| **课题组** | Harvard (Yacoby) × MIT (Jarillo-Herrero) × NIMS (Watanabe/Taniguchi) |
| **PDF / SI PDF** | ✅ /home/wyl/project/knowledge/physics/mirror_symmetric_ttg/references/exp/Pierce 等 - 2025 - Tunable interplay between light and heavy electrons in twisted trilayer graphene.pdf（txt 提取：/tmp/msTTG_txt/E13_pierce2025.txt） |
| **精读日期** | 2026-09-03 |

> **共享知识引用**：本 field pack 尚为 FRESH（note/ 下无 shared/ 讲义），无 [PHY-*] 锚点可引用 → 本笔记自包含；通用物理不在此展开。本文所有位置引用给出正文节名 + txt 行号（L#）便于反向核对。

---

## TL;DR

**本文想解决的问题**：在镜面对称魔角三层石墨烯（mirror-symmetric twisted trilayer graphene, msTTG/MATTG）中，轻（light）Dirac 电子与重（heavy）平带电子**如何共存、如何相互耦合**，以及这种"轻/重二流体"如何决定零场整数填充关联态与电荷中性点（charge neutrality point, CNP）附近高场相变的性质——从而约束"含色散带的扭转多层石墨烯中超导为何相空间更宽"这一问题的微观图景。

**主结果**（数字带标注）：
1. 单栅 msTTG 器件（θ≈1.53°，cut-and-stack，无顶栅）中，高场相位图的 Chern 数可严格分解为 Dirac（轻）与平带（重）两子系统的贡献之和 C = C_d + C_f；重构的 Hofstadter 能谱直接暴露轻 Dirac 带的 |N|>0 Landau 能级（Landau levels, LLs），给出 **v_F = (1.014 ± 0.002) × 10⁶ m s⁻¹** 📜Q[±]（Methods「Estimates of Fermi velocity」，L672），与单层石墨烯一致——轻/重带**共存且杂化可忽略**。
2. **零场部分能隙态（partially gapped states）**：ν = 1, ±2, 3 处的不可压缩（incompressible）峰稳定到 B = 0，但峰位偏离整数 ν（高场轨迹外推到 B=0 的 ν_f 为整数）→ 平带子系统打开关联能隙时，费米能级处仍有**有限数目的轻 Dirac 电子**（ν_d ≠ 0）；与"真绝缘体（zero DOS at E_F）"的判别实验（局域化电荷岛/充电峰 vs Dirac 电子屏蔽）确认该图景 📜Q（正文「Partially gapped states at zero magnetic field」，L293–431）。
3. **CNP 高场新相变序列**：ν_LL = ±6 为最强不可压缩峰（4 重 Dirac N=0 + 8 重平带 N=0 LL），±6 之间每个整数填充均有峰（自旋/谷/层简并全劈裂）；**巨负压缩率（giant negative compressibility）**区打断 ν_LL = −5,…,0 的整数量子霍尔峰，对应 Dirac LL 逐个去填充（depopulation）的相变；平均场模型需 **U ≈ 20W**（W 为 LL 宽）才能复现 📜Q（正文「Unexpected phase transitions near charge neutrality」，L465–543）。该相变序列在 ~9 μm（摘要措辞 "nearly 10 μm"）范围**鲁棒但具复杂空间依赖**：ν_i 空间变化不能全由局域扭转角 θ 解释 → 相变作为"味道自由度 g 因子"的局域探针。

**结论/意义**（保留作者措辞强度）：作者结论措辞为 "firmly establish and quantify the presence of Dirac electrons"（📜Q，L534–535）；相变区 Dirac 扇区被提议视为**类似自旋与谷的新量子数（flavour）**（"the Dirac sector can be viewed as a flavour analogous to the spin and valley degrees of freedom"，📜Q，L508–509，摘要 L34–35）。对超导的直接作用作者明确留作开放问题："whether they play any role in stabilizing superconductivity"（📜Q，L539–541）；但观测到 Dirac 带布居在 |ν|=2,3 最大，"this moiré filling window is where superconductivity is commonly observed"（📜Q，L727–730）——仅相关性陈述，非机制证据。

---

## 1. 系统辨识导览（判别表为全文唯一权威）

**黑箱三要素**：`{输入旋钮 u | 输出观测量 y | 声称结论}`

- 输入旋钮 u：背栅密度 n（以 moiré 填充因子 ν = n/n_s 表达）；垂直磁场 B（~0–11 T）；局域位置 r 与 SET 针尖-样品电压 V_t-s（局域静电势控制）；温度 T（输运/超导表征用）。**位移场 D 不是旋钮**：单栅几何（无顶栅），D 不可独立调、存在小的残余 D（见 [前提与限定]）。
- 输出观测量 y：局域逆压缩率 dµ/dn（SET 交流法，色标单位 ×10⁻¹¹ meV cm⁻²，⚠️ fig.1b 图内印为 mV cm⁻²，见更正日志）；离散充电信号 δI_SET（pA，局域化态指纹）；R_xx(T)（超导判据）；由 dµ/dn 轨迹外推的局域 θ（反推量之一）。
- 声称结论：(a) 轻 Dirac 与重平带共存、零杂化、弱耦合；(b) 零场整数填充"不可压缩态"实为平带隙 + 费米面上有限 Dirac 电子（非真绝缘体）；(c) CNP 高场存在由两子系统 N=0 LL 强耦合驱动的相变序列，Dirac 扇区可视为新味道自由度；(d) 该序列作为局域环境（g 因子）探针。

**四层变量图**（符号层一次钉死）：

| 层 | 本文实例 |
|----|----------|
| **L1 旋钮 u** | n（或 ν = n/n_s）、B、局域位置 r、V_t-s、T（D 固定 ≈ 0，不可调） |
| **L2 导出量 x₁** | ν = n/n_s；ν_LL = nh/eB；Chern 数 C（Streda 轨迹 dn/dB = Cϕ/ϕ0 + s）；重构 Hofstadter 谱 μ(n,B)；C_f = C − C_d（C_d = ±2）；高场轨迹 B=0 截距（= ν_f 整数）；ν_d = ν − ν_f |
| **L3 模型量 x₂** | 平均场 Gibbs 自由能 G = Σᵢ(Tᵢ(νᵢ)+gᵢμ_B B) + U Σᵢ≠ⱼ νᵢνⱼ；LL 动能取高斯形（宽 W）；Dirac-平带两 Dirac 点能量差 E_offset；密度-密度相互作用 U；LL g 因子（味道依赖）；C = C_d + C_f 可加性；ν = ν_f + ν_d |
| **固定参数（非旋钮）** | 石墨烯晶格常数 a ≈ 0.246 nm；n_s(θ) = 8θ²/(√3a²)；磁通量子 ϕ0 = h/e；SET 针尖直径 ≈ 100 nm、离样 ≈ 100 nm |
| **反推量 θ̂** | 局域扭转角 θ（位置1 ≈ 1.53°，位置2 ≈ 1.58°，拟合精度 ±0.02°）；轻带 Fermi 速度 v_F ≈ 1.014×10⁶ m s⁻¹；各整数填充的 Dirac 布居 n_D(ν)；LL g 因子组；各 ν_i 相变填充因子 |
| **L4 观测量 y** | dµ/dn(ν,B)、δI_SET 局域充电峰、R_xx(T)、Hofstadter 谱（n(µ) 点密度） |

**可辨识性判别表**（每条判别 = 判据 / 排除谁 / 确立谁）：

| 判别 | 判据（数据） | 排除谁 | 确立谁 |
|------|-------------|--------|--------|
| **D1 轻/重带共存且杂化可忽略** | ①高场 Chern 序列按 C = C_d + C_f 分离后，平带子系统的 C_f 序列与 MATBG 实验全同（📜Q「Coexistence…」L175–183, L293–309）；②重构 Hofstadter 谱暴露 |N|>0 Dirac LL（橙色点），v_F=(1.014±0.002)×10⁶ m s⁻¹ 与单粒子能带预言一致（L672）；③整数填充峰的中断模式与强杂化预言不符（L694–697）；④CNP 相变与"单个 Dirac 点"最自洽（L700–701） | "只有平带（MATBG-like）"的单带图景（解释不了大 Chern 数与色散特征）；**Dirac-平带显著杂化**（substantial hybridization，若杂化则 C_f 序列、峰中断模式、v_F 均会偏离） | msTTG 零 D 下 = MATBG 式平带 + 单层石墨烯式无质量 Dirac 带，二者共存、弱耦合；图 1b 高场部分可用"两子系统贡献相加"解释 |
| **D2 零场整数填充态 = 平带隙 + 费米面有限 Dirac 电子（非真绝缘体）** | ①高场 Chern 轨迹 B=0 截距处 ν_f 为整数，而 B=0 峰位偏离整数 ν → 有限密度偏移 ν_d ≠ 0（L305–315）；②密度偏移**非量子电容**所致：Δµ(能隙跨越) 与密度偏移不相关，栅压偏移比 Δµ 台阶大 1–2 个数量级（L697–699, L744–752）；③局域化判别实验：高场峰可分辨为单电子充电的局域化态（charge puddles），低场/零场下 Dirac 电子屏蔽无序 → 离散峰消失（ν=+2 短暂重返后消失）（L419–431, 图2h–k） | "零场弱电阻峰 = 真绝缘体（zero DOS at E_F）"的旧解释（输运/STM/全局 µ 测量无法区分——见 L701–707 挑战讨论）；量子电容伪信号 | 平带子系统自发对称性破缺打开能隙，Dirac 带更鲁棒、在 E_F 保持有限 DOS → "部分能隙态"；Dirac 布居 n_D 可定量（图2e，误差棒 = 线性拟合残差标准差） |
| **D3 CNP 高场相变 = Dirac–平带 N=0 LL 强耦合（Dirac 扇区 = 新味道自由度）** | ①ν_LL=±6 最强峰（4 重 Dirac + 8 重平带 N=0 LL 全满），±6 间每个整数有峰 → 两扇区 LL 简并全劈裂（L465–481）；②巨负压缩率打断 ν_LL=−5,…,0 的 IQH 峰（L485–488）；③单粒子线性色散 + 味道依赖 g 因子的能级图可复现打断位置与能隙演化（图3b、ED Fig.5）；④但负压缩率区需平均场 U≈20W 方能定性复现（L541–543, Methods）；⑤两位置 g 因子不同、ν_i 空间变化与 θ 只部分相关（L511–533） | 单粒子 LL 交叉图景（无 U 时不出现负压缩率区）；"整数 QH 区不应有此类相变"的常规预期（自由度受约束；对比非扭转多层石墨烯中由单粒子谷劈裂辅助的轨道间交叉 37,38）；MATBG-only 现象学（C 更大、峰中断于非整数处） | Dirac 与平带 N=0 LL 强关联（isospin/布居突变）；相变 = Dirac LL 逐个去填充（n_D 阶跃，图3d）；Dirac 扇区提供自旋/谷之外的第 4 类味道简并；空间 ν_i 变化 = 局域 g 因子变化的探针 |
| **D4 相位图鲁棒性（~9–10 μm）** | 空间图（图4a，B=11 T，9 μm 范围）相变序列可复现（L511–512）；但 ν_LL 处 ν_i 随位置变化（图4b）；θ 与 ν_i 在 0–5 μm 趋势相似、>5 μm 时 θ 快速演化而 ν_i 几乎不变（L523–526） | "扭转角空间变化是 ν_i 变化的唯一来源" | 相变鲁棒；ν_i 由 θ 之外的微观参数（→ 局域 g 因子）决定；SET 相变测量可作为电子环境的局域探针（L527–533） |

> **主结果 ↔ 判别表映射**：主结果①（共存/零杂化，v_F、C 分解）← {D1}；主结果②（零场部分能隙 + 有限 Dirac 布居）← {D2}；主结果③（CNP 相变序列、flavour 类比、空间依赖）← {D3, D4}。
> **分层排除注**：存在性（Dirac 电子存在于整数填充隙内）→ 定量（n_D(ν)）→ 耦合强度（弱耦合零场 vs 强耦合 CNP 高场）→ 新自由度（flavour 类比，作者措辞为 "can be viewed as / suggests"，属建议而非证明 📜Q）。作者明确称部分结论为解释性而非唯一证明（"enable us to establish…independent of any particular microscopic model" L429–431 只针对 Dirac 填充性；flavour 类比为模型建议）。

> **[前提与限定]**（判别结论的适用范围）：
> - **噪声/扰动**：局域无序势 φ 是中心分析对象（不是被抑制的背景）——用"压缩态屏蔽 vs 绝缘态电荷岛"响应来判别 DOS 是否为零；n_D 误差棒 = 高场线性轨迹拟合残差的标准差（图2e caption，L287–288）；密度不均一 δn_disorder 用于设定交流调制条件 eδn = CδV_BG < δn_disorder（Methods，L625）；单器件、两点 + 一条 9 μm 线扫描（无完整二维统计）。
> - **判别性扫轴**：B：0→11 T（压缩率主图）；ν：约 −6→+6（图1b 到 −4…+4 标注，图3 到 ν_LL ≈ −6…+2）；空间：两点 + 9 μm 线（位置1 θ≈1.53°，位置2 θ≈1.58°）；V_t-s 调局域电势（ED Fig.4）；T：输运中稀释制冷机底温 ~20 mK。**未扫 D 轴**（单栅限制）——"零位移场/零杂化"只能靠一致性论证（4 条证据，Methods「Evidence for negligible displacement field」），不能直接控制。
> - **候选集 M 边界**：结论在候选集内唯一幸存。①零场态的候选解释集：真绝缘体（被 D2 排除）｜弱电阻金属态（Dirac 电子，胜出）；②CNP 相变的候选集：单粒子 LL 交叉（非相互作用模型能复现打断位置与部分能隙演化，ED Fig.5，但负压缩率需 U）｜相互作用 isospin 相变（胜出）；③flavour 类比成立的范围 = 该平均场模型族；**集外未排除的必须声明**：位移场残余导致的弱杂化只能被"排除到与数据一致"，不能绝对排除；g 因子空间变化的微观来源（θ 之外是什么参数）未解；Dirac 电子对超导的作用未测（封闭世界假设风险：作者在 D3/D4 之外未宣称超导机制）。

三层标注：📜Q = 原文事实（附节名/txt 行号）｜推导｜📊F = 读图估算｜💭I = 推断。**不确定度（正交轴）**：[±] 原文误差棒 / [~] 原文无误差棒 / [读图] 图提取·色标值 / [相对] 仅相对量。**全文绝大多数数字无误差棒（除 v_F 与 θ 精度外），已按 QC 协议声明**。所有数字经 pdftotext + grep 反向核对（见文末 pass）。

---

## 2. 结果与机制（按论文自身论证结构三段）

### 2.1 段一：轻/重电子共存（"参照系"建立，Fig. 1）— 弱耦合图景

- 选材动机：MATTG 在零位移场带结构简单——平带几乎与 MATBG 相同（重），外加一条与单层石墨烯几乎相同的无质量 Dirac 带（轻）（📜Q，L154–157；带结构图 Fig.1a，蓝色平带/橙色 Dirac 带/灰色 remote bands，来自 Khalaf 2019 的预言 [ref 13]）。
- 图 1b：局域逆压缩率 dµ/dn 作为 (ν, B) 的函数；整数填充处出现鲁棒不可压缩峰，对应化学势变化"几个 meV"（📜Q[相对]，L157–159）；Chern 数经 Streda 公式 dn/dB = Cϕ/ϕ0 + s 从轨迹提取（📜Q，L167–168）。主 Chern 绝缘体列于 Wannier 图（Fig.1c）。
- **关键判别输入 1**：部分平带填充处 MATTG 出现 MATBG 不可能的大 Chern 数 → 轻带参与的证据；将 C 分解 C = C_d + C_f（费米面在导带/价带平带时分别减/加 2 得 C_f，因 Dirac 带在中等磁场已完全能隙化，贡献固定的 ±2）📜Q，L171–183。
- 0.5 T 特征场：仅 0.5 T 即可把轻 Dirac 带劈成宽能隙的四重简并 LL，且 N=0 级恰好钉在 B=0 Dirac 点能量（📜Q，L178–180）→ 这是后续"高场 ν_f 截距 = 平带整数填充"论证的物理前提。
- **关键判别输入 2（Hofstadter 谱）**：dµ/dn 对 n 积分重构 μ(n)、以 n(µ) 点密度作 DOS → 图 1e 实验 Hofstadter 谱；橙色点 = 快速色散的 |N|>0 Dirac LL，蓝色点 = 平带贡献；能量间隔分析给出 v_F ≈ 10⁶ m s⁻¹（正文，L301）与精确值 (1.014±0.002)×10⁶ m s⁻¹（Methods，L672）。在第二位置（θ≈1.58°）重复确认（ED Fig.2）。
- 段一结论：高场相位图 = MATBG 现象学 + 叠加的无质量 Dirac 带；两子系统杂化可忽略（📜Q，L305–309）。

### 2.2 段二：零场部分能隙态——轻电子填充的直接证据链（Fig. 2）

- 现象：ν = 1, ±2, 3 的不可压缩峰**稳定到 B=0**，但在 B < 0.5 T 偏离高场线性轨迹；同磁场区间有快速色散的可压缩特征"切穿"不可压缩峰（=|N|>0 Dirac LL）📜Q，L293–299。此前输运工作（Park 2021 [ref 11]、Hao 2021 [ref 12]、Zhang 2022 Science [ref 15]、Shen 2023 [ref 27]）把这些色散特征归为轻带 LL，但**未能在零场找到不可压缩态**；STM（Kim 2022 [ref 26]）与全局 µ 测量（Liu 2022 [ref 25]）探测到低压缩率特征 📜Q，L299–303 —— 即"不可压缩态与 Dirac 电子共存"的旧证据互相矛盾。
- 本文解法 1（密度偏移法）：高场下 Dirac 扇区完全能隙化 → 不可压缩峰高场轨迹外推到 B=0 的截距处 ν_f 为整数；观测到 B=0 峰位相对整数 ν 有**有限密度偏移** → 系统压缩率被压制时 ν_d = ν − ν_f ≠ 0（📜Q，L305–315）。
- 排除伪信号：该偏移**非量子电容**贡献——比较能隙上化学势变化 Δµ 与栅压偏移 ΔV_gate（ED Fig.3）：残差在 0→6.8 T 内（实验分辨率内）为零、约 0.7 T（Dirac LL 交叉场）开始下降、B=0 处达 −0.15 V；0 T 与 5 T 间残差差 0.15 V 而 Δµ 几乎相同；ΔV_gate 偏移比 Δµ 台阶大 1–2 个数量级 → 量子电容贡献可忽略（📜Q[~]，L739–752）。
- 本文解法 2（局域化判别实验，核心新方法）：真绝缘体（E_F 处 zero DOS）在无序势下破裂为局域化电荷岛网络，单电子充电产生**离散充电峰/充电环**（图2g 下、图2h–k 高场部分；ED Fig.4 证实峰随 V_t-s 可调、为局域态指纹）；而低但非零 DOS 的系统能屏蔽无序、不出现局域化态（图2g 上）。观测：高场时峰可分辨为离散局域态；**磁场降低后离散峰消失**（ν=+2 短暂重返再消失）→ 归因于 Dirac 电子在低场接近费米面、屏蔽无序（📜Q，L419–431）。结论独立于任何微观模型（"independent of any particular microscopic model"，📜Q，L429–431）。
- 机制叙述：平带可由自发对称性破缺打开能隙（类比 MATBG 关联绝缘体），而单层式 Dirac 带对该对称性破缺更鲁棒 → 阻止真绝缘体在 B=0 出现（📜Q，L411–417）。
- 定量：n_D 在**所有**整数填充（含 ν=0、±4）有限且对局域 θ 鲁棒；随 ν **非单调**（强相互作用的标志）；**|ν|=2,3 附近最大**——与超导常见填充窗重合（📜Q，L721–730；图2e [读图] 量级 ~10¹⁰ cm⁻²，见 §4）。

### 2.3 段三：CNP 高场相变——强耦合与新自由度（Fig. 3–4）

- 现象：CNP 高场 dµ/dn(ν_LL, B)：最强不可压缩峰在 ν_LL = ±6（4 重 Dirac N=0 LL + 8 重平带 N=0 LL 的满带=12 态全满/全空）；±6 之间每个整数填充都有峰 → 两扇区 LL 简并全劈裂（📜Q，L465–481）。
- **巨负压缩率区**打断 ν_LL = −5, −4, −3, −2, −1, 0 处 IQH 峰并贯穿本应完全可压缩的区域（📜Q，L485–488）；额外弱峰来自超 moiré（supermoiré）图案，与强负压缩率无关（L491–493）。
- 解释主张：峰被负压缩率打断 = isospin 极化与子系统布居**突变**的相变；此类特征此前仅见于分数量子霍尔区（composite fermion LL 的 isospin 相变，Feldman 2013 [ref 36]），在整数 QH 区极不寻常（自由度受约束）；四重结构提示与四重简并 Dirac N=0 LL 相关；对比非扭转多层石墨烯（单粒子谷劈裂辅助的轨道间 isospin 交叉）📜Q，L495–517。
- 建模：图 3b 单粒子能级图 = 两套线性色散 LL（Dirac 点相距 E_offset），味道依赖 g 因子；非相互作用模型（ED Fig.5）复现峰打断位置与能隙演化（定性）；但负压缩率需在能级间加**位点库仑 U**（类比 MATBG isospin 相变建模 39,40），U ≈ 20W 才定性复现（📜Q，L534–543）。图 3d：n_D（Dirac LL 布居数）在相边界**阶跃**；据此可按 n_D 画整个 ν_LL 的相图。
- **flavour 类比**：Dirac 扇区 = Hilbert 空间中类似自旋与谷的新量子数（📜Q，L508–509）——这是给理论/后续实验的核心概念输出。
- 空间维度：9 μm（摘要 "nearly 10 μm"）空间图（B=11 T）相变可复现但 ν_i 空间变化（图4a,b）；θ 与 ν_i 仅在 0–5 μm 趋势相似，>5 μm 处 θ 快速演化而 ν_i 基本不变 → θ 不是唯一决定因素，ν_i 反映 θ 之外的微观参数（局域 g 因子）📜Q，L511–533；第二位置（ED Fig.7）g 因子拟合结果不同。作者结论：相变可作为电子环境局域探针，微观来源留待后续。

**机制五问速答**（每问指向本文证据）：
- 轻/重电子从何而来？带结构预言（Khalaf 2019）：msTTG 零 D 带 = MATBG 平带 + 单层式 Dirac 带（📜Q，L154–157, L45–47）。
- 怎么定义"轻"？无质量 Dirac 锥，v_F=(1.014±0.002)×10⁶ m s⁻¹（≈单层石墨烯值）；"重"=平带（MATBG 同源）。本文**不以有效质量 m\* 表述**，用 v_F 与 LL 能级宽比（W_flat/W_dirac = 5，模型参数）量化轻重（📜Q，Methods L725）。
- 怎么提取？Hofstadter 谱 N=±1,±2 LL 能量差（v_F 公式）；密度偏移法 + 局域化判别（n_D）；Chern 轨迹（C、C_f）；平均场拟合（g 因子、E_offset、U）。
- 为什么随 ν/B 变？ν 控制两扇区相对填充（ν = ν_f + ν_d）；B 把 Dirac 扇区能隙化（>0.5 T）并让 N=0 LL 交叉（~0.7 T 起负压缩率/相变）；U 驱动 isospin 重排。
- 与邻近概念差在哪？"部分能隙态"≠ MATBG 关联绝缘体（后者可形成 zero-DOS 绝缘体，前者 E_F 处必有 Dirac DOS）；"Dirac 扇区 flavour"≠ 自旋/谷（是类比建议而非实测量子数，措辞 "can be viewed as"）；CNP 相变 ≠ 非扭转多层的轨道交叉（无单粒子谷劈裂主导）。

---

## 3. 实验方法

### 3.1 器件（cut-and-stack，msTTG 构型）
- 单栅（single-gated）hBN 封装 MATTG：单层石墨烯+ hBN 在 SiO₂/Si 上剥离质检，同一石墨烯片激光切成三块；玻璃载 poly(bisphenol A carbonate)–PDMS 印章 90 °C 先拾 hBN，室温拾第一块；Si 载台顺时针旋转约 1.53° 拾第二块，再逆时针 1.53° 回位拾第三块 → **外层两片对齐（0°）、中间片扭转 1.53°** = msTTG（📜Q，Methods「Device fabrication」，L620–637；θ 在正文 L144、图1a 标 1.53°）。
- 叠层释放在预置 hBN/PdAu 背栅上（175 °C）；电子束光刻 + RIE 定义几何；Cr/Au 边缘接触（edge contacts，ref 41）；器件光学图见 ED Fig.1a，测量点 1（θ≈1.53°）与点 2（θ≈1.58°）。
- ⚠️ 单栅 ⇒ 无顶栅（顶栅会挡住 SET 静电信号），D 不可独立调（📜Q，Methods「Evidence for negligible displacement field」，L679–682）。

### 3.2 静电学与量定义（本文自含，无 [PHY-GATE] 讲义可锚）
- n_s(θ) = 8θ²/(√3a²)，a ≈ 0.246 nm（📜Q，L678）；ν = n/n_s；ν_LL = nh/eB（L457）；Streda 公式 dn/dB = Cϕ/ϕ0 + s（L167–168）；C = C_d + C_f、C_d = ±2（费米面在平带导/价带时从总 C 减/加 2 得 C_f，L181–183）。
- 局域 θ 定标：由 ν=±4 出发的强 Chern 绝缘体线性轨迹外推到 B=0 密度 = 平带全空/全满点，按 n(B) = n_s + CB/ϕ0 拟合，**精度 ±0.02°**（📜Q[±]，L669–681）。

### 3.3 测量（扫描 SET 局域压缩率 + 离散电荷传感）
- SET 针尖直径 ≈100 nm，悬于样品上方 ≈100 nm；压缩率测量在 3He 低温恒温器（正文措辞）进行，协议同 Martin et al. 2010 [ref 28]（L648–655；输运部分在稀释制冷机、底温 ~20 mK，L641）。
- 交流法：背栅加小交流 δV_BG 调制密度，样品与栅同时加小交流偏置归一化 → 局域逆压缩率 dµ/dn；平衡时 δµ = −eδφ（SET 感受局域静电势变化）；PID 锁 SET 直流电流 → 直流补偿电压直接给出 µ(n)（📜Q，L654–667）。
- 离散电荷传感：选 eδn = CδV_BG < δn_disorder 的调制幅度，记录 δI_SET；观察"充电环"（charging rings）空间分布确认局域态，环形状可由 V_t-s 调（ED Fig.4；δn ~ 5.7×10⁸ cm⁻²，V_t-s = +1.35/+0.45/−0.65 V）。
- Hofstadter 谱重构：dµ/dn 对 n 积分得 µ(n)；各 B 均匀采样后以 µ 为横轴散点画 n(µ)，点密度 ∝ DOS；**负压缩率伪影处理**：将负压缩率区 1/(dµ/dn) 置 0（保留其对 µ 的影响）（L649–656）。
- 输运：稀释制冷机 ~20 mK；R_xx(T) 显示电子/空穴两侧超导均充分发展（ED Fig.1b caption；正文 L644–646）。

---

## 4. 关键数据（提取链 + 验证链 + 不确定度标注）

### 4.1 器件与计量参数

| 量 | 值 | 证据/不确定度 |
|---|---|---|
| 扭转角（点1） | ≈1.53° | 📜Q[~]（正文 L144、ED Fig.1 caption L800；图1a） |
| 扭转角（点2） | ≈1.58° | 📜Q[~]（ED Fig.2 caption L814） |
| 局域 θ 空间分布 | ~1.54–1.58° | 📊F[读图]（Fig.4c 横轴） |
| θ 拟合精度 | ±0.02° | 📜Q[±]（Methods L681） |
| SET 针尖直径 / 离样高度 | ≈100 nm / ≈100 nm | 📜Q[~]（Methods L652–653） |
| 输运底温 | ≈20 mK（稀释制冷机） | 📜Q[~]（Methods L641） |
| 超导 | 电子、空穴侧均存在，约在 ν = ±2 附近 | 📜Q[相对]（正文 L183 "robust superconductivity near ν = ±2"，ED Fig.1 caption L802） |
| 离散充电调制幅度 δn | ~5.7×10⁸ cm⁻² | 📜Q[~]（ED Fig.4 caption L840） |
| V_t-s | +1.35 / +0.45 / −0.65 V | 📜Q（ED Fig.4 caption L838–840） |
| 压缩率色标（图2） | dµ/dn：a −1.0→3.0、b −1.0→7.0、c −2.0→10、d −1.0→4.0 (×10⁻¹¹ meV cm⁻²)；δI_SET：h −0.65→0.80、i 0→1.5、j 0→2.0、k 0.5→1.7 (pA) | 📊F[读图]（Fig.2 caption L190–191, 234–235）⚠️ 仅作相对标度用；fig.1b 图内单位印为 mV cm⁻²（L65），与 fig.2 的 meV cm⁻² 不一致（见更正日志） |

### 4.2 物理结果关键数值

| 量 | 值 | 证据/不确定度 |
|---|---|---|
| 轻带 Fermi 速度 v_F | (1.014 ± 0.002) × 10⁶ m s⁻¹（由 N=+1,+2 LL 能量差拟合；正文写作 "approximately 10⁶ m s⁻¹"） | 📜Q[±]（Methods L670–675；正文 L301；公式 E_N = E_0 + sgn(N)v_F√(2eℏNB)） |
| Dirac 扇区完全能隙化的临界场 | ≈0.5 T（"beyond approximately 0.5 T"；"as little as 0.5 T is enough to break the light Dirac band into widely gapped fourfold-degenerate LLs"） | 📜Q[~]（L178–180, L310） |
| 稳定到 B=0 的整数填充峰 | ν = 1, ±2, 3（图2a–d；峰对应 µ 变化"several meV"） | 📜Q（L293–295, L157–159） |
| CNP 最强峰 / 峰密度 | ν_LL = ±6；±6 之间每个整数均有峰 | 📜Q（L465, L480–481） |
| 负压缩率打断的填充 | ν_LL = −5, −4, −3, −2, −1, 0（正文称 "four pronounced regions"，列 6 个填充——按原文照录） | 📜Q（L485–488）⚠️ "four regions" 与六个 ν_LL 的计数关系原文未展开 |
| 平均场参数（点1） | W_dirac ≡ 1 meV（归一化）；W_flat/W_dirac = 5；E_offset/W_dirac = 2；U/W_dirac = 20（正文 "U ≈ 20 W"）；g_Dirac = (−2.69, −0.28, 0.28, 2.69)；g_flat = (−8.08, −5.63, −3.14, 0) | 📜Q（Methods L724–727；正文 L542） |
| 平均场参数（点2，ED Fig.7 对应） | g_Dirac = (−2.53, −0.26, 0.26, 2.53)；g_flat = (−8, −5.65, −0.8, 0)；W/E_offset/U 同上 | 📜Q（Methods L728–731） |
| CNP 处 LL 总数目 | 12 个 = 平带 4（自旋×谷）+ Dirac 8（自旋×谷×层） | 📜Q（Methods L706–709；注意方向与正文 L471 的 "fourfold Dirac N=0 + eightfold flat N=0" 一致） |
| Dirac 布居 n_D(ν) | 所有整数填充（含 ν=0、±4）有限；随 ν 非单调；|ν|=2,3 最大；|ν|=2,3 = 超导常见填充窗 | 📜Q（Methods L721–730） |
| n_D 量级 | ~10¹⁰ cm⁻²（图2e 纵轴 ±(2–4)×10¹⁰ 区间） | 📊F[读图]（Fig.2e 轴标 L198–199）⚠️ 仅量级 |
| 空间鲁棒范围 | 9 μm（正文）/ nearly 10 μm（摘要）；图4a 于 B = 11 T | 📜Q[~]（L511, L33, Fig.4 caption L493） |
| 平均场对照场 | B = 8.44 T（图3c 虚线处，图3d） | 📜Q（Fig.3 caption L370, L402–403） |
| 量子电容检验 | 线性拟合残差 0→6.8 T 内在分辨率内为零，~0.7 T（Dirac LL 交叉）起降，B=0 达 −0.15 V；0 T 与 5 T 残差差 0.15 V 而 Δµ 几乎相同；栅压偏移比 Δµ 大 1–2 个数量级 | 📜Q[~]（Methods L739–752） |
| 晶格常数 / n_s | a ≈ 0.246 nm；n_s(θ) = 8θ²/(√3a²) | 📜Q[~]（Methods L678） |

### 4.3 验证链（互验 / 旋钮依赖）
- **两点互验**：位置1（1.53°）与位置2（1.58°）Hofstadter 谱一致（ED Fig.2）；CNP 相变在位置2 重复且 g 因子不同（ED Fig.7）→ 现象学鲁棒、参数依赖位置。
- **旋钮依赖**：B 依赖（0.5 T 能隙化 Dirac；~0.7 T 起 LL 交叉/负压缩率；图3a 相变轨迹）；ν 依赖（n_D(ν) 非单调）；空间依赖（图4）；V_t-s 依赖（ED Fig.4 充电环可调）。
- **方法互验**：两种独立方法给同一结论——密度偏移法（截距分析，含量子电容排除）与离散电荷/局域化判别法（真绝缘体 vs 低 DOS 屏蔽）→ "整数填充隙内有有限 Dirac DOS"。
- **负面对照**：量子电容伪信号对照（ED Fig.3）；杂化情景排除（4 条一致性证据，Methods）；超 moiré 弱峰与强负压缩率无关（L491–493）。

---

## 5. 主要结论

1. **共存且弱耦合**：msTTG 零位移场下重平带 + 轻无质量 Dirac 带共存，杂化可忽略；高场相位图 = 两子系统贡献可加（C = C_d + C_f），Hofstadter 谱 + v_F 定量确认（📜Q，作者强度 "firmly establish"，L534–535）。
2. **零场整数填充态是"部分能隙态"而非真绝缘体**：平带扇区开关联隙、E_F 处保留有限 Dirac 电子（ν_d ≠ 0，所有整数填充含 ±4、0）；这解释了既往输运弱电阻峰/低 DOS 区域的矛盾观测（📜Q，L166–169）。
3. **CNP 高场相变 = Dirac–平带 N=0 LL 强耦合**：巨负压缩率打断 IQH 峰（ν_LL = −5…0），n_D 阶跃；U ≈ 20W 平均场模型复现；Dirac 扇区可视为自旋/谷类似的新 flavour（📜Q + 作者建议性措辞，L508–509）。
4. **相变序列鲁棒（~9–10 μm）但 ν_i 空间变化**，与 θ 只部分相关 → 局域 g 因子空间变化；相变可作为电子环境局域探针（📜Q，L527–533）。
5. **对超导的意义（开放）**：Dirac 电子在 |ν|=2,3（超导常见窗）布居最大，提示联系；但过量轻电子在更高掺杂的 fate 与是否稳定超导 = "key unresolved question"（📜Q，L536–541）——论文不做超导机制断言。

---

## 6. 局限与未解决

- **单栅器件，D 轴缺失**：无顶栅 ⇒ D 不可独立调（顶栅遮挡 SET 信号，L679–682）；"零/弱 D、零杂化"只能靠 4 条一致性证据间接支持，无法直接控制——对本项目"位移场可调性 → 超导"叙事，本文**未提供 D 调制的可调性数据**（需 E2 Park 2021 / E14 Zhou 2025 等双栅器件补）。
- **单器件、采样几何有限**：压缩率主数据在位置1；第二位置 + 9 μm 线扫描，无二维面统计；n_D 估计依赖高场线性轨迹外推假设（Dirac 在 >0.5 T 全能隙化、N=0 钉在 Dirac 点能量）与拟合残差误差棒。
- **平均场模型现象学**：12-LL 截断（4 平带 + 8 Dirac）；LL 动能高斯形、宽度 W 与 E_offset 为唯象输入；正 g 因子平带 LL 被直接丢弃（"do not participate to level crossings"，L712–713）；g 因子无微观来源；U ≈ 20W 很大；"定性复现"（qualitatively reproduce）措辞（L542–543）。
- **g 因子空间变化的微观起源未解**：θ 之外什么参数起作用？作者明言需后续工作（L530–533）。
- **flavour 类比是建议非证明**："can be viewed as"（L508）；四重结构与 N=0 Dirac LL 的联系是提示（"suggests a connection"，L513–514）。
- **Dirac 电子与超导的直接因果未测**：超导仅在输运（ED Fig.1b）表征；本文压缩率测量与超导窗的重合是相关性；作者自述开放问题。
- **测量一致性小瑕疵**：摘要 "nearly 10 μm" vs 正文 "9 μm"；图1b 色标单位 mV cm⁻² vs 图2 meV cm⁻²（pdftotext 所见，需人工对照原 PDF 图确认）；正文 "four pronounced regions…at ν_LL = −5,…,0" 的计数表述（见更正日志）。
- **报告范围**：负压缩率区的"giant"表述与色标范围基于图内色标（[读图]），绝对值大小需以原文源数据为准。

---

## 7. 与其他工作的关系（跨论文对标）

> 本节仅横向定位，不做同族逐数字核对；registry E-编号只在文件名可确认处引用（E1 Hao 2021、E2 Park 2021、E6 Li 2022、E7 Turkel 2022、E9 Kim 2023、E14 Zhou 2025）。

- **同族实验（超导/关联态）**：本文器件即复现 E2 Park 2021（Nature 590, 249；MATTG 强耦合超导，[ref 11]）与 E1 Hao 2021（Science 371, 1133；电场可调超导，[ref 12]）的超导标志（ν=±2 附近，ED Fig.1b）。**本文增量**：此前输运（Park 2021 [ref 11]、Hao 2021 [ref 12]、Zhang 2022 Science [ref 15]、Shen 2023 Nat. Mater. [ref 27]）虽把快速色散特征识别为轻带 |N|>0 LL，却未在零/小位移场找到零场不可压缩态（📜Q，L298–301）；STM（Kim 2022 Nature 606 [ref 26]）与全局 µ（Liu 2022 Nat. Phys. [ref 25]）只见低压缩率特征——本文用局域 SET 的"密度偏移 + 局域化判别"双通道**把零场低压缩率特征确立为"平带隙 + 有限 Dirac DOS"，并首次定量 n_D(ν)**。
- **与 MATBG 谱系**：平带扇区 Chern 序列与 MATBG 实验一致（Pierce 2021 Nat. Phys. [ref 30]、Yu 2021 Nat. Phys. [ref 31] Hofstadter）；MATTG 在部分平带填充处出现 MATBG 不可及的大 Chern 数 = 轻带指纹；CNP 负压缩率/相变的建模借用 MATBG isospin 级联方法（Zondiner 2020 Nature [ref 39]、Park 2021 Nature [ref 40]）。
- **与非扭转多层对比**：Taychatanapat 2011（[ref 37]）、Datta 2017（[ref 38]）的 LL 交叉由单粒子谷劈裂等辅助；本文相变在整数 QH 区、无此类单粒子机制 → 强关联主导（L514–517）。
- **超 moiré**：弱峰归因于超 moiré 图案，衔接 E7 Turkel 2022（Science 376, 193 [ref 34]）与 Xie et al. 2024 preprint（[ref 35]，另一篇同组工作，n_D 数据图 1d 亦取自它）📜Q，L718–719。
- **理论谱系**：带结构预言 Khalaf 2019（[ref 13]，"magic angle hierarchy"：平带 + 单层式 Dirac 带）；重费米子/近藤图景 Ramires & Lado 2021（[ref 17]）、Yu–Xie–Bernevig–Das Sarma 2023（[ref 18]，msTTG 拓扑重费米子映射）、Song & Bernevig 2022（[ref 19]）、Chou & Das Sarma 2023（[ref 20]）、Zhou et al. 2024（[ref 21]）、Hu et al. 2023（[refs 22,23]）——本文结论（Dirac 扇区 = flavour、强耦合相变、U 大）为这些模型提供实验约束并受其启发（L548–552, L543）。
- **超导相空间论据**：引言引 quadri-/pentalayer 超导（Park 2022 Nat. Mater. [ref 14]、Zhang 2022 Science [ref 15]、Burg 2022 [ref 16]）论证"色散带普遍存在 → 轻/重相互作用普遍重要"（L38–48）——即本项目假说中"flat+Dirac → 高可调性"的跨体系背景，本文是 msTTG 上该图景的局域压缩率表达。

---

## 8. 对后续研究的影响

- **方法输出**：扫描 SET 的"真绝缘体 vs 低 DOS 屏蔽"判别协议（局域化充电峰随 B/V_t-s 的响应）可推广到其他扭转多层（quadri-/pentalayer）与其他填充——给"某态是不是真绝缘体"一个模型无关的判据。
- **定量约束**：n_D(ν) 曲线、0.5 T 能隙化阈值、v_F、C_f 序列、CNP 相变的 g 因子组成为任何 MATTG/msTTG 关联态理论（含超导机制候选）提供对标清单。
- **概念输出**："Dirac 扇区 = 与自旋/谷并列的新 flavour"为多味道 Hubbard/重费米子模型提供实验锚；CNP 相变序列作为"局域 g 因子/电子环境探针"开启空间分辨味道物理。
- **遗留问题接力**：过量轻电子 fate、Dirac 电子是否稳定超导、g 因子空间变化的微观起源——直接可立项。
- **对本项目**：见目的接口。

---

## 9. 理论模型映射（供计算对标）

- **D → Δ**：本文器件 D ≈ 0（单栅、无顶栅）；对"位移场可调性"（假说核心）本文不提供 D 轴数据——理论对标应把本文 ν 依赖的 n_D(ν)（D=0 切片）作为基准，再用双栅实验（E2/E14）补 D 轴。
- **θ → λ → A（连续模型参数）**：θ ≈ 1.53°（位置1）/1.58°（位置2）；局域 θ 变化 ~1.54–1.58° [读图]；可与 moiré 连续模型（Khalaf 参数）对照。
- **可对标观测量**：dµ/dn(ν, B) 全场图（图1b）、C_f 序列（平带扇区，应复现 MATBG 序列）、v_F = (1.014±0.002)×10⁶ m s⁻¹、ν_d(ν)/n_D(ν)（E_F 处 Dirac 布居）、0.5 T 能隙化阈值、CNP 相变序列与 n_D 阶跃、Hofstadter 谱（橙色 |N|>0 Dirac 支）。
- **模型输入供微观计算校验**：12-LL 截断（平带 4 = 自旋×谷；Dirac 8 = 自旋×谷×层）；W_flat/W_dirac = 5、E_offset/W_dirac = 2、U/W_dirac = 20；g 因子组（点1/点2）；负压缩率区 = isospin 重排信号（对标相互作用模型）；Dirac 扇区"flavour"假设的检验：若成立，平均场级 isospin 相变数目应随可调味道数变化。
- **"轻/重"量化口径**：本文不用 m\*，用 v_F（轻）与 LL 宽比 W_flat/W_dirac=5（重/轻动力学尺度比）+ 平带大 g 因子（|g|~8 vs Dirac |g|~2.7）——理论对标时避免把未出现的 m\* 数值当原文（无源数字禁令）。

---

## 目的接口（服务项目 Phase S 三问，不进入正文）

- **Q1（实验证据：轻/重电子"高可调性"的表达）**：本文是该假说"轻/重二流体共存"的最直接局域压缩率证据——ν 与 B 是两个有效旋钮：B 超过 ~0.5 T 把轻扇区能隙化（重扇区仍弱受扰），回到零场则轻电子重新进入 E_F 并决定态的性质（部分能隙而非绝缘体）；ν 扫描显示 Dirac 布居 n_D(ν) 非单调、在 |ν|=2,3 最大；CNP 高场相变由轻/重 N=0 LL 强耦合驱动且可被平均场 U 复现 → 系统确实存在可由外参量（n、B）在"轻主导/重主导/轻-重纠缠"之间切换的宽相空间。⚠️ 注意 D 不可调是本文缺口，需双栅器件补。
- **Q3（对"flat+Dirac 高可调性 → 超导"假说的证据贡献）**：贡献 = 相关性 + 机制线索，**非因果证明**：超导（ν=±2，ED Fig.1b）落在 n_D 最大的填充窗（|ν|=2,3）内（📜Q 相关性陈述）；Dirac 电子阻止 B=0 真绝缘体（维持金属性残存 DOS）与 CNP 处提供额外 flavour/相变自由度，与"含色散带的体系超导相空间更宽"叙事一致（引言 refs 14–16）；但作者明言轻电子是否稳定超导为开放问题，本文亦未测超导区内的轻电子行为 → 假说的"高可调性→超导"环节仍缺直接实验闭环。
- **增量价值**：本项目 E-系列中首份"扫描 SET 局域压缩率 + 电荷传感判别"视角笔记；提供可直接 grep 对标的 ν_d/n_D、0.5 T 阈值、v_F(±0.002)、U/W、g 因子与 CNP 相变清单（§4.2），供 registry 汇总与后续双栅/D 轴实验（E2/E14 类）对接。

---

## 反向核对 pass (2026-09-03)

- 方法与结果：对 /tmp/msTTG_txt/E13_pierce2025.txt（884 行，正文 + Methods + ED Fig. caption，参考文献至 L615 后）逐项 grep 核对 §2/§4 全部数字与专名。
- ✅ 通过：θ 1.53°/1.58°（L65,144,193,199,629,631,800,814）、±0.02°（L681）、0.5 T（L178,295,310）、v_F=1.014±0.002×10⁶（L672）、0.7 T/6.8 T/5 T/−0.15 V/0.15 V（L744–750）、U≈20W（L542）、W_dirac=1 meV、W_flat/W_dirac=5、E_offset/W_dirac=2、U/W_dirac=20（L725–726）、g 因子两组（L726–727, 730）、12 LLs=4+8（L707–709）、ν_LL=±6（L465）、ν_LL=−5…0 负压缩率（L485–488）、9 μm/nearly 10 μm（L511/33）、B=11 T（L493）、8.44 T（L370,402）、δn~5.7×10⁸ cm⁻²（L840）、V_t-s 三值（L838–840）、100 nm/20 mK（L652–653,641）、a≈0.246 nm（L678）、Streda（L167–168）、C=C_d+C_f（L175）、ν=1,±2,3（L293）、±2 超导（L183）、"several milli-electronvolts"（L159）、"1–2 orders of magnitude"（L697–699）、12 处引用文献编号与 §7 对应（L562–611）——全部 grep 命中。
- ✅ 全文无 ± 声明：除 v_F 的 (1.014±0.002)（[±]）与 θ 拟合精度 ±0.02°（[±]）外，正文/Methods 无其他显式误差棒；n_D 误差棒定义 = 线性拟合残差标准差（图2e caption）已注明。
- ⚠️ 降级/修正记录：①摘要 "nearly 10 μm" vs 正文 "9 μm" 并存，按各自出处引用（未合并）；②图1b 色标单位 txt 显示 "mV cm⁻²"（L65），图2/图3 显示 "meV cm⁻²"（L190 等）——内部不一致，pdftotext 或原图问题未决，色标值一律标 📊F[读图] 且仅作相对标度；③正文 "four pronounced regions of giant negative compressibility interrupt the incompressible peaks at ν_LL = −5, −4, −3, −2, −1 and 0"（L485–488）——"four regions" 与所列 6 个填充的对应关系原文未展开，照录并加 ⚠️；④正文 L179 "single-gated hexagonal boron nitride (hBN)-encapsulated MATTG device" vs Methods L635/L653 两处笔误写作 "MATBG"——器件本体即本文 MATTG，已在 §3.1 按语境校正并注明；⑤v_F 在正文（L301）写作 "approximately 10⁶ m s⁻¹"（txt 中 "106" 为 10⁶ 的排版脱落），Methods 给精确值——以 Methods 精确值为准并保留正文 ~ 表述。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-09-03 | 期刊信息更正：registry 记 "Nature 2024" → 实为 **Nature Physics 21, 1237–1242 (2025)**；received 18 Dec 2023、accepted 28 May 2025、online 26 June 2025、DOI 10.1038/s41567-025-02956-z（txt L9–16, L61）。 |
| 2026-09-03 | arXiv 2401.12284 为外部来源（registry 提供），正文未出现该号 → 元数据表标注 ⚠️。 |
| 2026-09-03 | 反向核对 pass：§2/§4 全部数字 grep 命中（见上）；确认全文无 ±（除 v_F 与 θ 精度）并显式声明。 |
| 2026-09-03 | 图1b 色标单位 "mV cm⁻²" 与图2/3 "meV cm⁻²" 不一致（txt 所见）→ 色标仅作 [读图] 相对标度，待人工对照原 PDF。 |
| 2026-09-03 | Methods 两处 "MATBG" 系 MATTG 笔误（L635, L653 上下文），按语境校正引用，未改原文。 |
| 2026-09-03 | "nearly 10 μm"（摘要 L33）与 "9 μm"（正文 L511）按各自出处并存引用。 |
