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
| **Phase S 卡片** | [../../Phase_S/cards.md](../../Phase_S/cards.md) |
| **精读日期** | 2026-08-11 |

---

## 1. 核心贡献

计算任意角度应变孤子（堆垛畴壁）上的局域光电导。光响应可探测畴壁态的电子结构——光电导谱中的特征峰对应畴壁子带间跃迁。为光学探测畴壁电子态提供了具体方案，补充了纯输运测量的局限性。

## 2. 物理机制 / 实验方法

- 紧束缚模型 + Kubo 公式计算局域光电导 $\sigma_{xx}(\mathbf{r}, \omega)$
- 应变孤子 = 堆垛畴壁；窄畴壁宽度 ~10 nm（原文 "narrow domain walls (width ∼10 nm)"）📜Q
- 孤子角度 $\phi$ 约定: **$\phi=0°$ 为 tensile、$\phi=90°$ 为 shear** 📜Q（⚠️ 旧版写反——原文 "tensile soliton (ϕ = 0°)"）
- 光电导谱特征峰对应畴壁（拓扑 + 高能孤子）态间跃迁 📜Q
- 光电导峰的位置和强度依赖孤子角度

## 3. 关键结果

1. 孤子角度 $\phi$ → 特征光电导谱——可作为光学指纹区分不同类型畴壁
2. 两个最显著峰随孤子角度分别被**连续抑制/增强** 📜Q（⚠️ 旧版 "shear 最强" 无源已弃）
3. 垂直于层的压强可**加倍共振峰能量**（在实验可达压强范围）📜Q（⚠️ 旧版 "子带间跃迁能量 ~50–200 meV" 无源已删——原文 200 meV 为 Fermi 能参数 $\epsilon_F$，非跃迁能）
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
任意角度应变孤子畴壁上的局域光电导——光响应可探测畴壁电子结构。孤子角度（$\phi=0°$ tensile / $90°$ shear）决定特征光电导谱 📜Q。

### Q3: 理论如何与实验结合?
预言畴壁局域光电导的特征谱——s-SNOM/光电流显微镜可检验；压强可大幅调制峰能 📜Q。为光学探测畴壁电子态提供方案。

---

## 更正日志 (2026-08-20, S-REV)

- **§2 孤子角约定修正**: 旧版 "0°=shear / 90°=tensile" 写反 → 原文 $\phi=0°$ 为 **tensile**、$\phi=90°$ 为 **shear**（grep "tensile (ϕ = 0◦)" ✓）。依据: §B.5#28 + cards.md T34。
- **§2 删除 "~50–200 meV 跃迁"**: 原文 200 meV 为 Fermi 能参数 $\epsilon_F$（"Vi = 150 mV, εF = 200 meV"），非跃迁能量。依据: §B.5#28。
- **§3 删除 "shear 最强"、"~100 meV 峰"**: 无源 → 改原文: 两主峰随孤子角连续抑制/增强；压强可加倍峰能（grep "continuous suppression and enhancement" / "double the energies" ✓）。依据: §B.5#28。
