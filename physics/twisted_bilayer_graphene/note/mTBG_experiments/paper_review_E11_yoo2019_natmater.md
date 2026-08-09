<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 22:02:15
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 22:02:19
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/mTBG_experiments/paper_review_E11_yoo2019_natmater.md
 * @Description  :
-->
<!--
 * @Author       : AI 精读 (research_onboarding_skill)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/note/mTBG_experiments/paper_review_E11_yoo2019_natmater.md
 * @Description  : E11: Yoo et al. 2019 — TBG 原子/电子重构的结构基础
-->

# Paper Review: Yoo et al. (2019) — TBG 原子与电子重构

| 字段 | 内容 |
|------|------|
| **编号** | E11 |
| **标题** | Atomic and electronic reconstruction at the van der Waals interface in twisted bilayer graphene |
| **作者** | Hyobin Yoo, Rebecca Engelke, Stephen Carr, Shiang Fang, Kuan Zhang, Paul Cazeaux, Suk Hyun Sung, Robert Hovden, Adam W. Tsen, Takashi Taniguchi, Kenji Watanabe, Gyu-Chul Yi, Miyoung Kim, Mitchell Luskin, Ellad B. Tadmor, Efthimios Kaxiras, Philip Kim |
| **期刊** | Nature Materials 18, 448–453 (2019) |
| **DOI** | 10.1038/s41563-019-0346-z |
| **arXiv** | 1804.03806 |
| **类型** | 实验 + 理论 — TEM/SAED + 输运 + 第一性原理 |
| **课题组** | Kim group (Harvard) |
| **PDF** | ✅ reference/pdfs/Yoo 等 - 2019 - ...pdf |
| **DW.bib** | ✅ `yoo_atomic_2019` |
| **精读日期** | 2026-08-06 (初稿), 2026-08-08 (更新 §5b/5c: Hofstadter 2D→1D 输运跨越 + DOS/band 计算方法) |

---

## 1. 核心贡献

这是整个 mTBG 畴壁领域的**结构地基论文**。核心发现：

1. 存在从"刚性莫尔结构"到"重构溶畴（solitonic）结构"的跨越，**特征角 θ_c ≈ 1°**
2. θ > θ_c：接近刚性扭转的莫尔图景
3. θ < θ_c：系统重构为近 Bernal（AB/BA）三角域 + 锐利域壁（soliton boundaries）网络
4. 结构重构直接引发电学重构：莫尔能带简单描述失效 → 次级 Dirac 带出现 → E 场下 1D 拓扑通道形成

## 2. 物理机制

### 2.1 两种能量竞争

- **层间 vdW 相互作用**：偏好局域共格堆垛（AB/BA），倾向于扩大低能域
- **层内弹性能**：抵抗过大晶格形变

### 2.2 原子重构

- 不是两层刚性旋转简单叠加
- 局部原子位置/局部转角被"再分配"：扩大低能 AB/BA 区域、压缩高能 AA 区域
- AA 区域被压缩成节点，AB/BA 域壁成为窄 soliton 边界

### 2.3 Soliton 边界特征

- AB 与 BA 近共格三角域之间的窄边界
- θ < θ_c：边界宽度近似守恒（solitonic 特征）
- θ > θ_c：域间过渡更平滑，AB/BA 纯度降低
- 跨越发生在莫尔长度与域壁宽度可比时 ≈ θ_c 判据

## 3. 实验方法

### 3.1 TEM 暗场成像

- 选取特定 Bragg 峰（如 g = 10̄10）做实空间堆垛映射
- 直接看到 AB/BA 交替三角域与镜像域壁

### 3.2 SAED（选区电子衍射）

- 关键指标：$I_{sat}/I_{Bra}$（satellite 峰与 Bragg 峰强度比）
- 量化重构周期与强度

### 3.3 电输运

- 双栅器件，扫描 n、D、B
- 温度依赖 + Hall 符号翻转识别能带重构

### 3.4 多尺度计算

- FEM 连续-原子耦合结构弛豫 + 基于 ab initio 参数的紧束缚/连续模型

## 4. 关键数据

### 4.1 结构参数

