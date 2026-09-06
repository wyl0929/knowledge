<!--
 * @Author       : AI 精读 (系统辨识式阅读法 → 三层分离整理)
 * @Date         : 2026-08-06（初读）→ 2026-09-01（4 块新架构重读）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/experiments/paper_review_E15_mahapatra2022_nanolett.md
 * @Description  : E15: Mahapatra et al. 2022 — mTBG 三角畴区 QH 干涉（磁热电 Sxx 测 FP+AB，2026-09-01 按 4 块辨识结构重读）
-->

# Paper Review: Mahapatra et al. (2022) — mTBG 三角畴区的量子霍尔干涉

| 字段 | 内容 |
|------|------|
| **编号** | E15 |
| **标题** | Quantum Hall Interferometry in Triangular Domains of Marginally Twisted Bilayer Graphene |
| **作者** | Phanibhusan S. Mahapatra, Manjari Garg, Bhaskar Ghawri, Aditya Jayaraman, Kenji Watanabe, Takashi Taniguchi, Arindam Ghosh, U. Chandni |
| **期刊** | Nano Letters 22, 5708–5714 (2022) |
| **DOI / arXiv** | 10.1021/acs.nanolett.2c00627（PDF 页脚 📜Q）/ 2112.03891（⚠️ 正文未出现，来自 registry，标外部来源） |
| **类型** | 实验 — 磁热电输运（Seebeck/磁热电功率 Sxx + 输运） |
| **课题组** | Chandni & Ghosh group (IISc Bangalore) |
| **PDF / SI PDF** | ✅ 正文 PDF（`reference/pdfs/Mahapatra 等 - 2022 - …pdf`，7 页）；❌ SI 缺失（末页 "Associated Content: Supporting Information (PDF)" 列 4 节：器件制备与表征、电/热电测量、磁热电中的 AB 振荡、磁热电中的 FP 振荡；Fig S2 的跨通道 ΔB 数据在 SI，无法核对） |
| **精读日期** | 2026-08-06（初读）→ 2026-09-01（4 块架构重读） |

> **共享知识引用**：通用物理（AB 干涉/退相干、SdH/朗道量子化、miniband、FP 维度判据、Hofstadter 标定、filling factor）已剥离到 `note/shared/physics/`，本 review 用锚点 `[PHY-AB] [PHY-FP] [PHY-SDH] [PHY-EF] [PHY-BERRY] [PHY-MB] [PHY-HOF] [PHY-GATE]` 引用，不重复讲义。阅读疑问见 `note/shared/method/mechanism_questions.md` `[METHOD-Q]`。

---

## TL;DR

**本文想解决的问题**：能否不用任何额外栅极定义架构，用 mTBG 自身重构形成的三角 AB/BA 畴区，直接做一个量子霍尔（QH）干涉仪，并在其中观测 FP + AB 干涉？

**主结果**：① 在 θ≈0.16° mTBG 的整数 QH 区间（ν=4, 8），磁热电功率 $V_{xx}^{2\omega}$ 同时出现**密度周期振荡（FP，Δn≈4×10¹⁴ m⁻²）与磁场周期振荡（AB，ΔB≈250 mT）**，且**只在热电、不在常规 Rxx** 中可见（Rxx 同区间无可识别振荡）📜Q[~]；② n-B 相空间**只有正斜率对角线**（α≈1.24×10¹⁵ m⁻² T⁻¹，谐波 2α/3α）→ 单向（chiral）QH 边缘模干涉 📜Q[~]；③ **ΔB 不随 ν 变**（≈250 mT）→ Coulomb 充电效应被抑制，是相对 GaAs 干涉仪的核心优势 📜Q[~]。

**结论/意义**：干涉面积内禀于 moiré 三角畴（$A_{loop}\approx2A_{moiré}$、Δn≈n_s、跨通道 ΔB 不变），"intrinsic quantum Hall interference effect in mtBLG **may act as** a novel platform for realizing anyonic statistics in the fractional QH regime"（作者措辞 may，非已实现）📜Q。

---

## 1. 系统辨识导览（判别表为全文唯一权威）

**黑箱三要素**：`{输入旋钮: Vtg / B / 加热电流 Iω | 输出观测量: Rxx, Rxy, Vxx^2ω, γ | 声称结论: 三角畴内禀 QH 干涉、充电抑制}`

**四层变量图**（符号层一次钉死）：

