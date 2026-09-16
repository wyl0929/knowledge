<!--
 * @Author       : AI 精读 (research_onboarding_skill, Phase 4) → 2026-09-08 按 5 块演绎结构重写
 * @Date         : 2026-08-06（初读）→ 2026-09-08（5 块重写 + 反向核对）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T16_thomson2021_prb.md
 * @Description  : T16: Thomson & Alicea 2021 — 强相互作用 + 无序下电荷中性点无质量 Dirac 费米子的恢复（理论；2026-09-08 按五块演绎结构重写：模型白箱/推导链/结论清单/假设-结论依赖图/接口）
-->

# Paper Review: Thomson & Alicea (2021) — 强相互作用 + 无序下电荷中性点无质量 Dirac 费米子的恢复

| 字段 | 内容 |
|------|------|
| **编号** | T16 |
| **标题** | Recovery of massless Dirac fermions at charge neutrality in strongly interacting twisted bilayer graphene with disorder |
| **作者** | Alex Thomson, Jason Alicea |
| **期刊** | Physical Review B 103, 125138 (2021) |
| **DOI / arXiv** | 10.1103/PhysRevB.103.125138 / arXiv:1910.11348（⚠️ arXiv 号正文未出现，标外部来源） |
| **类型** | 理论 — 关联 + 无序网络机制（连续模型 + Dirac 理论 + 朗道-金兹堡/RFIM，无实验数据） |
| **课题组** | Caltech（IQIM / Walter Burke Institute） |
| **PDF** | ✅ `reference/pdfs/Thomson和Alicea - 2021 - Recovery of massless Dirac fermions at charge neutrality in strongly interacting twisted bilayer gra.pdf`（正文 29 页 + 附录） |
| **精读日期** | 2026-08-06（初读）→ 2026-09-08（5 块重写 + 反向核对） |

> **结构说明**：按「理论论文演绎结构」五块记（`note/shared/method/theory_paper_reading.md` §3）。**全文无 ±**：数字统一 📜Q[~]。

---

## TL;DR

**本文想解决的理论问题**：魔角 TBG 电荷中性点（CNP）处，为什么**同一体系**有的样品表现半金属、有的样品表现绝缘？（Cao/Yankowitz 半金属 vs Lu 绝缘 vs hBN 对齐绝缘）

**主结果**：① **统一机制**：强关联（干净极限下自发破 $C_2\mathcal T$、形成 Chern 数 $C=\pm1$ 的量子谷霍尔 QVH 态）+ **弱平滑无序**（破坏 $C_2$ 但平均保持）→ QVH 序参量**直接耦合**无序 → 随机拼贴的 QVH 畴（RFIM）📜Q；② 每条畴壁束缚 **4 右移 + 4 左移**模（自旋/谷扇区 Chern 数改变 ±2），网络 = **4 份 Chalker-Coddington 网络模型**（IQH 平台转变，$\delta\sigma_{xy}=\pm2e^2/h$）= **8 个无质量 Dirac 费米子**（每扇区 2 个）→ 恢复无质量 Dirac 费米子 📜Q；③ **尺寸判据**：$L<\xi_{dom}$（单畴）→ 绝缘（Lu）；$L\gg\xi_{dom}$（多畴渗流网络）→ 半金属（Cao/Yankowitz）；$L>\xi_{loc}$ → 局域化 📜Q。

**结论/意义**：无序在强关联体系中**不是破坏而是选择/掩盖**关联态——它能从近简并态中选出 QVH，并把局域绝缘体伪装成半金属 📜Q。⚠️ 全文为理论（propose / argue / expect），依赖"干净极限 QVH 近基态"的核心假设（A1）。

---

## 1. 模型白箱（理想系统 + 假设清单）

### 1.1 哈密顿量/作用量（低能 Dirac 理论 + 无序 + 库仑 + 伊辛/RFIM）

**连续模型 → 平带 Dirac 理论**：魔角 $\theta\approx1.1°$（正文取 $\theta=1.05°$），平带 4 重简并（自旋×谷），每个平带在 Moiré BZ 的 $\pm\kappa$ 处有无质量 Dirac 锥且**同手征** 📜Q。$C_2\mathcal T$ 变换 $c(k)\to\eta_x c(k),\ i\to-i$（Eq. 1），$C_2\mathcal T$ 不变平带哈密顿量 $H_0=\sum_k c^\dagger(k)[h_0+h_x\eta_x+h_y\eta_y]c(k)$（Eq. 2）📜Q。投影到 $\pm\kappa$ 得单谷 Dirac 哈密顿量：

