<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-19 06:13:58
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-11
 * @FilePath     : /.agents/home/wyl/project/knowledge/README.md
 * @Description  : 领域知识包总目录
-->

# 领域知识包 (Field Packs) 总目录

> 最后更新: 2026-08-11

本目录存放所有通过 `research_onboarding_skill` 生成的领域文献研究包 (field packs)。

---

## 结构

```
knowledge/
├── README.md                    ← 本文件
├── UPDATE_LOG.md                ← 工作区变更日志
├── physics/                     ← 物理领域
│   ├── 量子霍尔效应/
│   ├── 强关联效应/
│   └── 三层和多层转角石墨烯/
├── philosophy/                  ← 哲学/思想领域
│   ├── mental_causation_closure/
│   ├── power_reductionism/
│   └── reductionism/
├── Economics/                   ← 经济/社会科学领域
│   └── macroeconomics/
├── political_science/           ← 政治学领域
│   ├── fundamentals/            ← 政治学入门——基本概念与研究范式
│   ├── us_two_party_politics/   ← 美国两党政治初探
│   │   └── subfields/
│   │       └── dsa_2026_wave/   ← DSA 2026 浪潮（子方向）
│   ├── central_local_relations/ ← 央地矛盾、集权与分权的治理逻辑
│   └── corporatism/             ← 法团主义（从央地矛盾 QA 派生）
├── systems_science/             ← 系统科学领域
│   ├── 00-12, 90, 99            ← 核心文档
│   ├── case/                    ← 案例研究 (01-08)
│   └── USER_BRIEF.md
└── computer_science/            ← 计算机/编程领域
    ├── cpp_for_tbplas/          ← C++ 学习 (面向 tbplas 源码)
    └── Image_Processing/        ← 图像处理 (空壳占位)
```
```

---

## 编号体系

每个 field pack 使用 `research_onboarding_skill` v1.0 统一编号：

| 编号段 | 层次 | 说明 |
|--------|------|------|
| `00-02` | 阅读与判断层 | beginner guide, overview, frontier compass |
| `10-17` | 证据与领域层 | self_inventory, term_disambiguation, field_map, actor_map, paper_registry, tool_registry, metrics, claims_ledger |
| `20-23` | 研究推进层 | gap_table, asset_match, project_candidates, mvp_plan |
| `90-99` | QA 与维护层 | QA, update_log |
| — | 特殊 | `USER_BRIEF.md`（本次需求说明）, `README.md`（包索引） |

---

## 各包状态

### physics/

| 包名 | 模式 | Domain Archetype | 创建日期 | 状态 |
|------|------|:---:|------|------|
| 量子霍尔效应 | quick_scan | science_technical | 2026-06-10 | ✅ 已填充 |
| 强关联效应 | quick_scan | science_technical | 2026-06 | ✅ 已填充 |
| 三层和多层转角石墨烯 | full_onboarding | science_technical | 2026-06 | ✅ 已填充，含 subfields/ |

### philosophy/

| 包名 | 模式 | Domain Archetype | 创建日期 | 状态 |
|------|------|:---:|------|------|
| mental_causation_closure | orientation | humanities_cultural | 2026-06 | ✅ 已填充 |
| power_reductionism | orientation | humanities_cultural | 2026-06-19 | ✅ 已填充 |
| reductionism（还原论） | orientation | humanities_cultural | 2026-07-17 | ✅ 已填充，含 subfields/power_reductionism_as_case/ |

### Economics/

| 包名 | 模式 | Domain Archetype | 创建日期 | 状态 |
|------|------|:---:|------|------|
| macroeconomics | quick_scan | social_science | 2026-06-19 | ✅ 已填充 |

### political_science/

| 包名 | 模式 | Domain Archetype | 创建日期 | 状态 |
|------|------|:---:|------|------|
| 美国两党政治初探 | orientation | social_science | 2026-07-03 | ✅ 已填充，含 subfields/dsa_2026_wave/ |
| 央地矛盾、集权与分权的治理逻辑 | quick_scan | social_science | 2026-07-08 | ✅ 已填充，种子文档为 conflict.md |
| 法团主义（Corporatism） | quick_scan | social_science | 2026-07-11 | ✅ 已填充，从央地矛盾 QA 派生 |

### systems_science/

| 包名 | 模式 | Domain Archetype | 创建日期 | 状态 |
|------|------|:---:|------|------|
| 控制论与系统工程 | full_onboarding | science_technical | 2026-06-21 | ✅ 核心文档 + 8 个 case study (case/01-08) + debug-workflow skill |

### computer_science/

| 包名 | 模式 | Domain Archetype | 创建日期 | 状态 |
|------|------|:---:|------|------|
| cpp_for_tbplas | project_incubation | science_technical | 2026-06-22 | ✅ MVP 实验计划已生成，待执行 |
| Image_Processing | — | — | — | ⏳ 空壳占位，未初始化 |

---

## 与计算项目的关系

| Field Pack | 关联计算项目 |
|------------|-------------|
| 量子霍尔效应 | TBG, TMBG, MG (Hall conductivity 计算) |
| cpp_for_tbplas | MG (tbplas C++ 源码阅读与修改) |
| 控制论与系统工程 | 量子霍尔效应 (QA-001: Kubo-Bastin NaN 调试案例分析) |
| 三层和多层转角石墨烯 | TBG, TMBG, TDBG |
| 强关联效应 | (待建立) |

---

## 维护

- 新建 field pack 使用 `research_onboarding_skill/scripts/init_field_pack.py --output /home/wyl/project/knowledge/...`
- 更新后请同步修改本文件和 `UPDATE_LOG.md`