| 层 | Mahapatra 2022 实例 |
|----|-------------|
| **L1 旋钮 u** | $V_{tg}$（顶栅→密度）、$B$、加热电流 $I_\omega$（→ΔT）、$T$（固定 3 K） |
| **L2 导出量 x₁** | $n$（由 $V_{tg}$ 经 $C_{hBN}$）、$\Delta T$、$E_F$、$\nu=n\Phi_0/B$（$\Phi_0=h/e$） |
| **L3 模型量 x₂** | $\lambda$、$A_{moiré}$、$A_{loop}$、$L_{tot}$、$N_{ch}=2\sqrt3/\lambda$（边缘通道线密度）、$n_{QH}$（1D 线密度）、$L_{cav}$、$r_c$ |
| **固定参数（非旋钮）** | $\theta\approx0.16°$、$\lambda\approx92$ nm、$n_s=5\times10^{14}$ m⁻²（第一 moiré 带满填充，空穴侧） |
| **反推量** | $A_{loop}$（由 $\Delta B=\Phi_0/A$）、$L_{tot}$（由 α 与 $A_{loop}$）、$A_{moiré}=(\sqrt3/2)\lambda^2$（推导） |
| **L4 观测量 y** | $R_{xx}$、$R_{xy}$、$V_{xx}^{2\omega}$、$\gamma=(1/R_{xx})dR_{xx}/dV_{tg}$ |

> 与 E12 符号差异：E12 测 $\rho_{xx}$/$\rho_{xy}$/导数，双栅独立调 n 与 D；本文是**单顶栅**（无位移场独立控制，D<0.1 V/nm）、主观测量是**热电二次谐波 $V_{xx}^{2\omega}$**，$R_{xx}$ 只作对照。

**可辨识性判别表**（唯一权威；本文八条判据）：

| 判别 | 判据（数据） | 排除谁 | 确立谁 |
|------|-------------|--------|--------|
| **热电 vs 电导** | $V_{xx}^{2\omega}$ 振荡在 ν=4 显著，同区间 Rxx **无可识别振荡**（Fig 2b 右轴）📜Q | 电荷流主导的常规输运振荡（信号被 Rxx 背景淹没） | 熵流（quasiparticle 激发携带）是干涉信号通道 |
| **AB vs SdH** | 振荡**在 B 轴周期**（ΔB≈250 mT 恒定，Fig 2f），非 SdH 的 1/B 周期；且对 ±B **对称**（Fig 2d）📜Q | SdH（2D 朗道量子化）；接触/加热器/Hall 杂散信号（±B 对称排除） | AB 干涉（闭合磁通）——判据逻辑见 [PHY-SDH] |
| **QH vs QVH（谷极化手征通道）** | 位移场 **<0.1 V/nm** 不足以在 AB/BA 开隙（QVH 畴壁态需位移场开隙）；振荡只在 ν=4,8 的 QH 区间出现 📜Q | 谷极化手征（QVH）通道 | QH 局域朗道能级干涉——见 [PHY-BERRY] |
| **1D vs 2D** | n-B 相空间对角线**线性**（kF∼nQH∼n），非 2D 的 √n 抛物线；$r_c\approx9$ nm@8 T < λ → 2D √n 关系失效 📜Q | 2D 体载流子干涉 | 1D 边缘通道运动——见 [PHY-FP]/[PHY-SDH] |
| **无充电 vs 充电** | ΔB≈250 mT **不随 ν 变**（充电效应会使 ΔB 随 ν 增大）📜Q | 强 Coulomb 充电（GaAs 型受限干涉仪） | 充电效应被抑制（扩展波函数） |
| **面积来源（内禀 vs 版图/非均匀）** | ΔB≈240 mT 在下一相邻通道（相似 θ、相似长度）**不变** → 仅依赖扭角；$A_{loop}=2A_{moiré}$；Δn≈n_s 📜Q | 版图定义通道面积、扭角非均匀、体平行输运 | 干涉面积内禀于 moiré 三角畴结构 |
| **chiral 单向 vs 双向** | n-B 相空间**只有正斜率**（负斜率缺失），ν=−4 负场仍正斜率；正斜率同 CNP 朗道扇 📜Q | 双向（顺/逆时针）传播 | 单向（chiral）QH 边缘模干涉 |
| **谐波归属** | 斜率 α/2α/3α → 同一干涉面积、不同路径长度；每 AA 节点 3 进 3 出 → 不同 $L_{tot}$ 围同一面积 📜Q | 其他面积/几何 | 高次谐波（路径长度不同） |

