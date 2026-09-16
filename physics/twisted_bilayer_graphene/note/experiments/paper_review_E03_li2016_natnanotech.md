<!--
 * @Author       : AI 精读 (系统辨识式阅读法 → 三层分离整理)
 * @Date         : 2026-07-15（初读，基于 arXiv 39 页含 SI 版）→ 2026-09-01（4 块新架构重读，基于期刊版正文）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/experiments/paper_review_E03_li2016_natnanotech.md
 * @Description  : E3: Li, J. et al. 2016 — 双分裂栅静电定义 EFW kink 态、栅控谷极化一维弹道输运（纯 review；通用物理锚点到 note/shared/physics/）
-->

# Paper Review: Li, J. et al. (2016) — 栅控拓扑导电通道（双分裂栅静电定义 kink 态）

| 字段 | 内容 |
|------|------|
| **编号** | E3 |
| **标题** | Gate-controlled topological conducting channels in bilayer graphene |
| **作者** | Jing Li, Ke Wang, Kenton J. McFaul, Zachary Zern, Yafei Ren, Kenji Watanabe, Takashi Taniguchi, Zhenhua Qiao, Jun Zhu |
| **期刊** | Nature Nanotechnology 11, 1060–1065 (2016) |
| **DOI / arXiv** | 10.1038/nnano.2016.158 / 1509.03912 |
| **类型** | 实验 — 低温输运（双分裂栅 + 准四探针） |
| **课题组** | Jun Zhu group (Penn State) + Zhenhua Qiao (USTC 理论) + NIMS (Watanabe/Taniguchi) |
| **PDF / SI PDF** | ✅ `reference/pdfs/Li 等 - 2016 - Gate-controlled topological conducting channels in bilayer graphene.pdf`（7 页期刊版正文）；✅ `reference/pdfs/Li 等 - 2016 - SI of Gate-controlled topological conducting channels in bilayer graphene.pdf`（期刊 SI；§7 能带 / §8 电导已读入 → §9.1/§9.2） |
| **精读日期** | 2026-07-15（初读，arXiv 39 页含 SI 版）→ 2026-09-01（4 块新架构重读，据期刊版正文） |

> **来源声明**：本重读仅基于 `reference/pdfs/` 中的 **7 页期刊版正文**（pdftotext → `/tmp/e3.txt`）。旧 review 基于 arXiv:1509.03912v2（39 页含 SI）所写的、在期刊版正文中 grep 不到的细节（SI §1–10 内容），本重读一律不继承，标注 `NEEDS_VERIFICATION` 或删除。
>
> **SI 已补入**（2026-09-03）：期刊 SI PDF（`Li 等 - 2016 - SI of ...`）已下载并读入 **SI §7「能带计算」→ §9.1** 与 **SI §8「kink 态电导计算」→ §9.2**（pdftotext → `/tmp/li2016_si.txt`）。SI §7/§8 是正文 Fig 3a（非手征态能带）与 Fig 3b（$L_k$ 提取）的建模/计算源头，补全了正文未给的紧束缚参数（$t$、$t_\perp$、$2U$、$W$、$d$、边界 $W$=10 eV）与两终端 Landauer-Büttiker 电导方法（Caroli 公式 + 30 样本平均）。其余 SI 节（§1–6, §9–10）本次未逐节精读。
>
> **共享知识引用**：双栅静电（n/D 换算、共模/差模）→ `[PHY-GATE]`；费米能/化学势/CNP → `[PHY-EF]`；谷相位与 chiral/helical 术语辨析 → `[PHY-BERRY]`。本 review 不复制讲义，只写"本文代入"的数值。

---

## TL;DR

**本文想解决的问题**：能否不依赖天然 AB/BA 结构畴壁，而用**纯电学栅控**（Martin 2008 的"两反向栅控区线结"方案）在双层石墨烯中定义并开关一条拓扑导电通道？

**主结果**：① **栅控开/关**——"奇"场配置（$D_L D_R<0$）结导 $\sigma_j$ 在体能隙内保持 **10–15 µS**，而"偶"配置（$D_L D_R>0$）降至 **<1 µS** 📜Q（Fig 2b）；② **零场 MFP 出乎意料短**——$R_j$=40–100 kΩ → $L_k$=70–200 nm（Landauer–Büttiker，device 1），归因于平滑势剖面引入的非手征束缚态介导谷间散射 📜Q；③ **垂直磁场恢复弹道**——device 1 在 B≈7 T 达 $R_{kink}$≈15 kΩ（$L_k$≈0.8 µm，比零场长 4–10 倍），device 2（L=400 nm）在 8–14 T 达 $h/4e^2$=6.5 kΩ 弹道极限附近 📜Q。

**结论/意义**：首次实验实现**电学可编程**（栅压定义、可开关）的 1D 拓扑通道；作者措辞 "paves the way to the realization of gate-controlled ballistic valley transport" 📜Q。

---

## 1. 系统辨识导览（判别表为全文唯一权威，机制细节见 [PHY-*]）

**黑箱三要素**：`{输入旋钮: V_Si, D_L, D_R, B, T | 输出观测量: σ_j=1/R_j, R_bulkCNP | 声称结论: 电场线结定义拓扑 kink 态、odd/even 开/关、B 场恢复弹道 4e²/h}`

**四层变量图**（符号层一次钉死）：

