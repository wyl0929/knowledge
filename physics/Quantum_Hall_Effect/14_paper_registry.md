<!--
Field: 量子霍尔效应
Mode: quick_scan
Domain archetype: science_technical
Created date: 2026-06-10
-->

# 14 Source Registry / 来源与阅读入口注册表

Last updated: 2026-06-10

## 推荐阅读顺序（研究切入）

1. TKNN (1982) — 理解 Chern 数的物理来源
2. Haldane (1988) — 理解 QAHE 的理论蓝图
3. Kane-Mele (2005) — 理解 QSHE 和 $\mathbb{Z}_2$
4. BHZ (2006) — QSHE 的具体实验方案
5. Chang et al. (2013) — QAHE 实验实现
6. Review: Hasan-Kane (2010) 或 Qi-Zhang (2011)

---

## 里程碑论文

### IQHE 奠基

| 条目 | 内容 |
|------|------|
| 来源类型 | foundational theory |
| 标题 | New Method for High-Accuracy Determination of the Fine-Structure Constant Based on Quantized Hall Resistance |
| 作者 | K. von Klitzing, G. Dorda, M. Pepper |
| 年份/期刊 | 1980, Phys. Rev. Lett. 45, 494 |
| 核心发现 | 首次观测到 Si MOSFET 中霍尔电阻的精确量子化平台 |
| 阅读建议 | 短小精悍（4 页），实验物理经典 |

### TKNN — 拓扑解释

| 条目 | 内容 |
|------|------|
| 来源类型 | foundational theory |
| 标题 | Quantized Hall Conductance in a Two-Dimensional Periodic Potential |
| 作者 | D. J. Thouless, M. Kohmoto, M. P. Nightingale, M. den Nijs |
| 年份/期刊 | 1982, Phys. Rev. Lett. 49, 405 |
| 核心公式 | $\sigma_{xy} = \frac{e^2}{h}C$，其中 $C$ 是 Chern 数 |
| 核心发现 | 霍尔电导量子化 = 占据态的拓扑不变量 |
| 与用户关系 | ⭐⭐⭐⭐⭐ — 计算 Chern 数的理论基础 |

### Haldane 模型 — QAHE 蓝图

| 条目 | 内容 |
|------|------|
| 来源类型 | foundational theory |
| 标题 | Model for a Quantum Hall Effect without Landau Levels: Condensed-Matter Realization of the "Parity Anomaly" |
| 作者 | F. D. M. Haldane |
| 年份/期刊 | 1988, Phys. Rev. Lett. 61, 2015 |
| 核心发现 | 六角晶格上交错磁通 + 破缺时间反演 → 零净磁场下的 Chern 绝缘体 |
| 与用户关系 | ⭐⭐⭐⭐⭐ — TB 模型可直接实现，graphene.py 改交错磁通即可 |
| 阅读建议 | 对石墨烯研究者尤其值得精读 |

### FQHE — Laughlin

| 条目 | 内容 |
|------|------|
| 来源类型 | foundational theory |
| 标题 | Anomalous Quantum Hall Effect: An Incompressible Quantum Fluid with Fractionally Charged Excitations |
| 作者 | R. B. Laughlin |
| 年份/期刊 | 1983, Phys. Rev. Lett. 50, 1395 |
| 核心发现 | Laughlin 波函数解释 $\nu=1/m$ FQHE |
| 与用户关系 | ⭐⭐ — 方法上距离较远，但概念上应了解 |

### QSHE — Kane-Mele + BHZ

| 条目 | 内容 |
|------|------|
| 来源类型 | foundational theory |
| 标题 | Quantum Spin Hall Effect in Graphene (Kane-Mele) |
| 作者 | C. L. Kane, E. J. Mele |
| 年份/期刊 | 2005, Phys. Rev. Lett. 95, 226801 |
| 核心发现 | 石墨烯中 SOC 可产生 QSHE（SOC 太弱无法实现，但打开了概念门） |
| 与用户关系 | ⭐⭐⭐⭐ — graphene.py 加入 Kane-Mele SOC 项是直通路径 |

| 条目 | 内容 |
|------|------|
| 来源类型 | foundational theory |
| 标题 | Quantum Spin Hall Effect in HgTe Quantum Wells (BHZ) |
| 作者 | B. A. Bernevig, T. L. Hughes, S. C. Zhang |
| 年份/期刊 | 2006, Science 314, 1757 |
| 核心发现 | 提出 HgTe/CdTe 量子阱中 QSHE 的可验证方案 |
| 与用户关系 | ⭐⭐⭐ — BHZ 模型是实现 $\mathbb{Z}_2$ 计算的常见测试基准 |