> **主结果 ↔ 判别表映射**：
> - 主结果① 磁热电 FP+AB 双周期、只热电不电导 ← {热电 vs 电导}
> - 主结果② QH（非 QVH）边缘模干涉、单向 ← {AB vs SdH, QH vs QVH, chiral 单向}
> - 主结果③ 无栅极架构 + 充电抑制 ← {无充电 vs 充电}
> - 主结果④ 干涉面积内禀 moiré（Aloop=2Amoiré、Δn≈ns、跨通道不变）← {面积来源, 1D vs 2D, 谐波}
>
> **分层排除注**：①「热电 vs 电导」先证信号在熵流通道（必要条件）；②「AB vs SdH」+「QH vs QVH」证干涉来自 QH 局域朗道能级（非 SdH、非谷极化）；③「1D vs 2D」+「chiral 单向」证 1D 手征边缘模；④「面积来源」+「谐波」证几何内禀于 moiré 畴。作者措辞 "consistent with"（一致，非"证明"）贯穿正文——FP/AB 均为"与……一致"的定性确认 📜Q。

> **[前提与限定]**（判别结论的适用范围）：
> - **噪声/扰动**：热电信号为二次谐波锁相（$V_{xx}^{2\omega}\propto I_\omega^2$ 验证线性响应），但**背景绝对值未给**（只能引相对周期量与斜率）；Mott 公式失效（作者推测 vHS+Umklapp 散射，**相关效应"cannot be entirely ruled out"** 📜Q）；SI 缺失 → Fig S2 跨通道 ΔB 无法核对。
> - **判别性扫轴**：扫 n（密度轴，Fig 2b/c）、扫 B（磁轴，Fig 2d-f）、n-B 二维相空间（Fig 3）；B 上限约 9 T（ν=4 数据在 8 T、次朗道序列 B≳5 T）；T 固定 3 K（**无变温数据**）。
> - **候选集 M 边界**：{电荷流干涉, SdH, QVH 畴壁态, 2D 体干涉, Coulomb 充电, 版图/非均匀来源} —— "QH 边缘模干涉"在该集合内唯一幸存；集合之外候选（如 phonon drag 等其他热电来源）原文**未讨论、未排除**（封闭世界假设风险 💭I）。

三层标注：📜Q = 原文事实（附位置）｜推导｜📊F = 读图估算｜💭I = 推断。**不确定度（正交轴）**：[±] 原文误差棒 / [~] 原文无误差棒 / [读图] 图提取·色标值 / [相对] 仅相对量。所有数字经 pdftotext + grep 反向核对。

---

## 2. 结果与机制（按论文自身论证：标定/热电背景 → FP → AB → 相空间 → 机制图景）

### 2.1 器件标定与热电测量背景

- **扭角/几何标定**：由 3 K 下 dRxx/dn 的 Hofstadter 蝶形图 + n_s 提取 📜Q。主朗道能级从 CNP（n=0）扇出，空穴侧从 $n_s=5\times10^{14}$ m⁻² 扇出第二组朗道能级（对应第一 moiré 带满填充）→ λ≈92 nm、θ≈0.16° 📜Q[~]。主序列 ν=±4, ±8, ±12；次序列 ν=±1, ±2（B≳5 T，高场自旋/谷简并解除）📜Q。标定逻辑见 [PHY-HOF]/[PHY-EF]。
- **热电测量**：扩展单层区局域焦耳加热（正弦电流 $I_\omega$ → ΔT 沿通道），在 Hall bar 的 tBLG 区记录二次谐波热电电压 $V_{xx}^{2\omega}$；线性响应（ΔT≪T）由 $V_{xx}^{2\omega}\propto I_\omega^2$ 验证 📜Q。
- **$V_{xx}^{2\omega}(n)$ 多次符号反转**：CNP 两侧近对称反转 = 最低导/价带 vHS 位置；空穴侧额外反转 = 最低价带满填充 📜Q。Rxy（800 mT）只在 CNP 反转一次 → 第一 miniband 无 Rxx 峰（低能大量重叠带）📜Q。
- **Mott 公式失效**：$S_{Mott}=\frac{\pi^2k_B^2T}{3|e|}\cdot\frac{1}{R_{xx}}\frac{dR_{xx}}{dV_{tg}}\frac{dV_{tg}}{dn}\frac{dn}{dE}|_{E_F}$（eq 1），其中 $\gamma=(1/R_{xx})dR_{xx}/dV_{tg}$ 可测、$dV_{tg}/dn=e/C_{hBN}$ 📜Q。$\gamma$ 只在 CNP 反转一次，**无法复现** $V_{xx}^{2\omega}$ 的多次反转，且 DOS 不能补偿 📜Q。作者推测：mtBLG DOS 中大量 vHS → 费米面小部分满足 Umklapp 条件 → 强各向异性散射 → Mott 失效；**相关效应不能排除** 📜Q（推测）。