| 层 | Li 2016 实例 |
|----|-------------|
| **L1 旋钮 u** | $V_{Si}$（Si 背栅，调结处 $E_F$）、$D_L, D_R$（四分裂栅，左右两侧体位移场）、$B$（0–14 T）、$T$（1.6 K；另 310 mK 单独冷却） |
| **L2 导出量 x₁** | $n_L=n_R=0$（CNP 条件，由 $R_{bulkCNP}$ 全局极小定）、$E_F$（结处）、$\Delta$（体能隙，随 $D$ 变） |
| **L3 模型量 x₂** | $w$（结宽 70/110 nm）、$L$（结长 1 µm/400 nm）、$R_0=h/4e^2$=6.5 kΩ、$W$=0.6 eV（Anderson 无序强度，理论） |
| **固定参数（非旋钮）** | $w, L$（光刻定）；$\mu$=100,000 / 22,000 cm²/V·s（D1/D2） |
| **反推量 θ̂** | $L_k$（MFP，由 $R_j$ 经 Landauer–Büttiker 反推）、$R_{kink}$（两通道模型扣除非手征平行通道）、$\Delta(D)$（温度依赖测量，ref 34） |
| **L4 观测量 y** | $\sigma_j=1/R_j$（结导/结阻）、$R_{bulkCNP}$（体 CNP 电阻） |

> 与 E10/E12 符号差异：本文测**结电导 $\sigma_j=1/R_j$**（非电阻率），且 $n$ 未分 $n_{in}/n_{out}$（结的 $E_F$ 由单一 $V_{Si}$ 全局调）；左右两侧各自一整套顶/底栅，$D_L, D_R$ 是**已合成的体位移场**（非顶/底场分别计）。

**可辨识性判别表**（唯一权威；本文五条判据）：

| 判别 | 判据（数据） | 排除谁 | 确立谁 |
|------|-------------|--------|--------|
| **kink 态存在（odd/even 对比）** | 体能隙内：odd 配置 $\sigma_j$ 保持 10–15 µS、even 配置 <1 µS（Fig 2b）；四象限 $R_j$(CNP) 系统性高（even）/低（odd）（Fig 2c）📜Q | 无通道 / 结绝缘（even 配置） | 结处存在**依赖 $D_L D_R$ 符号翻转**的导电通道（kink 态） |
| **体 vs 结** | $R_{bulkCNP}$>10 MΩ（体绝缘）vs $R_j$=40–100 kΩ（结导电），同一 $D$ 范围 📜Q | 体 2D 导电 | 导电通路在**结**（1D 通道，必要条件） |
| **拓扑（kink）vs 无序亚隙导电** | 通道开关由 $D_L D_R$ 符号翻转**对称地**控制（正负各两象限），与理论预测（ref 6）一致；但 $R_j\gg R_0$（非精确量子化）→ 亚隙非手征态共存 📜Q | 纯无序亚隙导电（无法解释符号依赖开关） | kink 态为主通道，但零场弹道性被非手征态破坏 |
| **零场背散射来源 = 非手征态** | 平滑势剖面能带计算出现 gap 内非手征束缚态（Fig 3a）；晶格缺陷被高迁移率 + 共振散射排除（ref 25）、点缺陷被大波函数展宽排除（ref 9）📜Q | 晶格缺陷、点缺陷 | 非手征态介导谷间散射（多粒子过程，类 QSH 边缘态 Kondo 类比） |
| **B 场恢复弹道 = 移除非手征态 + Lorentz 分离** | $R_{kink}\to h/4e^2$（device 2，8–14 T）；B=6 T 能带计算非手征态被朗道量子化推开（Fig 4c）；K/K′ 波函数 Lorentz 分离 14 nm（Fig 4d）📜Q | （无竞争解释，作者两机制并列） | 非手征态是零场背散射主源，B 场经两机制压制 |

> **主结果 ↔ 判别表的对应**：
> - 主结果① kink 态栅控开/关 ← {kink 态存在, 体 vs 结}
> - 主结果② 零场 $L_k$=70–200 nm（非手征态散射）← {零场背散射来源}
> - 主结果③ B 场恢复弹道（device 2 达 $4e^2/h$）← {B 场恢复弹道}
> - （前提）1D 拓扑通道 ← {kink 态存在, 体 vs 结, 拓扑 vs 无序亚隙}
>
> **分层排除，非一步证成**：①「体 vs 结」先证导电在结不在体（必要条件）；②「kink 态存在」证通道受 $D_L D_R$ 符号控制（理论预言的核心 signature）；③「B 场恢复弹道」证非手征态是零场背散射主源、kink 态本身是弹道的。⚠️ **拓扑性质本身**（谷极化、谷 Chern 数的直接测量）本文**未做**，靠理论（ref 6）支持——作者用词是 "evidence of ... kink states"（证据，非"证明"）📜Q。

> **[前提与限定]**（判别结论的适用范围）：
> - **噪声/扰动**：原始 $R_j$ 含接触电阻（数 kΩ，Supp §5，本文正文未给数值）；$R_j$ 可**小于** $h/4e^2$ 因非手征态平行导电（需两通道模型扣除，Supp §10）；单调背景成分数值未给。
> - **判别性扫轴**：固定 $D_L, D_R$ 扫 $V_{Si}$（$E_F$ 轴，Fig 2a）；固定 $V_{Si}$ 扫 $B$（磁轴，Fig 4a，0–14 T）；$T$ 只两个值（1.6 K、310 mK，无变温系列）。
> - **候选集 M 边界**：{无通道/结绝缘, 体 2D 导电, 纯无序亚隙导电, 晶格缺陷, 点缺陷} —— "kink 态"在该集内唯一幸存；**集外候选**（其他背散射机制的细节）原文明言 "the nature of the backscattering mechanisms remains to be understood" 📜Q。拓扑性质的独立直接证据（如谷极化测量）不在本文候选集内。

