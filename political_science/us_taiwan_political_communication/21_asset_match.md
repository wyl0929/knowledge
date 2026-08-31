<!--
Field: us_taiwan_political_communication
Mode: full_onboarding
Domain archetype: social_science
Created date: 2026-08-30
-->

# 21 Asset Match / 用户资产匹配

Last updated: 2026-08-30

## 使用说明

本文件把 gap table 中的机会和用户真实资产对齐，避免只因为方向热门就生成不可执行项目。用户的默认 profile 是计算物理研究者：**计算/编程/写作资产强，领域内数据资产与编码人力均为 UNKNOWN_USER_ASSET**——本文件按此现实匹配，不替用户假设资源。

Field / 领域：us_taiwan_political_communication

## Asset-to-Gap Matrix / 资产-缺口矩阵

| User asset / 用户资产 | Evidence of maturity / 成熟度证据 | Matching gap / 匹配缺口 | Why it matches / 匹配原因 | Missing resource / 缺失资源 | Risk / 风险 | Next action / 下一步 |
|---|---|---|---|---|---|---|
| Python 数据管线（采集/清洗/建模） | profile：Python 熟练 | G6 数据可得性探测、G2 流向检验、G3 固定效应建模 | 全部是脚本化任务，无特殊硬件需求 | 数据入口（X 子集、Yahoo 快照） | 平台反爬/许可限制 | 先跑 23 MVP 第 1 周三路探测 |
| LLM API 调用经验（可迁移） | profile：无直接证据（NEEDS_VERIFICATION），但 Python 基础足以快速上手 | G1/G4 编码管线 | LLM 批量编码是唯一经济可行的大规模编码路径 | API 预算、目标期刊接受政策 | 模型漂移、提示敏感 | MVP 内试跑编码 v0.1 并做人机信度 |
| LaTeX/中文学术写作 | profile：LaTeX 熟练 | 全部 gap 的产出端 | 论文/开题写作无瓶颈 | 目标期刊/学位要求确认 | — | 与用户确认目标载体 |
| 既有 political_science field packs | knowledge 树 4 个包 | G3 政策背景（战略模糊等） | 政策话语背景已在包内 | — | 概念漂移（媒体框架≠政策话语） | 引用 11/12 号概念边界防止混用 |
| 领域文献资产（本包 14 号） | 两轮系统搜索（2026-08-30） | G1/G2/G3/G7 的"已做部分"界定 | 缺口表述有据可查 | 经典文献精读尚未做 | 条目级≠论点级证据 | 优先精读 Wang & Guo 2018、Tan 2026、Amrullah 2023 |
| X/Twitter 数据访问 | UNKNOWN_USER_ASSET | G6 | 决定 X 侧取样路径 | 订阅/预算/机构授权 | 全部 X 侧结论依赖它 | 用户确认资产（问题 1） |
| 新闻档案访问（NewsBank/LexisNexis/机构图书馆） | UNKNOWN_USER_ASSET | G6 | 决定 Yahoo 侧取样路径 | 机构订阅 | Wayback 密度不足时的备份 | 用户确认资产（问题 2） |
| 人工编码人力（用户本人或编码员） | UNKNOWN_USER_ASSET | G1/G4 信度锚定 | 人-人 α 需要至少两名编码员 | 编码员或用户时间 | 单编码员无法报信度 | 用户确认（问题 3） |

## Strong Matches / 强匹配

- Gap / 缺口：G6（数据可得性探测）
- Plain-language fit / 人话匹配解释：第一周就能用 Python 脚本把"能拿到什么数据"这个总闸门问题变成三个小实验（Wayback CDX 密度、Media Cloud 收录、第三方 API 试采），不需要领域积累。
- Assets / 资产：Python 熟练 + 本包 15 号工具清单。
- Why this could work / 为什么可行：全部探测接口免费或有试采，失败成本低；结果无论正负都直接改变 P1 设计。
- Minimal proof / 最小证明：一个事件的 CDX 快照计数脚本跑通并产出密度表。

- Gap / 缺口：G1+G4（框架编码管线）
- Plain-language fit / 人话匹配解释：编码手册 v0.1 + LLM 批量编码 + 人工子样本信度，是"写 prompt、跑管线、算 α"的计算任务，正落在用户技能区。
- Assets / 资产：Python + LLM API（可快速上手）。
- Why this could work / 为什么可行：方法学全部有公开范本（Matthes & Kohring、Gilardi 2023）；领域新意来自语料而非方法。
- Minimal proof / 最小证明：100 条佩洛西事件文本产出可读的框架分布 + α ≥ .67（探索阈值）。

## Weak or Misleading Matches / 弱匹配或误导性匹配

- Direction / 方向：把计算物理的数值模拟/集群资产直接用于政治传播研究
- Plain-language warning / 人话提醒：SLURM 集群、MPI、TBPM 在本领域没有用武之地；不要因为"有算力"就选大规模训练类方法（如自训大模型做帧检测）。
- Why it looks attractive / 为什么看起来吸引人：用户对"大规模计算"有肌肉记忆，容易高估算力在本领域的边际价值。
- Why it may fail / 为什么可能失败：政治传播的瓶颈是数据获取、编码效度与领域判断，不是 FLOPs；自训模型还引入不可复现与立场偏差风险。
- Stop condition / 停止条件：若发现自己花时间在"优化模型/加大算力"而非"取样与编码效度"，立即回到 23 MVP 的周计划。

- Direction / 方向：用平台文本直接替代民意数据（把 X 话语当"美国公众舆论"）
- Plain-language warning / 人话提醒：这正是本包概念契约（C2）禁止的越界；Amrullah 2023 类研究标题即此写法。
- Why it looks attractive / 为什么看起来吸引人：文本数据便宜、量大、即时，民调昂贵低频。
- Why it may fail / 为什么可能失败：X 用户结构偏差 + 算法过滤 + 机器账号污染，文本分布与态度分布可以方向相反；审稿人一击即破。
- Stop condition / 停止条件：结论中出现"美国公众认为"类表述即改写为"平台文本中……"。

## Collaboration Needs / 合作需求

| Need / 需求 | Why needed / 为什么需要 | Possible collaborator / 可能合作者 | Urgency / 紧急度 | Status / 状态 |
|---|---|---|---|---|
| 框架编码的第二编码员（人-人信度） | G4 信度报告的硬要求 | 同校社科/传播学学生；或导师组内编码员 | high | UNKNOWN_USER_ASSET |
| 涉台/涉美政治传播的领域把关人（codebook 与框架命名的专家复核） | 防止归纳框架换名、防概念越界 | 政治传播/国际关系方向导师或合作者 | high | UNKNOWN_USER_ASSET |
| X 历史数据访问（API 预算或第三方数据许可） | G6 X 侧取样的硬约束 | 机构数据订阅；CMU CASOS 数据集（公开部分）；Sorsa 类商业 API | high | UNKNOWN_USER_ASSET |
| 目标载体确认（学位论文 / 期刊投稿，目标期刊） | 决定 LLM 编码接受政策与深度要求 | 用户/导师 | medium | NEEDS_VERIFICATION |
