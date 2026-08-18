<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-17 20:12:21
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-17 20:12:21
 * @FilePath     : /.agents/home/wyl/project/knowledge/sociology/social_survey_methods/USER_BRIEF.md
 * @Description  :
-->
<!--
Field: 社会调研方法论——从日常对话到结构化判断
Mode: quick_scan
Domain archetype: social_science
Created date: 2026-08-17
-->

# USER BRIEF / 本次需求说明

Last updated: 2026-08-17

## 这份文件的作用

这里保存用户对本 field pack 的特殊要求。内容可以直接用自然语言书写。
生成或更新本包中的任何主体文档前，agent 都必须先读取本文件。

本文件与其他文件的区别：

- `10_self_inventory.md`：记录本次使用的 profile 或用户背景快照；
- `USER_BRIEF.md`：记录本次调研的目标、重点、写作方式和回避事项；
- `90_QA.md`：保存后续自由讨论，默认不自动成为持续要求；
- `99_update_log.md`：保存修改历史。

## 路由决策

```yaml
detected_mode: quick_scan
selected_profile: default_user_profile（覆盖项：不结合计算物理背景，定位为跨学科知识整合者）
domain_archetype: social_science
confidence: high
```

## 用户原始需求

> 这里有一份关于社会调研的讨论，社会学内容应该放在政治学 pack 下还是应该新建一个新的 pack？
> 新建一个社会学的一级目录，将社会调研相关内容作为其下的一个 field。

## 当前有效要求

- 在 `knowledge/` 下新建社会学一级目录 `sociology/`，本 pack 为其下第一个 field pack，与 `political_science/` 平级。
- 以已移动至本目录的种子讨论文档 `seed_discussion_20260817.md` 为起点，建立"社会调研方法论"领域包。
- 种子文档的核心诉求：将离散、发散、高噪声的日常对话，转化为对地方经济政治状况的可靠判断。
- 内容围绕两条主线展开：社会学理论透镜（符号互动论、常人方法学、社会分层与流动、社会资本与信任）与调研工程管线（采样、降噪、编码、验证、推断）。
- 种子文档第 6 节提出的 6 个后续深入方向（问题库设计、编码体系、矛盾信息处理、报告模板、伦理边界、半定量化）作为本包的 gap 与项目候选起点。

## 内容侧重点

- 希望重点展开：社会调研方法论的学科定位（社会学与工程学的分工）、四大理论透镜的具体调研用法、调研操作流程各环节的机制解释。
- 希望简略处理：与物理背景的强行类比；过度形式化的统计推导。
- 暂时不需要涉及：对当代中国政治的具体规范性评价；具体调研执行过程中的敏感信息操作细节。

## 写作与呈现偏好

- 语言与风格：主体中文，关键术语初次出现附英文；先讲直觉，再讲术语；把分类写成谱系与 trade-off，而非百科清单。
- 期望深度：适合有学术训练但无社会科学专业背景的读者，能建立基本地图、边界感与可执行的操作起点。
- 是否需要公式 / 流程 / 作品例子 / 图表：适当使用流程图与比较表格；给出经典学者/著作作为锚点。
- 是否需要阅读清单：是，在 `14_paper_registry.md` 与 `00_beginner_guide.md` 中给出入门阅读路径。
- 是否需要派生子方向：暂不需要，但保留后续派生可能（如半定量化、编码工具链）。

## 与父方向的继承关系

本包为 `sociology/` 一级目录下的独立 field pack，不继承自任何父包。与 `political_science/` 下的各包（fundamentals、central_local_relations、corporatism、us_two_party_politics）为平行关系；种子文档最初存放于 `political_science/` 根目录，现已移入本包。

## 修改记录

| 日期 | 修改内容 | 来源 |
|---|---|---|
| 2026-08-17 | 初始化本次需求说明 | initial user prompt |
