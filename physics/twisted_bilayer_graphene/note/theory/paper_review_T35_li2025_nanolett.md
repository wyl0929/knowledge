<!--
 * @Author       : AI 精读 (系统辨识式阅读法 → 三层分离整理)
 * @Date         : 2026-08-11（初读）→ 2026-09-02（4 块新架构重读）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T35_li2025_nanolett.md
 * @Description  : T35: Li, Chen & Yao 2025 — 大转角 intervalley Umklapp 散射拓扑畴壁态（理论；2026-09-02 按 4 块新架构重读）
-->

# Paper Review: Li, Chen & Yao (2025) — 大转角 Umklapp 散射拓扑畴壁态

| 字段 | 内容 |
|------|------|
| **编号** | T35 |
| **标题** | Topological Domain-Wall States from Umklapp Scattering in Twisted Bilayer Graphene |
| **作者** | Juncheng Li, Cong Chen*, Wang Yao* |
| **期刊** | Nano Lett. 2025, 25, 17025−17031 |
| **DOI** | 10.1021/acs.nanolett.5c04006 |
| **arXiv** | 2508.03761（⚠️ 外部来源，正文未出现） |
| **类型** | 理论 — 大转角 intervalley Umklapp 散射畴壁态 |
| **课题组** | Wang Yao / Cong Chen group (University of Hong Kong) |
| **PDF / SI PDF** | ✅ `reference/pdfs/Li 等 - 2025 - Topological Domain-Wall States from Umklapp Scattering in Twisted Bilayer Graphene.pdf`（正文 + SI） |
| **精读日期** | 2026-08-11（初读）→ 2026-09-02（4 块新架构重读） |

> **共享知识引用**：valley Chern / Berry 相位 / chiral vs helical 见 `[PHY-BERRY]`；阅读疑问见 `note/shared/method/mechanism_questions.md` `[METHOD-Q]`。⚠️ 本文畴壁态机制（Jackiw–Rebbi 型 λ 符号反转）与 `[PHY-BERRY]` 的 AB/BA valley Chern 数差畴壁机制是**两类**，§2.3/§7 显式对照。

---

## TL;DR

**本文想解决的问题**：大转角 TBG（θ ≈ ±21.8°）的低能物理是否由 **intervalley Umklapp 散射**主导，并能否在「手性反转界面」上产生拓扑畴壁态——即一种独立于小转角 mTBG「AB/BA 畴壁」范式的新机制？

**主结果**（全文无实验数据，均为理论预言 + 数值自洽；作者措辞强度见 📜Q）：
① 大转角下同谷 Dirac 点远分离（抑制 intravalley 散射）、反谷 Kt/K′b 在 mBZ 角重叠 → **intervalley Umklapp 散射主导低能**；其隧穿能标 ~2 meV「不足以」显著重整化能带 → 能带高度色散、e–e 相互作用可忽略 📜Q。
② 手性耦合 λ 印迹堆垛手性：D6 构型 gapped + hidden BHZ 拓扑，D3 构型 semimetallic + quadratic band crossing 📜Q。
③ 手性反转（ζ=+ ↔ ζ=−）界面 → **Jackiw–Rebbi 型拓扑畴壁态** = 反向传播赝自旋模（两条零能模），即使两侧 bulk 能带与拓扑不变量**相同** 📜Q。
④ 对称破缺微扰（Δs=15 meV）+ 7% 单轴应变 + 3.2–3.5 Å 层间距 + 22.79° 小偏角 + hBN 衬底下态稳健存活 📜Q。

**结论/意义**：作者表态「our work unveils a novel approach to achieving robust topological channels」「open new pathways for engineering domain-wall states in twisted materials」——大转角 + 结构手性 = 畴壁态工程的新参数空间（理论预言，非实验证实）📜Q。

---

## 1. 系统辨识导览（判别表为全文唯一权威，机制细节见 [PHY-BERRY]）