$$
H_D=-v_F\psi^\dagger(i\partial_x\eta_x+i\partial_y\eta_y)\psi\tag{3}
$$

双谷（$\Psi=(\psi_+,\psi_-)^T$，$\mu$ 作用 K 谷指标，两谷手征相反）：

$$
H_{D,\mathrm{tot}}=-v_F\Psi^\dagger(i\partial_x\mu_z\eta_x+i\partial_y\eta_y)\Psi\tag{4}
$$

**质量项 → Chern 数**：质量项 $\psi^\dagger\eta_z M\psi$（$M\in\{1,\sigma_i,\tau_i,\tau_i\sigma_j\}$）；$\pm\kappa$ 两锥**同号质量 → $C=\pm1$**、反号质量 → $C=0$；$M=1,\sigma_i$ 给非零 Chern，$M=\tau_i,\tau_i\sigma_j$ 给平庸绝缘体 📜Q。QVH 态 = $\Psi^\dagger\eta_z\Psi$（一谷 $C=+1$ 双自旋、另一谷 $C=-1$ 双自旋，或反之）📜Q。

**无序**（弱、平滑、保 $\mathcal T$ 与自旋旋转）：$H_{dis}=\sum_r R_i(r)\Psi^\dagger T^i\Psi$（Eq. 5），$R_i$ 高斯关联 $\overline{R_iR_j}=\delta_{ij}g_i^2K_i$（Eq. 6），$K_i=e^{-r^2/(2\xi_i^2)}$（Eq. 7）📜Q。平滑性 $\xi_{dis}\gg a_M$ → 谷间（K↔K′）散射指数压低：

$$
g_{KK}\sim g\,e^{-K^2\xi_{dis}^2/4}=g\,e^{-4\pi^2\xi_{dis}^2/a^2}\tag{8}
$$

单 K 谷内最一般无序（Eq. 9）含质量 $M_0\eta_z+M_\tau\eta_z\tau$、矢量势 $A_{i,0}\eta_i+A_{i,\tau}\eta_i\tau$、标量势 $V_0+V_\tau\tau$ 📜Q；超平滑极限只留单 $\kappa$ 锥的 $m(r)\eta_z+\sum_i a_i\eta_i+v$（Eq. 10）📜Q。

**库仑相互作用**（Eq. 13）：$H_C=\frac12\sum_q V(q)\rho(q)\rho^\dagger(q)$，$V(r)=e^2/(4\pi\varepsilon|r|)$，石墨烯上 hBN 介电常数 $\varepsilon\sim8\varepsilon_0$；魔角 $\theta\sim1.05°$ 处特征相互作用能 $V(a_M)\sim14$ meV（$a_M=a/[2\sin(\theta/2)]$，$a=0.246$ nm）📜Q。

**朗道-金兹堡 / 随机场伊辛（RFIM）**：$C_2$ 破缺序参量 = 粗粒化 $C_2\mathcal T$ 破缺双线性 $\varphi(r)\sim\sum_{r'}\psi^\dagger\eta_z\psi\sim\Lambda_{UV}^2\psi^\dagger\eta_z\psi$（Eq. 14）；经典伊辛 $H_{Ising}=\sum_r[K(\nabla\varphi)^2+\frac r2\varphi^2+\frac{u}{4!}\varphi^4]$（Eq. 15，$r<0$）📜Q；无序耦合为随机"磁场" $H_{\varphi,dis}=\sum_r B(r)\varphi(r)$（Eq. 17），$B(r)\sim\sum M_0(r')/\xi_{int}^4$ 📜Q。相互作用长度 $\xi_{int}\sim\hbar v_F/\Delta_{CNP}$（Eq. 16）= 畴壁宽度/UV 截断；$v_F\approx0.15\times10^6$ m/s、$\Delta_{CNP}\approx1$ meV → $\xi_{int}\approx100$ nm $\sim10a_M$（$a_M\approx12.8$ nm）📜Q。主控无量纲比 $\alpha=\frac{\delta_m}{U}\cdot\frac{\xi_{dis}}{\xi_{int}}$（Eq. 18）📜Q。