| 参数 | 值 |
|------|-----|
| 扭角范围 | 0° < θ < 4° |
| 样品均匀性 | >10³ moiré 胞元，域尺度波动 <10%，域尺寸可达 ~200 nm |
| θ_c（跨越角） | ≈ 1° |
| Isat/IBra 衰减系数 α | ≈ 2.75 ± 0.3 deg⁻¹ |
| θ > 4° 时 satellite 峰 | 低于检测极限（重构可忽略）|

### 4.2 暗场图像证据

| θ | 特征 |
|---|------|
| 0.1° | 清晰 AB/BA 交替三角域网络（强重构）|
| 0.4°, 0.8°, 1.2° | 三角域对比逐步减弱，向条纹化莫尔过渡 |

### 4.3 电子结构（θ ~ 1.1°）

| 参数 | 值 |
|------|-----|
| 单粒子隙（电子侧）| ~32 meV |
| 单粒子隙（空穴侧）| ~26 meV |
| 激活能（电子，n/n₀=±4）| ~27 meV |
| 激活能（空穴，n/n₀=±4）| ~18 meV |
| 关联绝缘态激活能（±2）| 0.30 / 0.22 meV |

### 4.4 次级 Dirac 特征（θ ~ 0.47°–0.5°）

- G(n) 在 $n/n_0 = 0, \pm4, \pm8$ 出现极小值但不完全开隙
- 低场 Hall 符号翻转 → 支持 secondary Dirac band

### 4.5 Solitonic 区域拓扑输运（θ = 0.47° < θ_c）

- 加 E 场 → AB/BA 域开隙 → 电流转移到域壁 1D 通道网络
- $D/\varepsilon_0 \approx -0.7, 0, +0.7$ V/nm 下比较 Landau 图
- B = 5.4 T 出现横向特征对应 Φ/Φ₀ = 1 → θ ≈ 0.47°
- |D|↑ → Hofstadter 特征减弱 → 从 2D 体输运向 1D 网络输运转变

## 5. 主要结论

1. **θ_c ≈ 1°** 是原子/电子重构跨越角：上方偏莫尔、下方偏溶畴网络
2. θ < θ_c 时刚性莫尔能带描述失效，必须纳入结构弛豫
3. 低角区（~0.5°）出现稳定 secondary Dirac 光谱特征
4. 位移场可开隙 AB/BA 域，激活域壁 1D 拓扑通道网络输运
5. TBG 核心自由度 = 几何扭角 + 可调重构强度

---

## 5b. Figure 3e/3f 与最后一段详解 — Hofstadter 谱与 2D→1D 输运跨越

### 5b.1 实验设置

- 样品：小角 TBG，**θ = 0.47°**（< θ_c，solitonic 区间）
- 双栅器件，温度 **1.7 K**
- 三个位移场条件：$D/\varepsilon_0 \approx$ **−0.7, 0, +0.7 V/nm**
- 磁场 B 垂直平面，测量 $R_{xx}(B, n)$

### 5b.2 Figure 3e: D 依赖的 Hofstadter 扇图

**观察到的现象：**

1. 在所有三个 D 条件下，均出现发育良好的 **Landau fan**：
   - 从 CNP（主 Dirac 峰）发出的主 Landau 能级序列
   - 从 **side peaks**（$n/n_0 = \pm 4$）发出的额外 Landau fan → 表明 moiré 超晶格 Hofstadter 分形谱的形成

2. 多重 QH 特征从两套 side peaks 扇出，当每超胞磁通 $\phi$ 为磁通量子 $\phi_0 = h/e$ 的整数倍时出现周期性 QH 特征

3. **最显著特征**：在 $B = \mathbf{5.4\ T}$ 处（黑色箭头标注），所有三个 D 条件下均出现**水平特征**（即不随 n 变化、只由 B 决定的电阻特征）
   - 该场对应 $\phi/\phi_0 = 1$ → 每 moiré 超胞恰好穿过一个磁通量子
   - 由 $\phi = BA = 5.4\ \text{T} \times \frac{\sqrt{3}}{2}\lambda^2$ 可得 $\lambda \approx 29.7$ nm → **θ ≈ 0.47°**
   - 从 side peak 位置（B=0 时 $n \approx \pm 5.2 \times 10^{11}\ \text{cm}^{-2} = 4$ 电子/超胞）估算的 θ 与此一致（SI §6 详述）

