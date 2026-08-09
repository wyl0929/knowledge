<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-20 19:54:46
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-20 19:54:47
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/multilayer_graphene/subfields/stacking-dw/paper_review_yin2019_prl.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-20
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/stacking-dw/paper_review_yin2019_prl.md
 * @Description  : Yin et al. (2019) PRL — ABC TLG 高场 STS 阅读笔记
-->
# 论文阅读笔记：Yin et al., PRL 122, 146802 (2019)

> **Long-Jing Yin, Li-Juan Shi, Si-Yu Li, Yu Zhang, Zi-Han Guo, Lin He**
> "High-magnetic-field Tunneling Spectra of ABC-Stacked Trilayer Graphene"
> Phys. Rev. Lett. 122, 146802 (2019) | arXiv:1811.10142
>
> 机构：北京师范大学，Lin He 组

---

## 1. 一句话总结

通过**高场 STM/STS**（高达 ~14 T）系统测量 ABC 三层石墨烯的朗道能级谱学，发现**谷分裂和轨道分裂随 $B$ 线性增大**、谷分裂随 LL 指数增大而急剧减小、以及**准粒子逆寿命的线性能量标度**——三者共同构成 ABC TLG 中强电子-电子相互作用的 STS 证据链。

---

## 2. 背景：ABC TLG 中的相关能标

### 2.1 三个关键能标

在高场下，ABC TLG 的 LL 由三个能标决定：

| 能标 | 符号 | 物理起源 |
|---|---|---|
| **回旋能**（cyclotron energy） | $\hbar\omega_c$ | 轨道磁场效应 → 主 LL 间距 |
| **谷分裂**（valley splitting） | $\Delta_V$ | 谷自由度被磁场 + 交换相互作用极化 → LL 分裂为 $K$ 和 $K'$ 对应的子峰 |
| **轨道分裂**（orbital splitting） | $\Delta_{\text{orb}}$ | 同一谷内不同轨道指标的 LL 之间的额外分裂 → 来自多体交换效应 |

### 2.2 此前未知

- ABC TLG 的谷分裂 $\Delta_V$ 如何随 $B$ 和 LL 指数 $N$ 变化？——未知
- 轨道分裂 $\Delta_{\text{orb}}$ 是否由多体效应主导？——未知
- 准粒子的散射率（逆寿命 $\Gamma$）的能量标度？——未知

---

## 3. 实验方法

| 参数 | 细节 |
|---|---|
| 技术 | 低温高场 STM/STS |
| 磁场 | 高达 ~14 T（比 Zhang 2018 的 8 T 更高） |
| 温度 | ~4.2 K |
| 样品 | 机械剥离 ABC 三层石墨烯 |
| 堆叠鉴定 | 原子分辨 STM 形貌图 |

---

## 4. 核心实验结果

### 4.1 谷分裂 $\Delta_V$ 的 $B$ 场标度（关键发现）

- $\Delta_V \propto B$（近似线性）→ 谷 Zeeman 效应 + 交换增强
- **$\Delta_V$ 随 LL 指数 $N$ 增大而急剧减小**：
  - $N=0$ LL：$\Delta_V$ 最大（~几十 meV at 14 T）
  - $N=1$ LL：$\Delta_V$ 约为 $N=0$ 的一半
  - $N=2$ LL：$\Delta_V$ 继续减小
- 这种 $N$ 依赖 = **交换相互作用的特征**——$N=0$ LL 的波函数最局域 → 交换积分最大 → 谷分裂最大

### 4.2 轨道分裂 $\Delta_{\text{orb}}$ 的增强

- 轨道分裂也近似 $\propto B$
- **当最低 LL 部分填充时**（即费米能级落在 $N=0$ LL 内）：$\Delta_{\text{orb}}$ **显著增强**
- 增强幅度超出单粒子预期 → **多体交换效应**
- 部分填充 → 电子之间的交换相互作用最大化 → 轨道极化 → 轨道分裂增强

### 4.3 准粒子逆寿命 $\Gamma$ 的能量标度

- 从 LL 峰的宽度提取准粒子散射率 $\Gamma = \hbar/\tau$
- 发现 $\Gamma \propto |E|$（线性能量标度）→ 与二维费米液体的预期一致
- **但** $\Gamma$ 的绝对值异常大 → 比单层 graphene 大约一个数量级
- → ABC TLG 中的 e-e 散射比单层 graphene 强得多

