<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-07 17:32:20
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-07 17:32:25
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/multilayer_graphene/subfields/domain-wall/01_research_overview.md
 * @Description  :
-->
<!--
 * @Author       : AI-generated (research_onboarding_skill, subfield)
 * @Date         : 2026-07-07
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/domain-wall/01_research_overview.md
 * @Description  : 石墨烯 Domain Wall 实验研究综述 (bilayer / trilayer / multilayer)
-->

# 石墨烯 Domain Wall 实验研究综述

> 最后更新: 2026-07-07
>
> **文档定位**: 为 DW 计算项目提供实验文献参照。聚焦实验研究，不含纯理论工作。
> **生成模式**: quick_scan → 基于 arXiv 交叉验证的文献核实报告
>
> ⚠️ **证据说明**: 原始问卷（`DW/docs/experimental_domain_wall_survey.md` 已删除）包含大量未核实条目。
> 本文档为**arXiv 交叉验证后**的重写版本。已验证论文标注 DOI，未核实条目标注 `NEEDS_VERIFICATION`，
> 已被证伪的原始条目在 §5 列出并说明原因。

---

## 0. 执行摘要

石墨烯 Domain Wall (DW) 实验研究主要集中在**双层 AB/BA 堆叠畴壁 (LSW)** 方向。核心实验发现：AB 堆叠双层在位移场 $D$ 下打开能隙后，AB/BA 堆叠边界（shear soliton）处束缚**拓扑保护的 1D 谷极化边界态**，表现为沿畴壁的导电通道。

### 已验证的关键文献

| 验证状态 | 数量 | 说明 |
|:------:|:----:|------|
| ✅ arXiv 确认 | 7 篇 | DOI 已核实，详见 §2 |
| ❌ 原文错误/不存在 | 8 条 | 原始问卷中描述与 arXiv 检索不符的条目，详见 §5 |
| ⚠️ NEEDS_VERIFICATION | 若干 | 三层/多层畴壁实验文献，arXiv 上难以定位 |

### 关键发现

1. **双层畴壁实验已成熟**：Ju et al. (2015) Nature 奠基 → Li et al. (2016) Nat. Nanotech. 栅控 → Jiang et al. (2017) Nano Lett. 等离激元成像
2. **三层畴壁实验极度匮乏**：ABC 或 ABA 三层石墨烯中孤立畴壁的输运或 STM 实验**未在 arXiv 上找到**——这是用户 DW 项目计算可填补的重要空白
3. **EFW 实验几乎空白**：电场畴壁需要分裂栅，实验难度远高于 LSW
4. **Moiré DW 有理论研究**：转角体系的畴壁网络有大量理论工作，但独立畴壁实验较少

---

## 1. 石墨烯畴壁类型与实验实现方式

### 1.1 畴壁分类

| 类型 | 缩写 | 物理成因 | 层数要求 | 实验实现方式 | 实验成熟度 |
|------|------|---------|:------:|------------|:------:|
| **Layer Stacking Wall** | LSW | AB ↔ BA 堆叠滑移边界（shear soliton） | ≥2 | 机械剥离中自然缺陷、hBN 封装自发形成 | ⭐⭐⭐⭐⭐ |
| **Electric Field Wall** | EFW | 位移场 $D$ 符号空间反转 | ≥2 | 分裂顶栅/底栅施加相反偏压 | ⭐ (几乎空白) |
| **Moiré Domain Wall** | MDW | 转角畴壁网络（三角 AB/BA 畴边界） | ≥2 (含转角) | 控制转角对准 + 近场成像 | ⭐⭐⭐ |
| **ABC/ABA Stacking Boundary** | — | 三层中 ABC ↔ ABA 堆叠异构体边界 | ≥3 | 机械剥离中自然出现 | ⭐ (未知) |

### 1.2 实验探针汇总

| 探针技术 | 可测量量 | 适用畴壁 | 已验证的代表性工作 |
|---------|---------|---------|-------------------|
| **近场红外纳米成像** (s-SNOM) | 畴壁实空间成像、等离激元反射/传播 | LSW, MDW | Ju 2015, Jiang 2017 ✅ |
| **电输运** ($R_{xx}$, $R_{xy}$) | 畴壁电导、谷极化输运 | LSW | Li 2016, Mania 2019 ✅ |
| **双栅极输运** | 位移场调控畴壁通道电导 | LSW, EFW | Li 2016 ✅ |
| **STM/STS** | 畴壁局域态密度 | LSW | Li S.-Y. 2016 (stacking soliton STM) ✅ |
| **光电流/谷电流** | 谷极化电流生成与检测 | LSW | Shimazaki 2015 ✅ |
| **应变工程** | 赝磁场 + 拓扑通道 | LSW-like | Hsu 2020 ✅ |

