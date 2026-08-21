<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 17:17:00
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 17:17:01
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T10_ramires2018_prl.md
 * @Description  :
-->
<!--
 * @Author       : AI精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T10_ramires2018_prl.md
 * @Description  : T10: Ramires & Lado 2018 — 电场可调的人工规范场与赝朗道能级
-->

# 论文精读：Ramires & Lado, PRL (2018)

> **A. Ramires, J. L. Lado**
> "Electrically Tunable Gauge Fields in Tiny-Angle Twisted Bilayer Graphene"
> PRL 121, 146801 (2018) | DOI: 10.1103/PhysRevLett.121.146801
>
> 作者单位：ETH Zurich

---

## 1. 一句话总结

小角度 TBG + 位移场 = **电场可调的人工规范场** $g \propto U \cdot \theta$，产生赝朗道能级（pLL），态密度中出现平坦能带 + 谷极化局域态，且局域化长度随偏压增大而减小。

---

## 2. 背景与动机

### 2.1 已有知识背景

- TBG 小角度下 AB/BA 畴壁束缚拓扑通道（San-Jose 2013, Efimkin 2018）
- 应变石墨烯可产生赝磁场（$\sim 300$T），但不可电控
- 位移场 $U$ 使 AB/BA 区打开能隙，但在畴壁上能隙闭合

### 2.2 本文填补的空白

**首次揭示**：层间偏置 $U$ 不仅打开能隙，更重要的是在 TBG 中产生**等效的非阿贝尔规范场**，其强度 $\propto U \cdot \theta$ —— 这意味着 pLL 的能量和局域化可通过栅压**连续电控**，无需应变。

---

## 3. 方法与模型

### 3.1 有效 2-band 模型

将 4-band 连续模型投影到上层导带 + 下层价带的 2-band 子空间，得到有效哈密顿量：

$$H_{\text{eff}} = \gamma_x(\partial_x^2 - \partial_y^2) + i\gamma_y(\partial_x\partial_y + \partial_y\partial_x) + \cdots$$

通过 Peierls 替换 $\partial_{x,y} \to \partial_{x,y} + g_{x,y}(\mathbf{r})$，提取出人工规范场 $g_{x,y}(\mathbf{r})$。

### 3.2 规范场的解析形式

$$g_x(\mathbf{r}) = \frac{A_x\gamma_x - iA_y\gamma_y}{2(\gamma_x^2 + \gamma_y^2)}, \quad g_y(\mathbf{r}) = \frac{A_y\gamma_x - iA_x\gamma_y}{2(\gamma_x^2 + \gamma_y^2)}$$

其中 $A_x, A_y \propto \partial U(\mathbf{r})$，即规范场来源于**偏置的空间梯度**。

**关键标度**：$g_{x,y} \sim U \cdot k_M \sim U \cdot \theta$（小角度下 $k_M \propto \theta$）

### 3.3 验证方法

紧束缚数值计算验证 pLL 的三个判据：
1. $\partial E_n/\partial g > 0$（能量随规范场增大）
2. 局域化长度 $\ell \propto 1/\sqrt{g}$（类似磁长度 $l_B \propto 1/\sqrt{B}$）
3. 谷极化（单谷有效模型的要求）

---

## 4. 核心结果

### 4.1 规范场的空间结构

- $g(\mathbf{r})$ 在 AB/BA 畴壁处最大，AA 点处最小
- 规范场的空间分布与摩尔周期 $L_M$ 一致
- 矢量场 $g(\mathbf{r})$ 的旋度 $\nabla \times g$ 对应赝磁场 $B_{\text{ps}}$

### 4.2 赝朗道能级

- 偏压 $U=0$：无能隙，无 pLL
- $U \neq 0$：在电荷中性点附近出现**平坦能带**（pLL）
- pLL 能量随 $U$ 增大而升高：$\partial E_n/\partial U > 0$
- pLL 态在**实空间中局域化**，局域化长度随 $U$ 增大而减小

### 4.3 谷极化

pLL 态是**谷极化的**——来自单谷有效模型的自然结果。不同谷的 pLL 态空间分离。

---

## 5. 与其他工作的关系

| 相关工作 | 关系 |
|----------|------|
| San-Jose & Prada 2013 | 畴壁拓扑通道的原始预言——本文提供新的理解角度：规范场 |
| Efimkin & MacDonald 2018 | 螺旋网络模型——本文从规范场视角看畴壁态局域化 |
| Zheng et al. 2022 (PRL) | 实验：STM 观测到 PLL 在 Kagome 晶格中 — 本文的理论预言与之吻合 |
| Guinea et al. 2010 (应变赝磁场) | 应变产生赝磁场——本文用**电场**替代应变，可连续电控 |

---

## 6. 亮点与局限

### 亮点
- **电控赝磁场**：$g \propto U \cdot \theta$ → 栅压取代应变，实验操作性极强
- **三判据验证**：能量标度 + 局域化 + 谷极化，逻辑链完整
- 统一了畴壁拓扑态和赝朗道能级的理解

### 局限
- 2-band 有效模型仅在 $U \ll t_\perp$ 有效
- 未考虑晶格弛豫效应（后来 Tsim & Koshino 2020 补充）
- 规范场提取依赖于低能展开，高能修正未知
- 未给出可与输运实验直接对比的电导预言

---

## 7. 与用户研究的关联

| 维度 | 关联 |
|---|---|
| **方法** | pLL 局域化判据可用 tbplas LDOS 计算独立验证 |
| **扩展方向** | DW 项目中 EFW 的规范场描述 → 统一畴壁态和 pLL 的理解 |
| **可验证性** | $\partial E_{\text{pLL}}/\partial U$ 标度律可用 tbplas 直接检验 |

---

## 8. 关键公式速查

| 量 | 表达式 |
|-----|--------|
| 规范场-偏压标度 | $g \sim U \cdot \theta$ |
| 赝磁场 | $B_{\text{ps}} = \nabla \times g$ |
| pLL 能量标度 | $\partial E_n/\partial U > 0$（类比 $\partial E_n/\partial B > 0$） |
| 局域化长度 | $\ell \propto 1/\sqrt{g} \propto 1/\sqrt{U\theta}$ |

---

*报告生成日期：2026-08-06 | 基于 PDF pdftotext 精读*

---

## Phase S 补充 (2026-08-11): Q2/Q3

### Q2: 理论如何解释 edge state?
垂直电场在 moire 超晶格中产生有效规范场 → 畴壁态获得赝磁场特征，局域化为类赝朗道能级态。局域长度由偏压控制。电场-应变赝磁场的电控类比。

### Q3: 理论如何与实验结合?
预言偏压依赖的平带和局域态——STM/输运可见。提供无机械应变的 moire 量子态电控路径。
