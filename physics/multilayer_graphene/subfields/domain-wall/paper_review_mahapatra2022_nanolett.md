<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-09 21:35:07
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-09 21:35:11
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/multilayer_graphene/subfields/domain-wall/paper_review_mahapatra2022_nanolett.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-09
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-09
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/domain-wall/paper_review_mahapatra2022_nanolett.md
 * @Description  : Mahapatra et al. (2022) Nano Letters 阅读笔记
-->
# 论文阅读笔记：Mahapatra et al., Nano Lett. 22, 5708 (2022)

> **Phanibhusan S. Mahapatra, Manjari Garg, Bhaskar Ghawri, Aditya Jayaraman, Kenji Watanabe, Takashi Taniguchi, Arindam Ghosh, U. Chandni**
> "Quantum Hall interferometry in triangular domains of marginally twisted bilayer graphene"
> Nano Lett. 22, 5708 (2022) | arXiv:2112.03891
>
> 机构：Indian Institute of Science (IISc), Bangalore — Ghosh 组 + Chandni 组

---

## 1. 一句话总结

在**极低转角**（$\theta \approx 0.16^\circ$）的双层石墨烯中，利用 AB/BA 三角畴的**天然几何结构**作为量子霍尔干涉仪，通过**磁热电功率**（magneto-thermopower）观测到 Fabry-Pérot 和 Aharonov-Bohm 干涉振荡。无需额外门控定义复杂结构——畴壁网络本身就是干涉仪。

---

## 2. 与之前实验的关键区别

| 维度 | 之前实验（Rickhaus, Xu 等） | Mahapatra 2022 |
|---|---|---|
| 物理区域 | 零场或低场，畴壁主导的 1D 输运 | **量子霍尔区域**（$\nu = 4, 8$），朗道能级 + 畴壁共存 |
| 扭转角 | ~0.5°–1° | **~0.16°**（极低！） |
| 测量量 | 电阻/电导（$R_{xx}, G$） | **热电功率**（thermopower $S_{xx}$） |
| 干涉仪结构 | 不明确——依赖器件边界和畴壁 | 三角 AB/BA 畴天然构成干涉回路 |
| 库仑阻塞 | 可能存在 | **显著减弱**（关键优势） |

---

## 3. 物理背景：为什么需要量子霍尔干涉仪？

### 3.1 动机：非阿贝尔任意子的编织

QH 干涉仪是探测分数量子霍尔态中**非阿贝尔编织统计**的标准平台。基本思想：
- 让 FQH 边缘态沿两条路径传播
- 在干涉仪中形成一个闭合回路
- 准粒子绕另一个准粒子一周 → 波函数获得一个非平凡的编织相位
- 干涉图案的变化编码了编织统计信息

### 3.2 传统 QH 干涉仪的困境

传统方法用静电门控在 2DEG（如 GaAs）上定义干涉仪：
- 需要复杂的门控图案
- **库仑充电效应**：干涉仪作为一个量子点，充电能 $E_C$ 破坏相位相干
- 需要精细调谐以压制 $E_C$

### 3.3 mTBG 的天然优势

mTBG 中的 AB/BA 三角畴（在 $\theta \ll \theta_c$ 下形成）天然提供了：
- **三角形的闭合导电回路**——畴壁围成三角形
- **弱的库仑充电**——畴壁与体态之间的电容耦合使充电能被有效屏蔽
- 不需要人工定义门控结构

---

## 4. 实验方法

### 4.1 器件

| 参数 | 值 |
|---|---|
| 材料 | mTBG，hBN 封装 |
| 扭转角 | $\theta \approx 0.16^\circ$（极低） |
| 摩尔周期 | $a_M \approx 88$ nm |
| AB/BA 畴尺寸 | ~数百 nm（三角畴边长） |

### 4.2 测量方案

- **磁热电功率** $S_{xx}$：在器件上施加温度梯度 $\Delta T$，测量产生的热电压 → $S_{xx} = V_{xx} / \Delta T$
- 热电功率对费米能级的变化比电阻更敏感（$S \propto \partial \ln G / \partial E$），因此干涉振荡在 $S_{xx}$ 中更明显
- 扫描 $(n, B)$ 参数空间，寻找干涉图案

### 4.3 为什么用热电而非电阻？

热电功率 $S_{xx}$ 通过 Mott 公式与电导关联：

$$S_{xx} \propto \left. \frac{\partial \ln G}{\partial E} \right|_{E_F}$$

- 热电测量**放大**了费米能级附近的态密度变化
- QH 边缘态的干涉对 $E_F$ 极其敏感 → 热电信号中的干涉振荡比电阻中更清晰
- 这是本文的一个重要方法创新

---

## 5. 核心实验结果

### 5.1 QH 区域中的 Fabry-Pérot 振荡

在 $\nu = 4, 8$ 的 QH 平台区域：
- $S_{xx}$ 随 $B$（或 $n$）表现出**周期性振荡**
- 振荡周期与畴壁通道长度 $L$ 一致：$\Delta k \cdot 2L = 2\pi$ → FP 条件
- FP 振荡的"腔"是**畴壁的一维段**——畴壁通道在三角顶点之间的部分

**与 Rickhaus 2018（零场 FP）的对比**：
- Rickhaus：FP 振荡出现在**零场或低场**，振荡来源于畴壁态本身的干涉
- Mahapatra：FP 振荡出现在**QH 区域**（$\nu = 4, 8$），振荡来源于 QH 边缘态在畴壁通道中的干涉
- 两者都证明了畴壁通道的弹道性质，但在不同的物理区域

### 5.2 Aharonov-Bohm 振荡