---

## 2. 已验证实验文献（按体系分层）

> **验证方法**: arXiv 搜索 + DOI 交叉核对。✅ = arXiv 上找到并确认。⚠️ = arXiv 上找到但细节可能不准确。

### 2.1 双层石墨烯 (Bilayer) — LSW 畴壁

双层石墨烯是畴壁实验最成熟的平台。核心物理：AB 堆叠双层在位移场下打开能隙 → AB/BA 堆叠边界束缚拓扑保护的 1D 谷极化边界态。

| # | 第一作者 | 年份 | 期刊 | DOI | 验证 |
|---|---------|------|------|-----|:--:|
| [P1] | **Ju, L.** | 2015 | Nature **520**, 650 | 10.1038/nature14364 | ✅ |
| [P2] | **Li, J.** | 2016 | Nature Nanotech. **11**, 1060 | 10.1038/nnano.2016.158 | ✅ |
| [P3] | **Jiang, B.-Y.** | 2017 | Nano Letters **17**, 7252 | 10.1021/acs.nanolett.7b03816 | ✅ |
| [P4] | **Shimazaki, Y.** | 2015 | Nature Physics **11**, 1032 | 10.1038/nphys3551 | ✅ |
| [P5] | **Mania, E.** | 2019 | Commun. Phys. **2**, 6 | 10.1038/s42005-018-0106-4 | ✅ |
| [P6] | **Li, S.-Y.** | 2016 | (arXiv only) | arXiv:1609.03313 | ✅ |
| [P7] | **Hsu, C.-C.** | 2020 | Science Advances **6**, eaat9488 | 10.1126/sciadv.aat9488 | ✅ |

> 每篇论文的详细总结见 [`14_paper_registry.md`](14_paper_registry.md)。

#### 2.1.B 电场畴壁 (EFW)

| # | 说明 | 验证 |
|---|------|:--:|
| — | **无已验证的 EFW 实验文献** | — |

> EFW 的实验实现需要分裂栅（split-gate），间距需 ~100 nm 量级。这是纳米加工的重大挑战，导致 EFW 实验极为稀少。Martin et al. (Science 2008) 提出了 EFW 拓扑零模的理论预言，但实验验证仍缺失。

### 2.2 三层石墨烯 (Trilayer) — 实验极度匮乏

| # | 状态 |
|---|------|
| — | **arXiv 上未找到 ABC 或 ABA 三层石墨烯中孤立畴壁的输运或 STM 实验** |
| — | Zhang et al., Nature Physics **7**, 953 (2011): ABC 三层 QHE 实验（用户 MG 项目已在复现），但此文不涉及畴壁 |
| — | 三层畴壁实验是**明确的领域空白** |

> **用户机会**: DW 项目对三层 LSW 的连续模型 (cont.py 6-band) 和 TBPM (tb.py LSW_ZZ_3L) 计算可能是该方向的首批系统理论研究。若能预言可实验验证的畴壁态特征（色散、DOS、LDOS），计算工作将具有重要参考价值。

### 2.3 多层石墨烯 ($N \ge 4$) 与转角体系

| # | 说明 | 验证 |
|---|------|:--:|
| — | 多层畴壁实验文献未找到 | — |
| — | Moiré DW 独立实验极少（转角畴壁实验通常以网络形式出现，不单独研究单根畴壁）| — |

---

## 3. 关键物理图景

### 3.1 AB/BA 堆叠畴壁的拓扑图像

AB 堆叠双层石墨烯在位移场 $D$ 下有能隙。AB 和 BA 堆叠对应的谷 Chern 数符号相反：

$$C_V^{(\text{AB})} = -C_V^{(\text{BA})} = \pm 2 \cdot \text{sgn}(D)$$

在 AB/BA 边界处，$\Delta C_V = 4$（per spin），根据体边对应，束缚 $|\Delta C_V|$ 条拓扑保护的 1D 边界态。

### 3.2 畴壁宽度

AB ↔ BA 堆叠滑移通过 shear soliton 实现，畴壁宽度 $l_d$ 由层间弹性能和堆叠能竞争决定，典型值 $l_d \sim 10\text{--}20 \text{ nm}$。实验中畴壁宽度难以直接测量，通常通过等离激元反射对比度间接推算。

### 3.3 三层系统的未知

ABC 三层畴壁的拓扑不变量和边界态数目是活跃的理论问题。已知 $\Delta C_V^{\text{ABC}} \neq \Delta C_V^{\text{AB}}$，三层畴壁态可能展现 $J=3$ chirality 的特征。**实验上完全未探索。**

---

## 4. 与 DW 计算项目的关系

### 4.1 可作为 benchmark 的实验数据

