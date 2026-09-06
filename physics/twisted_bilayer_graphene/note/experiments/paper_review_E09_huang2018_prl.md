<!--
 * @Author       : AI 精读 (paper-reading SKILL → 系统辨识式阅读法 + 三层分离 + QC v1.1)
 * @Date         : 2026-08-06（初读，8 节版，已归档 archive/）→ 2026-09-01（含 SI 精读 + 4 块模板重写）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/experiments/paper_review_E09_huang2018_prl.md
 * @Description  : E9: Huang et al. 2018 — mTBG 畴壁拓扑保护螺旋态的 STM/STS 发现（正文 + SI 全读）
-->

# Paper Review: Huang et al. (2018) — mTBG 畴壁拓扑保护螺旋态的 STM 发现

| 字段 | 内容 |
|------|------|
| **编号** | E9 |
| **标题** | Topologically Protected Helical States in Minimally Twisted Bilayer Graphene（SI 题作 "Emergence of Topologically Protected Helical States in Minimally Twisted Bilayer Graphene"）📜Q |
| **作者** | Shengqiang Huang, Kyounghwan Kim, Dmitry K. Efimkin, Timothy Lovorn, Takashi Taniguchi, Kenji Watanabe, Allan H. MacDonald, Emanuel Tutuc, Brian J. LeRoy |
| **期刊** | PRL 121, 037702 (2018) |
| **DOI / arXiv** | 10.1103/PhysRevLett.121.037702 / 1802.02999 |
| **类型** | 实验 — STM/STS（局域谱学，无输运） |
| **课题组** | LeRoy group (Univ. Arizona) + MacDonald theory (UT Austin) |
| **PDF / SI PDF** | ✅ `reference/pdfs/Huang 等 - 2018 - ...pdf`（正文 6 页）+ `reference/pdfs/Supplementary_PRL.pdf`（SI 12 页） |
| **精读日期** | 2026-08-06（初读）→ 2026-09-01（含 SI 精读 + 4 块模板重写） |

> **共享知识引用**：通用物理已剥离到 `note/shared/physics/`，本 review 用锚点 `[PHY-BERRY]`（valley Chern / QVH 畴壁态 / chiral vs helical）、`[PHY-GATE]`（栅压 → 电场，STM 针尖不能独立调 n/D）、`[PHY-QPI]`（FT-STS 准粒子干涉色散提取）引用，不重复讲义。阅读疑问见 `note/shared/method/mechanism_questions.md` `[METHOD-Q]`。

---

## TL;DR

**本文想解决的问题**：极小扭角双层石墨烯（mTBG）在垂直电场使 AB/BA 畴区开隙后，AB/BA 畴壁网络上是否出现**拓扑保护螺旋态（TPH states）**，且能否用可控扭角制造这种畴壁网络？

**主结果**：① **首次直接观测**到 mTBG 畴壁网络上的 TPH 态——畴壁处隙内 LDOS 增强，呈**双线（double-line）空间分布**，且**仅在 AB/BA 区被电场开隙时出现** 📜Q（摘要 + Fig. 3）；② 畴壁高能 ±250 meV 增强（van Hove）是畴壁带结构、**非 TPH**（SI Fig. S4：单线、无电场时仍在）；③ 用同源石墨烯 sequential pickup 制备出 λ>50 nm 的"设计莫尔晶体"（主样品 λ=57.6±0.7 nm，θ=0.245±0.003°）📜Q。

**结论/意义**：作者用 "demonstrate the emergence of TPH states"（demonstrate，非 prove）📜Q；畴壁长度由扭角决定（制备时可控）→"可设计的拓扑通道网络"📜Q。⚠️ **注意**：拓扑保护本身靠理论一致 + 形态学（双线 + 电场开关），**未直接测谷保护**（无 intervalley 散射实验）💭I。

---

## 1. 系统辨识导览（判别表为全文唯一权威）

