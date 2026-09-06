<!--
 * @Author       : AI 精读 (系统辨识式阅读法 → 三层分离整理)
 * @Date         : 2026-07-15（初读）→ 2026-09-01（按 4 块辨识结构重读重写）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/experiments/paper_review_E17_zhang2024_arxiv.md
 * @Description  : E17: Zhang et al. (2024) arXiv:2406.06867 — CVD 双层石墨烯 LSW 束的电可调磁电导（4 块辨识结构）
-->

# Paper Review: Zhang et al. (2024) — CVD 双层石墨烯 LSW 束的电可调磁电导

| 字段 | 内容 |
|------|------|
| **编号** | E17 |
| **标题** | Electrically Tunable Magnetoconductance of Close-Packed CVD Bilayer Graphene Layer Stacking Walls |
| **作者** | Qicheng Zhang, Sheng Wang, Zhaoli Gao, Sebastian Hurtado-Parra, Joel Berry, Zachariah Addison, Paul Masih Das, William M. Parkin, Marija Drndic, James M. Kikkawa, Feng Wang, Eugene J. Mele, A. T. Charlie Johnson, Zhengtang Luo |
| **期刊** | arXiv:2406.06867（2024-06-11，v1）— **arXiv-only 预印本，无期刊版**（CUHK 机构库仅登记为 preprint/working paper；arXiv 无 journal-ref）⚠️ |
| **DOI / arXiv** | arXiv:2406.06867 |
| **类型** | 实验 + 理论 — 低温双栅输运 + DF-TEM/IR-SNOM 结构成像 + Bloch 模式计算 |
| **课题组** | Johnson (UPenn, CVD/纳米电子学) + Mele (UPenn, QVH 理论) + Drndic (UPenn, TEM) + Kikkawa (UPenn, 输运) + Feng Wang (Berkeley, IR-SNOM) + Luo (HKUST, CVD 合成) |
| **PDF / SI PDF** | ✅ 正文 `reference/pdfs/Zhang 等 - 2024 - …pdf`（14 页）；**SI：⚠️ 无**（正文引用 Supplementary Note 1–7 + Methods 尾 "Supplementary Information is available for this paper"，但 arXiv v1 无 ancillary 文件，暂搁置） |
| **精读日期** | 2026-07-15（初读）→ 2026-09-01（4 块辨识结构重读） |

> **共享知识引用**：双栅静电学 n/D 换算 → `[PHY-GATE]`；畴壁 = 1D 导线、无闭合网络故无 miniband → `[PHY-MB]` §1；相干长度 $L_\phi$ 退相干概念 → `[PHY-AB]` §3。⚠️ **弱局域（相干背散射）机制与 MC 公式是 E 序列首次遇到，通用物理未入 shared**，本文直接写 §2.3/§4，标「💭 可晋升 [PHY-WL]」。不复制讲义、不新建 shared 文件。

---

## TL;DR

**本文想解决的问题**：CVD 外延双层石墨烯中，不同应变源产生的两种 LSW 构型（well-separated vs close-packed bundle）输运有何差异？紧密堆积 LSW 束中多条 QVH 畴壁通道间的耦合能否被**电场连续调控**？

**主结果**：① 两种 LSW 构型：substrate corrugation → 相干应变 → proximity-avoiding 平行分离 LSW（间距 50–200 nm）；localized stress（纳米颗粒/双层汇合角）→ 随机 Burgers 矢量的 close-packed 束 📜Q。② 输运对比（3-LSW vs 7-LSW 器件）：CNP 电阻随 $\bar D$ 饱和于 ~3.2 kΩ（~8e²/h @ $\bar D$=1.6 V/nm），无 LSW 器件 >100 kΩ 不饱和；$\Delta G=G_{7}-G_{3}$ 在 $\bar D$>0.8 V/nm 后增加 ~3e²/h（0.8→1.6 V/nm）📜Q[~]。③ 磁电导 MC：7-LSW 的零场 MC 极小随 $\bar D$ 显著加深（$\bar D$=1.5 V/nm 时深 ~20%），3-LSW 的 MC 对 $\bar D$ 不敏感（体 2D 弱局域）📜Q[~]。④ 1D 弱局域拟合 → $L_\phi$ 随 $\bar D$ **近似指数增长** 📜Q。⑤ Bloch 模式模型：波函数重叠随体隙 $E_g$ 增而减（$x_0\propto 1/E_g$）→ 谷内背散射电可调。

**结论/意义**：不同应变源可工程化出电可调 QVH 畴壁模束；作者措辞为 "explained by a model"、"qualitatively accounts for"、"consistent with"——**定性解释，非定量证明** 📜Q。⚠️ 未 peer review（arXiv-only）。

---

## 1. 系统辨识导览（判别表为全文唯一权威）