- $S_{xx}$ 在固定 $n$ 下随 $B$ 的变化显示出 AB 振荡
- 振荡周期 $\Delta B = \Phi_0 / A$，其中 $A$ 为三角畴的面积
- **每个三角畴作为一个天然的 AB 干涉仪**——畴壁的三条边构成闭合回路
- 不同三角畴大小不同 → 多个叠加的 AB 周期 → 可用 FFT 分离

### 5.3 库仑充电效应的减弱

这是对 QH 干涉仪应用至关重要的发现：
- 在传统门控定义的干涉仪中，$E_C \sim e^2/C$ → 库仑阻塞 → 干涉条件被破坏
- 在 mTBG 中，畴壁与体态的强耦合 → 有效电容 $C_{\text{eff}}$ 很大 → $E_C$ 很小 → 库仑阻塞被抑制
- 实验上表现为**干净的干涉图案**，没有库仑阻塞的"扭曲"

### 5.4 干涉图案的 $(n, B)$ 相图

- 在 $n$–$B$ 参数空间中，干涉条纹形成规则的"棋盘"图案
- 固定 $n$ 时：$S_{xx}$ 随 $B$ 周期性振荡（AB 效应）
- 固定 $B$ 时：$S_{xx}$ 随 $n$ 周期性振荡（FP 效应 + 静电 AB 效应）
- 两种振荡的周期和相位提供互补信息

---

## 6. 在 mTBG 实验链中的位置

```
                            ┌─ 零场/低场 ─────────────────────┐
                            │                                    │
Yoo 2019 ──→ 结构：晶格重构 → AB/BA 畴 + 窄 AA 畴壁           │
Huang 2018 ──→ 电子：畴壁 LDOS 增强                            │
Rickhaus 2018 ──→ 输运：FP + AB（零场, 弹道）                  │
Xu 2019 ──→ 输运：巨幅 AB（零场, 三角网络）                    │
Verbakel 2021 ──→ 机制：FT-STM 证明谷保护                       │
                            │                                    │
                            └───────────────────────────────────┘
                                    │
                                    ▼
★ Mahapatra 2022 ★ ──→ QH 干涉：FP + AB（高场, ν=4,8 平台）
                            │
                    畴壁物理 + QH 物理的交汇！
                    天然干涉仪 → 非阿贝尔编织的潜在平台
```

**Mahapatra 2022 是唯一将畴壁网络放入量子霍尔区域来研究的实验**——它在畴壁物理（1D 拓扑通道）和 QH 物理（2D 朗道能级）之间架起了桥梁。

---

## 7. 输运性质方面的独特贡献

### 7.1 热电探针的视角

| 传统电阻测量 | 热电测量 |
|---|---|
| 对 $E_F$ 的一阶变化敏感 | 对 $E_F$ 的**导数**敏感 |
| 干涉信号可能淹没在背景中 | 干涉信号被放大 |
| QH 平台区域 $R_{xx} \to 0$ → 无信号 | $S_{xx}$ 在平台过渡处有强峰 → **有信号** |

热电使 QH 区域的干涉测量成为可能——在 $\nu = 4, 8$ 平台处 $R_{xx} \approx 0$，传统电阻测量无法看到干涉，但热电可以。

### 7.2 $\theta = 0.16^\circ$ 的意义

$\theta = 0.16^\circ$ 意味着：
- 摩尔周期 $a_M \approx 88$ nm——畴壁三角非常大
- AB/BA 畴尺寸 ~数百 nm → 干涉回路面积大 → AB 振荡周期小（$\Delta B \propto 1/A$）
- 更大的畴 → 畴壁更长 → 更易形成良好的 FP 腔

### 7.3 畴壁 + QH 边缘态的混合输运

在 QH 区域，输运不再是纯粹的畴壁态或纯粹的 QH 边缘态：

```
QH 边缘态（沿样品边界传播）
    +
畴壁通道（沿 AB/BA 畴边界传播）
    ↓
两者在三角顶点处耦合/混合
    ↓
形成复合的干涉仪网络
```

这是 Mahapatra 2022 与其他所有 mTBG 输运实验的本质区别。

---

## 8. 与用户研究的关联

| 维度 | 关联 |
|---|---|
| **TBPM QH 计算** | 可以在 TB 模型中同时模拟畴壁 + QH 边缘态（Peierls 替换 + 畴壁结构）→ TBPM 算 $\sigma_{xx}$ 和 $\sigma_{xy}$ |
| **热电模拟** | TBPM 可计算 $S_{xx} \propto \partial \ln \sigma_{xx} / \partial E$（通过能量微分） |
| **基准测试** | 在 $\nu = 4, 8$ 区域验证畴壁通道是否与 QH 边缘态共存——这是 TBPM 的理想 testbed |
| **干涉图案** | TBPM 能否重现 $(n, B)$ 参数空间中的 FP + AB 干涉条纹？这是对代码能力的严格检验 |

---

## 9. 关键参数速查

| 参数 | 值 |
|---|---|
| 扭转角 $\theta$ | ≈ 0.16°（极低） |
| 摩尔周期 $a_M$ | ≈ 88 nm |
| 测量量 | 磁热电功率 $S_{xx}$ |
| QH 平台 | $\nu = 4, 8$ |
| 干涉类型 | FP（畴壁段）+ AB（三角回路） |
| 库仑充电 | 显著减弱 |
| 样品 | hBN 封装 mTBG |
| 温度 | 低温（~K 量级，QH 区域所需） |

---

*笔记创建日期：2026-07-09 | 基于 arXiv:2112.03891v1 + Nano Lett. 22, 5708 (2022)*