**黑箱三要素**：`{输入旋钮：背栅 Vg、样品偏压 Vb、针尖位置、隧穿电流 | 输出观测量：dI/dV/(I/V) 谱、LDOS 空间图、对比度 C、FT-STS 色散 | 声称结论：畴壁上出现 TPH 态，仅在 AB/BA 开隙时出现}`

**四层变量图**（符号层一次钉死）：

| 层 | 本文实例 |
|----|----------|
| **L1 旋钮 u** | $V_g$（硅背栅）、$V_b$（样品偏压/tip bias）、隧穿电流 I（200 pA 稳定）、针尖位置（AB/BA/AA/畴壁） |
| **L2 导出量 x₁** | 电荷密度 n、层间破反演电场（三贡献：背栅 + tip bias + 功函数失配 📜Q）；$2u$（Dirac 点劈裂，由电场产生） |
| **L3 模型量 x₂** | 能隙 $\Delta$、网络能标 $E_\lambda=2\pi\hbar v/3\lambda\approx 24$ meV、畴壁带鞍点 $E\approx\pm 250$ meV（SI: ±256 meV）、$w$（层间杂化参数） |
| **固定参数（非旋钮）** | $\theta$、$\lambda=a/[2\sin(\theta/2)]$（同源拾取 → 晶格取向一致，θ 由旋转角直接定 📜Q）、$\gamma_1$（层间耦合，第二子带 onset）、$a_0$、$k_D=4\pi/3a_0$ |
| **反推量 θ̂** | $\Delta(V_g)$（gap 提取见 SI §EXTRACTION）、$E_c$（导带边，FT-STS 色散拟合）、$m^*$（有效质量）、$w$、$E_0$（能量偏移）、对比度 C |
| **L4 观测量 y** | 形貌 Z(x,y)、$dI/dV/(I/V)$ 归一化微分电导谱、LDOS 空间图、对比度 $C=[I(DW)-I(AB)]/I(AB)$、FT-STS 波矢谱（q 空间盘半径） |

**可辨识性判别表**（唯一权威）：

| 判别 | 判据（数据） | 排除谁 | 确立谁 |
|------|-------------|--------|--------|
| ① **边 vs 体** | 隙内能量（Vb=−0.11 V, Vg=+60 V）LDOS 图：畴壁网络亮、AB/BA 区暗（因 gap）📜Q（Fig. 3a） | 态局域在 AB/BA 体区 | 增强 LDOS 在畴壁（边态**存在**，必要条件） |
| ② **电场开关** | Vg=−50 V（电场≈0）畴壁增强缺失（Fig. 3c）；Vb=−0.245 V 移出隙 → 对比大降（Fig. 3b）📜Q | 无隙畴壁态、与 gap 无关的态 | TPH **仅在 AB/BA 开隙时出现** |
| ③ **TPH vs 非拓扑畴壁带** | 隙内 = **双线**；高能 ±250 meV = **单线**且无电场时仍在（SI Fig. S4a/b）📜Q | 高能 ±250 meV 增强是 TPH | 高能增强 = 畴壁带 van Hove 奇异（鞍点），**非 TPH** |
| ④ **DOS vs 物理起伏** | 形貌随样品电压变化（SI Fig. S1：+0.5 V 亮 → +0.2 V 暗）📜Q | 形貌亮线是物理高度起伏 | 亮线来自 DOS 变化（隧穿电流 ∝ ∫DOS） |
| ⑤ **与螺旋态预言一致** | 双线空间分离与孤立畴壁报道（ref [19] Yin 2016）+ 螺旋态预言一致 📜Q | —（形态学支持） | TPH = 螺旋态（**形态学一致**，非谷保护直接证明） |

