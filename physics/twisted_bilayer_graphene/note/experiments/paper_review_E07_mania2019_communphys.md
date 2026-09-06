<!--
 * @Author       : AI 精读 (系统辨识式阅读法 → 三层分离整理)
 * @Date         : 2026-07-15（初读）→ 2026-09-01（按 4 块新架构重读）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/experiments/paper_review_E07_mania2019_communphys.md
 * @Description  : E07: Mania et al. (2019) Communications Physics — 折叠 BLG 弯曲边界 kink 态零场弹道谷输运（4 块辨识结构；正文为 6 页期刊版，SI 缺失）
-->

# Paper Review: Mania et al. (2019) — 折叠 BLG 弯曲边界上的拓扑谷输运

| 字段 | 内容 |
|------|------|
| **编号** | E07 |
| **标题** | Topological valley transport at the curved boundary of a folded bilayer graphene |
| **作者** | E. Mania, A.R. Cadore, T. Taniguchi, K. Watanabe, L.C. Campos |
| **期刊** | Communications Physics **2**, Article 6 (2019) |
| **DOI / arXiv** | [10.1038/s42005-018-0106-4](https://doi.org/10.1038/s42005-018-0106-4) / [1901.08178](https://arxiv.org/abs/1901.08178)（⚠️ 本 PDF 为 6 页期刊版，非 26 页含 SI 的 arXiv 版） |
| **类型** | 实验 — 双栅低温输运（两探针 + 四探针） |
| **课题组** | L.C. Campos group (UFMG, Brazil；E. Mania 兼 State University of Feira de Santana) + NIMS (Taniguchi/Watanabe) |
| **PDF / SI PDF** | ✅ 正文 PDF（6 页期刊版）；❌ SI 缺失（arXiv 版含 SI，未存） |
| **精读日期** | 2026-07-15（初读）→ 2026-09-01（按 4 块新架构重读） |

> **共享知识引用**：双栅静电学/位移场换算用 `[PHY-GATE]`；电中性点 CNP / 能隙 / 半导体开隙概念用 `[PHY-EF]`；chiral vs helical（QVH 畴壁态）术语辨析用 `[PHY-BERRY]`。不重复讲义。阅读疑问见 `note/shared/method/mechanism_questions.md` `[METHOD-Q]`。

---

## TL;DR

**本文想解决的问题**：在**折叠双层石墨烯（folded-BLG）的弯曲边界**（天然畴壁）上，能否实现 kink 态的**零磁场长程弹道谷输运**——从而绕过前两条路线（SiO₂ 上 AB/BA 结构畴壁、静电栅控畴壁）各自的问题？

**主结果**：① 两探针电阻 $R_{CB,CNP}$ 在 $B=0$、$T=1.2$ K 下，$|D|>1.6$ V/nm 时饱和于弹道电阻 $h/4e^2 = 6.45$ kΩ 📜Q[~]；② 四探针纵向电阻 $R_{xx}^{CB,CNP}$ 降至 ~60 Ω（"a few tens of ohms"）📜Q[~]；③ 由 Landauer-Büttiker 反推平均自由程 $L_{MFP}\sim 20$ μm（device 1）/ $\sim 17$ μm（device 2）📜Q[~]；④ 温度依赖反转——弯曲边界 $R_{xx}$ 随 $T$ 升而升（金属型）、蚀刻边缘随 $T$ 升而降（半导体型），输运 "robust up to room temperature" 📜Q。

**结论/意义**：折叠弯曲边界构成高质量天然畴壁，实现零场长程弹道谷输运；作者措辞为 **"strong evidence of kink states"**（强证据，非"证明"）、MFP 是 **"one of the longest MFP ever reported in a DW"** 📜Q。拓扑保护/谷锁定是**理论佐证**（Martin 2008），本文无直接谷保护实验测量。

---

## 1. 系统辨识导览（判别表为全文唯一权威）

**黑箱三要素**：`{输入旋钮：V_TG、V_BG、T | 输出观测量：两探针 R、四探针 R_xx | 声称结论：弯曲边界 kink 态零场弹道谷输运}`

**四层变量图**（符号层一次钉死）：

| 层 | Mania 2019 实例 |
|----|----------------|
| **L1 旋钮 u** | $V_{TG}$（Cr/Au 顶栅）、$V_{BG}$（Si⁺⁺ 背栅）、$T$（1.2–300 K） |
| **L2 导出量 x₁** | $D=(C_{TG}V_{TG}-C_{BG}V_{BG})/\varepsilon_0$（本文公式，见 §3.2 ⚠️ 分母 ε₀ 非 2ε₀）、CNP 对角线（零电荷条件） |
| **L3 模型量 x₂** | $R_0=h/4e^2=6.45$ kΩ（4 通道弹道极限 = 2 自旋×2 谷）、$L$（通道长度 1/1.75 μm）、$L_{MFP}$（Landauer-Büttiker 反推） |
| **固定参数（非旋钮）** | 折叠几何（弯曲边界）、hBN 双封装、$L$、Cr/Au (1 nm/40 nm)、285 nm SiO₂/Si⁺⁺ |
| **反推量 θ̂** | $L_{MFP}$（由 $R=R_0(1+L/L_{MFP})$ 从 $R$、$L$ 反推） |
| **L4 观测量 y** | 两探针 $R(V_{TG},V_{BG})$、四探针 $R_{xx}(V_{TG},V_{BG})$、$R(D)$@CNP、$R_{xx}(T)$@$V_{BG}=-86$ V |

**可辨识性判别表**（每条判别 = 判据 / 排除谁 / 确立谁）：

| 判别 | 判据（数据） | 排除谁 | 确立谁 |
|------|-------------|--------|--------|
| **墙 vs 体** | $R_{EE,CNP}$ 随 $\|D\|$ **单调增**（半导体开隙），而 $R_{CB,CNP}$ 在 $\|D\|>1.6$ V/nm 后**饱和**于 $h/4e^2$（Fig. 2c）📜Q | 体 2D 半导体导电作为边界低阻来源 | 弯曲边界存在**与体电隔离**的导电通道（存在性，必要条件） |
| **弹道 vs 散射 1D** | 两探针 $R$ 接近 $h/4e^2=6.45$ kΩ（= 4 通道弹道极限）+ 四探针 $R_{xx}^{CB,CNP}\sim 60$ Ω（"a few tens of ohms"，准无背散射）📜Q | 强散射的普通 1D 通道 | 准弹道 1D 输运，通道数 ≈ 4（2 自旋 × 2 谷） |
| **金属 vs 半导体边界** | 弯曲边界 $R_{xx}$ 随 $T$ 升而**升**、蚀刻边缘 $R_{xx}$ 随 $T$ 升而**降**（Fig. 3d,e，$V_{BG}=-86$ V）📜Q | 边界导电由半导体热激活机制解释 | 边界是**金属型**通道，与体半导体行为正交 |
| **DW 形成机制（理论）** | Fig. 1d：层间势能 $\Delta/2$ 在两 BLG 片间**反号**、跨弯曲边界**过零** → 能隙反号 → 谷 Chern 数反号 → DW（Martin 2008，ref 1）📜Q | — | 折叠边界 = 能隙反号界面（**理论论证**，非独立实验测量） |

> **主结果 ↔ 判别表映射**（每条主结果由哪几条判别确立）：
> - 主结果①（$R\approx h/4e^2$ 零场饱和）← {墙 vs 体, 弹道 vs 散射 1D}
> - 主结果②（$L_{MFP}\sim 20$ μm）← {弹道 vs 散射 1D}（Landauer-Büttiker 反推）
> - 主结果③（温度依赖反转）← {金属 vs 半导体边界}
> - （前提）DW 形成 ← {DW 形成机制（理论）}
>
> **分层排除注**：本文证"弯曲边界存在**金属型准弹道 1D 通道**"（存在性 + 弹道性两层），但 **"拓扑保护/谷锁定"未独立实验证**——依赖 $R\approx h/4e^2$ 的数值（4 通道）+ Martin 2008 理论佐证。作者用词是 "strong evidence of kink states"（强证据，非"证明"）📜Q。无直接谷保护测量（对比 E13 的 FFT 判据）。

> **[前提与限定]**（判别结论的适用范围）：
> - **噪声/扰动**：两探针值是 "close to the ballistic resistance"（非严格量子化平台）；作者自陈 "we neglected any other residual resistances"（含接触电阻，未独立扣除）📜Q；**全文无 ± 误差棒**（所有数值为 $=/≈/\sim$ 表述）。
> - **判别性扫轴**：二维扫 $(V_{TG},V_{BG})$ + 沿 CNP 对角线取 $R(D)$；扫 $T$（1.2–300 K）@ $V_{BG}=-86$ V；**全部 $B=0$**（cryogen 可达 7 T 但本文未展示任何 $B\neq0$ 数据）。
> - **候选集 M 边界**：{体 2D 半导体, 散射 1D 通道, 半导体热激活} —— "金属型准弹道墙通道"在该集合内**通过排除法**成立；但"拓扑保护/谷锁定"依赖理论、**集外候选（如边缘缺陷金属导电、非拓扑弹道通道）未单独排除**（封闭世界假设风险，须声明）。

三层标注：📜Q = 原文事实（附位置）｜推导｜📊F = 读图估算｜💭I = 推断。**不确定度（正交轴）**：[±] 原文误差棒 / [~] 原文 $=/≈/\sim$ 无误差棒 / [读图] 图·色标提取 / [相对] 仅相对量。所有数字经 pdftotext + grep 反向核对。

---

## 2. 结果与机制（按论文三段：折叠→DW / 两探针量子电阻 / 四探针+温度）

### 2.1 折叠边界 → 天然畴壁（机制，Fig. 1）

- **器件**：折叠 BLG 夹在两层 hBN 之间，底 hBN 置于 285 nm SiO₂/Si⁺⁺（Si⁺⁺ 为背栅），顶 hBN 上覆盖 Cr/Au 金属栅（Fig. 1a）📜Q。
- **开隙**：横向电场打破每片 BLG 反演对称 → 能隙 $\Delta$（层间能差，ref 19 McCann）📜Q。在底层 BLG，顶层得 $+\Delta/2$、底层得 $-\Delta/2$；该分布在上层 BLG **反转**（Fig. 1d）📜Q。
- **DW 形成**：能隙在两片间**反号** → 谷在两侧持有相反 Chern 数 → 弯曲边界转变成 DW；用 Martin 2008（ref 1）模型论证 kink 态出现 📜Q。
- **kink 态性质**：每谷 2 条自旋简并、$K/K'$ 反向传播；对除**完美 armchair** 外几乎所有边界构型稳健；拓扑保护抑制光滑无序背散射（ref 10）📜Q。
- **术语辨析**：摘要称 "chiral"，正文机制是**谷锁定反向传播**（helical，$K/K'$ 反向）——严格是 QVH 畴壁态，非 QH 边缘通道（见 `[PHY-BERRY]`）💭I。
- **通道洁净**：Fig. 1c AFM（scale 1 μm）显示弯曲边界在清洗后无污染；hBN 平整 + AFM 机械清洁抑制短程散射 📜Q。

### 2.2 两探针量子电阻（Fig. 2）

- **体（蚀刻边缘）**：$R_{EE,CNP}$ 随 $|D|$ **单调增大** → 反映反演对称破缺产生的可调能隙（半导体区）📜Q。
- **边界（弯曲边界）**：$R_{CB,CNP}$ 在 $|D|>1.6$ V/nm 后**饱和**于弹道电阻 $R=h/4e^2$ 📜Q。
- **机制**：高 $D$ 下畴区（体）绝缘 → 弯曲边界 DW 与体**电隔离** → 1D 区进入弹道输运；电阻接近量子化 = 短程无序缺失下背散射被强烈抑制 → 稳健谷输运 📜Q。
- ⚠️ **论文笔误**：摘要与正文写 "R = e²/4h"（电导量纲），应为 $h/4e^2$；同段正文自写 "R = 6.45 kΩ (or R = e2/4h)"、Fig. 2 caption 写 "R = h/4e2"、讨论段写 "R = h/4e2" —— 三者混用，"e²/4h" 是笔误（物理值 = $h/4e^2$ = 6.45 kΩ）。

### 2.3 四探针确认 + 温度依赖（Fig. 3）

- **四探针**（排除接触电阻伪影）：$R_{xx}^{EE,CNP}$ 随 $|D|$ 从 ~1 kΩ **升**到 ~12 kΩ（半导体）；$R_{xx}^{CB,CNP}$ 随 $|D|$ 从 ~400 Ω **降**到 ~60 Ω（高 $D$ 时，"a few tens of ohms"）📜Q。~60 Ω 的纵向电阻 = 准无背散射弹道输运的特征 📜Q。
- **温度依赖**（$V_{BG}=-86$ V，$T$ 从 1.2 K 到 300 K）：蚀刻边缘 $R_{xx}$ 随 $T$ **降**（半导体热激活）；弯曲边界 $R_{xx}$ 随 $T$ **升**（声子增强谷间散射 + 散射到体态）📜Q。
- **室温稳健**：摘要 "topologically protected electronic transport is robust up to room temperature" 📜Q。⚠️ 期刊版正文**未给定量室温 $R$ 值**（温度两探针细节在 SI Note 3/Fig. 5，SI 缺失）。

---

## 3. 实验方法

### 3.1 器件
机械剥离 → MMA 495 C4 聚合物膜分离少层 → 选**自折叠** BLG 样品 → 转移到 hBN/285-nm SiO₂/Si⁺⁺（Si⁺⁺ 背栅）→ 电子束光刻 + Cr/Au (1 nm/40 nm) 热蒸发制电极 → 氧等离子体刻蚀定形 → AFM 探针机械清洁（ref 26）→ 覆盖顶 hBN + Cr/Au 顶栅 📜Q。作者贡献：L.C.C. 提主意、E.M./A.R.C. 制备、K.W./T.T. 供 hBN 📜Q。

### 3.2 静电学（本文公式，注意与 [PHY-GATE] 差异）
$$D=(C_{TG}V_{TG}-C_{BG}V_{BG})/\varepsilon_0$$
$C_{TG},C_{BG}$ = 顶/底电容器单位面积电容，$\varepsilon_0$ = 真空介电常数 📜Q。CNP = 栅压定义的零电荷对角线 📜Q（概念见 `[PHY-EF]`）。
> ⚠️ **本文 D 定义分母为 $\varepsilon_0$（非 $2\varepsilon_0$）**，与 `[PHY-GATE]` §3 标准约定 $D=(C_{tg}V_{tg}-C_{bg}V_{bg})/2\varepsilon_0$ **差因子 2** 💭I。跨论文比较 $|D|$（如本文 1.6 V/nm vs E12 的 0.5 V/nm）时须注意此约定差异。原文未给 $C_{TG},C_{BG}$ 数值。

### 3.3 测量
两探针：恒压 $V_{bias}=1$ mV、测电流，$G=I/V$；四探针：恒流 $I=100$ nA、测纵向电压 $V_{XX}$，$R_{XX}=V_{XX}/I$；低温 $f=17$ Hz 锁相；常态 $T=1.2$ K；cryogen 磁场可达 7 T（本文数据全 $B=0$）📜Q。

---

## 4. 关键数据（提取链 + 验证链 + 不确定度标注）

| 参数 | 值 | 证据/不确定度 |
|------|-----|--------------|
| 通道长度 $L$ | device 1 = 1 μm；device 2 = 1.75 μm | 📜Q[~]（引 SI Fig. 4/Note 2，SI 缺失） |
| 两探针量子电阻 | $R_{CB,CNP}\to h/4e^2 = 6.45$ kΩ，$\|D\|>1.6$ V/nm | 📜Q[~]（"close to"/"saturate close to"） |
| 四探针纵向电阻 | $R_{xx}^{CB,CNP}$ ~400 Ω → ~60 Ω（高 $D$）；$R_{xx}^{EE,CNP}$ ~1 → ~12 kΩ | 📜Q[~] |
| 平均自由程 | $L_{MFP}\sim 20$ μm (D1)；$\sim 17$ μm (D2) | 📜Q[~]（Landauer-Büttiker 反推） |
| 温度 | $T=1.2$ K（主数据）；1.2–300 K（变温 @ $V_{BG}=-86$ V） | 📜Q |
| 磁场 | $B=0$ T（全部数据）；cryogen 上限 7 T | 📜Q |
| 锁相频率 | $f=17$ Hz | 📜Q |
| 偏置 | 两探针 $V_{bias}=1$ mV；四探针 $I=100$ nA | 📜Q |
| 器件参数 | 285 nm SiO₂/Si⁺⁺；Cr/Au 1 nm/40 nm；hBN 双封装 | 📜Q |
| 色标值（caption） | Fig. 2 R: 0.2–19.5 kΩ；Fig. 3a $R_{xx}$: 0.06–11.7 kΩ；Fig. 3b $R_{xx}$: 0.01–0.4 kΩ；D 轴 −2.3–2.3 V/nm | [读图] |

**验证链**：
1. **两探针 ↔ 四探针互证**：两探针 $R\approx h/4e^2$（4 通道）与四探针 $R_{xx}\sim 60$ Ω（准无背散射）各自独立指向弹道输运，且四探针排除接触电阻伪影 📜Q。
2. **两器件一致**：$L=1$ μm 与 $1.75$ μm 各自反推 $L_{MFP}=20/17$ μm，量级一致 → 非单器件偶然 📜Q。
3. **边-体双轴正交对比**：同一 $D$ 轴上 $R_{EE}$（体）与 $R_{CB}$（边界）行为相反 → 墙/体区分 📜Q。
4. ⚠️ **缺失的验证**：无多器件面积/几何互验（对比 E12 的 ΔB↔Δn 互验）；无直接谷保护测量（对比 E13 的 FFT）；无 $B\neq0$ 数据（对比 E15 的 QH 区域）。

---

## 5. 主要结论
1. 折叠 BLG 弯曲边界 = 高质量天然畴壁，两探针 $R$ 在 $B=0$、$T=1.2$ K 饱和于 $h/4e^2=6.45$ kΩ（$|D|>1.6$ V/nm）📜Q。
2. 四探针 $R_{xx}$ 降至 ~60 Ω（"a few tens of ohms"）→ 准无背散射弹道输运 📜Q。
3. $L_{MFP}\sim 20$ μm (D1) / ~17 μm (D2)：作者称 "one of the longest MFP ever reported in a DW"；比 SiO₂ 上 DW **"at least two-orders higher"**（ref 13 = Ju 2015）、比 gate-confinement 通道 **"comparable"**（refs 15,16 = Li 2016 / Lee 2017）📜Q。
4. 温度依赖反转（边界金属型 / 体半导体型），输运 "robust up to room temperature" 📜Q。
5. 保守表态：作者用 "strong evidence of kink states"（非"证明"）；拓扑保护/谷锁定由 Martin 2008 理论佐证，本文**无直接谷保护实验证据** 📜Q。

---

## 6. 局限与未解决
| 局限 | 说明 | 证据 |
|------|------|------|
| $R$ 非严格量子化平台 | "close to" $h/4e^2$，非平台；残余（接触）电阻被"忽略"而非独立扣除 | 📜Q |
| 无直接谷保护测量 | 无 FFT 散射判据（E13）、无非局域测量 | 💭I |
| 无 $B\neq0$ 数据 | cryogen 可达 7 T，但全部数据 $B=0$；QH 区域未探索（E15 补） | 📜Q |
| 可扩展性未证 | 本文用自然**自折叠**样品（"we selected self-folded BLG samples"），同时称折叠结构"可受控制备"（"a variety of techniques enable the controlled production"）——可控性未在本实验验证 | 📜Q + 💭I |
| 单条弯曲边界 | 只一条 DW，无通道间耦合 | 💭I |
| 曲率效应未定量 | 正文无弯曲半径数值、无曲率对 kink 态影响的定量讨论 | 📜Q（无该数据）→ NEEDS_VERIFICATION |
| SI 缺失 | 器件几何（SI Fig. 4/Note 2）、温度两探针细节（SI Fig. 5/Note 3）、Martin 模型论证（SI Fig. 3/Note 1）均无法引用 | — |

---

## 7. 与其他工作的关系（跨论文对标，仅本文自述 + 外部标注）

| 工作 | 关系 |
|------|------|
| Martin 2008 (ref 1) | kink 态理论模型（gap 反号 → in-gap 1D 态）——本文机制依据 📜Q |
| Ju 2015 (ref 13) / Jiang L 2018 (ref 14) | SiO₂ 上 AB/BA 结构畴壁路线；本文 MFP "at least two-orders higher" 📜Q |
| Li J 2016 (ref 15) / Lee 2017 (ref 16) | 静电 gate-confinement 通道；本文 MFP "comparable" 📜Q |
| McCann 2006 (ref 19) | 不对称能隙 Δ 📜Q |
| Zhang 2009 (ref 20) / Taychatanapat 2010 (ref 21) | 双栅 BLG 可调能隙（体半导体行为参照）📜Q |
| Shimazaki 2015 (ref 7) | 谷电流产生（背景）📜Q |

> ⚠️ Phase S 外部对标（**非本文引用**，💭I）：E13 Verbakel 2021 用 FFT 直接证谷保护——补本文缺失的直接谷保护证据；E15 Mahapatra 2022 把畴壁放入 QH 区域——补本文缺失的 $B$ 场数据；E12 Xu 2019 用 AB 干涉证**相干**——本文证的是**弹道（MFP）**而非相干干涉，两者是不同表征维度。

---

## 8. 对后续研究的影响
- 提出折叠几何作为"少栅极"的谷电子学器件路线（valley filter / valley valve）📜Q。
- 平台可对接超导邻近（refs 23,24）与 Luttinger 液体（ref 25）研究 📜Q。
- 留下开放问题：kink 态 → 体态散射抑制的**微观机制**（作者自陈 "future microscopic measurements could bring more explanation"）📜Q。

---

## 9. 理论模型映射（供计算对标）

| 映射 | 说明 |
|------|------|
| $D\to\Delta$ | 位移场 → 双层能隙（层间能差 Δ，ref 19）；⚠️ 本文 $D=(C_{TG}V_{TG}-C_{BG}V_{BG})/\varepsilon_0$，分母 ε₀ 非 2ε₀（[PHY-GATE] §3）；原文未给 Δ 数值（仅定性 "tunable band gap"）📜Q |
| 折叠边界 → DW | 层间势 $\Delta/2$ 反号过零 → gap 反号 → Chern 反号（Martin 2008）📜Q |
| $R_0=h/4e^2$ | 4 通道（2 自旋 × 2 谷）弹道极限 📜Q |
| Landauer-Büttiker | $R=R_0(1+L/L_{MFP})$ → $L_{MFP}$ 反推 📜Q |
| 与 TBPM 对应 | 折叠几何 = AB 堆叠 + 层序反转线 → TB 模型可构造弯曲边界算 kink 态；但**弹道输运（MFP）**是有限尺寸量子输运量，bulk $\sigma_{xx}$ 只给背景，复现需有限器件 Landauer/Fisher-Lee 透射计算（同 E10/E12 §9 注记）💭I |

---

## Phase S 目的接口（三问引用式 + 增量价值）

- **Q1（edge state 如何表征）**：低温两探针 + 四探针输运，边-体区分靠 $R_{EE}$(体) vs $R_{CB}$(边界) 随 $D$ 的**正交行为**（体单调增、边界饱和）+ 温度反转（金属 vs 半导体）——见 §2/§4。表征维度 = 弹道性（$h/4e^2$、MFP），非相干（无 AB/FP）。
- **Q2（理论如何复现）**：无新理论；Martin 2008 kink 态模型 + Landauer-Büttiker 反推 MFP 📜Q。
- **Q3（理论↔实验对应）**：$D$ 开隙 ↔ 体半导体、边界 $h/4e^2$；折叠 ↔ 层序反转线；4 通道 ↔ $h/4e^2$；现有理论解释弹道极限 ✓，但**谷保护未直接实验证**（理论佐证）📜Q。

> **增量价值**：与 E10（相干 FP/AB）、E12（相干 AB + miniband）分工——本文是**单条畴壁弹道极限**的基准（$h/4e^2$ + $L_{MFP}\sim 20$ μm + 零场），**无相干振荡数据**。report.md §2 用其"边-体正交对比 + 金属型温度依赖"作**弹道输运**的代表性判据；§4 用 $R_0=h/4e^2$ 作单畴壁通道数的理论对标。

---

## 反向核对 pass (2026-09-01)

pdftotext 提取 6 页期刊版正文，逐项 grep 核对：全部数字（6.45 kΩ / h/4e² / 20 μm / 17 μm / 1 μm / 1.75 μm / 1.2 K / 300 K / 17 Hz / 1 mV / 100 nA / 1.6 V/nm / ~1 kΩ / ~12 kΩ / ~400 Ω / ~60 Ω / −86 V / 285 nm / Cr/Au 1 nm 40 nm / 7 T / 0.2–19.5 kΩ / 0.06–11.7 kΩ / 0.01–0.4 kΩ / −2.3–2.3 V/nm）均在原文找到。色标值与 D 轴范围标注 [读图]。

⚠️ 重读修正点（见更正日志）：① 旧 review "比 Li 2016 高 200 倍 / 70–110 nm" 等跨论文数字无本文来源 → 删除；② "two-orders higher" 是 vs SiO₂ DW（ref 13 = Ju 2015），对 gate-confinement 是 "comparable" → 修正归属；③ 旧 review 引 "Fig. 5"（室温）→ 期刊版温度数据在 Fig. 3d,e（无 Fig. 5）；④ 论文 "R = e²/4h" 为笔误（应为 h/4e²）；⑤ 本文 D 公式分母 ε₀ 非 2ε₀（[PHY-GATE] 差因子 2）→ 标注。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-09-01 | **按 4 块新架构整体重写**（TL;DR 问题句式 + 系统辨识导览/判别表 + 三段结果 + 数据表 + 验证链 + 理论映射 + 三问接口 + 反向核对）；证据分级 📜Q/💭I + 不确定度标注 [~]/[读图] 全程启用 |
| 2026-09-01 | **来源切换**：旧 review 基于 26 页含 SI 的 arXiv 版；本 PDF 为 6 页期刊版 → SI 数据（Supplementary Fig. 1–5 / Note 1–3）不可引用，相关处标注"SI 缺失"；器件几何（L 值）与温度两探针细节改标 SI 引用 |
| 2026-09-01 | **归属修正**：旧 "比 Li 2016 高两个数量级/200 倍" 无源 → 原文是 "at least two-orders higher than ... DW of BLG on SiO₂"（ref 13 = Ju 2015）、"comparable to ... gate-confinement"（refs 15,16） |
| 2026-09-01 | **跨论文数字清除**：旧 review 中 Li 2016 的 "70–110 nm / 70–200 nm / 4-gate <10 nm 对准" 等数字无本文来源（违反禁止跨论文迁移）→ 删除 |
| 2026-09-01 | **图号修正**：旧 "Fig. 5（室温）" → 期刊版温度数据在 Fig. 3d,e；论文仅 Fig. 1/2/3 |
| 2026-09-01 | **笔误/约定标注**：论文摘要 "R = e²/4h" 为笔误（=h/4e²=6.45 kΩ）；本文 D 公式分母 ε₀（非 2ε₀）与 [PHY-GATE] 差因子 2 → 均标注 ⚠️ |