**黑箱三要素**：`{输入旋钮: 顶栅 $V_t$、底栅 $V_b$（→ $\bar D,n$）、磁场 $B$ | 输出观测量: $R_{xx}(V_t,V_b)$、$G(\bar D)$、MC($B$)、$\Delta G(\bar D)$ | 声称结论: 紧密堆积 LSW 束支持电可调磁电导，机制 = 波函数重叠随 $E_g$ 电调}`

**四层变量图**（符号层一次钉死）：

| 层 | 本文实例 |
|----|----------|
| **L1 旋钮 u** | $V_t$（顶栅）、$V_b$（底栅/硅衬底）、$B$；$T$=2 K 固定 |
| **L2 导出量 x₁** | $\bar D=(D_b+D_t)/2$、$n=D_b-D_t$、$D_b=\varepsilon_b(V_b-V_{b0})/d_b$、$D_t=\varepsilon_t(V_{t0}-V_t)/d_t$、$E_g\sim\bar D$（低 $\bar D$<2 V/nm，引 ref 25） |
| **L3 模型量 x₂** | $x_0\propto 1/E_g$（畴壁态波函数衰减长度，引 ref 9）、$L_\phi$（1D WL 拟合参数）、有效准 1D 导体的 $N,W,L$ |
| **固定参数（非旋钮）** | LSW 数（3 vs 7）、沟道长 $L$=400 nm、条宽 1.5 µm、介电层（顶 40 nm Al₂O₃；底硅衬底氧化层厚度正文未给） |
| **反推量 θ̂** | $L_\phi(\bar D)$（从 1D WL 公式拟合 MC 曲线反推） |
| **L4 观测量 y** | $R_{xx}$、$G(\bar D)$、$MC(B)=G(B)-G(0)$、$\Delta G(\bar D)=G_{7}-G_{3}$ |

> 与 E12 静电学符号差异：E12 用 $n$=(共模)、$D$=(差模)；本文用 $\bar D$=(平均位移场，**开隙**)、$n=D_b-D_t$（**费米能**）——旋钮物理角色对调，见 §3.2 [PHY-GATE]。

**可辨识性判别表**（唯一权威；本文五条判据）：

| 判别 | 判据（数据） | 排除谁 | 确立谁 |
|------|-------------|--------|--------|
| **体 vs 墙导电** | 无 LSW 器件 CNP 电阻 >100 kΩ 无饱和迹象（Supplementary Fig. 5a）vs LSW 器件饱和 ~3.2 kΩ @ $\bar D$=1.6 V/nm 📜Q | 纯体 2D 导电 | 大隙下导电 QVH 畴壁通道**存在**（必要条件） |
| **平行独立 vs 通道耦合** | 7-LSW 每通道贡献 ~0.43（≈3/7）倍 3-LSW 每通道——与 ref 6 "平行导体"（每通道电导应相近）矛盾 📜Q | 多 LSW = 独立平行导体 | 束内通道间存在耦合/抑制 |
| **体 2D WL vs 墙 1D WL** | 3-LSW 零场小正 MC 对 $\bar D$ 不敏感（体 BLG 弱局域，Supplementary Note 5）vs 7-LSW MC 极小随 $\bar D$ 深；$\bar D\ge0.8$ V/nm 用 1D WL 拟合 📜Q | 7-LSW 的 MC 也归因于体 2D WL | 7-LSW 输运过渡到 1D 畴壁主导 |
| **谷间 vs 谷内背散射** | 拓扑保护压制 $K\leftrightarrow K'$；AB/BA 与 BA/AB LSW 空间反演关联 → 同谷模反向传播 → 重叠时形成背散射通道 📜Q | 谷间散射（被拓扑压制） | 背散射通道 = **谷内**（不同 LSW 间） |
| **电调机制** | $x_0\propto 1/E_g$、$E_g\sim\bar D$ → $\bar D$↑→重叠↓→背散射↓→$L_\phi$↑（指数）；与实测 $L_\phi$ 近似指数增长一致 📜Q | 与 $E_g$ 无关的固定耦合 | 波函数重叠 = 电可调 inter-wall 耦合 |

> **主结果 ↔ 判别表映射**：
> - 主结果① 两种 LSW 构型 ← 结构表征（DF-TEM invisibility criterion + Burgers 矢量分布，非输运判别，见 §2.1）
> - 主结果② 墙导电 + 束内耦合（$\Delta G\sim3e^2/h$、~0.43）← {体 vs 墙, 平行 vs 耦合}
> - 主结果③ 电可调 MC（深极小、$L_\phi$ 指数）← {体 2D vs 墙 1D WL, 电调机制}
> - 主结果④ 波函数重叠模型 ← {谷内背散射, 电调机制}
>
> **分层排除注**：①「体 vs 墙」先证导电在墙不在体（必要条件）；②「平行 vs 耦合」证束内耦合存在；③「体 2D vs 墙 1D WL」证 MC 归因到 1D 畴壁；④「电调机制」给耦合一个可调的微观来源。作者自述模型 "qualitatively accounts for the observed difference"（定性一致，非"证明"）📜Q。

