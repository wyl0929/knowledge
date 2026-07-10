<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-08 20:28:55
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-08 21:16:47
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/multilayer_graphene/subfields/domain-wall/paper_review_verbakel2021_prb.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-08
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-08
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/domain-wall/paper_review_verbakel2021_prb.md
 * @Description  : Verbakel et al. (2021) PRB 阅读笔记
-->
# 论文阅读笔记：Verbakel et al., PRB 103, 165134 (2021)

> **J.D. Verbakel, Q. Yao, K. Sotthewes, H.J.W. Zandvliet**
> "Valley-protected one-dimensional states in small-angle twisted bilayer graphene"
> Phys. Rev. B 103, 165134 (2021) | arXiv:2109.04128
>
> 机构：University of Twente（荷兰特温特大学），Physics of Interfaces and Nanomaterials 组

---

## 1. 一句话总结

通过**傅里叶变换扫描隧道显微镜（FT-STM）**在原子尺度上直接证明了：小转角 TBG 畴壁处的反传播一维态之间的电子输运**确实受到谷保护**——且该网络在**室温**下依然存在。

---

## 2. 背景：领域中的关键缺失

### 2.1 此前已知

| 已知事实 | 证据来源 |
|---|---|
| mTBG 中存在由 AB/BA 畴壁组成的三角网络 | STM 成像（Huang 2018） + STEM 结构（Yoo 2019） |
| 畴壁处态密度增强（LDOS peaks） | STM/STS 谱学（Huang 2018） |
| 畴壁通道支持弹道输运（FP + AB 振荡） | 电输运（Rickhaus 2018, Xu 2019） |

### 2.2 未解决的问题

**理论预言**畴壁态是**谷保护的**——即电子在畴壁中传播时，谷间散射（$K \leftrightarrow K'$）被强烈压制。

但在这篇论文之前，**没有任何实验直接证实了谷保护**。所有之前的输运实验（FP、AB 振荡）只证明了**弹道/相干**输运，但弹道输运 ≠ 谷保护——普通的一维弹道通道也可以有 FP 振荡，不依赖谷指标。

**Verbakel 2021 填补了这个关键空白。**

---

## 3. 实验方法：FT-STM 谷保护探测

### 3.1 核心创新：FT-STM 如何在 $\mathbf{q}$ 空间中区分谷内/谷间散射？

> **这是全文最精妙的方法论贡献，值得用五步完整展开。**

传统的 STM 测量 LDOS 随空间和能量的变化 → 只能看到态密度增强，无法判断谷指标。

**FT-STM（傅里叶变换 STM）的原理**利用了散射波矢 $\mathbf{q} = \mathbf{k}_f - \mathbf{k}_i$ 在 $\mathbf{q}$ 空间中对谷内/谷间散射的天然分离。

#### 第一步：STM 看到的是散射干涉图案

STM 测量局域态密度：

$$\text{LDOS}(\mathbf{r}, E) \propto \frac{dI}{dV}(\mathbf{r}, E) = \sum_n |\psi_n(\mathbf{r})|^2 \delta(E - E_n)$$

当有散射源（畴壁、缺陷）存在时，电子波函数是入射波和散射波的叠加：

$$\psi_{\text{total}}(\mathbf{r}) = \psi_{\text{入射}}(\mathbf{r}) + \psi_{\text{散射}}(\mathbf{r})$$

两者在实空间中**干涉** → 产生驻波图案 → LDOS 中出现空间调制。这些调制的周期携带着散射过程的信息。

#### 第二步：FT 将实空间干涉图案转化为 $\mathbf{q}$ 空间散射谱

对实空间 LDOS 做 2D 傅里叶变换：

$$\text{LDOS}(\mathbf{q}) = \int \text{LDOS}(\mathbf{r}) \, e^{-i\mathbf{q}\cdot\mathbf{r}} \, d^2\mathbf{r}$$