> **主结果 ↔ 判别表的对应**：
> - 主结果① TPH 态存在（双线、隙内）← {① 边 vs 体, ⑤ 与螺旋态预言一致}
> - 主结果② TPH 仅在开隙时出现 ← {② 电场开关}
> - 主结果③ 高能 ±250 meV 非 TPH ← {③ TPH vs 非拓扑畴壁带}
> - 主结果④ 可设计拓扑网络（λ 可控）← {④ DOS vs 物理起伏}（+ 器件制备 θ 控制）
>
> **分层排除注**：本文证的是"态在畴壁 + 开隙时出现 + 与螺旋态预言形态一致"三层；"**拓扑保护**"来自与网络模型 [10,38] 的一致性**推断**，非谷保护直接测量——即**必要 + 一致，非充分**（证据阶梯见 [PHY-BERRY]）。作者措辞 "demonstrate the emergence"（而非 prove）📜Q。封闭世界假设风险：未排除"同样双线 + 隙内但非拓扑"的竞争解释。

> **[前提与限定]**（判别结论的适用范围）：
> - **噪声/扰动**：无序（模型加背景 DOS $\nu_0$ + 能量偏移 $E_0$，SI 式(3) 📜Q）；tip 态（tip 校准排除 tip DOS 伪峰，SI §TIP CALIBRATION 📜Q）；热展宽（4.5 K，数值未给）。
> - **判别性扫轴**：$V_g$（−80~+40 V 及 +60/−50 V）、$V_b$（−0.6~+0.4 V）、空间位置（AB 中心/BA 中心/AA/畴壁）、能量（FT-STS 色散）。
> - **候选集 M 边界**：本文排除集 = {体态、无隙畴壁态、高能 van Hove、物理起伏}；"TPH（拓扑保护螺旋态）"在该集内唯一幸存。**集外未排除**：谷保护（intervalley 散射）未测——"topologically protected" 是理论一致推断（E13 Verbakel 2021 才做谷保护直接验证）💭I。

三层标注：📜Q = 原文事实（附位置）｜推导｜📊F = 读图估算｜💭I = 推断。**不确定度（正交轴）**：[±] 原文误差棒 / [~] 原文无误差棒 / [读图] 图提取·色标值 / [相对] 仅相对量。所有数字经 pdftotext + grep 反向核对（正文 + SI）。

---

## 2. 结果与机制（按论文论证结构：器件 → 双线 TPH → 电场开关 → 高能带 → 定量）

### 2.1 设计莫尔晶体（designer moiré crystal）

同源石墨烯 sequential pickup：从**同一片单层石墨烯**连续拾取两块 → 晶格取向一致 → 扭角 = 拾取过程旋转角（直接可控）📜Q。主样品 $\lambda=57.6\pm0.7$ nm，$\theta=0.245\pm0.003^\circ$ [±] 📜Q；畴壁宽度 "several nanometer" [~] 📜Q。AA 位呈亮点（与既往观测一致），连接 AA 的亮线 = 畴壁 📜Q。

### 2.2 TPH 态存在性：双线 + 隙内（判别①⑤）

- 畴壁谱（Fig. 1d, Vg=+60 V）无 −0.1 V dip（AB 区 dip = 电场开的 gap），而在电荷中性点两侧 ±0.25 V 出现**对称双峰**（高能 van Hove）📜Q。
- **空间成像**（Fig. 3a，Vg=+60 V，Vb=−0.11 V = gap 中心）：畴壁网络呈**双线**（两条平行 LDOS 增强线沿每根畴壁），AB/BA 区暗（gap）📜Q。双线空间分离与孤立畴壁报道 + 螺旋态预言一致 📜Q（ref [19]）。
- 机制（见 [PHY-BERRY]）：电场下 AB/BA 各开隙、valley Chern 数反号 → 界面束缚反向传播谷手征态对 = helical（TPH）态 📜Q。

### 2.3 电场开关：TPH 仅在开隙时出现（判别②）