> **[前提与限定]**（判别结论的适用范围）：
> - **噪声/扰动**：$\Delta G$ 是**差量**，依赖 3-LSW 作参照（两器件同 flake、相邻几 µm，体电导相似是前提）；MC 深度 ~20% 是**相对量**（背景绝对值未给，只能引相对量）；$L_\phi$ 是 1D WL 拟合的**模型参数**（非直接测量）；$T$=2 K 固定；杂质/无序 → bulk puddles（引 ref 26）。
> - **判别性扫轴**：扫 $\bar D$（0→1.6 V/nm，固定 $n=0$ 即 CNP）、扫 $B$（MC，$B=0$ 附近）；未测：变温、变 $n$ 的完整相图、更多器件统计（正文只 3-LSW/7-LSW 各一器件 + "其他 close-packed 器件类似" Supplementary Fig. 8）。
> - **候选集 M 边界**：{纯体导电, 平行独立导体, 体 2D WL, 谷间散射} 在**论文枚举的**集合内被排除；但"谷内背散射 + 波函数重叠"是本文**提出**的机制，仅做定性 Bloch 计算 + 一致性论证，**无实空间波函数/谷分辨率测量直接验证**；集合之外候选（如通道间隧穿、UCF、其他退相干源）原文未讨论、未排除。

三层标注：📜Q = 原文事实（附位置）｜推导｜📊F = 读图估算｜💭I = 推断。**不确定度（正交轴）**：[±] 原文误差棒 / [~] 原文用 ~ 给出无误差棒 / [读图] 图·色标提取 / [相对] 仅相对量。所有数字经 pdftotext + grep 反向核对（全文无 ±，见反向核对 pass）。

---

## 2. 结果与机制（按论文三段：应变→LSW 构型 / 输运 / MC+理论模型）

### 2.1 应变源 → 两种 LSW 构型（Fig. 1、2）

CVD 双层石墨烯生长在 optimized Ni-Cu gradient alloy 衬底（ref 18）上；主要 LSW 由 **substrate corrugation** 诱导（Supplementary Note 1），AB/BA 堆叠畴呈条纹、映射到衬底台阶（Fig. 1a；方法见 Supplementary Note 2）📜Q。DF-TEM 中 zig-zag LSW 沿石墨烯 zig-zag 方向，在 (21̄1̄) 反射下清晰可见、在 (12̄1) 反射下不可见（invisibility criterion，ref 15），Burgers 矢量垂直于衍射矢量——表明 LSW 两侧存在**应变相干**；armchair LSW 也显示相干（Supplementary Figs. 3a-d）📜Q。与 flat 衬底上机械力产生的 LSW（剪切力主导，ref 20）不同，本文 LSW 的相干应变由 **tensile/compressive** 主导，沿衬底峰谷最大曲率方向 📜Q。

**proximity-avoiding（分离）LSW**：环路论证——绕 LSW 环一周应变 = 0、跨环一周应变也 = 0 → 环两侧应变相互补偿 → 产生大量平行 LSW，间距 **50–200 nm**；亚稳态，转移到碳膜后 <50 nm 的 LSW 数天内 merge/annihilate（Supplementary Fig. 3e），外部机械力也致相邻 LSW 湮灭、有时留 ~1 µm 分离的单 LSW（IR-SNOM 成像，Fig. 1d）📜Q。

**close-packed（紧密堆积）LSW 束**：localized stress（衬底污染物纳米颗粒，Supplementary Figs. 4a-b；两个双层区域的汇合角，Fig. 2a）→ 局域大曲率产生层内应变不对称 / 应力集中 → 密集 LSW、**随机 Burgers 矢量**（DF-TEM 中不随衍射矢量同时消失）📜Q。这些束在转移到硅衬底后**保留**（Supplementary Fig. 4c-d），而 corrugation 诱导的分离 LSW 大多湮灭 📜Q。

### 2.2 输运：体 vs 墙导电、束内耦合（Fig. 3a–e）

pseudo-four-probe 器件（Supplementary Note 3）：3-LSW（间距 ~400 nm）与 7-LSW 束（相距几 µm），沟道 $L$=400 nm、条宽 1.5 µm，两器件同参数 📜Q。CNP 电阻随 $\bar D$ 增加并**饱和**于 ~3.2 kΩ（~8e²/h）@ $\bar D$=1.6 V/nm；对照：无 LSW 器件 >100 kΩ 无饱和（Supplementary Fig. 5a）📜Q。有限饱和电阻 → 大隙下 LSW 承载导电 QVH 畴壁通道 📜Q。

