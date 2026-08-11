<!--
 * @Author       : AI 精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-11
 * @Description  : T34: Wen, Lv & Li 2024
-->
# Paper Review: Wen, Lv & Li (2024)

| 字段 | 内容 |
|------|------|
| **编号** | T34 |
| **标题** | Local optical conductivity of strain solitons in bilayer graphene with arbitrary soliton angle |
| **作者** | Wen, Lv & Li |
| **期刊** | PRB 110, 235402 (2024) | **arXiv** | 2412.12630 |
| **类型** | 理论 — 应变孤子局域光电导 |
| **Phase S 卡片** | [../../Phase_S/cards/T34.md](../../Phase_S/cards/T34.md) |
| **精读日期** | 2026-08-11 |

---

## 1. 核心贡献

计算任意角度应变孤子（堆垛畴壁）上的局域光电导。光响应可探测畴壁态的电子结构——光电导谱中的特征峰对应畴壁子带间跃迁。为光学探测畴壁电子态提供了具体方案，补充了纯输运测量的局限性。

## 2. 物理机制 / 实验方法

- 紧束缚模型 + Kubo 公式计算局域光电导 $\sigma_{xx}(\mathbf{r}, \omega)$
- 应变孤子 = 堆垛畴壁，宽度 ~5-15 nm
- 孤子角度 $\theta$ 从 0°（shear soliton）到 90°（tensile soliton）
- 子带间跃迁能量 $\hbar\omega \sim 50-200$ meV (THz 到中红外)
- 光电导峰的位置和强度依赖孤子角度

## 3. 关键结果

1. 孤子角度 $\theta$ → 特征光电导谱——可作为光学指纹区分不同类型畴壁
2. 光电导峰对应畴壁子带间跃迁，能量 ~100 meV
3. Shear soliton ($\theta \approx 0$) 的光电导最强——最易实验探测
4. s-SNOM 或光电流显微镜可空间分辨光电导

## 4. 局限与开放问题

- 仅考虑单粒子光电导，激子效应未纳入（可能重要）
- 有限温展宽未定量化
- 实验实现需要 ~10 nm 空间分辨的光学测量（s-SNOM 可达到）

## 5. 与用户研究的相关性

- 若 DW 项目有兴趣扩展到光学性质，本文是入口
- 当前优先级较低（TBPM 以输运为主）

---

## Phase S 补充 (2026-08-11): Q1/Q2/Q3

### Q2: 理论如何解释 edge state?
任意角度应变孤子畴壁上的局域光电导——光响应可探测畴壁电子结构。孤子角度决定特征光电导谱。

### Q3: 理论如何与实验结合?
预言畴壁局域光电导的特征谱——s-SNOM/光电流显微镜可检验。为光学探测畴壁电子态提供方案。