- Vg=+60 V、Vb=−0.245 V（隙外）：畴壁/区域对比显著下降 → 隙外态退局域离 AA 点 📜Q（Fig. 3b）。
- Vg=−50 V、Vb=0.1 V（电场≈0）：畴壁增强缺失 → "无隙则无 TPH" 📜Q（Fig. 3c）。与 San-Jose & Prada 图 2(f) 预言（AA 附近耗尽区 + 复杂图案）一致 📜Q。

### 2.4 高能畴壁带：±250 meV 非 TPH（判别③，SI 新增）

- 畴壁高能 ±250 meV 增强在 **gap 外**，非 TPH 📜Q（SI §LDOS ON DOMAIN WALLS AT HIGH ENERGY）。
- **判别性成像**（SI Fig. S4）：+250 meV 处 = **单线**（连 AA，非双线）；且在**有电场（0.165 V @ +60 V）与无电场（0.365 V @ −50 V）都出现** → 与 gap/TPH 无关 📜Q。
- 机制（SI 模型）：畴壁局部带结构有 4 个 Dirac 点（E≈±150、±300 meV）+ 2 个鞍点（E≈±256 meV）→ van Hove 奇异（正文 Fig. 1d/2b 的 ±0.25 V 双峰）📜Q。

### 2.5 对比度定量（Fig. 4）

对比度 $C=[I(DW)-I(AB)]/I(AB)$ 📜Q（正文原式）：Vg=+60 V 时 C(V) 在 gap 中心有主峰、AB 带边附近降到近零（带边由 FT-STS 定，SI Fig. S8）📜Q；Vg=−50 V 时中央峰消失、±0.25 V 两高能峰仍在 📜Q。中央峰 FWHM 与 FWHM 内平均对比度均随 Vg 下降（Fig. 4c/d，误差棒 = 平均值的标准差）→ TPH 强度 ∝ gap 大小 📜Q。

---

## 3. 实验方法

### 3.1 器件
薄 h-BN（~10–20 nm）作拾取层；半球形手柄（覆 PVA）拾 h-BN → 连续拾两块同源石墨烯（旋转手柄定 θ）→ 置 SiO₂/Si 上、TBLG 在 h-BN 上（TBLG 暴露于针尖）📜Q。TBLG–h-BN 间取大扭角以免 h-BN 影响电子性质 📜Q。电极 Cr(5 nm)/Au(35 nm)，EBL 定义，接触 TBLG 与硅背栅（控电荷密度 + 层间偏压）📜Q。高真空 350°C 退火 6 h 📜Q。⚠️ "tear-and-stack" 原文未出现（惯称）💭I。

### 3.2 静电学（本文数值代入，通用推导见 [PHY-GATE]）
层间破反演电场三贡献 = 背栅 + tip bias + 针尖-TBLG 功函数失配；后两者使"零电场点"对应 Vg 偏移 📜Q → gap 在**正大 Vg** 最大（非 Vg=0）📜Q。SI 模型在 Vg=60 V 取能量偏移 $E_0\approx-0.1$ eV、$2u\approx\Delta\approx 60$ meV [~] 📜Q。

### 3.3 测量（含 SI 新增细节）
- STM/STS：4.5 K、超高真空、电化学刻蚀 W tip 📜Q。隧穿稳定 I=200 pA、V=+0.5 V 📜Q。dI/dV 加 3 mV/572 Hz 交流 📜Q；LDOS map 用 8 mV 交流 📜Q。⚠️ "锁相"原文无 lock-in 字样（推断标准做法）💭I。
- **Tip 校准**（SI §TIP CALIBRATION）：W tip 用稀 NaOH 电化学刻蚀 → UHV 电压脉冲修型 → 每次在 Au 表面检查 dI/dV 在 −0.5~+0.5 V 平直才用、测后再查 📜Q → 排除 tip DOS 伪峰；本篇用了几十根 tip、结果一致 📜Q。
- **Gap 提取**（SI §EXTRACTION OF BAND GAP WIDTH）：谱的 gap 段用二阶多项式 $y=a(x-x_0)^2+b$ 拟合，gap 取 $b+0.16$ 处的宽度（0.16 选为使 Vg=+70 V 时与对比度 FWHM 一致）📜Q。
- **FT-STS 色散**（SI §ENERGY MOMENTUM DISPERSION，~120 nm 样品）：从 LDOS 驻波做傅里叶变换得波矢（q 空间中央盘半径 = $2k_F$）→ $E=E_c+\hbar^2k^2/2m^*$ 拟合得导带边与有效质量 📜Q（见 §4.4；QPI 机制见 [PHY-QPI]）。

