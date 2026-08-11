<!--
 * @Author       : AI 精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-11
 * @Description  : T37: McDowell et al. 2026
-->
# Paper Review: McDowell et al. (2026)

| 字段 | 内容 |
|------|------|
| **编号** | T37 |
| **标题** | Probing the Potential Profile of Twisted Bilayer Graphene via Fabry-Perot Interference |
| **作者** | McDowell et al. |
| **期刊** | arXiv:2607.27948 (2026) | **arXiv** | 2607.27948 |
| **类型** | 理论/实验 — FP 干涉势探测 (预印本) |
| **Phase S 卡片** | [../../Phase_S/cards/T37.md](../../Phase_S/cards/T37.md) |
| **精读日期** | 2026-08-11 |

---

## 1. 核心贡献

逆向使用 FP 干涉：将畴壁态作为探针来测量 TBG 的 moire 势能轮廓。FP 振荡图案编码了畴壁通道的势能信息——通过分析振荡周期和振幅提取 moire 势参数。方法论创新：从「研究畴壁态本身」转向「用畴壁态研究其他物理」。

## 2. 物理机制 / 实验方法

- FP 振荡周期 $\Delta V_g \propto 1/L_{\rm FP}$，其中 $L_{\rm FP}$ 为通道有效长度
- 势能变化 $\delta U(x)$ 改变 $L_{\rm FP}$ → 观测振荡周期漂移
- 从振荡图案反解 moire 势 $U(\mathbf{r})$ ——逆问题
- 与 Rickhaus 2018 (E10) 和 Xu 2019 (E12) 数据直接兼容

## 3. 关键结果

1. FP 振荡可提取 moire 势的幅度 (~20-50 meV) 和周期 (~10 nm)
2. 不同栅压区间的 FP 周期变化反映 moire 势的非均匀性
3. 与 DFT 计算的 moire 势定性一致
4. 方法可推广到其他 moire 体系（TMD、三层石墨烯）

## 4. 局限与开放问题

- 预印本，未经同行评审——作为前沿展望引用
- 逆问题的唯一性未证明（不同势能轮廓可能产生相似 FP 图案）
- 仅分析了已有实验数据，未做独立实验验证

## 5. 与用户研究的相关性

- 方法论创新：TBPM 的 FP 振荡模拟可直接对标本文的分析方法
- 若 DW 项目产生 FP 振荡数据，本文提供了提取 moire 势的方法

---

## Phase S 补充 (2026-08-11): Q1/Q2/Q3

### Q2: 理论如何解释 edge state?
FP 干涉作为探针——畴壁通道的 FP 振荡图案编码 moire 势信息。逆向使用：用边缘态探测体性质。

### Q3: 理论如何与实验结合?
提供从 FP 振荡提取 moire 势参数的定量方法。直接应用于 Rickhaus 2018、Xu 2019 数据分析。
