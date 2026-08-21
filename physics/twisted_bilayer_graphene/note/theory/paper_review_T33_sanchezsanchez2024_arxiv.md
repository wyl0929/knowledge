<!--
 * @Author       : AI 精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-11
 * @Description  : T33: Sanchez-Sanchez et al. 2024
-->
# Paper Review: Sanchez-Sanchez et al. (2024)

| 字段 | 内容 |
|------|------|
| **编号** | T33 |
| **标题** | Edge-state transport in twisted bilayer graphene |
| **作者** | Sanchez-Sanchez et al. |
| **期刊** | arXiv:2407.04668 (2024) | **arXiv** | 2407.04668 |
| **类型** | 理论 — TBG 边缘态输运 (预印本) |
| **Phase S 卡片** | [../../Phase_S/cards.md](../../Phase_S/cards.md) |
| **精读日期** | 2026-08-11 |

---

## 1. 核心贡献

系统性研究 TBG 物理边缘（样品边界）而非内部畴壁的边缘态输运。边缘态性质由边缘原子结构（zigzag/armchair 类）和 moire 截断方式决定。关键贡献：区分了「moire 边缘态」和「畴壁态」——两者常被混淆，但物理起源不同。

## 2. 物理机制 / 实验方法

- 有限尺寸 TBG 器件（算例 $\theta=1.696°$）📜Q（grep "1.696"=27）
- 紧束缚 + 分子动力学弛豫结构，考虑纳米带切割方式（zigzag/armchair 类）
- 边缘态输运用多接触 Landauer 计算（原文 3/4 接触器件构型）
- 态局域于特定边缘——取决于纳米带切割方式 📜Q

## 3. 关键结果

1. （⚠️ 旧版 "zigzag 边缘 ~2-4 支/谷、armchair 几乎没有" 无源已删）
2. 边缘态承载电流、**电导值接近电导量子** 📜Q（原文 "conductance values close to the conductance quantum"）
3. 边缘态可导致**非局域电阻**——态局域于特定边缘（取决于纳米带切割）📜Q
4. 输运发生在超晶格能隙内、电导接近电导量子 📜Q
5. 区分实验判据：样品边缘输运 vs 内部畴壁输运的电导值不同

## 4. 局限与开放问题

- 预印本，未经过同行评审
- 仅覆盖特定边缘几何，普适性待验证
- 作为前沿展望引用，不作核心论据

## 5. 与用户研究的相关性

- TBPM 计算不同边缘终端的输运时，本文提供对照基准
- 提醒：实验中的边缘输运信号可能与畴壁输运混合

---

## Phase S 补充 (2026-08-11): Q1/Q2/Q3

### Q2: 理论如何解释 edge state?
TBG 物理边缘（样品边界）的边缘态由原子结构和 moire 截断决定——与内部畴壁态物理起源不同。需在实验中区分。

### Q3: 理论如何与实验结合?
预言边缘态电导接近电导量子、非局域电阻源于态局域于特定边缘 📜Q。为区分内部畴壁输运和样品边缘输运提供判据。

---

## 更正日志 (2026-08-20, S-REV)

- **§3 删除 "zigzag ~2-4 支/谷、armchair 几乎没有"**: 无源 → 改为原文: 边缘态电导接近电导量子、非局域电阻源于态局域于特定边缘（取决于纳米带切割；算例 $\theta=1.696°$，grep "1.696"=27、"conductance values close to the conductance quantum" ✓）。依据: §B.5#27 + cards.md T33。