**束内耦合判据**：7-LSW 每通道贡献 ~0.43（≈3/7，推导）倍 3-LSW 每通道——与 ref 6 "多 LSW = 平行导体（每通道电导应相近）"矛盾 📜Q。减掉体电导后，$\Delta G(\bar D)=G_{7}-G_{3}$：$\bar D$<0.8 V/nm 平坦（体主导，两器件体电导相似——同 flake 相邻验证）；$\bar D$>0.8 V/nm 增加；1.0–1.6 V/nm 区间 $G_7$ 小增而 $G_3$ 均匀减（体电导下降）📜Q。$\Delta G$ 在 0.8→1.6 V/nm 增 **~3e²/h**（假设 = 7-LSW 束畴壁通道电导增加），对比 $\bar D$=1.6 V/nm 总电导 ~8e²/h 是显著量 📜Q。

### 2.3 磁电导 MC 与弱局域拟合（Fig. 3f,g、4a,b）

- 3-LSW：$B=0$ 附近小**正** MC，对 $\bar D$ 不敏感；更大 $B$ 转负 📜Q。
- 7-LSW：正 MC 随 $\bar D$ **显著增长**，$B=0$ 深极小；$\bar D$=1.5 V/nm 深 **~20%** 📜Q。
- $n=0$ 时孤立畴壁模电导对磁场不敏感（Supplementary Note 4）；3-LSW 的小正 MC = **体 BLG 弱局域**、大场负 MC = 含 LSW 的 BLG 非均匀输运（Supplementary Note 5）；7-LSW 的 MC 极小随 $\bar D$ 深（核心特征）**不能用该框架解释** 📜Q。

**弱局域理论（本文代入的公式，💭 可晋升 [PHY-WL]）**：量子局域导致零场正 MC；1D/2D WL 均预测 MC 幅随 $L_\phi$ 增 📜Q。2D WL（ref 27）：

$$\Delta\sigma(B)=\sigma(B)-\sigma(0)=\frac{e^2}{\pi h}\left[F\!\left(\frac{B}{B_\phi}\right)-F\!\left(\frac{B}{B_\phi+2B_i}\right)\right],\quad F(z)=\ln z+\psi\left(\tfrac12+\tfrac1z\right),\quad B_{\phi,i}=\frac{\hbar}{4eL^2_{\phi,i}}$$

$\psi$ 双伽马函数、$L_i$ = intervalley 散射平均自由程；$\Delta\sigma(\infty)\sim\ln(1+2L_\phi^2/L_i^2)$（intervalley 散射率取常数）📜Q。1D WL（refs 28,29）：

$$G(B)-G(0)=-\frac{2e^2}{h}\frac{N}{L}\left[\left(\frac{1}{L_\phi^2}+\frac{W^2}{3(\hbar/eB)^2}\right)^{-1/2}-L_\phi\right]$$

$N,W,L$ = 有效准 1D 导体数/宽度/长度；极小深度 $(G(\infty)-G(0))\sim L_\phi$ 📜Q。故 7-LSW 零场 MC 极小振幅随 $\bar D$ 增 → 强 $L_\phi$ 随 $\bar D$ 增（同时 $\bar D$↑ 开体隙 → 输运从 2D 体主导过渡到 1D 畴壁主导）📜Q。$\bar D\ge0.8$ V/nm 用 1D WL 拟合（Fig. 4a；Supplementary Note 6），提取 $L_\phi$ **近似指数增长**（Fig. 4b）；其他 close-packed 器件类似（Supplementary Fig. 8）📜Q。

### 2.4 Bloch 模式模型（Fig. 4c–j；Supplementary Note 7）

计算两条 LSW 的电子 Bloch 模式。模型：分离 LSW 模彼此孤立；紧密堆积器件中**相似晶体动量**的不同 LSW Bloch 态之间可散射（Fig. 4d），影响 MFP 与 $L_\phi$；该 inter-wall 散射率随体隙变 → 电可调 📜Q。拓扑保护压制 $K\leftrightarrow K'$ 谷间散射，但**谷内**不同 LSW 间散射允许；AB/BA 与 BA/AB LSW 由空间反演关联 → 同谷模**反向传播** → 一旦波函数重叠即形成背散射通道 📜Q。

分离墙（$L\gg v_F\hbar/E_g$）：每墙每自旋每谷两条拓扑模跨越能隙（Fig. 4e）；电荷密度集中在 LSW、指数衰减、随 $E_g$ 变（Fig. 4f-g）📜Q。墙间距减 → 波函数在略高于 $E=0$ 处重叠（Fig. 4h,i）→ 背散射不再禁止 📜Q。模型**定性**解释 MC 差异：分离模加和贡献电导、对磁场不敏感；紧密堆积有背散射通道 → 输运环路包磁通 → 弱局域 📜Q。

