<!--
 * @Author       : AI 精读 (系统辨识式阅读法 → 三层分离整理)
 * @Date         : 2026-08-11（初读）→ 2026-09-01（按 4 块新架构重读）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/experiments/paper_review_E02_shimazaki2015_natphys.md
 * @Description  : E2: Shimazaki et al. 2015 — 双栅 BLG 电学产生/检测纯体谷流（VHE→IVHE 非局域输运 + 立方标度判据；纯 review）
-->

# Paper Review: Shimazaki et al. (2015) — 双栅 BLG 电学产生/检测纯谷流

| 字段 | 内容 |
|------|------|
| **编号** | E2 |
| **标题** | Generation and detection of pure valley current by electrically induced Berry curvature in bilayer graphene |
| **作者** | Y. Shimazaki, M. Yamamoto, I. V. Borzenets, K. Watanabe, T. Taniguchi, S. Tarucha |
| **期刊** | Nature Physics 11, 1032–1036 (2015) |
| **DOI / arXiv** | 10.1038/nphys3551（PDF 首页）/ 1501.04776（⚠️ arXiv，正文未出现，外部来源） |
| **类型** | 实验 — 非局域输运（电学产生/检测纯谷流，**非畴壁/非边缘态路线**） |
| **课题组** | Tarucha group（东京大学）+ Watanabe/Taniguchi（NIMS） |
| **PDF / SI PDF** | ✅ `reference/pdfs/Shimazaki 等 - 2015 - …pdf`（6 页期刊版）；❌ SI 缺失（暂搁置） |
| **精读日期** | 2026-08-11（初读）→ 2026-09-01（4 块新架构重读） |

> **共享知识引用**：静电学/双栅 n-D 换算用 `[PHY-GATE]`；费米能/CNP/能隙参考用 `[PHY-EF]`；Berry 曲率↔谷霍尔电导↔拓扑谷输运的联系用 `[PHY-BERRY]`。**本文核心物理（体谷霍尔效应 VHE + 非局域检测 + 立方标度判据）尚无现成锚点**，直接写在 review 内，通用性够 → 💭 可晋升 `[PHY-VHE]`。

---

## TL;DR

**本文想解决的问题**：双栅双层石墨烯（BLG）能否用**纯电学**手段（非局域输运）在**绝缘区、零磁场**下产生并检测**纯谷流**（有谷不平衡、无净电荷流）——即体谷霍尔效应（VHE），而非畴壁/边缘态路线？

**主结果**：① 绝缘区（带传导区 ρ<7 kΩ）非局域电阻 $R_{NL}$ 比 van der Pauw Ohmic 贡献大 **3 个数量级** 📜Q[相对]；② **立方标度** $R_{NL}\propto\rho^3$（与 $R_{NL}\propto(\sigma_{xy}^{VH})^2\rho^3$、$\sigma_{xy}^{VH}=4e^2/h$ 时一致，eq 6）——纯谷流的"指纹" 📜Q；③ 由 eq 3 反推谷间散射长度 $l_v=1.6\ \mu m$ 📜Q[~]。

**结论/意义**：非局域电阻的起源是"gap 内、电学诱导 Berry 曲率下的**纯体谷流**" 📜Q（原文 "transport mediated by pure bulk valley current in a gapped state with electrically induced Berry curvature"）；并显式**排除 Ohmic 与边缘态输运**两个竞争机制 📜Q。

---

## 1. 系统辨识导览（判别表为全文唯一权威）

**黑箱三要素**：`{输入旋钮 V_TG/V_BG/T | 输出观测量 R_L/R_NL/ρ_max(T)/R_NL^max(T) | 声称结论 = 纯体谷流} `

**四层变量图**（符号层一次钉死）：

