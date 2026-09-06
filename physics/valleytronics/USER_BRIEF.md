<!--
Field: 量子谷霍尔效应与谷电子学（Quantum Valley Hall Effect & Valleytronics）
Mode: full_onboarding
Domain archetype: science_technical
Created date: 2026-09-02
-->

# USER BRIEF / 本次需求说明

Last updated: 2026-09-02

## 这份文件的作用

这里保存用户对本 field pack 的特殊要求。生成或更新本包中的任何主体文档前，agent 都必须先读取本文件。

本文件与其他文件的区别：

- `10_self_inventory.md`：记录本次使用的 profile 或用户背景快照；
- `USER_BRIEF.md`：记录本次调研的目标、重点、写作方式和回避事项；
- `90_QA.md`：保存后续自由讨论，默认不自动成为持续要求；
- `99_update_log.md`：保存修改历史。

## 用户原始需求

> 用 `/research-onboarding`（full_onboarding）开一个新 L1 field pack，覆盖**量子谷霍尔效应（QVH）/ 谷电子学（valleytronics）**的通用理论，服务现有 **TBG** 与新增 **TMBG** 两个方向的畴壁/谷物理。
>
> 触发背景（前一会话已完成的"第一层修正"）：QVH 已被判定**不属量子霍尔效应**——总霍尔电导 $\sigma_{xy}=0$（时间反演 $C_K+C_{K'}=0$），无量子化平台；`Quantum_Hall_Effect` field 已把它从子方向移出、标注为相邻领域，并补了"QHE ≠ QVHE"边界。QVH 理论目前散落在 `twisted_bilayer_graphene/note/shared/physics/`，没有独立 field pack；TMBG（twisted monolayer–bilayer / rhombohedral 三层，ABC/ABA 畴壁，谷陈数 $C_v=\pm3$）的畴壁/谷物理是 QVH 的泛化，但 TBG field 不会去覆盖 trilayer。

## 当前有效要求

- **scope 是"现象/理论"层**：谷陈数、谷输运、谷保护的通用理论；不是"材料平台"层（moiré、魔角、畴壁制备属 TBG/TMBG platform field）。
- **服务对象**：TBG（AB/BA 双层畴壁）+ TMBG（ABC/ABA 三层畴壁）+ 单层/TMD 的一般谷物理。
- **模式**：`full_onboarding`（有明确 seed + 明确服务对象，非从零 quick_scan）。
- **种子论文**：从 `twisted_bilayer_graphene/14_paper_registry.md` 的 T1–T39 / E1–E18 中筛 QVH 相关的，**不重新搜索**；PDF 已在 `twisted_bilayer_graphene/reference/pdfs/`，精读笔记已在 `note/theory/` 与 `note/experiments/`。
- **已有资产（引用锚点，不复制）**：`[PHY-BERRY]`（谷陈数/helical vs chiral/证据阶梯）、`[PHY-QPI]`（谷保护软保护机制）、`[PHY-GATE]`（STM 静电学）、`[PHY-EF]`（费米能/band bending），以及 E01/E09/E13 精读的 worked example。
- **必须先钉死的术语边界**：QVH ≠ QHE；helical ≠ chiral；存在性 ≠ 拓扑保护；谷保护是软保护；谷陈数约定（见下）。
- **必须核的开放问题**：**C_v 约定不一致**（Huang 2018 "unit magnitude" vs `[PHY-BERRY]` 写 $C_v=\pm2$）；tMBG（ABC/ABA）$C_v=\pm3$ 与畴壁通道数对应；trilayer 谷保护是否同样"软"。

如果当前没有额外特殊要求，按所选 mode、profile 与 domain archetype 的默认规则执行。

## 内容侧重点

- **希望重点展开**：谷陈数（valley Chern number）的统一分类框架、谷输运（valley Hall conductivity / valley current）、谷保护的机制与证据阶梯、从双层到三层/TMD 的泛化。
- **希望简略处理**：moiré 晶格重构、魔角关联态、BM 连续模型的完整推导（这些属 TBG/强关联 platform field，仅引用不展开）。
- **暂时不需要涉及**：FQHE 级多体方法（DMRG/精确对角化）、自旋电子学器件化细节、量子霍尔效应的朗道量子化/分数态本体。

## 写作与呈现偏好

- **语言与风格**：主体中文，关键英文术语出现时附英文；先直觉后术语；连续可读。
- **期望深度**：研究级——重要方法给出机制、公式或流程、具体例子、比较关系和研究边界，不只概括。
- **是否需要公式 / 流程 / 图表**：需要核心公式（谷陈数、谷霍尔电导、QPI 散射矢量）与 ASCII 谱系图；不需要作品/案例。
- **是否需要阅读清单**：是（`14_paper_registry.md` 给推荐阅读顺序）。
- **是否需要派生子方向**：暂不派生；把 TMBG 三层泛化作为边界与 gap 显式标注，指向 `multilayer_graphene/subfields/tmbg/` 与 `twisted_bilayer_graphene`。

## 与相邻 field 的继承关系

本文件属于**独立 L1 field pack**（非子方向包），但逻辑上从以下 field 的相邻边界派生：

- **继承的上游理论锚点**：`twisted_bilayer_graphene/note/shared/physics/`（[PHY-BERRY]/[PHY-QPI]/[PHY-GATE]/[PHY-EF]）与 `Quantum_Hall_Effect`（QHE ≠ QVHE 边界、`subfields/tbplas_conductivity` 的 Kubo-Bastin 能力）。
- **本 field 新增要求**：把散落的 QVH 理论收拢为一个独立的"现象/理论"field，钉死它与 QHE（不同族）、QSHE（同族不同内部量子数）、TBG/TMBG（下游平台）的关系。
- **本 field 覆盖要求**：TMBG 三层畴壁/谷物理——TBG field 的 registry 只覆盖 AB/BA 双层，三层泛化由本 field 显式纳入（指向 Chen 2021 / Phong 2026 待核）。

## 修改记录

| 日期 | 修改内容 | 来源 |
|---|---|---|
| 2026-09-02 | 初始化本次需求说明（full_onboarding，valleytronics） | handoff 交接表 + init_field_pack.py |