**电调机制**：$\bar D$ 通过 $E_g$ 控制畴壁态局域与 inter-wall 耦合；单 LSW 畴壁态波函数 $e^{-x/x_0}$、$x_0\propto 1/E_g$（引 ref 9）；$E_g\sim\bar D$ → $\bar D$↑ → $x_0$↓ → 波函数收缩、重叠↓（Fig. 4i→j）→ inter-wall 背散射↓（Supplementary Fig. 9）📜Q。把 close-packed 器件视为多耦合畴壁模的有效准 1D 导体 → 其 $L_\phi$ 与 MFP 随 $\bar D$ 增（重叠减的直接结果）📜Q。$\Delta G$（Fig. 3e）突出 inter-wall 耦合贡献：小 $\bar D$ 抑制电导、$\bar D$↑ 该效应消失（MFP 增）📜Q。$L_\phi$ 近似指数增长 ↔ 波函数重叠指数依赖 $\bar D$ **一致** 📜Q。

---

## 3. 实验方法

### 3.1 器件与生长
- **生长**（Methods，ref 18）：160 nm Ni 溅射于 25 µm Cu 箔（4 mTorr、100 W）；常压 CVD，1050 °C（60 °C/min）、500 sccm Ar + 30 sccm H₂；2.2 sccm CH₄（1% in Ar）1–3 h；快速冷却（10 sccm H₂ + 1000 sccm Ar）📜Q。
- **DF-TEM**（Methods）：amorphous carbon TEM grid 转移；JEOL F200、200 keV、束流 10 nA、camera length 80 cm、选区光阑 1 µm、倾角至 20° 📜Q。
- **IR-SNOM**（Methods）：10.6 µm 红外、金属针尖、第三谐波解调（Zurich HF2LI）压制背景 📜Q。
- **双栅器件**（Methods）：e-beam + O₂ 等离子刻蚀；接触 1 nm Cr/40 nm Pd；HSQ buffer + ALD 40 nm Al₂O₃ 顶介电层；顶栅 5 nm Ti/40 nm Au；底栅 = 硅衬底 📜Q。

### 3.2 静电学（推导见 [PHY-GATE]，本文数值在此）
$$\bar D=\frac{D_b+D_t}{2},\qquad n=D_b-D_t,\qquad D_b=\frac{\varepsilon_b(V_b-V_{b0})}{d_b},\qquad D_t=\frac{\varepsilon_t(V_{t0}-V_t)}{d_t}$$

$\varepsilon_{b(t)}$ 底(顶)栅氧化层介电常数、$d_{b(t)}$ 厚度、$V_{b0}/V_{t0}$ 环境掺杂有效偏移 📜Q。**平均位移场 $\bar D$ 控带隙**（低 $\bar D$<2 V/nm 时 $E_g\sim\bar D$，引 ref 25）、$n$ 控费米能 📜Q。⚠️ 与 E12 的共模/差模角色对调（E12: $n$=共模、$D$=差模；本文: $\bar D$=平均、$n$=差）——同一双栅物理的等价参数化，见 [PHY-GATE] §5。底介电层厚度/常数正文未给数值（见 SI Note 3，暂缺）。

### 3.3 测量（Methods）
PPMS、$T$=2 K、He 压 ~0.1 Torr；顶/底栅 Keithley 2410/237；SR830 锁相，激励 10 mV @ 1 kHz + 1 MΩ 串联 → 电流 10 nA；四探针、漏接地、测 (A−B) 差分 📜Q。观测量 $R_{xx}(V_t,V_b)$；MC = $G(B)$ 相对 $G(0)$；$\Delta G = G_7-G_3$（去体电导的差量）。⚠️ 背景绝对值/$\bar D$ 轴标定细节正文未给，只可引相对量。

---

## 4. 关键数据

### 4.1 器件与构型
| 参数 | 值 | 证据 |
|------|-----|------|
| 分离 LSW 间距 | 50–200 nm（平行；转移后 <50 nm 湮灭，可留 ~1 µm 单 LSW） | 📜Q |
| 3-LSW 器件 LSW 间距 | ~400 nm | 📜Q[~] |
| 7-LSW 器件 | close-packed bundle（束内 LSW 数 7） | 📜Q |
| 沟道长 / 条宽 | $L$=400 nm / 1.5 µm（两器件同） | 📜Q |
| 顶介电层 / 顶栅 | 40 nm Al₂O₃ / 5 nm Ti + 40 nm Au | 📜Q |

