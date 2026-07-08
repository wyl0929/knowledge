<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-12 14:25:08
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-12 14:25:09
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/tmbg/21_asset_match.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-12
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-12
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/tmbg/21_asset_match.md
 * @Description  : TMBG 缺口与用户资产的匹配分析
-->
# 21 Asset Match / TMBG · 资产-缺口匹配

Last updated: 2026-06-12

> 将 TMBG 的缺口与用户现有资产进行匹配，识别可直接动手的、需要补充资源的、以及需要合作的方向。
> **注意**：用户已在 `/home/wyl/project/TMBG` 建立完整的 TMBG 紧束缚计算项目，
> 具备 n=6/29/183/472 建模 + TBPM DOS + Haydock LDOS + QE + gap/FWHM 分析管线。

---

## 1. 用户资产快照（基于实际代码）

| 资产 | 等级 | 详情 |
|---|---|---|
| **TMBG 项目** (`/home/wyl/project/TMBG`) | ⭐⭐⭐⭐⭐ 核心 | 完整 TBG/TMBG 模型 + TBPM + LD + QE + auto-Δ 扫描 |
| **tbplas** | ⭐⭐⭐⭐⭐ 核心 | 紧束缚核心库，TBPM/Haydock/对角化 |
| **YAML 配置系统** | ⭐⭐⭐⭐ 熟练 | 批量扫描参数，batch_submit.sh 集群提交 |
| **LAMMPS 弛豫** | ⭐⭐⭐ 可用 | DRIP+REBO 弛豫，rlxd 结构已支持 |
| **连续模型 (BM/Koshino)** | ⭐⭐ 基础 | src/arc/C_*.py 有参考实现，待整合到主线 |
| **Berry 曲率 / Chern 数** | ⭐⭐ 基础 | src/arc/berry.py, topo.py 有参考实现 |
| **DFT** | ⭐ 无经验 | 无 VASP/QE 使用经验 |
| **强关联方法 (DMFT/QMC)** | ⭐ 无经验 | 未接触 |
| **实验合作** | ❌ 无 | 无实验合作者 |

## 2. 缺口-资产匹配矩阵

### 🟢 直接匹配（用户资产 ≥ 缺口需求）

| Gap ID | 缺口 | 所需资产 | 用户匹配度 | 备注 |
|---|---|---|---|---|
| TMBG-T01 | 紧束缚超胞收敛性 | TB + 对角化 | ✅ 完美 | TMBG 项目已支持 n=6/29/183/472 |
| TMBG-T02 | 连续模型 vs TB 定量对比 | TB + 连续模型 | ✅ 良好 | TB 就绪，连续模型在 src/arc/C_*.py |
| TMBG-M01 | 公开基准数据集 | TB + TBPM | ✅ 完美 | 已有 n=183/472 LDOS 数据可直接整理 |
| TMBG-M02 | TBPM 适用性验证 | TBPM + 对角化 | ✅ 完美 | TMBG 项目含对角化能带 |
| TMBG-M03 | 紧束缚超胞构建标准化 | TB + 文档化 | ✅ 完美 | 构建流程即已文档化在 README/CONTEXT |

### 🟡 部分匹配

| Gap ID | 缺口 | 缺什么 | 获取难度 | 备注 |
|---|---|---|---|---|
| TMBG-T03 | 转角不均匀对平带的定量效应 | 无序模型设计 | ⭐ 低 | 在现有 TB 中加空间缓变转角分布 |
| TMBG-T04 | 平带拓扑分类（Chern 相图） | Berry curvature 计算代码 | ⚠️ **TBPM 无法算 Berry 曲率**（需 diag），diag 限 n≤29 | 需探索新方法或小体系外推 |
| TMBG-T05 | 位移场的 TB 微观实现 | 模型比较框架 | ⭐ 低 | model.py 已实现 top/mid/bot onsite ~Δ |
| TMBG-M04 | TBPM 输运（Kubo） | Kubo 公式在 TBPM 中的实现 | ⭐⭐ 中 | 需要理论推导 + 编码 |
| TMBG-M05 | **大体系拓扑不变量** | 超越 diag 的拓扑方法 | ⭐⭐⭐ 高 | TBPM 无法访问本征态，需探索 Wilson loop/实空间 Chern 标记 |

## 3. ⚠️ 拓扑计算的现实策略

