<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-12 14:23:19
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-12 14:24:37
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/tmbg/02_frontier_compass.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-12
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-12
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/tmbg/02_frontier_compass.md
 * @Description  : TMBG 边界罗盘 —— 内圈、baseline、边界和用户切口
-->
# 02 Frontier Compass / TMBG · 边界罗盘

Last updated: 2026-06-12

> 明确 TMBG 子领域中：哪些是内圈常识、哪些是成熟 baseline、哪些是真正边界、哪些是伪 gap，以及用户个人可以切哪里。

---

## 1. TMBG 内圈知识（已牢固确立）

继承父 pack 内圈知识（`../02_frontier_compass.md` §1），外加 TMBG 专有：

| 知识点 | 为什么可靠 |
|---|---|
| TMBG 由单层 + AB 双层转角构成，仅 1 个转角界面 | 构型定义 |
| TMBG 魔角在 θ ≈ 1.0°–1.15° 附近存在平带 | 实验（输运）+ 理论（连续模型）一致 |
| TMBG 中关联绝缘态在 ν = ±1, ±2, ±3 处出现 | 3+ 独立实验组确认 |
| 位移场 D 可以移动 TMBG 平带的能量位置和拓扑性质 | 实验 + 连续模型理论一致 |
| 连续模型（BM 推广）可以定性正确描述 TMBG 的低能能带 | Liu, Khalaf et al. (2021) + 实验对比 |

---

## 2. TMBG 成熟 Baseline（1–2 周可复现的计算）

这些是"验证性计算"——你应该能做，但不是研究贡献：

| Baseline | 方法 | 工作量 | 产出价值 |
|---|---|---|---|
| 连续模型计算 TMBG 能带 vs (θ, D) | Python, ~300 行 | 2–3 天 | ⭐ 验证理解 |
| 紧束缚 TMBG 能带（固定 θ）与连续模型对比 | 改造 graphene.py | 3–5 天 | ⭐⭐ 方法验证 |
| TBPM 计算 TMBG DOS（固定 θ, D=0） | 现有 TBPM 代码 | 1 天 | ⭐⭐ 基准数据 |
| 复现 Liu, Khalaf et al. 的 Chern 数计算 | Python, Berry curvature | 3–5 天 | ⭐⭐ 方法学习 |

---

## 3. TMBG 真正的知识边界

### 3.1 实验边界

| 边界问题 | 状态 | 为什么难 |
|---|---|---|
| TMBG 超导是否真实且可重复？ | `suspected` | 仅 1 组报道，转角均匀性要求高 |
| TMBG 中 ν = ±1 绝缘态的序参量是什么？| `suspected` | 需要自旋/谷分辨的探针 |
| TMBG 的 STM 平带谱（局域态密度）长什么样？| `weak` | 三层体系针尖信号复杂 |
| TMBG 在有限磁场下的完整 Hofstadter 谱？| `weak` | 需要极高 B 或极低 θ |

### 3.2 理论边界

| 边界问题 | 状态 | 计算可行性 | 你的优势 |
|---|---|---|---|
| 紧束缚模型在 TMBG 中的定量精度 vs 连续模型？| `weak` | ✅ 高 | TBPM 天然 |
| 转角不均匀（twist angle inhomogeneity）对 TMBG 平带的定量破坏？| `weak` | ✅ 高 | TBPM + 无序 |
| TMBG 所有平带的完整拓扑分类（Chern 数序列 vs θ vs D）？| `suspected` | ✅ 中 | TB + Berry |
| 晶格弛豫在 TMBG 三层中的逐层差异化效应？| `suspected` | ⚠️ 需要 DFT 输入 | 有限 |
| TMBG 超导的微观配对机制？| `speculation` | ❌ 需要强关联方法 | 无 |

### 3.3 方法边界

| 边界问题 | 状态 | 你的优势 |
|---|---|---|
| TMBG 紧束缚能带的超胞收敛性（要多大的超胞才够）？| `weak` | TBPM 可系统测试 |
| TBPM 在转角度不均匀的 TMBG 体系中的精度？| `weak` | 你控制 TBPM |
| 能否为 TMBG 建立"连续 → 紧束缚 → TBPM"的完整方法链？| `weak` | 你有全部零件 |

---

## 4. TMBG 的伪 gap（not-a-gap）

| 看似 gap 的问题 | 为什么不是 gap |
|---|---|
| "TMBG 魔角是多少？" | 连续模型已给出 ~1.0°–1.15°，精确值取决于参数，不是未知 |
| "TMBG 有没有平带？" | 实验和理论一致确认有 |
| "TMBG 的关联绝缘态是否真实？" | 多组独立实验已确认 |
| "位移场 D 能否调控 TMBG？" | Xu et al. (2021) 已漂亮展示 |

---

## 5. 用户个人切口（你的切入角度）

基于你的资产（TBPM、graphene.py、MPI 并行、SLURM 集群），以下切口按**投入产出比**排序：

### 🥇 切口 1：TMBG 紧束缚能带基准 + 连续模型桥接

**做什么**：系统计算 TMBG 在不同 θ、不同超胞大小下的紧束缚能带，与连续模型做定量对比。
**为什么是切口**：
- 父 pack gap G-M03 的直接落实
- 文献中没有人做过 TMBG 的"紧束缚 vs 连续模型"系统基准
- 你的 TB 代码只需加一层 + 层间耦合即可
**预计产出**：1 篇 methodology benchmark 论文或至少可公开的基准数据

### 🥈 切口 2：转角不均匀对 TMBG 平带的定量效应

**做什么**：在紧束缚超胞中引入随机局域转角涨落 δθ(r)，用 TBPM 计算平带 DOS 和无序下的输运。
**为什么是切口**：
- 父 pack gap G-T02 在 TMBG 的具体化
- TBPM 天然适合大规模无序平均
- 实验上转角不均匀是限制器件质量的主要因素，但缺乏定量理论
**预计产出**：理论-实验桥接论文

### 🥉 切口 3：TMBG 平带的完整拓扑分类

**做什么**：扫描 (θ, D) 二维参数空间，计算所有平带的 Chern 数，建立 TMBG 的拓扑相图。
**为什么是切口**：
- Liu, Khalaf et al. 只做了连续模型的定性分析，缺少系统 TB 结果
- 父 pack gap G-T03 的直接落实
- 可产出漂亮的拓扑相图
**预计产出**：理论论文中的核心图

### 切口 4（远期）：位移场在紧束缚中的微观建模

**做什么**：研究 on-site 电势差、层间电荷转移、弛豫修正等不同方案对 TMBG 能带的影响。
**为什么是远期**：
- 需要 DFT 输入或实验参数标定（你目前缺 DFT）
- 但可以先做"模型研究"——探索不同方案对能带的定性影响
**预计产出**：方法论论文

---

## 6. 建议行动路线

```
Week 1: 切口 1 — TMBG 紧束缚能带基准
  Day 1–2: 构建 TMBG 超胞（改造 graphene.py）
  Day 3–4: 计算能带 vs θ, vs 超胞大小，对比连续模型
  Day 5: 产出初步基准数据

Week 2: 切口 2 的初步探索
  Day 1–2: 实现局域转角涨落模型
  Day 3–5: TBPM DOS 计算 vs 无序强度，观察平带鲁棒性

Week 3–4: 整理结果，决定主攻方向
  选项 A: 深化切口 1 → 完整 benchmark 论文
  选项 B: 深化切口 2 → 无序-平带论文
  选项 C: 扩展切口 3 → 拓扑分类 + 相图论文
```

> 详细项目卡片见 `22_project_candidates.md`。