三层标注：📜Q = 原文事实（附位置）｜推导｜📊F = 读图估算｜💭I = 推断。**不确定度（正交轴）**：[±] 原文误差棒 / [~] 原文以 =/≈ 给出但无误差棒 / [读图] 图·色标提取 / [相对] 仅相对量。所有数字经 pdftotext + grep 反向核对。

---

## 2. 结果与机制（按论文三段：栅控开/关 → 零场短 MFP → B 场恢复弹道）

### 2.1 kink 态的栅控开/关

**原理**（Martin 2008 方案，ref 6）📜Q：同一 AB 堆叠 BLG 两侧施加反向体位移场，$D(x)$ 在结处过零 → Berry 曲率 $\Omega$ 符号反转（$K$ 与 $K'$ 谷符号相反）→ 沿层间静电势差 $V=0$ 线束缚**反传播的谷编码 1D 模**。每个谷 4 条手征模（2 自旋 × 2 层），不同谷反向传播（Fig 1a）→ 总 8 模（4 条 $K$ + 4 条 $K'$）📜Q。无谷混合散射时背散射被禁，预期结导量子化 $4e^2/h$ 📜Q。

> 术语辨析：摘要称 "chiral modes"，但正文机制是**谷锁定反向传播**（helical）——严格是 QVH 畴壁态，非总电荷手征的 QH 边缘通道（见 [PHY-BERRY] "chiral vs helical"）。⚠️ "EFW（电场壁）" 是我们对 "line junction of two oppositely gated regions"（ref 6 方案）的 shorthand，**原文未用 "EFW" 一词** 💭I。

**观测**（device 1）📜Q：$\sigma_j$ 作为 $(D_R, V_{Si})$ 函数（Fig 2a，$D_L=\pm0.25$ V/nm），对角线 = 结 CNP 区。体能隙内（对应 $V_{Si}$ 约 25 V 宽，Fig 2b caption）$\sigma_j$ 在 odd 配置保持 **10–15 µS**、even 配置降至 **<1 µS**（Fig 2b）📜Q[~]；四象限 $R_j$(CNP) 系统性高（even $(+,+),(-,-)$）/低（odd $(+,-),(-,+)$）（Fig 2c）📜Q。这是 kink 态存在的核心 signature。

### 2.2 零场 MFP 出乎意料短

- $R_j$（kink 态）= **40–100 kΩ** → Landauer–Büttiker $R_j=R_0(1+L/L_k)$（$R_0=h/4e^2$=6.5 kΩ、$L$=1 µm）→ $L_k$=**70–200 nm** 📜Q[~]（Fig 2 段 + 式 (1)）。
- **矛盾**：$L_{2D}$ 由小动量转移（谷内、长程库仑杂质）主导；kink 谷间背散射需大动量转移、在 h-BN 封装清洁样品中应罕见 → 预期 $L_k\gg L_{2D}$，但实测 $L_k<200$ nm 与 $L_{2D}$（数百 nm）相当 📜Q。
- **解释 = 非手征束缚态**📜Q：平滑静电势剖面（Fig 1b）在 kink 态之外还支持**非手征态**，其能级伸入体能隙 $\Delta$（Fig 3a，refs 9,10）——非手征态被结宽束缚、沿结长延展，**有效缩小能隙**（理论 $\Delta$=30 meV 被压到 ~21 meV）📜Q。晶格缺陷被排除（高迁移率 + 共振杂质散射 ref 25）；点缺陷被排除（大波函数展宽 ref 9）📜Q。非手征态可因库仑势涨落形成量子点、介导 kink 态谷间混合（多粒子过程，类比 QSH 边缘态的 Kondo 机制 refs 26–30）📜Q。作者明言背散射机制 "remains to be understood"、留待未来研究 📜Q。
- **理论**（Green 函数 + 在位 Anderson 无序，$W$=0.6 eV，Supp §8）📜Q：$L_k$=266 / 210 / 141 nm（$E_F$=0 / 5 / 14 meV）→ $L_k$ 随 $E_F$ 增大而减小（更多散射路径）；$L_k$ 随 $\Delta$ 增大、$w$ 减小而增大（改善弹道方向）📜Q。

### 2.3 垂直磁场恢复弹道

- **device 1**（$L$=1 µm）：$R_{kink}$ 随 $B$ 快速下降，在 B≈7 T 达 ~15 kΩ → $L_k$≈0.8 µm，比零场长 **4–10 倍** 📜Q[~]（Fig 4a 段）。
- **device 2**（$L$=400 nm）：$R_{kink}$ 在 **8–14 T** 达并维持 $h/4e^2$=6.5 kΩ 弹道极限附近 📜Q[~]。Fig 4b：B=8 T 近 CNP 处 odd 配置 $R_j$≈6–10 kΩ，对 $|D|$=0.3–0.5 V/nm **不敏感**；even 配置数百至数千 kΩ 📜Q[~]。
- **两机制**（作者并列）📜Q：① **朗道量子化推开非手征态**（Fig 4c，B=6 T 能带计算）→ 减少非手征态介导的背散射；② **Lorentz 力反向分离 K/K′ 波函数**（Fig 4d，B=6 T 分离 14 nm；$E_F$=0 时零分离、随 $E_F$ 与 $B$ 增大而增）→ 压制一切谷混合。作者类比："resembles the picture of the chiral edge state in the quantum Hall effect" 📜Q。
- **两通道模型提取 $R_{kink}$**📜Q（Supp §10）：原始 $R_j$ 可小于 $h/4e^2$ 因非手征态平行导电；用 $(+,+)$ 配置的 $R_j$ 近似平行通道电阻，扣除得 $R_{kink}$。