### QAHE 实验实现

| 条目 | 内容 |
|------|------|
| 来源类型 | recent study |
| 标题 | Experimental Observation of the Quantum Anomalous Hall Effect in a Magnetic Topological Insulator |
| 作者 | C.-Z. Chang et al. (薛其坤组) |
| 年份/期刊 | 2013, Science 340, 167 |
| 核心发现 | Cr 掺杂 (Bi,Sb)₂Te₃ 薄膜中首次测量到 $\sigma_{xy}=e^2/h$ 零场量子化 |
| 当前引用 | > 4000+ |
| 与用户关系 | ⭐⭐⭐⭐ — 实验里程碑，理论计算理解其机制仍是活跃方向 |

---

## 关键综述

| 综述 | 覆盖范围 | 推荐程度 |
|------|---------|:---:|
| Hasan & Kane, *Rev. Mod. Phys.* 82, 3045 (2010) | 拓扑绝缘体全景 | ⭐⭐⭐⭐⭐ |
| Qi & Zhang, *Rev. Mod. Phys.* 83, 1057 (2011) | 拓扑绝缘体理论 | ⭐⭐⭐⭐⭐ |
| Weng et al., *Rep. Prog. Phys.* 79, 074401 (2016) | QAHE 综述 | ⭐⭐⭐⭐ |
| Bansil et al., *Rev. Mod. Phys.* 88, 021004 (2016) | 拓扑材料计算 | ⭐⭐⭐⭐ |
| Haldane, *Rev. Mod. Phys.* 89, 040502 (2017) | 诺奖演讲：拓扑物态 | ⭐⭐⭐⭐ |
| Vanderbilt, *Berry Phases in Electronic Structure Theory* (2018) | Berry 相位与计算 | ⭐⭐⭐⭐⭐ |
| C.-X. Liu et al., *Annu. Rev. Condens. Matter Phys.* 7, 301 (2016) | QAHE 理论与实验进展 | ⭐⭐⭐⭐ |

---

## 计算方法关键文献

| 文献 | 核心方法 | 与用户关系 |
|------|---------|:---:|
| Fukui, Hatsugai, Suzuki, JPSJ 74, 1674 (2005) | 离散 k 空间 Chern 数计算 | ⭐⭐⭐⭐⭐ |
| Soluyanov & Vanderbilt, PRB 83, 235401 (2011) | Wannier 电荷中心 / $\mathbb{Z}_2$ | ⭐⭐⭐⭐ |
| Marzari & Vanderbilt, PRB 56, 12847 (1997) | 最大局域化 Wannier 函数 | ⭐⭐⭐ |
| Gresch et al., PRB 95, 075146 (2017) | 自动 Wannier 化 + 拓扑计算 | ⭐⭐⭐⭐ |

---

## 近期趋势信号 (2020-)

| 趋势 | 代表工作 (NEEDS_VERIFICATION 细节) |
|------|------|
| 高温 QAHE | MnBi₂Te₄ 家族（本征磁性拓扑绝缘体），~5-10 K 量级 |
| 分数陈绝缘体 | 摩尔超晶格中零磁场分数态，twisted MoTe₂ |
| 拓扑材料高通量 | 中科院物理所拓扑材料数据库，~8000+ 种拓扑材料 |
| 高阶拓扑绝缘体 | 铰链态、角态的量子化 |
| 机器学习 + 拓扑 | ML 预测拓扑材料，加速 DFT 筛选 |
| 非线性霍尔效应 | 量子度规 (quantum metric) 对非线性输运的贡献 |

## 证据角色

- 概念定义；
- 领域入口；
- 代表论证；
- 近期趋势；
- 第一手阅读对象；
- 方法资源。

## Source Entry / 来源条目

**Source ID / 来源编号：**

**来源类型：**

**证据角色：**

**Title / 题名：**

**Authors / 作者或机构：**

**Year / 年份：**

**Venue / Source / 来源：**

**URL / DOI：**

**Status:** seed / skimmed / parsed / verified / archived

**人话摘要：**
这个来源到底提供了什么？它为什么会被放进这个领域地图？

**核心贡献或用途：**

**关键假设或边界：**

**与本 field pack 的关系：**

**Need verification / 待核验：**

**Last updated / 最后更新：**

---

## Registry Table / 汇总表

| Source ID | 来源类型 | 证据角色 | Title | Year | Status | 人话摘要 | Need verification | Last updated |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | seed |  | NEEDS_VERIFICATION |  |
