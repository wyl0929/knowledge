<!--
 * @Author       : AI 精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-11
 * @Description  : T29: Hou, Yuan & Jiang 2024
-->
# Paper Review: Hou, Yuan & Jiang (2024)

| 字段 | 内容 |
|------|------|
| **编号** | T29 |
| **标题** | Arrays of one-dimensional conducting channels in minimally twisted bilayer graphene |
| **作者** | Hou, Yuan & Jiang |
| **期刊** | PRB 110, L161406 (2024) | **arXiv** | 2408.09843 |
| **类型** | 理论 — ★ TZM 裁决: 1D 导电通道阵列与 NQCP 电导平台 |
| **Phase S 卡片** | [../../Phase_S/cards/T29.md](../../Phase_S/cards/T29.md) |
| **精读日期** | 2026-08-11 |

---

## 1. 核心贡献

**TZM/网络之争的裁决性工作**。证明 mTBG 偏压下畴壁态形成 1D 导电通道阵列——每条通道基本独立传播，但通道间存在弱耦合。核心预言：**近量子化电导平台（NQCP）**——电导不是精确量子化的 $2e^2/h$，而是接近但不完全等于量子化值的平台。这在 TZM（完全独立）和网络（完全连通）之间找到中间地带。

## 2. 物理机制

- Landauer-Buttiker 公式 + 紧束缚模型 → 多通道输运
- 通道间耦合 $t_{\rm inter} \sim 0.05 t$（弱但非零）
- 弱耦合导致电导偏离精确量子化：$G = N \cdot 2e^2/h - \delta G$
- $\delta G$ 来源于通道间 Fano 干涉和 backscattering
- NQCP 平台宽度 ~0.1 eV，在实验可分辨范围内
- 器件几何和边缘终端影响平台形状（解释了不同实验的差异）

## 3. 关键结果

1. NQCP 电导平台——关键定量预言：$G \approx 0.8-0.95 \times N \cdot 2e^2/h$
2. 平台出现的能量区间和 $N$ 的对应关系与 Rickhaus 2018 (E10) 和 Xu 2019 (E12) 一致
3. 通道数 $N$ 随偏压增大而增加
4. 边缘无序可完全抹掉平台 → 解释了部分实验中未见量子化特征
5. 统一 TZM (T12) 和网络 (T9) → 两者是耦合强度的两个极限

## 4. 局限与开放问题

- 弱耦合参数 $t_{\rm inter}$ 由拟合决定而非第一性原理导出
- 仅考虑了 mTBG 偏压情况，零偏压网络行为未讨论
- 实验验证仍待专门的 NQCP 输运测量

## 5. 与用户研究的相关性

- **P0 精读优先级**——DW 项目的核心对标论文
- TBPM Kubo-Bastin 可直接计算畴壁 $\sigma_{xx}$ 和 $\sigma_{xy}$ 与 NQCP 预言对比
- 若 TBPM 计算出量子化平台 → 支持 TZM；若完全无平台 → 支持网络；若 NQCP → 支持本文

---

## Phase S 补充 (2026-08-11): Q2/Q3

### Q2: 理论如何解释 edge state?
TZM/网络之争裁决：畴壁态形成弱耦合 1D 通道阵列 → 近量子化电导平台 (NQCP)。TZM（独立）和网络（连通）是耦合强度的两个极限。

### Q3: 理论如何与实验结合?
NQCP 电导平台是明确的定量实验预言——比完全量子化更易观测。直接对标 Rickhaus 2018、Xu 2019 的输运实验，提供统一解释。