**黑箱三要素**：`{输入旋钮: θ、结构手性 ζ、堆垛对称性 D6/D3/D3′、对称破缺微扰/无序 | 输出观测量: 畴壁能谱（in-gap band-crossing 模）、bulk 能带、能带几何量 ωn(k) | 声称结论: intervalley Umklapp 主导大转角低能拓扑 + 手性反转 → Jackiw–Rebbi 拓扑畴壁态}`

**四层变量图**（符号层一次钉死；理论版）：

| 层 | 本文实例 |
|----|----------|
| **L1 旋钮 u** | θ（±21.8°、13.8°、22.79°、4° 对照）、结构手性 ζ=±、堆垛（D6/D3/D3′）、层间位移 d、对称破缺微扰 Δs、层间距（3.2–3.5 Å）、7% 单轴应变、hBN 衬底 |
| **L2 导出量 x₁** | moiré 超胞（28 atoms）、moiré 周期 Li/7（7 倍收缩）、mBZ 角 Km/K′m、Dirac 锥动量分离（C2/C4 同心圆） |
| **L3 模型量 x₂** | k·p 哈密顿 H_D6/H_D3、层间耦合 T = M（非手性）+ λ（手性）、bulk 能隙、hidden BHZ 拓扑、ζ 投影赝自旋织构、in-gap 零能模、能带几何量 ωn(k) |
| **固定参数（拟合，非旋钮）** | D6：ℏvF=6.61 eV·Å、M=4.70 meV、λ=1.31 meV；D3：ℏvF=6.43 eV·Å、ℏ²v²/2m=10.40 eV·Å²、ℏv⊥=7.32 meV·Å、M=5.40 meV（由 a-SKTB 低能带拟合）📜Q |
| **反推量 θ̂** | 无实验反推——纯理论论文；M/λ/vF 由 SKTB 低能带拟合（非谱学/输运反推）📜Q |
| **L4 观测量 y** | 畴壁能谱（Fig 4b,c / Fig 5a–f）、bulk 能带（Fig 3a,b,d,e）、ωn(k) 色标；实验可检验信号原文仅定性给「chiral transport」📜Q |

> 与实验论文（E12）符号差异：本文**没有** L1 实验旋钮（无 Vtg/B/T 扫描），θ/ζ/堆垛是模型可调参数而非器件旋钮；L4 观测量 = 计算谱而非测量量。全文无实验数据、无误差棒。

**可辨识性判别表**（理论版：每条判别 = 判据 / 排除谁[竞争图景] / 确立谁）：

| 判别 | 判据（理论论证/数值） | 排除谁（竞争图景） | 确立谁 |
|------|-------------|--------|--------|
| **小转角 vs 大转角主导散射** | 大转角同谷 Dirac 点远分离（抑制 intravalley），反谷 Kt/K′b 在 C2/C4 圆重叠并折叠到 mBZ 角 → intervalley Umklapp 主导；隧穿能标 ~2 meV 不足以重整化 → 色散带、e–e 可忽略 | 小转角范式（intravalley 散射 + 平带 + 多体关联） | 大转角 intervalley Umklapp 主导低能物理 📜Q |
| **能隙 vs 无能隙（D6 vs D3）** | C2z 对称性保留（D6, space group No. 177）vs 破缺（D3, No. 150）→ D6 gapped+hidden BHZ，D3 semimetallic+quadratic crossing | 无 C2z 区分时 D6/D3 低能谱简并 | 手性耦合 λ 为 P 破缺标志、印迹堆垛手性 📜Q |
| **畴壁态来源：Chern 数差 vs Jackiw–Rebbi** | 界面两侧 bulk 能带与拓扑不变量**相同**，态源于 λ 符号反转（mass inversion） | mTBG 型 valley Chern 数差畴壁（[PHY-BERRY] 的 AB/BA 机制） | Jackiw–Rebbi（λ 符号反转）→ 反向传播赝自旋模 📜Q |
| **拓扑 vs 平凡** | 单式变换把 H_D6 映射到 BHZ 模型；M 对应有效 exchange field（破 TRS 但不毁拓扑） | 平凡（非拓扑）界面态 | hidden BHZ 拓扑 📜Q |
| **稳健 vs 脆弱** | 对称破缺微扰（Δs=15 meV）+ 7% 应变 + 3.2–3.5 Å + 22.79° + hBN 下 in-gap 模存活 | 仅在高对称点成立的偶然态 | 拓扑保护（bulk gap 不闭合则态存活）📜Q |

