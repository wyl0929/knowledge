<!--
 * @Author       : AI 精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-11
 * @Description  : T30: Wittig, Dominguez & Recher 2024
-->
# Paper Review: Wittig, Dominguez & Recher (2024)

| 字段 | 内容 |
|------|------|
| **编号** | T30 |
| **标题** | Effects of spin-orbit coupling in a valley chiral kagome network |
| **作者** | Wittig, Dominguez & Recher |
| **期刊** | PRB 109, 245429 (2024) | **arXiv** | 2403.10181 |
| **类型** | 理论 — SOC 在谷手征 Kagome 网络中的效应 |
| **Phase S 卡片** | [../../Phase_S/cards/T30.md](../../Phase_S/cards/T30.md) |
| **精读日期** | 2026-08-11 |

---

## 1. 核心贡献

将**自旋轨道耦合（SOC）**引入畴壁 Kagome 网络。SOC 产生自旋-谷锁定——每个谷的手征模携带确定的自旋。SOC 打开拓扑能隙，实现从量子自旋霍尔态到手征态的连续过渡。为在 mTBG/WSe2 异质结中实现量子自旋霍尔效应提供理论路线。

## 2. 物理机制

- Rashba SOC $H_R = \lambda_R (\sigma_x p_y - \sigma_y p_x)$ + 内禀 SOC $H_I = \lambda_I \sigma_z \tau_z$
- 谷 $\tau_z = \pm 1$ + 自旋 $\sigma_z = \pm 1$ → 自旋-谷锁定：每个谷的手征模携带确定自旋
- $\lambda_I$ 打开拓扑能隙 $\Delta \sim 2\lambda_I$ → 量子自旋霍尔相 ($Z_2=1$)
- Kagome 网络的平带获得非零自旋 Chern 数
- 通过 TMD 衬底 (WSe2) 的邻近效应可实现 $\lambda_I \sim 1-5$ meV

## 3. 关键结果

1. SOC 将网络从半金属变为量子自旋霍尔绝缘体
2. 螺旋边缘态携带自旋流——可通过自旋分辨 STM 或非局域输运检测
3. Rashba SOC 导致自旋进动——边缘态的自旋方向旋转
4. 相图：$\lambda_I$-$\lambda_R$ 平面上存在 QSH 相和金属相
5. 与 Barrier 2024 (E16, QH+超导) 互补——SOC 是另一条实现拓扑超导的路线

## 4. 局限与开放问题

- SOC 强度由 TMD 衬底决定——实验上不可独立调控
- 仅考虑单粒子 SOC，多体效应（如自旋液体）未涉及
- Kagome 网络的 SOC 效应在真实 mTBG 中可能被无序掩盖

## 5. 与用户研究的相关性

- TBPM 可引入 SOC 项 → 计算自旋霍尔电导
- 若 DW 项目探索 mTBG/WSe2 异质结，本文是理论入口
- 当前优先级低于 T29/T12/T9（SOC 是锦上添花）

---

## Phase S 补充 (2026-08-11): Q2/Q3

### Q2: 理论如何解释 edge state?
SOC 引入自旋-谷锁定 → 畴壁 Kagome 网络从半金属变为量子自旋霍尔绝缘体。螺旋边缘态携带自旋流。通过 TMD 衬底邻近效应实现。

### Q3: 理论如何与实验结合?
预言自旋-谷锁定的边缘态可通过自旋分辨 STM 或非局域输运检测。为 mTBG/WSe2 异质结中实现 QSH 效应提供理论路线。
