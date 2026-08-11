<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 17:14:09
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 17:14:12
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/helical_network/paper_review_efimkin2018_prb.md
 * @Description  :
-->
<!--
 * @Author       : AI精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/note/helical_network/paper_review_efimkin2018_prb.md
 * @Description  : T9: Efimkin & MacDonald 2018 — 螺旋网络模型的系统理论构建
-->

# 论文精读：Efimkin & MacDonald, PRB (2018)

> **Dmitry K. Efimkin, Allan H. MacDonald**
> "Helical network model for twisted bilayer graphene"
> PRB 98, 035404 (2018) | arXiv:1803.06404
>
> 作者单位：The University of Texas at Austin

---

## 1. 一句话总结

为小角度 TBG + 位移场下的低能电子结构建立了**唯象螺旋网络模型**：畴壁上的拓扑螺旋态构成三角网络，能带无隙、含 Dirac 点，态密度在能量上周期性振荡（每周一个零点 + 一个发散）。

---

## 2. 背景与动机

### 2.1 已有知识背景

- BLG + 位移场 → AB/BA 堆叠能隙打开，谷陈数非平庸 → AB/BA 边界束缚拓扑螺旋态（THS）
- Huang et al. 2018 (PRL) 刚用 STM 观测到 mTBG 的 THS 网络——但缺乏系统理论
- San-Jose & Prada 2013 已提出网络模型雏形，但未给出完整能带结构和色散

### 2.2 本文填补的空白

需要从连续模型出发，**严格推导**出描述 THS 网络的低能有效理论，给出可实验检验的能带结构、态密度和对称性预言。

---

## 3. 方法与模型

### 3.1 连续模型 → 2-band 投影

起点：4-band $k \cdot p$ 连续模型（valley $K$，sublattice $\otimes$ layer 空间）：

$$H_0 = \begin{pmatrix} v\boldsymbol{\sigma}_t \cdot \mathbf{p} - u & T(\mathbf{r}) \\ T^\dagger(\mathbf{r}) & v\boldsymbol{\sigma}_b \cdot \mathbf{p} + u \end{pmatrix}$$

层间隧穿 $T(\mathbf{r}) = \frac{w}{3}\sum_{i=1}^3 e^{-i\mathbf{k}_i \cdot \mathbf{r}} T_i$，其中 $\mathbf{k}_i$ 连接两层 Dirac 点。

**关键投影**（大位移场 $L \ll u \sim w$）：投影到上层导带 + 下层价带的 2-band 子空间：

$$H_{\text{2-band}} = \begin{pmatrix} v(p - p_u) & t_P + t_S \\ t_P^* + t_S^* & -v(p - p_u) \end{pmatrix}$$

其中 $t_P(\phi_p, \mathbf{r}) = [T_{BA}e^{-i\phi_p} - T_{AB}e^{i\phi_p}]/2$ 有 $p$-波对称性。

### 3.2 局域能隙的各向异性

$$^2_p = \delta_-^2 \cos^2[\phi_p - \Theta] + \delta_+^2 \sin^2[\phi_p - \Theta]$$

- **畴壁条件**：$|T_{AB}| = |T_{BA}| \Rightarrow \delta_- = 0$ → 能隙闭合
- $\Theta(\mathbf{r}) = (\arg[T_{BA}] - \arg[T_{AB}])/2$ 给出动量空间能隙最小方向
- $\delta_-$ 在畴壁处改变符号 → 谷陈数跳变 $\Delta C = 2$

### 3.3 网络模型构建

每根畴壁 = 1D Jackiw-Rebbi 零模，色散 $\epsilon_p = v p_\parallel$。

三条畴壁在 AA 堆叠点交汇 → 散射矩阵 $S$（3×3），由 $C_{3z}$ + $\mathcal{T}$ 约束：

$$S = \begin{pmatrix} 0 & t & r \\ r & 0 & t \\ t & r & 0 \end{pmatrix}$$

其中 $|t|^2 + |r|^2 = 1$，$t/r$ 由 AA 点能隙决定。

---

## 4. 核心结果