> **主结果 ↔ 判别表映射**（每条主结果由哪几条判别确立）：
> - 主结果① intervalley Umklapp 主导 ← {小转角 vs 大转角主导散射}
> - 主结果② D6 gapped / D3 semimetallic（手性印迹） ← {能隙 vs 无能隙}
> - 主结果③ 手性反转畴壁态（反向传播赝自旋模） ← {畴壁态来源判别, 拓扑 vs 平凡}
> - 主结果④ 稳健性 ← {稳健 vs 脆弱}
>
> **分层排除注**：本文不是「存在性→相干→拓扑」的实验逐层证成，而是**理论建构 + 数值互验**：①「小转角 vs 大转角」确立机制图景（Umklapp 而非 intravalley）；②「D6 vs D3」确立 λ 的拓扑作用；③「Chern 数差 vs Jackiw–Rebbi」确立畴壁态**不依赖** valley Chern 数差（两侧拓扑相同，态来自 λ 反转）；④「拓扑 vs 平凡」经 BHZ 映射确立拓扑本质。作者用词 "predict"、"demonstrate"、"unveil"，畴壁态是**预言**（数值 a-SKTB 自洽确认，无实验）📜Q。

> **[前提与限定]**（判别结论的适用范围）：
> - **近似/扰动**：k·p 模型截断到低能（高阶项远离 K/K′ 才显著，对低能可忽略；但作者明言对光学响应等可能关键，留待未来）📜Q；单粒子图景（e–e 只定量重整化参数、不诱发 band inversion/gap closure）📜Q；理想周期 moiré。
> - **判别性扫轴**：旋钮 = θ（±21.8°/13.8°/22.79°/4° 对照）、ζ=±（手性反转）、堆垛（D6/D3/D3′）、微扰强度 Δs（15 meV）/应变（7%）/层间距（3.2–3.5 Å）/衬底（hBN）——均为计算扫参，非实验扫场。
> - **候选模型集 M 边界**：{小转角 intravalley 范式, D6 拓扑 vs D3 半金属, Chern 数差畴壁 vs Jackiw–Rebbi, 拓扑 vs 平凡} —— 本文机制在该集内确立；**集外候选未排除须声明**：实验可观测信号（STM/输运定量预言）原文未展开（grep "STM"=0），真实大转角样品的无序/畴壁可制备性/手性反转界面如何实验实现均未讨论。

三层标注：📜Q = 原文事实（附位置）｜推导 = 由原文公式合成｜📊F = 读图估算｜💭I = 推断。**不确定度（正交轴）**：[±] 原文误差棒 / [~] 原文无误差棒 / [读图] 图·色标提取 / [相对] 仅相对量。⚠️ 本文为理论论文，**全文无 ±、无实验误差棒**；所有数字为模型参数（拟合/设定），= / ≈ 给出，标 [~]。所有数字经 pdftotext + grep 反向核对。

---

## 2. 结果与机制（按论文论证结构：结构 → Umklapp → 能带拓扑 → 畴壁态 → 稳健性）

### 2.1 大转角下的 intervalley Umklapp 散射（机制核心）