---

## 3. 实验方法

### 3.1 器件
六步制备 📜Q（Methods）：多层石墨烯（Kish graphite 剥离，~2 nm 薄片）分裂底栅 → h-BN（15–30 nm）→ BLG → 顶 h-BN → Ti/Au 电极（5/70 nm）→ 顶分裂栅 Ti/Au（5/20 nm），Si 背栅（SiO₂ 290 nm 热氧化）。结连四个 BLG 电极、**准四探针**几何消除电极电阻（Fig 1d）📜Q。顶/底分裂栅对准 **<10 nm**（宽度匹配 <15 nm；分裂宽可到 50 nm、w>70 nm 高良率）📜Q。测量 $T$=1.6 K（另 310 mK 单独冷却）📜Q。

### 3.2 静电学
四分裂栅独立控制左右体位移场 $D_L, D_R$；Si 背栅调结处 $E_F$。栅效率用量子霍尔标定；$D=0$、$n=0$ 由 $R_{bulkCNP}$ 全局极小确定；测量在 $n_L=n_R=0$、固定 $D_L, D_R$ 下进行 📜Q（Fig 1a caption）。⚠️ 原文**未给** $D$ 与栅压的显式公式（仅称 $D_L, D_R$ 为左右"bulk displacement fields"）；$D$↔栅压换算见 [PHY-GATE] §3，$E_F$/CNP 区分见 [PHY-EF]。

### 3.3 测量
$R_{bulkCNP}$（体 CNP 电阻）、$\sigma_j=1/R_j$（结导）📜Q；变 $B$（0–14 T）、固定 $D_L, D_R$ 扫 $V_{Si}$。

---

## 4. 关键数据（提取链 + 验证链 + 不确定度标注）

### 4.1 器件几何与质量
| 参数 | Device 1 | Device 2 |
|------|----------|----------|
| 结宽 $w$ | 70 nm 📜Q[~] | 110 nm 📜Q[~] |
| 结长 $L$ | 1 µm 📜Q[~] | 400 nm（=0.4 µm）📜Q[~] |
| 体迁移率 $\mu$ | 100,000 cm²/V·s 📜Q[~] | 22,000 cm²/V·s 📜Q[~] |

（氧化物支撑样品 $\mu$ 仅数千 cm²/V·s，作对照 📜Q。）

### 4.2 能隙与体绝缘
- $\Delta$（实验）= **数十 meV** 📜Q[~]（正文 "a few tens of millielectronvolts"）；Fig 1e 右轴 $\Delta(D)$ 温度依赖（ref 34）标度至 ~70 meV（$D$ 轴至 0.6 V/nm）📊F[读图]。
- $R_{bulkCNP}$>**10 MΩ**（测量 $D$ 范围）📜Q[~]；Fig 2b 结处 $\Delta$ 对应 $V_{Si}$ 约 **25 V** 📜Q[~]。
- 理论 $\Delta$=**30 meV**（Fig 3a 计算参数）📜Q[~]；因非手征态有效缩至 ~**21 meV** 📜Q[~]（正文 "effectively reduced to ∼21 meV"）。

### 4.3 kink 态开/关与零场 MFP
- even 配置（体隙内）$\sigma_j$<**1 µS**；odd 配置 **10–15 µS** 📜Q[~]（Fig 2b）。
- $R_j$（kink）=**40–100 kΩ** → $L_k$=**70–200 nm**（$R_0$=6.5 kΩ、$L$=1 µm）📜Q[~]；接触电阻数 kΩ（Supp §5，正文未给值）💭I[相对]。

### 4.4 理论 MFP（Green 函数 + Anderson 无序）
$W$=0.6 eV；$L_k$=**266 / 210 / 141 nm**（$E_F$=0 / 5 / 14 meV）📜Q[~]（正文）。⚠️ **原文内部不一致**：Fig 3 caption 中间值写 **223 nm**，正文写 **210 nm**（$E_F$=5 meV 处），此处按正文取 210 并标注差异 📜Q。$L_k$ 随 $\Delta$ 增、$w$ 减而增 📜Q。

### 4.5 B 场恢复弹道
- device 1：$R_{kink}$≈**15 kΩ** @ B≈7 T → $L_k$≈**0.8 µm**，4–10 倍于零场 📜Q[~]。
- device 2：$R_{kink}$ 达并维持 **6.5 kΩ**（$h/4e^2$）@ **8–14 T** 📜Q[~]。
- B=8 T 近 CNP：odd 配置 $R_j$≈**6–10 kΩ**（$|D|$=0.3–0.5 V/nm 不敏感）；even 配置数百–数千 kΩ 📜Q[~]。
- B=6 T 计算：K/K′ 波函数 Lorentz 分离 **14 nm** 📜Q[~]（Fig 4d caption）。

