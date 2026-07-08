<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-27 23:15:56
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-27 23:16:02
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/gamma_mu_sim/CONTEXT.md
 * @Description  :
-->
# CONTEXT.md — Γ-μ 随机游走模拟

> 角色：参考模型（AI 百科全书） | 读者：🤖 AI
> 动态进度见 STATUS.md | 任务清单见 docs/tasks.md

## 项目标识

- **路径**: `physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/gamma_mu_sim/`
- **目标**: 在纯 Python 下用合成 Γ/μ 矩阵定量验证 Kubo-Bastin 双重求和中浮点随机游走累积的标度关系
- **语言**: Python 3.10+（venv: `/home/wyl/project/knowledge/.venv/`）

## 环境约定

- **Python 解释器**: `/home/wyl/project/knowledge/.venv/bin/python`
- **依赖**: numpy, scipy, mpmath, pandas, tqdm, matplotlib
- **源码根**: `src/`（所有 .py 可直接 `python src/<module>.py` 运行自测）
- **输出目录**: `output/data/` (CSV), `output/figures/` (PNG/PDF)
- **文档**: `docs/plan.md`（架构）, `docs/tasks.md`（任务）, `docs/log.md`（日志）

## 目录结构

```
gamma_mu_sim/
├── src/                    ← 核心代码（7 模块）
│   ├── config.py           ← 参数 + M 网格
│   ├── gamma_matrix.py     ← Γ 矩阵生成（向量化）
│   ├── mu_matrix.py        ← μ 矩阵生成（3 核模型）
│   ├── summation.py        ← 求和引擎（sequential + Kahan）
│   ├── reference.py        ← mpmath 高精度基准
│   ├── analysis.py         ← 标度律拟合
│   └── main.py             ← CLI 入口 + M 扫描流水线
├── output/                 ← 数据 + 图表
├── docs/                   ← plan + tasks + log + report
```

## 核心概念速查

| 概念 | 对应模块 | 关键公式 |
|------|---------|---------|
| Γ 矩阵 | gamma_matrix | Γ_{mn}=cos(mθ)(cosθ-in·sinθ)e^{inθ} + cos(nθ)(cosθ+im·sinθ)e^{-imθ} |
| μ 矩阵（clean） | mu_matrix | μ_{mn}=T_m(E0)T_n(E0), T_n=Chebyshev 多项式 |
| Jackson 核 | mu_matrix | g_n=((M-n+1)cos(πn/(M+1))+cot(π/(M+1))sin(πn/(M+1)))/(M+1) |
| Lorentz 核 | mu_matrix | g_n=sinh(λ(1-n/M))/sinh(λ) |
| Sequential 求和 | summation | 标准双重循环累加 |
| Kahan 求和 | summation | 补偿项修正低位舍入 |
| mpmath 参考 | reference | dps=50 高精度 ground truth |

## 已知注意事项

- Γ 矩阵量级 ≈ M·sinθ（非精确 M），θ=π/4 时 max|Γ| ≈ 0.707M
- mpmath 参考值使用 mu_true（干净），不是 mu_noisy——解耦"噪声累积"与"核效应"
- 相对误差在 S_ref≈0（信号零点）时会发散——属正常，以绝对误差为准
- **α≈2.08（非 1.0）**: Γ 元素 ∝ M 使随机游走标度修正为 M²·ε（T4 实测确认）
- **Kahan 无显著改善**: 噪声源自 δμ（μ 矩阵浮点噪声），非求和舍入（T4 确认）
- **scipy eval_chebyt NaN**: n≥2466 时产生 NaN，mu_matrix.py 已改用 cos(n·π/2) 解析式（E0=0）
- **fsum 参考**: math.fsum (Shewchuk 精确舍入) 替代 mpmath 用于大 M（性能原因，M=256 验证一致）
- **Lorentz 核无法消除随机游走（T5 确认）**: λ∈[2,8] 所有 α≈2，核加权仅改变 β 不改变 α。不存在"甜点 λ"实现绝对收敛。与 VBL Phase M 诊断一致——高 |Γ| 区主导贡献，核阻尼不足以压制
- **实用 M 上限**: M ≤ 2560（双精度安全范围），M ≥ 3072 不推荐除非四精度