### 4.4 综合物理图像

```
强磁场下的 ABC TLG:

B ↑ → ℏω_c ↑ (主 LL 间距增大)
    → Δ_V ∝ B (谷极化增强)
    → Δ_orb ∝ B (轨道极化)

最低 LL 部分填充 → 交换增强 → Δ_orb 额外增大
高能 LL → Δ_V 急剧减小 → 谷自由度"解冻"
准粒子寿命 → Γ ∝ |E| → 费米液体行为，但关联极强
```

---

## 5. 物理意义

### 5.1 与 ABA TLG（Zhang 2018）的对比

| 维度 | ABA (Zhang 2018) | ABC (Yin 2019) |
|---|---|---|
| 无质量 Dirac | ✅ ($l=1$) | ❌ |
| 有质量 Dirac | ✅ ($l=2$) | ❌ |
| 三次 Dirac ($l=3$) | ❌ | ✅ |
| LL 交叉 | ✅（两套 LL 之间） | ❌（单一 $l=3$） |
| 谷分裂 | 未定量提取 | **定量提取** $\Delta_V(B, N)$ |
| 轨道分裂 | 未定量提取 | **定量提取** $\Delta_{\text{orb}}(B, \text{filling})$ |
| LL 寿命分析 | 未涉及 | **$\Gamma \propto |E|$** |
| 最大磁场 | 8 T | **14 T** |
| 发表期刊 | PRB | **PRL** |

### 5.2 对强关联物理的启示

ABC TLG 在零场下已经被发现具有超导和关联绝缘态（Zhou et al., Nature 2021）。Yin 2019 的 LL 谱学提供了**高场下的关联物理基准**：

- 谷分裂的 $N$ 依赖 → 说明交换相互作用在 ABC TLG 中极其重要 → 与零场下关联态的发现一致
- $\Gamma \propto |E|$ → ABC TLG 是"强关联的费米液体"——费米液体框架仍适用，但关联强度远大于普通金属

### 5.3 对 TBPM 计算的启示

| 观测 | TBPM 可验证 |
|---|---|
| ABC $l=3$ LL 序列 | ✅ 直接计算 |
| $\Delta_V \propto B$ | ✅ 从 LL 谱提取 |
| $\Delta_V$ 随 $N$ 衰减 | ✅ 验证 |
| **$\Delta_{\text{orb}}$ 增强**（部分填充） | ⚠️ 单粒子 TB 无法复现——需要 HF 或 DMFT |
| **$\Gamma \propto |E|$** | ⚠️ 需要自能修正（TBPM 本身算的是单粒子谱） |

---

## 6. 关键参数

| 参数 | 值 |
|---|---|
| 体系 | ABC 堆叠三层石墨烯 |
| 磁场范围 | 0–14 T |
| 温度 | ~4.2 K |
| 谷分裂 ($N=0$, 14 T) | ~几十 meV |
| 谷分裂 $N$ 依赖 | 随 $N$ 急剧减小 |
| $\Gamma$ 能量标度 | $\propto |E|$ |
| 发表期刊 | **Phys. Rev. Lett.** |

---

## 7. Lin He 组 ABA/ABC 三部曲全貌

```
           ABA TLG                 ABC TLG               ABA/ABC 边界
              │                       │                       │
    Zhang 2018 (PRB)         Yin 2019 (PRL)          Yin 2017 (PRB)
    ─────────────────────────────────────────────────────────────
    两套 LL ($l=1,2$)        单一 LL ($l=3$)         手征性过渡 $l=1,2→3$
    LL 交叉                  谷分裂 ∝ B              畴壁 ~10 nm
    质量重整化               轨道分裂增强            平滑过渡
    ★ LL 非常规分裂          ★ Γ ∝ |E|
```

**三篇 = 三种 stacking 的 LL 谱学完整实验数据集。** 对 TBPM 来说，这是验证代码对三种堆叠的 LL 谱计算准确性的理想 benchmark。

---

*笔记创建日期：2026-07-20 | arXiv:1811.10142v1 + PRL 122, 146802 (2019)*
