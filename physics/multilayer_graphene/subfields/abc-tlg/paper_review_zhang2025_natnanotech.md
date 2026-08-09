<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-20 23:48:47
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-20 23:48:48
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/multilayer_graphene/subfields/abc-tlg/paper_review_zhang2025_natnanotech.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-20
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/abc-tlg/paper_review_zhang2025_natnanotech.md
 * @Description  : Zhang et al. (2025) Nature Nanotechnology — Rhombohedral 多层石墨烯层数依赖的电子结构与关联 阅读笔记
-->
# 论文阅读笔记：Zhang et al., Nature Nanotech. 20, 222 (2025)

> **Yang Zhang, Yue-Ying Zhou, Shihao Zhang, Hao Cai, Ling-Hui Tong, Yuan Tian, Tongtong Chen, Qiwei Tian, Chen Zhang, Yiliu Wang, Xuming Zou, Xingqiang Liu, Yuanyuan Hu, Ya-Ning Ren, Li Zhang, Lijie Zhang, Wen-Xiao Wang, Lin He, Lei Liao, Zhihui Qin, Long-Jing Yin**
> "Layer-dependent evolution of electronic structures and correlations in rhombohedral multilayer graphene"
> Nature Nanotechnology 20, 222–228 (2025) | arXiv:2312.13637
>
> 机构：湖南大学 (Yin/Qin/Liao 组) + 北京师范大学 (Lin He) + 多单位合作 | 20 pp, 4 figs

---

## 1. 一句话总结

将 STM/STS 从三层推广到 **3–9 层** rhombohedral (ABC) 多层石墨烯，在**液氮温度（77 K）**下首次系统测量了层数依赖的平带扁平化和关联态演化——发现**六层时关联最强**，验证了理论预言，确立了 RG 多层作为强关联平台的层数 tunability。

---

## 2. 背景与动机

### 2.1 从三层到多层

- **2021 年**：Zhou et al. (Nature) 在 ABC 三层中发现超导 → 引爆 rhombohedral graphene 领域
- **问题**：三层只是起点——更多层时，平带和关联效应如何演化？
- **理论预言**：层数 ↑ → 低能平带带宽 ↓ → 关联效应 ↑，但需要实验验证

### 2.2 本文回答的核心问题

| 问题 | 此前状态 |
|---|---|
| 平带带宽随层数如何变化？ | 理论预测但无系统实验 |
| 关联态能在多高温度存活？ | 仅知三层在 mK 温区 |
| 最优关联发生在几层？ | 理论预测 6 层，但无实验 |
| 层间耦合在多层中是否均匀？ | 未知 |

---

## 3. 实验方法

| 参数 | 细节 |
|---|---|
| 技术 | 低温 STM/STS |
| 温度 | **77 K（液氮）**——关键突破 |
| 样品 | Rhombohedral 多层石墨烯（3–9 层），机械剥离 on SiO₂ |
| 层数鉴定 | 原子分辨 STM 形貌图 + 台阶高度测量 |
| 测量量 | $dI/dV$ 谱（局域 DOS）、$dI/dV$ mapping（空间分辨 LDOS） |

---

## 4. 核心实验结果

### 4.1 平带随层数进一步扁平化

- 从 3 层到 9 层，低能平带的带宽**持续减小**
- 3 层：平带带宽 ~几十 meV（与 Yin 2019 PRL 一致）
- 6 层：平带最平 → DOS 峰最尖锐
- 9 层：平带仍扁平，但比 6 层略宽
- **直接验证了理论预测**：更多层 → 更强的层间杂化 → 更平的低能带

### 4.2 层间耦合强度的层数依赖

- 从 STS 谱中提取了层间耦合参数 $\gamma_1, \gamma_3, \gamma_4$ 的层数依赖
- 发现**层间耦合并非均匀**——不同层的耦合强度有差异
- → 紧束缚模型中假设均匀 $\gamma_i$ 的传统做法需要修正

### 4.3 77 K 下的关联态分裂（最惊人发现）