- **commensurate 结构**：θ 满足 cos θ = (3m²+3mn+n²/2)/(3m²+3mn+n²)（eq 1），(m,n)=(1,1) 给出最小 commensurate 转角 θ ≈ ±21.8°；moiré 超胞 28 atoms、原胞矢量相对单层石墨烯拉长 7 倍、实空间 moiré 周期 Li/7（7 倍收缩）📜Q（正文 + Fig 1d caption）。
- **三种高对称构型**：D6（绕六角中心转）/ D3（tA–bB）/ D3′（tB–bA）；位移 d = ±(L1+L2)/21 使 D6 ↔ D3/D3′ 互转 📜Q（Fig 1d）。⚠️ **与小转角的区别**：小转角弛豫倾向于 AB/BA 畴，而 21.8° 下 D6 vs D3 能量差可忽略 → **抑制晶格重构** 📜Q（引言段）——这正是「动量空间折叠 vs 实空间重构」对立的原文依据。
- **Umklapp 条件**（eq 2）：k1 + Gt = k2 + Gb → G = k1 − k2 = Gb − Gt = **Gm**（moiré 倒格矢参与散射）📜Q。
- **两段式论证**：小转角 → 同谷 Dirac 锥接近，**intravalley** 主导（连续模型基础 + 平带 + 多体）📜Q；大转角 → 同谷 Dirac 点远分离（抑制 intravalley），反谷 Kt/K′b 在外同心圆接近——13.8° 在 C4 圆重叠、21.8° 在 C2 圆重叠（更接近原点）→ **intervalley Umklapp 主导低能** 📜Q（Fig 2b）。
- **能标自洽**：intervalley Umklapp 隧穿能标 **~2 meV**，「不足以」诱导显著能带重整化 → θ=21.8° 能带高度色散（Fig S1）→ e–e 相互作用可忽略 📜Q。
- **隙与拓扑**：Kt 与 K′b 折叠到 mBZ 角 Km 后简并 → intervalley Umklapp 在 Dirac 点打开 hybridization gap + 引入非平凡拓扑 📜Q（Fig 2b caption + 正文）。

### 2.2 D6 vs D3：手性耦合 λ 与能带拓扑

- **对称性定构型**：D6（space group No. 177）保留 C3z + C2z + C2x；D3（No. 150）破 C2z（其余面内转动全破）📜Q。
- **层间耦合分区**：T 分解为 **P 保持（M，非手性）+ P 破缺（λ，手性）** 两项；λ 是反演破缺的标志，解除镜像对称简并、把系统劈成左手（ζ=+）/右手（ζ=−）📜Q。
- **D6**：gapped 谱 + **hidden BHZ-like 拓扑** 📜Q；**D3**：semimetallic + **quadratic band crossing**（q² 项不可或缺，决定能带几何量与三角翘曲）📜Q。
- **模型参数**（Fig 3 caption）：D6 → ℏvF=6.61 eV·Å、M=4.70 meV、λ=1.31 meV；D3 → ℏvF=6.43 eV·Å、ℏ²v²/2m=10.40 eV·Å²、ℏv⊥=7.32 meV·Å、M=5.40 meV 📜Q[~]。
- **λ 的角色**：去掉 λ → 退化为 AA 堆垛双层石墨烯；保留 λ → 引入二值 ζ=± 📜Q。k·p 模型复现 a-SKTB 的能带色散 **与** 能带几何量 ωn(k)（ζ 敏感）📜Q（Fig 3a,b）。

### 2.3 手性反转 → Jackiw–Rebbi 拓扑畴壁态（核心预言）