### 4.2 输运
| 参数 | 值 | 证据 |
|------|-----|------|
| CNP 饱和电阻（3-/7-LSW） | ~3.2 kΩ（~8e²/h）@ $\bar D$=1.6 V/nm | 📜Q[~] |
| 无 LSW 器件 CNP 电阻 | >100 kΩ（无饱和） | 📜Q |
| 7-LSW 每通道贡献 | ~0.43 ×（3-LSW 每通道） | 📜Q[~]（≈3/7 推导） |
| $\Delta G$ 平坦区间 | $\bar D$<0.8 V/nm | 📜Q |
| $\Delta G$ 增幅 | ~3e²/h（0.8→1.6 V/nm） | 📜Q[~] |
| 总电导 @1.6 V/nm | ~8e²/h | 📜Q[~] |

### 4.3 磁电导与 $L_\phi$
| 参数 | 值 | 证据 |
|------|-----|------|
| 3-LSW 零场 MC | 小正、对 $\bar D$ 不敏感；大 $B$ 转负 | 📜Q（相对量） |
| 7-LSW 零场 MC 极小深度 | ~20% @ $\bar D$=1.5 V/nm | 📜Q[~][相对] |
| $L_\phi$ vs $\bar D$ | 近似指数增长（Fig. 4b 对数坐标线性拟合） | 📜Q |
| 1D WL 拟合区间 | $\bar D\ge0.8$ V/nm | 📜Q |

### 4.4 理论参数（Bloch 模式计算，Fig. 4）
| 参数 | 值 | 证据 |
|------|-----|------|
| 计算体隙 | 60 meV（Fig. 4f,h,i）、80 meV（Fig. 4g,j） | 📜Q（Fig. 4 caption） |
| 分离墙判据 | $L\gg v_F\hbar/E_g$（每墙每自旋每谷两条拓扑模） | 📜Q |
| 波函数衰减 | $e^{-x/x_0}$，$x_0\propto 1/E_g$（引 ref 9） | 📜Q |
| 位置单位 | 单层石墨烯晶格常数 $a_0$ | 📜Q（Fig. 4 caption） |
| 能隙标定 | 低 $\bar D$<2 V/nm 时 $E_g\sim\bar D$（引 ref 25） | 📜Q |

### 4.5 证据链与论证结构（三支柱）
| 支柱 | 轴 | 证什么 | 数据 |
|------|-----|--------|------|
| ① 墙导电 + 束内耦合 | 静电轴（$\bar D$） | 墙导电存在、束内非平行独立 | Fig. 3b–e、Supplementary Fig. 5a |
| ② 电可调 MC | 磁轴（$B$） | 7-LSW 1D 弱局域、$L_\phi$ 电调 | Fig. 3f,g、4a,b |
| ③ 波函数重叠机制 | 能量轴（$E_g\sim\bar D$） | 谷内背散射电可调 | Fig. 4e–j、Supplementary Note 7 |

**完整认定链**：存在性（墙导电）→ 束内耦合（~0.43、$\Delta G$）→ 归因到 1D（WL 拟合）→ 微观机制（波函数重叠 $x_0\propto 1/E_g$）。但**机制层是定性一致性论证**（"qualitatively accounts for"），非定量锁定 📜Q。

---

## 5. 主要结论

1. 不同应变源（substrate corrugation → 相干应变 → 分离 LSW；localized stress → 随机 Burgers 矢量 → close-packed 束）可工程化 LSW 构型 📜Q。
2. 分离 LSW 的正 MC 小而 $\bar D$ 不敏感；紧密堆积束的正 MC 随 $\bar D$ 增长、零场深极小（$\bar D$=1.5 V/nm 深 ~20%）📜Q[~]。
3. 7-LSW 束的 $L_\phi$ 随 $\bar D$ 近似指数增长（1D WL 拟合）📜Q。
4. 机制（作者模型）：$\bar D$ 经 $E_g$ 调波函数延展度 $x_0\propto 1/E_g$ → 束内波函数重叠电调 → 谷内背散射电调；$\Delta G$ 在 0.8→1.6 V/nm 增 ~3e²/h 反映 inter-wall 耦合随 $\bar D$ 减弱 📜Q。
5. 作者定位：scalable back-diffusion 生长 + 应变源共存 → 可编程量子输运平台候选（all-electric valleytronics、Chalker-Coddington 网络 ref 30、QVH qubit 类比 ref 31）📜Q。

