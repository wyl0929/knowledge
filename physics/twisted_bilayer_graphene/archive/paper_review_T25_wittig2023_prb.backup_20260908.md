<!--
 * @Author       : AI 精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-11
 * @Description  : T25: Wittig, Dominguez, De Beule & Recher 2023 — 揭示 mTBG 网络中**不仅存在传播的手征模，还存在局域态**——AA 堆垛点或畴壁交叉处的准束缚态。这些局域态与手征
-->
# Paper Review: Wittig, Dominguez, De Beule & Recher (2023)

| 字段 | 内容 |
|------|------|
| **编号** | T25 |
| **标题** | Localized states coupled to a network of chiral modes in minimally twisted bilayer graphene |
| **作者** | Wittig, Dominguez, De Beule & Recher |
| **期刊** | PRB 108, 085431 (2023) | **arXiv** | 2303.03901 |
| **类型** | 理论 — 局域态+手征网络耦合 |
| **Phase S 卡片** | [../../Phase_S/cards.md](../../Phase_S/cards.md) |
| **精读日期** | 2026-08-11 |

---

## 1. 核心贡献

揭示 mTBG 网络中**不仅存在传播的手征模，还存在局域态**——AA 堆垛点或畴壁交叉处的准束缚态。这些局域态与手征网络耦合在输运中产生**共振附近的反共振 dip**（⚠️ 2026-08-20 修正: 旧版称 "Fano 共振"——原文未用 Fano 术语，grep "Fano"=0），是局域态存在的明确实验特征。修正了"网络态全是传播模"的简化图景。

## 2. 物理机制

- AA 区域能量谱中出现平带 → 局域态密度（原文 "flatbands in the energy spectrum associated to a localized density of states at the AA regions"）📜Q
- 在唯象网络模型中引入 AA 区域的**离散能级集合**（隧穿幅度 $t_{ij}$）→ 能量依赖 S 矩阵 📜Q
- 同时保留能量无关的偏转过程（入模 ↔ 邻近出模）📜Q
- 还以平均场方式考虑 AA 区域库仑排斥的影响 📜Q
- 局域态能级在 gap 内，与手征连续谱能量重叠 → 共振附近电导 dip（⚠️ "Fano 线形 $G(E) \propto (q+\epsilon)^2/(1+\epsilon^2)$" 为 review 层推演 💭I，原文未给该公式）

## 3. 关键结果

1. 共振附近出现电导 dip——反共振 dip 是局域态耦合的直接特征；dip 宽度 $\propto |\tau|^2\hbar v_F/l$ 📜Q
2. （⚠️ 旧版 "局域长度 ~3 nm" 无源已删——grep "3 nm"=0）
3. 多个 AA 点 → 多个离散能级 → 复杂的输运谱
4. 栅压可调谐局域态能量 → 移动共振位置

## 4. 局限与开放问题

- 未考虑多体效应（局域态的充电能可能重要）
- 仅研究了单层网络，真实 mTBG 有多层畴壁
- 共振 dip 在有限温下的展宽未定量化

## 5. 与用户研究的相关性

- TBPM LDOS 计算可检验 AA 点是否存在局域态
- DW 项目若做输运模拟，Fano 线形是重要诊断工具

---

## Phase S 补充 (2026-08-11): Q2/Q3

### Q2: 理论如何解释 edge state?
mTBG 网络中 AA 区域存在局域准束缚态（离散能级）——与手征传播模耦合产生共振附近的反共振 dip 📜Q。网络态不全为传播模，局域态是网络物理的重要组成部分。

### Q3: 理论如何与实验结合?
预言输运谱中反共振 dip——局域态耦合的明确特征。为从输运数据中区分传播模和局域态提供诊断工具。对解释非单调电导-栅压曲线有直接意义。

---

## 更正日志 (2026-08-20, S-REV)

- **§1/§3 "Fano 共振" → "共振附近反共振 dip"**: 原文未用 Fano 术语（grep "Fano"=0）；Fano 线形公式为 review 层推演 → 标 💭I。依据: §B.5#23 + cards.md T25。
- **§2 机制改写**: 改为原文表述（AA 平带局域 DOS + 离散能级 + 能量依赖 S 矩阵 + 平均场库仑排斥，grep "discrete"=48 上下文 ✓）。
- **§3 删除 "局域长度 ~3 nm"**: grep "3 nm"=0 无源。依据: §B.5#23。