由于 **TBPM 无法计算 Berry 曲率**（需本征态，仅 diag 可用），TMBG 拓扑分类必须分层处理：

| 层级 | 方法 | 可达体系 | 产出 |
|---|---|---|---|
| **L1: 精确拓扑** | diag + Berry curvature (src/arc/berry.py) | n=6,29 (θ≥3.9°) | 大角度精确 Chern 数，建立方法基准 |
| **L2: 连续模型拓扑** | BM/Koshino 连续模型 (src/arc/C_*.py) | 任意 θ（无超胞限制） | 魔角区 C_v 预测，与 TB 能带对比验证 |
| **L3: TBPM 间接信号** | DOS gap + LDOS 空间分布 + 输运 | n=183,472 (θ~0.2-0.6°) | 关联态/能隙特征，与 He et al. 实验对比 |
| **L4: 新方法探索** | Wilson loop / 实空间 Chern 标记 | 待研究 | 绕过 diag 限制在大超胞直接算拓扑 |

**当前建议**：优先推进 L1+L2+L3，不阻塞在 L4 上。

## 4. 已有数据资产

| 数据 | 位置 | 说明 |
|---|---|---|
| n=29 LDOS 冒烟测试 | runs/0610/ | DOS+LDOS+QE 全部通过 |
| n=183 LDOS Δ 扫描 (101 个点) | configs/n183/ + runs/0610/ | Δ∈[-0.050, 0.050] eV, step=0.001 |
| n=183 FWHM 收敛测试 (m=4,6,8,10,12,14,16) | runs/0611/ | LDOS 峰 FWHM vs 超胞大小 |
| n=472 极小转角 | runs/0610/, runs/0611/ | θ≈0.24°, ~4M 轨道, max_distance=0.4 |
| n=472 gap 分析 | runs/0611/ | ldos_n472_d0.016 gap 图 |

### 🔴 需要外部资源

| Gap ID | 缺口 | 缺什么 | 可能的获取方式 |
|---|---|---|---|
| TMBG-T06 | 晶格弛豫逐层效应 | DFT 或力场弛豫数据 | 合作 DFT 组，或从文献中提取有效参数 |
| TMBG-T08 | Hubbard 参数提取 | Wannier90 构造 MLWF | 学习 Wannier90（~2 周），或合作 |
| TMBG-T07 | 超导微观理论 | 强关联方法（DMFT/QMC） | 需要理论合作者 |
| TMBG-E01 | 超导实验验证 | 实验合作 | 需要建立实验连接 |

---

## 3. 推荐的"最小可行切入点"排名

按**投入产出比 × 资产匹配度 × 成果独立性**排序：

| 排名 | 切入点 | 预计投入 | 预计产出 | 依赖风险 |
|---|---|---|---|---|
| 🥇 | **TMBG-T01 + TMBG-M01：紧束缚基准** | 1–2 周 | 独立可发表的 benchmark 数据集 + 方法论文 | 极低 |
| 🥈 | **TMBG-T03：转角无序效应** | 2–3 周 | 与实验直接对话的理论结果 | 低 |
| 🥉 | **TMBG-T04：拓扑分类** | 3–4 周 | 漂亮的拓扑相图 + 理论论文核心结果 | 中低（需要学习 Berry curvature） |
| 4 | **TMBG-T02：连续模型桥接** | 2–3 周 | 方法学贡献 | 低 |
| 5 | **TMBG-T05：位移场建模** | 2–3 周 | 方法论论文 | 低 |

---

## 4. 建议的研究策略

### Phase 1：建立基础（1–2 周）
做 🥇 **TMBG 紧束缚基准**：
- 这是所有后续工作的基础
- 产出即为贡献（公开基准数据集）
- 期间自然学会 TMBG 紧束缚的所有技术细节

### Phase 2：选择一个主攻方向（2–4 周）
基于 Phase 1 的经验和兴趣，选择以下之一深入：
- **路线 A（实验对话型）**：🥈 转角无序效应 → 产出与实验组可对话的结果
- **路线 B（理论深化型）**：🥉 拓扑分类 → 产出完整的 Chern 数相图
- **路线 C（方法论型）**：TMBG-T02 + TMBG-T05 → 产出方法桥接论文

### Phase 3：扩展与发表（4–8 周）
将 Phase 1 + Phase 2 的结果整合成论文。