### 4.6 证据链与论证结构
三支柱 = ① 存在性（odd/even 开/关，Fig 2）→ ② 弹道性被非手征态破坏（Fig 2b/3 + 理论）→ ③ B 场恢复弹道（Fig 4）。**双轴判别**：密度/静电轴（$R_{bulkCNP}$>10 MΩ vs $R_j$ 导电）+ 磁轴（$R_{kink}\to h/4e^2$）各排除一次体导电/非拓扑通道。**两通道模型**是 $R_{kink}$ 提取的关键（原始 $R_j$ 含非手征平行通道贡献）。

---

## 5. 主要结论

1. 双分裂栅在 BLG 中**静电定义并开关**了 1D 拓扑 kink 态：odd 配置导电（10–15 µS）、even 配置绝缘（<1 µS）📜Q。
2. 零场 MFP $L_k$=70–200 nm，出乎意料短；归因于平滑势剖面的**非手征束缚态**介导谷间散射（机制细节留作未来研究）📜Q。
3. 垂直磁场经「朗道量子化移除非手征态」+「Lorentz 力分离 K/K′」两机制**恢复弹道**，device 2 在 8–14 T 达 $4e^2/h$ 极限附近 📜Q。
4. 作者结论措辞："paves the way to gate-controlled ballistic valley transport" + "valley-controlled valves, beam splitters and waveguides" 📜Q。
5. 展望：更窄结 + 更大带隙 → 非低温运行；双分裂栅 → 势控少电子量子点（ref 32）与 BLG QH 区域 edge-state/domain-wall 物理（refs 31,33）📜Q。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 零场弹道性差、电导未量子化 | $R_j$=40–100 kΩ vs $R_0$=6.5 kΩ；即使 B=8 T 也只是"接近" $4e^2/h$ 非精确平台 | 📜Q |
| 背散射机制未解 | "remains to be understood"，非手征态量子点介导为候补 | 📜Q |
| 非结构 DW | 静电 $V=0$ 线非原子级 sharp AB/BA 边界 → 结宽 $w$~70–110 nm 引入非手征态 | 💭I（正文"平滑静电势剖面支持非手征态"） |
| 4 栅加工难 | 对准 <10 nm 需特殊 re-alignment 流程（否则达 90 nm 失配） | 📜Q（Methods） |
| 无拓扑性质直接测量 | 谷极化/谷 Chern 数的独立探测本文未做，拓扑性靠理论（ref 6）+ odd/even 对称支持 | 💭I |
| 无变温系列 | 仅 1.6 K 与 310 mK 两点 | 📜Q |

---

## 7. 与其他工作的关系（跨论文对标放这里）

| 工作 | 关系 |
|------|------|
| Martin, Blanter & Morpurgo 2008 (ref 6) | **直接理论原型**——"两反向栅控区线结"的 EFW 方案 | 📜Q |
| Ju et al. 2015 (ref 14) | LSW 路线对照——结构 AB/BA 畴壁（天然、随机位置）vs 本文电场线结（栅编程、可扩展） | 📜Q |
| Jung 2011 (ref 8) / Qiao 2011 (ref 9) / Zhang 2013 (ref 11) | valley-Hall kink / valley Chern 数的理论框架 | 📜Q |
| Qiao et al. 2014 (ref 15) | 通道交叉电流分配 → valley valve/beam splitter 的理论基础 | 📜Q |

> ⚠️ Phase S 外部对标（**非本文引用**）💭I：本文是 E1–E18 中**唯一 EFW（栅控电场壁）**实验——vs Ju 2015（LSW，$L_0$=420 nm）与 Mania 2019（LSW 折叠，$L_{MFP}$~20 µm）。EFW 核心优势 = 栅编程可开关/可扩展；代价 = 非原子级 sharp 结宽引入非手征态 → 零场 $L_k$ 远短于 LSW 路线。与 Zhang 2024（结构 LSW 的 CVD 输运，后续工作）互补：单条静电 DW（本文）vs 多条结构 LSW（Zhang）。

---

## 8. 对后续研究的影响

- 证明**电学可编程**拓扑通道（定义位置、开关）可行——valleytronics 器件化的关键一步 📜Q。
- 双分裂栅结构 → 势控少电子量子点（ref 32）、BLG QH 区域的 edge-state/domain-wall 物理（refs 31,33）📜Q。
- 给出改善弹道的明确方向：**更窄结 + 更大带隙** → $L_k$ 增（理论 + 作者展望）📜Q。

---

## 9. 理论模型映射（供 tbplas / Landauer 对标）

| 映射 | 说明 |
|------|------|
| $D\to\Delta$ | 体位移场 → 体带隙（实验"数十 meV"，理论参数 30 meV）📜Q |
| EFW 拓扑 | 反向 $D$ → $V=0$ 线 $\Omega$ 符号反转 → 每谷 2 模（×2 自旋 = 4 模/谷）→ $4e^2/h$ 💭I（[PHY-BERRY] + ref 6/8/11；原文未显式写 Chern 数） |
| $R_j=R_0(1+L/L_k)$ | Landauer–Büttiker → $L_k$ 提取 📜Q |
| 两通道模型 | 原始 $R_j$ 扣除非手征平行通道 → $R_{kink}$ 📜Q（Supp §10） |
| 无序散射 | 在位 Anderson 无序（$W$=0.6 eV）+ Green 函数 → $L_k(E_F,w,\Delta)$ 📜Q（Supp §8） |