### 1.2 参数分册（区分"作者设定" vs "推导所得"）

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | 系统尺寸 $L$、无序强度 $\delta_m$（= $g_{M_0}$）、关联长度 $\xi_{dis}$、相互作用能标 $U$、费米能 |
| **导出量（由旋钮+常数算出）** | $a_M=a/[2\sin(\theta/2)]\approx12.8$ nm、$\xi_{int}=\hbar v_F/\Delta_{CNP}\approx100$ nm、$\alpha$（Eq. 18）、$\xi_{dom}$（Eq. 19/20）、$g_{KK}$（Eq. 8）、$\delta\varepsilon_c(\alpha)$ |
| **模型内部量（解的性质）** | QVH 畴结构、畴壁模（4右+4左）、8 个无质量 Dirac 费米子、Chern 数 $C=\pm1$、局域化长度 $\xi_{loc}$ |
| **固定常数** | $a=0.246$ nm、$w_0=85$ meV、$w_1=110$ meV、$v_F\approx0.15\times10^6$ m/s、$v_0=9.1\times10^5$ m/s、$\varepsilon\sim8\varepsilon_0$、$\Delta_{CNP}\approx1$ meV |
| **预言量（可检验）** | STM 畴结构、输运条宽依赖（$w$ vs $\xi_{dom}$）、半金属/绝缘尺寸判据 |

> **符号防混**：$\alpha$（无序/相互作用比，Eq. 18）≠ 扭角 $\theta$（本文扭角用 $\theta$，$\alpha$ 是 RFIM 参量）；$\xi_{int}$（畴壁宽/UV 截断）≠ $\xi_{dis}$（无序关联长）≠ $\xi_{dom}$（畴尺寸）≠ $\xi_{loc}$（局域化长）；$\nu$（mTBG 填充因子）≠ Landau 填充 $\tilde\nu$。**无"反推量"层**。

### 1.3 显式假设清单

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **干净极限关联偏好（或近偏好）$C_2\mathcal T$ 破缺 $C=\pm1$ 态**（QVH 类） | 核心 | 📜Q（"we assume ... bolstered by numerics"） |
| A2 | **无序弱、平滑**（$\xi_{dis}\gg a_M$），保 $\mathcal T$ 与自旋旋转 | 模型 | 📜Q |
| A3 | **QVH 序参量唯一直接耦合平滑无序**（QSVH/QH/QSH/极化态序参量被对称性禁耦合，IVC 被平滑性禁耦合） | 核心 | 📜Q |
| A4 | **平滑性压制畴壁模间散射** → 自旋/谷扇区（一阶）解耦 | 推导 | 📜Q |
| A5 | **平带能级孤立**（$C_2\mathcal T$ 保护 Dirac 锥无质量） | 模型 | 📜Q（refs 14,22 可闭合此隙，作者判为不太可能） |
| A6 | **相互作用能标主导无序**（$\delta_m/U\ll1$） | 推导（RFIM） | 📜Q |
| A7 | **自旋简并 / 无自旋轨道耦合** | 模型 | 📜Q |

---

## 2. 推导链（顺论文演绎顺序）

### 2.0 总览

| 层 | 论文内容 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 前提定理层 | 平带 Dirac 理论 | 连续模型 + 平带 | $H_D$（Eq. 3/4）、质量→Chern | C2T、C3 | 平带孤立（A5） |
| 自由无序层 | 自由 Dirac + 无序 | $H_D$ + $H_{dis}$ | 局域化、IQH 平台转变 | Ludwig 等、CC 网络 | 无相互作用 |
| 相互作用层 | 干净库仑 | $H_C$ | QVH 能量竞争（$C=\pm1$） | A1、HF 数值 | 干净极限 |
| 推导层 | 相互作用+无序 | QVH + 随机场 | RFIM、$\xi_{dom}$、Dirac 恢复 | A2–A6 | $\delta_m/U\ll1$ |
| 边界层 | 竞争相 + 局域化 | $\delta\varepsilon$、$g_{KK}$ | $\delta\varepsilon_c(\alpha)$、$\xi_{loc}$ | Blume-Capel、Imry-Ma | 大 $L$ |

