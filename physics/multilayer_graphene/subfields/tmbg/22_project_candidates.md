<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-12 14:25:08
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-12 14:25:09
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/tmbg/22_project_candidates.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-12
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-12
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/tmbg/22_project_candidates.md
 * @Description  : TMBG 候选项目卡片
-->
# 22 Project Candidates / TMBG · 候选项目卡片

Last updated: 2026-06-12

> 基于 gap 表和资产匹配的 TMBG 候选项目卡片。
> 每个项目包含：motivation → approach → baseline → metrics → risks → stop criteria。
> **注意**：用户 TMBG 项目位于 `/home/wyl/project/TMBG`，已具备生产级 TBPM 计算能力。

---

## 项目卡片 1：TMBG 紧束缚能带基准 🥇

| 属性 | 内容 |
|---|---|
| **ID** | TMBG-P1 |
| **对应 gap** | TMBG-T01, TMBG-T02, TMBG-M01 |
| **优先级** | 🥇 最高 |
| **operational_status** | `ready` — TB 计算已就绪，待连续模型整合 |

### Motivation

TMBG 文献中缺乏紧束缚模型和连续模型的系统定量对比。用户已有 `/home/wyl/project/TMBG` 的生产级 TB 代码（n=183/472 已计算），以及 `src/arc/C_*.py` 中的连续模型参考实现。桥接这两者可以：
1. 产出 TMBG 社区首个公开 TB 基准
2. 建立用户在该方向的独特竞争力

### Approach

1. 整合 `src/arc/C_core.py`, `C_func.py` 的连续模型到主线
2. 基于已有 TB 管线（model.py → calc.py → io_vis.py）
3. 系统扫描：
   - θ ∈ [0.8°, 1.5°] — 用已有 n=183 (0.63°), n=472 (0.24°), 补充 n=70 (1.63°)
   - Δ ∈ [-0.05, 0.05] eV → D ∈ [-1.5, 1.5] V/nm
   - 堆垛区域: ABA, ABC, AA, DW
4. 对每个参数：TB 能带/DOS/LDOS + 连续模型能带 → 定量比较

### Baseline

- 连续模型在 θ=1.16°, D>0 的 C_v=2 (Liu, Khalaf et al. 2021; He et al. 2021 验证)
- 已有 n=183 LDOS 101 点扫描数据 (Δ∈[-0.050, 0.050]) → 可直接作为 anchor
- He et al. (2021) 输运相图 → 可作为定性验证目标

### Metrics

| 指标 | 定义 | 成功条件 |
|---|---|---|
| 平带带宽收敛 | W(N_atoms) − W(N_atoms→∞) | < 1 meV 偏差 |
| TB vs 连续模型偏差 | ΔE(k) 的 RMS | < 5 meV 平均 |
| DOS gap | calc_gap 检测的带隙 | 与连续模型一致 |

### Risks

| 风险 | 概率 | 缓解 |
|---|---|---|
| 连续模型实现有 bug | 低 | 先复现已知 TBG 魔角能带 |
| 超大超胞对角化内存不足 | 低 | 已有 n=472 max_distance=0.4 方案 |

### 预计时间

1–2 周

---

## 项目卡片 2：转角不均匀对 TMBG 平带的定量破坏 🥈

| 属性 | 内容 |
|---|---|
| **ID** | TMBG-P2 |
| **对应 gap** | TMBG-T03, 父 pack G-T02 |
| **优先级** | 🥈 高 |
| **operational_status** | `ready` |

### Motivation

实验上 TMBG 器件的转角总有空间不均匀性（~0.1° 量级的涨落）。这种不均匀性被认为是限制超导可重复性的关键因素，但缺乏定量理论研究。你的 TBPM 天然适合做大规模无序平均。

### Approach

1. 在 TMBG 紧束缚超胞中引入空间依赖的局域转角涨落 δθ(r)
   - 模型 1：高斯随机场，关联长度 ξ
   - 模型 2：长程渐变（模拟实验中的宏观转角梯度）
2. 用 TBPM 计算 DOS 作为无序强度 σ_θ 和关联长度 ξ 的函数
3. 观察平带的 DOS 峰如何随无序展宽和劈裂
4. 比较 TMBG vs TBG 对转角无序的相对敏感性

### Baseline

- 均匀 TMBG 的 DOS（σ_θ = 0）
- 均匀 TBG 的 DOS（θ = 1.1°）作为参照

### Metrics

