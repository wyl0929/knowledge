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
| **Phase S 卡片** | [../../Phase_S/cards.md](../../Phase_S/cards.md) |
| **精读日期** | 2026-08-11 |

---

## 1. 核心贡献

**TZM/网络之争的裁决性工作**。证明 mTBG 偏压下畴壁态自组织为 1D 畸变 TZM——每条通道绕过 AA 堆叠点、独立传播 📜Q。核心预言：**近量子化电导平台（NQCP）**——电导不是精确量子化的 $2e^2/h$，而是接近但不完全等于量子化值的平台。这在 TZM（完全独立）和网络（完全连通）之间找到中间地带。

## 2. 物理机制

- Landauer-Buttiker 公式 + 紧束缚模型 → 多通道输运
- 拓扑螺旋态自组织为 1D 畸变 TZM，绕过 AA 堆叠点独立传播（原文 "bypassing the AA-stacking spots and propagating independently"）📜Q
- NQCP 平台值接近 1、2、3（单位 $2e^2/h$）📜Q；可通过扭转中心垂直移动微调到 1 或 3
- （⚠️ 旧版 "通道间耦合 $t_{\rm inter}\sim0.05t$（弱但非零）" 无源已删——grep "0.05"=0；"通道间存在弱耦合" 为 review 层综合 💭I⚠️）
- 器件几何和边缘终端影响平台形状（解释了不同实验的差异）

## 3. 关键结果

1. NQCP 电导平台——关键定量预言：平台值**接近 1、2、3（单位 $2e^2/h$）**，而非精确量子化 📜Q
2. 算例 $\theta=0.82°$ 平台接近 2 📜Q（grep "0.82"=3）
3. 通道沿三方向独立传播——支持 TZM 图景 📜Q
4. 文中引 Rickhaus 2018 观测到的振荡 📜Q（grep "Rickhaus"=1 正文引用；"与 Xu 2019 对标" 原文无，为 review 层 💭I⚠️）
5. （⚠️ 旧版 "$G \approx 0.8-0.95 \times N \cdot 2e^2/h$"、"平台宽度 ~0.1 eV" 无源已删——grep "0.1 eV"=0）
6. 统一 TZM (T12) 和网络 (T9) → 两者是耦合强度的两个极限

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
TZM/网络之争裁决：畴壁态自组织为 1D 畸变 TZM（绕过 AA 点独立传播）→ 近量子化电导平台 (NQCP)，平台值接近 1/2/3（单位 $2e^2/h$）📜Q。TZM（独立）和网络（连通）是耦合强度的两个极限。

### Q3: 理论如何与实验结合?
NQCP 电导平台是明确的定量实验预言——比完全量子化更易观测。直接对标 Rickhaus 2018、Xu 2019 的输运实验，提供统一解释。

---

## 更正日志 (2026-08-20, S-REV)

- **§2/§3 删除三处无源数字**: "$t_{\rm inter}\approx0.05t$"（grep "0.05"=0）、"$G\approx0.8$–0.95×$N·2e²/h$"、"平台宽度~0.1 eV"（grep "0.1 eV"=0）→ 改为原文可验证表述: "nearly quantized conductance plateau with its value close to 1, 2, and 3 (in units of 2e²/h)"（grep ✓）与 $\theta=0.82°$ 算例平台接近 2 📜Q；TZM 绕过 AA 点独立传播 📜Q。依据: §B.5#3 + cards.md T29。
- **"通道间弱耦合"标注 💭I⚠️**: 原文未给耦合参数，该定性为 review 层综合。依据: cards.md T29。
