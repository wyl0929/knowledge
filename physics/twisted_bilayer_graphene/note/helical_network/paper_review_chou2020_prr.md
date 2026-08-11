<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 17:20:22
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 17:20:26
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/helical_network/paper_review_chou2020_prr.md
 * @Description  :
-->
<!--
 * @Author       : AI精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/note/helical_network/paper_review_chou2020_prr.md
 * @Description  : T14: Chou, Wu & Das Sarma 2020 — Hofstadter蝴蝶与Floquet拓扑绝缘体
-->

# 论文精读：Chou, Wu & Das Sarma, PRR (2020)

> **Yang-Zhi Chou, Fengcheng Wu, Sankar Das Sarma**
> "Hofstadter butterfly and Floquet topological insulators in minimally twisted bilayer graphene"
> Phys. Rev. Research 2, 033271 (2020) | arXiv:2004.15022
>
> 作者单位：University of Maryland

---

## 1. 一句话总结

在 mTBG 三角网络模型中计算 Hofstadter 蝴蝶 → 强磁场下实现**零陈数 Floquet 拓扑绝缘体**（FTI），体态陈数为零但有手征边缘态穿越体能隙——首次在平衡态固体系统中预言 FTI 的实现。

---

## 2. 背景与动机

- mTBG 的三角网络模型已建立（Efimkin & MacDonald 2018），但拓扑性质未完整表征
- Hofstadter 蝴蝶是 2D 电子在磁场中的指纹——可用于确定模型参数
- FTI 通常需要周期驱动（非平衡），本文发现平衡态 mTBG 即可实现

---

## 3. 核心结果

### 3.1 弱磁场：Dirac 点重入

- 有限磁场下 Dirac 点可重新出现 → 提供确定网络模型参数的实验指纹
- 蝴蝶图的周期性和对称性受 $S$ 矩阵参数 $(P_{a\bar{a}}, P_{a\bar{b}})$ 控制

### 3.2 强磁场：FTI 相

- 强磁场下左右偏转概率不对称 → Dirac 点打开能隙
- **体态陈数 $C=0$，但体带隙中存在手征边缘态**
- 拓扑不变量 $\nu = \pm 1$ 表征 FTI（区别于传统 Chern 绝缘体的 $C \neq 0$）

### 3.3 相图

- 蓝色区：FTI（$\nu = \pm 1$） — 零陈数 + 手征边缘态
- 红色区：金属相（Dirac 锥有隙但体态未全打开）
- 黄色线：无能隙 Dirac 锥

---

## 4. 与用户研究的关联

| 维度 | 关联 |
|---|---|
| **方法** | Hofstadter 蝴蝶计算可用 tbplas + 磁场 Peierls 相位实现 |
| **扩展方向** | DW 项目中检验：EFW 在强磁场下是否出现 FTI 相 |

---

*报告生成日期：2026-08-06 | 基于 PDF pdftotext 精读*

---

## Phase S 补充 (2026-08-11): Q2/Q3

### Q2: 理论如何解释 edge state?
磁场下 moire 网络映射为 Hofstadter 问题。能带拓扑支持零陈数 Floquet 拓扑绝缘体相——手征边缘模穿越体能隙（即使体陈数为零）。

### Q3: 理论如何与实验结合?
预言重入 Dirac 点和蝴蝶状能谱——可通过磁场依赖输运/光谱学检验。为网络拓扑区域识别提供边缘态磁场特征判据。