| 指标 | 定义 | 成功条件 |
|---|---|---|
| 平带 DOS 峰宽 vs σ_θ | FWHM(σ_θ) | 定量给出展宽规律 |
| 临界无序强度 | σ_θ^crit：DOS 峰消失在背景中 | 给出数值 |
| TMBG vs TBG 鲁棒性比值 | σ_θ^crit(TMBG) / σ_θ^crit(TBG) | 定量比较 |

### Risks

| 风险 | 概率 | 缓解 |
|---|---|---|
| TBPM 精度不足以分辨平带细节 | 低 | TBPM 已在大体系石墨烯中验证 |
| 无序模型过于简化 | 中 | 从最简单的白噪声开始，逐步加物理 |
| 结果对无序模型细节敏感 | 中 | 测试多种模型，寻找鲁棒结论 |

### Stop Criteria

- ❌ 如果在物理合理的 σ_θ 范围内（< 0.2°）平带 DOS 完全消失 → 说明 TMBG 对无序极端敏感 → 这本身也是重要结论
- ✅ 如果找到平带存活的无序窗口 → 定量给出存活条件

### 预计时间

2–3 周

---

## 项目卡片 3：TMBG 平带的拓扑分类 🥉

| 属性 | 内容 |
|---|---|
| **ID** | TMBG-P3 |
| **对应 gap** | TMBG-T04, 父 pack G-T03 |
| **优先级** | 🥉 中高 |
| **operational_status** | `needs_prerequisite`（需要先完成 P1 的 TB 能带计算） |

### Motivation

TMBG 平带的 Chern 数在 (θ, D) 空间中如何分布？Liu, Khalaf et al. (2021) 用连续模型做了初步分析，但缺系统紧束缚结果。产出一张漂亮的 Chern 数相图就是一篇好论文的核心。

### Approach

1. 基于 P1 的紧束缚代码，为每个平带计算 Berry curvature Ω(k) 和 Chern 数 C
2. 扫描 (θ, D) 二维参数空间
3. 绘制 Chern 数相图
4. 寻找拓扑相变边界，与连续模型比较

### Baseline

- Liu, Khalaf et al. (2021) 连续模型的 Chern 数定性结果
- TBG 已知的 Chern 数序列（±1, ±2 等）

### Metrics

| 指标 | 定义 | 成功条件 |
|---|---|---|
| Chern 数计算精度 | |C_num − C_analytical| | < 0.1（数值误差） |
| 相图分辨率 | (θ, D) 网格密度 | ≥ 20×20 |
| 与连续模型一致性 | 相变边界位置 | 定性一致 |

### Risks

| 风险 | 概率 | 缓解 |
|---|---|---|
| Berry curvature 计算在小能隙处不收敛 | 中 | 增大 k 点密度，或用 Wannier 插值 |
| 拓扑相变边界对超胞大小敏感 | 中 | 做超胞收敛性测试（依托 P1 的结果） |

### Stop Criteria

- ❌ 如果 Chern 数相图在所有计算的参数点都平庸（C = 0）→ 说明你的参数范围不对或实现有误
- ✅ 如果产出了至少包含 2 种不同 Chern 数区域的相图

### 预计时间

3–4 周（依赖 P1 完成）

---

## 项目卡片 4：TMBG 中位移场的紧束缚微观建模

| 属性 | 内容 |
|---|---|
| **ID** | TMBG-P4 |
| **对应 gap** | TMBG-T05, 父 pack G-T06 |
| **优先级** | 中 |
| **operational_status** | `needs_refinement`（需要更明确的方案选择） |

### Motivation

位移场 D 是 TMBG 的核心调控参数，但其在紧束缚中的实现方式没有标准做法。不同方案（均匀 on-site 偏移、层依赖偏移、DFT 标定的有效势）可能给出定性不同的结果。这个问题需要被系统澄清。

### Approach

比较 3 种方案：
- **方案 A**：均匀 on-site 偏移 ±Δ/2（最简单，但忽略了层间电荷重分布）
- **方案 B**：层依赖偏移（Δ₁, Δ₂, Δ₃ 三层各自不同，从 DFT 或实验提取比例）
- **方案 C**：自洽的 Hartree 修正（在 TB 层面做平均场电荷自洽）

比较每种方案对能带、平带带宽、Chern 数的影响。

### Baseline

- 连续模型中的 D 效果（Liu, Khalaf et al. 2021）

### 预计时间

2–3 周

---

## 5. 推荐执行顺序

```
              P1（紧束缚基准）
              /    |    \
             /     |     \
         P2       P3      P4
    （无序效应）（拓扑分类）（位移场建模）

建议：P1 → P2（最快出独立结果）
     或 P1 → P3（理论深度更高）
     或 P1 → P2 + P3 → 合并成一篇综合论文
```
