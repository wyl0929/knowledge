<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 17:20:32
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 17:20:36
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/helical_network/paper_review_debeule2021_prb.md
 * @Description  :
-->
<!--
 * @Author       : AI精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/note/helical_network/paper_review_debeule2021_prb.md
 * @Description  : T18: De Beule et al. 2021 — mTBG的有效Floquet模型
-->

# 论文精读：De Beule, Dominguez & Recher, PRB (2021)

> **Christophe De Beule, Fernando Dominguez, Patrik Recher**
> "Effective Floquet model for minimally twisted bilayer graphene"
> PRB 103, 195432 (2021) | arXiv:2011.12989
>
> 作者单位：TU Braunschweig

---

## 1. 一句话总结

为 mTBG 畴壁网络建立**有效 Floquet 模型**：畴壁上的手征模式在磁翻译对称性下等效于周期性驱动的 1D 系统 → 用 Floquet 理论解析求解能带和拓扑不变量。

---

## 2. 核心贡献

- 将 2D 三角网络映射为等效 1D Floquet 问题——利用摩尔平移对称性
- 畴壁手征模式在 AB/BA 区域交替传播 → 等效于时间周期的"踢"（kick）
- Floquet 能带给出网络的完整色散，自动包含拓扑边缘态
- 与连续模型和 TB 结果一致，但计算成本大幅降低

---

## 3. 亮点与局限

### 亮点
- **方法创新**：Floquet 映射将 2D 网络问题降维为 1D
- 解析可控，便于分析参数依赖性和拓扑相变

### 局限
- 依赖网络模型的有效性（即畴壁态与其他态分离）
- 未考虑相互作用和晶格弛豫

---

## 4. 与用户研究的关联

| 维度 | 关联 |
|---|---|
| **方法** | Floquet 映射可作为 tbplas 计算的解析对照 |
| **扩展方向** | DW 项目中检验 Floquet 能带 vs TB 能带的一致性 |

---

*报告生成日期：2026-08-06 | 基于 PDF 和已有知识综合*

---

## Phase S 补充 (2026-08-11): Q2/Q3

### Q2: 理论如何解释 edge state?
2D moire 网络映射为有效 1D Floquet 问题：手征模在交替畴区运动视为周期踢动 → Floquet 能带和拓扑边缘态。无需完整 2D 网络计算。

### Q3: 理论如何与实验结合?
提供解析可解有效模型，再现连续/紧束缚模型主要谱特征。为实验学家提供更直观的理论工具。