$\mathbf{q}$ 空间中的每一个峰对应一个活跃的散射通道：

$$\mathbf{q}_{\text{峰}} = \mathbf{k}_f - \mathbf{k}_i$$

FT 功率谱本质上是**散射通道的"普查"**——告诉你哪些 $\mathbf{k}_i \to \mathbf{k}_f$ 的散射在样品中实际发生了，以及各自的强度。

#### 第三步：石墨烯中两类散射映射到 $\mathbf{q}$ 空间的不同区域（关键！）

石墨烯的布里渊区有两个不等价谷：$K$ 和 $K'$。

```
石墨烯布里渊区示意（仅显示 K 和 K' 附近）：

        K'                    K
        ★                     ★
         \                   /
          \                 /
           \               /
            \             /
             \           /
              \         /
               \       /
                \     /
                 \   /
                  \ /
                   ★  Γ (q=0)
```

**谷内散射**（$K \to K$ 或 $K' \to K'$）：
- 初态和末态在**同一个谷**附近
- 散射波矢 $\mathbf{q} = \mathbf{k}_f - \mathbf{k}_i$ 是小矢量（$\mathbf{q} \approx 0$ 附近）或中等矢量（晶格 Bragg 峰附近）
- 例如：forward scattering（$\mathbf{q} \approx 0$），backscattering within a valley（$\mathbf{q} \sim |K|$ 量级）

**谷间散射**（$K \leftrightarrow K'$）：
- 初态在 $K$，末态在 $K'$（或反之）
- 散射波矢 $\mathbf{q} \approx K - K'$——这是一个**大且特定**的矢量
- 在 $\mathbf{q}$ 空间中定位于远离 $\Gamma$ 点的特定位置

**核心洞察**：这两类散射在 $\mathbf{q}$ 空间中**天然分离、互不重叠**。FT-STM 可以通过检查特定 $\mathbf{q}$ 区域的信号强度，来分别量化谷内和谷间散射。

#### 第四步：谷保护在 FT-STM 中的"信号"

如果畴壁态是**谷保护的**（电子传播时保持谷指标不变）：

| 散射类型 | 理论预期 | FT-STM 中应看到的 |
|---|---|---|
| 谷内散射 | ✅ 允许 | **强峰**——电子可以在同一谷内自由散射 |
| 谷间散射 | ❌ 被拓扑保护压制 | **峰极弱或消失**——电子不能翻转到另一个谷 |

定量判据：

$$\frac{I_{\text{FT}}(\mathbf{q}_{\text{谷内}})}{I_{\text{FT}}(\mathbf{q}_{\text{谷间}})} \gg 1 \quad \Longrightarrow \quad \text{谷保护成立}$$

如果谷保护不成立（即畴壁态是普通的无拓扑保护的一维态），两类散射的强度应该是可比的。

#### 第五步：FT-STM 比输运测量的独特优势

| | 电输运（FP/AB 振荡） | FT-STM |
|---|---|---|
| 测量对象 | 总电导/电阻——所有散射通道的**积分** | 散射通道的**$\mathbf{q}$ 分辨**谱 |
| 能否区分谷内/谷间？ | ❌ 不能——总电导不区分谷指标 | ✅ **能**——$\mathbf{q}$ 空间天然分离两类散射 |
| 弹道输运 = 谷保护？ | 弹道输运只说明散射少，不说明谷指标守恒 | FT-STM 直接告诉你是**哪种**散射少了 |

这就是为什么 Verbakel 2021 的 4 页 PRB 短文能填补关键空白——弹道输运可以通过多种机制实现（弱无序、短通道……），但**谷保护只能通过 FT-STM 这种动量分辨的散射探针来直接证实**。

### 3.2 实验配置