---

## 4. 关键数据（提取链 + 验证链 + 不确定度）

### 4.1 几何
| 参数 | 值 | 证据 |
|------|-----|------|
| 莫尔周期 λ（主样品） | 57.6±0.7 nm | 📜Q [±]（正文 + Fig. 1c caption） |
| 扭角 θ | 0.245±0.003° | 📜Q [±]（正文） |
| 畴壁宽度 | several nanometer | 📜Q [~]（正文） |
| 莫尔周期下限 | >50 nm（波长可控） | 📜Q（摘要/末段） |
| SI 考察波长范围 | 上至 200 nm；λ>35 nm 定性一致 | 📜Q [~]（SI §TIP） |
| FT-STS 样品波长 | ~120 nm | 📜Q [~]（SI Fig. S8 caption） |
| Fig. 1c / Fig. 3 标尺 | 80 nm / 50 nm | 📜Q（caption） |

### 4.2 能谱特征
| 量 | 值 | 证据 |
|----|-----|------|
| 网络能标 $E_\lambda$ | $2\pi\hbar v/3\lambda\approx 24$ meV | 📜Q [~]（正文，代入 λ=57.6 nm） |
| AB 区 gap dip | −0.1 V 附近（Vg=+60 V） | 📜Q [~]（正文 + Fig. 1d） |
| 第二子带 onset | +0.3 V（正文）≈ 0.4 V（SI）↔ $\gamma_1$ | 📜Q [~]（正文 + SI §AB/BA） |
| 畴壁 van Hove 双峰 | ±0.25 V（正文）≈ ±250 meV；SI 鞍点 ±256 meV | 📜Q [~]（正文 + SI） |
| gap 宽度范围 | ~10–70 meV（Fig. 2c 纵轴，Vg −80~+40 V） | 📊F [读图] |
| SI 模型 gap（Vg=60 V） | Δ≈60 meV | 📜Q [~]（SI §LOCAL BAND） |

> ⚠️ **E_F 位置（易误读）**：Vg=+60 V 时 CNP 在 −0.1 V（$E_0\approx-0.1$ eV），故 **E_F 不在 gap 内**，而是在 gap 中心之上 100 meV = 导带内 ~70–100 meV（FT-STS 给 $E_c=-107$ meV 佐证）📜Q/推导。TPH 态是**靠 V_b 扫到 −0.11 V**（E_F 之下 110 meV）探测的，并非 E_F 在 gap 内——"成像 gap 内态 ≠ E_F 在 gap 内"，见 [PHY-GATE] §11。

### 4.3 SI 连续模型参数（§DENSITY OF STATES IN LOCAL BAND APPROXIMATION）
| 参数 | 值 | 证据 |
|------|-----|------|
| 层间杂化 w | ≈0.45 eV（略大于无扭转 BLG 的 ≈0.4 eV） | 📜Q [~]（SI） |
| 能量偏移 E₀（Vg=60 V） | ≈−0.1 eV | 📜Q [~]（SI） |
| Dirac 点劈裂 2u | ≈Δ≈60 meV | 📜Q [~]（SI） |
| 畴壁计算位置 r_DW | {0, 9.4 nm}（偏离 AA 连线中点 r₀={0,0}） | 📜Q（SI） |
| AB/BA 计算位置 r_AB/BA | {±16 nm, 0} | 📜Q（SI） |
| 畴壁带 Dirac 点 | E≈±150、±300 meV（4 个） | 📜Q [~]（SI） |
| 畴壁带鞍点 | E≈±256 meV（2 个） | 📜Q [~]（SI） |
| 理论 LDOS 算法 | 线性四面体法，代码 github.com/tflovorn/{tightbinding,blg_moire} | 📜Q（SI ref [3]） |

