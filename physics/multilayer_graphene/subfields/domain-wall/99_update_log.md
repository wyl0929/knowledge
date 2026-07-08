<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-07 17:34:03
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-07 17:34:04
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/multilayer_graphene/subfields/domain-wall/99_update_log.md
 * @Description  :
-->
<!--
 * @Author       : AI-generated (research_onboarding_skill, subfield)
 * @Date         : 2026-07-07
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/domain-wall/99_update_log.md
 * @Description  : Domain Wall 实验研究 — 子方向更新日志
-->

# 99 Update Log / 更新日志 — Domain Wall 实验

Last updated: 2026-07-08

---

## 2026-07-08: 论文笔记迁移 + 父 pack 英文重命名

- **父 pack 重命名**：`多层石墨烯：转角与非转角体系/` → `multilayer_graphene/`
- **子领域重命名**：`domain-wall-experiments/` → `domain-wall/`
- **论文笔记迁入**：
  - `paper_review_hou2024_prb.md` — Hou et al. (2024) PRB 精读报告
  - `paper_review_rickhaus2018_nanolett.md` — Rickhaus et al. (2018) Nano Lett. 阅读笔记
  - 原存放于父 pack 临时目录 `refer/`（已删除），现按 `research_onboarding_skill` v1.2 规范移至子领域目录
- **更新**：
  - `14_paper_registry.md` — 新增「mTBG 畴壁输运」分类（DW-m1–m4）
  - 父级 `14_paper_registry.md` DW3/DW7 链接同步修复

---

## 2026-07-07: 子方向初始化 — graphene domain wall 实验文献扫描

- **来源**: 用户要求检查 graphene 体系 Domain wall 的实验研究（两层/三层/多层），基于 research_onboarding_skill 的 quick_scan 模式
- **父 pack**: `knowledge/physics/multilayer_graphene/`
- **新建文件**:
  - `USER_BRIEF.md` — 调研需求记录
  - `01_research_overview.md` — 实验综述（arXiv 验证后重写）
  - `14_paper_registry.md` — 已验证关键文献详细总结
  - `99_update_log.md` — 本文件

- **迁移历史**:
  - 原始文档 `DW/docs/experimental_domain_wall_survey.md`（含大量未核实条目）已删除
  - DW 项目其他修改（`DW/docs/log.md`, `DW/STATUS.md`）已全部撤销

- **关键发现**:
  - **7 篇论文经 arXiv + DOI 验证为真实存在**：Ju 2015 Nature, Li 2016 Nat. Nanotech., Jiang 2017 Nano Lett., Shimazaki 2015 Nat. Phys., Mania 2019 Commun. Phys., Li S.-Y. 2016 (STM), Hsu 2020 Sci. Adv.
  - **8 条原始问卷中的条目标记为错误/不存在**——AI 训练记忆的文献列举不可靠，必须交叉验证
  - **双层 LSW 畴壁实验已成熟**（2015–2019 期间 5 篇顶刊实验论文）
  - **三层畴壁实验完全空白**——arXiv 未找到任何 ABC 或 ABA 三层畴壁的输运或 STM 实验
  - **EFW 实验几乎空白**——分裂栅加工难度导致
  - **DW 项目的三层 LSW 计算 + 磁场下 $\sigma_{xy}$ 计算可能填补实验空白**

- **NEEDS_VERIFICATION**:
  - 原始问卷中 8 条错误条目（Yin 2014/2015, Rickhaus 2018, Kim 2019, Sunku 2018, Huang 2018, McGilly 2020, Edelberg 2022）——用户应在 Web of Science 按作者名搜索确认
  - Li S.-Y. 2016 论文的正式发表状态（arXiv 可见但未见正式发表）
  - 三层畴壁"实验空白"的判断 —— 若有近年新实验工作被 arXiv 遗漏，需用户补充

- **注**: 本子方向为纯文献扫描，不生成 gap table 或 project candidates
