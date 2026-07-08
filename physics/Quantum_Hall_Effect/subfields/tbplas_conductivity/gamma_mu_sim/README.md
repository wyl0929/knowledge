<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-28 00:25:30
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-28 00:25:35
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/gamma_mu_sim/README.md
 * @Description  :
-->
# Γ-μ 随机游走模拟

> 在纯 Python 下用合成 Γ/μ 矩阵定量验证 Kubo-Bastin 双重求和中浮点随机游走累积的标度关系

## 快速启动

```bash
# 激活虚拟环境
source /home/wyl/project/knowledge/.venv/bin/activate

# 安装依赖
pip install numpy scipy mpmath pandas tqdm matplotlib

# 运行完整 M 扫描（T4+T5）
python src/t4_scan.py    # 6 kernel×method 线, M=64→8192
python src/t5_scan.py    # Lorentz λ 扫描 + 综合排名

# 生成全部图表
python src/visualize.py

# 查看报告
cat docs/report.md
```

## 依赖

- Python 3.10+
- numpy, scipy — 矩阵生成
- mpmath — 高精度参考
- pandas — CSV 读写
- matplotlib — 图表

## 目录结构

```
gamma_mu_sim/
├── src/                    ← 核心代码
│   ├── config.py           ← 参数配置 + M 网格
│   ├── gamma_matrix.py     ← Γ 矩阵生成（向量化）
│   ├── mu_matrix.py        ← μ 矩阵生成（3 核模型）
│   ├── summation.py        ← 求和引擎（sequential + Kahan）
│   ├── reference.py        ← mpmath 高精度基准
│   ├── analysis.py         ← 标度律拟合
│   ├── main.py             ← CLI 入口
│   ├── t4_scan.py          ← T4 M 系统性扫描
│   ├── t5_scan.py          ← T5 Lorentz λ 扫描 + 排名
│   └── visualize.py        ← 图表生成（8 张发表级图表）
├── output/
│   ├── data/               ← CSV + JSON 数据
│   └── figures/            ← PNG 图表
└── docs/
    ├── plan.md             ← 技术设计计划书
    ├── tasks.md            ← 任务清单
    ├── log.md              ← 执行日志
    └── report.md           ← 最终分析报告
```

## 核心结论

**随机游走 RMS ∝ M²·ε（α≈2.08）**。三种核加权（clean/Jackson/Lorentz）和 Kahan 补偿求和均**无法改变标度指数**——仅改变前因子 β 而不改变 α。这与 VBL Phase M 诊断完全一致：δμ 噪声通过高 |Γ| 项放大，核阻尼不足以压制 ‖Γμ‖ 增长。

**实用建议**：tbplas Kubo-Bastin 计算中 M ≤ 2560 为安全范围，始终使用 `rescale=-1`，不推荐 M ≥ 3072 除非使用四精度。

详见 [docs/report.md](docs/report.md)。
