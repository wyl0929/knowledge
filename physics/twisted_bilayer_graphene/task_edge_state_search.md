<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 02:34:35
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 02:34:39
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/multilayer_graphene/subfields/tbg/task_edge_state_search.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/tbg/task_edge_state_search.md
 * @Description  : TBG edge state 文献搜集任务 — AI agent 可执行
-->

# Task: TBG Edge State 文献搜集

> 状态: ✅ 已完成 (2026-08-06)
> 创建: 2026-08-06
> 优先级: medium
> 搜索范围: 2013–2026 实验 + 理论
> 产出: 14_paper_registry.md (62篇文献, 含36篇新发现)

---

## 搜索目标

系统搜集**转角双层石墨烯（TBG）中拓扑边缘态/畴壁导电通道**的全部关键文献，覆盖：

- **AB/BA 畴壁处的量子谷霍尔（QVH）边缘态**
- **畴壁导电网络的输运实验**（FP/AB 振荡、电导平台等）
- **STM/STS 对畴壁态的实空间观测**
- **螺旋网络模型（helical network model）及后续理论发展**
- **PLL（pseudo-Landau levels）在畴壁处的形成**
- **畴壁拓扑态对无序/缺陷的稳健性**

## 排除范围

- TBG 魔角附近的体态物理（超导、关联绝缘态等）——除非明确涉及边缘/畴壁
- ABC trilayer graphene 中的边缘态（这属于另一个子方向 stacking-dw）
- 纯器件工程/制备方法

---

## 执行步骤

**请按照以下步骤执行，每步完成后输出中间结果，最后汇总。**

### Step 1：种子文献确认（基于已有知识库）

检查 `/home/wyl/project/knowledge/physics/multilayer_graphene/` 中已整理的论文，提取已确认的 TBG domain wall / edge state 相关种子论文。

**应包含（已知的种子）**：
- San-Jose & Prada, PRB 88, 121408(R) (2013) — 螺旋网络理论奠基
- Efimkin & MacDonald, PRB 98, 035404 (2018) — 螺旋网络系统理论
- Huang et al., PRL 121, 037702 (2018) — STM 首次观测畴壁 THS
- Rickhaus et al., Nano Lett. 18, 6725 (2018) — 输运 FP+AB 振荡
- Yoo et al., Nature Mater. 18, 448 (2019) — STEM 晶格重构 + 畴壁输运
- Xu et al., Nat. Commun. 10, 4008 (2019) — 巨幅 AB 振荡
- Verbakel et al., PRB 103, 165134 (2021) — FT-STM 谷保护
- Mahapatra et al., Nano Lett. 22, 5708 (2022) — QH 干涉仪
- Zheng et al., PRL 129, 076803 (2022) — PLL + 电子 Kagome
- Hou et al., PRB 110, L161406 (2024) — TZM vs 网络模型裁决

→ 输出：确认的种子论文完整列表（作者、年份、标题、arXiv ID/DOI、期刊）

### Step 2：向前追溯——引用链（Semantic Scholar API）

对上述种子论文中最重要的 5 篇（San-Jose 2013, Huang 2018, Rickhaus 2018, Yoo 2019, Zheng 2022），查询 2019–2026 年间的**被引用列表**。

**查询方法**：
```
优先使用 Semantic Scholar API:
https://api.semanticscholar.org/graph/v1/paper/arXiv:{arxiv_id}/citations?fields=title,authors,year,externalIds,journal&limit=50

备选: arXiv 搜索引用了这些论文的新工作
```

→ 输出：每篇种子的被引用列表中与 edge state 相关的新论文

### Step 3：关键词组合搜索（arXiv）

使用以下 8 组关键词在 arXiv 搜索（每组取前 10 条）：

| # | 搜索词 | 目标 |
|---|---|---|
| 1 | `"twisted bilayer graphene" "edge states"` | 精确匹配 TBG 边缘态 |
| 2 | `"twisted bilayer" "domain wall" topological` | TBG 畴壁拓扑 |
| 3 | `"TBG" "valley Hall" edge` | 缩写 + QVH 机制 |
| 4 | `"moiré graphene" "boundary mode"` | 变体 + 同义词 |
| 5 | `"helical network" graphene twisted` | 螺旋网络模型 |
| 6 | `"topological helical state" graphene domain` | 拓扑螺旋态 |
| 7 | `"quantum valley Hall" "twisted bilayer"` | QVH 机制变体 |
| 8 | `"domain wall" "twisted bilayer" transport conductance` | 畴壁输运 |