| 参数 | 细节 |
|---|---|
| 技术 | 超高真空 STM（UHV-STM），室温 |
| 样品 | 小转角 TBG（$\theta < 1^\circ$），在 SiC 上外延生长（非 hBN 封装） |
| 测量量 | 恒流模式形貌图 + $dI/dV$ 谱 + $dI/dV$ mapping |
| 关键分析 | 2D FFT of $dI/dV$ maps → $\mathbf{q}$ 空间散射矢量强度 |
| 对比实验 | 同一器件在不同偏压（不同能量）下重复 FT-STM 测量 |

---

## 4. 核心发现

### 4.1 室温下的畴壁网络

**这是本文最引人注目的发现之一：**

- 在**室温（~300 K）**下，STM 形貌图和 $dI/dV$ 图中仍清晰可见 AB/BA 三角畴壁网络
- 畴壁处的 LDOS 增强在室温下依然存在 → 畴壁态的能隙或束缚能至少大于 $k_B T \approx 26$ meV
- 这表明畴壁态的拓扑保护在室温下仍然有效——对于实际应用（室温 valleytronics）意义重大

### 4.2 FT-STM 证明谷保护

**核心实验证据：**

1. **实空间 $dI/dV$ mapping**：清晰显示三角畴壁网络，畴壁处 LDOS 增强
2. **2D FFT 功率谱**：
   - 在**谷内散射**特征 $\mathbf{q}$ 处：**强信号**
   - 在**谷间散射**特征 $\mathbf{q}$ 处：**信号显著弱于谷内散射**（甚至接近背景噪声）
3. **能量依赖性**：在不同偏压（不同能量窗口）下重复 FT-STM，谷间散射始终被压制 → 谷保护不依赖于特定能量

**定量对比**：
- 谷内散射强度 / 谷间散射强度 ≫ 1（具体比值取决于能量和设备，但定性上非常显著）
- 这与理论预言的"谷间散射被拓扑压制"一致

### 4.3 与理论的一致性

- 畴壁态的谷 Chern 数差异 → 反传播通道来自不同谷 → 谷间散射需要破坏拓扑保护 → 被指数级压制
- FT-STM 的结果与 Efimkin & MacDonald (2018) 的螺旋网络模型和 San-Jose & Prada (2013) 的早期理论预言定性一致

---

## 5. 在 mTBG 实验链中的独特位置

```
Huang 2018 (STM)
  └→ 观测到畴壁处 LDOS 增强
      └→ 但无法判断谷保护

Yoo 2019 (STEM + 输运)
  └→ 晶格重构 → 畴壁的结构起源
      └→ D 场调控下观测到畴壁导电
          └→ 但无法判断谷保护

Rickhaus 2018 / Xu 2019 (输运)
  └→ FP + AB 振荡 → 弹道/相干输运
      └→ 但弹道输运 ≠ 谷保护

★ Verbakel 2021 (FT-STM) ★
  └→ 首次直接证明：畴壁态传输是谷保护的！
      └→ 且室温下仍有效
```

**Verbakel 2021 是所有后续理论的实验锚点**——Hou 2024 等理论工作的谷极化输运预言，其可信度建立在 Verbakel 2021 的谷保护实验证据之上。

---

## 6. 输运性质方面的贡献

### 6.1 间接输运信息

虽然 FT-STM 不是直接的电输运测量，但它提供了输运的**微观机制证据**：

| STM 观测 | 输运推论 |
|---|---|
| 畴壁处 LDOS 增强（室温） | 畴壁态在室温下存活 → 输运通道的热稳定性高 |
| 谷间散射被压制 | 电子在畴壁中传播时保持谷指标 → **谷极化电流** |
| 反传播通道来自不同谷 | 谷过滤效应——正方向走 $K$ 谷，反方向走 $K'$ 谷 |
| 散射矢量 $\mathbf{q}$ 的分布 | 背散射（$+k \to -k$）需要谷翻转 → 被压制 → **弹道输运** |

### 6.2 对输运实验的约束

