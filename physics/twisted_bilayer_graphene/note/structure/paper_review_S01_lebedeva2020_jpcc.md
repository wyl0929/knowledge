<!--
 * @Author       : AI 精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-11
 * @Description  : S1: Lebedeva & Popov 2020
-->
# Paper Review: Lebedeva & Popov (2020)

| 字段 | 内容 |
|------|------|
| **编号** | S1 |
| **标题** | Energetics and Structure of Domain Wall Networks in Minimally Twisted Bilayer Graphene under Strain |
| **作者** | Lebedeva & Popov |
| **期刊** | JPCC 124, 2120 (2020) | **arXiv** | 10.1021/acs.jpcc.9b08306 |
| **类型** | 结构理论 — mTBG 应变下畴壁网络能量与结构 |
| **Phase S 卡片** | [../../Phase_S/cards.md](../../Phase_S/cards.md) |
| **精读日期** | 2026-08-11 |

---

## 1. 核心贡献

原子级模型 (DFT+经验势) 计算 mTBG 畴壁网络在应变下的结构和能量。畴壁宽度、网络几何和稳定性由弹性能和堆垛能竞争决定。为理解实验中的畴壁结构提供定量基础。

## 2. 物理机制 / 实验方法

- DFT 计算层间结合能 + 经验势 (Kolmogorov-Crespi) 计算层内弹性能
- 总能量最小化 → 平衡畴壁宽度 $w_{\rm DW}$ 和网络几何
- 应变 $\epsilon$ 改变弹性能 → $w_{\rm DW}(\epsilon)$ 和网络拓扑变化
- 三角形网络 → 应变下可能变为六边形或其他拓扑

## 3. 关键结果

1. 畴壁宽度 $w_{\rm DW} \sim 5-15$ nm，依赖转角和应变
2. 应变 ~0.1% → 畴壁网络从三角形重构为六边形
3. 网络拓扑转变是可逆的（弹性范围内）
4. 与 Yoo 2019 (E11) 的 STEM 观测一致

## 4. 局限与开放问题

- 仅提供结构信息——未涉及电子态
- 经典经验势精度有限——可能低估畴壁宽度
- 仅考量了静态结构，动力学弛豫过程未考虑

## 5. 与用户研究的相关性

- 为 TBPM 构建畴壁几何模型提供结构参数（$w_{\rm DW}$、网络几何）
- 辅助参考——不直接用于输运计算

---

## Phase S 补充 (2026-08-11): Q1/Q2/Q3

### Q2: 理论如何解释 edge state?
原子级结构计算——不直接解释电子态。提供畴壁宽度 ($\sim 5-15$ nm) 和网络几何的定量参数。应变可改变网络拓扑（三角形→六边形）。

### Q3: 理论如何与实验结合?
为解释 mTBG 实验中应变对畴壁网络几何的影响提供定量结构模型。可与 TEM/STM 结构成像直接比较。