| 层 | 本文实例 |
|----|----------|
| **L1 旋钮 u** | $V_{TG}$（顶 Au 栅）、$V_{BG}$（背 p-Si 栅）、$T$（主测量 70 K；Fig 4 inset 副器件 50 K；迁移率标定 1.5 & 70 K） |
| **L2 导出量 x₁** | $n$、$D$（$D_{BG}=\varepsilon_{BG}(V_{BG}-V_{BG}^0)/d_{BG}$、$D_{TG}=-\varepsilon_{TG}(V_{TG}-V_{TG}^0)/d_{TG}$、$D=(D_{BG}+D_{TG})/2$，Fig 2 caption 📜Q） |
| **L3 模型量 x₂** | $\Delta$（半能隙，能隙=2Δ）、$E_F$、$\Omega(E_F)$（eq 1）、$\sigma_{xy}^{VH}(E_F)$（eq 2）、$l_v$、$W,L$ |
| **固定参数（非旋钮）** | 迁移率 ~15 000 cm²/V·s（1.5 & 70 K）📜Q[~]；h-BN 厚度 top 21 nm / bottom 35 nm、SiO₂ 285 nm、接触 Ti/Au 10/190 nm（Methods）📜Q |
| **反推量 θ̂** | $l_v=1.6\ \mu m$、能隙 $2E_{1L}\approx 80\ meV$、$T_c(D)$、激活能 $E_{1L/2L},E_{1NL/2NL}$（从 $T$ 谱双指数拟合反推） |
| **L4 观测量 y** | $R_L=R_{57,38}$、$R_{NL}=R_{45,67}$、$\rho=R_L(W/L)$、$\rho^{max}$、$R_{NL}^{max}$ |

**可辨识性判别表**（唯一权威；本文四条判据）：

| 判别 | 判据（数据） | 排除谁 | 确立谁 |
|------|-------------|--------|--------|
| **Ohmic vs 谷流** | $R_{NL}$ 在 CNP + 垂直场下比 van der Pauw Ohmic 贡献（$R_{NL}=\frac{\rho}{\pi}e^{-\pi L/W}$）大 **3 个数量级**（Fig 2c）📜Q[相对] | 经典扩散 Ohmic 非局域电阻 | 非局域信号**非 Ohmic 起源** |
| **立方标度 = 谷流指纹** | 带传导区（ρ<7 kΩ）$R_{NL}\propto\rho^3$，与 eq 6（$\sigma_{xy}^{VH}=4e^2/h$ 时）一致（Fig 4 绿线）📜Q | 非立方标度机制（含线性边缘态） | **纯体谷流**（VHE→IVHE）——"unambiguous evidence of the valley transport" 📜Q |
| **边缘 vs 体** | 边缘拓扑局域态预期线性 $R_{NL}\propto\rho$，"does not fit any of the observed features"（Fig 4 蓝线）；Corbino 几何器件 ref 19 亦排除边缘局域态 📜Q | 拓扑边缘局域态输运 | 非局域电阻来自**体** |
| **机制自洽** | 立方标度仅在 gap 内/近 CNP（$\sigma_{xy}^{VH}\approx4e^2/h$ 恒定）成立；多器件 + 正/负 D 均复现（Fig 4 及 inset）📜Q | 单一器件偶然 / $\sigma_{xy}^{VH}$ 非常数 | 内在（intrinsic）VHE 机制 |

> **主结果 ↔ 判别表映射**：主结果① 大非局域电阻 ← {Ohmic vs 谷流}；主结果② 立方标度 ← {立方标度, 边缘 vs 体}；主结果③ $l_v=1.6\ \mu m$ ← {机制自洽（依赖 $\sigma_{xy}^{VH}=4e^2/h$ 代入 eq 3）}；主结果④ band/hopping 传导 + $T_c(D)$ ← 传导机制判别（独立于谷流，解释饱和区）。

> **[前提与限定]**（判别结论的适用范围）：
> - **噪声/扰动**：锁相 ~1 Hz；高温低 D 时非局域电压很小 → $T_c$ 低估（D<0.4 V/nm 偏离的两个可能原因之一，📜Q）；电压放大器输入阻抗泄漏造成 artefact（Supplementary Section I，正文声明误差不显著 📜Q）；eq 4/5 四个拟合参数均有 D 依赖、无解析关系（📜Q）。
> - **判别性扫轴**：扫 $T$（Fig 3，强依赖 >79 K）；扫 $D$（0.01–0.85 V/nm；Fig 4 主图 0.22–0.85）；扫 $n$（沿 CNP/ρ 轴）。**未测**：主测量零场（B 只用于迁移率/Hall 标定，正文未给主器件 W/L）。
> - **候选集 M 边界**：{Ohmic 扩散, 边缘态输运, 体谷流} —— 谷流在该集内唯一幸存。**集外候选未排除**：spin Hall（BLG 弱 SOC 为领域背景、非本文论证，本文只在 Supplementary Section IX 作类比、未显式排除）→ 封闭世界假设风险 💭I⚠️。
> - **公式有效性边界**：eq 3/6 仅在 $\sigma_{xx}\gg\sigma_{xy}^{VH}$ 时成立；饱和区（ρ>7 kΩ，hopping）eq 6 不适用（作者自陈，📜Q）。