- 当平带**部分填充**时（通过栅压或局域掺杂），$dI/dV$ 谱出现 ~**50–80 meV** 的**分裂**
- **分裂仅在平带被部分填充时出现**——排除了单粒子效应（如 SOC、晶场分裂）
- 分裂的能量标度 ~50–80 meV ≫ $k_B \times 77\text{ K} \approx 7$ meV → **强关联态在液氮温度下稳定存在**
- 这与三层中仅在 mK 温区观测到超导形成鲜明对比——**多层的关联能标远超三层**

### 4.4 六层最优（关键定量结论）

- 关联态分裂的强度随层数变化：3L < 4L < 5L < **6L（最大）** > 7L > 8L > 9L
- **6 层 rhombohedral graphene = 关联最强**
- 这与理论预言的"6 层时平带最平"完全一致
- → 如果想找最强的关联效应，应该做 6 层而非 3 层

---

## 5. 物理意义

### 5.1 从"三层"到"多层平台"的范式转变

| 维度 | Yin 2019 (ABC 三层) | Zhang 2025 (RG 多层) |
|---|---|---|
| 层数 | 3 | 3–9 |
| 温度 | 4.2 K | **77 K** |
| 磁场 | 0–14 T | **0 T** |
| 核心物理 | 高场 LL 谱学 | 零场平带 + 关联态 |
| 期刊 | PRL | **Nature Nanotech.** |

### 5.2 对 rhombohedral graphene 领域的启示

- **三层不是最优的**——要做强关联，应该选 6 层
- **超导可能不止在三层**——6 层中更强的关联态可能意味着更高的 $T_c$
- **77 K 关联态** → 暗示如果存在超导，$T_c$ 可能远高于目前三层中的 ~100 mK

### 5.3 与用户 TBPM 计算的关联

| 本文观测 | TBPM 可验证 |
|---|---|
| 平带带宽 vs 层数 | ✅ 直接计算 DOS vs $N_{\text{layers}}$ |
| 层间耦合的层数依赖 | ✅ 从能带色散中提取有效 $\gamma_i$ |
| **77 K 关联态分裂** | ⚠️ 单粒子 TB 无法复现（需多体方法） |
| 6 层最优 | ✅ 单粒子 TB 可验证平带带宽是否在 6 层最小 |

---

## 6. 与 Lin He 组之前工作的演进

```
2015   Xu et al. (PRB)        — ABC 三层 STM 首次表征
2017   Yin et al. (PRB Rapid) — ABA/ABC 堆叠孤子
2018   Zhang et al. (PRB)     — ABA 三层高场 LL
2019   Yin et al. (PRL)       — ABC 三层高场 LL
         ↓  三部曲完成
2020–2023  研究重心转移：三层 LL → 多层零场平带
         ↓
2025   ★ Zhang et al. (Nat. Nanotech.) — 3–9 层 RG 平带与关联
```

**研究轨迹**：从"在一个体系（三层）中做深"→"在多个体系（3–9 层）中做广"。

---

## 7. 关键参数速查

| 参数 | 值 |
|---|---|
| 体系 | Rhombohedral (ABC) 多层石墨烯 |
| 层数范围 | 3–9 层 |
| 温度 | **77 K（液氮）** |
| 磁场 | 0 T（零场） |
| 关联态分裂 | ~50–80 meV |
| 最优关联层数 | **6 层** |
| 期刊 | Nature Nanotechnology (2025) |

---

## 8. 后续该组相关论文

| 论文 | 关联 |
|---|---|
| **Zou et al., Appl. Phys. Lett. 126, 163105 (2025)** | 同组 (Yin, Qin) — 聚合物微探针操控折纸法制备稳定转角少层石墨烯 |
| **Hoke et al., Nature Mater. (2025)** | Feldman 组 (Stanford) — 螺旋三层中超摩尔弛豫的 STM 成像，与 Lin He 组方法互补 |

---

*笔记创建日期：2026-07-20 | arXiv:2312.13637v2 + Nature Nanotech. 20, 222 (2025)*