### 4.4 FT-STS 色散（SI Fig. S8，~120 nm 样品）
| 量 | Vg=40 V | Vg=60 V | 证据 |
|----|---------|---------|------|
| 导带边 $E_c$ | −73±4 meV | −107±2 meV | 📜Q [±]（SI） |
| 有效质量 $m^*$ | (0.048±0.004)$m_e$（两 Vg 相同） | 同左 | 📜Q [±]（SI） |
| 色散形式 | $E=E_c+\hbar^2k^2/2m^*$（k² 依赖） | — | 📜Q（SI） |
| 意义 | $m^*$ 大于既往 BLG 隧道/磁阻/光学测量值（因电场开隙） | — | 📜Q（SI） |

### 4.5 关键能量点（Fig. 3/Fig. 4/SI Fig. S4）
| 条件 | 位置 | 证据 |
|------|------|------|
| 隙内（双线 TPH） | Vb=−0.11 V, Vg=+60 V | 📜Q（Fig. 3a） |
| 隙外（对比降） | Vb=−0.245 V, Vg=+60 V | 📜Q（Fig. 3b） |
| 无电场（无 TPH） | Vb=0.1 V, Vg=−50 V | 📜Q（Fig. 3c） |
| 高能单线（有电场） | Vb=0.165 V, Vg=+60 V | 📜Q（SI Fig. S4a） |
| 高能单线（无电场） | Vb=0.365 V, Vg=−50 V | 📜Q（SI Fig. S4b） |
| AA 中央峰（大 DOS） | 各 Vg 均在费米面附近，>100 V 栅压填不满 | 📜Q（SI Fig. S2） |

### 4.6 验证链
- **AB vs BA 等价**：SI Fig. S3 两区谱定性相同（论证堆垛对称性）📜Q。
- **形貌 = DOS**：SI Fig. S1 电压依赖形貌（+0.5 V 亮 → +0.2 V 暗）→ 亮线非物理起伏 📜Q（判别④）。
- **tip 可重复性**：几十根 tip 结果一致 + 多波长（35–200 nm）定性一致 📜Q（SI §TIP）——样本级稳健性。
- **理论与实验互验**：模型（w=0.45 eV, 2u≈60 meV）捕获 E≳Δ 全部主特征，AB/BA gap 值 Δ≈60 meV 与实测一致 📜Q（SI Fig. S5/S6）。

---

## 5. 主要结论
1. mTBG 畴壁网络上出现 TPH 态：隙内双线 LDOS 增强、仅在 AB/BA 开隙时出现 📜Q。
2. 畴壁高能 ±250 meV 增强是畴壁带 van Hove 奇异（鞍点 ±256 meV），非 TPH（单线 + 无电场仍在）📜Q（SI）。
3. 同源 sequential pickup 可制 λ>50 nm 的可控畴壁网络 → "可设计拓扑通道网络" 📜Q。
4. 畴壁网络"可用作拓扑通道以无耗散方式输运电荷"（作者表述 "can be used as ... dissipationless manner"）📜Q（末段）——⚠️ 此为能力声明，本文无输运测量佐证 💭I。