三层标注：📜Q = 原文事实（附位置）｜推导｜📊F = 读图估算｜💭I = 推断。**不确定度（正交轴）**：[±] 原文误差棒 / [~] 原文以 ∼/≈/around 给出无误差棒 / [读图] 图·色标提取 / [相对] 仅相对量。所有数字经 pdftotext + grep 反向核对。

---

## 2. 结果与机制（按论文论证：机制 → 大信号/Ohmic 排除 → 传导判别 → 立方标度 → 边缘排除）

### 2.1 物理机制：gapped BLG 的 Berry 曲率 → VHE/IVHE（Fig 1）

垂直电场破坏空间反演对称 → BLG 开能隙 $2\Delta$ + 出现 Berry 曲率 $\Omega$（符号相反于两谷）📜Q。$\Omega$ 是动量空间"赝磁场"，经反常速度产生横向**纯谷流**（谷霍尔效应 VHE）；逆效应 IVHE 把谷流转回电压 → 非局域电阻 📜Q。公式（引 refs 10,20,21）：

$$\Omega(E_F)=\tau_z\frac{\hbar^2}{m}\frac{\Delta\sqrt{E_F^2-\Delta^2}}{E_F^3}\qquad(1)\quad\text{（仅 }|E_F|\geq\Delta\text{）}$$

$$\sigma_{xy}^{VH}(E_F)=\begin{cases}\dfrac{4e^2}{h}\dfrac{\Delta}{|E_F|},&|E_F|\geq\Delta\\[4pt]\dfrac{4e^2}{h},&|E_F|<\Delta\end{cases}\qquad(2)$$

- $\tau_z$ = 谷指标（K: −1，K′: +1）；$m$ = 无破缺 BLG 有效质量 📜Q。$\sigma_{xy}^{VH}$ 在 gap 内**饱和到 $4e^2/h$**（价带全部占据态都贡献 VHE）📜Q；有限 T 下略降，但本文 D 范围内几乎恒等于 $4e^2/h$（Supplementary Section X）📜Q。

### 2.2 大非局域电阻 + Ohmic 排除（Fig 2）

$R_L,R_{NL}$ 的栅压二维图：CNP 处 $R_L$ 随 D 增大（能隙打开）；$R_{NL}$ 亦随 D 增大、且在 CNP 最大 📜Q。非局域检测方案与自旋霍尔效应完全类比（eq 3，引 ref 23）：

$$R_{NL}=\frac{1}{2}\left(\frac{\sigma_{xy}^{VH}}{\sigma_{xx}}\right)^2\frac{W}{L}\exp\left(-\frac{L}{l_v}\right)\qquad(3)$$

- $R_{NL}$ 在 CNP+垂直场下比 Ohmic 贡献大 **3 个数量级**（Fig 2c，Ohmic 曲线放大 1000 倍仍远低于 $R_{NL}$）📜Q[相对] → 排除 Ohmic。
- 交换测量端子 $R_{45,67}\sim R_{67,45}$ 不变（reciprocity，Supplementary Section II）📜Q。

### 2.3 传导机制判别：band vs hopping + $T_c$（Fig 3）

高温 = 跨能隙热激活（band conduction），低温 = 杂质态间跳跃（hopping）📜Q。$\rho^{max}$ 与 $R_{NL}^{max}$ 的 $1/T$ 双指数拟合（eq 4/5）：

$$\frac{1}{\rho^{max}}=\frac{1}{\rho_1}e^{-E_{1L}/k_BT}+\frac{1}{\rho_2}e^{-E_{2L}/k_BT}\qquad(4),\qquad \frac{1}{R_{NL}^{max}}=\frac{1}{R_1}e^{-E_{1NL}/k_BT}+\frac{1}{R_2}e^{-E_{2NL}/k_BT}\qquad(5)$$