| 特征 B 场 | $\phi/\phi_0$ | 含义 |
|:---:|:---:|------|
| 5.4 T | 1 | 每超胞 1 磁通量子 |
| 10.8 T | 2 | 每超胞 2 磁通量子 |

### 5b.3 Figure 3f: 固定 B 场下 D 依赖的 R_xx 线扫

**观察到的现象：**

- **左图**：$B = 10$ T 下三种 D 条件的 $R_{xx}(n)$
- **右图**：$B = 4$ T 下三种 D 条件的 $R_{xx}(n)$
- **核心观察**：$|D|$ 增大时，Hofstadter 特征（QH 振荡幅度、Landau gap 的锐利程度）**显著减弱**

### 5b.4 结论：2D→1D 输运跨越（最后一段的核心论证）

论文最后一段（正文倒数第 2–3 段 + 最后一段）的逻辑链：

**① 观察到 1D 网络的形成证据（Figure 3d + 前文）**

- $R(D)/R_0$ 在 $|D|$ 增大时上升并**饱和**（Fig. 3d 插图）
- 饱和值与 $R_q = h/4e^2 \approx 6.4$ kΩ 同数量级 → AB/BA 域被开隙后电流以**非相干混合**方式在 1D 通道网络中流动
- 四个额外样品（SI S1–S4, θ = 0.37°–0.41°）均显示类似行为，饱和电阻值 1.6–13 kΩ 不等（SI Fig. S10i）

**② Hofstadter 特征随 |D| 增大而减弱（Figure 3e, 3f）**

- QH 特征在高位移场下变弱 → **Landau gap 在 Hofstadter 分形能谱中减小**
- 这表明载流子不再以 2D 体态方式参与 QH 效应

**③ 归因：2D→1D 网络输运转变**

> "We thus attribute this change in the fan diagram to the **transition of electronic transport from the 2D to 1D network mode** with increasing |D|, confining the carriers to the topologically protected boundaries of gapped AB/BA domains in structurally reconstructed TBG."

- |D| 小 → AB/BA 域未充分开隙 → 电子在 2D 平面内运动 → 完整 Hofstadter 分形谱
- |D| 大 → AB/BA 域充分开隙（绝缘化）→ 电子被迫沿畴壁 1D 拓扑通道运动 → Hofstadter 特征减弱（因为 1D 通道不支持同样的 2D Landau 量子化）

**④ 全文总结句（最后一句）**

> "Together with our experimental finding of the crossover between the soliton and moiré regime, the appearance of these topological modes can be further utilized in **engineering vdW epitaxy of 2D materials**."

### 5b.5 跨实验的一致性验证

| 证据 | 来源 |
|------|------|
| θ 从 Hofstadter 谱 ($\phi/\phi_0=1$ 处 B=5.4T) 估算 | Fig. 3e |
| θ 从 side peak 位置 (B=0, n≈±5.2×10¹¹ cm⁻²) 估算 | Fig. S9c |
| θ 两方法一致 → **同一样品均匀畴结构** | SI §6 |
| Hall 符号在 $n/n_0=0,\pm4,\pm8$ 处翻转 → Dirac 锥形成 | Fig. S9d |
| 4 个额外器件均显示 $R(D)$ 饱和行为 | Fig. S10i |

---

## 5c. DOS 和能带计算方法详解

Yoo 2019 中的电子结构计算采用的是**多方法混合策略**——不同层次的计算分工明确，最终由重构的原子坐标驱动电子结构。

### 5c.1 计算流程图

```
FEM 结构弛豫（得到重构后原子坐标）
        │
        ├──→ 紧束缚模型（supercell TB）→ 能带结构 E(k)
        │         │
        │         └── 输入：ab initio TB 参数 (Fang & Kaxiras 2016)
        │
        └──→ ab initio 连续模型 → DOS
                  │
                  ├── FEM (Lehmann-Taut 方法) 在 60×60 k 点网格上
                  ├── 输入：动量依赖的应变场 + 层间耦合项
                  └── 对重构晶格的描述需足够大的 k 范围
```

### 5c.2 各方法详细说明

#### A. 结构弛豫：FEM（有限元法）

