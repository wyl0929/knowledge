/*
 * @Author       : Yulong Wang
 * @Date         : 2026-06-24 16:34:24
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-24 16:42:04
 * @FilePath     : /.agents/home/wyl/project/knowledge/computer_science/cpp_for_tbplas/kubo_bastin.h
 * @Description  : 用 Kubo-Bastin 方法计算直流电导率 (DC conductivity)。
 *                 本文件定义了抽象基类 AbstractKuboBastin 及其 CPU 实现 KuboBastinCPU。
 */

// ============================================================================
//                          文件概述 (File Overview)
// ============================================================================
// 本文件实现了 Kubo-Bastin 数值方法, 用于计算材料的直流 (DC) 电导率。
//
// 【物理背景 (给新手)】
// - "电导率" (conductivity) 描述材料导电能力。DC = 直流, 即频率为 0 的极限。
// - Kubo 公式是量子力学中计算线性响应的标准框架。
// - Bastin 将其改写为便于数值计算的形式, 核心是把对能量的积分换成
//   切比雪夫多项式 (Chebyshev polynomial) 展开。
// - 切比雪夫展开的好处: 不需要知道哈密顿量的所有本征态, 只需要
//   随机采样 + 矩阵向量乘, 适合超大稀疏矩阵 (如紧束缚模型)。
//
// 【算法流程概览】
//   阶段1 (kbdc_mu / kbdc_mu_raw):
//     用随机态 + 切比雪夫递推, 计算展开系数 μ_{mn}。
//     - kbdc_mu:    带上 Jackson 核 (减少 Gibbs 振荡), 直接得到平滑的 μ。
//     - kbdc_mu_raw: 不带核, 保存原始系数, 方便后续用不同的截断 M' 重分析。
//   阶段2 (apply_jackson_kernel / truncate_mu):
//     可选地对原始系数做核加权或截断。
//   阶段3 (cond_from_trace):
//     从 μ_{mn} 出发, 乘上 Γ 矩阵并对角度 θ 积分, 得到最终电导率 σ(E)。
//
// 【C++ 知识要点 (给新手)】
// - template <typename T>:  C++ 模板, 让同一个类能处理不同类型, 类似"类型参数化"。
// - virtual ... = 0:       纯虚函数, 子类必须实现, 类似其他语言的"接口/抽象方法"。
// - final:                 表示"最终", 用于类=禁止继承, 用于虚函数=禁止进一步重写。
// - inline:                建议编译器把函数体直接嵌入调用处, 减少函数调用开销。
// - static:                静态成员函数, 不依赖具体对象, 可通过 类名::函数() 调用。
// - #pragma omp ...:        OpenMP 并行指令, 自动把循环分配到多个 CPU 核心上同时跑。
// - Eigen::MatrixXcd:      Eigen 库的"动态大小 × 动态大小, 元素为复数 double"矩阵。
// - const T&:              常量引用传参, 避免拷贝大对象, 且保证原对象不会被修改。
//
// @author Yunhai Li (liyunhai1016@hotmail.com)
// @copyright Copyright (c) 2024, TBPLaS develop team.

// ============================================================================
//                    头文件保护 (Include Guard)
// ============================================================================
// 防止同一个头文件被多次 #include 导致"重复定义"编译错误。
// 原理: 第一次遇到时 TBPLAS_TBPM_KUBO_BASTIN_H 还没定义 → 编译内容并定义它。
//       第二次遇到时发现已经定义过了 → 跳过所有内容直到 #endif。
#ifndef TBPLAS_TBPM_KUBO_BASTIN_H
#define TBPLAS_TBPM_KUBO_BASTIN_H

// ============================================================================
//                    标准库头文件 (Standard Library)
// ============================================================================
#include <algorithm>   // 通用算法, 如 std::max, std::min
#include <cmath>       // 数学函数: std::sin, std::cos, std::pow, std::log10
#include <fstream>     // 文件输入输出: std::ofstream (写文件)
#include <iostream>    // 标准输入输出: std::cout (打印到屏幕)
#include <ostream>     // 输出流基类
#include <vector>      // 动态数组: std::vector<T>, 大小可在运行时改变

// ============================================================================
//                    第三方库: Eigen
// ============================================================================
#include <eigen3/Eigen/Dense>  // Eigen 线性代数库
// Eigen 提供的主要类型 (本文件中用到):
//   Eigen::MatrixXcd  — 动态大小矩阵, 元素类型 complex<double> (复数双精度)
//   Eigen::VectorXd   — 动态大小列向量, 元素类型 double (双精度实数)
//   Eigen::VectorXcd  — 动态大小列向量, 元素类型 complex<double>

// ============================================================================
//                    项目内头文件 (Project Headers)
// ============================================================================
#include "base/consts.h"       // 物理/数学常量 (如 PI = π)
#include "base/datatypes.h"    // 自定义数据类型 (complex_t, RandomGenerator 等)
#include "base/utils.h"        // 基础工具 (ProgressBar 进度条等)
#include "config.h"            // 计算配置结构体 TBPMConfig (存放用户设定的参数)
#include "dense.h"             // 稠密矩阵相关工具函数
#include "fermi_dirac.h"       // Fermi-Dirac 分布函数 f(E) = 1/(1+exp(β(E-μ)))
#include "kpm.h"               // 核多项式方法 (KPM) 核心: jackson_kernel, PARA_EXEC 宏等
#include "utils.h"             // 辅助工具: mat_alloc, vec_copy, vec_dot 等

