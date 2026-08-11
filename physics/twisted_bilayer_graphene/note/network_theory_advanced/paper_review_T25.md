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
| **Phase S 卡片** | [../../Phase_S/cards/T25.md](../../Phase_S/cards/T25.md) |
| **精读日期** | 2026-08-11 |

---

## 1. 核心贡献

揭示 mTBG 网络中**不仅存在传播的手征模，还存在局域态**——AA 堆垛点或畴壁交叉处的准束缚态。这些局域态与手征网络耦合产生 **Fano 共振**——输运中出现反共振 dip，是局域态存在的明确实验特征。修正了"网络态全是传播模"的简化图景。

## 2. 物理机制

- AA 堆垛点处能带扁平化 → 有效质量发散 → 准束缚态
- 畴壁交叉处（三角形网络顶点）具有 $C_3$ 对称性 → 角动量局域化
- 局域态能级在 gap 内，与手征连续谱能量重叠 → Fano 干涉条件
- Fano 线形：$G(E) \propto (q+\epsilon)^2/(1+\epsilon^2)$，$\epsilon = (E-E_0)/\Gamma$
- 不对称参数 $q$ 由局域态-连续谱耦合强度决定

## 3. 关键结果

1. Fano 共振出现在畴壁交叉点附近的输运谱中——反共振 dip 是局域态的直接特征
2. 局域态密度随偏离 AA 点指数衰减 (~3 nm 局域长度)
3. 多个 AA 点 → 多个 Fano 共振 → 复杂的输运谱
4. 栅压可调谐局域态能量 → 移动 Fano 共振位置

## 4. 局限与开放问题

- 未考虑多体效应（局域态的充电能可能重要）
- 仅研究了单层网络，真实 mTBG 有多层畴壁
- Fano 共振在有限温下的展宽未定量化

## 5. 与用户研究的相关性

- TBPM LDOS 计算可检验 AA 点是否存在局域态
- DW 项目若做输运模拟，Fano 线形是重要诊断工具

---

## Phase S 补充 (2026-08-11): Q2/Q3

### Q2: 理论如何解释 edge state?
mTBG 网络中 AA 点和畴壁交叉处存在局域准束缚态——与手征传播模耦合产生 Fano 共振。网络态不全为传播模，局域态是网络物理的重要组成部分。

### Q3: 理论如何与实验结合?
预言输运谱中 Fano 线形和反共振 dip——局域态耦合的明确特征。为从输运数据中区分传播模和局域态提供诊断工具。对解释非单调电导-栅压曲线有直接意义。