| 项目 | 内容 |
|------|------|
| 方法 | 连续-原子混合 FEM（Zhang & Tadmor 2018, Ref. 16）|
| 层内力学 | 非线性弹性模型：Saint Venant–Kirchhoff 膜项 + Helfrich 弯曲项 |
| 层间相互作用 | **Kolmogorov-Crespi (KC)** registry-dependent 势（Ref. 40）|
| 优化算法 | L-BFGS 能量最小化 |
| 输出 | 弛豫后的原子坐标 + 局域应变场 |

> 详见 SI §4 和 Ref. 16 (Zhang & Tadmor, JMPS 2018)

#### B. 能带结构：紧束缚（Tight-Binding）

| 项目 | 内容 |
|------|------|
| 方法 | 标准超胞紧束缚哈密顿量 |
| 参数来源 | **Fang & Kaxiras (2016)** 的 ab initio 紧束缚参数（Ref. 41）|
| 参数特点 | 从 DFT 计算中提取，适合弱相互作用双层体系 |
| 适用体系 | 重构/未重构的 TBG，不同扭角 |

> "The electronic structure of TBG was modelled using **previously obtained ab initio tight-binding parameters**." (Methods, Ref. 41, 42)

- Ref. 41: Fang & Kaxiras, PRB 93, 235153 (2016) — 弱相互作用双层的电子结构理论
- Ref. 42: Carr, Fang et al., PRB 98, 085144 (2018) — magic angle 的压力依赖性

#### C. DOS：ab initio 连续模型

| 项目 | 内容 |
|------|------|
| 方法 | ab initio 连续模型（continuum model）|
| k 点网格 | **60 × 60** |
| 积分方法 | **FEM（Lehmann-Taut 方法）**（Ref. 44）— 四面体数值积分 |
| 关键输入 | **动量依赖的应变场** + 层间耦合项（从 FEM 重构结构提取）|
| 应变场处理 | 在足够大的 k 范围内定义，以捕获重构晶格的细节 |

> "The DOS used an **ab initio continuum model**. An **FEM** was used on a **60 × 60 k-point grid** to generate the DOS profiles." (Methods)

> "The **momentum-dependent strain field** and **interlayer coupling terms** were defined in a large enough range of k to capture the details of the reconstructed lattice. This strain field correction becomes **more significant as one approaches the solitonic regime (θ < θ_c)** where the reconstructed lattice cannot be captured with only a few Fourier components." (Methods)

这意味着对于 θ < θ_c（solitonic 区间），简单的 Bistritzer-MacDonald 连续模型（只用少数几个傅里叶分量）不再足够——必须纳入应变场修正。

### 5c.3 重构在计算中的角色

| 体系 | 处理方法 | 特点 |
|------|---------|------|
| **未重构** TBG | 刚性扭转晶格 → 标准紧束缚/连续模型 | 简单 moiré 描述 |
| **重构** TBG（θ ~ 1.1°）| FEM 弛豫后 → 紧束缚能带 + 连续模型 DOS | 修正单粒子隙和带宽，但 magic-angle 基本物理不变 |
| **重构** TBG（θ < θ_c）| FEM 弛豫 → **需在足够大 k 范围纳入动量依赖应变场** | 少量傅里叶分量**不能**捕获重构晶格 → 必须用完整应变场修正 |

### 5c.4 未重构 vs 重构的结果差异

#### θ ~ 1.1°（第一 magic angle）— Fig. 2a, 2b

| 方面 | 未重构 | 重构 |
|------|--------|------|
| 单粒子隙 | 无或很小 (~0) | 电子侧 32 meV, 空穴侧 26 meV |
| 带宽 | 较窄 | 修正 |
| DOS 峰值 | 尖锐 | 略压低 |
| **物理本质** | 不变 — magic-angle 关联物理**定性保持** | |

> "Reconstruction changes the details of the band structure such as single-particle gap size, bandwidth and overall DOS. However, the **essential physics of the correlated behaviour stays the same**." (Fig. 2 caption)

#### θ ~ 0.5°（第二 magic angle）— Fig. 2c, 2d