> 与 tbplas 对应 💭I：静电 DW 可在 TB 模型用**层偏压（on-site energy offset）**构造（$D(x)$ 过零），算完整能带（核对 gap 内非手征态）+ Landauer 透射 → 提取 $L_k$；B 场用 Peierls 替换核对朗道量子化 + Lorentz 分离。$L_k$ 参数扫描（$w, \Delta, E_F$）可复现 §4.4 的单调趋势（$L_k$ 随 $\Delta$ 增、$w$ 减、$E_F$ 减而增）📜Q。

### 9.1 SI §7 能带计算细节（EFW 建模与参数，📜Q SI §7）

正文 Fig 3a 的"非手征束缚态"能带、Fig 3b 的 $L_k$ 提取，全部来自 SI §7 的紧束缚计算。SI §7 把 **EFW（电场壁）建模的完整参数链**写全，是复现其能带与 $L_k$ 的最直接依据。

**紧束缚哈密顿量（Eq. S1，π-轨道，AB 堆叠 + 层间偏置 + Anderson 无序）**：

$$H_0 = -t\sum_{\langle ij\rangle}(c_i^\dagger c_j+\mathrm{h.c.}) + t_\perp\sum_{\langle i\in T,\,j\in B\rangle}(c_i^\dagger c_j+\mathrm{h.c.}) + \sum_{i\in T}U_{\mathrm{top}}c_i^\dagger c_i - \sum_{i\in B}U_{\mathrm{bot}}c_i^\dagger c_i + \sum_i\epsilon_i c_i^\dagger c_i$$

| 项 | 含义 | 参数（📜Q） |
|----|------|------|
| 第一项 | 层内最近邻跳跃 | $t$ = **2.6 eV** |
| 第二项 | 层间最近邻跳跃（$T$=顶层、$B$=底层） | $t_\perp$ = **0.34 eV** |
| 第三/四项 | 顶/底层 on-site 能（层间势差 **$2U = U_{\mathrm{top}} - U_{\mathrm{bot}}$**，偏置区设为 $+U/-U$） | $2U$ 可调 |
| 第五项 | 在位 Anderson 无序，$\epsilon_i$ 均匀分布于 $[-W/2,\,W/2]$ | $W$ = 无序强度 |

**几何与对称性**：有限宽 $d$（$x$ 向）$+$ $y$ 向平移对称；结宽 $w$；$U(x)$ 结左侧 $+2U$、右侧 $-2U$，跨结连续变化 📜Q。$d$ = **120 nm**（远窄于真实器件，"受计算能力限制，但足以捕捉结区主要物理"）；$w$ = **70/110 nm**（device 1/2，实验值）📜Q。zigzag 与 armchair 两种取向均检验，主结果（Anderson 无序致谷间散射的电导衰减、B 场致 K/K′ 波函数分离）**对取向不敏感**，下文用 zigzag 📜Q。方法 = **精确对角化** Eq. S1 📜Q。

**三组参数扫描**（能带均只画 K 谷，K′ 对称）：

| 扫描 | 参数 | 结果（📜Q） |
|------|------|------|
| **结宽 $w$**（Fig 10） | $2U$=100 meV；$w$=0/20/40/60 nm | 体带隙 $\Delta\approx 2U$ = **100 meV**（绿虚线）；反极性配置（左 $+2U$、右 $-2U$）产生隙内**手征 kink 态**（红）；$w$↑ → 隙内**非手征束缚态**（蓝）增多（ref 9 类似）；$E_F$ 扫过隙时 kink 态可与非手征态共存 |
| **势剖面 $U(x)$**（Fig 11） | $2U$=30 meV；cosinusoidal / linear / COMSOL 三种 | 三种剖面**定性一致**（隙内现非手征态 → 有效缩小 $\Delta$；器件 2 更宽结更显著）；后续统一采用 **cosinusoidal** |
| **层间势差 $2U$**（Fig 12） | $2U$=30/100/300 meV | $U$↑ → $\Delta$↑ → **仅 kink 态存在的能量范围**↑（黄虚线）；$L_0$ 随 $\Delta$↑ 而↑（耦合非手征态减弱）→ 增大带隙可抑制 kink 背散射 |

**关键点**：

- **$\Delta \approx 2U$**：体带隙 = 层间势差（Fig 10 caption "$\Delta\sim 2U$ = 100 meV"；Fig 11/12 用 $2U$=30 meV 对应正文 Fig 3a "$\Delta$=30 meV"）→ 这是 $D\to 2U\to\Delta$ 的 TB 表示（补全 §3.2"原文未给 $D$ 公式"的缺口，锚点 [PHY-GATE]）📜Q。
- **zigzag 边缘模**（青，Fig 10）：无无序时贡献 $4e^2/h$；实验上因结边界随机原子取向可忽略 → 计算在边界 **10 原子宽条带**加**强无序 $W$=10 eV** 人为消除其电导贡献 📜Q。
- **MFP 符号**：SI §7 用 **$L_0$** 记 kink 平均自由程（正文用 $L_k$，同一量）；$L_0$ 随 $\Delta$↑ 增、随 $w$↑ 减 📜Q（与 §4.4 单调趋势一致）。
- **四 kink 模**（Fig 12d）：无自旋 π-轨道 + 双谷全带结构标出**4 条 kink 模** = 2 谷 × 2 层（无自旋）；正文 Fig 1a 补自旋后每谷 4 模（2 自旋 × 2 层）、总 8 模（见 §2.1），二者自洽 📜Q。