### 2.2 FP 密度振荡（QH 区间）

ν=4 时 $V_{xx}^{2\omega}$ 随 n 强振荡（Fig 2b），**周期 Δn≈4×10¹⁴ m⁻² 不随 B 明显变化**（固定 ν）；ν=8 时 Δn≈5×10¹⁴ m⁻² → **Δn 与 ν、B 均无关** 📜Q[~]。机制 = 2D 体系 FP 干涉的量子版（腔由外部栅极定义，refs 15,28,38）；干涉相位 $\phi_\epsilon=L_{tot}k_F/2\pi$（$L_{tot}=2L_{cav}$ 路径差），由 $E_F$ 调制 $k_F$ 📜Q。关键发现：**Δn 与 n_s 同量级** → 干涉路径差远小于版图定义通道面积（~few μm²）、与 moiré 晶格尺度可比 📜Q。

> 洛伦兹力限定（作者自证 1D）：观测相位调制需回旋半径 $r_c=\hbar k_F/eB>L_{cav}$；作者用 2D 关系 $k_F=\sqrt{\pi n}$ 估 $r_c\approx9$ nm@8 T < λ → **2D √n 关系对参与干涉的载流子失效** → 约束运动 → 有效 1D（QH 边缘通道，不再随 B 增而变）📜Q[~]。维度判据见 [PHY-FP]。

### 2.3 AB 磁振荡

固定 n 扫 B（Fig 2d: n=1.55×10¹⁵、Fig 2e: n=7.75×10¹⁵ m⁻²），$V_{xx}^{2\omega}$ 振荡**在 B 轴周期**（Fig 2f，ΔB≈250 mT），**非 1/B 周期** → 排除 SdH、与 AB 一致 📜Q[~]。两条重要排除 📜Q：
1. **对 ±B 对称** → 排除接触、单层加热器杂散信号、横向 Hall 分量。
2. **只在 ν=4,8 出现、更高朗道能级消失** → 因 ν>8 朗道谱弱、能隙在 n/B 实验范围内不可分辨（Rxx 与 V2ω 均无）；干涉与 QH 态形成深度关联。对比：位移场驱动的螺旋态 AB 振荡在极低场出现、高场消失（ref 28）📜Q。
- **充电判据**：受限 QH 干涉仪中 Δν↔充电能，增强的 Coulomb 相互作用使有效面积收缩 → AB 周期增大（refs 13,38,41）；本文 ΔB≈250 mT **不随 ν 变** → 充电效应被抑制 📜Q[~]。
- **面积反推**：由 $\phi_{AB}=BA_{loop}/\Phi_0$ → $A_{loop}\approx1.6\times10^{-14}$ m² = **恰好 2 倍 moiré 单胞面积**，与 Fig 2b 密度振荡互证 📜Q[~]（⚠️ 原文印刷 "m⁻²"，面积量纲应为 m²，疑为出版笔误）。
- **跨通道**：下一相邻通道（相似 θ、相似长度）ΔB≈240 mT 不变 → ΔB 只依赖扭角（moiré 晶格尺寸）→ 干涉面积内禀于三角畴结构，非扭角非均匀/体平行输运（Fig S2，SI）📜Q[~]。

### 2.4 n-B 相空间（chiral 单向 + 谐波）

Fig 3a/b 为 $|ν|=4$ 的 $V_{xx}^{2\omega}$ 色图，干涉相位的极大/极小呈**对角斜线**。总相位累积指数 $j=L_{tot}k_F/2\pi \pm A_{loop}B/\Phi_0$（eq 2，± 号 = 顺/逆时针环绕）📜Q。观察要点 📜Q：
1. **只有正斜率**（负斜率缺失），ν=−4 负场下仍正斜率；正斜率同 CNP 朗道扇 → 载流子**只允许单向运动**，与 QH 态干涉特征一致。
2. 主斜率 α≈1.24×10¹⁵ m⁻² T⁻¹（黑），弱斜线 2α（蓝）/3α（粉）= **同一干涉面积、不同路径长度的高次谐波** 📜Q[~]。
3. 变 $V_{tg}$ 只改 $n(E_F)$、**不改干涉面积** → 与石墨烯/GaAs 栅定义 QH 干涉仪（面积随栅变）本质不同 📜Q。