## 6. 局限与未解决
| 局限 | 说明 | 证据 |
|------|------|------|
| **未 peer review** | arXiv-only 预印本 v1，无期刊版 | ⚠️ 元数据 |
| **理论定性** | Bloch 模型 "qualitatively accounts for"，无定量预言/拟合参数对比 | 📜Q |
| **无实空间/谷分辨验证** | 波函数重叠、谷内背散射是模型推断，无直接测量 | 💭I |
| **器件统计少** | 正文 3-LSW/7-LSW 各一器件；"其他 close-packed 类似"仅在 Supplementary Fig. 8（SI 缺失） | 📜Q |
| **$L_\phi$ 是拟合量** | 依赖 1D WL 公式与 $N,W$ 参数化；$\bar D\ge0.8$ V/nm 才适用 | 📜Q |
| **背景未给绝对值** | MC 深度 ~20% 是相对量，$\Delta G$ 是差量（依赖 3-LSW 参照） | 📜Q |
| **底介电层参数缺失** | $d_b,\varepsilon_b$ 正文未给数值（SI Note 3 暂缺） | ⚠️ |
| **未变温/变 $n$ 相图** | 仅 $T$=2 K、$n=0$（CNP） | 📜Q |

## 7. 与其他工作的关系
| 工作 | 关系 |
|------|------|
| Ju 2015 (ref 6) / Li 2016 (ref 7) | QVH 畴壁输运 / 栅控拓扑通道——"平行导体"预期来源 📜Q |
| Jiang 2017 (ref 13) / Jiang 2016 (ref 22) | LSW 等离激元反射——IR-SNOM 定位 LSW 的方法基础 📜Q |
| Alden 2013 (ref 14) / Butz 2014 (ref 15) | 应变孤子/位错的 DF-TEM invisibility criterion 基础 📜Q |
| Jiang 2018 (ref 20) / Schweizer 2018 (ref 21) | 机械力/原位畴壁操控——本文对比"剪切 vs 拉伸/压缩应变" 📜Q |
| Efimkin & MacDonald 2018 (ref 30) | 螺旋网络模型——"Chalker-Coddington 网络"未来方向 📜Q |
| Gorbachev 2007 (ref 27) | 双层石墨烯 2D 弱局域公式来源 📜Q |

> ⚠️ Phase S 外部对标（非本文引用，💭I）：E10/E12/E15 的 FP/AB/QH 干涉是**相干双路径干涉**，本文是**弱局域（相干背散射）**——不同量子干涉机制，勿混淆（判别逻辑见 [PHY-AB] vs 本文 §2.3）。

## 8. 对后续研究的影响
- 把畴壁研究从"单条通道"推进到"束内多通道耦合 + 电调"维度；栅压从"开关 QVH"升级为"调耦合旋钮"（作者自述，📜Q）。
- CVD 平台的可扩展性（大面积 back-diffusion 生长）为多通道网络提供了机械剥离不具备的材料基础 💭I。
- 留下理论任务：inter-wall 谷内背散射的定量低能有效理论（本文只做两条 LSW 的 Bloch 计算 + 定性）💭I。
- 提出 QVH qubit 类比（interdot coupling ↔ inter-wall coupling）作为远期方向（ref 31）📜Q。

## 9. 理论模型映射（供 tbplas / Kubo-Bastin / TBPM 对照）
| 映射 | 说明 |
|------|------|
| 双栅 → $\bar D,n$ | $\bar D=(D_b+D_t)/2$ 开隙、$n=D_b-D_t$ 调费米能 [PHY-GATE] 📜Q |
| $\bar D\to E_g$ | 低 $\bar D$<2 V/nm 时 $E_g\sim\bar D$（ref 25）📜Q |
| 畴壁态波函数 | $e^{-x/x_0}$、$x_0\propto 1/E_g$（ref 9）📜Q |
| 同谷反向传播 | AB/BA 与 BA/AB LSW 空间反演关联 → 同谷模反向 → 重叠即背散射 📜Q |
| 1D WL → $L_\phi$ | $G(B)-G(0)=-\frac{2e^2N}{hL}\left[\left(\frac{1}{L_\phi^2}+\frac{W^2}{3(\hbar/eB)^2}\right)^{-1/2}-L_\phi\right]$ 📜Q |
| TBPM 对标 | 构造 2 条（/7 条）平行 AB/BA + BA/AB 畴壁，扫层间偏压（on-site 偏移）→ 波函数重叠↓ → 计算 $\sigma_{xx}(B)$ 与 $L_\phi$ |

> 与 TBPM/Kubo 对应：本文 MC 是**有限尺寸相干输运量**（弱局域），bulk $\sigma_{xx}$ 只给背景；复现需有限器件 Landauer/Fisher-Lee 透射 + 相位相干（同 E12 §9 注记）💭I。

---

## Phase S 目的接口（三问引用式 + 增量价值）