## 6. 局限与未解决
| 局限 | 说明 | 证据 |
|------|------|------|
| 仅局域谱学 | 全文无输运（无反散射长度、电导平台、"无耗散"未验证） | 📜Q（只做 STS）+ 💭I |
| 谷保护未直接验证 | 仅形态学（双线）+ 电场开关；无 intervalley 散射测量 | 💭I（cards.md E9 同判） |
| $E_\lambda\ll\Delta$ 不满足 | 仅 −0.05 V 一个网络峰清晰分辨 | 📜Q（正文） |
| 高温/磁场未知 | 全测 4.5 K，无 B | 💭I |
| 无损耗声明过强 | "dissipationless" 未在本文验证 | 💭I |
| 与 magic-angle 关联态无关 | 极小扭角但未涉强关联 | 💭I |

## 7. 与其他工作的关系
| 工作 | 关系 |
|------|------|
| Martin et al. 2008 (ref [2]) | 电场畴壁拓扑束缚原始预言 📜Q |
| San-Jose & Prada 2013 (ref [10]) | 螺旋网络理论——本文引其图 2(f) 作 −50 V 对照 + 网络模型 [10,38] 📜Q |
| Efimkin & MacDonald 2018 (ref [38]) | 畴壁网络能谱理论（$E_\lambda$）📜Q |
| Ju et al. 2015 (ref [18]) / Li et al. 2016 (ref [16,17]) | 均匀 BLG 畴壁输运（split-gate TPH 弹道输运）📜Q |
| Yin et al. 2016 (ref [19]) | STM 单条畴壁边缘态；双线分离此前已报 📜Q |
| Rickhaus 2018 (E10, ref [16 in Xu]) | 同年 FP+AB 输运——与本文并行（本文 STM、Rickhaus 输运）💭I |
| Verbakel 2021 (E13) | **后续**谷保护直接实验（intervalley 散射缺失）——补本文未做之判别 💭I |

## 8. 对后续研究的影响
- 把拓扑界面态从单条畴壁推进到**二维可工程化网络**（"controllable topological networks"）📜Q。
- 方法学：扭角工程（同源拾取）+ 局域探针（STM/STS + FT-STS + 对比度）可直接鉴别拓扑态 📜Q。
- 与 2018 magic-angle 热潮并行，开辟"非强关联拓扑网络"主线 💭I。
- 遗留给 E13 的判别任务：谷保护直接验证 💭I。

## 9. 理论模型映射（供 tbplas / Kubo 对照）
| 映射 | 说明 |
|------|------|
| $\theta\to\lambda\to$ 莫尔图案 | 同源拾取定 θ；$\lambda=a/[2\sin(\theta/2)]$ 📜Q |
| 电场→$2u\approx\Delta$ | Vg+tip+功函数三贡献；Vg=60 V 时 $2u\approx\Delta\approx60$ meV 📜Q |
| 观测量↔LDOS | STS dI/dV/(I/V) ↔ 连续模型 LDOS（+背景 $\nu_0$+偏移 $E_0$）📜Q |
| 理论代码 | 线性四面体法 tight-binding LDOS：github.com/tflovorn/{tightbinding,blg_moire} 📜Q（SI ref [3]）——可直接对标复现 |
| 色散↔$m^*$ | FT-STS $E=E_c+\hbar^2k^2/2m^*$ → $E_c,m^*$ 📜Q |

> 与 TBPM/Kubo 对应：本文是**局域谱学**（LDOS 空间图 + 点谱），非输运——tbplas 可直接对标 SI 的 tight-binding LDOS 计算（w、u、r_DW 等参数已给全）；双线形态与鞍点位置是 TBPM 可直接复现的可观测量 💭I。

---

## Phase S 目的接口（三问，引用式）

