<!--
 * @Author       : AI 精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-11
 * @Description  : T36: Du, Qi, Jiang & Xie 2025
-->
# Paper Review: Du, Qi, Jiang & Xie (2025)

| 字段 | 内容 |
|------|------|
| **编号** | T36 |
| **标题** | Domain wall engineering in graphene-based Josephson junctions |
| **作者** | Du, Qi, Jiang & Xie |
| **期刊** | PRB (2025) | **arXiv** | 2509.02082 |
| **类型** | 理论 — Josephson 结畴壁工程 |
| **Phase S 卡片** | [../../Phase_S/cards/T36.md](../../Phase_S/cards/T36.md) |
| **精读日期** | 2026-08-11 |

---

## 1. 核心贡献

将畴壁工程概念引入石墨烯 Josephson 结。畴壁的手征性和谷极化导致非常规的 Andreev 束缚态谱和超流-相位关系。畴壁可承载 Majorana 零模候选态（在合适条件下）。为超导-畴壁耦合提供具体实现方案。

## 2. 物理机制 / 实验方法

- 石墨烯 Josephson 结 + AB/BA 畴壁穿过结区
- 畴壁手征模在超导界面发生 Andreev 反射 → 形成 Andreev 束缚态
- 手征性 → Andreev 谱 $E(\phi)$ 不对称于 $\phi=0$
- 合适条件（SOC+磁场+超导）下畴壁可承载 Majorana 零模

## 3. 关键结果

1. 畴壁 Josephson 结的临界电流-相位关系 $I_c(\phi)$ 含特征锯齿形状
2. 零偏压电导峰 (ZBCP) 是 Majorana 的潜在信号
3. 谷极化导致正负磁场下 $I_c$ 不对称——实验可检验特征

## 4. 局限与开放问题

- 偏离核心叙事（拓扑边缘态输运）——**Scope Out，仅需知道存在**
- Majorana 实现条件苛刻（SOC+磁场+超导三者同时满足）
- 实验实现难度极高

## 5. 与用户研究的相关性

- **Scope Out**——Josephson 畴壁需要独立调研，当前不深入
- 若 DW 项目未来扩展到超导畴壁，本文是入口

---

## Phase S 补充 (2026-08-11): Q1/Q2/Q3

### Q2: 理论如何解释 edge state?
畴壁在 Josephson 结中作为 Andreev 束缚态的特殊通道——手征性和谷极化导致非常规超导邻近效应。

### Q3: 理论如何与实验结合?
预言特征 $I_c(\phi)$ 锯齿形、ZBCP、正负磁场不对称——可通过超导输运检验。与 Barrier 2024 (E16) 互补。