- **问题设定**：ζ=+ 与 ζ=− 两侧 bulk 能带色散与二阶拓扑**相同**，但它们界面上的拓扑畴壁模是开放问题 📜Q。
- **畴壁模型**（eq 9–11）：平坦边界 x=0，左手 tBG（ζ=+）占 x<0、右手（ζ=−）占 x>0；qy 为边界好量子数、qx→−iℏ∂x；qy=0 处解出**两条指数局域零能模** ψ1,2，投影得 1D 边缘模型 H_edge = ℏvF qy σy 📜Q（eq 10–11）。
- **关键判别**：态存在于 bulk 能带与拓扑不变量**相同**的界面——band-crossing 来自内禀 bulk 参数 **λ 的符号反转** = Jackiw–Rebbi mass inversion 📜Q。⚠️ 这排除了「畴壁态由两侧 valley Chern 数差产生」的 mTBG 机制（[PHY-BERRY] 的 AB/BA 图景）——**本文畴壁两侧拓扑相同**。
- **M=0 极限与 BHZ 映射**：M=0 时 ψ1,2 是 ℏvFqyτ0σy 的本征态（本征值 ±ℏvF）= 手性模沿 y 反向传播；有限 M 混合赝自旋通道但不毁拓扑（类比 BHZ 的面内 Zeeman field）📜Q。单式变换 U†H_D6U = ℏvFτ0·q + (λ/2)τzσz（eq 12）把模型映射到 BHZ（QSH，反向自旋流）；M 对应有效 exchange field，破 TRS 但不毁拓扑 📜Q。
- **数值确认**：构造 tBG 带（左=右旋 / 右=左旋，沿畴壁周期边界），a-SKTB 谱确认 in-gap band-crossing 模（Fig 4b,c 红线）📜Q。
- **术语辨析**：摘要称 "counterpropagating pseudospin modes"；机制是 K/K′ 谷锁定反向（helical，QVH 畴壁态），非总电荷手征的 QH 边缘通道——见 [PHY-BERRY] 💭I。

### 2.4 稳健性（对称破缺 + 现实无序）

- **三种 on-site 微扰**（Fig 5a–c，Δs=15 meV）：C2z 破缺 Hs(1)=Δsτzσz、C2z+C2x 破缺 Hs(2)=Δsτ0σz、C2x 破缺 Hs(3)=Δsτzσ0 → in-gap 模均存活；SKTB 佐证（Fig S2）📜Q。
- **现实无序**：层间距 3.2–3.5 Å（out-of-plane 应变，Fig S5）✅；7% 面内单轴应变（破 C3z，Fig 5d）✅；小偏角 22.79°（Fig S6，intervalley Umklapp 仍主导）✅；hBN 衬底（Fig S7）✅；e–e 关联仅定量重整化（Fig S1）✅ 📜Q。
- **generic tBG 推广**：任意层间位移下 H = H_D6 + Δ，只要 Δ 不闭合 bulk gap 则畴壁态存活；θ=21.8° 随机位移下 band-crossing 存活（Fig 5e,f）📜Q。
- **⚠️ 末尾注**：ζ 反转畴壁态在 gapless 区**消失**，但 **valley-Chern 主导**的拓扑通道出现（D3/D3′ 界面，见 SI）📜Q。

---

## 3. 理论模型与方法

### 3.1 模型
对称约束 k·p 有效模型：D6 四带低能模型（eq 3–4，层间耦合 T 含 M+λ）；D3 到 q² 阶（eq 5–6，含 p 波手性耦合 + f(q) 三角翘曲项）；D3′ 经 C2z 与 D3 联系（eq 7）📜Q。

### 3.2 畴壁推导（非常规步骤一行）
沿边界做 qx→−iℏ∂x 替换 → 解 qy=0 零能模 → 投影到 H_edge（eq 9–11）；BHZ 映射用单式变换 U（eq 12）📜Q。手性耦合 λ 从 P 破缺项分离出二值 ζ=± 是本文记号核心（chiral vs helical 辨析见 [PHY-BERRY]）📜Q。

### 3.3 计算
a-SKTB（Slater–Koster 紧束缚）验证 k·p；第一性原理方法、有效简化紧束缚模型见 SI 📜Q。参数由低能带拟合（M/λ/vF），无实验输入 📜Q。

---

## 4. 关键预言与数据（提取链 + 验证链 + 不确定度标注）