### 2.1 前提定理层：平带 Dirac 理论（§II）

- 连续模型（附录 A）谷解耦 $H_{cont}=H_++H_-$（涌现 $U(1)_v$ 谷对称）📜Q；$C_2\mathcal T$ + $C_3$ 保持 → $\pm\kappa$ 处无质量 Dirac 锥（Berry 相 $\pi$ 保护）；两锥同手征（阻碍局域两带模型）📜Q。
- 平带（$\theta=1.05°$，$w_0=85$ meV、$w_1=110$ meV 模拟弛豫）4 重简并 📜Q；投影得 $H_D$（Eq. 3/4）📜Q。
- 质量项分类 → Chern 数（同号 → $C=\pm1$，反号 → $C=0$）→ QVH 态定义 📜Q。

### 2.2 自由无序层：自由 Dirac + 无序的归宿（§III）

- 无序源：电荷无序（$\delta n\sim1-2\times10^{10}$ cm⁻²）、扭角无序（$\delta\theta\sim0.1°$，STM 直接成像）、hBN 对齐（均匀 $C_2$ 破缺）📜Q。
- 平滑无序 → 谷间散射指数压低（Eq. 8）📜Q。
- 自由 Dirac + 随机质量/矢量势/标量势：Ludwig 等——三类场分别边缘无关/边缘/边缘相关；三者共存 → 流向 IQH 平台转变不动点（CC 网络映射到无质量 Dirac 锥）📜Q。
- 恢复 $\kappa$ 谷间散射 → 热力学极限局域化，但 $\ell_{mfp}\sim a_M\exp[\frac\pi2(\hbar v_F/g\xi_{dis})^2]$（Eq. 11）、$\xi_{loc}\sim\ell_{mfp}\exp(64N_f^2/9)$ 指数长 📜Q。

### 2.3 相互作用层：干净极限 QVH 竞争（§IV）

- 库仑 $H_C$（谷内 $\gg$ 谷间，比值 $V(K)/V(\kappa)\sim|\kappa|/|K|\sim\theta\ll1$）📜Q；$V(a_M)\sim14$ meV、平带带宽 ~10 meV、van Hove 劈裂 ~5 meV（理论）/10–20 meV（STM）📜Q。
- 单味 HF 数值（refs 14,16,21,22）→ $C_2\mathcal T$ 破缺 $C=\pm1$ 态为低能解 📜Q；四候选绝缘体 QVH/QSVH/QH/QSH（Fig. 4 + Table I：QVH 保 T、破 C2、保 SU(2)s）📜Q。
- QVH 相对其他绝缘体在现实模型（无粒子-空穴对称）中**能量略高**，但差 $<10^{-5}$ meV/电子 📜Q。
- **唯一耦合**：只有 QVH 序参量 $\Psi^\dagger\eta_z\Psi$ 直接耦合平滑 T/自旋对称无序（QSVH/QH/QSH/极化态被对称禁、IVC 被平滑禁）📜Q。

### 2.4 推导层：RFIM 与 Dirac 恢复（§V，核心）

- 相互作用能标主导 → 只留随机质量场 $M_0$（耦合 QVH 序参量）→ 伊辛 + 随机场 = **2D RFIM**（Eq. 15+17），2D 泛无序 → $\xi_{dom}$ 有限 📜Q。
- $\alpha\gg1$（极平滑无序）：序参量直接追踪无序，$\xi_{dom}\sim\xi_{dis}$（Eq. 19）📜Q；$\alpha\ll1$（强相互作用）：畴壁粗糙化给下界 $\xi_{dom}\ge\max(\xi_{int},\xi_{dis})e^{c/\alpha^2}$（Eq. 20，Imry-Ma 型）📜Q。
- $L\gg\xi_{dom}$：多畴、相反 Chern 数 → **8 个独立 CC 网络模型**（每扇区 2 个 Dirac 锥 × 4 自旋/谷扇区）→ 每个网络映射到单个无质量 Dirac 锥 → **恢复无质量 Dirac 费米子** 📜Q。每条畴壁束缚 4 右移 + 4 左移模（Chern 改变 ±2），$\delta\sigma_{xy}=\pm2e^2/h$ 📜Q。
- **另一论证**：全无序 Dirac 理论 + 平均场关联 → 相互作用大幅增强 QVH 序参量耦合的随机场，其余无序场弱 → 退化为纯随机质量（边缘无关）→ 无质量 Dirac 费米子自然再现 📜Q。
- **尺寸判据**：$L<\xi_{dom}$（单畴）→ 绝缘（Lu et al.）；$L\gg\xi_{dom}$（多畴渗流）→ 半金属（Cao/Yankowitz）；$L>\xi_{loc}$ → 局域化 📜Q。hBN 对齐 → 均匀 $C_2$ 破缺 → 一种 QVH 畴面积缩小 → 畴壁不渗流 → 绝缘 📜Q。