- 高 T 段激活能 $2E_{1L}$ = 能隙大小，最高 D 处 **≈80 meV** 📜Q[~]（Supplementary Section IV）。
- $T_c$（band/hopping 交叉）：$D>0.4$ V/nm 时 $\rho^{max}$ 与 $R_{NL}^{max}$ 的 $T_c$ 吻合（局域/非局域关联）；$D<0.4$ V/nm 偏离，两可能原因：① 高温低 D 非局域电压太小 → $T_c$ 低估；② 谷流对电荷 puddle 不如局域输运敏感（作者自陈"未完全理解"）📜Q。
- 注意点：局域与非局域的高 T 激活能**不同** → 已暗示 $R_{NL}$ 与 $\rho$ **无线性关系**（与单层石墨烯 ref 12 报告不同）📜Q。

### 2.4 核心证据：立方标度 $R_{NL}\propto\rho^3$ + $l_v$ 提取（Fig 4）

假定 $l_v$ 恒定、代入 $\sigma_{xx}=\rho^{-1}$ 到 eq 3：

$$R_{NL}\propto(\sigma_{xy}^{VH})^2\,\rho^3\qquad(6)$$

- 带传导区（ρ<7 kΩ）$R_{NL}$ 随 $\rho$ **立方标度**（Fig 4 绿线）📜Q[~]；hopping 区（ρ>7 kΩ）**饱和** 📜Q[~]。
- 立方标度仅在 $\sigma_{xy}^{VH}$ 恒定（gap 内/近 CNP，$=4e^2/h$）时成立 → 观察到的立方关系 = **谷输运的确凿证据**（"unambiguous evidence"）📜Q。
- 用 $\sigma_{xy}^{VH}=4e^2/h$ 代入 eq 3 → **$l_v=1.6\ \mu m$** 📜Q[~]，与既往谷间散射长度估计（refs 12,29）可比 📜Q。
- 不同四端子组测到 $R_{NL}$ 随 L 显著加快衰减（Supplementary Section V）——归因于边缘散射导致的谷弛豫（弱局域研究 ref 29）📜Q。
- 多器件复现：立方 + 饱和标度在多个器件、不同 n/T 均得到（Fig 4 inset 副器件 D=+0.51…0.75 与 −0.50…−0.76 V/nm）📜Q。

### 2.5 竞争机制排除：边缘态输运

gap 内 BLG 边缘可能存在的拓扑局域态（ref 31 预言）也可能贡献非局域输运；大能隙下体 shunting 小、边缘输运主导 → 此时 $R_{NL}$ 应正比于四端局域电阻（**线性标度**）📜Q。该线性标度"does not fit any of the observed features"（Fig 4 蓝线），且考虑体 shunting 后仍远离立方线（Supplementary Section X）📜Q。**结论**：排除边缘输运，起源是 gap 内**体谷流** 📜Q。另：Corbino 几何器件（ref 19）也证伪了边缘局域态输运 📜Q。

---

## 3. 实验方法

### 3.1 器件
机械剥离 BLG + h-BN，PMMA 转移（ref 34）到 SiO₂/Si（SiO₂ 285 nm、Si 重 p 掺杂做背栅）；Ti/Au（10/190 nm）欧姆接触；Ar 等离子刻 Hall bar；AFM 机械清洁（refs 35–37）；顶 h-BN + Ti/Au 顶栅；每步 300 °C Ar/H₂ 退火（除欧姆接触—刻蚀之间）📜Q（Methods）。BLG 迁移率 ~15 000 cm²/V·s（1.5 & 70 K）📜Q[~]。顶/底 h-BN 厚度 21/35 nm（AFM）📜Q。主器件 Hall bar 的 $W,L$ 正文未给（⚠️ SI 缺失，待补）；Fig 4 inset 副器件 $W=1\ \mu m$、$L=4.5\ \mu m$ 📜Q。