**arXiv 搜索 URL 格式**：
```
https://arxiv.org/search/?searchtype=all&query={url_encoded_query}&start=0
```

→ 输出：每个搜索词的命中列表，标注初步相关性（相关/待定/无关）

### Step 4：概念扩展搜索

对上一步中表现不佳的关键词，用同义词替换后重新搜索：

| 原关键词 | 扩展替换词 |
|---|---|
| edge states | boundary modes, edge channels, chiral edge, helical edge |
| domain wall | stacking boundary, stacking soliton, AB/BA interface, DW |
| topological | valley-protected, Chern number boundary, QVH |
| TBG | twisted bilayer, mTBG, minimally twisted, small-angle graphene |

→ 输出：扩展搜索的新发现论文

### Step 5：核心作者追踪

逐个查询以下作者 2020–2026 年的全部 arXiv 论文，筛选 edge state 相关者：

| 作者 | arXiv 查询 URL |
|---|---|
| **Lin He** (BNU) | `https://arxiv.org/search/?searchtype=author&query=He,+L` |
| **Francisco Guinea** | `https://arxiv.org/search/?searchtype=author&query=Guinea,+F` |
| **Mikito Koshino** | `https://arxiv.org/search/?searchtype=author&query=Koshino,+M` |
| **Allan MacDonald** | `https://arxiv.org/search/?searchtype=author&query=MacDonald,+A+H` |
| **Pablo Jarillo-Herrero** | `https://arxiv.org/search/?searchtype=author&query=Jarillo-Herrero,+P` |
| **Feng Wang** | `https://arxiv.org/search/?searchtype=author&query=Wang,+Feng` |
| **Peter Rickhaus** | `https://arxiv.org/search/?searchtype=author&query=Rickhaus,+P` |
| **Cory Dean** | `https://arxiv.org/search/?searchtype=author&query=Dean,+C+R` |
| **Klaus Ensslin** | `https://arxiv.org/search/?searchtype=author&query=Ensslin,+K` |
| **Jinhai Mao** | `https://arxiv.org/search/?searchtype=author&query=Mao,+Jinhai` |

→ 输出：每个作者的相关新论文

### Step 6：综述挖掘

从以下综述的参考文献中提取 edge state / domain wall 相关论文：

| 综述 | 搜索关键 |
|---|---|
| Andrei & MacDonald, Nat. Mater. 19, 1265 (2020) | "domain wall", "edge", "boundary", "topological" |
| Balents et al., Nat. Phys. 16, 725 (2020) | 同上 |
| Kennes et al., Nat. Phys. 17, 155 (2021) | 同上 |

→ 输出：综述引用的 edge state 相关论文（注意与已有结果去重）

### Step 7：引文图谱补漏

使用 Connected Papers 或 Semantic Scholar 图谱功能：
- 输入 `arXiv:1308.XXXX` (San-Jose & Prada 2013)
- 输入 `arXiv:1802.07317` (Rickhaus 2018)
- 输入 `arXiv:2204.XXXXX` (Zheng 2022)

→ 输出：图谱中孤立的、可能的遗漏论文

---

## 最终汇总格式

搜索完成后，按以下格式整理结果：

### 实验论文

| # | 年份 | 作者 | 标题 | 期刊 | arXiv ID | 核心贡献 |
|---|---|---|---|---|---|---|
| E1 | ... | ... | ... | ... | ... | ... |

### 理论论文

| # | 年份 | 作者 | 标题 | 期刊 | arXiv ID | 核心贡献 |
|---|---|---|---|---|---|---|
| T1 | ... | ... | ... | ... | ... | ... |

### 时间线图

```
2013 ── 理论奠基
  ├── San-Jose & Prada (螺旋网络)
  └── ...
2018 ── 实验突破
  ├── Huang (STM THS)
  ├── Rickhaus (FP+AB 输运)
  └── ...
2019–2021 ── 巩固与扩展
  ├── Yoo (晶格重构+畴壁输运)
  ├── Xu (巨幅 AB)
  └── Verbakel (FT-STM 谷保护)
2022–2024 ── 新方向
  ├── Zheng (PLL+Kagome)
  ├── Mahapatra (QH 干涉仪)
  └── Hou (TZM 理论裁决)
2025–2026 ── ?
  └── (本次搜索填补)
```

### 标记

- ★ = 必读（领域奠基或突破性工作）
- 📄 = 已有笔记（标注文件路径）
- ⚡ = 新发现（此前知识库未收录）
- 🔮 = 预印本（未经同行评审）
- ❓ = 需进一步确认相关性

---

*任务创建日期：2026-08-06 | 基于 paper_search_workflow.md 模板*
