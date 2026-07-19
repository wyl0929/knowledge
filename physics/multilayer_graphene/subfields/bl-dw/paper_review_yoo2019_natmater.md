<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-08 20:10:31
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-08 20:10:32
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/多层石墨烯：转角与非转角体系/refer/paper_review_yoo2019_natmater.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-08
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-08
 * @FilePath     : /project/knowledge/physics/多层石墨烯：转角与非转角体系/refer/paper_review_yoo2019_natmater.md
 * @Description  : Yoo et al. (2019) Nature Materials 阅读笔记
-->
# 论文阅读笔记：Yoo et al., Nature Mater. 18, 448 (2019)

> **Hyobin Yoo, Rebecca Engelke, Stephen Carr, Shiang Fang, Kuan Zhang, Paul Cazeaux, Suk Hyun Sung, Robert Hovden, Adam W. Tsen, Takashi Taniguchi, Kenji Watanabe, Gyu-Chul Yi, Miyoung Kim, Mitchell Luskin, Ellad B. Tadmor, Efthimios Kaxiras, Philip Kim**
> "Atomic and electronic reconstruction at van der Waals interface in twisted bilayer graphene"
> Nature Materials 18, 448–453 (2019) | arXiv:1804.03806
>
> 机构：Harvard (Philip Kim 组) + 多单位理论合作（Kaxiras, Tadmor, Luskin 等）

---

## 1. 一句话总结

通过 **STEM 原子尺度成像**直接观测到：小转角双层石墨烯（$\theta < \theta_c \approx 1^\circ$）中，层间范德华相互作用驱动**晶格重构**——光滑的摩尔条纹转变为尖锐的 AB/BA 三角畴 + 窄 AA 畴壁的阵列结构，简单摩尔能带图像在此转角以下**失效**。

---

## 2. 核心问题

### 2.1 简单摩尔图像 vs 现实

BM 连续模型的标准假设：
- 两层 graphene 保持各自的刚性晶格
- 层间耦合仅在倒空间中产生 Dirac 锥之间的耦合 → 摩尔平带

**但这个假设在小转角下不成立！**
- 层间 vdW 相互作用倾向于使两层原子 local 地对齐到 AB/BA 堆叠（能量更低）
- 但要实现这一点，层内晶格必须发生弹性形变（有能量代价）
- 两种能量的竞争决定了实际结构

### 2.2 关键参数：转角 $\theta$

- **大转角**（$\theta > 1^\circ$）：摩尔周期小 → 层内形变代价高 → 保持非公度（incommensurate）结构
- **小转角**（$\theta < 1^\circ$）：摩尔周期大 → 层内形变代价低 → 晶格重构为 AB/BA 公度畴

---

## 3. 实验方法：STEM 直接成像

### 3.1 技术手段

| 方法 | 用途 |
|---|---|
| **STEM-ADF**（环形暗场扫描透射电镜） | 原子分辨率成像，Z 衬度区分碳原子堆叠方式 |
| **STEM-EELS**（电子能量损失谱） | 局域电子结构（等离激元能量） |
| **暗场 TEM** | 大面积畴结构成像 |
| **电输运** | 位移场调控下的畴壁导电 |

### 3.2 样品制备

- 不同转角的 TBG 器件（$\theta \approx 0.1^\circ$–$2^\circ$）
- 部分器件：hBN 封装 + 双栅结构（用于输运测量）
- STEM 样品：转移到 TEM 网格上

---

## 4. 核心发现

### 4.1 临界转角 $\theta_c \approx 1^\circ$

**这是本文最核心的定量发现：**

> 存在一个特征转角 $\theta_c \approx 1^\circ$，将 TBG 的晶格行为分为两个不同的区域。

| 区域 | $\theta > \theta_c$ | $\theta < \theta_c$ |
|---|---|---|
| 结构 | 光滑的正弦型摩尔条纹 | 尖锐的三角 AB/BA 畴 + 窄 AA 畴壁 |
| 层间耦合 | 均匀/平滑变化 | 局域化：AB/BA 区域强耦合，AA 区域弱耦合 |
| 能带描述 | 简单摩尔能带有效 | **简单摩尔能带失效** |
| 物理 | 刚性晶格近似可接受 | 晶格重构不可忽略 |

### 4.2 STEM 直接观测到的重构

在 $\theta < \theta_c$ 的器件中：
- **AB/BA 三角畴**：平顶的亮/暗区域，尺寸达数十纳米 → 表明这些区域内部原子几乎完美地对齐到 AB 或 BA 堆叠
- **AA 畴壁**：AB 和 BA 畴之间极窄（~几纳米）的过渡区域 → 畴壁处原子堆叠快速翻转
- 这种结构与简单正弦摩尔条纹有**质的不同**——后者预测的是平滑调制的堆叠变化

### 4.3 理论建模：多尺度模拟

本文结合了**连续介质力学 + 紧束缚电子结构**的多尺度模拟：

- **连续介质模型**：描述晶格重构的弹性能 + vdW 相互作用能 → 预测畴结构
- **紧束缚模型**：基于重构后的原子坐标计算电子结构
- **关键结果**：重构使费米速度 $v_F$ 在 AB/BA 畴内恢复接近单层 graphene 值（~10⁶ m/s），而在 AA 畴壁处显著降低

### 4.4 电子结构后果

| 非重构（刚性） | 重构后 |
|---|---|
| 全局平带（魔角物理） | AB/BA 畴内 $v_F$ 恢复 → 畴内无平带 |
| 态密度均匀分布 | 态密度局域化：畴壁处态密度增强 |
| BM 能带适用 | 需要超胞紧束缚或连续介质+TB 混合方法 |