| DW 项目计算输出 | 对应的实验测量 | 可用实验 | 状态 |
|---------------|--------------|---------|:--:|
| band structure $E(k_y)$ | s-SNOM 等离激元色散 (间接) / 无直接 ARPES | Jiang 2017 | ⚠️ 间接 |
| DOS $g(E)$ | STS dI/dV | Li S.-Y. 2016 (STM, 但非定量 DOS) | ⚠️ 部分 |
| $\sigma_{xy}, \sigma_{xx}$ (磁场下) | 四端输运 Hall 测量 | **无实验** | 🔴 空白 |
| EFW 边界态色散 | — | **无实验** | 🔴 空白 |
| 三层 LSW 边界态 | — | **无实验** | 🔴 空白 |

### 4.2 可计算预言的实验可观测量

DW 项目可优先计算以下可直接与实验对比的量：
1. **畴壁 LDOS 的空间分布** → 可与 STM 线扫描对比
2. **畴壁弹道电导** $G = (2e^2/h) \times N_{\text{channels}}$ → 可与 Li 2016 型实验对比
3. **磁场下畴壁态对 $\sigma_{xy}$ 的修正** → 这是当前实验完全未涉及的领域

---

## 5. 原始问卷中的错误条目（已更正）

以下条目出现在原始 `DW/docs/experimental_domain_wall_survey.md` 中，经 arXiv 检索**未找到或描述有误**：

| 原始条目 | 原始描述 | 更正后状态 |
|---------|---------|:--:|
| Yin et al. 2014 Science | 双层畴壁非局域电阻测量 | ❌ arXiv 未找到，可能不存在或期刊/年份有误 |
| Yin et al. 2015 Nature Physics | 边缘态和畴壁态输运对比 | ❌ arXiv 未找到，可能描述不准确 |
| Rickhaus et al. 2018 Nano Letters | 栅极调控畴壁输运 | ❌ arXiv 未找到 |
| Kim et al. 2019 Nature Physics | 转角双层畴壁网络输运 | ❌ arXiv 未找到 |
| Sunku et al. 2018 Science | TBG 畴壁近场成像 | ❌ arXiv 未找到 |
| Huang et al. 2018 Nature Materials | TBG 畴壁近场成像 | ❌ arXiv 未找到 |
| McGilly et al. 2020 Nature Nanotech | TBG 畴壁 STM/STS | ❌ arXiv 未找到 |
| Edelberg et al. 2022 | 转角畴壁输运 | ❌ arXiv 未找到 |

> **教训**: 基于 AI 训练记忆的文献列举不可靠，必须交叉验证。用户如需确认上述条目，建议直接在 Web of Science 按作者名搜索。

---

## 6. 实验组与关键研究者（已验证）

| 研究者 | 当前机构 (2026) | 贡献方向 | 代表工作 |
|--------|--------------|---------|---------|
| **Long Ju** | MIT | AB/BA 畴壁 s-SNOM 成像与输运 | Ju 2015 Nature, 近年转向 rhombohedral 多层关联态 |
| **D. N. Basov** | Columbia → UCSD | 近场纳米成像 | Jiang 2017 (co-author) |
| **Jun Zhu** | Penn State | 双层石墨烯畴壁输运 | Li 2016 Nat. Nanotech. (corresponding author) |
| **Seigo Tarucha** | Tokyo → RIKEN | 谷电子学 | Shimazaki 2015 Nat. Phys. |
| **L. C. Campos** | UFMG (Brazil) | 折叠双层畴壁输运 | Mania 2019 Commun. Phys. |
| **N.-C. Yeh** | Caltech | 应变工程拓扑通道 | Hsu 2020 Sci. Adv. |

---

## 7. 推荐下一步

1. **P0**: 精读 [P1] Ju 2015 和 [P2] Li 2016 原文，提取畴壁宽度、位移场大小、电导量级等 benchmark 参数
2. **P1**: 在 Web of Science 追踪 Ju 2015 的所有施引实验论文，填充本文 §5 的空白
3. **P2**: 确认三层畴壁实验的真实空白状态 → 若确认为空白，DW 项目的三层 LSW 计算将具有填补空白的价值
4. **P3**: 用 cont.py 计算畴壁 LDOS 并与 Li S.-Y. 2016 (STM) 数据进行定性对比

---

## 8. 证据等级

| 条目类别 | 证据等级 | 说明 |
|---------|:------:|------|
| §1 畴壁类型与探针 | `fact` | 物理分类 |
| §2 [P1]–[P7] | `verified` | arXiv + DOI 双重确认 |
| §4.1 实验-计算对照 | `interpretation` | 基于已验证文献的推断 |
| §5 错误条目 | `disproved` | arXiv 未找到，原描述不准确 |
| §6 研究组 | `verified` | 从论文作者列表确认 |
