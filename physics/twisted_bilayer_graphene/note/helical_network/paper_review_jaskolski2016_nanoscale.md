<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 17:12:59
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 17:13:02
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/helical_network/paper_review_jaskolski2016_nanoscale.md
 * @Description  :
-->
<!--
 * @Author       : AI精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/note/helical_network/paper_review_jaskolski2016_nanoscale.md
 * @Description  : T8: Jaskólski et al. 2016 — 晶界拓扑态:五边形缺陷不破坏保护
-->

# 论文精读：Jaskólski et al., Nanoscale (2016)

> **W. Jaskólski, M. Pelc, Leonor Chico, A. Ayuela**
> "Existence of nontrivial topologically protected states at grain boundaries in bilayer graphene: signatures and electrical switching"
> Nanoscale 8, 6079–6084 (2016) | DOI: 10.1039/c5nr08630b

---

## 1. 一句话总结

**推翻"原子缺陷→谷间散射→拓扑态消失"的直觉**：在含五边形-八边形缺陷的 BLG 晶界上，拓扑保护隙态依然存在；更意外的是，栅压极性反转会改变隙态数目 → 产生不对称电导，可做电控开关。

---

## 2. 背景与动机

### 2.1 已有知识背景

- Martin 2008、Zhang 2013 等确立了 AB/BA 堆叠畴壁 + 位移场的拓扑隙态
- Ju et al. 2015 (Nature) 实验首次确认畴壁导电通道
- 此前理论**默认前提**：畴壁必须保持子晶格对称性（无原子缺陷），否则谷间散射会破坏拓扑保护

### 2.2 本文填补的空白

晶界（grain boundary）在 CVD 生长的 BLG 中普遍存在，且天然包含五边形-八边形等拓扑缺陷。这些缺陷是否必然杀死拓扑隙态？本文首次回答：**不必然**。

---

## 3. 方法与模型

### 3.1 体系

- TB 模型：$\gamma_0 = -2.66$ eV（层内），$\gamma_1 = 0.1\gamma_0$（层间）
- 上层含 8-55（八边形-双五边形）缺陷线（沿 zigzag 方向），下层为完整石墨烯
- 缺陷两侧分别为 AB 和 BA 堆叠 → 形成晶界型畴壁
- 栅压 $V = \pm 0.3$ eV 加在下层

### 3.2 关键方法

- Green 函数匹配法计算 LDOS$(E, k_y)$
- 逐原子、逐子晶格、逐层分辨 LDOS

---

## 4. 核心结果

### 4.1 隙态数目不对称：栅压极性可控

| 栅压 | 隙态数目 | 标识 |
|------|:--------:|------|
| $V = +0.3$ eV | **3** | D (缺陷平带), S1 (拓扑), S2-D (杂化) |
| $V = -0.3$ eV | **2** | D-S3 (杂化), S4 (拓扑) |

- **D 带**：来自单层 8-55 缺陷线的平带（$E=0$ 钉扎，$k=0$ 到 Dirac 点）
- **S1/S4**：纯拓扑隙态，连接价带和导带连续区
- **S2-D / D-S3**：缺陷带与堆叠畴壁带的杂化态

### 4.2 杂化选择定则

**同层 + 同子晶格 → 强杂化**：
- $V>0$：D 带与 S2 带同在顶层 + unconnected 子晶格 → S2-D 杂化
- $V<0$：D 带与 S3 带同在顶层 + connected 子晶格 → D-S3 强反交叉

**拓扑带 S1/S4 不受杂化影响**：因为它们与 D 带的子晶格分布正交（D 在 connected，S1 在 unconnected）。

### 4.3 电控开关机制

核心发现：栅压从 $+V$ 翻转到 $-V$，隙态数目从 3 → 2 → 沿晶界的电导不对称！可做**电控开关**。

关键物理：混合节点（mixing nodes，五边形共享边上的两个原子）在低能处有反常大 LDOS — 不是因为缺陷本征态，而是 AB/BA 堆叠畴壁 + 子晶格挫折的协同效应。

---

## 5. 与其他工作的关系

| 相关工作 | 关系 |
|----------|------|
| Ju et al. 2015 Nature | 实验动机：首次可视化 BLG 畴壁导电 |
| Martin 2008 PRL | 理论起点：EFW 拓扑零模 |
| Zhang 2013 PNAS | 谷陈数 boundary mode 分类 |
| Lahiri et al. 2010 (单层 8-55 缺陷实验) | 缺陷线结构参考 |

---

## 6. 亮点与局限

### 亮点
- **反直觉发现**：五边形缺陷不破坏拓扑保护 → 拓宽了畴壁拓扑态的"生存区间"
- **电控开关预言**：栅压极性控制隙态数目 → 可实验检验
- **杂化选择定则**：层 + 子晶格匹配决定杂化强度

### 局限
- 单轨道 TB，无相互作用
- 仅考虑了一种特定缺陷构型（8-55），普适性未证明
- 未计算输运量（电导），仅 LDOS
- 栅压值 $V=0.3$ eV 偏大（实验典型 $V \sim 0.1$ eV）

---

## 7. 与用户研究的关联

| 维度 | 关联 |
|---|---|
| **方法** | Green 函数匹配法——与 DW 项目 cont.py 中的 EFW LDOS 计算思路一致 |
| **扩展方向** | DW 项目可验证：真实 8-55 缺陷构型的谷过滤效率 |
| **可验证性** | 可用 tbplas 复现 LDOS$(E,k)$ → 检验杂化选择定则是否在更精确模型下成立 |

---

## 8. 关键参数速查

| 参数 | 值 |
|------|-----|
| $\gamma_0$ (层内) | -2.66 eV |
| $\gamma_1$ (层间) | 0.1$\gamma_0$ = -0.266 eV |
| 栅压 $V$ | $\pm 0.3$ eV |
| 晶界方向 | zigzag |
| 缺陷类型 | 8-55 (八边形-双五边形) |

---

*报告生成日期：2026-08-06 | 基于 PDF pdftotext 精读*

---

## Phase S 补充 (2026-08-11): Q2/Q3

### Q2: 理论如何解释 edge state?
紧束缚 Green 函数模型：AB/BA 畴壁 8-5-5 缺陷线中拓扑 gap state 存活——波函数占据与缺陷带正交的子晶格。位移场反转时局域态数目变化，不同分支与缺陷带杂化不同。

### Q3: 理论如何与实验结合?
预言栅压可调晶界导电性，正反位移场下晶界输运不对称——含拓扑缺陷时仍可检验。
