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

Last updated: 2026-07-15

---

## 2026-07-15: 三篇单 LSW 输运实验精读笔记

- **新建文件**:
  - `paper_review_ju2015_nature.md` — Ju et al. (2015) Nature 精读（s-SNOM 首次可视化畴壁 + 等离激元证明谷-动量锁定）
  - `paper_review_li2016_natnanotech.md` — Li et al. (2016) Nat. Nanotech. 精读（首个栅控静电 DW 电学输运实验，零场 $L_k \sim 100$ nm，$B=8$T 恢复弹道性）
  - `paper_review_mania2019_communphys.md` — Mania et al. (2019) Commun. Phys. 精读（折叠 BLG，零场量子电阻 $h/4e^2$，$L_{MFP} \sim 20$ μm）
- **更新文件**: `14_paper_registry.md` — P1/P2/P5 添加精读报告链接
- **关键发现**:
  - Ju 2015 是光学探针（非直接电学输运），证明谷极化但不测 $\sigma/R$
  - Li 2016 是静电 DW（栅控 $V=0$ 线），非结构 AB/BA 边界——与 Ju 2015/Mania 2019 的 DW 类型不同
  - Mania 2019 的折叠 DW 给出 $L_{MFP} \sim 20$ μm，比 Li 2016 高 200 倍——DW 锐度是弹道输运的决定性因素
  - 三篇各自代表了单 LSW 实验的不同路径：光学→静电→折叠，DW 质量递进
- **来源**: Li 2016 arXiv:1509.03912 全文（39 页）+ Mania 2019 arXiv:1901.08178 全文（26 页）+ Ju 2015 registry 条目

---

## 2026-07-15: Zhang 2024 笔记追加理论-实验关联附录

- **更新文件**: `paper_review_zhang2024_arxiv.md`
- **新增**: 附录 B — 理论计算与实验的逻辑关联（~100 行）
  - 实验 → 唯象拟合 → 微观机制三层推理完整追踪
  - 7-LSW vs 3-LSW 的 MC 行为差异的因果链映射表
  - Bloch 计算如何解释 $L_\phi(\bar{D})$ 指数增长、$\Delta G$ 增加、MC 极小值深度
  - 核心概念：$\bar{D}$ 通过 $E_g$ → $x_0 \propto 1/E_g$ → 波函数重叠 → 谷内背散射 → 弱局域化
  - 三个可检验理论预言的实验验证状态
  - 模型关键参考文献（Li-Morpurgo-Buttiker-Martin 2010, Jung-Zhang-Qiao-MacDonald 2011 等）
- **来源**: 正文 §4 全文提取（arXiv PDF pdftotext 解析）

---

## 2026-07-15: Zhang 2024 论文精读 + CVD LSW 新类别

- **新建文件**: `paper_review_zhang2024_arxiv.md` — Zhang et al. (2024) 8 节精读报告
  - arXiv:2406.06867（2024-06-11），期刊状态 NEEDS_VERIFICATION
  - 核心发现：CVD 双层石墨烯中两种 LSW 构型（分离 vs 紧密堆积束），后者展现电场可调磁电导
  - 作者阵容：UPenn（Johnson/Mele/Drndic/Kikkawa）+ UC Berkeley（Feng Wang）+ HKUST（Luo）
  - 阅读笔记中文撰写，遵循 8 节模板
  - 多处标 NEEDS_VERIFICATION（仅基于 arXiv 摘要，未获全文 PDF）
  - 附录了与 Mahapatra 2022 的详细体系对比表
- **更新文件**: `14_paper_registry.md`
  - 新增「CVD 外延双层石墨烯 LSW 束输运」分类
  - 新增 [DW-c1] Zhang et al. (2024) 条目 + 精读链接
  - 三种畴壁平台对比（CVD LSW / 非转角畴壁 / mTBG 畴壁）
- **Zotero Key**: `DGAFNKRR`，DOI 待确认

---

## 2026-07-15: Mahapatra 2022 笔记追加 AB 振荡附录

- **更新文件**: `paper_review_mahapatra2022_nanolett.md`
- **新增**: 附录 A — Aharonov-Bohm (AB) 振荡
  - AB 效应定义、历史（Aharonov & Bohm 1959）
  - 相位积累公式 $\Delta\varphi = 2\pi\Phi/\Phi_0$ 与磁通量子 $\Phi_0 = h/e$
  - 揭示的物质基本性质：矢势实在性、量子非定域性、Berry 相位、拓扑保护
  - AB vs FP 振荡对照表（含石墨烯特殊性）
  - AB vs AAS 振荡（$h/e$ vs $h/2e$ 周期）
  - 石墨烯中 Dirac 费米子的 Berry 相位 $\pi$ 对干涉条件的影响
  - QH 干涉测量中 AB 效应的核心角色（编织相位探测）
  - 参考原始文献：Aharonov-Bohm 1959, Chambers 1960, Webb 1985, Berry 1984, AAS 1981, Beenakker 1991

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