// ============================================================================
//                    命名空间 (Namespace)
// ============================================================================
// 命名空间像一个"姓氏", 把相关的函数/类组织在一起, 防止不同库中的同名冲突。
// tbplas::tbpm = "TBPLaS 项目 :: TBPM (tight-binding propagation method) 模块"
namespace tbplas::tbpm {

// using 声明: 给长类型名起一个短别名, 方便书写。
// complex_t 通常是 std::complex<double> 的别名 (实部+虚部, 双精度)。
using tbplas::base::complex_t;
// ProgressBar 是控制台进度条工具, 用于在终端显示计算进度。
using tbplas::base::ProgressBar;

// ============================================================================
//           抽象基类 AbstractKuboBastin<sparse_t>
// ============================================================================
// 【设计意图】定义一个"接口", 所有 Kubo-Bastin 实现都必须提供这些函数。
// 目前有 CPU 实现 (KuboBastinCPU), 将来可能扩展 GPU 实现 (KuboBastinCUDA)。
//
// 【模板参数 sparse_t】
// 不同场景可能用不同的稀疏矩阵存储格式 (如 CSR, 自定义格式)。
// 模板让这个基类与具体格式解耦——子类指定 sparse_t 是什么即可。
//
// 【C++ 知识】
// template <typename sparse_t>  声明一个"类型参数" sparse_t, 类似函数的参数但传递的是类型。
// class 后面没有 final → 允许被继承。
// 带 = 0 的函数是"纯虚函数" → 子类必须提供实现, 否则子类也是抽象类。
template <typename sparse_t>
class AbstractKuboBastin {
public:
    // ========================================================================
    //  纯虚函数: 计算 Chebyshev 展开系数 μ_{mn} (带 Jackson 核)
    // ========================================================================
    // 【物理意义】
    // μ_{mn} 是 Kubo-Bastin 公式中对两个切比雪夫多项式 T_m(H) 和 T_n(H) 的
    // 期望值 (矩阵迹的随机估计)。 它是计算电导率的中间量。
    //
    // 【参数说明】
    // @param[in]  h_sparse  缩放后的稀疏 Hamiltonian 矩阵 H̃ = (H - b)/a
    //                       其中 a, b 是缩放参数, 保证 H̃ 的本征值在 [-1, 1] 内
    // @param[in]  curr_x    x 方向的电流算符 (稀疏矩阵形式)
    // @param[in]  curr_y    y 方向的电流算符 (稀疏矩阵形式)
    // @param[in]  config    用户设定的计算配置 (截断阶数、能量网格等)
    // @param[in]  meta      运行时元信息 (样本数、MPI 进程编号、缩放参数等)
    // @param[out] mu_avg    输出的 μ_{mn} 矩阵, 尺寸 (M × M), 已带 Jackson 核加权
    //
    // = 0 表示"纯虚函数", 子类必须提供实现。
    virtual void kbdc_mu(
        const sparse_t& h_sparse,
        const sparse_t& curr_x,
        const sparse_t& curr_y,
        const TBPMConfig& config,
        const TBPMMeta& meta,
        Eigen::MatrixXcd& mu_avg)
        = 0;

    // ========================================================================
    //  纯虚函数: 计算原始 Chebyshev 展开系数 μ_{mn} (不带 Jackson 核)
    // ========================================================================
    // 【与 kbdc_mu 的区别】
    // kbdc_mu_raw 计算时不乘 Jackson 核, 保留"原始"的 Chebyshev 系数。
    // 这样用户可以把原始系数保存下来, 以后用不同的截断阶数 M' ≤ M
    // 重新做核加权, 而不需要重新跑昂贵的随机采样。
    //
    // 【使用场景】
    // 当你不确定该用多大 M 时, 先用大的 M 跑一次 kbdc_mu_raw, 然后
    // 用 truncate_mu + apply_jackson_kernel 尝试不同 M' 的效果。
    virtual void kbdc_mu_raw(
        const sparse_t& h_sparse,
        const sparse_t& curr_x,
        const sparse_t& curr_y,
        const TBPMConfig& config,
        const TBPMMeta& meta,
        Eigen::MatrixXcd& mu_raw)
        = 0;

    // ========================================================================
    //  apply_jackson_kernel: 对原始 Chebyshev 系数施加 Jackson 核
    // ========================================================================
    // 【什么是 Jackson 核?】
    // 切比雪夫展开在截断 (只用有限项) 时会产生 Gibbs 振荡 (类似傅里叶级数
    // 在跳变处的过冲现象)。 Jackson 核是一组权重 g_n^J, 乘到展开系数上可以
    // 平滑这些振荡, 代价是略微降低能量分辨率。
    //
    // 【公式】
    // μ_{mn}^{smoothed} = μ_{mn}^{raw} × g_m^J × g_n^J
    // 其中 g_n^J 由 jackson_kernel() 函数计算 (定义在 kpm.h 中)。
    //
    // 【inline】建议编译器把函数体嵌入调用处, 避免函数调用的额外开销。
    // 【static】静态成员函数, 不依赖对象实例, 直接用 AbstractKuboBastin::apply_jackson_kernel(...) 调用。
    //
    // @param[in,out] mu         输入的原始 μ 矩阵, 会被原地修改为核加权后的值
    // @param[in]     num_kernel Chebyshev 展开阶数 M (即矩阵的行数/列数)
    //
    // @note kernel[0] 额外乘了 0.5, 这是 CPC 论文 eq.70 中 1/(1+δ_{0,n}) 因子的体现。
    inline static void apply_jackson_kernel(
        Eigen::MatrixXcd& mu,
        int num_kernel)
    {
        // 分配一个长度为 M 的向量存放 Jackson 核系数
        Eigen::VectorXd kernel(num_kernel);
        // 调用 kpm.h 中的函数填充核系数
        jackson_kernel(kernel);
        // 第 0 项乘 0.5: 因为切比雪夫展开中 T_0(x)=1, 对应的内积权重是 1/(1+δ_{0,n})
        kernel[0] *= 0.5;

        // 对矩阵的每个元素乘上对应的核权重: μ_{mn} *= g_m × g_n
        int m = 0, n = 0;
        // #pragma omp parallel for: OpenMP 指令, 把外层 for 循环分给多个 CPU 核心并行执行
        // private(n): 每个线程拥有自己独立的 n 变量副本, 避免线程间互相干扰
#pragma omp parallel for private(n)
        for (m = 0; m < num_kernel; ++m) {
            for (n = 0; n < num_kernel; ++n) {
                mu(m, n) *= kernel(m) * kernel(n);
            }
        }
    }

