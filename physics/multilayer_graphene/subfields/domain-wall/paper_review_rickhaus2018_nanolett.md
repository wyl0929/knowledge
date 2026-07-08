<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-08 17:16:04
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-08 17:43:37
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/multilayer_graphene/subfields/domain-wall/paper_review_rickhaus2018_nanolett.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-08
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-08
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/domain-wall/paper_review_rickhaus2018_nanolett.md
 * @Description  : Rickhaus et al. (2018) Nano Letters 阅读笔记
-->
# 论文阅读笔记：Rickhaus et al., Nano Lett. 18, 6725 (2018)

> **Peter Rickhaus, John Wallbank, Sergey Slizovskiy, Riccardo Pisoni, Hiske Overweg, Yongjin Lee, Marius Eich, Ming-Hao Liu, K. Watanabe, T. Taniguchi, Vladimir Fal'ko, Thomas Ihn, Klaus Ensslin**
> "Transport through a network of topological states in twisted bilayer graphene"
> Nano Lett. 18, 6725–6730 (2018) | arXiv:1802.07317
>
> 机构：ETH Zurich（Ihn/Ensslin 组）+ 理论合作者 Fal'ko（Manchester/Lancaster），日本 NIMS 提供 hBN
>
> **DOI**: [10.1021/acs.nanolett.8b02387](https://doi.org/10.1021/acs.nanolett.8b02387)
> **Zotero Key**: `AE42BE4G` → `cmd.exe /c start "zotero://select/items/AE42BE4G"`

---

## 1. 一句话总结

在**小转角（< 1°）双层石墨烯**中，通过电输运测量首次观测到 Fabry-Pérot 和 Aharonov-Bohm 干涉振荡，且这些振荡在 **0–8 T 磁场范围内保持稳健**——直接证明了 mTBG 中存在**拓扑保护的一维导电通道网络**。

---

## 2. 物理背景

### 2.1 小转角 TBG 的畴结构

在 $\theta \ll 1.1^\circ$（远小于魔角）的双层石墨烯中：
- 摩尔周期极大 → AB/BA 堆叠区域形成微米级三角畴
- 畴壁处出现**量子谷霍尔（QVH）边缘态**：来源于 AB/BA 两侧谷 Chern 数之差 $\Delta C_V = 2$
- 这些一维通道交汇于 AA 堆叠点，形成**三角网络**

### 2.2 本文之前的状态

- **理论**：San-Jose & Prada (2013) 预言了螺旋网络；Efimkin & MacDonald (2018) 系统化
- **STM**：Huang et al. (2018) 已在实空间观测到畴壁处的拓扑态
- **输运**：尚无实验报道——本文是第一个

---

## 3. 实验方法

### 3.1 器件制备

- 小转角双层石墨烯（$\theta \approx 0.5^\circ$–$1^\circ$），通过 tear-and-stack 方法制备
- hBN 封装 → 高迁移率
- 双栅结构（顶栅 + 底栅）→ 独立调控载流子密度 $n$ 和垂直位移场 $D$
- 标准霍尔棒几何，多端口测量

### 3.2 测量方案

- **温度**：$T = 1.5$ K（液氦）和 $T = 30$ mK（稀释制冷机）
- **磁场**：$B = 0$–$8$ T，垂直平面
- **测量量**：
  - 四端电阻 $R_{xx}$ 和霍尔电阻 $R_{xy}$
  - 重点关注 $R_{xx}$ 中叠加在缓慢背景上的快速振荡

### 3.3 关键实验参数

| 参数 | 典型值 |
|---|---|
| 扭转角 $\theta$ | ~0.5°–1° |
| 摩尔周期 $a_M$ | ~14–28 nm |
| 器件迁移率 | ~10⁵ cm²/Vs（hBN 封装） |
| 温度 | 30 mK – 1.5 K |
| 磁场范围 | 0–8 T |

---

## 4. 核心实验结果

### 4.1 Fabry-Pérot (FP) 振荡

**观测**：
- 在 $R_{xx}$ 随栅压（载流子密度 $n$）的扫描中，观察到**规则的周期性振荡**
- 振荡周期 $\Delta n$ 与密度呈**线性关系**

**物理图像**：
- 电子在 1D 通道中传播 → 在畴壁交点（AA 点）处部分反射 → 电子在两反射点之间形成 Fabry-Pérot 干涉
- FP 谐振条件：$2L = m\lambda_F$，其中 $L$ 为通道长度，$\lambda_F$ 为费米波长
- 线性 $\Delta n$ 关系 → 确认了 1D 导电通道的弹道输运

### 4.2 Aharonov-Bohm (AB) 振荡

**观测**：
- 在固定栅压下扫磁场 $B$，$R_{xx}$ 出现**周期性振荡**
- 振荡周期 $\Delta B \approx \Phi_0 / A$，其中 $\Phi_0 = h/e$ 为磁通量子，$A$ 为干涉回路面积

**物理图像**：
- 电子沿三角畴壁网络形成闭合回路 → AB 效应
- 回路面积 $A \sim (a_M)^2 \propto 1/\theta^2$ → 从 $\Delta B$ 可反推畴尺寸
- 不同栅压对应不同干涉回路面积 → AB 周期随栅压变化

### 4.3 拓扑保护的最强证据：磁场稳健性

**这是本文最关键的发现**：

> FP 和 AB 振荡在 **0–8 T 的整个磁场范围内持续存在**。

为什么这很惊人？
- 在传统的 2D 电子气中，磁场会使体态电子偏转（洛伦兹力）→ 轨迹弯曲 → 干涉条件被破坏
- 在 mTBG 中，振荡对磁场**不敏感** → 电子被**拓扑束缚**在 1D 通道中，洛伦兹力无法将其拉出畴壁
- 这是拓扑保护的直接输运证据

### 4.4 补充证据

| 观测 | 推论 |
|---|---|
| 振荡周期 $\Delta n \propto n$（线性） | 1D 通道的弹道输运 |
| 振荡对温度不敏感（30 mK – 1.5 K） | 相位相干长度 > 通道长度 |
| 振荡对 $B$ 不敏感（0–8 T） | 拓扑保护 |
| 位移场 $D$ 可调控振荡幅度 | $D$ 调控畴壁的拓扑能隙 |

---

## 5. 理论支持（与 Fal'ko 合作）

本文的实验分析与 Fal'ko 组的理论计算紧密结合：

- **连续模型**：计算 mTBG 的能带结构和畴壁态的色散
- **螺旋网络模型**：将畴壁态建模为 1D 手征通道的网络
- **量子输运模拟**：基于网络模型计算预期干涉图案

理论关键结论：
- 畴壁处存在两条相反手征的边缘态（per spin per valley）
- 网络模型的干涉图案与实验观测的 FP 和 AB 振荡定性一致
- 干涉对磁场的稳健性来源于 QVH 态的拓扑保护

---

## 6. 论文意义与影响

### 6.1 历史地位

- **第一篇**在 mTBG 中通过输运测量观测到拓扑通道网络的实验论文
- 与 Huang et al. (2018, STM) 互补：STM 看结构，输运看量子相干
- 开启了 mTBG 畴壁输运这一子领域

### 6.2 对 Hou 2024 争议的贡献

Rickhaus 2018 观察到的 FP 振荡被**双方引用**但给出不同解释：

| 解释 | 模型 |
|---|---|
| 电子在三角网络中干涉（AA 点处散射） | 2D 网络模型 |
| 电子在独立 1D 通道中来回反射（两端边界） | 1D TZM 模型（Hou 2024 支持） |

**关键点**：Hou 2024 指出，Rickhaus 观测到的 FP 振荡**可以完全由 TZM 模型解释**（电子在通道的两端——即与电极接触处——反射形成 FP 腔），**不需要**假设 AA 点处的散射。

### 6.3 后续实验

- **Xu et al., Nat. Commun. 10, 4008 (2019)**（Geim 组）：在更大面积器件中观测到巨幅 AB 振荡，进一步支持网络模型
- **Mahapatra et al., Nano Lett. 22, 5708 (2022)**：在 mTBG 三角畴中实现量子霍尔干涉测量

---

## 7. 方法局限

| 局限 | 说明 |
|---|---|
| 无法直接成像通道 | 输运测量只能推断，无法像 STM 那样直接看到畴壁态 |
| 振荡的定量建模困难 | 真实器件中畴壁网络不规则 → 精确模拟干涉图案需要知道确切的畴结构 |
| 无法区分网络 vs TZM | 本文的 FP 振荡被双方模型解释，本身不能裁决模型争议 |
| 仅低磁场 | 8T 不足以进入量子霍尔区域（mTBG 的 Hofstadter 物理需要更高场） |
| 器件之间差异大 | 畴结构依赖于局域应变和扭转角不均匀 → 器件间可重复性受限 |

---

## 8. 与用户研究的关联

| 维度 | 关联 |
|---|---|
| **计算方法** | 本文的实验结果（FP/AB 振荡）可以用 TBPM + Kubo-Bastin 在真实空间 TB 模型中模拟——验证你的代码对此类干涉现象的捕捉能力 |
| **扩展方向** | (1) FP 振荡与温度的关系（退相干）；(2) 磁场下的 Hofstadter 物理 + 畴壁输运的相互作用（本文仅到 8T）；(3) 三层 mTBG 中畴壁网络的输运 |
| **Benchmark** | 如果能在 TB 模型中复现 FP 振荡的线性 $\Delta n \propto n$ 关系，就是对 TBPM 输运代码的有力验证 |

---

## 9. 关键参数速查

| 参数 | 值 |
|---|---|
| 器件类型 | hBN 封装的 mTBG Hall bar |
| 扭转角 | ~0.5°–1° |
| 摩尔周期 | ~14–28 nm |
| 载流子密度范围 | ~10¹¹–10¹² cm⁻² |
| 位移场范围 | ±0.5 V/nm（典型值） |
| 温度 | 30 mK（最低）；1.5 K（常规） |
| 磁场 | 0–8 T |
| 迁移率 | ~10⁵ cm²/Vs |

---

## 10. 与 Hou 2024 的对比

| 维度 | Rickhaus 2018 | Hou 2024 |
|---|---|---|
| 类型 | **实验** | 理论/计算 |
| 核心证据 | FP + AB 振荡（输运） | NQCP $G=1,2,3$（模拟） |
| 对 THS 传播方式的立场 | 倾向网络模型（但未排除 TZM） | 明确支持 TZM 模型 |
| 磁场 | 0–8T → 证明拓扑保护 | 未考虑磁场 |
| 通道可视化 | 间接（通过干涉） | 直接（非平衡 LDOS） |
| 后续可验证预言 | — | NQCP 1/2/3 平台 |

---

*笔记创建日期：2026-07-08 | 基于 arXiv:1802.07317v2 + 已发表 Nano Lett. 18, 6725 (2018)*