### 2.5 机制图景（畴壁=边缘、AA 节点=hopping）

作者提出的微观图景 📜Q：QH 区间载流子轨迹受 B 与 moiré 晶格双重影响；畴壁分离三角 AB/BA 畴 → **QH 手征通道沿畴壁出现**（畴壁充当 QH 区的"样品边缘"，畴内形成局域朗道能级，Fig 4a）；AA 区充当**节点**，令相邻畴的局域手征边缘通道间隧穿/hopping → 传播模可携带电荷与热 → 围磁通时产生 FP/AB 干涉（Fig 4b）。⚠️ 与谷极化手征通道**定性不同**：后者只在 $E_F$ 落在位移场能隙内时出现，前者依赖畴内局域朗道能级形成 📜Q。

**充电抑制的机制**：任一 AA 区都可 hopping → 大量可能传播模 → 波函数**扩展**；相对 GaAs 小面积干涉仪（只能容纳有限电荷、受限主导）→ 扩展波函数 → 载流子间 Coulomb 排斥减弱（即便赝朗道能级畴内局域）；且只有 AA 区供 hopping → 总散射截面大幅减小 → 传播模在样品尺度保持相位相干 📜Q（postulate）。

**Ltot 与 1D 标度**：n-B 对角线对 n、B **线性** → QH 区 $k_F\sim n_{QH}$（1D 线密度）→ 1D 运动（对比 2D 的 √n）📜Q。$n_{QH}=n/N_{ch}$，$N_{ch}=2\sqrt3/\lambda$（边缘通道线密度，见 SI）📜Q。代入 eq 2 得 $L_{tot}$ 与 $A_{loop}$、简并度 g 的关系（原文式 $L_{tot}=A_{loop}\cdot2\sqrt3\cdot g/\Phi_0$，⚠️ pdftotext 丢失 √ 与 $\Phi_0$ 符号、因子未经 SI 复核）；由实测 α 与 $A_{loop}$ → **$L_{tot}\approx450$ nm ≈ 4λ** 📜Q[~]。但 4λ 太短围不出 $A_{loop}$（最小三角路径 6λ）→ 矛盾 → 解释：栅压载流子**非全部**进 1D（nQH 被高估 → $L_{tot}$ 被低估）；$A_{loop}\approx2A_{moiré}$ 对应围住四畴的有效轨迹，具体路径可多几何 📜Q。每 AA 节点可 3 进 3 出 → 不同 $L_{tot}$ 围同一面积 → 多谐波斜率 📜Q。

---

## 3. 实验方法

### 3.1 器件
mtBLG Hall bar（θ≈0.16°）+ 扩展单层区局域焦耳加热器；hBN 封装（K.W./T.T. 合成 hBN 单晶）📜Q。制备细节在 SI（缺失，无法核对）。

### 3.2 静电学
单顶栅（$C_{hBN}$ 顶栅电容/面积，$dV_{tg}/dn=e/C_{hBN}$）；无位移场独立控制（"negligible displacement fields"、D<0.1 V/nm 不足以开隙）📜Q。$\nu=n\Phi_0/B$（$\Phi_0=h/e$）📜Q。静电学通用推导见 [PHY-GATE]。

### 3.3 测量
局域焦耳加热（正弦 $I_\omega$ → ΔT → $V^{2\omega}$ 二次谐波锁相）；测量温度 3 K；$V_{xx}^{2\omega}\propto I_\omega^2$ 验证线性响应（ΔT≪T）📜Q。观测量 Rxx（四端）、Rxy（Hall，800 mT）、$V_{xx}^{2\omega}$。非常规点：**热电二次谐波作主信号、Rxx 只作对照**（Mott 分析用 $\gamma=(1/R_{xx})dR_{xx}/dV_{tg}$）📜Q。去背景/FFT 细节与 Fig S2 数据在 SI（缺失）。

---

## 4. 关键数据

### 4.1 几何与标定
| 参数 | 值 | 等级 |
|------|-----|------|
| θ | ≈0.16°（Hofstadter 蝶形图 + n_s 双法）📜Q | [~] |
| λ | ≈92 nm（由 n_s 推）📜Q | [~] |
| n_s | 5×10¹⁴ m⁻²（第一 moiré 带满填充，空穴侧）📜Q | [~] |
| $A_{moiré}$ | $(\sqrt3/2)\lambda^2\approx7.3\times10^{-15}$ m²（系数见正文 "(√3/2)"，数值为推导） | 推导 |

