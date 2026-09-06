<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-05-24 15:44:56
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-25
 * @FilePath     : /knowledge/systems_science/case/12_case_study_context_status_relation.md
 * @Description  : 案例研究 — CONTEXT.md 与 STATUS.md 的互补关系（参考模型 vs 状态观测器）
-->

# 案例研究: CONTEXT.md 与 STATUS.md 的互补关系 — 参考模型 vs 状态观测器

> **领域标签**: 系统科学 · 控制论 · 知识管理 · 文档工程
> **时间跨度**: 2026-05-24
> **来源项目**: `AI_test/docs/comments/relation_context_status.md`（2026-08-25 随 AI_test 结构调整迁入本案例）
> **关联案例**:
>   - `11_case_study_six_doc_system_tiered_response.md` — 六文档体系（本案例聚焦其中 CONTEXT/STATUS 两个文档的分工与协同）
>   - `05_case_study_session_handoff.md` — 会话交接（STATUS 作为会话间状态传递的载体）
> **核心方法**: 控制论视角的文档二分 —— CONTEXT.md=参考模型（静态、机器可解析）、STATUS.md=状态观测器（动态、人类看板）
> **关键数据**: 6 维对比表（读者/用途/风格/频率/粒度/维护）、常见错误 4 条、协同工作流 4 步

---

## 摘要

从控制论视角把 CONTEXT.md 建模为系统的**参考模型**（Reference Model，定义项目"应该是什么样"），把 STATUS.md 建模为**状态观测器**（State Observer，记录"现在是什么样"）。二者读者不同（AI vs 人类）、粒度不同（粗 vs 细）、更新频率不同（低 vs 高），但通过链接协同：AI 新对话读 CONTEXT 获得静态知识，人类维护 STATUS 传递动态进度，任务完成后 AI 更新 STATUS 形成闭环。核心结论：没有 CONTEXT，AI 会瞎猜；没有 STATUS，人类会迷失方向。

---

`CONTEXT.md` 和 `STATUS.md` 是为不同受众设计的两个互补文档，它们的核心区别在于**目标读者**和**信息粒度**。

---

## 一、核心定位对比

| 维度 | **CONTEXT.md** | **STATUS.md** |
|------|----------------|----------------|
| **目标读者** | AI 助手（如 Claude Code） | 人类开发者（你自己或协作者） |
| **主要用途** | 让 AI 快速理解项目现状、约定、可用命令 | 让人快速掌握项目进度、阻塞、下一步计划 |
| **内容风格** | 结构化、条目化、机器可解析（含路径、命令、环境） | 自然语言、看板式、侧重状态和决策 |
| **更新频率** | 低（项目结构/接口变化时） | 高（每次工作会话后） |
| **信息粒度** | 粗（整体架构、目录约定、常用命令） | 细（当前任务进度、昨天做了什么、明天做什么） |
| **典型长度** | 1~2 页（稳定） | 半页~1 页（动态变化） |
| **是否需要人工维护** | 初期需人工写，后期 AI 可协助更新 | 每次任务结束由人或 AI 更新 |

---

## 二、CONTEXT.md 应该包含什么？（给 AI 看）

```markdown
# 项目上下文（AI 专用）

## 项目根目录
`/home/user/project/`

## 环境与依赖
- conda 环境：`myenv`（激活命令 `conda activate myenv`）
- 主要库：`tbplas`, `numpy`, `scipy`, `matplotlib`

## 关键文件路径
- 主入口：`src/main.py`
- 配置文件：`configs/*.yaml`
- 输出目录：`data/`、`runs/`

## 常用命令（供 AI 执行）
- 本地测试：`python src/test.py --quick`
- 远程提交：`sbatch slurm/template.sh`
- 结果回传：`scp h3clogin:~/scratch/project/runs/ ./`

## 目录约定
- `src/`：源代码（不可自动修改）
- `configs/`：YAML 配置
- `slurm/`：生成的脚本
- `runs/`：运行产物（按时间戳隔离）

## 安全约束
- 私钥必须有密码短语
- 禁止执行 `rm -rf /`
- 远程命令白名单：`sbatch`, `squeue`, `scancel`, `ls`, `mkdir`, `cd`
```

**特点**：稳定、可复用、AI 每新对话开始时先读取此文件。

---

## 三、STATUS.md 应该包含什么？（给人看）

```markdown
# 项目状态看板（人类用）

## 当前目标（本周）
- [ ] 完成 n=29 的 DOS 计算
- [ ] 修复 LDOS 在 DW 区域的画图 bug

## 进度跟踪
- ✅ n=2 能带计算完成（2026-05-20）
- 🔄 n=29 DOS 作业已提交（Job ID: 123456），等待完成
- ⏳ 待开始：n=134 LDOS 扫描

## 阻塞
- 无

## 下一步
1. 检查作业 123456 是否完成：`squeue -j 123456`
2. 若完成，运行 `python vis_dos.py --n 29`
3. 更新本文件

## 最近决策
- 2026-05-22：统一使用 10022 端口转发，避免权限错误
- 2026-05-21：私钥已添加密码短语，配置 ControlMaster

## 健康度
- 进度：60% 🟡
```

**特点**：每日变化、记录实际进展和临时问题。

---

## 四、两者关系：**参考模型 vs 状态观测器**

从控制论角度：

- **CONTEXT.md** 是系统的 **“参考模型”**（Reference Model）—— 定义了项目应该是什么样的（文件结构、环境、约定）。AI 以此为基础做出正确决策。
- **STATUS.md** 是系统的 **“状态观测器”**（State Observer）—— 记录当前实际状态（任务完成度、阻塞、临时决策）。人类通过它进行控制调整。

**协同工作流**：
1. **新对话开始时**：AI 读取 `CONTEXT.md`，获得项目的静态知识。
2. **人类更新 STATUS.md**：记录当天的进展和下一步计划。
3. **人类要求 AI 执行任务**：AI 同时参考 CONTEXT（知道怎么做事）和 STATUS（知道做什么事）。
4. **任务完成后**：AI 更新 STATUS.md 中的进度（如把 `[ ]` 改为 `[x]`），人类审视并调整方向。

---

## 五、常见错误与避免方法

| 错误 | 后果 | 正确做法 |
|------|------|----------|
| 把 STATUS 的内容写进 CONTEXT | AI 会读到过时的任务细节，干扰决策 | CONTEXT 只放稳定信息 |
| 忘记更新 STATUS | 人类失去对进度的掌控，AI 也无从得知下一步 | 每次工作会话结束前更新 STATUS |
| CONTEXT 过于冗长（包含每日命令） | AI 浪费 token，且容易过时 | CONTEXT 只放“永久”或“长期有效”的内容 |
| STATUS 缺少“下一步行动” | 人类或 AI 不知道接下来该做什么 | 始终保留一个清晰的“下一步”条目 |

---

## 六、总结

- **CONTEXT.md**：给 AI 的“项目百科全书”，稳定、结构化、机器友好。
- **STATUS.md**：给人类的“项目仪表盘”，动态、自然语言、行动驱动。
- **两者独立但互补**：没有 CONTEXT，AI 会瞎猜；没有 STATUS，人类会迷失方向。
- **建议两者同时维护**：CONTEXT 可由 AI 协助初始生成，STATUS 由人每天更新（也可让 AI 协助勾选完成项）。

在 `AI_test` 项目中，你已经有了 `CONTEXT.md` 和 `plan.md`，但没有 `STATUS.md`。建议添加 `STATUS.md` 作为日常看板，而 `CONTEXT.md` 保持稳定，`plan.md` 作为长期蓝图。三者形成完整的文档体系。