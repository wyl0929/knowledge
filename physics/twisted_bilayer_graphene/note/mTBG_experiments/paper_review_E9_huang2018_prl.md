<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 22:02:08
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 22:02:12
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/mTBG_experiments/paper_review_E9_huang2018_prl.md
 * @Description  :
-->
<!--
 * @Author       : AI 精读 (research_onboarding_skill)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/note/mTBG_experiments/paper_review_E9_huang2018_prl.md
 * @Description  : E9: Huang et al. 2018 — STM 首次发现 mTBG 畴壁 TPH 态
-->

# Paper Review: Huang et al. (2018) — mTBG 拓扑螺旋态的 STM 发现

| 字段 | 内容 |
|------|------|
| **编号** | E9 |
| **标题** | Topologically Protected Helical States in Minimally Twisted Bilayer Graphene |
| **作者** | Shengqiang Huang, Kyounghwan Kim, Dmitry K. Efimkin, Timothy Lovorn, Takashi Taniguchi, Kenji Watanabe, Allan H. MacDonald, Emanuel Tutuc, Brian J. LeRoy |
| **期刊** | PRL 121, 037702 (2018) |
| **DOI** | 10.1103/PhysRevLett.121.037702 |
| **arXiv** | 1802.02999 |
| **类型** | 实验 — STM/STS |
| **课题组** | LeRoy group (Univ. Arizona) + MacDonald theory (UT Austin) |
| **PDF** | ✅ reference/pdfs/Huang 等 - 2018 - ...pdf |
| **DW.bib** | ✅ `huang_topologically_2018` |
| **精读日期** | 2026-08-06 |

---

## 1. 核心贡献

**首次直接实验观测**到极小扭角双层石墨烯（TBLG）畴壁网络上的**拓扑保护螺旋态（TPH states）**。通过 STM/STS：

- 观测到畴壁上增强的局域态密度（LDOS）
- 观测到 TPH 态特有的**双线（double-line）空间分布**
- 证实 TPH 态仅在 AB/BA 区域被垂直电场打开能隙时才出现
- 展示了可控扭角制备超长莫尔周期（>50 nm）畴壁网络的方法

## 2. 物理机制

### 2.1 TPH 态的形成条件

1. AB 与 BA 堆垛在外加垂直电场下开隙 → 产生 Berry 曲率
2. 每谷 valley Chern number = ±1（符号依赖电场方向与堆垛）
3. AB 与 BA 在同一电场下 valley Chern number 符号相反 → 边界支持反向传播谷手征模 = TPH 态
4. **仅在 AB/BA 开隙时 TPH 态才出现**；电场近零时畴壁对比显著减弱

### 2.2 理论框架

- 低能连续模型（Bistritzer–MacDonald 框架）
- 畴壁网络模型（San-Jose & Prada 2013; Efimkin & MacDonald 2018）
- 网络特征能标：$E_\lambda = \frac{2\pi\hbar v}{3\lambda} \approx 24\,\text{meV}$（λ = 57.6 nm）

### 2.3 两类能量特征

- $E \ll \Delta$（隙内）：畴壁螺旋态主导，网络干涉导致低能结构
- $E \gtrsim \Delta$（隙外）：出现高能 van Hove 特征（约 ±0.25 V）

## 3. 实验方法

### 3.1 样品制备（tear-and-stack / sequential pickup）

- 薄 h-BN（~10–20 nm）作拾取层，从**同一片单层石墨烯**连续拾取两块
- 拾取两块之间旋转手柄设定扭角（两块同源 → 晶格取向一致 → 扭角由旋转角直接决定）
- 电极：Cr 5 nm / Au 35 nm
- 退火：高真空 350°C, 6 h

### 3.2 STM/STS 测量

- 温度：4.5 K，超高真空
- 探针：电化学刻蚀 W tip
- 隧穿电流：200 pA，稳定电压：+0.5 V
- STS 锁相调制：3 mV @ 572 Hz（点谱）；8 mV（LDOS map）
- 背栅调控层间电场

## 4. 关键数据