### 4.2 朗道序列
主序列（CNP）ν=±4, ±8, ±12；次序列（n_s）ν=±1, ±2（B≳5 T，高场自旋/谷简并解除）📜Q。

### 4.3 FP 密度振荡
| 参数 | 值 | 等级 |
|------|-----|------|
| Δn（ν=4） | ≈4×10¹⁴ m⁻² | 📜Q[~] |
| Δn（ν=8） | ≈5×10¹⁴ m⁻² | 📜Q[~] |
| Δn 对 ν、B | 无关 | 📜Q |
| Δn vs n_s | Δn≈n_s（同量级） | 📜Q |

### 4.4 AB 磁振荡
| 参数 | 值 | 等级 |
|------|-----|------|
| ΔB（与 ν 无关） | ≈250 mT | 📜Q[~] |
| ΔB（相邻通道） | ≈240 mT（Fig S2，SI 缺失） | 📜Q[~] |
| $A_{loop}$ | ≈1.6×10⁻¹⁴ m² = 2$A_{moiré}$（"exactly twice"） | 📜Q[~] |
| B 周期 vs 1/B | B 周期（非 SdH） | 📜Q |
| ±B 对称 | 对称（排除接触/加热器/Hall） | 📜Q |
| 出现区间 | 只 ν=4,8，更高朗道能级消失 | 📜Q |
| 掺杂点（Fig 2d/e） | n=1.55×10¹⁵ / 7.75×10¹⁵ m⁻² | 📜Q |

### 4.5 n-B 相空间
| 参数 | 值 | 等级 |
|------|-----|------|
| 主斜率 α | ≈1.24×10¹⁵ m⁻² T⁻¹ | 📜Q[~] |
| 谐波斜率 | 2α（蓝）、3α（粉） | 📜Q |
| 斜率符号 | 只正（ν=±4 均正） | 📜Q |
| $r_c$ | ≈9 nm@8 T（$k_F=\sqrt{\pi n}$ 2D 关系） | 📜Q[~] |
| D 场 | <0.1 V/nm（不足以开隙） | 📜Q |

### 4.6 机制反推
| 参数 | 值 | 等级 |
|------|-----|------|
| $N_{ch}$ | $2\sqrt3/\lambda$（边缘通道线密度） | 📜Q（√/λ 符号恢复） |
| $n_{QH}$ | $=n/N_{ch}$ | 📜Q |
| $L_{tot}$ | ≈450 nm ≈ 4λ（由 α 与 $A_{loop}$） | 📜Q[~] |
| 最小围面积路径 | 6λ（三角有效面积） | 📜Q |
| AA 节点通道数 | 3 进 3 出 | 📜Q |

### 4.7 证据链与论证结构
**三支柱**：① 热电通道（熵流）承载干涉信号（§2.1/2.3）；② FP+AB 双周期（§2.2/2.3）；③ 面积内禀 moiré + 充电抑制（§2.3/2.5）。**双轴判别**：密度轴（Δn≈n_s、Δn 与 B/ν 无关）与磁轴（B 周期非 1/B、±B 对称、只 ν=4,8）各排除一次体/SdH/QVH 解释。**交叉验证**：ΔB→$A_{loop}$=1.6×10⁻¹⁴ 与 "$A_{loop}=2A_{moiré}$" 互验；$L_{tot}$≈4λ 与最小围面积 6λ 的**矛盾被作者显式指出**并以"部分载流子进 1D"化解 📜Q。**完整认定链**：熵流通道存在 → AB（非 SdH）+ QH（非 QVH）→ 1D 手征 + 面积内禀 → 充电抑制 = "内禀 QH 干涉仪"的完整可辨识。

---

## 5. 主要结论
1. 磁热电功率在 n 与 B 两轴都出现周期振荡，与电子 FP 与 AB 干涉一致（3 K、闭合磁通）📜Q。
2. 振荡**只在热电、不在常规电阻**中可见 📜Q。
3. 共振只在 QH 区间 ν=4,8 出现，且贯穿器件不同通道 📜Q。
4. 由 AB 周期反推的闭合回路面积与 moiré 晶格尺寸可比（=2$A_{moiré}$）📜Q。
5. 载流子在 AB/BA 畴内形成局域朗道能级，相邻 QH 模经 AA 区干涉；充电效应被抑制 📜Q。
6. 作者保守表态："intrinsic QH interference **may act as** a novel platform for realizing anyonic statistics"（may，非已实现）📜Q。

