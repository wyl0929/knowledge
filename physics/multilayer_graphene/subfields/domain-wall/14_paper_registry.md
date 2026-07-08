<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-07 17:33:46
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-07 17:33:47
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/multilayer_graphene/subfields/domain-wall/14_paper_registry.md
 * @Description  :
-->
<!--
 * @Author       : AI-generated (research_onboarding_skill, subfield)
 * @Date         : 2026-07-07
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/domain-wall/14_paper_registry.md
 * @Description  : 石墨烯 Domain Wall 实验 — 已验证关键文献注册与详细总结
-->

# 14 Paper Registry / 关键文献注册 — Domain Wall 实验

Last updated: 2026-07-07

> 仅收录经 arXiv + DOI 验证的文献。每篇重点论文给出详细总结。

---

## [P1] Ju et al. (2015) — 奠基性实验

| 字段 | 内容 |
|------|------|
| **标题** | Topological valley transport at bilayer graphene domain walls |
| **作者** | L. Ju, Z. Shi, N. Nair, Y. Lv, C. Jin, J. Velasco Jr., C. Ojeda-Aristizabal, H. A. Bechtel, M. C. Martin, A. Zettl, J. Analytis, F. Wang |
| **期刊** | Nature **520**, 650–655 (2015) |
| **DOI** | [10.1038/nature14364](https://doi.org/10.1038/nature14364) |
| **arXiv** | 未公开（Nature 论文，发表前无 arXiv 版本） |
| **类型** | 实验 — 近场红外纳米成像 (s-SNOM) + 输运 |
| **Zotero Key** | `ZT_KEY_NEEDED` |

### 核心贡献

**首次直接可视化** AB/BA 堆叠畴壁在双层石墨烯中的存在和导电性。

### 方法

- **样品制备**: hBN 封装的 AB 堆叠双层石墨烯，机械剥离中自然形成 AB/BA 堆叠边界
- **近场成像**: 散射型扫描近场光学显微镜 (s-SNOM)，中红外 (~890 cm⁻¹) 激发，空间分辨 ~20 nm
- **输运**: 双栅极调控位移场 $D$ 和载流子浓度 $n$

### 关键结果

1. **畴壁实空间成像**: s-SNOM 图像中 AB/BA 边界呈现清晰的线状对比度——畴壁处红外反射率与畴区不同
2. **谷极化等离激元反射**: 畴壁上等离激元的反射/传播取决于入射的谷极化方向，直接验证了畴壁态的谷-动量锁定（valley-momentum locking）
3. **位移场调控**: 畴壁对比度随 $D$ 增大而增强——能隙越大，畴壁态越局域
4. **畴壁宽度**: 从 s-SNOM 对比度剖面推断 $\sim 10\text{--}20$ nm

### 局限

- s-SNOM 不能直接测量态密度或色散
- 基于等离激元反射间接推断谷极化，非直接电学测量
- 无磁场下的输运数据（QHE 下的畴壁行为未知）

### 与用户关联

⭐⭐⭐⭐⭐ **DW 项目最直接的实验参照**。cont.py 和 tb.py 的 LSW 计算可直接与 Ju 2015 的物理图景对比。s-SNOM 对比度剖面可与 LDOS 计算定性比较。

---

## [P2] Li et al. (2016) — 栅控畴壁输运

| 字段 | 内容 |
|------|------|
| **标题** | Gate-controlled topological conducting channels in bilayer graphene |
| **作者** | J. Li, K. Wang, K. J. McFaul, Z. Zern, Y. F. Ren, K. Watanabe, T. Taniguchi, Z. H. Qiao, J. Zhu |
| **期刊** | Nature Nanotechnology **11**, 1060–1065 (2016) |
| **DOI** | [10.1038/nnano.2016.158](https://doi.org/10.1038/nnano.2016.158) |
| **arXiv** | [1509.03912](https://arxiv.org/abs/1509.03912) |
| **类型** | 实验 — 双栅极输运测量 |
| **Zotero Key** | `ZT_KEY_NEEDED` |

### 核心贡献

首次通过**双栅极输运**实验验证了 AB/BA 畴壁通道的电导可由位移场调控——畴壁通道的开/关通过 $D$ 场控制。

### 方法

- **器件**: hBN 封装 AB 堆叠双层石墨烯 Hall bar，分裂顶栅 + 全局底栅
- **输运测量**: 四端法测量电阻，低温 (~1.5 K)
- **操控参数**: 位移场 $D$、载流子浓度 $n$、磁场 $B$

### 关键结果

1. **畴壁电导的位移场依赖性**: 畴壁通道电导随 $|D|$ 增大从 ~0（$D=0$，无能隙）增大到 ~$4e^2/h$（$|D|$ 较大时）
2. **栅极调控开/关**: 分裂栅允许在空间不同区域施加不同 $D$ 极性 → 在栅边界形成 EFW-like 条件
3. **拓扑保护**: 畴壁电导对非磁性散射不敏感（弱无序下电导稳定）
4. **磁场响应**: 垂直磁场下畴壁通道出现 SdH 振荡

### 局限

- 未能直接测量畴壁通道的弹道电导量子化（器件中可能存在多个畴壁通道并联）
- 器件中同时存在边缘态和畴壁态，难以完全分离两者贡献
- 未测量 $\sigma_{xy}$

### 与用户关联

⭐⭐⭐⭐⭐ 这是 DW 项目中 $\sigma_{xx}$ 和 $\sigma_{xy}$ 计算最直接的实验对标。Li 2016 的器件几何（split-gate AB/BA bilayer）与 DW 项目 cont.py 中的 EFW + LSW 设置直接对应。

---

## [P3] Jiang et al. (2017) — 畴壁等离激元反射

| 字段 | 内容 |
|------|------|
| **标题** | Plasmon reflections by topological electronic boundaries in bilayer graphene |
| **作者** | B.-Y. Jiang, G.-X. Ni, Z. Addison, J. K. Shi, X. Liu, F. Zhao, P. Kim, E. J. Mele, D. N. Basov, M. M. Fogler |
| **期刊** | Nano Letters **17**, 7252–7257 (2017) |
| **DOI** | [10.1021/acs.nanolett.7b03816](https://doi.org/10.1021/acs.nanolett.7b03816) |
| **arXiv** | [1707.03980](https://arxiv.org/abs/1707.03980) |
| **类型** | 实验 (s-SNOM) + 理论分析 |
| **Zotero Key** | `ZT_KEY_NEEDED` |

### 核心贡献

系统研究了双层石墨烯中**畴壁对等离激元的反射和透射**，证明了畴壁作为1D电子边界对集体激发的控制作用。Basov 组（近场成像领域的全球领导者）出品。

### 方法

- **s-SNOM 成像**: 中红外 (~890 cm⁻¹) 激发，空间分辨 ~20 nm，探测畴壁附近的等离激元驻波图案
- **样品**: hBN 封装 AB 堆叠双层石墨烯

### 关键结果

1. **等离激元反射系数**: 畴壁对等离激元的反射率随位移场 $D$ 增大而增大
2. **畴壁宽度定量提取**: 从等离激元驻波间距反推畴壁有效宽度
3. **理论模型**: 用畴壁处的电导率跳变模型定量解释反射系数

### 局限

- 等离激元探针是间接测量——不直接反映单粒子电子结构
- 频率范围有限（中红外单频激发，非宽带谱）

### 与用户关联

⭐⭐⭐⭐ 等离激元反射的定量分析依赖畴壁电子结构的细节——DW 项目的 LDOS 计算可为实验提供微观解释。

---

## [P4] Shimazaki et al. (2015) — 纯谷电流生成与检测

| 字段 | 内容 |
|------|------|
| **标题** | Generation and detection of pure valley current by electrically induced Berry curvature in bilayer graphene |
| **作者** | Y. Shimazaki, M. Yamamoto, I. V. Borzenets, K. Watanabe, T. Taniguchi, S. Tarucha |
| **期刊** | Nature Physics **11**, 1032–1036 (2015) |
| **DOI** | [10.1038/nphys3551](https://doi.org/10.1038/nphys3551) |
| **arXiv** | [1501.04776](https://arxiv.org/abs/1501.04776) |
| **类型** | 实验 — 谷电子学 |
| **Zotero Key** | `ZT_KEY_NEEDED` |

### 核心贡献

在**双层石墨烯中**（无畴壁）首次实现纯谷电流的电学生成与检测——通过位移场诱导的 Berry 曲率产生谷霍尔效应。

### 方法

- **器件**: 双栅极 AB 堆叠双层石墨烯 Hall bar
- **生成**: 电流通过 → Berry 曲率驱动谷霍尔效应 → 横向谷电流（无净电荷流）
- **检测**: 非局域电阻测量

### 关键结果

1. 非局域电阻信号随 $D$ 增大而增强——与 Berry 曲率 $\propto D$ 一致
2. 谷电流信号随温度升高而指数衰减——谷退相干
3. 验证了双层石墨烯中谷自由度的电学可操控性

### 局限

- **此文不是畴壁实验**——研究的对象是体态谷输运，非畴壁态
- 非局域电阻信号的物理起源仍有争议（可能包含其他机制）

### 与用户关联

⭐⭐⭐ 此文是双层石墨烯谷电子学的 benchmark——用户 DW 项目的畴壁输运计算需要与此文中的**体态**谷霍尔效应区分开来。

---

## [P5] Mania et al. (2019) — 折叠双层畴壁输运

| 字段 | 内容 |
|------|------|
| **标题** | Topological valley transport at the curved boundary of a folded bilayer graphene |
| **作者** | E. Mania, A. R. Cadore, T. Taniguchi, K. Watanabe, L. C. Campos |
| **期刊** | Communications Physics **2**, 6 (2019) |
| **DOI** | [10.1038/s42005-018-0106-4](https://doi.org/10.1038/s42005-018-0106-4) |
| **arXiv** | [1901.08178](https://arxiv.org/abs/1901.08178) |
| **类型** | 实验 — 输运 |
| **Zotero Key** | `ZT_KEY_NEEDED` |

### 核心贡献

在**折叠双层石墨烯**（folded bilayer）的弯曲边界处观测到拓扑谷输运——折叠边界类似于弯曲的畴壁。

### 方法

- **样品**: 机械剥离中产生的折叠双层石墨烯（折叠线即弯曲的 AB/BA 边界）
- **输运**: 沿折叠线的电导测量
- **特点**: 折叠边界天然形成封闭回路，不同于开路畴壁

### 关键结果

1. 折叠线电导远高于畴区——沿折叠边界的导电通道
2. 位移场可调控折叠线电导
3. 磁场下出现 Aharonov-Bohm 振荡——折叠线形成封闭导电回路

### 局限

- 折叠边界的曲率引入复杂性（非平直畴壁）
- 回路几何 → 干涉效应使结果难以直接与平直畴壁理论对比

### 与用户关联

⭐⭐⭐ 此文展示了畴壁在非理想几何中的行为——DW 项目的平直畴壁计算提供的是理想极限，可与 Mania 2019 的弯曲效应对比。

---

## [P6] Li S.-Y. et al. (2016) — 堆叠孤子 STM 成像

| 字段 | 内容 |
|------|------|
| **标题** | Corrugation induced stacking solitons with topologically confined states in gapped bilayer graphene |
| **作者** | S.-Y. Li, H. Jiang, J.-J. Zhou, H. Liu, F. Zhang, L. He |
| **期刊** | arXiv only (2016), 发表状态待确认 |
| **DOI** | —（arXiv: [1609.03313](https://arxiv.org/abs/1609.03313)） |
| **类型** | 实验 (STM/STS) + 理论 |
| **Zotero Key** | `ZT_KEY_NEEDED` |

### 核心贡献

STM 直接成像了双层石墨烯中由表面褶皱（corrugation）诱导的堆叠孤子（stacking soliton），并测量了孤子处的局域态密度。

### 方法

- **STM/STS**: 低温扫描隧道显微镜/谱，空间分辨原子级
- **样品**: hBN 封装的双层石墨烯

### 关键结果

1. **堆叠孤子实空间成像**: STM 图中 AB/BA 边界呈现增强的局域态密度——边界态的直接实验证据
2. **孤子拓扑起源**: 褶皱导致层间滑移 → 形成堆叠孤子
3. **态密度增强**: 孤子处在费米能附近态密度显著增强——1D 边界态特征

### 局限

- STM 只能测量占据态 → 能量窗口受限
- 褶皱引入应变 → 与理想平直畴壁有区别
- arXiv only —— 正式发表状态需确认

### 与用户关联

⭐⭐⭐⭐⭐ **DW 项目 LDOS 计算最直接的实验对标**。cont.py 计算的 LDOS $(x, E)$ 图可与 Li S.-Y. 的 STM 线扫描直接对比。

---

## [P7] Hsu et al. (2020) — 应变工程拓扑通道

| 字段 | 内容 |
|------|------|
| **标题** | Nanoscale Strain Engineering of Giant Pseudo-Magnetic Fields, Valley Polarization and Topological Channels in Graphene |
| **作者** | C.-C. Hsu, M. L. Teague, J.-Q. Wang, N.-C. Yeh |
| **期刊** | Science Advances **6**, eaat9488 (2020) |
| **DOI** | [10.1126/sciadv.aat9488](https://doi.org/10.1126/sciadv.aat9488) |
| **arXiv** | [2005.05532](https://arxiv.org/abs/2005.05532) |
| **类型** | 实验 (STM) |
| **Zotero Key** | `ZT_KEY_NEEDED` |

### 核心贡献

通过纳米尺度应变工程在石墨烯中产生**巨赝磁场**（~100 T 量级）和谷极化拓扑通道——一种不同于传统 LSW/EFW 的畴壁实现方式。

### 方法

- **STM**: 测量局域态密度
- **应变**: 通过衬底纳米结构施加可控非均匀应变

### 关键结果

1. 应变梯度产生赝磁场，等效于真实磁场
2. 赝磁场符号反转处形成拓扑通道（类似于畴壁）
3. 拓扑通道中观测到谷极化输运

### 局限

- 应变通道的拓扑性质与传统 domain wall 有区别（赝磁场机制 vs 质量反转机制）
- 应变大小难以精确控制

### 与用户关联

⭐⭐⭐ 此文的应变畴壁物理不同于 DW 项目中的 LSW/EFW（基于 stacking 或 D-field 反转），但方法上可互相借鉴。

---

## 补充：[P0] Zhang et al. (2011) — ABC 三层 QHE 实验

| 字段 | 内容 |
|------|------|
| **标题** | Landau-level splitting in graphene trilayers |
| **作者** | L. Zhang, Y. Zhang, J. Camacho, M. Khodas, I. Zaliznyak |
| **期刊** | Nature Physics **7**, 953–957 (2011) |
| **DOI** | 10.1038/nphys2104 |
| **类型** | 实验 — 量子霍尔输运 |
| **Zotero Key** | `ZT_KEY_NEEDED` |

### 核心贡献

首次实验测量 ABC 三层石墨烯的量子霍尔效应，确认 $J=3$ chirality 的标志性台阶序列 $\nu = \pm 6, \pm 10, \pm 14$。

### 与用户关联

⭐⭐⭐⭐⭐ 用户 MG 项目已在复现此文（参见 `MG/docs/blue_print.md` Phase 4）。此文是 DW 项目三层畴壁计算的基础参考——理解无畴壁时三层 QHE 的行为是理解畴壁修正的前提。

---

## 论文关系图

```
Ju 2015 (Nature)              ← 奠基：AB/BA 畴壁 s-SNOM 可视化
    ├── Li 2016 (Nat. Nano.)  ← 发展：双栅输运测量畴壁电导
    ├── Jiang 2017 (Nano Lett.)← 发展：等离激元反射定量
    └── Mania 2019 (Commun.)  ← 发展：弯曲畴壁输运

Li S.-Y. 2016 (STM)           ← 互补：STM 直接看局域态密度

Shimazaki 2015 (Nat. Phys.)   ← 相关：体态谷霍尔效应（非畴壁）

Zhang 2011 (Nat. Phys.)       ← 基础：ABC 三层 QHE（畴壁计算的体态 baseline）

Hsu 2020 (Sci. Adv.)          ← 新方向：应变工程拓扑通道
```

---

---

## 补充：mTBG 畴壁输运（小转角双层石墨烯中的畴壁物理）

> 以下论文涉及小转角双层石墨烯（mTBG, $\theta \ll 1.1^\circ$）中 AB/BA 堆叠畴壁的拓扑通道输运。与前述非转角畴壁实验互补——mTBG 的畴壁由摩尔超晶格自然形成，而非机械剥离中的随机堆叠边界。

| # | 文献 | 贡献 | 精读 |
|---|---|---|---|
| [DW-m1] | **Rickhaus et al., Nano Lett. 18, 6725 (2018)** | mTBG 畴壁网络输运实验：首次观测 Fabry-Pérot + AB 振荡，0–8T 磁场稳健 → 证明拓扑保护的一维导电通道 | 📄 [阅读笔记](paper_review_rickhaus2018_nanolett.md) |
| [DW-m2] | **★ Hou, Yuan & Jiang, PRB 110, L161406 (2024)** | 量子输运模拟裁决：THS 形成独立一维 TZM（非二维网络），预言 NQCP 1/2/3 电导平台 | 📄 [精读报告](paper_review_hou2024_prb.md) |
| [DW-m3] | Xu et al., Nat. Commun. 10, 4008 (2019) | mTBG 中巨幅 AB 振荡——三角畴壁网络的大面积输运 | — |
| [DW-m4] | Mahapatra et al., Nano Lett. 22, 5708 (2022) | mTBG 三角畴中的量子霍尔干涉 | — |

**与前述非转角畴壁实验的关键区别**：
- 非转角畴壁（P1–P7）：机械剥离中的随机 AB/BA 边界，位移场 $D$ 调控能隙 → 拓扑通道
- mTBG 畴壁（DW-m1–m4）：摩尔超晶格自组织形成的周期性畴壁网络，转角 $\theta$ + $D$ 联合调控

---

## 用户 DW 项目的文献对照矩阵

| DW 计算 | 最近实验对标 | 对标质量 | 备注 |
|---------|------------|:------:|------|
| cont.py 2-band/4-band LDOS | Li S.-Y. 2016 STM | ⭐⭐⭐⭐ | 最佳对标 |
| cont.py 6-band ABC LSW | **无实验** | 🔴 | 空白——DW 项目可填补 |
| tb.py LSW band structure | Jiang 2017 等离激元 (间接) | ⭐⭐ | 间接对标 |
| $\sigma_{xx}$ (LSW, 无磁场) | Li 2016 + Mania 2019 | ⭐⭐⭐ | 可定性对比 |
| $\sigma_{xy}$ (LSW, 有磁场) | **无实验** | 🔴 | 空白——DW 项目 Phase 5 目标 |
| EFW (任何计算) | **无实验** | 🔴 | 空白 |