### 2.5 边界层：竞争相与局域化（§V C/D）

- 若 QVH 非干净基态，无序仍可"翻盘"：竞争相 Ising 场 $\Theta$ 不线性耦合无序 → 三态（$s=\pm1$ = 两 QVH，$s=0$ = 竞争相）Blume-Capel 模型 + Imry-Ma → 临界能量差 $\delta\varepsilon_c(\alpha)$（Fig. 5 相图）；$\delta\varepsilon<\delta\varepsilon_c(\alpha)$ 时 QVH 主导 📜Q。
- 局域化：$\kappa$ 谷间散射 → $\xi_{loc}\sim\xi_{dom}\xi_{loc,fr}/a_M$（重标 UV 截断推迟局域化）；K 谷间散射沿畴壁为 1D 过程，大畴下主导，$\xi_{loc}\sim\hbar v_F/g_{KK}\sim\hbar v_F e^{4\pi^2\xi_{dis}^2/a^2}/g$ 📜Q。现实样品 $L\sim2-8$ μm $\sim150-600a_M$，局域化可能不相关 📜Q。

---

## 3. 结论清单（分层）

### 3.1 定理式主张（模型/对称论证的产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| Chern 分类 | 同号质量 → $C=\pm1$、反号 → $C=0$；QVH = $C=\pm1$ 每自旋/谷 | A5（平带孤立） |
| 唯一耦合 | 只有 QVH 序参量直接耦合平滑 T/自旋对称无序 | A3 |
| 畴壁模计数 | 每畴壁 4 右 + 4 左（Chern 改变 ±2）；8 个无质量 Dirac 费米子 | A4（扇区解耦） |
| RFIM 无序性 | 2D RFIM 泛无序 → $\xi_{dom}$ 有限 | A6 |

### 3.2 估算（数值/近似，非严格定理）

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| 相互作用能 | $V(a_M)\sim14$ meV（$\theta\sim1.05°$） | $\varepsilon\sim8\varepsilon_0$ | 📜Q[~] |
| 平带带宽 / vHs 劈裂 | ~10 meV / ~5 meV（理论）、~10–20 meV（STM） | — | 📜Q[~] |
| 畴壁宽 / UV 截断 | $\xi_{int}\approx100$ nm $\sim10a_M$（$a_M\approx12.8$ nm） | $v_F\approx0.15\times10^6$ m/s、$\Delta_{CNP}\approx1$ meV | 📜Q[~] |
| 畴尺寸 | $\xi_{dom}\sim\xi_{dis}$（$\alpha\gg1$）；$\ge\max(\xi_{int},\xi_{dis})e^{c/\alpha^2}$（$\alpha\ll1$） | A2、A6 | 📜Q[~] |
| 谷间散射压低 | $g_{KK}\sim g\,e^{-4\pi^2\xi_{dis}^2/a^2}$ | A2 | 📜Q[~] |
| QVH 能量差 | $<10^{-5}$ meV/电子（vs 其他绝缘体） | HF | 📜Q[~] |
| 样品尺寸 | $L\sim2-8$ μm $\sim150-600a_M$ | — | 📜Q[~] |
| 自由 Dirac 均自由程 | $\ell_{mfp}\sim a_M\exp[\frac\pi2(\hbar v_F/g\xi_{dis})^2]$ | A2 | 📜Q[~] |