## 6. 局限与未解决
| 局限 | 说明 | 证据 |
|------|------|------|
| 熵流机制不明 | AA 节点为何作为可压缩区偏袒熵流、具体机制"not clear at present" | 📜Q |
| Mott 失效解释为推测 | vHS+Umklapp 散射；相关效应"cannot be entirely ruled out" | 📜Q |
| 仅整数 QH | 尚未推进到分数 QH（ν=1/3 等）| 📜Q→💭I |
| 无变温 | 仅 3 K 数据，退相干温度依赖未知 | 📜Q |
| Ltot 反推矛盾 | 4λ vs 最小 6λ 靠"部分载流子进 1D"化解，非定量自洽 | 📜Q |
| SI 缺失 | Fig S2（ΔB≈240 mT 跨通道）与制备/测量细节无法核对 | ⚠️ 本笔记标注 |
| 无实空间成像 | 路径几何靠输运反推（多几何并存） | 💭I |

## 7. 与其他工作的关系
| 工作 | 关系 |
|------|------|
| San-Jose & Prada 2013 (ref 24) / Efimkin & MacDonald 2018 (ref 25) / Walet & Guinea 2020 (ref 26) | 位移场开隙后畴壁螺旋 1D 网络的来源 📜Q |
| Xu 2019 (ref 27) / Rickhaus 2018 (ref 28) | 螺旋 1D 网络的 AB 振荡（但体被耗尽、对 QH 不敏感）；本文在 QH 区间、无位移场 📜Q |
| De Beule 2020 (ref 44) + Tsim 2020 (ref 46) + Ramires & Lado 2018 (ref 45) | 大位移场下 zigzag 通道 + 赝朗道能级图景（本文机制的类比源）📜Q |
| Ronen 2021 (ref 15) / GaAs (refs 3,13,38,41) | 石墨烯/GaAs 栅定义 QH 干涉仪——本文**无需栅极架构**且面积不随栅变，对比基准 📜Q |
| Huang 2018 (ref 23) / Yoo 2019 (ref 22) | STM 螺旋态 / 重构结构基础（间接）📜Q |

> ⚠️ Phase S 外部对标（非本文引用）：Barrier 2024 Nature（QH+超导畴壁）是**后续**工作，本文是其方向前驱 💭I（cards.md 交叉）。

## 8. 对后续研究的影响
- 提出**无需栅极架构的内禀 QH 干涉仪**范式（三角畴 = 天然干涉腔 + 畴壁 = 边缘 + AA = 节点）📜Q。
- **充电抑制**（ΔB 不随 ν 变）是 mtBLG 干涉仪相对 GaAs 的核心优势 → 对分数 QH 任意子编织统计极具吸引力 📜Q。
- 热电测量作为 QH 干涉的**新探测通道**（Rxx 不可见的振荡）📜Q。
- 留下任务：熵流机制定量化、Mott 失效理论、Ltot 反推矛盾的严格处理、推进到分数 QH 💭I。

## 9. 理论模型映射（供 tbplas / 有限器件对照）
| 映射 | 说明 |
|------|------|
| $\theta\to\lambda\to A_{moiré}$ | θ≈0.16°→λ≈92 nm→$A_{moiré}=(\sqrt3/2)\lambda^2$（推导）📜Q |
| $\Delta B=\Phi_0/A_{loop}$ | AB 周期↔闭合回路面积（$A_{loop}=2A_{moiré}$）📜Q |
| $N_{ch}=2\sqrt3/\lambda$ | 边缘通道线密度→$n_{QH}=n/N_{ch}$（1D 换算）📜Q |
| $k_F\sim n_{QH}$ | QH 区 1D 线性标度（判 1D vs 2D）📜Q |
| $j=L_{tot}k_F/2\pi\pm A_{loop}B/\Phi_0$ | 统一玻尔-索末菲干涉条件（密度轴 FP / 磁轴 AB）📜Q |

> 与 TBPM/Kubo 对应：AB/FP 是**有限尺寸相干效应**，bulk σxx 只给背景；复现"畴壁=边缘 + AA=hopping + 局部朗道能级"需有限器件 Landauer/Fisher-Lee 或畴壁网络散射模型（De Beule 2020 ref 44 是最近的类比框架）💭I。

---

## Phase S 目的接口（三问引用式）