### 3.2 静电学（推导见 [PHY-GATE]，本文数值在此）
双栅独立调 $n$ 与 $D$（共模/差模，[PHY-GATE] §5）。本文 D 定义：$D_{BG}=\varepsilon_{BG}(V_{BG}-V_{BG}^0)/d_{BG}$、$D_{TG}=-\varepsilon_{TG}(V_{TG}-V_{TG}^0)/d_{TG}$、$D=(D_{BG}+D_{TG})/2$（Fig 2 caption，含环境掺杂偏移 $V^0$）📜Q。$\rho=R_L(W/L)$ 定义 📜Q。注意：gapped 区 $E_F$ 在能隙内时 $n\approx0$（[PHY-GATE] §9 电荷密度 vs 载流子密度）。

### 3.3 测量
低频锁相 ~1 Hz、主测量 70 K、副器件 50 K 📜Q[~]。四端电阻 $R_{ij,kl}$ = i,j 间电压 ÷ k,l 间注入电流；$R_L=R_{57,38}$、$R_{NL}=R_{45,67}$（除非另注）📜Q。Fig 4 inset 用高输入阻抗自研电压放大器抑制泄漏 artefact（Supplementary Section I）📜Q。

---

## 4. 关键数据（提取链 + 验证链 + 不确定度标注）

| 量 | 值 | 来源/不确定度 |
|------|-----|---------------|
| 迁移率 | ~15 000 cm²/V·s（1.5 & 70 K） | 📜Q Fig 1 caption [~] |
| 主测量温度 / 锁相频率 | 70 K / ~1 Hz（副器件 50 K） | 📜Q 正文+Methods [~] |
| $R_{NL}$ vs Ohmic | 大 **3 个数量级** | 📜Q [相对] |
| 立方标度区 / 饱和区 | ρ<7 kΩ / ρ>7 kΩ | 📜Q [~] |
| $l_v$ | **1.6 μm** | 📜Q [~]（依赖 $\sigma_{xy}^{VH}=4e^2/h$ 代入 eq 3） |
| 能隙 $2E_{1L}$（最高 D） | **≈80 meV** | 📜Q [~]（Supplementary Section IV） |
| $\sigma_{xy}^{VH}$（gap 内） | $4e^2/h$ | 📜Q eq 2 [~] |
| band/hopping 交叉温度 | $D>0.4$ V/nm 吻合 / $D<0.4$ 偏离 | 📜Q |
| D 范围（Fig 4 主图 / inset） | 0.22–0.85 / +0.51…0.75 & −0.50…−0.76 V/nm | 📜Q Fig caption [~] |
| 副器件 Hall bar W×L | 1 μm × 4.5 μm | 📜Q Fig 4 inset caption [~] |
| h-BN / SiO₂ / 接触 | 21 & 35 nm / 285 nm / Ti/Au 10/190 nm | 📜Q Methods [~] |
| 退火 | 300 °C Ar/H₂ | 📜Q Methods |

**验证链**：① 大信号 + 非 Ohmic（Fig 2c）；② 立方标度 ↔ eq 6（Fig 4 绿线）；③ 多器件/正负 D 复现（Fig 4 及 inset）；④ $l_v=1.6\ \mu m$ 与既往估计（refs 12,29）可比；⑤ 边缘线性标度不符 + Corbino（ref 19）双排除。**⚠️ 主器件 $W,L$ 正文未给**（SI 缺失），$l_v$ 提取依赖该几何参数，正文未给出独立交叉验证。

---

## 5. 主要结论
1. 双栅 BLG 在**绝缘区、零磁场**下产生/检测**纯体谷流**（VHE→IVHE），非局域电阻比 Ohmic 大 3 个数量级 📜Q。
2. 核心指纹 = **立方标度** $R_{NL}\propto\rho^3$（带传导区 ρ<7 kΩ），与 $\sigma_{xy}^{VH}=4e^2/h$ 时 eq 6 一致 → "unambiguous evidence of the valley transport" 📜Q。
3. 排除 Ohmic 与**拓扑边缘态输运**（线性标度不符 + Corbino ref 19）两个竞争机制 📜Q。
4. $l_v=1.6\ \mu m$，能隙（最高 D）≈80 meV；band（高 T）/hopping（低 T）传导交叉温度 $T_c(D)$ 📜Q。
5. 谷流完全由电学栅控（能隙、费米能、破缺反演对称三参数）📜Q——为 $\sigma_{xx}<\sigma_{xy}^{VH}$ 区与无耗散电子学铺路 📜Q。