### 3.3 预言（可检验性 → §5.1）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| 统一解释 CNP 半金属 vs 绝缘矛盾（尺寸判据） | "propose / argue" 📜Q | 中——条宽依赖输运 |
| STM 应看到局域 QVH 畴（gapped）+ 畴壁 gapless 模 | "should reveal" 📜Q | 中——大范围 STM |
| 无序可"选择" QVH（从近简并态）并"掩盖"关联（全局输运） | "propose / may have broader applications" 📜Q | 弱——间接 |
| 局域探针（STM）vs 全局输运的畴结构差异 | "leads to falsifiable predictions" 📜Q | 中 |

### 3.4 内部验证（自洽核对，非"排除竞争解释"）

1. **双论证一致性**：CC 网络映射（8 无质量 Dirac 费米子）与全无序 Dirac 理论（随机质量边缘无关）两路都推出"无质量 Dirac 恢复" 📜Q。
2. **RFIM 一致性**：$V(a_M)\approx14$ meV 与 $\Delta_{CNP}\approx1$ meV 作为 $U$ 的两候选，作者取后者（保守），且选择对后续讨论影响不大 📜Q。
3. **$\xi_{int}$ 自洽**：$v_F\approx0.15\times10^6$ m/s、$\Delta_{CNP}\approx1$ meV → $\xi_{int}\approx100$ nm $\sim10a_M$，满足 $\xi_{int}>a_M$ 的一致性要求 📜Q。
4. **Blume-Capel 负对照**：平均场错误预言长程序（低维），改 Imry-Ma → 纠正 📜Q。

### 3.5 概念区分（分类，非溯因排除）

| 区分 | 依据 | 结论 |
|---|---|---|
| QVH vs QSVH/QH/QSH | 破 C2（保 T）vs 破 T（保 C2）、SU(2)s 保/破（Table I）📜Q | 四类 $C_2\mathcal T$ 破缺绝缘体 |
| 关联 QVH vs minTBG QVH | 关联驱动 vs 单粒子位移场驱动；畴形状/尺寸由无序 vs 固定 Moiré 单胞 📜Q | 机理本质不同 |
| 半金属 vs 绝缘 | $L/\xi_{dom}\gg1$ vs $\ll1$；hBN 对齐抑制渗流 | 尺寸/无序决定 |

---

## 4. 假设-结论依赖图（含金量所在）

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性 |
|---|---|---|---|
| A1（干净极限 QVH 近基态） | 干净极限偏好其他相（IVC/极化/平庸绝缘体） | 整个 QVH 网络图景 | **核心假设**；作者用 §V C 竞争相分析兜底（无序可翻盘）📜Q |
| A3（QVH 唯一耦合无序） | 其他序参量也耦合无序 | 畴结构 | 由对称性严格论证（非 QVH 序参量被禁）📜Q |
| A4（扇区解耦） | 畴壁模间散射强 | 8 无质量 Dirac / 4 CC 网络 | 平滑性压制（一阶）；残余散射 → 局域化 📜Q |
| A5（平带孤立） | 相互作用闭合平带-色散带隙 | Dirac 锥保护失效（→ 平庸绝缘体） | refs 14,22 可发生，作者判为不太可能（STM 支持孤立）📜Q |
| A6（$\delta_m/U\ll1$） | 强无序 $\delta_m\sim U$ 或 $\xi_{dis}\sim a_M$ | RFIM 有效性 | 伊辛公式崩溃（作者显式声明）📜Q |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（实验靶标）

- **大范围 STM**：局域探测 gapped QVH 畴 + gapless 畴壁模（作者注：畴壁模证据文献尚未报告）📜Q；
- **条宽依赖输运**：单样品刻多条不同宽 $w$ 的条（Fig. 7a）或静电门局域调化学势（Fig. 7b）——$w\gg\xi_{dom}$ 半金属、$w\ll\xi_{dom}$ 绝缘 📜Q；
- 干净绝缘样品中 QVH 态的观测（非局域谷霍尔电流）可支撑场景 📜Q；
- 平带能谱随磁场演化（自旋单态 → 平行场影响小；平均场预言 CNP 隙随场减小）📜Q。

### 5.2 设计原则

无序（弱平滑）**选择** QVH + 样品尺寸/条宽**控制**半金属↔绝缘 + 局域探针 vs 全局输运**分离**观测 📜Q（本文 "propose / may have broader applications"）。

### 5.3 后续文献修正（时间倒挂，💭I）

