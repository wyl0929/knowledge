<!--
 * @Author       : AI 精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-11
 * @Description  : E6: Jiang, B.-Y. et al. (Basov group) 2017
-->
# Paper Review: Jiang, B.-Y. et al. (Basov group) (2017)

| 字段 | 内容 |
|------|------|
| **编号** | E6 |
| **标题** | Plasmon reflections by topological electronic boundaries in bilayer graphene |
| **作者** | Jiang, B.-Y. et al. (Basov group) |
| **期刊** | Nano Lett. 17, 7252 (2017) | **arXiv** | 1707.03980 |
| **类型** | 实验 — s-SNOM: 等离激元在拓扑边界反射 |
| **Phase S 卡片** | [../../Phase_S/cards.md](../../Phase_S/cards.md) |
| **精读日期** | 2026-08-11 |

---

## 1. 核心贡献

利用 s-SNOM 观测等离激元在 BLG 畴壁处的反射。反射归因于束缚在畴壁上的拓扑手征模：手征模与体能带之间的光学跃迁增强局域 ac 电导 → 等离激元被畴壁反射 📜Q（摘要: "strong coupling of domain walls to surface plasmons ... is due to topological chiral modes confined to the walls"）。畴壁作为电子边界不仅束缚电子态，还影响集体激发传播——非侵入式光学探测拓扑边界。

## 2. 物理机制 / 实验方法

- s-SNOM，红外波长 **λ = 11.2 μm** 📜Q（Methods: "Infrared light (λ = 11.2 µm) was focused onto the tip"）；大气环境、tapping 模式、pseudo-heterodyne 检测 📜Q
- 等离激元由 AFM 针尖发射 → 传播 → 畴壁反射 → 与入射波干涉形成驻波 📜Q
- 干涉条纹周期 = 等离激元波长之半 📜Q（正文: "the period equal to one-half of the plasmon wavelength"）
- 反射系数 r 的幅值/相位由驻波剖面拟合提取 📜Q（Fig. 2e/f）
- 样品：机械剥离 BLG 于 285 nm SiO₂/Si，单底栅 Vg 📜Q（Methods；实验无顶栅 → 无位移场 D 控制）
- 理论：畴壁宽度 l = 6–10 nm（由层间堆叠能与层内弹性应变竞争决定）📜Q；剪切壁 N=2 个等离激元通道，拉伸壁 N=2/4/6（依赖化学势与层间偏压）📜Q

## 3. 关键结果

1. 畴壁反射系数 r：**拉伸壁 r 幅值较大且近似纯虚数；剪切壁 r 幅值较小且近似实数** 📜Q（Fig. 2e/f caption）；差异源于拉伸壁除拓扑态外还有常规束缚态 📜Q
2. 反射图样随栅压 Vg 变化（Fig. 2: 拉伸壁由单峰过渡到双峰、剪切壁由单峰到三峰）📜Q；Vg = −80 V / −110 V 拟合示例 📜Q（Fig. 4 caption）
3. 计算等离激元干涉剖面与实验定量一致 📜Q（摘要: "quantitative agreement with our experiments"）

## 4. 局限与开放问题

- 仅光学测量，无输运数据 💭I（全文无输运）
- 单 SiO₂ 底栅：不能独立调控位移场 D，只能调载流子密度 μ 💭I（依据 Methods 器件结构）
- 等离激元波长/反射率的绝对值未在正文给出（r 为拟合幅值/相位）📜Q

## 5. 与用户研究的相关性

- 光学探测畴壁的先行实验——补充纯电学输运
- 若 DW 项目扩展到光学性质，本文是基准

---

## 反向核对 pass (2026-08-19)

pdftotext 提取 → grep 逐项核对（PDF: `Jiang 等 - 2017 - Plasmon reflections ...pdf`，含 SI 1476 行）：
- ✅ 11.2 µm / 285 nm / 6–10 nm / N=2,4,6 / −80 V / −110 V / shear / tensile / quantitative agreement —— 全部在原文找到
- ⚠️ 原文无："反射率 ~5-15%"、"等离激元波长 λp ~ 100-200 nm"、"空间分辨 ~20 nm"、"10.6 μm"、"反射信号仅在 D≠0 时出现"——旧 review 整组虚构数字，已全部删除

## 更正日志 (2026-08-19)

| 原表述 | 问题 | 修正 |
|---|---|---|
| λ ~ 10.6 μm | 原文为 11.2 μm | → 11.2 μm 📜Q |
| 反射率 ~5-15% | 原文无任何反射率百分数 | → 删；改为 r 幅值/相位定性结论 📜Q |
| λp ~ 100-200 nm | 原文无此数值 | → 删 |
| 空间分辨 ~20 nm | 原文无 | → 删 |
| 反射信号仅在 D≠0 时出现 | 实验为单底栅、无 D 控制 | → 删；改为 Vg 依赖 📜Q |
| 仅探测了单条畴壁 | 原文未明确样品壁数 | → 删 |

---

## Phase S 补充 (2026-08-11)

### Q1
s-SNOM 观测等离激元在畴壁处的反射。等离激元干涉条纹编码畴壁反射率和位置。非侵入式光学探测拓扑边界。
