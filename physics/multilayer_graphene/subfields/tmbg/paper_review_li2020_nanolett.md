<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-01
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/tmbg/paper_review_li2020_nanolett.md
 * @Description  : Li et al. (2020) Nano Letters 阅读笔记
 * @ZoteroKey    : ZKGJCR5G
-->
# 论文阅读笔记：Li et al., Nano Lett. 20, 3106 (2020)

> **Hongyuan Li, M. Iqbal Bakti Utama, Sheng Wang, Wenyu Zhao, Sihan Zhao, Xiao Xiao, Yue Jiang, Lili Jiang, Takashi Taniguchi, Kenji Watanabe, Alexander Weber-Bargioni, Alex Zettl, Feng Wang**
> "Global Control of Stacking-Order Phase Transition by Doping and Electric Field in Few-Layer Graphene"
> Nano Lett. 20, 3106-3112 (2020) | DOI: [10.1021/acs.nanolett.9b05092](https://doi.org/10.1021/acs.nanolett.9b05092) | Zotero: zotero://select/items/ZKGJCR5G
>
> 机构：UC Berkeley (Feng Wang 组) + 香港中文大学 + NIMS (Watanabe/Taniguchi) + LBNL

---

## 1. 一句话总结

通过**双栅极静电调控 + 红外近场光学显微镜（IR-SNOM）**在少层石墨烯中实现了 ABA ↔ ABC 堆叠序的**可逆全局相变**——以 ~50 μeV/atom 的精度测定了堆叠能量差，并揭示了**掺杂（功函数差异）和位移场（ABC 能隙打开）两种不同机制的协同驱动**。

---

## 2. 实验方法

### 2.1 核心技术：IR-SNOM 堆叠序成像

| 参数 | 细节 |
|---|---|
| 探针 | 红外散射扫描近场光学显微镜 (IR-SNOM) |
| 光源 | 10.6 μm 连续波 CO2 激光 |
| 针尖 | 金属涂层，~25 nm 曲率半径 |
| 空间分辨率 | ~40 nm |
| 物理原理 | ABA 和 ABC 堆叠在 10.6 μm 具有**不同的红外光学电导率** → ABC（暗）比 ABA（亮）吸收弱 |
| 优势 | 非侵入式、可原位成像堆叠畴的演化 |

### 2.2 器件结构

- **双栅极**：顶栅 = 单层 graphene + 薄 hBN (~4-5 nm)，底栅 = Si/SiO2 (285 nm)
- 少层石墨烯封装在 hBN 中
- 独立调控：n = (DB - DT)/e + n0，D = (DB + DT)/2 + D0

### 2.3 两种样品体系

| 体系 | 用途 |
|---|---|
| **Pristine 三层**（无转角） | 演示全局堆叠相变的基本可行性 |
| **小转角少层**（θ < 0.1°） | 系统定量研究——畴壁网络中的 ABA/ABC 畴受拓扑保护不会消失，可自由膨胀/收缩 |

---

## 3. 核心实验结果

### 3.1 Pristine 三层：全局堆叠相变的直接演示

- 固定 VB = -100 V，扫描 VT
- VT = -1.5 V → 全部 **ABA**（亮）
- VT = +1.5 V → **ABC** 畴出现（暗）
- VT = +2 V → **全视场变为 ABC**
- 畴壁运动可被褶皱（wrinkles）和裂纹（cracks）钉扎

### 3.2 畴壁曲率法精密测量堆叠能量差（★ 核心创新）

**原理**：弯曲堆叠畴壁（SDW）的形状由畴壁能量密度 E_SDW(θ) 和 ABA/ABC 能量差 ΔE 共同决定。

- 局域曲率：κ = ΔE / (E_SDW + ∂²E_SDW/∂θ²)
- 通过拟合弯曲 SDW 椭圆形状，获得：
  - **畴壁能量比** ET/ES = 1.6（实验）vs DFT 预测 1.53 ✓
  - **零掺杂零 D 场堆叠能量差** ΔE0 ≈ 50 μeV/atom（ABA 更稳定）

### 3.3 完整 (n, D) 堆叠序相图

| 区域 | 稳定堆叠 |
|---|---|
| 低掺杂 + 低 D | **ABA** |
| 高空穴掺杂 | **ABC** |
| 大位移场 D | **ABC** |
| 高电子掺杂 | ABA |

---

## 4. 物理机制：两种独立驱动力

### 4.1 掺杂驱动：功函数差异（★ 本文首次揭示）

- **KPFM 测量**：ABA 功函数比 ABC **高 ~18 meV**（范围 10-20 meV）
- 这是**首次**定量测定不同堆叠序之间的功函数差
- 掺杂 → 费米能级移动 → 功函数差导致 ΔE 随 n 线性变化：贡献 n·ΔW

### 4.2 位移场驱动：ABC 能隙打开

- D 场在 **ABC** 三层中打开能隙（ABA 不打开）
- ABC 能隙降低其总电子能量 → ABC 在 D 场下更稳定
- **仅当石墨烯接近 CNP 时才有效**——这解释了为什么单背栅无法实现全局相变

### 4.3 双栅公式

ΔE(n,D) − ΔE0 ≈ ∫[DOS₂ − DOS₁]·ε·f·dε − n·ΔW

- 第一项 = D 场通过 DOS 差异的贡献 | 第二项 = 掺杂通过功函数差的贡献
- 两项符号可同向或反向 → **双栅独立调控 n 和 D 是必需的**

---

## 5. 普适性

- **三层**（ABA ↔ ABC）和**四层**（ABAB ↔ ABCA）均演示成功
- **双层不适用**：AB 和 BA 堆叠等价（仅旋转 60°）
- 原理可推广到其他范德华材料（TMD 多层等）

---

## 6. 与用户研究领域的关联

| 维度 | 关联 |
|---|---|
| **TMBG** | 底层是 AB 堆叠双层——Li 2020 方法可**原位切换底层堆叠序** |
| **ABA/ABC 畴壁** | 本文关注**全局相变**（消除畴壁），与畴壁一维物理互补 |
| **TBPM 计算** | 可验证功函数差 ~18 meV、D 场下 ABC 能隙贡献、ET/ES = 1.6 |

---

## 7. 关键参数速查

| 参数 | 值 |
|---|---|
| 堆叠能量差 ΔE0 | ~50 μeV/atom（零掺零 D，ABA 更稳） |
| 功函数差 ABA − ABC | ~18 meV（KPFM，ABA > ABC） |
| 畴壁能量比 ET/ES | 1.6（实验）vs DFT 1.53 |
| IR-SNOM 分辨率 | ~40 nm（IR 波长 10.6 μm） |
| 顶栅介质 | 单层 graphene + ~5 nm hBN |
| 温度 | **300 K**（室温！） |
| 转角范围 | < 0.1° |

---

*笔记更新日期：2026-08-01 | PDF 全文已读 ✓ | Zotero Key: ZKGJCR5G*