- **T12（Tsim 2020, TZM）/ T29（Hou 2024, NQCP）**：本文是**关联驱动**的畴壁网络（无序拼贴），区别于 mTBG 单粒子 AB/BA 畴网络（T5/T9/T12/T29）——两图景 QVH 起源不同，作者 §V 显式区分 📜Q。
- **Wu et al.（ref 81）**：minTBG 畴壁模的 bosonization——本文 §VI 引为其边缘相互作用分析的先例 📜Q。
- **Uri et al. 2019 (ref 19)**：SQUID-on-tip 扭角无序成像（$\delta\theta\sim0.1°$）——本文无序源的经验依据 📜Q。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 核心假设未证 | 干净极限 QVH 近基态是假设（"bolstered by numerics"） | 📜Q（A1） |
| RFIM 有效域 | $\delta_m/U\to1$ 或 $\xi_{dis}\to a_M$ 时失效 | 📜Q |
| 局域化未定量深究 | 相互作用下局域化微妙，仅给一般特征 | 📜Q |
| 边缘相互作用未处理 | 畴壁模可能 Luttinger 液体/关联现象 | 📜Q |
| 输运非 CNP 未细 | $\sigma\propto\sqrt{|n|}$ 仅粗论 | 📜Q |

## 7. 与其他工作的关系（跨论文对标放这里）

| 工作 | 关系 |
|------|------|
| Cao et al. 2018 (ref 1,2) / Yankowitz 2019 (ref 9) / Lu et al. 2019 (ref 14) | 引用——三组 CNP 实验（半金属 vs 绝缘）的待解释矛盾 |
| Sharpe 2019 (ref 10) / Serlin 2020 (ref 11) | 引用——hBN 对齐绝缘/QAH |
| Liu 2019 (ref 21) / Choi 2019 (ref 16) / Xie-MacDonald 2020 (ref 22) | 引用——单味 HF 数值（QVH 竞争依据） |
| Ludwig et al. 1994 (ref 49) / Chalker-Coddington (ref 37) / Fradkin (ref 58,59) | 引用——自由 Dirac + 无序 / CC 网络 / 局域化 |
| Bistritzer-MacDonald 2011 (ref 3,4) / Koshino 2018 (ref 43) | 引用——连续模型/弛豫参数 |
| Wu et al. (ref 81) / minTBG 网络（ref 80–83） | 引用——关联 vs 单粒子 QVH 网络的对照 |

> ⚠️ Phase S 外部对标（**非本文引用**，时间倒挂 💭I）见 §5.3。

## 8. 对后续研究的影响

- 提出**无序在基态选择中的建设性角色**（选择 QVH、掩盖关联）——推广到其他填充的潜在框架 📜Q。
- "局域绝缘、全局半金属"的统一图景——调和 mTBG CNP 的矛盾实验 📜Q。
- 为 STM（局域畴）+ 输运（全局网络）双探针设计提供蓝图 📜Q。

## 9. 理论模型映射（供 TBPM/数值对标）

| 映射 | 说明 |
|------|------|
| 连续模型参数 | $w_0=85$ meV、$w_1=110$ meV、$v_0=9.1\times10^5$ m/s、$\theta=1.05°$ 📜Q |
| Dirac 理论 | $H_D=-v_F\psi^\dagger(i\partial_x\eta_x+i\partial_y\eta_y)\psi$（Eq. 3/4）📜Q |
| 无序 | $H_{dis}=\sum R_i\Psi^\dagger T^i\Psi$（Eq. 5），高斯关联（Eq. 6/7），$g_{KK}$ 压低（Eq. 8）📜Q |
| 库仑 | $V(r)=e^2/(4\pi\varepsilon|r|)$、$\varepsilon\sim8\varepsilon_0$、$V(a_M)\sim14$ meV 📜Q |
| RFIM | $H_{Ising}$（Eq. 15）+ $H_{\varphi,dis}$（Eq. 17）、$\alpha$（Eq. 18）、$\xi_{dom}$（Eq. 19/20）📜Q |
| 尺寸判据 | $L$ vs $\xi_{dom}$ vs $\xi_{loc}$（Fig. 2）📜Q |

---

## Phase S 目的接口（引用式，随项目增删）