| 方面 | 未重构 | 重构 |
|------|--------|------|
| DOS 特征 | 许多尖锐但不稳定的峰（对 θ 微小变化极敏感）| **稳定**的 Dirac 锥特征在 $n/n_0 = 0, \pm 4, \pm 8$ |
| 能带结构 | 杂乱的多带交叉 | 清晰的 secondary Dirac 谱 |
| 实验可重复性 | 不可能（任何小 θ 变化都会改变 DOS）| **可重复**（对 θ 微小变化鲁棒）|
| 关联态 | — | DOS 峰值比 1.1° 压低一个数量级以上 → **无显著关联电子行为** |

### 5c.5 SI 中的数学建模（SI §5）

SI §5 (Cazeaux, Luskin & Massatt) 提供了一个补充的数学建模视角：

- 用**广义堆垛层错能（GSFE）** 作为连续模型的层间能量泛函
- GSFE 函数形式（六重对称傅里叶展开）：

$$\phi(x,y) = c_0 + c_1[\cos x + \cos y + \cos(x+y)] + c_2[\cos(x+2y) + \cos(x-y) + \cos(2x+y)] + c_3[\cos 2x + \cos 2y + \cos(2x+2y)]$$

- 系数从 vdW-DFT 拟合：
  - $c_0 = 6.832$, $c_1 = 4.064$, $c_2 = -0.374$, $c_3 = -0.095$ meV/unit cell
  - 体模量 $K = 69518$ meV/unit cell，剪切模量 $G = 47352$ meV/unit cell

- 该模型可系统地调谐重构强度（Fig. S7），验证了卫星峰强度对域内共格度的敏感性

### 5c.6 方法总结

```
┌──────────────────────────────────────────────────┐
│                Yoo 2019 计算方法全景               │
├──────────────┬──────────────┬────────────────────┤
│   结构弛豫    │   能带结构    │       DOS          │
├──────────────┼──────────────┼────────────────────┤
│ FEM (Zhang & │ 紧束缚 (Fang │ 连续模型 (Massatt  │
│ Tadmor 2018) │ & Kaxiras    │ et al. 2018)       │
│              │ 2016)        │                    │
│ KC 层间势    │ supercell TB │ 60×60 k FEM 积分   │
│ 非线性弹性   │              │ 动量依赖应变场修正  │
└──────────────┴──────────────┴────────────────────┘
```

---

## 6. 局限与未解决的问题

| 局限 | 说明 |
|------|------|
| 应变未标定 | 无统一实验应变百分比，仅定性讨论 |
| 低角能带敏感 | ~0.5° DOS 特征对模型参数/局部构型敏感 |
| 单通道证据不足 | 拓扑网络输运证据来自宏观电输运，单条域壁的散射长度/相干长度缺直接测量 |
| 角度不确定度 | ±0.3° 影响临界角附近精细比较 |
| 强关联未展开 | 未完整展开多体态在全角度区间的统一理论 |

## 7. 与其他工作的关系

| 工作 | 关系 |
|------|------|
| Cao et al. 2018 | Magic-angle 物理要与结构重构共同考虑，尤其在 θ ≲ 1° |
| Huang 2018 PRL | 本文提供其所依赖的实空间结构基础：AB/BA 三角域 + 域壁网络 = TPH 态几何载体 |
| Rickhaus 2018 Nano Lett. | 本文给出"为什么网络会形成"的原子尺度根基与临界扭角判据 |
| Xu 2019 Nat. Commun. | 本文的重构图景是其 AB 振荡几何解释的前提 |

## 8. 对后续研究的影响

- 将"扭角工程"升级为**"扭角 + 重构 + 电场"三参数工程**
- 给出 θ_c ≈ 1° 的实践分界 — **这是整个 mTBG 域壁领域不可绕过的基准**
- 建立了从原子结构表征（TEM/SAED）到电子响应（输运/Hall/Landau）的闭环证据链
- 对后续的启发：
  1. 低角区器件设计应优先考虑域壁网络连通性
  2. E 场可作"拓扑网络开关"
  3. 关联态研究须纳入重构导致的带宽/能隙/DOS 峰形变化
  4. 域壁网络为 valley/topological 器件提供结构模板

---

*初稿：2026-08-06 | 更新 §5b/§5c：2026-08-08 | 基于 pdftotext 全文(含SI)提取 + AI 精读分析*