    // ========================================================================
    //  truncate_mu: 截断 μ 矩阵到更小的尺寸
    // ========================================================================
    // 【用途】
    // 当你用 M_large = 8000 跑了 kbdc_mu_raw, 但后来想试试 M_small = 4000
    // 的效果时, 不需要重新跑昂贵的计算, 直接从大矩阵左上角切一块就行。
    //
    // 【为什么是左上角?】
    // 切比雪夫展开系数 μ_{mn} 中, 小的 m,n 对应低频 (平滑) 分量,
    // 大的 m,n 对应高频 (细节+噪声) 分量。 截断就是把高频部分丢掉。
    //
    // @param[in]  mu_large         大尺寸 μ 矩阵 (M_large × M_large)
    // @param[out] mu_small         输出的小尺寸 μ 矩阵 (M_small × M_small)
    // @param[in]  num_kernel_small 目标尺寸 M_small (必须 ≤ M_large)
    inline static void truncate_mu(
        const Eigen::MatrixXcd& mu_large,
        Eigen::MatrixXcd& mu_small,
        int num_kernel_small)
    {
        // topLeftCorner(r, c): 取矩阵左上角 r 行 × c 列的子块
        mu_small = mu_large.topLeftCorner(num_kernel_small, num_kernel_small);
    }