- **Q1（edge state 如何表征）**：畴壁 gapless 模（4右+4左）↔ 8 无质量 Dirac 费米子；STM 应见 gapped 畴 + gapless 畴壁（文献尚未报告）📜Q。
- **Q2（理论如何解释）**：关联 QVH + 弱平滑无序 → RFIM 畴拼贴 → 4 CC 网络 → 恢复无质量 Dirac；尺寸判据解释半金属/绝缘矛盾 📜Q。与 T5/T9/T12/T29 的单粒子 AB/BA 网络**机理不同**（关联驱动 vs 位移场驱动）。
- **Q3（理论↔实验对应）**：$L/\xi_{dom}$ ↔ 样品均匀性（Lu 单畴 vs Cao/Yankowitz 多畴）、hBN 对齐 ↔ 畴不渗流、条宽 $w$ ↔ 可控实验 📜Q。

> **增量价值**：是 5 篇中唯一把**强关联 + 无序**纳入畴壁网络机制的理论（其他 T10/T11/T13/T14 均单粒子/无相互作用）；贡献"无序建设性角色 + RFIM 畴尺寸定量"两要素。report 可用数字（均 📜Q）：$C=\pm1$、$V(a_M)\sim14$ meV、$\xi_{int}\approx100$ nm、$a_M\approx12.8$ nm、$\delta\sigma_{xy}=\pm2e^2/h$、8 无质量 Dirac 费米子。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` 提取正文到 `/tmp/T16.txt`，逐项 grep 核对：

| 数字/公式 | grep 命中位置 | 结论 |
|------|--------------|------|
| $\theta\approx1.1°$、$\theta=1.05°$、$a=0.246$ nm、$a_M\approx12.8$ nm | §I/§II/§V | ✓ 📜Q[~] |
| $w_0=85$ meV、$w_1=110$ meV、$v_F\approx0.15\times10^6$ m/s、$v_0=9.1\times10^5$ m/s | §II B/附录 | ✓ |
| $V(a_M)\sim14$ meV、带宽 ~10 meV、vHs ~5 meV（理论）/10–20 meV（STM）、$\varepsilon\sim8\varepsilon_0$ | §IV A | ✓ |
| $\Delta_{CNP}\approx1$ meV、$\xi_{int}\approx100$ nm $\sim10a_M$ | §V A | ✓ |
| $\delta\sigma_{xy}=\pm2e^2/h$、8 无质量 Dirac 费米子、4 右 + 4 左、4 CC 网络 | §I/§V B | ✓ |
| $\alpha$（Eq. 18）、$\xi_{dom}\sim\xi_{dis}$、$\xi_{dom}\ge\max e^{c/\alpha^2}$（Eq. 19/20） | §V A | ✓ |
| $g_{KK}\sim g e^{-4\pi^2\xi_{dis}^2/a^2}$（Eq. 8）、$\ell_{mfp}$（Eq. 11） | §III B/C | ✓ |
| $\delta n\sim1-2\times10^{10}$ cm⁻²、$\delta\theta\sim0.1°$、$L\sim2-8$ μm、$\ell_B\approx25$ nm（1 T） | §III A/§VI | ✓ |
| $\delta E<10^{-5}$ meV/电子、$C=\pm1$ | §IV C/B | ✓ |
| $H_D$（Eq. 3/4）、质量→Chern、$H_{Ising}$（Eq. 15） | §II B/§V A | ✓ |

⚠️ 修正/降级：① 旧 review "无序破坏 C2 对称性 → QVH 序参量直接耦合"准确，但本次补全 RFIM/Ising 定量（$\alpha$、$\xi_{dom}$）；② 全文数字重 grep 全命中；③ 未引入无源数字（旧 review 无具体数值）。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-06 | 初读（research_onboarding Phase 4），叙事体 4 节。 |
| 2026-09-08 | **按 5 块演绎结构整体重写**。旧叙事体归档 `archive/paper_review_T16_thomson2021_prb.backup_20260908.md`。 |
| 2026-09-08 | **QC 修正**：① 补参数分册 + 7 条假设清单 + 假设-结论依赖图；② 补 RFIM/Ising 定量推导链（$\alpha$、$\xi_{dom}$、$g_{KK}$、$\delta\varepsilon_c$）；③ 全文数字重 grep 全命中。 |
