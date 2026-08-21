<!--
 * @Author       : AI 精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-11
 * @Description  : T28: Mondal, Ghadimi & Yang 2023
-->
# Paper Review: Mondal, Ghadimi & Yang (2023)

| 字段 | 内容 |
|------|------|
| **编号** | T28 |
| **标题** | Quantum Valley and Sub-valley Hall Effect in large-angle twisted bilayer graphene |
| **作者** | Mondal, Ghadimi & Yang |
| **期刊** | PRB 108, L121405 (2023) | **arXiv** | 2306.02655 |
| **类型** | 理论 — 大转角 TBG 中的量子谷和子谷霍尔效应 |
| **Phase S 卡片** | [../../Phase_S/cards.md](../../Phase_S/cards.md) |
| **精读日期** | 2026-08-11 |

---

## 1. 核心贡献

将拓扑畴壁态的概念从 mTBG（小转角）扩展到**大转角 TBG**。⚠️ 2026-08-20 修正（§B.5#34）: 原文算例为 commensurate 转角 $\theta_c=38.21°$（grep "38.21"=9），微小偏离产生 1D 畴壁导电网络；子谷 Dirac 锥（Haldane/Semenoff 质量）承载畴壁模；网络可现非费米液体行为；电场/层滑动调控。旧版 "~5-15°"、"~6°/~10°" 转角列表无源已弃。

## 2. 物理机制

- 大转角 commensurate 角 $\theta_c=38.21°$ 附近，微小偏离产生 1D 畴壁网络 📜Q
- 子谷（sub-valley）Dirac 锥携带 Haldane/Semenoff 质量 → 畴壁模（grep "Haldane"=9、"Semenoff"=8 ✓）📜Q
- 网络可表现出非费米液体行为 📜Q
- 电场与层滑动作为调控手段 📜Q

## 3. 关键结果

1. 大转角 TBG 在 commensurate 角 $\theta_c=38.21°$ 附近支持量子谷/子谷霍尔相 📜Q
2. 子谷霍尔效应给出不同于 mTBG 的电导量子化阶数
3. （⚠️ 旧版 "边缘态 ~1 nm vs mTBG ~5 nm" 无源已删）
4. （⚠️ 旧版 "圆偏振光激发/检测读出" 无源已删——grep "circular" 未见光读出方案）

## 4. 局限与开放问题

- 实验验证仍缺乏：大转角 TBG 的畴壁输运实验几乎空白
- 子谷的退相干时间未知——可能极短
- 仅考虑单粒子图像

## 5. 与用户研究的相关性

- TBPM 可计算不同转角下的 $\sigma_{xy}$ → 检验子谷霍尔电导平台
- 若 DW 项目考虑大转角体系，本文是理论入口

---

## Phase S 补充 (2026-08-11): Q2/Q3

### Q2: 理论如何解释 edge state?
大转角 TBG 在 commensurate 角 $\theta_c=38.21°$ 附近产生 1D 畴壁网络——子谷 Dirac 锥（Haldane/Semenoff 质量）承载畴壁模 📜Q。子谷自由度提供额外拓扑分类——畴壁态数目可能不同于传统谷陈数预言。

### Q3: 理论如何与实验结合?
将拓扑畴壁态概念从 mTBG 扩展到大转角 TBG——实验上更易制备。预言的子谷霍尔电导阶数可直接与 mTBG 比较。

---

## 更正日志 (2026-08-20, S-REV)

- **§1–§3 转角列表重写**: 旧版 "~5-15°"、"(~6deg, ~10deg)" 无源 → 改为原文算例 commensurate 角 $\theta_c=38.21°$（grep "38.21"=9），微小偏离产生 1D 畴壁网络。依据: §B.5#34 + cards.md T28。
- **§3 删除 "~1 nm vs ~5 nm"、"圆偏振光读出"**: 均无源。依据: §B.5#34。
- **§2 补充 Haldane/Semenoff 子谷质量、非费米液体、电场/层滑动调控**: 原文验证（grep "Haldane"=9、"Semenoff"=8、"non-Fermi"=4 ✓）。依据: §B.5#34。