### 4.1 样品参数

| 参数 | 值 |
|------|-----|
| 莫尔周期 λ | 57.6 ± 0.7 nm |
| 扭角 θ | 0.245 ± 0.003° |
| 畴壁宽度 | 数 nm 量级 |

### 4.2 STS 谱特征

- **AB 区**：在 ~−0.1 V 处有带隙相关 dip；~+0.3 V 处有导带次带特征
- **畴壁**：无明显 −0.1 V dip；在 ~±0.25 V 出现高能双峰（van Hove 特征）
- **背栅依赖**（图 2c）：带隙宽度随 Vg 变化（十几到数十 meV 量级），扫描范围约 −80 到 +40 V

### 4.3 空间 LDOS 成像（TPH 关键证据）

- **Vg = +60 V（大电场），能量在隙内（~−0.11 V）**：畴壁网络亮、AB/BA 区暗，呈**双线**分布
- **Vg = +60 V，能量在隙外（~−0.245 V）**：畴壁与区域对比显著下降
- **Vg = −50 V（近零电场）**：畴壁增强缺失 → 支持"无隙则无 TPH"

### 4.4 定量对比度分析（图 4）

定义对比度 $C = [I(DW) - I(AB)] / I(AB)$：

- Vg = +60 V：C(V) 在 AB 带隙中心有主峰，带边附近降到近零
- Vg = −50 V：中心峰消失，仅保留 ±0.25 V 高能峰
- 中央峰 FWHM 与平均对比度随 Vg 减小而下降

## 5. 主要结论

1. **TPH 态存在**：畴壁处隙内 LDOS 增强 + 双线空间分布 + 仅在开隙时显著
2. **多重一致性**：与连续模型和网络模型在能谱特征上相符
3. 畴壁长度通过扭角可控 → **可设计的拓扑通道网络**平台

## 6. 局限与未解决的问题

| 局限 | 说明 |
|------|------|
| 仅局域谱学 | 无器件级输运量化（无反散射长度、电导平台等） |
| 保护性未量化 | valley 混合、无序、边缘粗糙度的影响未系统研究 |
| 低能分辨率不足 | $E_\lambda \ll \Delta$ 条件"不非常理想"，低能网络结构仅有限特征 |
| 多谷散射未知 | 高温下 TPH 稳健性未测 |
| 与强关联物理的关系 | 未涉及 magic-angle 关联态与拓扑态的竞争/耦合 |

## 7. 与其他工作的关系

| 工作 | 关系 |
|------|------|
| San-Jose & Prada (2013) | 理论预言 — 本文给出直接实验证据 |
| Efimkin & MacDonald (2018) | 畴壁网络能谱理论 — 本文 STS 谱与之一致 |
| Martin et al. (2008) | 电场畴壁零模的原始预言 |
| Ju et al. (2015) | 均匀 BLG 单条畴壁的 s-SNOM 可视化 |
| Yin et al. (2016) | STM 观测 BLG 单条畴壁边缘态 |

## 8. 对后续研究的影响

- 将"拓扑界面态"从单条界面推进到**二维可工程化网络**
- 方法学：证明扭角工程 + 局域探针可直接鉴别拓扑态
- 与 2018 年 magic-angle 热潮并行，开辟了"非强关联拓扑网络"研究主线
- 启示：畴壁长度 = f(θ) → 可按需设计拓扑通道网络

---

*精读完成日期：2026-08-06 | 基于 pdftotext 全文提取 + AI 精读分析*

---

## Phase S 补充 (2026-08-11): Q1

### Q1: edge state 实验上如何表征?
低温 STM/STS 直接成像 mTBG 畴壁网络。核心可观测量：LDOS 空间图——畴壁上的强能隙内 LDOS 增强，呈特征双线 (double-line) 图案。关键对照：LDOS 增强仅在垂直电场打开 AB/BA 能隙时出现。通过畴壁处 gap 内态 vs AB/BA 区域 gapped 谱区分边缘 vs 体。首次直接观测 mTBG 中 TPH 态。
