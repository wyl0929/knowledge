/*
 * @Author       : Yulong Wang
 * @Date         : 2026-06-26 20:45:04
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-26 20:45:05
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/kubo_bastin.h
 * @Description  :
 */
/**
 * @brief Functions for calculating DC conductivity using Kubo-Bastin method.
 *
 * @author Yunhai Li (liyunhai1016@hotmail.com)
 *
 * @copyright Copyright (c) 2024, TBPLaS develop team.
 */

#ifndef TBPLAS_TBPM_KUBO_BASTIN_H
#define TBPLAS_TBPM_KUBO_BASTIN_H

#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <ostream>
#include <vector>

#include <eigen3/Eigen/Dense>

#include "base/consts.h"
#include "base/datatypes.h"
#include "base/utils.h"
#include "config.h"
#include "dense.h"
#include "fermi_dirac.h"
#include "kpm.h"
#include "utils.h"

namespace tbplas::tbpm {
using tbplas::base::complex_t;
using tbplas::base::ProgressBar;

/**
 * @brief Abstract KuboBastin class.
 *
 * @tparam sparse_t datatype of sparse Hamiltonian matrix
 */
template <typename sparse_t>
class AbstractKuboBastin {
public:
    virtual void kbdc_mu(
        const sparse_t& h_sparse,
        const sparse_t& curr_x,
        const sparse_t& curr_y,
        const TBPMConfig& config,
        const TBPMMeta& meta,
        Eigen::MatrixXcd& mu_avg)
        = 0;

    /**
     * @brief Calculate raw \mu_{mn} WITHOUT Jackson kernel.
     *
     * Identical to kbdc_mu() except the Jackson kernel is NOT applied.
     */
    virtual void kbdc_mu_raw(
        const sparse_t& h_sparse,
        const sparse_t& curr_x,
        const sparse_t& curr_y,
        const TBPMConfig& config,
        const TBPMMeta& meta,
        Eigen::MatrixXcd& mu_raw)
        = 0;

    /**
     * @brief Apply Jackson kernel to raw Chebyshev moments in-place.
     *
     * @param[inout] mu raw \mu_{mn} matrix, overwritten with kernel-weighted values
     * @param[in]    num_kernel number of Chebyshev moments (M)
     *
     * @note The Jackson kernel includes the 1/(1+\delta_{0,n}) factor on g_0
     *       (the 0.5 factor from eqn.70 of CPC paper).
     */
    inline static void apply_jackson_kernel(
        Eigen::MatrixXcd& mu,
        int num_kernel)
    {
        Eigen::VectorXd kernel(num_kernel);
#ifdef TBPLAS_LORENTZ_KERNEL
        lorentz_kernel(kernel);
#else
        jackson_kernel(kernel);
#endif
        kernel[0] *= 0.5;
        int m = 0, n = 0;
#pragma omp parallel for private(n)
        for (m = 0; m < num_kernel; ++m) {
            for (n = 0; n < num_kernel; ++n) {
                mu(m, n) *= kernel(m) * kernel(n);
            }
        }
    }

    /**
     * @brief Truncate a larger \mu matrix to a smaller M.
     *
     * @param[in]  mu_large         source \mu matrix, dim (M_large, M_large)
     * @param[out] mu_small         target \mu matrix, dim (M_small, M_small)
     * @param[in]  num_kernel_small target M_small (must be <= M_large)
     */
    inline static void truncate_mu(
        const Eigen::MatrixXcd& mu_large,
        Eigen::MatrixXcd& mu_small,
        int num_kernel_small)
    {
        mu_small = mu_large.topLeftCorner(num_kernel_small, num_kernel_small);
    }

