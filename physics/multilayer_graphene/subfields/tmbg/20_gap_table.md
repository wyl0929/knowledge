<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-12 14:25:07
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-12 14:25:08
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/tmbg/20_gap_table.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-12
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-12
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/tmbg/20_gap_table.md
 * @Description  : TMBG 专属缺口表
-->
# 20 Gap Table / TMBG · 缺口表

Last updated: 2026-06-12

> TMBG 子领域的知识缺口，继承并细化了父 pack（`../20_gap_table.md`）中与 TMBG 相关的条目。
>
> 缺口分类：
> - `confirmed` = 多来源确认的知识空缺
> - `suspected` = 有初步证据的疑似缺口
> - `weak` = 推测性缺口，可能是伪缺口
> - `not-a-gap` = 已解决或不是缺口

---

## 1. 实验缺口（TMBG 专属）

| ID | 缺口描述 | 类型 | 验证方式 | 用户相关性 |
|---|---|---|---|---|
| TMBG-E01 | TMBG 超导的独立重复验证 | `suspected` | 需要更多实验组尝试 | ⭐⭐（计算无法直接帮助，但可提供理论支持） |
| TMBG-E02 | TMBG 中 ν = ±1 关联绝缘态的序参量确定 | `suspected` | 需要自旋/谷分辨探针（如 STM 的自旋分辨） | ⭐⭐ |
| TMBG-E03 | TMBG 的高质量 STM/STS 平带谱 | `weak` | 三层体系针尖信号解析困难 | ⭐（计算可提供预测） |
| TMBG-E04 | TMBG 在磁场下的 Hofstadter 谱实验 | `weak` | 需要极高 B/T 比或大摩尔周期 | ⭐⭐（计算可先行） |

## 2. 理论缺口（TMBG 专属）

| ID | 缺口描述 | 类型 | 验证方式 | 用户相关性 |
|---|---|---|---|---|
| TMBG-T01 | TMBG 紧束缚能带的超胞收敛性（多大超胞够？） | `weak` | 系统测试不同超胞大小 → 比较能带和 DOS | ⭐⭐⭐⭐⭐ |
| TMBG-T02 | 连续模型 vs 紧束缚模型在 TMBG 中的定量偏差 | `weak` | 固定 θ 和 D，计算两种方法能带的差异 vs 超胞大小 | ⭐⭐⭐⭐⭐ |
| TMBG-T03 | 转角不均匀对 TMBG 平带带宽和 DOS 的定量影响 | `weak` | 紧束缚 + 局域 δθ(r) 随机场 + TBPM DOS | ⭐⭐⭐⭐⭐ |
| TMBG-T04 | TMBG 中所有平带的 Chern 数在 (θ, D) 空间中的完整相图 | `suspected` | TB + Berry curvature 扫描 | ⭐⭐⭐⭐ |
| TMBG-T05 | 位移场 D 在 TMBG 紧束缚中的微观实现方案比较 | `weak` | 比较 on-site 偏移、层间电荷转移、DFT 标定等方案 | ⭐⭐⭐⭐ |
| TMBG-T06 | 晶格弛豫在 TMBG 三层中的逐层差异化效应 | `suspected` | DFT + 力场弛豫 → 提取有效 TB 参数 | ⭐⭐⭐（需要 DFT 输入） |
| TMBG-T07 | TMBG 超导的微观配对理论 | `speculation` | 需要强关联多体方法 | ⭐（超出用户当前能力） |
| TMBG-T08 | TMBG 平带中关联效应的最小模型（如 Hubbard 模型参数提取） | `weak` | Wannier 函数构造 → Hubbard U 和 t 参数 | ⭐⭐⭐ |

## 3. 方法缺口（TMBG 专属）

| ID | 缺口描述 | 类型 | 验证方式 | 用户相关性 |
|---|---|---|---|---|
| TMBG-M01 | TMBG 的公开紧束缚基准数据集（标准能带、DOS、Chern 数） | `confirmed` | 社区没有，你可以产出第一个 | ⭐⭐⭐⭐⭐ |
| TMBG-M02 | TBPM 在 TMBG 转角体系中的适用性验证（vs 精确对角化在小体系上） | `weak` | 小超胞对角化 vs TBPM DOS 对比 | ⭐⭐⭐⭐⭐ |
| TMBG-M03 | TMBG 紧束缚超胞构建的标准化流程（如何找近公度周期、如何截断层间耦合） | `weak` | 文档化你的构建流程 | ⭐⭐⭐⭐ |
| TMBG-M04 | TMBG 输运计算（Kubo 公式）在 TBPM 框架中的实现 | `weak` | 扩展 TBPM 代码 | ⭐⭐⭐ |

## 4. TMBG 伪缺口（not-a-gap）

| ID | 描述 | 为什么不是缺口 |
|---|---|---|
| TMBG-NG01 | "TMBG 的魔角是多少？" | 连续模型已给出 ~1.0°–1.15°，BM 推广已解决 |
| TMBG-NG02 | "TMBG 有没有平带？" | 实验 + 理论多重确认 |
| TMBG-NG03 | "位移场能不能调控 TMBG？" | Xu et al. (2021) 已漂亮展示 |
| TMBG-NG04 | "TMBG 平带是否拓扑？" | Liu, Khalaf et al. (2021) 已给出 Chern 数非零的证明 |

## 5. 按用户切入优先级排序

```
🥇 可立即动手（1–2 周可产出结果）：
  TMBG-T01   紧束缚超胞收敛性              ← 纯 TB 计算，无依赖
  TMBG-T02   连续模型 vs 紧束缚定量对比      ← 已有连续模型参考代码
  TMBG-M01   公开基准数据集                  ← 上述计算的副产品
  TMBG-M02   TBPM 适用性验证                 ← 现有 TBPM 代码直接用

🥈 中期探索（2–4 周）：
  TMBG-T03   转角不均匀对平带的定量效应       ← 需要无序模型
  TMBG-T04   平带拓扑分类（Chern 相图）       ← 需要 Berry curvature
  TMBG-T05   位移场的 TB 微观实现方案比较      ← 需要模型研究

🥉 需要外部输入或长期投入：
  TMBG-T06   晶格弛豫逐层效应                ← 需要 DFT/LAMMPS
  TMBG-T08   关联效应的 Hubbard 参数          ← 需要 Wannier90
  TMBG-T07   超导微观理论                    ← 需要强关联方法
  TMBG-E01   超导实验验证                    ← 实验资源
```