### 4.1 网络能带结构

能带方程为（Bloch 定理 + $S$ 矩阵）：

$$\cos(q_n^0 L_\parallel) = \frac{1 - 2|t|^2}{2|t|^2}$$

能带无隙，含 Dirac 锥（$K, K', \Gamma$ 点）。能带结构仅依赖一个参数 $\alpha = |t/r|$。

### 4.2 态密度（DoS）

$\rho(E)$ 在能量上**周期性振荡**，周期 $\sim L = 2\pi\hbar v/L$：
- 每周一个 Van Hove 奇点（发散）
- 每周一个 DoS 零点（Dirac 点处）

→ 实验 signature：STM $dI/dV$ 在畴壁上应出现多峰结构，峰值间距 $\propto 1/L \propto \theta$

### 4.3 与 continuum 模型的对比

网络模型在 $|E| < \delta_+$ （AB/BA 堆叠能隙内）精确成立 → 低能有效理论。超出此能区需回到 full continuum 模型。

---

## 5. 与其他工作的关系

| 相关工作 | 关系 |
|----------|------|
| San-Jose & Prada 2013 PRB | 网络模型发起者；本文是系统化、严格化版本 |
| Huang et al. 2018 PRL | 实验同时期发表，STM 观测到 THS 网络 — 本文提供理论框架 |
| Chalker-Coddington 模型 | 方法论祖先（QH 网络模型） |
| Tsim & Koshino 2020 (TZM) | 后继挑战者：TZM 认为网络不连通 |

---

## 6. 亮点与局限

### 亮点
- **从连续模型严格推导**出网络模型，而非唯象假设
- **$\delta_-$ 符号变化 → 谷陈数跳变** 的几何解释清晰
- DoS 周期的解析表达式 → 可直接与 STM 对比
- 仅用一个参数 $\alpha$ 控制全部能带拓扑

### 局限
- **假设 AA 点是连通的散射节点** — 这是网络模型 vs TZM 的核心分歧
- 忽略了同一链路上两条螺旋通道间的散射（要求 $L \ll w \sim u$）
- 未考虑无序、有限温度、非均匀应变
- 仅 AB/BA 畴壁；未处理 AA 堆叠区内的态

---

## 7. 与用户研究的关联

| 维度 | 关联 |
|---|---|
| **方法** | 网络 $S$ 矩阵 + Bloch 定理 → 可数值对角化验证（与 tbplas 互补） |
| **扩展方向** | DW 项目中可验证：不同位移场下 $\delta_-$ 的空间分布 |
| **可验证性** | DoS 周期 $\propto 1/L$ 可用 tbplas LDOS 计算直接检验 |

---

## 8. 关键公式速查

| 量 | 表达式 |
|-----|--------|
| 局域能隙 | $\delta_\pm(\mathbf{r}) = (\|T_{BA}\| \pm \|T_{AB}\|)/2$ |
| 谷陈数 | $C = \delta_-/\|\delta_-\|$ — 畴壁两侧符号相反 |
| 畴壁螺旋态色散 | $\epsilon_p = v p_\parallel$（无质量 1D Dirac） |
| 网络能带方程 | $\cos(q_n^0 L_\parallel) = (1-2\|t\|^2)/(2\|t\|^2)$ |
| DoS 周期 | $E_{\text{period}} \sim L = 2\pi\hbar v/L$ |

---

*报告生成日期：2026-08-06 | 基于 PDF pdftotext 精读*

---

## Phase S 补充 (2026-08-11): Q2/Q3

### Q2: 理论如何解释 edge state?
TBG 连续模型投影到双带子空间 → 螺旋网络模型：每条畴壁承载 1D 手征模，AA 点散射连接为三角形网络。网络能带无隙，态密度周期性振荡随 moire 尺度缩放。mTBG 畴壁态标准低能理论框架。

### Q3: 理论如何与实验结合?
为 Huang 2018 (STM 螺旋态) 和 Rickhaus 2018 (输运网络) 提供直接理论解释。定义了后续几乎所有 mTBG 畴壁网络理论研究的基准语言。