- **Q1（edge state 如何表征）**：磁热电功率 $S_{xx}$（$V_{xx}^{2\omega}$）在 QH 区间测畴壁网络 FP（密度）+ AB（磁场）干涉；边-体区分靠"振荡只在 QH 边缘通道、Rxx 体背景不可见 + D<0.1 V/nm 未开隙排除 QVH"——详见 §2/§4。
- **Q2（理论如何复现）**：无新理论；De Beule 2020 散射框架（ref 44）+ 局部朗道能级/AA hopping 图景（Fig 4）📜Q。
- **Q3（理论↔实验对应）**：$\Delta B=\Phi_0/A_{loop}\leftrightarrow$250 mT；$A_{loop}=2A_{moiré}\leftrightarrow$1.6×10⁻¹⁴ m²；Δn≈n_s↔4×10¹⁴ m⁻²；$N_{ch}=2\sqrt3/\lambda$、$n_{QH}=n/N_{ch}$↔Ltot≈450 nm（推导）📜Q。

> **增量价值**：与 E10/E12（位移场驱动、低场 QVH 畴壁态）**分工互补**——本文把畴壁干涉推进到 **QH 区间（ν=4,8）、无位移场**，且用**热电**而非电导探测；比 E12 多的维度 = QH 手征单向判别 + 充电抑制判据，少的 = 密度谱学（miniband/Hall 反号）与实空间信息。report.md §2 用其判别表与 §4 数字；§4 用 $\Delta B=\Phi_0/A_{loop}$、$A_{loop}=2A_{moiré}$ 与充电抑制（ΔB 与 ν 无关）。

## 反向核对 pass (2026-09-01)
pdftotext -layout 提取正文（7 页，SI 缺失），逐项 grep 核对：θ≈0.16°、λ≈92 nm、n_s=5×10¹⁴、Δn≈4/5×10¹⁴、ΔB≈250/240 mT、$A_{loop}$≈1.6×10⁻¹⁴、α≈1.24×10¹⁵、2α/3α、$r_c$≈9 nm@8 T、D<0.1 V/nm、Ltot≈450 nm≈4λ、6λ、3 进 3 出、ν=±4,±8,±12 / ±1,±2（B≳5 T）、3 K、Rxy 800 mT、n=1.55/7.75×10¹⁵、$V_{xx}^{2\omega}\propto I_\omega^2$、Mott eq 1、γ、$C_{hBN}$、四电子/单胞、θm=1.1° —— 全部在原文找到。⚠️ 三处标注：① 原文印刷 "$A_{loop}\approx1.6\times10^{-14}$ m⁻²"（面积量纲应为 m²，疑出版笔误，正文已注明）；② $N_{ch}=2\sqrt3/\lambda$、$L_{tot}=A_{loop}\cdot2\sqrt3\cdot g/\Phi_0$ 的 √ 与 $\Phi_0$ 符号被 pdftotext 丢失（正文已标"符号恢复"）；③ ΔB≈240 mT 与 $N_{ch}$ 出处为 SI（Fig S2 / "see Supporting Information"），SI 缺失无法逐字核对，已标注。

## 更正日志
| 日期 | 条目 |
|------|------|
| 2026-08-06 | 初读，旧格式（核心贡献/机制/方法/数据/结论/局限/关系/影响 8 节 + Phase S 补充） |
| 2026-09-01 | **按 4 块新架构整体重写**（TL;DR 问题句式 + 判别表 + 结果机制 + 数据提取链 + 三问接口 + 反向核对）；全文 📜Q/推导/💭I 分级 + 不确定度标注；对齐 `_task_reread_spec.md` 与 E12 canonical |
| 2026-09-01 | **判别表新增 8 条**（热电 vs 电导、AB vs SdH、QH vs QVH、1D vs 2D、无充电 vs 充电、面积来源、chiral 单向、谐波归属）+ 主结果↔判别表映射 + [前提与限定]（M 边界含 phonon drag 未排除 💭I） |
| 2026-09-01 | **两处旧版修正**：① 旧版"ΔB（ν=4/8）≈250 mT（相同）"→ 精确为"ΔB≈250 mT 与 ν 无关 + 相邻通道 ≈240 mT"（原文未分别给出 ν=8 独立值）；② 旧版"△B 精确 2 倍"与 "Ltot/6λ 矛盾"未记 → 补 §4.6 机制反推（Ltot≈450 nm≈4λ 与最小 6λ 的显式矛盾 + 作者化解） |
| 2026-09-01 | **三处 QC 标注**：$A_{loop}$ 出版量纲笔误（m⁻²→m²）、√/Φ0 符号 OCR 丢失、ΔB≈240 mT 与 $N_{ch}$ 依赖缺失 SI（Fig S2）无法核对 |