| 参数 | 值 | 来源等级 / 不确定度 |
|------|-----|---------------------|
| 主算例转角 θ | ±21.8°（commensurate，(m,n)=(1,1)） | 📜Q[~]（全文 18 处 "21.8"） |
| 对照转角 | 13.8°（C4 圆）；22.79°（稳健性）；4°（小转角对照） | 📜Q[~] |
| moiré 超胞 | 28 atoms；原胞矢量拉长 7×；周期 Li/7 | 📜Q[~] |
| Umklapp 隧穿能标 | ~2 meV「insufficient」（不足以重整化能带） | 📜Q[~]（正文段） |
| D6 模型参数 | ℏvF=6.61 eV·Å、M=4.70 meV、λ=1.31 meV | 📜Q[~]（Fig 3 caption） |
| D3 模型参数 | ℏvF=6.43 eV·Å、ℏ²v²/2m=10.40 eV·Å²、ℏv⊥=7.32 meV·Å、M=5.40 meV | 📜Q[~]（Fig 3 caption） |
| 对称破缺微扰强度 | Δs=15 meV | 📜Q[~]（Fig 5 caption） |
| 稳健性参数 | 层间距 3.2–3.5 Å；7% 单轴应变；22.79°；hBN | 📜Q[~]（Fig S5–S7、5d） |
| 畴壁零能模数 | 两条（ψ1,2，反向传播） | 📜Q[~]（eq 10） |

**验证链（三重互验）**：① k·p 模型 ↔ a-SKTB（能带色散 + ωn(k) 几何量均复现）📜Q；② 解析零能模 ↔ 数值 in-gap band-crossing 模（Fig 4b,c 红线）📜Q；③ BHZ 单式映射 ↔ hidden BHZ 拓扑 📜Q。

**⚠️ 无源数字修正（本次重读新增）**：
- 旧版「STM 和输运的预期信号与 mTBG 定性不同（空间/能量尺度）」：**"STM" 无源**（grep "STM"=0、"spectroscopy"=0、"LDOS"=0）→ 降级为原文仅有的定性措辞「chiral transport engineering / chiral transport phenomena」（引言段）📜Q[相对]；正文**无**任何 STM/输运定量预言。
- 旧版「畴壁态数目由 moiré 子带 Chern 数决定」：**无源且与原文矛盾**（grep "number of"=0；原文明言界面两侧「identical bulk bands and topological invariants」、态来自 λ 符号反转）→ 改为「两条反向传播赝自旋模 + Jackiw–Rebbi 机制」📜Q。valley-Chern 通道仅在 gapless 区作为对照出现（D3/D3′ 界面，一句话）📜Q。

---

## 5. 主要结论
1. 大转角 tBG 低能由 **intervalley Umklapp 散射**主导（隧穿 ~2 meV、色散带、e–e 可忽略）📜Q。
2. 手性耦合 λ 印迹堆垛手性：D6 gapped + hidden BHZ、D3 semimetallic + quadratic crossing 📜Q。
3. 手性反转界面 → **Jackiw–Rebbi 拓扑畴壁态**（反向传播赝自旋模），即使两侧拓扑不变量相同 📜Q。
4. 稳健性：Δs=15 meV / 7% 应变 / 3.2–3.5 Å / 22.79° / hBN 下存活；generic tBG 需 Δ 不闭合 bulk gap 📜Q。
5. 作者定性表态（预言非证实）：「unveil a novel approach to achieving robust topological channels」「open new pathways for engineering domain-wall states」📜Q。

## 6. 局限与未解决
| 局限 | 说明 | 证据 |
|------|------|------|
| 实验验证空白 | 全部为理论预言 + 数值自洽，无 STM/输运实验 | 📜Q（无实验） |
| 无定量实验信号预言 | 只给「chiral transport」定性，无 STM/电导/LDOS 定量预言 | 📜Q（grep "STM"=0） |
| k·p 低能截断 | 高阶项对低能可忽略，但作者明言对光学响应等可能关键 | 📜Q |
| 理想周期 moiré | 只抽查了若干典型无序（应变/层间距/偏角/hBN），未穷尽真实样品无序 | 📜Q→💭I |
| 手性反转界面可制备性 | θ=+21.8° ↔ −21.8° 界面如何实验实现未讨论 | 💭I |
| gapless 区 valley-Chern 通道 | 仅一句话提及，D3/D3′ 界面机制见 SI，正文未展开 | 📜Q |

