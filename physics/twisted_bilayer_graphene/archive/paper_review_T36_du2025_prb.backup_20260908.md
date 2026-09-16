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
| **Phase S 卡片** | [../../Phase_S/cards.md](../../Phase_S/cards.md) |
| **精读日期** | 2026-08-11 |

---

## 1. 核心贡献

将畴壁工程概念引入石墨烯 Josephson 结。⚠️ 2026-08-20 修正（§B.5#29）: 旧版 "$I_c(\phi)$ 锯齿形、ZBCP、Majorana 信号" 无源已弃——grep "sawtooth"=0、"ZBCP"=0，Majorana 仅在引言作为动机提及（grep "Majorana"=2）。原文三条畴壁工程策略: (i) 数目工程 (ii) 对称性工程 (iii) 几何工程。

## 2. 物理机制 / 实验方法

- 石墨烯 Josephson 结 + AB/BA 畴壁穿过结区，畴壁拓扑 kink 态充当体内超流通道
- 畴壁手征模在超导界面发生 Andreev 反射 → 形成 Andreev 束缚态
- 临界电流对外场调制的响应——畴壁工程策略:
  - (i) **DW 数目工程**: $I_c$ 干涉图案随畴壁数从 AB 振荡连续过渡到 Fraunhofer 衍射 📜Q（复现 Barrier 2024, Nature 628, 741 观测 📜Q）
  - (ii) **DW 对称性工程**: 磁场下非对称畴壁构型 → 理想 Josephson 二极管（显著非互易输运）📜Q
  - (iii) **DW 几何工程**: 交叉畴壁实现可控超流分流（比例由交叉角、磁场、超导相位差调控）📜Q

## 3. 关键结果

1. $I_c$ 干涉图案 AB → Fraunhofer 连续过渡（畴壁数增多）→ 磁力计应用灵敏度增强 📜Q
2. 非对称畴壁构型 → Josephson 二极管 📜Q
3. 交叉畴壁 → 超流分流（可调比例）📜Q
4. （⚠️ 旧版 "谷极化导致正负磁场下 Ic 不对称" 无源，已删）

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
畴壁拓扑 kink 态在 Josephson 结中充当体内超流通道——畴壁工程（数目/对称性/几何）调控临界电流响应 📜Q。

### Q3: 理论如何与实验结合?
预言 AB→Fraunhofer 过渡（复现 Barrier 2024 Nature 628, 741）、Josephson 二极管、超流分流 📜Q——可通过超导输运检验。

---

## 更正日志 (2026-08-20, S-REV)

- **§1–§3 重写**: 旧版 "$I_c(\phi)$ 锯齿形、ZBCP/Majorana 信号" 无源（grep "sawtooth"=0、"ZBCP"=0；Majorana 仅为引言动机 grep=2）→ 改为原文三条 DW 工程策略: (i) 数目工程 AB→Fraunhofer（复现 Barrier 2024 Nature 628, 741）(ii) 对称性工程 → Josephson 二极管 (iii) 几何工程 → 超流分流（grep "Fraunhofer"=11、"diode"=22 ✓）。依据: §B.5#29 + cards.md T36。