## 6. 局限与未解决
| 局限 | 说明 | 证据 |
|------|------|------|
| eq 3/6 仅 $\sigma_{xx}\gg\sigma_{xy}^{VH}$ 成立 | 饱和区（ρ>7 kΩ）eq 6 不适用 | 📜Q |
| 饱和机制未定论 | 提两个候选：反常霍尔标度 $\sigma_{xy}\propto\sigma_{xx}^{1.6}$（ref 13）、side-jump 外禀贡献使 $\sigma_{xy}^{VH}<4e^2/h$；均需进一步实验/理论 | 📜Q |
| $T_c$ 偏离（D<0.4）未完全解释 | 谷流对电荷 puddle 不敏感的原因"未完全理解" | 📜Q |
| 主器件 W/L 未给（SI 缺失） | $l_v$ 提取的几何参数无法独立核对 | ⚠️ SI 缺失 |
| 未显式排除 spin Hall | BLG 弱 SOC 是领域背景，非本文论证 | 💭I⚠️ |
| 无 B 依赖/无实空间证据 | 体谷流是输运反推，无谷分辨直接成像 | 💭I |

## 7. 与其他工作的关系（跨论文对标放这里）
| 工作 | 关系 |
|------|------|
| Gorbachev 2014（ref 12，单层石墨烯/h-BN） | 谷霍尔效应的金属区先例；本文补**绝缘区**（更适合纯谷流）📜Q |
| Ju 2015（ref 32，E1，畴壁拓扑谷输运）/ Sui 2015（ref 33） | Note added in proof：AB–BA 畴壁拓扑谷流与本文同源于 gap 内非零 $\sigma_{xy}^{VH}$（非零谷 Chern 数）📜Q |
| Li 2010（ref 31，绝缘 BLG 亚能隙电导拓扑起源）/ Yan & Fuhrer 2010（ref 19，Corbino） | 边缘态候选 / Corbino 排除依据 📜Q |
| 反常霍尔效应（ref 13，Nagaosa 2010） | 金属↔hopping 交叉标度 $\sigma_{xy}\propto\sigma_{xx}^{1.6}$ 的类比来源 📜Q |

> ⚠️ Phase S 外部对标：本文是**体**谷霍尔效应（无畴壁、无 B、非局域 + 立方标度判据），与 E1/E3/E7 的**畴壁/EFW 拓扑谷输运**是两条互补路线（cards.md E2 卡片已标注"不直接研究畴壁，提供体效应路线"）。

## 8. 对后续研究的影响
- 首次把谷霍尔效应推进到**绝缘区**（转换耗散更低、注入电流更小），此前 spin/valley Hall 体系未达 📜Q。
- 确立"立方标度 $R_{NL}\propto\rho^3$"为纯谷流（体 VHE）的可辨识判据，可复用于后续谷流检测 📜Q。
- 留下理论任务：绝缘区（$\sigma_{xx}<\sigma_{xy}^{VH}$）谷霍尔效应的饱和/交叉标度需新公式（常规公式不适用）📜Q。

## 9. 理论模型映射（供 tbplas / Kubo-Bastin 对照）
| 映射 | 说明 |
|------|------|
| $D\to\Delta$ | 垂直场 → 半能隙 Δ（能隙 2Δ ≈ 80 meV @ 最高 D）📜Q |
| $\Omega(E_F)$、$\sigma_{xy}^{VH}(E_F)$ | eq 1/2（refs 10,20,21 的 gapped BLG Berry 曲率/谷霍尔电导）📜Q |
| $R_{NL}\leftrightarrow\sigma_{xy}^{VH},\sigma_{xx}$ | eq 3 非局域输运（spin Hall 类比）；立方标度 eq 6 📜Q |
| 观测量 $\rho,\ R_{NL}$ | $\rho=R_L(W/L)$；$R_{NL}$ 是有限几何器件量（需 Landauer/Fisher-Lee，bulk $\sigma_{xy}^{VH}$ 只给材料本征量）💭I |