> **复现清单（tbplas / Landauer 对标）💭I**：层内 $t$=2.6 eV + 层间 $t_\perp$=0.34 eV + 层偏置 $U(x)$（cosinusoidal，$2U$=30/100/300 meV）+ Anderson $\epsilon_i\in[-W/2,W/2]$（正文取 $W$=0.6 eV）+ 条带 $d$=120 nm、$w$=70/110 nm + 边界 10 原子 $W$=10 eV 强无序消除 zigzag 边缘模。计算链：精确对角化出能带（核对隙内非手征态 + kink 模）→ Landauer–Büttiker（Green 函数，SI §8）透射 → $L_k$。SI §7 与 §8 合起来即"能带 → 电导 → MFP"的完整可复现管线。⚠️ **tbplas 本身无两终端 Landauer/NEGF 模块**（只有 Kubo 体电导），能力边界与替代方案见 §9.2。

### 9.2 SI §8 电导计算（可计算观测量 = 两终端电导 → $L_k$；tbplas 能力边界）

**可计算对应物理量**：SI §8 直接给出**两终端 Landauer–Büttiker 电导** $G_{LB}$（实验测的结电导 $\sigma_j=1/R_j$ 的相干极限），并从长度依赖 $G(L)$ 拟合出 MFP $L_0$（正文记 $L_k$）📜Q。

**方法（§8.1）**：Caroli/NEGF 形式

$$G_{LB}=\frac{2e^2}{h}\mathrm{Tr}\big[\Gamma_L\, G^r\, \Gamma_R\, G^a\big]$$

$G^{r(a)}$ = 中心散射区推迟（超前）Green 函数；$\Gamma_{L(R)}=i[\Sigma_{L(R)}^r-\Sigma_{L(R)}^a]$ 线宽函数，自能 $\Sigma^r$ 由**转移矩阵法**（Sancho 迭代，ref 11）求得；**每个数据点 30 个无序样本取平均** 📜Q。

**关键结果（§8.2–8.3）**：

- 固定 $W$ 下 $G(L)$ 随 $L$ 增大而减小，$W$ 越大衰减越快（Fig 13，$W$=0.1–0.7 eV）；$W$=**0.6 eV** 是为**数值匹配实验电导量级**而选定 📜Q。
- $E_F$=0/5/14 meV 的 $G(L)$（device 1 参数，正文 Fig 3b）→ 拟合 $G=G_0/(1+L/L_0)$ 得 $L_0$=**266/210/141 nm**（caption 写 223，见 §4.4 不一致标注）📜Q。
- $E_F$=14 meV（占住 1 个非手征态）时 $L=0$ 初始电导 = **$8e^2/h$**（vs 仅 kink 态 $4e^2/h$），且随 $L$ 衰减更快 → 非手征态共存增强背散射路径 📜Q。
- Supplementary Table II：$L_0$ 随 $\Delta$ 增而增；device 2（$w$=110 nm）的 $L_0$ 比 device 1（$w$=70 nm）小约 **25%** 📜Q。

**tbplas 能力边界 💭I**（据本地 checkout `tbplas-py-1a43ccb` + `tbplas-cpp-a021ca8/exp`）：

| 环节 | tbplas 是否可用 | 说明 |
|------|----------------|------|
| **SI §7 能带** | ✅ 可用 | `diag.calc_bands`（精确对角化）+ `builder`（BLG + 层偏置 $U(x)$ + Anderson 无序 + Peierls 磁场）直接复现 |
| **SI §8 两终端电导** | ❌ **无此模块** | 无 lead 自能 / recursive Green 函数 / Caroli 公式；输运工具只有 **Kubo 体电导**（`tbpm` Kubo-Bastin DC + `diag.lindhard` Kubo-Greenwood AC），是热力学极限体线性响应，**无长度依赖**，不能直接给 $L_0$ |

> **复现 $G(L)\to L_0$ 的路径 💭I**：(a) 自写 recursive Green 函数 / Sancho 自能 + Caroli 模块（tbplas 现有 `SuperCell`/`Sample` 可直接供哈密顿量）；(b) 换 **Kwant**（内置 NEGF Landauer 两终端，最直接）；(c) 用 tbplas **Kubo 体电导**作替代探针——但它是体电导 $\sigma_{2D}$，与 Li 的结电导 $G(L)$ **非同观测量**，需另行论证 $\sigma_{2D}$ 与 $L_k$ 的对应关系后方可对标。

---

## Phase S 目的接口（引用式）

- **Q1（edge state 如何表征）**：纯电学——odd/even 开/关（$\sigma_j$ 10–15 µS vs <1 µS）+ 边-体区分（$R_{bulkCNP}$>10 MΩ vs $R_j$=40–100 kΩ）+ $L_k$=70–200 nm + B 场恢复弹道（device 2 达 6.5 kΩ）——见 §2/§4。
- **Q2（理论如何解释）**：Martin 2008 EFW 方案（无新理论）；Green 函数 + Anderson 无序解释非手征态散射 → $L_k(E_F,w,\Delta)$ 📜Q。
- **Q3（理论↔实验对应）**：$D_L D_R$ 符号翻转 ↔ kink 开/关；$R_j=R_0(1+L/L_k)$ ↔ $L_k$；B 场两机制 ↔ $R_{kink}\to h/4e^2$ 📜Q。