- **Q1（edge state 如何表征）**：STM/STS 直接成像——畴壁隙内**双线 LDOS 增强**（Fig. 3a）+ **边体区分**（AB/BA 暗 vs 畴壁亮）+ **电场开关**（移电场/移隙 → 对比消失）+ **定量对比度** $C=[I(DW)-I(AB)]/I(AB)$。核心可观测量 = LDOS 空间图 + 双线形态。详见 §2/§4。
- **Q2（理论如何解释）**：网络模型 [10,38]（$E_\lambda=2\pi\hbar v/3\lambda\approx24$ meV）+ 连续模型 [39]（畴壁带鞍点 ±256 meV → van Hove）。详见 §9 映射。
- **Q3（理论↔实验对应）**：电场开隙 ↔ 双线出现；高能 ±250 meV ↔ 鞍点 van Hove（SI 模型 ±256 meV）；gap Δ≈60 meV ↔ 模型 $2u$；色散 $E_c,m^*$ ↔ FT-STS 拟合。作者表述 "captures all the principal observed features" 📜Q（E≳Δ）。

> **增量价值**：比归档 8 节版新增 **SI 全读**——FT-STS 色散（$E_c=-73\pm4/-107\pm2$ meV、$m^*=0.048\pm0.004\,m_e$）、gap 提取算法（$b+0.16$）、连续模型参数（$w\approx0.45$ eV、$2u\approx60$ meV、鞍点 ±256 meV、4 Dirac 点 ±150/±300 meV）、高能单线 vs 双线判别（Fig. S4）、tip 校准与多波长稳健性（35–200 nm）、理论 LDOS 代码（github tflovorn）。report.md §2 用其判别表 + §4 双线/电场开关数据；§4 用 Q3 映射链。比 E13 少的维度 = 谷保护（intervalley）直接证据，比输运论文（E10/E12）少的 = 相干/输运量化。

## 反向核对 pass (2026-09-01)
pdftotext 提取正文 + SI，逐项 grep 核对：λ=57.6±0.7 nm / θ=0.245±0.003° / >50 nm / several nanometer / 24 meV / 10–20 nm / Cr 5 nm / Au 35 nm / 350°C 6h / 4.5 K / 200 pA / +0.5 V / 3 mV 572 Hz / 8 mV / −0.1 V / +0.3 V / ±0.25 V / ±250 meV / −0.05 V / +60 V / −0.11 V / −0.245 V / −50 V / 0.1 V / −80~+40 V / 80 nm / 50 nm / sequential pickup / same lattice orientation / polyvinyl alcohol / dissipationless —— 全部在正文找到；SI 新增 w≈0.45 eV / 2u≈Δ≈60 meV / E0≈−0.1 eV / r_DW={0,9.4 nm} / r_AB/BA={±16 nm,0} / ±150/±300 meV / ±256 meV / b+0.16 / +70 V / Ec=−73±4 / −107±2 meV / m*=(0.048±0.004)me / ~120 nm / 0.165 V / 0.365 V / >100 V / 200 nm / 35 nm / NaOH / −0.5~+0.5 V / tens of tips / tetrahedron / tflovorn —— 全部在 SI 找到。
⚠️ 原文无：lock-in（降级 💭I）；tear-and-stack（标注惯称）。"gap 10–70 meV" 与 "−80~+40 V 扫轴" 为 Fig. 2c 读图 → 标 📊F[读图]。

## 更正日志
| 日期 | 条目 |
|------|------|
| 2026-09-01 | 自 archive 8 节版重写为 4 块模板（TL;DR + 判别表置顶 + [前提与限定] + 数据/提取链 + 目的接口） |
| 2026-09-01 | **补 SI 全读**（此前仅引 "SI[30]" 未提取内容）：FT-STS 色散、gap 提取算法、连续模型参数、Fig. S4 单线/双线判别、tip 校准、理论 LDOS 代码 |
| 2026-09-01 | **判别表重构**：新增判别③（TPH vs 非拓扑畴壁带，SI Fig. S4 单线/双线）与判别④（DOS vs 物理起伏，SI Fig. S1）；显式标注"拓扑保护=理论一致推断，非谷保护直接证明"（M 边界声明） |
| 2026-09-01 | SI 标题与正文标题差异（"Emergence of ..." vs "Topologically Protected ..."）录入头部表；±250（正文）vs ±256（SI）meV 鞍点两处并记 |
