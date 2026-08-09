<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 17:17:55
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 17:17:57
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/helical_network/paper_review_hou2020_prb.md
 * @Description  :
-->
<!--
 * @Author       : AI精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/note/helical_network/paper_review_hou2020_prb.md
 * @Description  : T11: Hou et al. 2020 — 金属畴壁网络的电子结构与输运
-->

# 论文精读：Hou et al., PRB (2020)

> **Tao Hou, Yafei Ren, Yujie Quan, Jeil Jung, Wei Ren, Zhenhua Qiao**
> "Metallic network of topological domain walls"
> PRB 101, 201403(R) (2020) | arXiv:1904.12826
>
> 作者单位：USTC (Qiao group), Univ. of Seoul (Jung), Shanghai Univ.

---

## 1. 一句话总结

用 TB + Landauer-Büttiker 全面分析了谷陈数畴壁网络的电子和输运性质：**体态为半金属**（Dirac 色散），**锯齿边纳米带出现近量子化电导** $G \approx e^2/h$，**三叉戟边纳米带因有限尺寸效应打开小能隙**。

---

## 2. 背景与动机

- 实验上已在 mTBG 中观测到畴壁导电网络（Huang 2018, Rickhaus 2018）
- 但网络的**输运性质**（体态 vs 边缘态、量子化条件、无序效应）尚未系统研究
- 使用简化模型（单层石墨烯 + 交错子晶格势）抓住 mTBG 畴壁网络的拓扑本质

---

## 3. 方法与模型

### 3.1 简化模型

**核心简化**：用单层石墨烯的 AB 子晶格交错势 $U_A = -U_B = \pm\lambda\Delta$ 模拟 mTBG 的 AB/BA 谷陈数畴区。

$$H = -t\sum_{\langle ij\rangle} c_i^\dagger c_j + \sum_{i\in A} U_A c_i^\dagger c_i + \sum_{j\in B} U_B c_j^\dagger c_j$$

- $t = 2.6$ eV, $\Delta = 0.1t$（能隙 $2\Delta = 0.2t$）
- 畴壁处 $U_A, U_B$ 改变符号 → 谷陈数跳变 → ZLM

### 3.2 输运计算

Landauer-Büttiker 公式 + 递归 Green 函数：
$$G_{pq} = \frac{2e^2}{h} \text{Tr}[\Gamma_p G^r \Gamma_q G^a]$$

---

## 4. 核心结果

### 4.1 体能带：半金属

体态色散在 $\Gamma$ 点有 Dirac 线性锥 → 畴壁网络是 **Dirac 半金属**，非绝缘体。

### 4.2 边缘几何决定性

| 边缘构型 | CNP 附近行为 | 原因 |
|----------|-------------|------|
| **锯齿边** (sawtooth) | **近量子化** $G \approx e^2/h$ | 无能隙边缘模沿锯齿边界传播 |
| **三叉戟边** (trident) | **小能隙** → 绝缘 | 有限尺寸效应打开 avoided gap |

### 4.3 费米能偏离 CNP

当 $E_F$ 偏离 CNP → 电流**扩展到所有畴壁** → 输运与边缘构型无关 → 体态主导。

### 4.4 无序稳健性

- CNP 附近的量子化电导对**弱无序**稳健（$\langle G_{LR}\rangle$ 在弱无序下保持 $e^2/h$）
- 强无序 → 电导下降（Anderson 局域化）

### 4.5 多端输运

四端器件计算 + LDOS 电流分布图 → 直观展示了锯齿边 vs 三叉戟边的电流路径差异。

---

## 5. 与其他工作的关系

| 相关工作 | 关系 |
|----------|------|
| Qiao et al. 2011 (Nano Lett.) | 同组早期工作：单条畴壁 ZLM — 本文拓展到网络 |
| Efimkin & MacDonald 2018 | 网络模型理论 — 本文用 TB+输运补充 |
| Rickhaus 2018 (实验) | 实验动机 — 本文的锯齿边量子化电导可解释 FP+AB 振荡 |
| Hou/Yuan/Jiang 2024 | 同组后续裁决：TZM vs 网络 — 本文是网络模型的 TB 实现 |

---

## 6. 亮点与局限

### 亮点
- **边缘几何控制输运**的清晰结论：锯齿边 → 量子化，三叉戟边 → 绝缘
- **简化模型抓住本质**：单层石墨烯 + 交错势等价于 mTBG 畴壁网络的拓扑
- **完整的输运分析**：二端/四端、体态/边缘态、无序效应、角度依赖

### 局限
- 简化模型忽略了层自由度、摩尔周期调制、晶格弛豫
- 未讨论 TZM 的可能性（2020 年同时期 Tsim & Koshino 已提出）
- 量子化电导的平台质量（是严格量子化还是近量子化）未深入讨论
- 仅 $T=0$，无温度效应

---

## 7. 与用户研究的关联

| 维度 | 关联 |
|---|---|
| **方法** | Green 函数 + Landauer-Büttiker 输运 — DW 项目可直接复用 |
| **扩展方向** | 用 tbplas 的 TB 模型复现 + 升级到 mTBG 全模型 |
| **可验证性** | 锯齿边 $G=e^2/h$ 量子化可用 tbplas NEGF 独立验证 |

---

## 8. 关键参数速查

| 参数 | 值 |
|------|-----|
| $t$ | 2.6 eV |
| $\Delta$ | 0.1t |
| 能隙 $2\Delta$ | 0.2t |
| 超胞边长 | 8.1 nm |
| 锯齿边量子化电导 | $G \approx e^2/h$（每层每自旋 → mTBG 中 $4e^2/h$） |

---

*报告生成日期：2026-08-06 | 基于 PDF pdftotext 精读*