## 7. 与其他工作的关系（跨论文对标放这里，不放正文）
| 工作 | 关系 |
|------|------|
| 小转角 mTBG（BM 连续模型，refs 15/36/37） | 对照：intravalley 散射 + 平带 + 多体；本文 intervalley Umklapp + 色散 + 单粒子 📜Q |
| AB/BA 畴壁（valley Chern，[PHY-BERRY]） | **对照（本文核心卖点）**：mTBG 畴壁 = 两侧 Cv 相反 → gap 反号；本文畴壁 = 两侧拓扑相同、态来自 λ 符号反转（Jackiw–Rebbi）📜Q |
| Park 2019 (ref 20) / Liu 2021 (ref 21) | 2D 二阶拓扑绝缘体（本文 D6 "hidden BHZ" 与 ζ 二阶拓扑的谱系关联）📜Q |
| Qian 2023 (ref 22) / Chen & Yao 2025 (ref 23) | 3D chiral 拓扑半金属 / 交替扭转多层——Umklapp 机制谱系 📜Q |
| 21.8° 合成（refs 30–32） | 结构稳定性已实验证实（引用，非本文实验）📜Q |
| Mele 2010 (ref 38) / Moon 2013 (ref 39) | 21.8° 四带低能谱与未扭转双层相似 📜Q |

> ⚠️ Phase S 外部对标（非本文引用）：cards.md 的「突破小转角范式 / 开辟大转角新参数空间」属项目层定性评价 💭I，非本文原话。

## 8. 对后续研究的影响
- 开辟「大转角 + 结构手性」畴壁工程新路径（作者措辞 "novel approach"、"new pathways"）📜Q。
- 供计算对标：大转角 σxy / 畴壁 in-gap 模 / 手性反转界面透射（见 §9）💭I。
- 遗留任务：高阶项对光学响应的作用、gapless 区 valley-Chern 通道、实验信号定量化 💭I→📜Q（部分作者明言）。

## 9. 理论模型映射（供 TBPM / Kubo-Bastin 对照）
| 映射 | 说明 |
|------|------|
| θ → moiré 超胞 | 21.8° → 28 atoms、原胞矢量 7×、周期 Li/7 📜Q |
| 手性 ζ → 结构 chirality | ζ=± ↔ 左右手 ↔ λ 符号 📜Q |
| H_D6 (eq 4) → TBPM 哈密顿 | ℏvF=6.61 eV·Å、M=4.70 meV、λ=1.31 meV 📜Q |
| 畴壁 ↔ 界面构型 | θ=+21.8°(ζ=+) ↔ −21.8°(ζ=−) ribbon（Fig 4a）📜Q |
| 拓扑 ↔ σxy / 边缘态 | hidden BHZ ↔ QSH 类比（helical 反向通道，非净电荷 Chern）→ TBPM 可算畴壁 in-gap 模与 σxy 💭I |
| 能标 ↔ 数值网格 | 隧穿 ~2 meV、Δs=15 meV → 需 < meV 能级分辨率 💭I |

---

## Phase S 目的接口（引用式）

- **Q1（edge state 如何表征）**：本文是理论，无实验表征；预言 = 畴壁能谱 in-gap band-crossing 模（Fig 4b,c / 5）+ 反向传播赝自旋模 📜Q（§2.3）。
- **Q2（理论如何解释）**：大转角 intervalley Umklapp → mBZ 角开隙 → 手性 λ 印迹拓扑；畴壁态 = Jackiw–Rebbi（λ 反转），**非** valley Chern 数差 📜Q（§2.1–2.3）。
- **Q3（理论↔实验对应）**：尚无实验；潜在信号仅定性「chiral transport」📜Q；作者**未**给 STM/电导定量预言（grep "STM"=0）📜Q。

> **增量价值**：提供与 mTBG（E12）对照的**第二种畴壁机制**——动量空间 Umklapp + Jackiw–Rebbi（λ 反转）vs 实空间 AB/BA valley Chern；供大转角 TBPM 对标（§9）；并纠正旧版两处无源数字（"STM 信号"、"Chern 数决定态数目"）。

## 反向核对 pass (2026-09-02)