- **Q1（edge state 如何表征）**：输运为主——墙导电（饱和 ~3.2 kΩ vs 无 LSW >100 kΩ）、束内耦合（每通道 ~0.43、$\Delta G\sim3e^2/h$）、MC 弱局域区分体/墙（3-LSW 体 2D WL vs 7-LSW 1D WL）、1D WL 提取 $L_\phi(\bar D)$；结构 = DF-TEM invisibility criterion（Burgers 矢量方向）+ IR-SNOM 定位 LSW（详见 §2/§4）。
- **Q2（理论如何复现）**：本文自带 Bloch 模式计算（两条 LSW、单谷、60/80 meV 体隙），机制 = 波函数重叠 $x_0\propto 1/E_g$ → 谷内背散射电调；无闭合网络 miniband（与 E12 不同，墙是开放的）📜Q。
- **Q3（理论↔实验对应）**：$\bar D\to E_g\to x_0\to$ 重叠 $\to$ 背散射 $\to L_\phi$；$\Delta G$ 增 ~3e²/h、MC 深 ~20%、$L_\phi$ 指数增长——三者统一归因于同一电调机制 📜Q。

> **增量价值**：E 序列里**第一篇弱局域（WL）通道**——区别于 E10/E12/E15 的 FP/AB/QH 相干双路径干涉；首次把"畴壁通道间耦合"用电场连续调控；CVD 平台（可扩展）vs 机械剥离。⚠️ 但 arXiv-only 未审、理论定性、SI 缺失。report.md §2 可引用其"体/墙 MC 判别 + 电调耦合"思路，但核心量化结论（$L_\phi$ 指数、~3e²/h）标注来源为预印本。

## 反向核对 pass (2026-09-01)
pdftotext -layout 提取正文（14 页，599 行），逐项 grep 核对：全部数字（160 nm/25 µm/4 mTorr/100 W/1050 °C/60 °C/min/500 sccm/30 sccm/2.2 sccm/1-3 h/200 keV/10 nA/80 cm/1 µm/20°/10.6 µm/40 nm Al₂O₃/5+40 nm/1+40 nm/2 K/~0.1 Torr/10 mV/1 kHz/1 MΩ/10 nA/50–200 nm/<50 nm/~1 µm/~400 nm/1.5 µm/400 nm/~3.2 kΩ/~8e²/h/>100 kΩ/~0.43/~3e²/h/0.8/1.0/1.6/1.5 V/nm/~20%/60/80 meV/D̄<2 V/nm/x₀∝1/Eg/波函数公式/1D·2D WL 公式/谷内背散射/空间反演）全部在原文找到。**全文无 ± 误差棒**（所有数字为 ~ 近似，故一律标 [~]/[相对]，无 [±]）。静电学原式在正文 "Results and Discussion"（$D_b,D_t$ 定义），晶格常数 $a_0$ 在 Fig. 4 caption。SI（Supplementary Note 1–7）无文件，正文引用处已如实标注"暂搁置"。

## 更正日志
| 日期 | 条目 |
|------|------|
| 2026-07-15 | 初版 review：基于 arXiv 摘要 + 领域背景推断，多处 NEEDS_VERIFICATION；附录 B 基于正文 §4（Fig. 4 + 弱局域分析）追加 |
| 2026-09-01 | **按 4 块辨识结构整体重读重写**（TL;DR + 系统辨识导览 + 判别表 + 结果/方法/数据/结论/局限/关系/影响/模型映射 + 三问接口 + 反向核对 + 更正日志）；全文 pdftotext + grep 反向核对 |
| 2026-09-01 | **修正旧 review 错误**：① 删 "Xu et al. Nature 572, 95 (2019)" 错误引用（Xu 2019 巨幅 AB 实为 Nat. Commun. 10, 4008，且本文未引用 Xu 2019）；② 旧附录 B 表 "3-LSW ΔG 单调下降" 混淆 $\Delta G$ 与 $G_{3LSW}$——按原文改为 "$\Delta G=G_7-G_3$ 在 $\bar D$>0.8 V/nm 增 ~3e²/h，其中 $G_3$ 均匀减（体电导）、$G_7$ 小增"；③ 旧 "分离 LSW 两条简并 vs 紧密堆积劈裂成键/反键" 为读图推断，原文只写 "overlap for states slightly above E=0" → 降级 💭I/📊F 表述 |
| 2026-09-01 | **核实 NEEDS_VERIFICATION**：① 期刊状态 = arXiv-only 预印本（CUHK 机构库仅登记 preprint，arXiv 无 journal-ref）；② 衬底 = Ni-Cu 梯度合金生长 + 转移至硅衬底（非 hBN 封装），底栅 = 硅衬底，顶介电 = 40 nm Al₂O₃；③ 器件几何 = 沟道 400 nm、条宽 1.5 µm；④ 温度 = 2 K；⑤ 全部生长/TEM/SNOM/测量参数已从 Methods 补齐 |
| 2026-09-01 | **SI 缺失声明**：正文引用 Supplementary Note 1–7 与 "Supplementary Information is available for this paper"，但 arXiv v1 无 ancillary 文件，SI 未取得 → 正文依赖 SI 的细节（底介电层 $d_b/\varepsilon_b$、器件参数、拟合细节）标注"暂搁置" |