**物理图像**：重构后，AB/BA 畴内电子几乎感受不到摩尔超晶格（因为两层的原子已对齐），畴壁处才是所有有趣物理（平带、拓扑态）发生的地方。

### 4.5 畴壁处的输运

施加垂直位移场 $D$ 后：
- AB/BA 畴中打开能隙 → 变成绝缘体
- 畴壁处出现**一维拓扑导电通道**（量子谷霍尔边缘态）
- 输运测量证实了畴壁导电网络的存在

**这与 Rickhaus 2018 和 Huang 2018 的实验形成完美互补：**
- Huang 2018 (STM)：实空间看到畴壁态密度
- Yoo 2019 (STEM)：原子尺度看到晶格重构 → **解释了畴壁为什么存在**
- Rickhaus 2018 (输运)：测量到畴壁网络的量子干涉

---

## 5. 对领域的深远影响

### 5.1 对魔角物理的修正

- **BM 模型忽略了晶格重构** → 在 $\theta \sim 1.1^\circ$（魔角！）时 $\theta \approx \theta_c$，重构效应**恰好开始变得重要**
- 后续的理论工作（如 Guinea & Walet 2019, Carr et al. 2019 等）系统地包含了弛豫效应
- 弛豫修正了魔角的精确值，并定性地改变了平带的性质（从全局平带 → 畴壁局域的平带）

### 5.2 为畴壁输运子领域奠基

Yoo 2019 直接证明了：
- $\theta < \theta_c$ 时，畴壁是**本征的结构特征**（而非缺陷或无序）
- 畴壁的宽度、形状和电子结构可以通过 $\theta$ 和 $D$ 调控
- 这为 Rickhaus 2018、Xu 2019、Mahapatra 2022 等后续输运实验提供了结构基础

### 5.3 统一了"魔角物理"和"小转角畴壁物理"

```
θ << 1°             θ ~ 1° (θc)        θ ~ 1.1° (魔角)    θ >> 1°
  ← 畴壁物理 →        ← 过渡区 →        ← 关联物理 →       ← 弱耦合 →

强重构               开始重构           临界区域            刚性晶格
AB/BA 大畴          畴壁网络           弛豫对平带重要       BM 模型适用
1D 拓扑通道          混合行为           SC + 关联绝缘态      弱相互作用
```

**Yoo 2019 的核心贡献之一就是确立了 $\theta_c \approx 1^\circ$ 这个分界线，将整个 TBG 物理统一在一张图上。**

---

## 6. 实验技术亮点

| 技术 | 创新点 |
|---|---|
| STEM-ADF 原子成像 | 首次在 TBG 中直接分辨 AB/BA/AA 堆叠的原子级差异 |
| 多尺度理论 | 连续介质力学 + TB 的混合方法——从弹性理论到电子结构的桥梁 |
| 结构-电子关联 | 同一器件上做 STEM + 输运（罕见！） |
| EELS 等离激元 mapping | 直接测量局域电子密度 → 验证畴壁处态密度增强 |

---

## 7. 方法局限

| 局限 | 说明 |
|---|---|
| STEM 是局部探针 | 只能看 ~μm² 区域，无法覆盖整个器件 |
| 输运和 STEM 在不同器件上做 | 结构-输运的直接一一对应仍然困难 |
| 理论是 continuum + TB | 非第一性原理，层间耦合参数 $\gamma_i$ 依赖经验 |
| 动力学未涉及 | 只看了静态结构，畴壁在电场/热扰动下的动力学行为未知 |
| $\theta_c$ 的普适性 | 是否依赖于应变、层数、衬底？→ 未系统研究 |

---

## 8. 与用户研究的关联

| 维度 | 关联 |
|---|---|
| **紧束缚建模** | 重构后的原子坐标可以用 LAMMPS（你已有的工具）做弛豫 → 用弛豫后坐标建 TB 模型 → TBPM 算输运——这是直接的扩展路径 |
| **畴壁的紧束缚描述** | 你的 graphene TB 代码可以直接模拟 AB/BA 畴壁结构（只需在层间 hopping 中引入位置依赖） |
| **Hou 2024 的物理基础** | Yoo 2019 解释了为什么 mTBG 中有清晰定义的 1D 畴壁通道——因为晶格重构将它们锐化了 |
| **Benchmark** | 在 TB 模型中实现晶格重构 → 验证畴壁处的态密度增强（与 STEM-EELS 对比） |

---

## 9. 关键参数速查

| 参数 | 值 |
|---|---|
| 临界转角 $\theta_c$ | ≈ 1°（~0.8°–1.2° 过渡区） |
| AB/BA 畴尺寸 | 几十 nm（取决于 $\theta$） |
| AA 畴壁宽度 | ~几 nm |
| 重构驱动力 | 层间 vdW 能 vs 层内弹性能 |
| STEM 分辨率 | ~1 Å（原子分辨率） |
| 位移场 $D$ | ±0.5 V/nm（畴壁输运实验） |

---

## 10. 在三篇论文链条中的位置

```
Yoo 2019 (Nature Mater.)          ← 结构基础：晶格重构 → 畴壁从何而来
  ├→ Huang 2018 (PRL, STM)        ← 电子结构：畴壁态密度实空间成像
  ├→ Rickhaus 2018 (Nano Lett.)   ← 输运证据：FP + AB 振荡
  └→ Hou 2024 (PRB)              ← 理论裁决：TZM vs 网络模型
```

**Yoo 2019 是这一链条的底层**——它回答了"为什么小转角 TBG 中会自然形成一维导电通道"的结构起源问题。

---

*笔记创建日期：2026-07-08 | 基于 arXiv:1804.03806v2 + Nature Materials 18, 448 (2019)*
