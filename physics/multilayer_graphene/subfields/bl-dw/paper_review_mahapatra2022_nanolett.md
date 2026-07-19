<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-09 21:35:07
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-15 16:36:48
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
>
> Nano Lett. 22, 5708 (2022) | arXiv:2112.03891
> **DOI**: [10.1021/acs.nanolett.2c00627](https://doi.org/10.1021/acs.nanolett.2c00627) | **Zotero Key**: `cmd.exe /c start "zotero://select/items/SD7UCT4M"`
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

---

## 附录 A：Aharonov-Bohm (AB) 振荡

> 追加日期：2026-07-15

### A.1 一句话定义

Aharonov-Bohm（AB）振荡是带电粒子在**无磁场区域**（$B = 0$）中沿闭合回路运动时，因包围磁通量 $\Phi$ 而产生的量子干涉效应。其本质是：**电磁矢势 $\mathbf{A}$ 具有物理实在性，而不只是数学工具**——这是经典电磁学无法解释的纯量子效应。

### A.2 历史起源

1959 年，Yakir Aharonov 和 David Bohm 发表了一篇划时代的理论论文（Phys. Rev. 115, 485），提出一个思想实验：

> 让一束电子分成两路，绕过一个无限长螺线管的两侧后重新汇合。螺线管内部有磁场 $B \neq 0$，但外部空间 $B = 0$（矢势 $\mathbf{A} \neq 0$）。

经典物理的预测：电子只感受 Lorentz 力 $\mathbf{F} = -e\mathbf{v} \times \mathbf{B}$，螺线管外 $B = 0$，所以电子不受任何力，不会出现干涉。

量子力学的预测：电子的波函数相位由**矢势** $\mathbf{A}$ 决定，即使 $B = 0$，只要 $\mathbf{A} \neq 0$，两路径就会积累相位差 → **干涉条纹**。

1960 年 Chambers 首次实验验证，此后成为量子力学非定域性的标志性证据。

### A.3 核心物理

#### 相位积累

在磁场中，带电粒子的波函数沿路径 $C$ 获得一个额外的量子相位：

$$\Delta\varphi = \frac{e}{\hbar} \int_C \mathbf{A} \cdot d\mathbf{l}$$

对于闭合回路，利用 Stokes 定理：

$$\Delta\varphi = \frac{e}{\hbar} \oint_C \mathbf{A} \cdot d\mathbf{l} = \frac{e}{\hbar} \iint_S \mathbf{B} \cdot d\mathbf{S} = \frac{e}{\hbar} \Phi = 2\pi \frac{\Phi}{\Phi_0}$$

其中：
- $\Phi = \iint_S \mathbf{B} \cdot d\mathbf{S}$ 是回路包围的磁通量
- $\Phi_0 = h/e$ 是**磁通量子**（单电子 AB 效应的通量周期）
- 注意：超导中的磁通量子是 $h/2e$（Cooper 对），与单电子 AB 效应不同

#### 干涉条件

电子波分两路绕闭合回路：

$$\psi_{\text{total}} = \psi_1 + \psi_2 \cdot e^{i\Delta\varphi}$$

当 $\Delta\varphi = 2\pi n$（$n$ 为整数）时，相长干涉 → 电导极大；
当 $\Delta\varphi = (2n+1)\pi$ 时，相消干涉 → 电导极小。

因此，电导（或电阻）随 $B$ 呈现**周期性振荡**：

$$\Delta B = \frac{\Phi_0}{A}$$

其中 $A$ 是回路在垂直于 $B$ 方向的投影面积。

### A.4 AB 效应揭示的物质基本性质

AB 效应不是一个孤立的量子现象——它触及了量子力学和规范场论的深层结构：

#### ① 矢势 $\mathbf{A}$ 的物理实在性

| | 经典电磁学 | 量子力学（AB 效应） |
|---|---|---|
| 基本量 | $\mathbf{E}, \mathbf{B}$（场） | $\mathbf{A}, \phi$（势） |
| $\mathbf{A}$ 的地位 | 数学辅助量，无物理意义 | **可观测的物理量**（通过相位） |
| 粒子在 $B=0$ 区域 | 不受电磁影响 | 仍受 $\mathbf{A}$ 影响 |

这是量子力学对经典世界观的根本修正：**势比场更基本**。这一认识后来成为规范场论（Yang-Mills 理论）的出发点——所有基本相互作用都是"势"（规范联络）的理论，而非"场"的理论。

#### ② 量子力学的非定域性

电子在**从未进入**磁场区域的情况下，其波函数相位仍被磁场改变。这意味着：
- 量子粒子的行为不仅由局域场决定，还由空间的全局几何结构决定
- 这是与 EPR 纠缠不同的另一种量子非定域性——**拓扑非定域性**

#### ③ 几何相位（Berry 相位）的前身

AB 相位是 Berry 相位（1984）的最早实例。Berry 相位的一般公式：

$$\gamma_n = i \oint_C \langle n(\mathbf{R}) | \nabla_{\mathbf{R}} | n(\mathbf{R}) \rangle \cdot d\mathbf{R}$$

AB 相位对应 $\mathbf{R} = \mathbf{A}$ 参数空间中的 Berry 相位。在石墨烯中，Dirac 点附近的电子携带 $\pi$ 的 Berry 相位，这是理解石墨烯 QH 效应中"半整数"量子化的关键（$\sigma_{xy} = \pm 2, \pm 6, \pm 10, \ldots$ 的序列，而非传统 2DEG 的 $\pm 1, \pm 3, \pm 5, \ldots$）。

#### ④ 拓扑保护

AB 相位 $\Delta\varphi \propto \oint \mathbf{A} \cdot d\mathbf{l}$ 是一个**拓扑不变量**——它只依赖于回路包围的总通量，不依赖于回路的具体形状或路径细节。这意味着：
- AB 振荡对无序和杂质有某种程度的**鲁棒性**
- 只要相位相干长度 $L_\phi$ 超过回路周长，干涉就存在
- 这使得 AB 干涉仪成为探测拓扑量子态的理想工具

### A.5 AB 振荡 vs Fabry-Pérot 振荡

Mahapatra 2022 中同时观测到了两种振荡，它们的区分是理解实验的关键：

| 维度 | AB 振荡 | FP 振荡 |
|---|---|---|
| **物理来源** | 矢势 $\mathbf{A}$ 导致的 Aharonov-Bohm 相位 | 电子在腔两端反射形成的驻波 |
| **相位条件** | $\Delta\varphi_{\text{AB}} = 2\pi\Phi/\Phi_0$ | $\Delta\varphi_{\text{FP}} = 2kL$（$L$ 为腔长） |
| **磁场依赖** | 周期 $\Delta B = \Phi_0/A$（固定 $n$） | 通过 $k \propto \sqrt{n}$ 同时依赖 $B$ 和 $n$ |
| **载流子密度依赖** | 弱（仅通过面积 $A$ 的微弱静电调制） | **强**（直接改变 $k_F$ → 振荡相位） |
| **对面积敏感** | 面积 $A$ 直接决定周期 | 腔长 $L$ 决定周期，面积不直接出现 |
| **石墨烯特殊之处** | Berry 相位 $\pi$ 改变干涉条件 | 谷自由度可提供额外的相位自由度 |

在 Mahapatra 2022 中：
- 固定 $n$ 扫 $B$ → **AB 振荡**（周期 $\Delta B \propto 1/A_{\text{triangle}}$）
- 固定 $B$ 扫 $n$ → 同时包含 **FP 振荡**（$2kL = 2\pi m$）和**静电 AB 效应**（$n$ 变化 → 面积静电微调 → AB 相位偏移）
- 不同三角畴大小不同 → 多个 AB 周期叠加 → **FFT 频谱**可分离各畴贡献

### A.6 石墨烯中的特殊考量

石墨烯中的 AB 效应与传统 2DEG（如 GaAs）有几个关键区别：

1. **Berry 相位 $\pi$**：Dirac 费米子的手性使 AB 干涉条件偏移 $\pi$——干涉极大/极小位置与 Schrodinger 费米子相反
2. **谷自由度**：$K$ 和 $K'$ 谷的电子在磁场下获得相反的 AB 相位符号 → 谷间散射会破坏干涉 → 这是畴壁中谷极化保护对 AB 干涉至关重要的原因
3. **Dirac 谱**：零质量 Dirac 谱使 Landau 能级按 $\pm v_F\sqrt{2e\hbar B|N|}$ 排列（而非 $\hbar\omega_c(N+1/2)$），QH 平台序列变为 $\nu = \pm 2, \pm 6, \pm 10, \ldots$
4. **相干长度**：石墨烯中 $L_\phi$ 可达数微米（hBN 封装下），使 ~100 nm 尺度的三角畴 AB 干涉成为可能

### A.7 AB 振荡的变体：AAS 振荡

在**扩散输运**区域（$L_\phi < L$），与 AB 效应相关但不相同的是 **Altshuler-Aronov-Spivak（AAS）振荡**：

| | AB 振荡 | AAS 振荡 |
|---|---|---|
| 周期 | $h/e$ | $h/2e$ |
| 来源 | 单电子绕回路一周的相位 | 时间反演路径对（电子顺时针+逆时针）的干涉 |
| 输运区域 | 弹道或准弹道 | **扩散**（多次散射） |
| 温度依赖 | 幂律衰减 | 指数衰减（更敏感） |
| 应用 | 弹道干涉仪、拓扑态探测 | 弱（反）局域化修正的傅里叶分量 |

在 Mahapatra 2022 中，畴壁输运处于准弹道区域（畴壁段 ~100 nm，$L_\phi$ 足够长），所以观测到的是 **$h/e$ 周期的 AB 振荡**而非 $h/2e$ 的 AAS 振荡——这本身就证明了畴壁中的弹道输运质量。

### A.8 为什么 AB 效应在 QH 干涉测量中重要

回到 Mahapatra 2022 的核心故事：QH 干涉仪用于探测非阿贝尔任意子的编织统计。AB 效应在这里扮演的角色是：

1. **基本干涉机制**：QH 边缘态绕闭合回路的 AB 相位是干涉信号的物理来源
2. **编织相位的载体**：当 FQH 准粒子被局域在干涉仪内部时，边缘态绕行获得的不仅是 AB 相位 $\Phi/\Phi_0$，还有编织统计相位 $\theta_{\text{braid}}$——干涉图案的**偏移**直接编码了编织统计
3. **电荷的指纹**：AB 振荡周期 $\Delta B \propto 1/e^*$（有效电荷），改变周期 = 探测准粒子分数电荷

这解释了为什么 Mahapatra 等人要在 mTBG 中寻找干净的 AB 干涉信号——它是通往非阿贝尔编织统计测量的**实验前提**。

---

### A.9 参考文献（AB 效应）

- **Aharonov & Bohm, Phys. Rev. 115, 485 (1959)** — 原始理论论文
- **Chambers, Phys. Rev. Lett. 5, 3 (1960)** — 首次实验验证
- **Webb et al., Phys. Rev. Lett. 54, 2696 (1985)** — 金属环中 $h/e$ AB 振荡的经典实验
- **Berry, Proc. R. Soc. Lond. A 392, 45 (1984)** — Berry 相位的统一理论框架
- **Altshuler, Aronov & Spivak, JETP Lett. 33, 94 (1981)** — AAS 振荡理论
- **Beenakker & van Houten, Solid State Phys. 44, 1 (1991)** — 固态 AB 效应的权威综述