> 与 TBPM/Kubo 对应：$\sigma_{xy}^{VH}$ 是**体**本征响应（Kubo 可算，含 Berry 曲率）；$R_{NL}$ 的非局域检测依赖 Hall bar 几何 + $l_v$ 扩散，复现需有限器件透射计算（同 E12 §9 注记）💭I。

---

## Phase S 目的接口（三问引用式）

- **Q1（edge state 如何表征）**：本文**不表征边缘态**——反而是**显式排除边缘态**作为非局域电阻来源（线性标度不符 + Corbino ref 19），确立**体**谷霍尔效应路线（见 §2.2/§2.5）。与畴壁路线（E1/E3/E7）互补。
- **Q2（理论如何复现）**：gapped BLG 的 $\Omega(E_F)$、$\sigma_{xy}^{VH}(E_F)$（eq 1/2，refs 10,20,21）+ 非局域输运 eq 3（ref 23 spin Hall 类比）→ 立方标度 eq 6 📜Q。
- **Q3（理论↔实验对应）**：$\sigma_{xy}^{VH}=4e^2/h$（gap 内）↔ 立方标度成立；能隙 2Δ≈80 meV ↔ D；$l_v=1.6\ \mu m$ ↔ 非局域衰减。

> **增量价值**：给 report.md 提供"谷输运两条路线"的对照锚点——**体 VHE**（本文 E2：无畴壁、零场、非局域 + 立方标度 $R_{NL}\propto\rho^3$）vs **畴壁/边缘拓扑谷输运**（E1/E3/E7）。cards.md E2 的"体效应路线"定位在此得到证据支撑（立方标度判据 + 边缘态显式排除）。

## 反向核对 pass (2026-09-01)
pdftotext -layout 提取 6 页期刊版正文（/tmp/e2.txt），逐项 grep 核对：~15 000 cm²/V·s（Fig 1 caption）、70 K/50 K/~1 Hz、3 个数量级、立方标度 $R_{NL}\propto\rho^3$ 与 eq 6、$\sigma_{xy}^{VH}=4e^2/h$（eq 2）、$l_v=1.6\ \mu m$、2E1L≈80 meV、ρ<7 kΩ / >7 kΩ、D=0.22–0.85 与 inset ±0.50…0.76、W×L=1×4.5 μm、21/35 nm、285 nm、10/190 nm、300 °C、van der Pauw、$\sigma_{xy}\propto\sigma_{xx}^{1.6}$、$R_{45,67}\sim R_{67,45}$、Corbino、>79 K、D>0.4/<0.4 V/nm、note added in proof（Ju 2015/Sui 2015）——均在原文找到。⚠️ 澄清：本文为**纯电学**方法，正文无"圆偏振光"实验（optical 仅指 intro 的 TMDC 光学调控与 Methods 的层数辨识）；主器件 W/L 正文未给（SI 缺失）。

## 更正日志
| 日期 | 条目 |
|------|------|
| 2026-09-01 | **按 4 块新架构整体重写**（系统辨识式阅读法）：新增 TL;DR 问题句式、四层变量表、可辨识性判别表（Ohmic/立方标度/边缘 vs 体/自洽）、主结果↔判别映射、[前提与限定] 块、关键数据表、理论模型映射、反向核对 pass |
| 2026-09-01 | **旧 review 无源/过强论断修正**：① "谷流衰减长度 ~2–3 μm" → 原文 $l_v=1.6\ \mu m$（删改）；② "谷信号 100 K 以下可观测" → 原文无此说，实际主测量 70 K、副器件 50 K、band conduction >79 K（删改）；③ "非局域信号幅度小 (~Ω)" → 相反，原文 $R_{NL}$ 比 Ohmic 大 3 个数量级（Fig 4 达 ~10³ Ω 量级）（修正）；④ "栅压反转→信号反转→排除热电/接触" → 原文**无符号反转实验**，核心证据是立方标度 $R_{NL}\propto\rho^3$（删除/改述） |
| 2026-09-01 | **主题澄清**：本文是**体谷霍尔效应**（非局域输运、零场、无畴壁），非"圆偏振光"方法（圆偏振仅出现在 intro 的 TMDC 光学语境） |