> **增量价值**：E1–E18 中**唯一"电场壁 EFW"**实验——与 E10/E12/E14（表征天然 mTBG 畴壁网络）本质不同，本文是"**用栅压从零定义**一条拓扑通道"而非"表征已有畴壁"。report.md §2 用其判别表（odd/even 开/关 + 体 vs 结）与 §4 数字（70–200 nm / 6.5 kΩ）；§4 用"EFW vs LSW"作为通道定义方式的二分（栅编程 vs 结构畴壁）。TBPM 可对标静电 DW 的非手征态与 $L_k$ 参数扫描。

---

## 反向核对 pass (2026-09-01)

pdftotext 提取 `/tmp/e3.txt`（7 页期刊版），逐项 grep：w=70/110 nm、L=1 µm/400 nm、μ=100,000/22,000、RbulkCNP>10 MΩ、Δ "a few tens of meV"/30 meV/~21 meV、σj <1 µS/10–15 µS、Rj 40–100 kΩ、Lk 70–200 nm、R0=6.5 kΩ、8 modes/4 chiral per valley、W=0.6 eV、Lk 266/210/141、Rkink 15 kΩ@7 T、0.8 µm、4–10×、8–14 T、6–10 kΩ、14 nm、T=1.6 K/310 mK、<10 nm 对准、50 nm 分裂宽、15–30 nm hBN、5/20 5/70 nm Ti/Au —— 全部在原文找到。**无 ± 声明**（全文数字均为 =/≈/范围给出，无误差棒 → 统一 [~]）；Fig 1e Δ(D) 轴读数标 [读图]。

⚠️ 修正记录（相对旧 review）：① 删除"漏电 < pA"（原文无）；② "Δ~30 meV（实验值）"改为"实验数十 meV + 理论 30 meV"；③ 删除"变温 1.6–40 K"（原文只有 1.6 K 与 310 mK）；④ 删除未在正文出现的 $D=(D_{top}-D_{bottom})/2$ 公式（降为 [PHY-GATE] 引用）；⑤ Chern 数表述降级 💭I（原文用 Ω 符号反转、未写 Chern 数）；⑥ Fig 3 caption 223 nm 与正文 210 nm 不一致处显式标注。

## 反向核对 pass — SI §7–§8 (2026-09-03)

pdftotext 提取 `/tmp/li2016_si.txt`（SI），逐项 grep §7：$t$=2.6 eV、$t_\perp$=0.34 eV、$d$=120 nm、$w$=70/110 nm、$2U$=100 meV（Fig 10）/ 30 meV（Fig 11、12）/ 30-100-300 meV（Fig 12）、$\Delta\sim 2U$、边界 10 原子 $W$=10 eV 强无序、zigzag 边缘模 $4e^2/h$、SI 用 $L_0$（正文 $L_k$）、Fig 12d "four kink modes" —— 全部在原文找到。正文 "each valley supports four chiral modes (two ... spin ... two ... layer)"（Fig 1a）与 SI Fig 12d 无自旋 π-轨道图的 4 kink 模（2 谷 × 2 层）核对**自洽**。

§8 逐项 grep：Caroli 公式 $G_{LB}=\frac{2e^2}{h}\mathrm{Tr}[\Gamma_L G^r\Gamma_R G^a]$、转移矩阵法（Sancho 迭代）自能、每点 30 无序样本平均、$W$=0.6 eV 为匹配实验电导、$E_F$=14 meV 处 $L$=0 初始电导 $8e^2/h$、device 2 $L_0$ 小 ~25% —— 全部在原文找到。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-07-15 | 初读（基于 arXiv:1509.03912v2 39 页含 SI 版），旧 8 节格式 review |
| 2026-09-01 | **4 块新架构重读**（据 7 页期刊版正文）：旧 review 中 grep 不到的数字全部修正——"漏电 < pA"（无源）删除；"体带隙 Δ~30 meV（实验值）"→ 实验"数十 meV" + 理论 30 meV；"变温 1.6–40 K"→ 1.6 K + 310 mK；$D=(D_{top}-D_{bottom})/2$ 公式（正文未给）→ [PHY-GATE] 引用；Chern 数表述 → 💭I；补判别表/[前提与限定]/两通道模型/§4.6 证据链 |
| 2026-09-01 | **证据分级 + 不确定度轴全面启用**：所有数字标 📜Q/📊F/💭I + [~]/[读图]/[相对]；声明"全文无 ± 误差棒"；Fig 1e Δ(D) 轴读数标 [读图] |
| 2026-09-01 | **内部不一致标注**：Fig 3 caption $L_k(E_F=5\ \text{meV})$=223 nm 与正文 210 nm 不一致，正文取 210 并显式标注 |
| 2026-09-03 | **SI 补入**：下载期刊 SI PDF，精读 SI §7（能带计算），整理到 §9.1（Eq. S1 紧束缚模型 + 参数 $t$=2.6/$t_\perp$=0.34 eV + $\Delta\approx 2U$ + 三组扫描 $w$/剖面/$2U$ + 边界 $W$=10 eV 消除 zigzag 边缘模 + 复现清单）；更新头部 SI 状态与来源声明；补 SI §7 反向核对 pass |
| 2026-09-03 | **SI §8 补入 + tbplas 能力边界**：精读 SI §8（kink 态电导），整理到 §9.2（Caroli/NEGF 两终端电导 + 30 样本平均 + $G(L)\to L_0$ 提取 + $E_F$=14 meV 处 $8e^2/h$ + device 2 小 25%）；核对本地 tbplas **无两终端 Landauer/NEGF 模块**（仅 Kubo 体电导）→ 记录能力边界与 Kwant/自写模块替代方案 |