    /**
     * @brief Calculate DC conductivity from \mu_{mn}.
     *
     * @param[in] config user-defined calculation configurations
     * @param[in] meta additional meta info.
     * @param[in] mu_avg averaged \mu_{mn}, dimension (num_kernel, num_kernel)
     * @param[out] cond DC conductivity, has same length as TBPMConfig::dckb_energies
     */
    inline void cond_from_trace(
        const TBPMConfig& config,
        const TBPMMeta& meta,
        const Eigen::MatrixXcd& mu_avg,
        Eigen::VectorXd& cond)
    {
        // Initialize DC conductivity
        size_t num_eng = config.dckb_energies.size();
        cond = Eigen::VectorXd::Zero(num_eng);

        // Local variables
        int num_theta = config.dckb_num_integ_steps;
        int num_kernel = config.dckb_num_kernel;
#ifdef TBPLAS_LONG_DOUBLE
        // Phase I: use long double (80-bit) for accumulation paths
        std::vector<long double> theta_array(num_theta);
        std::vector<long double> sum_gamma_mu(num_theta);
#else
        Eigen::VectorXd theta_array(num_theta);
        Eigen::VectorXd sum_gamma_mu(num_theta);
#endif
        Eigen::MatrixXcd gamma(num_kernel, num_kernel);

        // Utilities
        ProgressBar prog_bar(num_theta, 256, "Finished energy");

        // Sum up gamma * mu over m,n
        PARA_EXEC(std::cout << "Calculating sum." << std::endl);
#ifdef TBPLAS_LONG_DOUBLE
        long double theta = base::PI / static_cast<long double>(num_theta);
#else
        double theta = base::PI / num_theta;
#endif
        for (int k = 0; k < num_theta; ++k) {
            theta_array[k] = (k + 0.5) * theta; // Shift by 0.5 to avoid k = 0

            // Get Gamma matrix
#ifdef TBPLAS_LONG_DOUBLE
            gamma_matrix(static_cast<double>(theta_array[k]), gamma);
#else
            gamma_matrix(theta_array[k], gamma);
#endif

            // Summation
#ifdef TBPLAS_LONG_DOUBLE
            long double sum = 0.0L;
#else
            double sum = 0.0;
#endif
            int i = 0;
            int j = 0;
#pragma omp parallel for private(i) reduction(+ : sum)
            for (j = 0; j < num_kernel; ++j) {
                for (i = 0; i < num_kernel; ++i) {
                    sum += (gamma(i, j) * mu_avg(i, j)).real();
                }
            }
            sum_gamma_mu[k] = sum;

            PARA_EXEC(prog_bar.count());
        }

        // Integrate over energies
        PARA_EXEC(std::cout << "Final integration." << std::endl);
        PARA_EXEC(prog_bar.reset(num_eng, 10, "Finished energy"));
        for (int i = 0; i < num_eng; ++i) {
#ifdef TBPLAS_LONG_DOUBLE
            long double dcx = 0.0L;
            long double efermi_re = (config.dckb_energies[i] - meta.rescale_center) / meta.rescale;
            long double eng_re = 0.0L;
            long double div = 0.0L;
            long double fd = 0.0L;
#pragma omp parallel for private(eng_re, div, fd) reduction(+ : dcx)
            for (int k = 0; k < num_theta; ++k) {
                eng_re = std::cos(theta_array[k]);
                div = std::pow(std::sin(theta_array[k]), 3);
                fd = static_cast<long double>(fermi_dirac(meta.beta_re,
                    static_cast<double>(efermi_re),
                    static_cast<double>(eng_re)));
                dcx += sum_gamma_mu[k] * fd * theta / div;
            }
            cond[i] = static_cast<double>(dcx);
#else
            double dcx = 0.0;
            double efermi_re = (config.dckb_energies[i] - meta.rescale_center) / meta.rescale;
            double eng_re = 0.0;
            double div = 0.0;
            double fd = 0.0;
#pragma omp parallel for private(eng_re, div, fd) reduction(+ : dcx)
            for (int k = 0; k < num_theta; ++k) {
                eng_re = std::cos(theta_array[k]);
                div = std::pow(std::sin(theta_array[k]), 3);
                fd = fermi_dirac(meta.beta_re, efermi_re, eng_re);
                dcx += sum_gamma_mu[k] * fd * theta / div;
            }
            cond[i] = dcx;
#endif
            PARA_EXEC(prog_bar.count());
        }
    }

private:
    /**
     * @brief Get the Gamma matrix in eqn.69 of TBPLaS CPC paper after
     * the substitution: E->cos(theta), theta = [0, pi].
     *
     * @param[in] theta angle theta
     * @param[inout] gmn Gamma matrix
     *
     * @note gmn must be pre-allocated before calling this function.
     */
    inline static void gamma_matrix(
        const double& theta,
        Eigen::MatrixXcd& gmn)
    {
        size_t num_kernel = gmn.cols();

        // The formula of \Gamma_{mn} after the substitution E->cos(theta) is:
        // cos(m * theta) * (cos(theta) - i * n * sin(theta)) * exp(i * n * theta) +
        // cos(n * theta) * (cos(theta) + i * m * sin(theta)) * exp(-i * m * theta)
        double sin_t = std::sin(theta);
        double cos_t = std::cos(theta);
        Eigen::VectorXd cos_nt(num_kernel); // cos(n * theta)
        Eigen::VectorXcd fn(num_kernel); // (cos(theta) - i * n * sin(theta)) * exp(i * n * theta)
        Eigen::VectorXcd fm(num_kernel); // (cos(theta) + i * m * sin(theta)) * exp(-i * m * theta)
        double nt = 0.0;
        int i = 0;
        int j = 0;

#pragma omp parallel for private(nt)
        for (i = 0; i < num_kernel; ++i) {
            nt = static_cast<double>(i) * theta;
            cos_nt[i] = std::cos(nt);
            fn[i] = complex_t(cos_t, -i * sin_t) * complex_t(cos_nt[i], std::sin(nt));
            fm[i] = std::conj(fn[i]);
        }

#pragma omp parallel for private(i)
        for (j = 0; j < num_kernel; ++j) {
            for (i = 0; i < num_kernel; ++i) {
                gmn(i, j) = cos_nt[i] * fn(j) + cos_nt(j) * fm(i);
            }
        }
    }

};

template <typename sparse_t>
class KuboBastinCPU final : public AbstractKuboBastin<sparse_t> {
public:
    /**
     * @brief Calculate \mu_{mn} in eqn.70 of CPC paper.
     *
     * @param[in] h_sparse scaled sparse Hamiltonian
     * @param[in] curr_x sparse current operator along x direction
     * @param[in] curr_y sparse current operator along y direction
     * @param[in] config user-defined calculation configurations
     * @param[in] meta additional meta info.
     * @param[out] mu_avg averaged \mu_{mn}, dimension (num_kernel, num_kernel)
     */
    void kbdc_mu(
        const sparse_t& h_sparse,
        const sparse_t& curr_x,
        const sparse_t& curr_y,
        const TBPMConfig& config,
        const TBPMMeta& meta,
        Eigen::MatrixXcd& mu_avg) final
    {
        PARA_EXEC(std::cout << "Calculating mu of DC conductivity." << std::endl);

        // Initialize wave functions
        size_t n_wf = h_sparse.get_dim();
        int num_kernel = config.dckb_num_kernel;
        Eigen::VectorXcd wf0(n_wf); // Initial random state
        Eigen::VectorXcd t0(n_wf); // Tn(H)|wf0> and Tm(H)*v_alpha|wf0>
        Eigen::VectorXcd t1(n_wf); // Tn(H)|wf0> and Tm(H)*v_alpha|wf0>
        std::vector<Eigen::VectorXcd> wf_vb_tn; // v_beta*Tn(H)|wf0>
        mat_alloc(wf_vb_tn, n_wf, num_kernel);

        // Initialize correlation functions
        mu_avg = Eigen::MatrixXcd::Zero(num_kernel, num_kernel);
        Eigen::MatrixXcd mu_sample(num_kernel, num_kernel);

        // Initialize utilities
        RandomGenerator rand_gen(config.seed);
        ProgressBar prog_bar(num_kernel, 256, "Finished i");

        // Get Jackson kernel (or Lorentz kernel if TBPLAS_LORENTZ_KERNEL is defined)
        // First element has a factor of 0.5 due to the 1/(1+\delta(0,n)) factor in eqn.70.
        Eigen::VectorXd kernel(num_kernel);
#ifdef TBPLAS_LORENTZ_KERNEL
        lorentz_kernel(kernel);
#else
        jackson_kernel(kernel);
#endif
        kernel[0] *= 0.5;

        // Main loop
        int num_samples = meta.num_samples_dist;
        int rank = meta.mpi_rank;
        for (int i_sample = 1; i_sample <= num_samples; ++i_sample) {
            PARA_EXEC(std::cout << "Sample " << i_sample << " of " << num_samples << std::endl);
            int seed_i = config.seed * (i_sample + rank * num_samples);
            PARA_EXEC(prog_bar.reset());

            // Evaluate v_beta*Tn(H)|wf0> and save to wf_tb_vn
            PARA_EXEC(std::cout << "Evaluating v_beta*Tn(H)|wf0>." << std::endl);
            rand_gen.random_state(wf0, seed_i);
            vec_copy(wf0, t0);
            h_sparse.mv(t0, t1);
            const sparse_t* curr_beta = nullptr;
            if (config.dckb_component == 1) {
                curr_beta = &curr_x;
            } else {
                curr_beta = &curr_y;
            }
            curr_beta->mv(t0, wf_vb_tn[0]);
            curr_beta->mv(t1, wf_vb_tn[1]);
            PARA_EXEC(prog_bar.count());
            PARA_EXEC(prog_bar.count());
            Eigen::VectorXcd* p0 = &t0;
            Eigen::VectorXcd* p1 = &t1;
            Eigen::VectorXcd* p2 = nullptr;
            for (int i = 2; i < num_kernel; ++i) {
                p2 = p0;
                h_sparse.amxsy(2.0, *p1, *p0); // p2 = 2 * H * p1 - p0
                curr_beta->mv(*p2, wf_vb_tn[i]);
                p0 = p1;
                p1 = p2;
                PARA_EXEC(prog_bar.count());
            }

            // Evaluate Tm(H)*v_alpha|wf0> and mu
            PARA_EXEC(std::cout << "Evaluating Tm(H)*v_alpha|wf0> and mu" << std::endl);
            PARA_EXEC(prog_bar.reset());
            const sparse_t* curr_alpha = &curr_x; // Currently alpha = x
            curr_alpha->mv(wf0, t0);
            h_sparse.mv(t0, t1);
            for (int j = 0; j < num_kernel; ++j) {
                mu_sample(0, j) = vec_dot(t0, wf_vb_tn[j]);
            }
            for (int j = 0; j < num_kernel; ++j) {
                mu_sample(1, j) = vec_dot(t1, wf_vb_tn[j]);
            }
            PARA_EXEC(prog_bar.count());
            PARA_EXEC(prog_bar.count());
            // Rebind pointers. This is essential.
            p0 = &t0;
            p1 = &t1;
            p2 = nullptr;
            for (int i = 2; i < num_kernel; ++i) {
                p2 = p0;
                h_sparse.amxsy(2.0, *p1, *p0); // p2 = 2 * H * p1 - p0
                for (int j = 0; j < num_kernel; ++j) {
                    mu_sample(i, j) = vec_dot(*p2, wf_vb_tn[j]);
                }
                p0 = p1;
                p1 = p2;
                PARA_EXEC(prog_bar.count());
            }

            // Apply Jackson kernel and average
            // Note: eqn.70 of CPC paper is \mu_{nm} rather than \mu_{mn}. But it makes no sense
            // swapping m and n. Also, PRL 114, 116602 (2015) uses \mu_{mn}. So we do not take the
            // transpose here.
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

    /**
     * @brief Calculate raw \mu_{mn} WITHOUT Jackson kernel.
     *
     * Identical to kbdc_mu() except the Jackson kernel is NOT applied.
     * The raw moments can be saved, truncated, and later kernel-weighted
     * for any M' <= original num_kernel.
     *
     * @param[in]  h_sparse  scaled sparse Hamiltonian
     * @param[in]  curr_x    sparse current operator along x
     * @param[in]  curr_y    sparse current operator along y
     * @param[in]  config    user-defined calculation configurations
     * @param[in]  meta      additional meta info
     * @param[out] mu_raw    raw averaged \mu_{mn}, dim (num_kernel, num_kernel)
     *                       NO Jackson kernel applied
     */
    void kbdc_mu_raw(
        const sparse_t& h_sparse,
        const sparse_t& curr_x,
        const sparse_t& curr_y,
        const TBPMConfig& config,
        const TBPMMeta& meta,
        Eigen::MatrixXcd& mu_raw)
    {
        PARA_EXEC(std::cout << "Calculating raw mu of DC conductivity (no Jackson kernel)." << std::endl);

        // Initialize wave functions
        size_t n_wf = h_sparse.get_dim();
        int num_kernel = config.dckb_num_kernel;
        Eigen::VectorXcd wf0(n_wf);
        Eigen::VectorXcd t0(n_wf);
        Eigen::VectorXcd t1(n_wf);
        std::vector<Eigen::VectorXcd> wf_vb_tn;
        mat_alloc(wf_vb_tn, n_wf, num_kernel);

        // Initialize correlation functions
        mu_raw = Eigen::MatrixXcd::Zero(num_kernel, num_kernel);
        Eigen::MatrixXcd mu_sample(num_kernel, num_kernel);

        // Initialize utilities
        RandomGenerator rand_gen(config.seed);
        ProgressBar prog_bar(num_kernel, 256, "Finished i");

        // Main loop
        int num_samples = meta.num_samples_dist;
        int rank = meta.mpi_rank;
        for (int i_sample = 1; i_sample <= num_samples; ++i_sample) {
            PARA_EXEC(std::cout << "Sample " << i_sample << " of " << num_samples << std::endl);
            int seed_i = config.seed * (i_sample + rank * num_samples);
            PARA_EXEC(prog_bar.reset());

            // Evaluate v_beta*Tn(H)|wf0> and save to wf_tb_vn
            PARA_EXEC(std::cout << "Evaluating v_beta*Tn(H)|wf0>." << std::endl);
            rand_gen.random_state(wf0, seed_i);
            vec_copy(wf0, t0);
            h_sparse.mv(t0, t1);
            const sparse_t* curr_beta = nullptr;
            if (config.dckb_component == 1) {
                curr_beta = &curr_x;
            } else {
                curr_beta = &curr_y;
            }
            curr_beta->mv(t0, wf_vb_tn[0]);
            curr_beta->mv(t1, wf_vb_tn[1]);
            PARA_EXEC(prog_bar.count());
            PARA_EXEC(prog_bar.count());
            Eigen::VectorXcd* p0 = &t0;
            Eigen::VectorXcd* p1 = &t1;
            Eigen::VectorXcd* p2 = nullptr;
            for (int i = 2; i < num_kernel; ++i) {
                p2 = p0;
                h_sparse.amxsy(2.0, *p1, *p0);
#ifdef TBPLAS_NORM_DIAG
                if (i % 128 == 0 || i == num_kernel - 1) {
                    double norm_vec = p2->norm();
                    std::cout << "[NORM_DIAG] loop_beta n=" << i
                              << " log10|T_n|=" << std::log10(std::max(norm_vec, 1e-300))
                              << std::endl;
                }
#endif
                curr_beta->mv(*p2, wf_vb_tn[i]);
                p0 = p1;
                p1 = p2;
                PARA_EXEC(prog_bar.count());
            }

            // Evaluate Tm(H)*v_alpha|wf0> and mu
            PARA_EXEC(std::cout << "Evaluating Tm(H)*v_alpha|wf0> and mu" << std::endl);
            PARA_EXEC(prog_bar.reset());
            const sparse_t* curr_alpha = &curr_x;
            curr_alpha->mv(wf0, t0);
            h_sparse.mv(t0, t1);
            for (int j = 0; j < num_kernel; ++j) {
                mu_sample(0, j) = vec_dot(t0, wf_vb_tn[j]);
            }
            for (int j = 0; j < num_kernel; ++j) {
                mu_sample(1, j) = vec_dot(t1, wf_vb_tn[j]);
            }
            PARA_EXEC(prog_bar.count());
            PARA_EXEC(prog_bar.count());
            p0 = &t0;
            p1 = &t1;
            p2 = nullptr;
            for (int i = 2; i < num_kernel; ++i) {
                p2 = p0;
                h_sparse.amxsy(2.0, *p1, *p0);
#ifdef TBPLAS_NORM_DIAG
                if (i % 128 == 0 || i == num_kernel - 1) {
                    double norm_vec = p2->norm();
                    std::cout << "[NORM_DIAG] loop_alpha n=" << i
                              << " log10|T_n|=" << std::log10(std::max(norm_vec, 1e-300))
                              << std::endl;
                }
#endif
                for (int j = 0; j < num_kernel; ++j) {
                    mu_sample(i, j) = vec_dot(*p2, wf_vb_tn[j]);
                }
                p0 = p1;
                p1 = p2;
                PARA_EXEC(prog_bar.count());
            }

            // Average WITHOUT Jackson kernel
            double factor = 1.0 / static_cast<double>(num_samples);
            int n = 0;
#pragma omp parallel for private(n)
            for (int m = 0; m < num_kernel; ++m) {
                for (n = 0; n < num_kernel; ++n) {
                    mu_raw(m, n) += factor * mu_sample(m, n);
                }
            }
        }
    }
};

} // namespace tbplas::tbpm
#endif