Verbakel 2021 的谷保护证据对后续输运实验有重要影响：
- 验证了畴壁态不仅仅是"一维的"，而且是"谷选择性的"——这构成了 valleytronics 的基础
- 解释了为什么 Rickhaus 2018 看到 0–8T 磁场稳健性——谷保护 + 时间反演对称性保护的联合效应
- 为 Hou 2024 的 TZM 模型提供了微观支撑——独立传播的 TZM 要求谷间散射可忽略

### 6.3 室温 valleytronics 前景

- 畴壁网络在室温下稳定存在 → 不需要低温即可利用谷自由度
- 结合 D 场调控（Yoo 2019），原则上可以实现室温下的谷过滤器和谷阀门
- 在 SiC 上外延生长（本文方法）比 hBN 封装更适合规模化

---

## 7. 与其他 STM 实验的对比

| 维度 | Huang 2018 (PRL) | Verbakel 2021 (PRB) |
|---|---|---|
| 温度 | 低温（~4 K） | **室温（~300 K）** |
| 样品 | hBN 封装，撕裂-堆叠 | SiC 外延生长 |
| 主要发现 | 畴壁处 THS 的 LDOS 增强 | **FT-STM 证明谷保护** |
| 分析方法 | 实空间 LDOS + 谱学 | 实空间 LDOS + **$\mathbf{q}$ 空间 FFT 分析** |
| 谷保护 | 未涉及 | **核心贡献** |
| 技术门槛 | 需要稀释制冷机 | 室温 STM（更低门槛） |

---

## 8. 方法局限

| 局限 | 说明 |
|---|---|
| SiC 外延 vs hBN 封装 | SiC 上的 TBG 与 hBN 封装的 TBG 在无序度和应变分布上可能不同——结果能否直接推广到 hBN 封装器件？ |
| 无直接输运测量 | FT-STM 提供的是散射信息（间接输运），而非 $I$–$V$ 或 $G$ 的直接测量 |
| 室温下能量分辨率有限 | 室温 STM 的热展宽 ~$4k_BT \approx 100$ meV → 精细的能谱特征被抹平 |
| 未扫描 $D$ 场 | SiC 外延器件可能没有双栅结构 → 无法像 Yoo 2019 那样连续调控畴壁 |
| 无磁场依赖 | 未测量磁场下的谷保护行为 → 无法判断磁场如何影响谷间散射 |

---

## 9. 关键参数速查

| 参数 | 值 |
|---|---|
| 测量温度 | **室温（~300 K）** |
| 样品体系 | 小转角 TBG（$\theta < 1^\circ$）on SiC |
| 实验技术 | UHV-STM + $dI/dV$ mapping + 2D FFT |
| 论文篇幅 | 4 页 + 3 张图（短报告） |
| 核心方法 | FT-STM：实空间 LDOS → $\mathbf{q}$ 空间功率谱 → 区分谷内/谷间散射 |
| 畴壁网络 | 三角 AB/BA 畴壁，与 Yoo 2019 的 STEM 观测一致 |
| 谷保护证据 | 谷间散射强度 ≪ 谷内散射强度 |

---

## 10. 与用户研究的关联

| 维度 | 关联 |
|---|---|
| **TBPM 验证** | FT-STM 的 $\mathbf{q}$ 空间功率谱可以通过 TBPM 计算 LDOS 的 FFT 来复现——这是一个直接可做的 benchmark |
| **谷极化输运** | TBPM + Kubo-Bastin 可以区分谷内和谷间电导贡献 → 验证畴壁通道的谷极化度 |
| **室温效应** | TBPM 可以引入有限温度展宽 → 模拟畴壁态在室温下的 LDOS 是否仍可分辨 |
| **SiC 衬底** | TB 模型中能否加入衬底效应（如 SiC 的掺杂和应变）来模拟外延生长的 TBG？→ 可能的扩展方向 |

---

*笔记创建日期：2026-07-08 | 基于 arXiv:2109.04128v1 + Phys. Rev. B 103, 165134 (2021)*
