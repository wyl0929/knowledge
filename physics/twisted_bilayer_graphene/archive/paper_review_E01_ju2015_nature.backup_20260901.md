<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-15
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-16
 * @FilePath     : /project/knowledge/physics/note/experiments/paper_review_E01_ju2015_nature.md
 * @Description  : Ju et al. (2015) Nature 精读报告 — 双层石墨烯畴壁拓扑谷输运的首次实验验证（基于原文 PDF 重写）
-->

# 论文精读：Ju et al., Nature 520, 650 (2015)

> **Long Ju\*, Zhiwen Shi\*, Nityan Nair, Yinchuan Lv, Chenhao Jin, Jairo Velasco Jr, Claudia Ojeda-Aristizabal, Hans A. Bechtel, Michael C. Martin, Alex Zettl, James Analytis, Feng Wang** (\*equal contribution)
> "Topological valley transport at bilayer graphene domain walls"
> Nature **520**, 650–655 (2015) | 正文 6 页 + Methods + Extended Data
>
> 作者单位：UC Berkeley（F. Wang 组）+ LBNL Advanced Light Source
>
> **DOI**: [10.1038/nature14364](https://doi.org/10.1038/nature14364)
> **arXiv**: 无（Nature 论文，发表前无公开 preprint）
> **Zotero Key**: `IV7DIBD2` → `cmd.exe /c start "zotero://select/items/IV7DIBD2"`

> **来源声明**：本笔记基于 `Ju 等 - 2015 - Topological valley transport at bilayer graphene domain walls.pdf` 全文（pdftotext 提取，Nature 出版版本，10 页含 Methods 和 Extended Data）。数据可靠。

---

## 1. 一句话总结

**首次实验验证**了双层石墨烯中 AB/BA 堆叠畴壁承载拓扑保护的谷极化一维导电通道。两套互补探针：（1）s-SNOM 红外近场成像直接可视化畴壁；（2）**双栅电学输运测量**——发现畴壁通道电阻在体带隙打开后饱和于 ~14 kΩ，弹道长度 $L_0 \approx 420$ nm（4 K），200 nm 通道电导接近 $4e^2/h$。畴壁表现出金属性温度依赖（$R$ 基本不随 $T$ 变），与体 BLG 的绝缘行为形成鲜明对比。

---

## 2. 背景与动机

### 2.1 2015 年的领域状态

- 理论预言双层石墨烯的 AB/BA 堆叠畴壁处存在拓扑保护的谷极化一维通道（Martin et al. PRL 2008 提出静电壁方案；Zhang et al. PRB 2011 / Qiao et al. Nano Lett. 2011 提出结构堆叠壁方案）
- 透射电镜（TEM）已看到悬浮 BLG 中存在 ~几 nm 宽的 AB-BA 畴壁（Alden et al. 2013, Lin et al. 2013），但悬浮样品无法做栅控输运
- **核心空白**：没有人（1）在器件衬底上找到畴壁，（2）测量其电学输运，（3）证明谷极化

### 2.2 本文填补的所有空白

| 问题 | 本文的回答 |
|---|---|
| 机械剥离 BLG 在 SiO₂/Si 上是否有畴壁？ | ✅ ~30% 的双层样品有，s-SNOM 直接成像 |
| 畴壁是否导电？ | ✅ 电阻饱和于 ~14 kΩ（体绝缘后） |
| 导电通道的弹道长度？ | ✅ $L_0 \approx 420$ nm（4 K） |
| 是否达到量子电导？ | ✅ 200 nm 通道接近 $4e^2/h$ |
| 畴壁 vs 体 BLG 的温度依赖？ | ✅ 畴壁金属性，体绝缘性 |

---

## 3. 方法与体系

### 3.1 样品制备

| 参数 | 值 |
|---|---|
| 材料 | 机械剥离少层石墨烯于 280 nm SiO₂/Si |
| 畴壁鉴定 | s-SNOM 红外成像（中红外 6.1 μm，空间分辨 ~40 nm） |
| 畴壁出现率 | ~30% 的双层样品 |
| 介质 | 35 nm ALD Al₂O₃ 顶栅介质 |
| 栅极 | Si 底栅 + Au 顶栅（双栅独立调控 $D$ 和 $n$） |
| 电极 | 40 nm Au / 0.5 nm Cr，EBL 定义 |

### 3.2 双探针互补策略

| 探针 | 信息 | 空间分辨 |
|---|---|---|
| **s-SNOM**（Fig. 1–2） | 畴壁位置 + 红外响应 | ~40 nm |
| **电学输运**（Fig. 3–4） | $R(D, T)$ + 弹道长度 | 通道长度 200–1000 nm |

### 3.3 s-SNOM 对比度机制

- AB 和 BA 堆叠有相同的电子结构和红外吸收 → 畴区内对比度均匀
- 畴壁可近似为"随机堆叠双层" → 局域红外电导率 $\approx 2\sigma_{\text{monolayer}}$，比 $\sigma_{\text{bilayer}}$ 高 ~20% → **亮线**

### 3.4 器件布局（关键！）

```
电极 1 ──DW── 电极 2 ──DW── 电极 3
                 │
            (单畴 BLG 参考)
                 │
              电极 4 ──(无 DW)── 电极 5
```

- 电极 2–3：单条 DW 通道（主测量）
- 电极 3–4 和 4–5：同片上的无 DW 参考器件
- 顶栅 TG1/TG2 宽 1 μm 定义通道长度
- 另外 4 对额外器件（Extended Data Fig. 1），含一个双 DW 器件

---

## 4. 核心结果

### 4.1 s-SNOM 畴壁成像（Fig. 1–2）

- **单层石墨烯**：内部永远均匀，无边界的亮线 → 畴壁仅存在于 ≥ 双层
- **双层石墨烯**：~30% 样品有内部亮线 → AB-BA 畴壁
- **三层石墨烯**：亮线分隔不同对比度的畴区 → 不同堆叠（ABA vs ABC）→ 拉曼确认
- 畴壁宽度：s-SNOM 分辨率限制（~40 nm），实际畴壁宽度 ~几 nm（TEM 文献值）

### 4.2 输运：畴壁 vs 无畴壁的鲜明对比（Fig. 3–4）

| | 无 DW 参考器件 | 有 DW 器件 | 双 DW 器件 |
|---|---|---|---|
| CNP 电阻行为 | **单调增长**至 > 80 kΩ | **饱和**于 ~14 kΩ | 饱和于 ~8 kΩ |
| 物理 | 体带隙增大 → 绝缘 | DW 通道分流 → 电阻上限 | 两条 DW 并联 → 更低 |
| 温度依赖 (1.8→50 K) | $R$ 增加 2.5×（绝缘） | $R$ 仅增 < 50%（金属） | — |

**5 对器件全部一致**（Extended Data Fig. 1）——畴壁导电是鲁棒的。

### 4.3 弹道长度与量子电导（Fig. 4b）

测量同一畴壁上不同长度（200, 400, 600, 800 nm + 另一批 1000 nm）的通道电导：

Landauer-Büttiker 拟合：

$$G = \left(R_c + R_0\left(1 + \frac{L}{L_0}\right)\right)^{-1}, \quad R_0 = \frac{h}{4e^2}$$

结果：**$L_0 = 420$ nm, $R_c = 0$**（4 K）

- **200 nm 通道电导接近 $4e^2/h$** ← 弹道极限！
- 所有通道电导在 $e^2/h$ 量级

### 4.4 谷-动量锁定的物理图像（Fig. 4c–d）

- 能带计算：$K$ 和 $K'$ 谷的畴壁态具有**相反的色散** → $K$ 谷态沿 $+x$、$K'$ 谷态沿 $-x$ 传播
- 每个谷 2 个自旋简并模式 → 共 4 个一维通道 → 理想电导 $4e^2/h$
- 谷间散射需要 $\Delta k = 4\pi/(3\sqrt{3}a_{c-c})$ 的大动量转移 → 在 smooth DW 中被压制
- 实测 $L_0 = 420$ nm 与文献中 BLG 在 SiO₂ 上的谷间散射长度 300–800 nm 一致（Gorbachev et al. PRL 2007）

---

## 5. 与其他工作的关系

### 5.1 在三篇单 LSW 实验中的奠基地位

| | Ju 2015 | Li 2016 | Mania 2019 |
|---|---|---|---|
| DW 类型 | **结构 AB/BA** | 静电 $V{=}0$ 线 | 折叠结构 |
| 探针 | s-SNOM **+ 电学** | 电学 | 电学 |
| 零场弹道长度 | **420 nm** | 70–200 nm | **~20 μm** |
| 零场量子电导 | 接近（200 nm 通道） | 否（需 8T） | **是（$R \approx h/4e^2$）** |
| 关键局限 | SiO₂ 衬底（迁移率低） | 宽结引入非手征态 | 折叠随机不可扩展 |

> **重要纠正**：Ju 2015 **确实测量了电学输运**！$R(D)$ 饱和、$L_0 = 420$ nm、接近 $4e^2/h$ 的电导——这些是货真价实的单 LSW 输运测量。之前基于 registry 概要将 Ju 2015 归为"纯光学探针"是不准确的。

### 5.2 Ju 2015 输运 vs Li 2016 输运的本质区别

| 维度 | Ju 2015 | Li 2016 |
|---|---|---|
| DW 类型 | 天然结构 AB/BA 边界 | 栅控静电 $V{=}0$ 线 |
| DW 锐度 | **~几 nm**（smooth shear soliton） | **~70–110 nm**（栅极间距限制） |
| 器件衬底 | SiO₂/Si | **hBN 封装** |
| 迁移率 | 低（SiO₂） | **高**（10⁵ cm²/Vs） |
| 弹道长度 | **420 nm** | 70–200 nm |
| 为什么 Ju 2015 反而更好？ | SiO₂ 上但 DW 锐利 | hBN 上但 DW 宽（非手征态引入背散射） |

这暗示：**DW 锐度比衬底质量对弹道输运更重要**——Mania 2019（原子级 sharp 折叠 DW + hBN）给出 $L_{MFP} \sim 20$ μm 也支持这一结论。

---

## 6. 亮点与局限

### 亮点

1. **首次全方位验证**：s-SNOM 定位 + 电学输运 + 温度依赖 + 长度依赖 + 栅控——一套完整证据链
2. **电学量子输运**：200 nm 通道接近 $4e^2/h$，$L_0 = 420$ nm——首个 DW 弹道输运实验
3. **双 DW 器件**：电阻减半（~8 kΩ vs ~14 kΩ）→ 证明 DW 通道可并联
4. **金属性温度依赖**：DW 通道 $R(T)$ 近乎平坦，与体 BLG 绝缘行为鲜明对比
5. **s-SNOM 对比度机制清晰**：DW ≈ 随机堆叠 → $2\sigma_{\text{monolayer}}$ 的红外响应
6. **三层畴壁的附带发现**：ABA/ABC 堆叠畴壁也可见，且拉曼可区分

### 局限

1. **SiO₂ 衬底限制**：迁移率远低于 hBN 封装 → 无法探索更高弹道性的可能性
2. **$L_0 = 420$ nm 仍远短于理论极限**：受限于 SiO₂ 上的谷间散射（已知 300–800 nm）
3. **仅两探针测量**：无法分离接触电阻和通道电阻（虽然 $R_c = 0$ 拟合支持忽略接触）
4. **无磁场数据**：QH 区域的行为完全未探索（留给 Mahapatra 2022）
5. **s-SNOM 无法分辨单条 DW 的内部结构**：~40 nm 空间分辨 vs ~几 nm 的 DW 宽度
6. **无法独立证明谷极化**：电学测量只能说明通道存在，谷-动量锁定的直接证据需要等离激元或 valley filter 实验

---

## 7. 与用户研究的关联

| 维度 | 关联 |
|---|---|
| **TBPM 对标** | $L_0 = 420$ nm 是可计算量——TBPM 能否复现？扫 DW 宽度、无序强度 |
| **$R(D)$ 饱和曲线** | 直接对标——TBPM 计算 $\sigma_{xx}(E_F, D)$ → $R(D)$ |
| **长度依赖** | Landauer-Büttiker 拟合 → TBPM 计算 $\sigma_{xx}(L)$ 提取 $L_0$ |
| **双层 AB/BA DW** | TB 模型中构造 shear soliton → 计算能带 → 验证 4 通道简并度 |
| **双 DW 并联** | 构造 2 条独立 DWs → 验证电导是否加倍 |
| **LDOS 对标 s-SNOM** | s-SNOM 对比度剖面 ↔ TBPM LDOS 空间分布 |

### 关键待验证的计算预测

1. $L_0 = 420$ nm 在你的 TBPM 模型中能否复现？需多少无序强度？
2. 200 nm 通道的 $G \approx 4e^2/h$ 在你的计算中是否出现平台？
3. SiO₂ vs hBN 衬底（即不同无序水平）如何影响 $L_0$？

---

## 8. 关键参数速查

| 参数 | 值 | 来源 |
|---|---|---|
| 红外波长 | 6.1 μm（中红外） | 正文 |
| s-SNOM 空间分辨 | ~40 nm | 正文 |
| DW 出现率（双层） | ~30% | 正文 Fig. 2 |
| 顶栅介质 | 35 nm ALD Al₂O₃ | 正文 |
| 顶栅宽度（通道长度） | 200–1000 nm | 正文 Fig. 4 |
| 单 DW 饱和电阻 | **~14 kΩ**（4.2 K） | 正文 Fig. 3d |
| 双 DW 饱和电阻 | **~8 kΩ** | Extended Data Fig. 1d |
| 无 DW 参考电阻 | > 80 kΩ | 正文 Fig. 3c |
| 弹道长度 $L_0$ | **420 nm** | Landauer-Büttiker 拟合 |
| 最短通道电导 | ~$4e^2/h$（200 nm, 4 K） | 正文 Fig. 4b |
| 温度范围 | 1.8–50 K（输运） | Methods |
| 测量器件数 | 5 对 DW + 参考 + 2 批长度依赖 | 正文 + Extended Data |
| 理论模型 | $K/K'$ 谷反色散 → valley-momentum locking | 正文 Fig. 4c–d |

---

*报告生成日期：2026-07-15 | 重写于 2026-07-16*
*来源：Nature 520, 650–655 (2015) 出版版 PDF（10 页），pdftotext 全文提取*
*Zotero Key: IV7DIBD2*

---

## 附录 C：tbplas Kubo-Bastin 复现 Ju 2015 Fig. 4b 的物理映射

> 追加日期：2026-07-16 | 后续 DW 计算项目的操作参考

### C.1 核心问题

Ju 2015 Fig. 4b 测量的是**准 1D DW 通道的两探针电导 $G(L)$**。tbplas 的 Kubo-Bastin 计算的是**2D 周期超胞的电导率张量 $\sigma_{xx}$**。两者量纲不同，需要一套明确的物理映射和数据处理流水线。

### C.2 关键物理量的关系

| | 实验 (Ju 2015) | tbplas Kubo-Bastin |
|---|---|---|
| **物理量** | $G$ [S] — 1D 通道电导 | $\sigma_{xx}$ [S/□] — 2D 平均电导率 |
| **几何依赖** | 随 $L$ 变化（Landauer-Büttiker） | 强度量（但含 DW 时反比于 $W_x$） |
| **量子化极限** | $G_0 = 4e^2/h \approx 155$ μS | 不直接量子化（被 $W_x$ 稀释） |

### C.3 三步提取流水线

#### 步骤 1：减除体背景

$$\boxed{\sigma_{xx}^{\text{DW}}(E_F, D) = \sigma_{xx}^{\text{with DW}}(E_F, D) - \sigma_{xx}^{\text{no DW}}(E_F, D)}$$

- $\sigma_{xx}^{\text{with DW}}$：AB/BA DW 超胞的 Kubo-Bastin 结果（CNP, 大 $D$）
- $\sigma_{xx}^{\text{no DW}}$：同尺寸纯 AB 超胞的结果
- 当 $D$ 足够大、$E_F$ 在带隙内时，$\sigma_{xx}^{\text{no DW}} \approx 0$，减法退化为直接使用 $\sigma_{xx}^{\text{with DW}}$

#### 步骤 2：2D → 1D 换算

$$\boxed{G_{\text{DW}}(L) = \sigma_{xx}^{\text{DW}} \times \frac{L_y}{W_x}}$$

| 符号 | 含义 | 建议值 |
|---|---|---|
| $L_y$ | 超胞沿 DW 方向的长度 | 扫描 200, 400, 600, 800, 1000 nm |
| $W_x$ | 超胞垂直于 DW 的宽度 | ≥ 30 nm（含 DW + 两侧足够体区） |

**物理直觉**：TBPM 把 DW 的 1D 弹道电导 $G_{\text{DW}} \sim 4e^2/h$ "稀释"到宽度 $W_x$ 上 → $\sigma_{xx}^{\text{DW}} = G_{\text{DW}} \cdot (W_x/L_y)$。$W_x$ 越大，$\sigma_{xx}^{\text{DW}}$ 越小。

**自洽性检验**：固定 $L_y$，加倍 $W_x$ → $\sigma_{xx}^{\text{DW}}$ 应减半 → $G_{\text{DW}}$ 不变。

#### 步骤 3：长度扫描 + Landauer-Büttiker 拟合

对 $G_{\text{DW}}(L_y)$ 做与 Ju 2015 完全相同的拟合：

$$G(L) = \left(R_c + \frac{h}{4e^2}\left(1 + \frac{L}{L_0}\right)\right)^{-1}$$

提取 **$L_0$**（弹道平均自由程）和 **$R_c$**（接触电阻，TBPM 中应 ≈ 0），直接对标 Ju 2015 的 $L_0 = 420$ nm。

### C.4 超胞设计的约束条件

| 约束 | 原因 | 建议 |
|---|---|---|
| $W_x \gg 2x_0$ | DW 波函数衰减长度 $x_0 \propto 1/E_g$；$W_x$ 太小则 DW 态与边界镜像耦合 | $D=1$ V/nm 时 $x_0 \sim 5$ nm → $W_x \geq 30$ nm |
| DW 沿 $y$ 方向 | 确保 DW 通道与电流方向一致 | $L_y$ 扫描 |
| 周期边界 | Kubo-Bastin 要求周期超胞 | AB/BA/AB 或 BA/AB/BA 三区结构 |
| KPM 参数 | $M \leq 2560$, `rescale: -1` | memory 中经验约束 |

### C.5 YAML 配置模板

```yaml
system:
  model:
    type: bilayer_graphene_dw
    stacking: AB_BA
    dw_width: 10               # nm
    supercell:
      L_x: 30                  # nm
      L_y: 200                 # nm, 扫描此值

  disorder:
    type: Anderson
    strength: 0.1              # eV, 需调参匹配 SiO₂

  field:
    displacement: 1.0          # V/nm

calc:
  type: dckb
  dckb_num_kernel: 2048
  dckb_num_random: 10
  temperature: 4               # K
  energy:
    range: [-0.1, 0.1]
    points: 51
  rescale: -1                  # 必须！

output:
  quantities: [sigma_xx, sigma_xy]
```

### C.6 提取伪代码

```python
from scipy.optimize import curve_fit

h_over_e2 = 25812.807  # Ω, von Klitzing constant
G0 = 4 / h_over_e2      # 4e²/h in S

def LB(L, L0, Rc):
    """Landauer-Buttiker formula for 1D ballistic channel"""
    return 1.0 / (Rc + (1.0/G0) * (1.0 + L/L0))

G_data, L_data = [], []
for L in [200, 400, 600, 800, 1000]:
    sigma_with = load_kubo(f"dw_L{L}.h5")    # sigma_xx at CNP
    sigma_without = load_kubo(f"nodw_L{L}.h5")
    sigma_dw = sigma_with - sigma_without
    G_dw = sigma_dw * L / W_x               # 2D → 1D
    G_data.append(G_dw)
    L_data.append(L)

popt, _ = curve_fit(LB, L_data, G_data, p0=[420, 0])
L0_fitted, Rc_fitted = popt
print(f"TBPM: L0 = {L0_fitted:.0f} nm (Ju 2015: 420 nm)")
print(f"TBPM: Rc = {Rc_fitted:.0f} Ω (Ju 2015: ~0)")
```

### C.7 对标实验的检验清单

| # | 检验项 | 判定标准 |
|---|---|---|
| 1 | $W_x$ 缩放检验 | $\sigma_{xx}^{\text{DW}} \propto 1/W_x$ → $G_{\text{DW}}$ 不变 |
| 2 | $L_0$ 的 $D$ 依赖 | $D \uparrow$ → $x_0 \downarrow$ → $L_0 \uparrow$（与 Zhang 2024 机制一致） |
| 3 | 无序强度扫描 | Anderson $W \uparrow$ → $L_0 \downarrow$ |
| 4 | 弹道极限 | $L_y \to 0$ 时 $G_{\text{DW}} \to 4e^2/h$ |
| 5 | 体绝缘极限 | $D$ 足够大时 $\sigma_{xx}^{\text{no DW}} \approx 0$ |
| 6 | $L_0$ 对标实验 | 在合理无序强度下 $L_0 \approx 420$ nm |

### C.8 TBPM 能捕捉和不能捕捉的物理

| ✅ 能捕捉 | ⚠️ 需注意 |
|---|---|
| AB/BA DW 能带色散 | KPM 收敛：$M \leq 2560$, `rescale: -1` |
| 四重简并模式计数 | Anderson 无序 ≠ 长程 Coulomb 无序 |
| 谷间散射对 $L_0$ 的影响 | $W_x$ 必须足够大（$\gg$ 波函数衰减长度） |
| 位移场 $D$ 调控 $L_0$ | 短通道极限（$L_y < 200$ nm）可能欠收敛 |
| 长度依赖的弹道-扩散过渡 | 体背景扣除在高 $T$ 或小 $D$ 下不干净 |

### C.9 适用范围

此映射方法同样适用于：
- **Li 2016**：静电 DW → TB 模型中层偏压在空间中平滑翻转
- **Mania 2019**：折叠 DW → 层序反转的 AB/BA 边界极限情况
- **Zhang 2024**：多 LSW 束耦合 → 超胞中构造多条 DW，提取耦合效应
- **任意 DW 构型的 1D 弹道输运对标**

---

*附录 C 追加于 2026-07-16 | 基于 tbplas Kubo-Bastin 与 Ju 2015 Fig.4b 的物理映射分析*