    // ========================================================================
    //  cond_from_trace: 从 Chebyshev 展开系数 μ_{mn} 求直流电导率 σ(E)
    // ========================================================================
    // 【原理说明】
    // CPC 论文 eq.69 给出了从 μ_{mn} 求电导率的公式。算法分两步:
    //   第1步: 对每个角度 θ_k ∈ [0, π), 计算 sum_gamma_mu[k] = Σ_{m,n} Γ_{mn}(θ_k) × μ_{mn}
    //          其中 Γ_{mn} 是一个解析的几何因子矩阵 (由 gamma_matrix 函数计算)。
    //   第2步: 对每个目标能量 E, 沿着 θ 积分 (本质上是对能量的积分做了变量替换
    //          E → cos θ), 加权上 Fermi-Dirac 分布函数, 得到 σ(E)。
    //
    // 【inline】嵌入到调用处, 省去函数调用开销。
    //
    // @param[in]  config  用户配置 (含能量列表、角度步数、截断阶数 M)
    // @param[in]  meta    运行时元信息 (含缩放参数、温度倒数 β)
    // @param[in]  mu_avg  已加权的 Chebyshev 展开系数 μ_{mn}, (M × M) 矩阵
    // @param[out] cond    输出的直流电导率向量, 长度 = config.dckb_energies 的长度
    inline void cond_from_trace(
        const TBPMConfig& config,
        const TBPMMeta& meta,
        const Eigen::MatrixXcd& mu_avg,
        Eigen::VectorXd& cond)
    {
        // ---- 第0步: 准备输出数组 ----
        // config.dckb_energies 是用户指定的能量点列表, 每个能量点算一个电导率值
        size_t num_eng = config.dckb_energies.size();
        cond = Eigen::VectorXd::Zero(num_eng);  // 初始化为全 0

        // ---- 准备角度积分所需要的局部变量 ----
        int num_theta = config.dckb_num_integ_steps;  // θ 的离散点数 (越大积分越精确)
        int num_kernel = config.dckb_num_kernel;       // Chebyshev 截断阶数 M
        Eigen::VectorXd theta_array(num_theta);         // 存放每个离散的 θ_k 值
        Eigen::VectorXd sum_gamma_mu(num_theta);         // 存放 Σ Γ·μ 在每个 θ_k 的结果
        Eigen::MatrixXcd gamma(num_kernel, num_kernel);  // Γ 矩阵, 会被 gamma_matrix 填充

        // 控制台进度条: 显示角度积分进度
        ProgressBar prog_bar(num_theta, 256, "Finished energy");

        // ====================================================================
        //   第1步: 对每个角度 θ_k, 计算 sum_gamma_mu[k] = Σ_{m,n} Γ_{mn}(θ_k) × μ_{mn}
        // ====================================================================
        // 这里使用了 CPC 论文中的变量替换 E → cos θ, 积分区间变为 θ ∈ [0, π)。
        // θ = π / num_theta 是每个小区间的宽度。
        PARA_EXEC(std::cout << "Calculating sum." << std::endl);
        double theta = base::PI / num_theta;  // θ 的步长
        for (int k = 0; k < num_theta; ++k) {
            // θ_k = (k + 0.5) × Δθ: 中点法则 (midpoint rule)
            // 加 0.5 是为了避开 θ=0, 因为被积函数在 θ=0 有奇点 (分母含 sin³θ)
            theta_array[k] = (k + 0.5) * theta;

            // 计算 Γ 矩阵: Γ_{mn}(θ) 由 gamma_matrix 给出 (CPC 论文 eq.69)
            gamma_matrix(theta_array[k], gamma);

            // 求和: Σ_{m,n} Γ_{mn}(θ_k) × μ_{mn}, 只取实部
            // .real() 取实部: 理论上这个和应该是实数, 复数只是计算过程中引入的
            double sum = 0.0;
            int i = 0;
            int j = 0;
            // reduction(+ : sum): 每个线程有自己局部的 sum, 循环结束后把所有局部 sum 累加起来
#pragma omp parallel for private(i) reduction(+ : sum)
            for (j = 0; j < num_kernel; ++j) {
                for (i = 0; i < num_kernel; ++i) {
                    sum += (gamma(i, j) * mu_avg(i, j)).real();
                }
            }
            sum_gamma_mu[k] = sum;  // 保存该角度的结果
            PARA_EXEC(prog_bar.count());  // 更新进度条
        }

#ifdef TBPLAS_VBL_TRACE
        // 【调试用】: 当编译时定义了 TBPLAS_VBL_TRACE 宏, 把 sum_gamma_mu 输出到文件
        // 方便可视化验证中间结果, 用追加模式 (std::ios::app) 避免覆盖之前的数据
        {
            std::ofstream vbl_file("vbl_sum_M" + std::to_string(num_kernel) + ".log",
                                   std::ios::app);
            vbl_file << "M=" << num_kernel << " rs=" << meta.num_samples_dist;
            for (int kk = 0; kk < num_theta; ++kk) {
                vbl_file << " " << theta_array[kk] << ":" << sum_gamma_mu[kk];
            }
            vbl_file << std::endl;
        }
#endif

        // ====================================================================
        //   第2步: 对每个目标能量 E, 沿 θ 积分得到电导率 σ(E)
        // ====================================================================
        // 公式: σ(E) = ∫_0^π dθ × (Δθ) × sum_gamma_mu(θ) × f'(E,θ) / sin³θ
        // 其中 f'(E,θ) 是 Fermi-Dirac 分布对能量的导数 (体现在 fermi_dirac 函数中)
        // meta.rescale_center 和 meta.rescale 用于把能量反缩放回原始能量
        PARA_EXEC(std::cout << "Final integration." << std::endl);
        PARA_EXEC(prog_bar.reset(num_eng, 10, "Finished energy"));
        for (int i = 0; i < num_eng; ++i) {
            double dcx = 0.0;  // 当前能量点的电导率累加器
            // 把目标能量 E 反缩放到 Chebyshev 域 ([-1, 1] 区间)
            // efermi_re: "还原后的 Fermi 能量" = (E - b) / a
            double efermi_re = (config.dckb_energies[i] - meta.rescale_center) / meta.rescale;
            double eng_re = 0.0;  // cos θ, 即 Chebyshev 域的能量值
            double div = 0.0;     // 分母: sin³θ
            double fd = 0.0;      // Fermi-Dirac 导数值
            // 对 θ_k 做数值积分 (中点法则)
#pragma omp parallel for private(eng_re, div, fd) reduction(+ : dcx)
            for (int k = 0; k < num_theta; ++k) {
                eng_re = std::cos(theta_array[k]);              // 能量 E(θ) = cos θ
                div = std::pow(std::sin(theta_array[k]), 3.0);  // 分母 sin³θ (来自 Jacobian)
                // 计算 Fermi-Dirac 分布的贡献: f(β, E_F, E(θ))
                fd = fermi_dirac(meta.beta_re, efermi_re, eng_re);
                // 累加: sum_gamma_mu[k] × fd × (Δθ) / sin³θ
                dcx += sum_gamma_mu[k] * fd * theta / div;
            }
            cond[i] = dcx;  // 存入输出数组
            PARA_EXEC(prog_bar.count());
        }
    }

private:
    // ========================================================================
    //  gamma_matrix: 计算 Γ 矩阵 (CPC 论文 eq.69)
    // ========================================================================
    // 【物理背景】
    // Γ_{mn}(θ) 是 Kubo-Bastin 公式中的几何因子。经过变量替换 E → cos θ 后,
    // 它的形式是:
    //   Γ_{mn}(θ) = cos(mθ)·(cosθ + i·m·sinθ)·e^{-imθ}
    //             + cos(nθ)·(cosθ - i·n·sinθ)·e^{+inθ}
    // 注意: 代码中的公式与上面符号可能差一个共轭, 但最终电导率只取实部所以不影响。
    //
    // 【inline static】可以不依赖对象实例来调用, 函数体嵌入调用处。
    //
    // @param[in]  theta  角度 θ ∈ [0, π)
    // @param[out] gmn    Γ 矩阵, 必须在调用前分配好尺寸 (M × M)
    inline static void gamma_matrix(
        const double& theta,
        Eigen::MatrixXcd& gmn)
    {
        size_t num_kernel = gmn.cols();  // M = Chebyshev 截断阶数

        // Γ_{mn} 的公式:
        // cos(m*θ) * (cosθ - i*n*sinθ) * exp(i*n*θ)  +
        // cos(n*θ) * (cosθ + i*m*sinθ) * exp(-i*m*θ)
        double sin_t = std::sin(theta);  // sin θ (预先算好, 避免重复调用)
        double cos_t = std::cos(theta);  // cos θ
        // cos_nt[i] = cos(i × θ), 对所有 i 预先算好
        Eigen::VectorXd cos_nt(num_kernel);
        // fn[i] = (cosθ - i×n×sinθ) × exp(i×n×θ), 即上面公式中的第二行
        Eigen::VectorXcd fn(num_kernel);
        // fm[i] = (cosθ + i×m×sinθ) × exp(-i×m×θ) = conj(fn[i]), 即第一行的后半部分
        Eigen::VectorXcd fm(num_kernel);
        double nt = 0.0;  // n × θ
        int i = 0;
        int j = 0;

        // 第一个并行循环: 对每个 i, 计算 cos(iθ), fn[i], fm[i]
        // complex_t(a, b) 构造复数 a + i·b
        // std::conj(z) 取复数的共轭: conj(a+ib) = a-ib
#pragma omp parallel for private(nt)
        for (i = 0; i < num_kernel; ++i) {
            nt = static_cast<double>(i) * theta;           // nt = i × θ
            cos_nt[i] = std::cos(nt);                       // cos(iθ)
            // fn[i] = (cosθ - i × i × sinθ) × (cos(iθ) + i × sin(iθ))
            // = (cosθ - i × i × sinθ) × exp(i × i × θ)
            fn[i] = complex_t(cos_t, -i * sin_t) * complex_t(cos_nt[i], std::sin(nt));
            // fm[i] = fn[i] 的复共轭 = (cosθ + i × i × sinθ) × exp(-i × i × θ)
            fm[i] = std::conj(fn[i]);
        }

        // 第二个并行循环: 组装 Γ_{mn}(θ) = cos(mθ)·fn(n) + cos(nθ)·fm(m)
#pragma omp parallel for private(i)
        for (j = 0; j < num_kernel; ++j) {
            for (i = 0; i < num_kernel; ++i) {
                gmn(i, j) = cos_nt[i] * fn(j) + cos_nt[j] * fm(i);
            }
        }
    }

};

// ============================================================================
//           CPU 实现: KuboBastinCPU<sparse_t>
// ============================================================================
// 【final】关键字表示该类不能再被别的类继承, 是"最终"实现。
// 继承自 AbstractKuboBastin<sparse_t>, 必须实现所有纯虚函数。
//
// 【与基类的关系】
// AbstractKuboBastin 定义"做什么" (接口),
// KuboBastinCPU    定义"怎么做" (具体算法)。
// 将来如果要写 GPU 版本, 只需再写一个 KuboBastinCUDA 类即可。
template <typename sparse_t>
class KuboBastinCPU final : public AbstractKuboBastin<sparse_t> {
public:
    // ========================================================================
    //  kbdc_mu: 计算 μ_{mn} — Chebyshev 展开系数 (带 Jackson 核加权)
    // ========================================================================
    // 【算法概述】
    // CPC 论文 eq.70 的核心公式:
    //   μ_{mn} = (1/Nsamples) Σ_{samples} <v_α·T_m(H)·r|  v_β·T_n(H)|r>
    // 其中 |r> 是随机态, T_n(H) 是第 n 阶切比雪夫多项式在 H 上的取值。
    // 这个公式用随机态近似了矩阵的迹 (trace):
    //   Tr[A·v_x·B·v_y] ≈ (1/R) Σ_r <r|A·v_x·B·v_y|r>
    //
    // 【代码结构】
    // 对每个随机样本:
    //   a) 生成随机态 |r>, 用切比雪夫递推计算 v_β·T_n(H)|r> (n=0,1,...,M-1)
    //   b) 用切比雪夫递推计算 T_m(H)·v_α|r> (m=0,1,...,M-1)
    //   c) 内积: μ_sample(m,n) = <T_m(H)·v_α|r|  v_β·T_n(H)|r>
    //   d) 乘上 Jackson 核并累加到平均值
    //
    // final = 重写 (override) 基类的纯虚函数, 且禁止子类进一步重写。
    void kbdc_mu(
        const sparse_t& h_sparse,
        const sparse_t& curr_x,
        const sparse_t& curr_y,
        const TBPMConfig& config,
        const TBPMMeta& meta,
        Eigen::MatrixXcd& mu_avg) final
    {
        PARA_EXEC(std::cout << "Calculating mu of DC conductivity." << std::endl);

        // ================================================================
        //  初始化: 波函数和中间变量
        // ================================================================
        // n_wf: 向量维度 = 哈密顿量矩阵的行数 (即系统自由度)
        size_t n_wf = h_sparse.get_dim();
        int num_kernel = config.dckb_num_kernel;  // M: Chebyshev 截断阶数
        // |r>: 随机初始态 (样本态的起点)
        Eigen::VectorXcd wf0(n_wf);
        // t0, t1: 切比雪夫递推的缓冲变量, 分别存 T_{k-1} 和 T_k 作用在态上的结果
        Eigen::VectorXcd t0(n_wf);
        Eigen::VectorXcd t1(n_wf);
        // wf_vb_tn[n] = v_β · T_n(H) |r>, 共 M 个向量
        // 为什么叫 vb? 因为电流算符有 v_x 和 v_y, β 表示取其中一个方向
        std::vector<Eigen::VectorXcd> wf_vb_tn;
        mat_alloc(wf_vb_tn, n_wf, num_kernel);  // 一次分配 M 个 n_wf 维向量

        // ================================================================
        //  初始化: μ 矩阵
        // ================================================================
        // mu_avg: 最终输出, 所有样本的平均 μ_{mn} (带 Jackson 核)
        mu_avg = Eigen::MatrixXcd::Zero(num_kernel, num_kernel);
        // mu_sample: 单个样本的 μ_{mn} (会被重复覆盖)
        Eigen::MatrixXcd mu_sample(num_kernel, num_kernel);

        // ================================================================
        //  初始化: 随机数生成器 & 进度条
        // ================================================================
        // RandomGenerator 封装了随机数生成逻辑
        RandomGenerator rand_gen(config.seed);
        ProgressBar prog_bar(num_kernel, 256, "Finished i");

        // ================================================================
        //  预计算 Jackson 核系数
        // ================================================================
        // 注意: kernel[0] 额外 × 0.5, 这是 CPC eq.70 中因子 1/(1+δ_{0,n}) 的体现
        // (Kronecker δ: 当 n=0 时分母 = 2, 所以权重 = 1/2)
        Eigen::VectorXd kernel(num_kernel);
        jackson_kernel(kernel);     // 从 kpm.h 获取 Jackson 核
        kernel[0] *= 0.5;           // 0 阶特殊处理

        // ================================================================
        //  主循环: 对每个随机样本重复
        // ================================================================
        // num_samples_dist: 当前 MPI 进程分配的样本数
        // mpi_rank: 当前进程在 MPI 通信中的编号 (0 号是主进程)
        int num_samples = meta.num_samples_dist;
        int rank = meta.mpi_rank;
        for (int i_sample = 1; i_sample <= num_samples; ++i_sample) {
            PARA_EXEC(std::cout << "Sample " << i_sample << " of " << num_samples << std::endl);
            // 为保证不同 MPI 进程的随机种子不重复, 把 rank 也乘进去
            int seed_i = config.seed * (i_sample + rank * num_samples);
            PARA_EXEC(prog_bar.reset());

            // ============================================================
            //  步骤 A: 计算 v_β·T_n(H)|r>   (n = 0, 1, ..., M-1)
            // ============================================================
            // 思路:
            //  - 先生成随机态 |r>
            //  - 用切比雪夫递推 T_{n+1}(H) = 2H·T_n(H) - T_{n-1}(H)
            //    逐步生成 T_0|r>, T_1|r>, T_2|r>, ...
            //  - 每一步把电流算符 v_β 作用上去, 存入 wf_vb_tn[n]
            PARA_EXEC(std::cout << "Evaluating v_beta*Tn(H)|wf0>." << std::endl);
            rand_gen.random_state(wf0, seed_i);  // 生成随机态 |r>
            vec_copy(wf0, t0);                    // t0 = |r> = T_0(H)|r> (因为 T_0(x)=1)
            h_sparse.mv(t0, t1);                  // t1 = H·|r> = T_1(H)|r> (因为 T_1(x)=x)
            // 确定 β 方向: dckb_component==1 取 x, 否则取 y
            // curr_beta 是指向相应电流算符的指针 (避免拷贝大矩阵)
            const sparse_t* curr_beta = nullptr;
            if (config.dckb_component == 1) {
                curr_beta = &curr_x;
            } else {
                curr_beta = &curr_y;
            }
            // v_β 作用在 T_0|r> 和 T_1|r> 上
            curr_beta->mv(t0, wf_vb_tn[0]);  // wf_vb_tn[0] = v_β·T_0(H)|r>
            curr_beta->mv(t1, wf_vb_tn[1]);  // wf_vb_tn[1] = v_β·T_1(H)|r>
            PARA_EXEC(prog_bar.count());      // 进度+1
            PARA_EXEC(prog_bar.count());      // 进度+1

            // 指针轮转技巧: 用 3 个指针 p0, p1, p2 轮转, 避免频繁拷贝大向量
            // p0 → T_{n-1},  p1 → T_n,  p2 → T_{n+1}
            // 初始: p0 = &t0 (存 T_{n-1}), p1 = &t1 (存 T_n)
            Eigen::VectorXcd* p0 = &t0;
            Eigen::VectorXcd* p1 = &t1;
            Eigen::VectorXcd* p2 = nullptr;
            for (int i = 2; i < num_kernel; ++i) {
                p2 = p0;  // 复用 p0 的内存给 p2 (即 T_{n+1})
                // amxsy(a, x, y): 计算 y = a*H*x - y, 即切比雪夫递推的核心
                h_sparse.amxsy(2.0, *p1, *p0);  // *p2 = 2*H·T_n|r> - T_{n-1}|r> = T_{n+1}|r>
                curr_beta->mv(*p2, wf_vb_tn[i]); // wf_vb_tn[i] = v_β·T_i(H)|r>
                // 轮转:  p0 ← p1,  p1 ← p2
                p0 = p1;
                p1 = p2;
                PARA_EXEC(prog_bar.count());
            }

            // ============================================================
            //  步骤 B: 计算 T_m(H)·v_α|r> 并与步骤A的结果做内积
            // ============================================================
            // 和步骤A对称: 用切比雪夫递推计算 T_m(H)·(v_α|r>)
            // 然后内积: μ_sample(m,n) = <T_m·v_α|r|  v_β·T_n|r>
            // 注意: 当前 α 固定为 x 方向 (curr_alpha = &curr_x)
            PARA_EXEC(std::cout << "Evaluating Tm(H)*v_alpha|wf0> and mu" << std::endl);
            PARA_EXEC(prog_bar.reset());
            const sparse_t* curr_alpha = &curr_x;  // α = x
            curr_alpha->mv(wf0, t0);                // t0 = v_α|r>
            h_sparse.mv(t0, t1);                     // t1 = H·v_α|r> = T_1(H)·v_α|r>
            // 手算 m=0 和 m=1 的情况 (因为递推公式需要前面两项)
            for (int j = 0; j < num_kernel; ++j) {
                mu_sample(0, j) = vec_dot(t0, wf_vb_tn[j]);  // <v_α·r| v_β·T_n|r>
            }
            for (int j = 0; j < num_kernel; ++j) {
                mu_sample(1, j) = vec_dot(t1, wf_vb_tn[j]);  // <T_1·v_α·r| v_β·T_n|r>
            }
            PARA_EXEC(prog_bar.count());
            PARA_EXEC(prog_bar.count());

            // 重新绑定指针: 这步至关重要! 因为循环中 p0/p1/p2 被重新赋值了
            p0 = &t0;
            p1 = &t1;
            p2 = nullptr;
            // 递推: T_{m+1}·v_α|r> = 2H·T_m·v_α|r> - T_{m-1}·v_α|r>
            for (int i = 2; i < num_kernel; ++i) {
                p2 = p0;
                h_sparse.amxsy(2.0, *p1, *p0);  // 切比雪夫递推
                // 内积 μ_sample(i,j) = <T_i·v_α|r|  v_β·T_j|r>
                for (int j = 0; j < num_kernel; ++j) {
                    mu_sample(i, j) = vec_dot(*p2, wf_vb_tn[j]);
                }
                p0 = p1;
                p1 = p2;
                PARA_EXEC(prog_bar.count());
            }

            // ============================================================
            //  步骤 C: 乘 Jackson 核并累加到平均值
            // ============================================================
            // factor = 1 / 样本总数: 将累加变为平均
            // 注: CPC 论文 eq.70 写的是 μ_{nm} 而非 μ_{mn}, 但交换 m,n 不影响
            //     最终结果 (Γ 矩阵是对称的), 所以这里直接用 μ_{mn}。
            double factor = 1.0 / static_cast<double>(num_samples);
            int n = 0;
#pragma omp parallel for private(n)
            for (int m = 0; m < num_kernel; ++m) {
                for (n = 0; n < num_kernel; ++n) {
                    mu_avg(m, n) += factor * kernel(m) * kernel(n) * mu_sample(m, n);
                }
            }
        }
    }

