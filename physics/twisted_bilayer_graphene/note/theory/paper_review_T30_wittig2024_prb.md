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
| **Phase S 卡片** | [../../Phase_S/cards.md](../../Phase_S/cards.md) |
| **精读日期** | 2026-08-11 |

---

## 1. 核心贡献

将**自旋轨道耦合（SOC）**引入畴壁 Kagome 网络。⚠️ 2026-08-20 修正（§B.5#25）: 原文只含 **Rashba SOC**（grep "Rashba"=9、"intrinsic"=0）——旧版 "自旋-谷锁定、内禀 SOC $\lambda_I$、量子自旋霍尔相（$Z_2=1$）、自旋 Chern 数" 原文均无，已弃。原文效应: 磁电导周期性缩减 + 特征尖锐共振 + 电导自旋极化（自旋电子学应用）📜Q。

## 2. 物理机制

- Rashba SOC 作用于谷手征 Kagome 网络
- Rashba 导致磁电导周期性缩减、特征尖锐共振 📜Q
- 电导出现自旋极化——自旋电子学应用潜力 📜Q
- 引用 WSe2 上 Rashba 耦合 $\alpha_R\approx15$ meV 测量值 📜Q（grep "15 meV"=1）

## 3. 关键结果

1. Rashba SOC → 磁电导周期性缩减 + 尖锐共振 📜Q
2. 电导自旋极化 → 自旋分辨探测可能
3. （⚠️ 旧版 "SOC 将网络变为 QSH 绝缘体"、"$\lambda_I$-$\lambda_R$ 相图 QSH/金属" 无源已删）
4. 与 Barrier 2024 (E16, QH+超导) 互补——SOC 是另一条实现拓扑超导的路线（⚠️ review 层综合 💭I，原文未提 Barrier）

## 4. 局限与开放问题

- SOC 强度由 TMD 衬底决定——实验上不可独立调控
- 仅考虑单粒子 SOC，多体效应（如自旋液体）未涉及
- Kagome 网络的 SOC 效应在真实 mTBG 中可能被无序掩盖

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
⚠️ 修正: 原文只含 Rashba SOC → 磁电导周期性缩减 + 特征尖锐共振 + 电导自旋极化 📜Q。（旧版 "自旋-谷锁定 → QSH 绝缘体、螺旋边缘态携带自旋流" 无源已弃）

### Q3: 理论如何与实验结合?
预言电导自旋极化与磁电导特征——可通过自旋分辨测量检验。为 mTBG/WSe2 异质结中的 SOC 效应提供理论路线。

---

## 更正日志 (2026-08-20, S-REV)

- **§1–§3/Q2 重写**: 旧版 "QSH 绝缘体（$Z_2$=1）/自旋-谷锁定/$\lambda_I$~1–5 meV/自旋 Chern 数/相图" 原文均无（grep "QSH"=0、"intrinsic"=0）→ 改为原文: 只含 Rashba SOC（grep "Rashba"=9），磁电导周期性缩减 + 尖锐共振 + 电导自旋极化 📜Q；$\alpha_R\approx15$ meV 引自 WSe2 测量（grep "15 meV"=1）。依据: §B.5#25 + cards.md T30。