pdftotext 提取正文（/tmp/T35.txt，507 行），逐项 grep 核对：θ=21.8°(18) / 13.8°(1) / 22.79°(1) / ~2 meV(2) / Δs=15 meV(1) / M=4.70 meV & λ=1.31 meV & 6.61 eV·Å（Fig 3 caption）/ 6.43 eV·Å & 10.40 eV·Å² & 7.32 meV·Å & 5.40 meV（Fig 3 caption）/ 28 atoms / 7-fold / 3.2–3.5 Å / 7% / hBN / Jackiw–Rebbi / BHZ / Bernevig / valley-Chern / counterpropagating / two zero-energy modes / space group 177 & 150 / C2 & C4 circle / (m,n)=(1,1) / d=±(L1+L2)/21 —— **全部命中**。

⚠️ 无源降级/删除（本次重读新增）：
- "STM"(0) / "spectroscopy"(0) / "LDOS"(0) → 旧版「STM 预期信号」删除，降级为定性「chiral transport」📜Q[相对]。
- "number of"(0) + 原文「identical bulk bands and topological invariants」→ 旧版「畴壁态数目由 moiré 子带 Chern 数决定」删除，改为「两条反向传播模 + Jackiw–Rebbi」。
- "10 meV"(0) / "50 meV"(0) / "~6°~10°~13°"(0) / "1.1° 魔角比较"（grep "magic" 仅命中参考文献）→ 沿用旧更正日志，已删。
- arXiv 2508.03761 正文未出现 → 标外部来源。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-20 | **删除转角列表**："(~5-15°)"、"(~6°, ~10°, ~13°)" 无源 → 改为原文算例 commensurate 转角 θ=21.8°（grep "21.8"=18）、13.8° 一处、22.79° 稳健性检查。依据 §B.5#4 |
| 2026-08-20 | **删除 "Umklapp 能隙 10-50 meV"**：无源（grep "10 meV"=0、"50 meV"=0）→ 改原文 "energy scale of ∼2 meV … insufficient"（grep "2 meV" ✓）与模型参数 Δs=15 meV（grep "15 meV"=1）。依据 §B.5#5 |
| 2026-08-20 | **删除 "与超导魔角 (1.1°) 比较"**：原文无此比较（grep "magic" 仅命中参考文献）。依据 QC 跨论文迁移规则 |
| 2026-09-02 | **4 块新架构整体重写**（对齐 E12，理论适配）：新增 TL;DR 问题句式、四层变量表（理论版）、可辨识性判别表（5 条）+ 主结果↔判别表映射 + [前提与限定] 块、§2 按论文论证结构（结构→Umklapp→能带拓扑→畴壁态→稳健性）、§3 理论模型与方法（模型/推导/计算）、§4 关键预言与数据（提取链+验证链+不确定度标注）、§5–9（结论/局限/关系/影响/模型映射）、Phase S 三问接口 + 增量价值、反向核对 pass |
| 2026-09-02 | **删除无源 "STM 预期信号"**：旧版「STM 和输运的预期信号与 mTBG 定性不同」中 STM 无源（grep "STM"=0、"spectroscopy"=0、"LDOS"=0）→ 降级为原文定性措辞「chiral transport engineering/phenomena」📜Q[相对]，并显式声明正文无 STM/输运定量预言 |
| 2026-09-02 | **删除无源且矛盾 "畴壁态数目由 Chern 数决定"**：grep "number of"=0，且原文明言界面两侧「identical bulk bands and topological invariants」、态来自 λ 符号反转（Jackiw–Rebbi）→ 改为「两条反向传播赝自旋模 + Jackiw–Rebbi 机制」；valley-Chern 通道仅作为 gapless 区对照出现 |
| 2026-09-02 | **证据分级与不确定度补全**：全文数字补 📜Q[~]（理论参数，无 ±）；arXiv 2508.03761 标外部来源（正文未出现）；术语「chiral modes counterpropagating」辨为 helical（QVH 畴壁态），锚 [PHY-BERRY] |
