<!--
Field: 平面设计
Mode: quick_scan
Domain archetype: mixed
Created date: 2026-08-30
-->

# 10 Self Inventory / 用户背景快照

Last updated: 2026-08-30

## 使用说明

本文件是当前 field pack 使用的 profile 快照。它记录"这次生成时默认假设用户是谁、有没有研究资产、是否需要资产匹配"。它不同于 `USER_BRIEF.md`：profile 是长期背景，brief 是本次任务的写作与调研要求。

Field / 领域：平面设计

Depth mode / 深度模式：quick_scan

## Profile source / 背景来源

/home/wyl/.agents/skills/research-onboarding/profiles/default_user_profile.md

## Snapshot date / 快照日期

2026-08-30

## Profile snapshot / Profile 快照

```markdown
# Default User Profile / 默认用户背景
- 身份：计算凝聚态物理研究者
- 学科背景：物理学、计算物理
- 当前阶段：研究生/博士后（进行中）
- 主要训练：凝聚态理论、数值模拟
- 主要研究方向：石墨烯及二维材料电子性质计算、TBPM 大规模量子输运模拟
- 已有代码和工具：graphene.py、test_mpi.py、TBPM/DOS 计算、submit.py、SLURM 脚本
- 方法能力：理论建模（中等）、数值模拟（熟练）、Python/Shell/Git/SLURM（熟练）、matplotlib/LaTeX（熟练）
- 机器学习 / 控制优化：NEEDS_VERIFICATION
```

## 用户研究背景

- 身份与学科背景：计算凝聚态物理研究者（研究生/博士后），与平面设计**高度正交**——本次是兴趣/实践型进入，不是科研方向延伸。
- 主要研究方向：二维材料电子性质、量子输运模拟。与设计无直接交叉。
- 已有领域知识：无系统设计训练；但有很强的"参数化/可复现"思维习惯（对后续走程序化设计是隐性优势）。
- 数学、理论、实验或写作基础：数学与数值扎实，可视化（matplotlib）熟练，LaTeX 排版熟练（对字体与版式有朴素敏感性）。

## 用户已有工具或材料

| 工具 / 材料 | 类型 | 位置 | 成熟度 | 相关性 | 备注 |
|---|---|---|---|---|---|
| Python | code | 工作区 | mature | high | 程序化壁纸的核心引擎（Pillow/cairo 待装） |
| matplotlib | tool | 环境 | mature | medium | 可视化经验可迁移到几何构图 |
| LaTeX | tool | 环境 | mature | medium | 字体/行距/版式的朴素直觉来源 |
| Git / Shell | tool | 环境 | mature | low | 版本管理设计脚本 |
| SLURM 集群 | hardware | h3clogin | mature | low | 与本地壁纸生成无关，基本不用 |
| 设计软件（Figma/AI/PS） | tool | 未安装 | — | medium | 手工方案可选，非必须（NEEDS_VERIFICATION 是否可用） |

## 本次调用中的特殊覆盖项

本次用户明确给出"平面设计入门 + 壁纸设计方案"，与默认 profile 的科研方向不同。这是**兴趣/实践型进入**，不是科研选题。

| 覆盖项 | 来源 | 对 field pack 的影响 | Last updated |
|---|---|---|---|
| 定位为兴趣/实践型，非科研延伸 | user input | 不强行产出学术研究 gap；gap 与 project 写成"学习/实践缺口与可执行设计方向" | 2026-08-30 |
| 聚焦"理论基础 + 桌面壁纸设计方案"双主线 | user input | 所有理论都映射到"一张壁纸的某个设计决策"；project candidates 以壁纸方案为核心 | 2026-08-30 |
| 默认 profile 的科研资产（集群/量子计算）与设计正交 | profile 事实 | 资产匹配不做科研关联，只保留"Python→程序化设计"这一条真实桥梁 | 2026-08-30 |

## Claims to Verify / 待核验判断

| 判断 | 为什么重要 | 需要来源 | 状态 |
|---|---|---|---|
| 用户是否已安装 Pillow/cairo 等绘图库 | 决定"程序化壁纸"第一周动作能否立刻落地 | 本地环境检查 | NEEDS_VERIFICATION |
| 用户是否可用 Figma/Illustrator | 决定手工方案 vs 纯代码方案的优先级 | 用户确认 / 本地检查 | NEEDS_VERIFICATION |
| 用户的具体审美偏好（冷/暖、极简/繁复） | 决定壁纸配色与风格方向 | 用户确认 | NEEDS_VERIFICATION |