    // ========================================================================
    //  kbdc_mu_raw: 计算原始 Chebyshev 展开系数 μ_{mn} (不带 Jackson 核)
    // ========================================================================
    // 【与 kbdc_mu 的区别】
    // 算法流程完全相同, 唯一的区别在于最后一步: 只做样本平均, 不乘 Jackson 核。
    // 这样做的好处是你可以把原始系数保存下来, 以后用不同的截断阶数 M' ≤ M
    // 重新做核加权 (先 truncate_mu, 再 apply_jackson_kernel), 而不用重新跑昂贵的随机采样。
    //
    // 【使用场景】
    // 当你不确定该用多大的 Chebyshev 截断阶数 M 时:
    //   1. 先用一个大 M (如 8000) 跑 kbdc_mu_raw, 把 raw μ 存盘。
    //   2. 之后尝试 M' = 2000, 4000, 6000 的效果:
    //      truncate_mu(raw_mu_8000, mu_4000, 4000);  // 截断
    //      apply_jackson_kernel(mu_4000, 4000);       // 核加权
    //      cond_from_trace(config, meta, mu_4000, cond);  // 求电导率
    //   3. 比较不同 M' 的结果, 选最合适的。
    //
    // 【TBPLAS_NORM_DIAG 诊断宏】
    // 当定义 TBPLAS_NORM_DIAG 时, 每 128 步打印一次切比雪夫向量的范数 (取 log10)。
    // 范数太大 → 递推可能数值发散; 范数太小 → 可能下溢。用于调试收敛性。
    //
    // @param[in]  h_sparse  缩放后的稀疏 Hamiltonian 矩阵 H̃ = (H - b)/a
    // @param[in]  curr_x    x 方向的电流算符 (稀疏矩阵)
    // @param[in]  curr_y    y 方向的电流算符 (稀疏矩阵)
    // @param[in]  config    用户设定的计算配置 (截断阶数、能量网格等)
    // @param[in]  meta      运行时元信息 (样本数、MPI 进程编号、缩放参数等)
    // @param[out] mu_raw    输出的原始 μ_{mn} 矩阵, 尺寸 (M × M), 未加权
    void kbdc_mu_raw(
        const sparse_t& h_sparse,
        const sparse_t& curr_x,
        const sparse_t& curr_y,
        const TBPMConfig& config,
        const TBPMMeta& meta,
        Eigen::MatrixXcd& mu_raw) final
    {
        PARA_EXEC(std::cout << "Calculating raw mu of DC conductivity (no Jackson kernel)." << std::endl);

        // ================================================================
        //  初始化: 波函数和中间变量 (与 kbdc_mu 完全相同)
        // ================================================================
        size_t n_wf = h_sparse.get_dim();          // 系统自由度 (向量维度)
        int num_kernel = config.dckb_num_kernel;    // Chebyshev 截断阶数 M
        Eigen::VectorXcd wf0(n_wf);                 // |r>: 随机初始态
        Eigen::VectorXcd t0(n_wf);                  // 切比雪夫递推缓冲 T_{k-1}
        Eigen::VectorXcd t1(n_wf);                  // 切比雪夫递推缓冲 T_k
        std::vector<Eigen::VectorXcd> wf_vb_tn;     // wf_vb_tn[n] = v_β · T_n(H) |r>
        mat_alloc(wf_vb_tn, n_wf, num_kernel);     // 一次性分配 M 个 n_wf 维复数向量

        // ================================================================
        //  初始化: μ 矩阵 (注意: 这里没有 Jackson 核系数)
        // ================================================================
        mu_raw = Eigen::MatrixXcd::Zero(num_kernel, num_kernel);    // 累加器, 最终输出
        Eigen::MatrixXcd mu_sample(num_kernel, num_kernel);          // 单样本临时结果

        // ================================================================
        //  初始化: 随机数生成器 & 进度条
        // ================================================================
        RandomGenerator rand_gen(config.seed);
        ProgressBar prog_bar(num_kernel, 256, "Finished i");

        // ================================================================
        //  主循环: 对每个随机样本重复
        // ================================================================
        // 与 kbdc_mu 的流程完全相同, 只是在最后一步不乘 Jackson 核。
        int num_samples = meta.num_samples_dist;  // 本 MPI 进程分配的样本数
        int rank = meta.mpi_rank;                  // MPI 进程编号
        for (int i_sample = 1; i_sample <= num_samples; ++i_sample) {
            PARA_EXEC(std::cout << "Sample " << i_sample << " of " << num_samples << std::endl);
            // 每个进程用不同的随机种子, 保证样本不重复
            int seed_i = config.seed * (i_sample + rank * num_samples);
            PARA_EXEC(prog_bar.reset());

            // ---- 步骤 A: 计算 v_β·T_n(H)|r>  (n = 0, 1, ..., M-1) ----
            PARA_EXEC(std::cout << "Evaluating v_beta*Tn(H)|wf0>." << std::endl);
            rand_gen.random_state(wf0, seed_i);    // 生成随机态 |r>
            vec_copy(wf0, t0);                      // t0 = T_0(H)|r> = |r>
            h_sparse.mv(t0, t1);                    // t1 = T_1(H)|r> = H|r>
            // 选择 β 方向 (x 或 y)
            const sparse_t* curr_beta = nullptr;
            if (config.dckb_component == 1) {
                curr_beta = &curr_x;   // β = x
            } else {
                curr_beta = &curr_y;   // β = y
            }
            // 电流算符作用在 T_0 和 T_1 上 (手算前两项, 给递推提供初始值)
            curr_beta->mv(t0, wf_vb_tn[0]);    // v_β · T_0(H) |r>
            curr_beta->mv(t1, wf_vb_tn[1]);    // v_β · T_1(H) |r>
            PARA_EXEC(prog_bar.count());
            PARA_EXEC(prog_bar.count());

            // 指针轮转递推: p0↔T_{n-1}, p1↔T_n, p2↔T_{n+1}
            // 用指针替换而非拷贝向量的原因: 向量维度可能达到百万级, 拷贝代价太大
            Eigen::VectorXcd* p0 = &t0;
            Eigen::VectorXcd* p1 = &t1;
            Eigen::VectorXcd* p2 = nullptr;
            for (int i = 2; i < num_kernel; ++i) {
                p2 = p0;  // 复用 p0 的内存, 存入 T_{i}(H)|r>
                // amxsy(2.0, *p1, *p0): *p0 = 2*H*(*p1) - *p0
                // 即 Chebyshev 递推: T_{i} = 2H·T_{i-1} - T_{i-2}
                h_sparse.amxsy(2.0, *p1, *p0);
#ifdef TBPLAS_NORM_DIAG
                // ====================================================
                // 【诊断模式】检查切比雪夫向量的范数是否异常
                // 如果 log10|T_n| 增长 → 递推不稳定 (数值发散)
                // 如果 log10|T_n| 趋近 -300 → 下溢 (向量变成零)
                // ====================================================
                if (i % 128 == 0 || i == num_kernel - 1) {
                    double norm_vec = p2->norm();
                    std::cout << "[NORM_DIAG] loop_beta n=" << i
                              << " log10|T_n|=" << std::log10(std::max(norm_vec, 1e-300))
                              << std::endl;
                }
#endif
                curr_beta->mv(*p2, wf_vb_tn[i]);   // v_β · T_i(H) |r>
                // 轮转指针: T_{i-2} 的内存给 T_{i+1} 用
                p0 = p1;
                p1 = p2;
                PARA_EXEC(prog_bar.count());
            }

            // ---- 步骤 B: 计算 T_m(H)·v_α|r> 并与步骤 A 的结果做内积 ----
            PARA_EXEC(std::cout << "Evaluating Tm(H)*v_alpha|wf0> and mu" << std::endl);
            PARA_EXEC(prog_bar.reset());
            const sparse_t* curr_alpha = &curr_x;   // α = x (固定取 x 方向)
            curr_alpha->mv(wf0, t0);                 // t0 = v_α|r>
            h_sparse.mv(t0, t1);                      // t1 = H·v_α|r> = T_1(H)·v_α|r>
            // 手算 m = 0 和 m = 1 (递推需要前两项)
            // mu_sample(m,n) = <T_m(H)·v_α·r | v_β·T_n(H)·r>
            for (int j = 0; j < num_kernel; ++j) {
                mu_sample(0, j) = vec_dot(t0, wf_vb_tn[j]);
            }
            for (int j = 0; j < num_kernel; ++j) {
                mu_sample(1, j) = vec_dot(t1, wf_vb_tn[j]);
            }
            PARA_EXEC(prog_bar.count());
            PARA_EXEC(prog_bar.count());

            // 重新绑定指针 (上一步循环中 p0/p1/p2 已被修改)
            p0 = &t0;
            p1 = &t1;
            p2 = nullptr;
            for (int i = 2; i < num_kernel; ++i) {
                p2 = p0;
                h_sparse.amxsy(2.0, *p1, *p0);   // Chebyshev 递推: T_m
#ifdef TBPLAS_NORM_DIAG
                if (i % 128 == 0 || i == num_kernel - 1) {
                    double norm_vec = p2->norm();
                    std::cout << "[NORM_DIAG] loop_alpha n=" << i
                              << " log10|T_n|=" << std::log10(std::max(norm_vec, 1e-300))
                              << std::endl;
                }
#endif
                // 内积: μ_sample(i,j) = <T_i·v_α·r | v_β·T_j·r>
                for (int j = 0; j < num_kernel; ++j) {
                    mu_sample(i, j) = vec_dot(*p2, wf_vb_tn[j]);
                }
                p0 = p1;
                p1 = p2;
                PARA_EXEC(prog_bar.count());
            }

            // ---- 步骤 C: 样本平均 (注意: 不乘 Jackson 核!) ----
            // kbdc_mu 在这里会乘 kernel(m)*kernel(n), 但 kbdc_mu_raw 不乘。
            // 这样保留了"原始"展开系数, 后续可以灵活选择不同的 M' 和核函数。
            double factor = 1.0 / static_cast<double>(num_samples);  // 1 / 样本总数
            int n = 0;
#pragma omp parallel for private(n)
            for (int m = 0; m < num_kernel; ++m) {
                for (n = 0; n < num_kernel; ++n) {
                    mu_raw(m, n) += factor * mu_sample(m, n);  // 仅累加平均, 不乘核
                }
            }
        }
    }
};

} // namespace tbplas::tbpm
#endif // TBPLAS_TBPM_KUBO_BASTIN_H
