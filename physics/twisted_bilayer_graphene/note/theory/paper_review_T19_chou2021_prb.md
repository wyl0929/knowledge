<!--
 * @Author       : AI 精读 (理论论文五块演绎结构)
 * @Date         : 2026-08-06（粗读）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T19_chou2021_prb.md
 * @Description  : T19: Chou, Wu & Sau 2021 — mTBG 畴壁网络的 CDW 与有限温输运（理论 — 玻色化 + Luttinger 液体 + Kubo）
-->

# Paper Review: Chou, Wu & Sau (2021) — mTBG 畴壁网络的 CDW 与有限温输运

| 字段 | 内容 |
|------|------|
| **编号** | T19 |
| **标题** | Charge density wave and finite-temperature transport in minimally twisted bilayer graphene |
| **作者** | Yang-Zhi Chou, Fengcheng Wu, Jay D. Sau |
| **期刊** | Physical Review B 104, 045146 (2021) |
| **DOI / arXiv** | 10.1103/PhysRevB.104.045146 / arXiv:2104.02084（⚠️ arXiv 号正文未出现，标外部来源） |
| **类型** | 理论 — 相互作用（玻色化 + 重整化群 + Kubo 自能），无实验数据 |
| **课题组** | Chou / Wu / Sau (University of Maryland) |
| **PDF / SI PDF** | ✅ `reference/pdfs/Chou 等 - 2021 - Charge density wave and finite-temperature transport in minimally twisted bilayer graphene.pdf`（正文 12 页 + Appendices A–E：双通道模型/CDW 序参量/相称-不相称相变/标度维数/自能） |
| **精读日期** | 2026-08-06（粗读）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」五块记。理论论文无黑箱、无反推、无可辨识实验。
> **共享知识引用**：通用物理（Luttinger 液体、玻色化、Umklapp 散射、Kubo 公式）锚点引用 `note/shared/physics/`，不复制讲义。

---

## TL;DR

**本文想解决的理论问题**：偏置下 mTBG 的低能自由度是**一维畴壁态的网络**（每条畴壁 = 两通道一维线性色散自旋-1/2 费米子）。1D 系统中相互作用不可忽略，但 mTBG 网络中的相互作用此前未被系统研究。排斥电子-电子相互作用在畴壁中会实现什么相？有限温电阻率如何？

**主结果**：① 零温下两通道间库仑相互作用可驱动**自旋能隙的道间电荷密度波（interchannel CDW）**态——形成通道间"Coulomb drag"、只剩一个电荷导电模 📜Q；② 足够高温度下，畴壁内**电荷 Umklapp 散射**给出幂律电阻率 $\rho_{1d}\propto T^{4K_c-3}$（$K_c$ 为电荷 Luttinger 参数）📜Q；③ CDW 态**增强** Umklapp 散射，在中间温度 $T\sim\Delta_-$（CDW 关联能）处诱导**电阻率极小值**（$3/4<K_c\le1$）；$K_c=1$ 时预言**线性温度电阻率**，可复现未掺杂 mTBG 实验中 80 K 以下的线性电阻 📜Q。

**结论/意义**：首次系统研究 mTBG 畴壁网络的相互作用效应，把"非费米液体电阻率"与"道间 CDW 关联"联系；预言可用自旋能隙 CDW（隧道 DOS 指数压制 + Zeeman 场相变）与电阻率极小值检验。⚠️ 全文为理论预言，作者用词 show / predict / expect，**非已验证事实**。

---

## 1. 模型白箱（理想系统 + 假设清单）

### 1.1 单粒子哈密顿量（两通道，每自旋）

偏置下 mTBG 的 AB/BA 区成为 QVH 绝缘体，畴壁态 = valley Hall kink 态；绕数差为 2 → 每条畴壁每自旋每谷承载**两条手征边缘态** 📜Q。同谷两条 co-moving 态通过杂化 $t$ 分裂为能差 $2t$ 的两个通道（$p=0,\pi$），费米波矢差 $k_{F,0}-k_{F,\pi}=2t/v_F$（填充无关）📜Q。

$$
\hat H_0 = v_F\sum_{p,\sigma}\int dx\,\big[R^\dagger_{p\sigma}(-i\partial_x R_{p\sigma}) - L^\dagger_{p\sigma}(-i\partial_x L_{p\sigma})\big]
$$

📜Q（Eq. (1)）。$p=0,\pi$ 通道指标，$\sigma$ 自旋，$R_{p\sigma}$（$L_{p\sigma}$）右（左）mover。两条通道能量偏移 $2t$。畴壁段长 $d=a/[2\sin(\theta/2)]$（$a$ 石墨烯晶格常数）📜Q。

### 1.2 相互作用与玻色化

短程排斥、自旋 SU(2) 对称相互作用，分解为前向散射（Luttinger 液体）+ 背散射（含谷对称破缺项）：

- $\hat H_{I,c}=U_c\sum_{p}\int dx[e^{i\delta Q_p x}L^\dagger_{p\uparrow}R_{p\uparrow}L^\dagger_{p\downarrow}R_{p\downarrow}+H.c.]$（Eq. 2a，道内电荷隙，**破谷对称**）
- $\hat H_{I,s}=U_s\sum_{p}\int dx[L^\dagger_{p\uparrow}R_{p\uparrow}R^\dagger_{p\downarrow}L_{p\downarrow}+H.c.]$（Eq. 2b，道内自旋隙，谷对称）
- $\hat H_{I,+}=V_+\sum_{\sigma\sigma'}\int dx[e^{i\delta Q_+ x}L^\dagger_{0\sigma}R_{0\sigma}L^\dagger_{\pi\sigma'}R_{\pi\sigma'}+H.c.]$（Eq. 2c，道间，**破谷对称**）
- $\hat H_{I,-}=V_-\sum_{\sigma\sigma'}\int dx[e^{i\delta Q_- x}L^\dagger_{0\sigma}R_{0\sigma}R^\dagger_{\pi\sigma'}L_{\pi\sigma'}+H.c.]$（Eq. 2d，道间，谷对称）

其中 $\delta Q_p=4k_{F,p}-Q$、$\delta Q_\pm=2k_{F,0}\pm2k_{F,\pi}-Q$、$Q=0,\pm2\pi/d$（相称波矢）；$\delta Q_-=4t/v_F-Q$ 填充无关 📜Q。排斥下 $U_c,U_s,V_+,V_->0$ 📜Q。另有道间密度-密度相互作用 $V\int dx(n_{0\uparrow}+n_{0\downarrow})(n_{\pi\uparrow}+n_{\pi\downarrow})$（$V>0$）📜Q。

**玻色化**（Eq. 3–5）→ $\hat H_c+\hat H_s+\hat H_{cs}$（Eq. 6/7/8）：电荷/自旋玻色场 $\varphi^c_p,\varphi^s_p$，电荷速度 $v_c$、Luttinger 参数 $K_c$（排斥下 $K_c<1$）、自旋 $v_s,K_s$、道间耦合 $V$ 📜Q。对称/反对称电荷模（Eq. 10/11）：

$$
\varphi^c_+=\tfrac{1}{\sqrt2}(\varphi^c_0+\varphi^c_\pi),\quad \varphi^c_-=\tfrac{1}{\sqrt2}(\varphi^c_0-\varphi^c_\pi)
$$

→ $\hat H_c'$（Eq. 12，$v_+,K_+,v_-,K_-$，排斥下 $K_+<K_-<1$）📜Q。

### 1.3 参数分册

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | 相互作用强度 $U_c,U_s,V_+,V_-,V$、杂化 $t$（→$\delta Q_-=4t/v_F-Q$）、Zeeman 场 $B$、温度 $T$、化学势 $\mu$（→$k_{F,p}$） |
| **导出量（由旋钮+常数算出）** | $\delta Q_p,\delta Q_\pm$、$v_c,v_s,K_c,K_s,v_+,K_+,v_-,K_-$、CDW 关联能 $\Delta_-$、散射长度 $\Gamma_p$、电阻率 $\rho_{1d}$ |
| **模型内部量（解的性质）** | 相图（CDW/相称-不相称）、CDW 序参量 $O_-$、电阻率 $\rho(T)$ |
| **固定常数** | $v_F$、$d=a/[2\sin(\theta/2)]$、$e,\hbar$ |
| **预言量（可检验）** | 自旋能隙道间 CDW、电阻率极小值、$\rho\propto T^{4K_c-3}$ / $T^{2K_c-3}$、线性-$T$（$K_c=1$）、Zeeman 场相变 |

> 无"反推量 θ̂"层。**符号防混**：$\delta Q_-$（道间反对称背散射动量失配 $=4t/v_F-Q$）≠ $\delta Q_p$（道内 $=4k_{F,p}-Q$）；$K_c$（电荷 Luttinger 参数）≠ $K_+,K_-$（对称/反对称电荷扇区参数）；$\Delta_-$（CDW 关联能）≠ 能隙（CDW 是准长程序）。

### 1.4 显式假设清单

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **谷对称弱破缺**（允许谷破缺的 Umklapp 背散射 $U_c,V_+$） | 模型 | 📜Q |
| A2 | **忽略单粒子背散射**（矩阵元压制 = 有效谷对称；非必要假设） | 模型 | 📜Q（Sec. V 说明非必要） |
| A3 | **自旋 SU(2) 对称**（RG 下 $K_s\to1$、$U_s\to0$） | 模型 | 📜Q |
| A4 | **短程排斥**（$U_c,U_s,V_+,V_->0$；$K_c<1,V>0$） | 模型 | 📜Q |
| A5 | **解耦 1D 链极限**（$P_{a\bar a}=1$）为主分析，junction 作微扰 | 模型 | 📜Q |
| A6 | **$k_F$ 无关耦合常数**（简化，结果不依赖） | 模型 | 📜Q（作者自述） |
| A7 | **声速 $>$ 费米速度**（使局域电导率可用——此为 T21 的同类条件，本文不涉） | 无 | （本文不涉等离激元，不列） |
| A8 | **有限温 $T\gg T^*=v_F/d$**（网络可视为耦合 1D 系统，输运由畴壁内 Umklapp 主导） | 推导 | 📜Q |

---

## 2. 推导链（顺论文演绎顺序）

### 2.0 总览

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 模型层 | Sec. II | 单粒子 $H_0$ + 相互作用 | 玻色化 $\hat H_c+\hat H_s+\hat H_{cs}$ | A1–A6 | 1D 畴壁 |
| 推导层 | Sec. III | 玻色化哈密顿量 | 零温相图（道间 CDW） | A3、RG | $\delta Q_-=0$ |
| 边界层 | Sec. III B | $\delta Q_-\ne0$ + Zeeman | 相称-不相称相变（Fig. 3） | 半经典分析 | 附录 C |
| 推导层 | Sec. IV | $\hat H_{I,c}$ + CDW | 有限温电阻率 $\rho_{1d}(T)$ | Kubo、标度分析 | $T\gg T^*$ |

### 2.1 零温相图（Sec. III）

- **自旋扇区**：自旋 SU(2) → RG 下 $K_s\to1$、$U_s\to0$，自旋扇区退化为 $K_s=1$ 的 Luttinger 液体（Eq. 9）📜Q。
- **电荷扇区**：$U_c$ 在零温可忽略（$\delta Q_{p=0,\pi}=0$ 于 generic 填充，且近 CNP 不能形成良定义 CDW）；换到对称/反对称模 $\hat H_c'$（Eq. 12，$K_+<K_-<1$）📜Q。
- **$V_-$ 是零温唯一重要的背散射**（$\delta Q_-=4t/v_F-Q$ 填充无关）；$\hat H_{cs}'$（Eq. 13）📜Q。
- **$\delta Q_-=0$（$k_{F,0}=k_{F,\pi}=k_F$，$Q=0$）**：等价于两条自旋量子线的 **1D Coulomb drag 问题**（Klesse-Stern），排斥下 RG 流向无限 $V_-$ 📜Q。强耦合固定点钉住 $\varphi^c_-,\varphi^s_0,\varphi^s_\pi$ → 对称电荷扇区是 Luttinger 液体、反对称电荷扇区 + 两通道自旋扇区全部有隙 📜Q。主导准长程序参量 = **反对称道间 CDW** $O_-$（Eq. 14），$O_-(r)O_-(0)\propto\cos(2k_F r)/r^{K_+/2}$，$2k_F$ 振荡 → CDW 周期 $\xi=\pi/|k_F|$（两通道错开半周期）📜Q。
- **CDW 关联能**：$\Delta_-\sim\frac{v_F}{\alpha}\left(\frac{V_-}{v_F}\right)^{1/(1-K_c)}$（Eq. 15），$K_c<1$；良定义 CDW 需 $\Delta_->v_F/d$ 且 $d>\pi/|k_F|$ 📜Q。
- **$\delta Q_-\ne0$**：相称-不相称（Pokrovsky-Talapov）相变；相称相 = 上述 CDW，不相称相无 CDW；因自旋能隙，Zeeman 场 $B$ 也能诱导相变（Fig. 3，临界线 $\tilde t^2+\tilde B^2=2V_-/(\pi v_F)$）📜Q。较大 $t$ 和/或 $B$ 倾向不相称相、去稳 CDW 📜Q。

### 2.2 有限温输运（Sec. IV）

- **网络→1D 畴壁**：解耦阵列极限 + junction 散射微扰；$C_{2z}T$ 网络总是无隙、junction 不产生直接背散射 📜Q。$T\gg T^*=v_F/d$ 时输运由畴壁内 Umklapp + junction 耦合主导（Sec. IV 聚焦此区）📜Q。
- **Kubo 电导率**：$\sigma_{1d}=-\frac{2e^2}{\pi^2\hbar}\lim_{\omega\to0}\sum_p\mathrm{Im}[\omega G_p^{(R)}(\omega,k=0)]$（Eq. 17），玻色子自能 → 逆散射长度 $\Gamma_p$（Eq. 19）📜Q。电阻率 $\rho_{1d}=(h/2e^2)\frac{\Gamma_0\Gamma_\pi}{\Gamma_0+\Gamma_\pi}$（Eq. 20）📜Q。
- **无 CDW**：$U_c$ 二阶自能（Eq. 21）→ $\Gamma_p\propto\exp(-v_c\delta Q_p/2T)$（$T\ll v_c\delta Q_p$，Arrhenius）；$T\gg v_c\delta Q_p$ 时 $\Gamma_p\propto T^{4K_c-3}$（Eq. 21 高 $T$ 极限 + Fig. 4）📜Q。$K_c>3/4$ 时电阻率随 $T$ 增大（金属性），$K_c<3/4$ 反之 📜Q。
- **有 CDW**：$c_-,\varphi^s_0,\varphi^s_\pi$ 被钉住 → $U_c,V_+$ 顶点标度维数下降 → Umklapp **增强**（Eq. 22/23 平均场退耦）📜Q。新绝缘型幂律 $\rho_{1d}\propto T^{2K_c-3}$（$v_+\delta Q_p\ll T\ll\Delta_-$）；$T\gg\Delta_-$ 恢复 $T^{4K_c-3}$；$T\ll v_c\delta Q_p$ 回到热激活 📜Q。
- **电阻率极小值**：$3/4<K_c\le1$ 时在 $T\sim\Delta_-$ 出现极小（Fig. 5）📜Q。$K_c<3/4$ 时幂律指数在 $T\sim\Delta_-$ 从 $2K_c-3$ 变 $4K_c-3$，CDW 存在更难识别 📜Q。
- **网络层次**：$K_c=1$ 时（弱相互作用，mTBG 实验可能情形）junction 散射贡献与温度无关，畴壁内非弹性散射给**线性-$T$** 📜Q；可复现 Xu 2019 在未掺杂 mTBG 中 80 K 以下的线性电阻 📜Q。$V_+$ 项贡献类似但高 $T$ 指数换为 $2K_+-1$ 📜Q。

---

## 3. 结论清单（分层）

### 3.1 定理式主张（RG/玻色化论证的产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 零温相 | $\delta Q_-=0$ 时 $V_-$ RG 流向无限 → 自旋能隙道间 CDW（$c_+$ 无隙、$c_-,\varphi^s_{0,\pi}$ 有隙） | A3、A4 |
| CDW 幂律关联 | $O_-(r)O_-(0)\propto\cos(2k_F r)/r^{K_+/2}$，周期 $\xi=\pi/|k_F|$ | A4 |
| 电阻率幂律 | 无 CDW $\rho_{1d}\propto T^{4K_c-3}$；有 CDW $\rho_{1d}\propto T^{2K_c-3}$ | A1、A4、A5 |

### 3.2 估算（经验/近似，非严格定理）

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| CDW 关联能 | $\Delta_-\sim(v_F/\alpha)(V_-/v_F)^{1/(1-K_c)}$ | A4 | 📜Q[~] |
| 电阻率极小值窗口 | $T\sim\Delta_-$，需 $3/4<K_c\le1$ | A4 | 📜Q[~] |
| 相变临界线 | $\tilde t^2+\tilde B^2=2V_-/(\pi v_F)$ | A4 | 📜Q[~] |
| 线性-$T$ 条件 | $K_c=1$（弱相互作用） | A4 | 📜Q[~] |
| 实验对标 | 未掺杂 mTBG 80 K 以下线性电阻（Xu 2019） | 引文 | 📜Q[~] |

### 3.3 预言（可检验性 → §5.1）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| 零温自旋能隙道间 CDW（对比旧作自旋无隙 channel singlet） | "show / predict" 📜Q | 中——隧道 DOS 指数压制 |
| 电阻率极小值在 $T\sim\Delta_-$ | "develop a local minimum" 📜Q | 中——$\rho(T)$ 曲线 |
| $\rho\propto T^{4K_c-3}$、$K_c=1$ 线性-$T$ | "predict" 📜Q | 中——温度依赖 |
| Zeeman 场去稳 CDW（相称-不相称相变） | "can be examined experimentally" 📜Q | 中——STM + 面内磁场 |
| 结果适用其他拓扑畴壁网络（如 mTDBG、拓扑螺旋表面） | "should be relevant to" 📜Q | 弱——迁移性 |

### 3.4 内部验证（自洽核对）

1. **玻色化↔标度分析互验**：Kubo 自能（Eq. 21）的 $T^{4K_c-3}$ 与附录 D 标度维数分析一致 📜Q。
2. **平均场退耦↔标度分析互验**：有 CDW 时 $T^{2K_c-3}$ 同时由平均场退耦（Eq. 22/23）与标度分析（附录 D）给出 📜Q。
3. **零温极限对照**：$\rho_{1d}$ 在 $T\to0$ 恢复零电阻（与 Luttinger 液体弹道输运一致）📜Q。

### 3.5 概念区分（分类）

| 区分 | 依据 | 结论 |
|---|---|---|
| 谷对称 vs 谷破缺背散射 | 是否守恒谷量子数（$U_s,V_-$ 是 / $U_c,V_+$ 否）📜Q | 零温 CDW 来自谷对称 $V_-$，有限温电阻率来自谷破缺 $U_c,V_+$ |
| 道内 vs 道间 | $p$ 内 vs $p=0\leftrightarrow\pi$ 📜Q | CDW 是道间反对称 |
| 自旋能隙 CDW vs 旧作 channel singlet | 自旋扇区有隙 vs 无隙（相互作用模型不同）📜Q | 本文与 Wu-Jian-Xu 2019 / Chou 2019 的区别 |
| $T\lessgtr T^*=v_F/d$ | 2D 费米液体 $\rho\sim A+BT^2$ vs 耦合 1D 系统 📜Q | 网络输运两温区 |

---

## 4. 假设-结论依赖图

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性（作者如何对待） |
|---|---|---|---|
| A1 谷对称弱破缺 | 谷对称严格守恒（无 $U_c,V_+$） | 有限温电阻率（Umklapp）消失 | 作者：弱破缺即可，非零温主导项 📜Q |
| A3 自旋 SU(2) | 自旋各向异性 | $K_s\to1$、$U_s\to0$ 不成立，自旋扇区结构改变 | 未处理 💭I |
| A4 短程排斥 | 长程/其他相互作用 | $K_c<1,V>0$ 假定改变 | 作者声明结果不依赖 $k_F$ 依赖细节 📜Q |
| A5 解耦链极限 | 通用 junction 构型 | 电阻率须加 junction 散射（$K_c\ne1$ 时也非费米液体） | 作者：系统计算留待后续 📜Q |
| A8 $T\gg T^*$ | $T\ll T^*$ | 网络→2D 费米液体 $\rho\sim A+BT^2$，畴壁内耗散可忽略 | 作者区分两温区 📜Q |
| 单粒子背散射忽略 | 存在单粒子背散射 | 能带开隙（但实验未见隙） | 作者声明非必要假设，CDW 自旋隙会压制它 📜Q |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（本文预言的实验靶标）

- 隧道 DOS 在费米能处指数压制（自旋能隙 CDW 的电子分数量化签名）📜Q；
- $\rho(T)$ 曲线：幂律 $T^{4K_c-3}$/线性-$T$（$K_c=1$）+ 电阻率极小值 $T\sim\Delta_-$ 📜Q；
- STM + 面内磁场测 Zeeman 驱动的相称-不相称相变 📜Q。

### 5.2 设计原则（增强相互作用的调谐）

- 更小的电场 → 更强相互作用（**反直觉**，引 ref 41）；但电场须足够强以形成畴壁网络 → **最优为中等面外电场**（速度够小、畴壁态仍锐利）📜Q。

### 5.3 后续文献修正（时间倒挂，💭I）

- 本文补足了 T15/T18（散射/拓扑网络）**未处理的相互作用层**；与 TZM（T12）的"独立 1D 通道"图景兼容——本文把每条畴壁的两通道进一步做 CDW 关联分析。
- 本文引 Lee-Oshikawa-Cho 2021（ref 60）作为 junction 散射的非费米液体互补工作 📜Q。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 单畴壁为主 | 网络 junction 的完整非费米液体电阻率未系统算 | 📜Q（作者声明留待后续） |
| 相称填充 $K_c<1$ 非微扰区 | 相互作用隙发展需非微扰处理，本文省略 | 📜Q |
| 忽略电子-声子等 | 其他有限温电阻率机制未纳入；预言仅对 $T<$ AB/BA 隙有效 | 📜Q |
| 短程相互作用 | 长程库仑仅以筛后短程近似 | 📜Q→💭I |

## 7. 与其他工作的关系（跨论文对标）

| 工作 | 关系 |
|------|------|
| Klesse & Stern 2000 (ref 49) | 1D 两自旋量子线 Coulomb drag 问题的直接类比来源 📜Q |
| Efimkin & MacDonald 2018 (ref 24, =T09) | 三角网络模型 + 无隙 $C_{2z}T$ 网络结论 📜Q |
| Wu-Jian-Xu 2019 (ref 46)、Chou 2019 (ref 47) | 旧作 channel singlet（自旋无隙），本文自旋能隙 CDW 的区别 📜Q |
| Lee-Oshikawa-Cho 2021 (ref 60) | junction 散射的非费米液体互补工作 📜Q |
| Xu et al. 2019 Nat. Commun. 10, 4008 (ref 27) | 未掺杂 mTBG 线性-$T$ 电阻实验（80 K 以下）📜Q |
| Chou-Levchenko-Foster 2015 (ref 57) | 玻色子自能→电阻率的记忆函数方法 📜Q |

> ⚠️ Phase S 外部对标（**非本文引用**，时间倒挂 💭I）见 §5.3。

## 8. 对后续研究的影响

- 首次把 mTBG 畴壁网络**相互作用效应**系统化：道间 CDW + 非费米液体电阻率 📜Q。
- 建立"CDW 关联增强 Umklapp → 电阻率极小值"的机制链，为实验 $\rho(T)$ 非单调提供候选解释 📜Q。
- 把预言扩展到 mTDBG、拓扑螺旋表面等"导电网络"系统（作者 "should be relevant to"）📜Q。

## 9. 理论模型映射（供计算对标）

| 映射 | 说明 |
|------|------|
| $H_0$（Eq. 1）→ 两通道 1D Dirac | 畴壁两通道模型，可作 TBPM/NEGF 的非相互作用锚点 📜Q |
| 玻色化 → Luttinger 参数 | $K_c,v_c$ 需从微观参数估计（本文给唯象）📜Q |
| $\rho\propto T^{4K_c-3}$ / $T^{2K_c-3}$ → 幂律拟合 | 供实验/数值幂律指数对标 💭I |
| 电阻率极小值 $T\sim\Delta_-$ | 供有限温输运计算对标 📜Q |

---

## Phase S 目的接口（引用式）

- **Q1（edge state 如何表征）**：本文把畴壁态从"拓扑通道"推进到"**强关联 1D 系统**"——表征靶标是 CDW 关联（隧道 DOS 指数压制）与幂律/极小值电阻率，**非**单粒子电导平台 📜Q。
- **Q2（理论如何解释）**：相互作用在畴壁两通道间打开自旋能隙 CDW、只剩一个导电模；Umklapp 散射给非费米液体 $\rho(T)$，CDW 增强 Umklapp → 电阻率极小值 📜Q。
- **Q3（理论↔实验对应）**：$K_c=1$ 线性-$T$ ↔ Xu 2019 80 K 以下线性电阻；$\Delta_-$ ↔ 电阻率极小值温度；Zeeman 场相变 ↔ STM 面内磁场实验 📜Q。

> **增量价值**：补足网络模型（T09/T12/T15/T18）**缺失的相互作用层**；与 T15/T18 分工——T15/T18 是**单粒子散射/拓扑**，本文是**相互作用 + 输运**；比 T15/T18 多 = CDW 相 + 非费米液体电阻率；少 = 无散射 S 矩阵/拓扑不变量。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` + `-raw` 提取到 `/tmp/T19.txt`，逐项 grep 核对：**全部数字命中原文**——

| 数字 | grep 命中位置 | 结论 |
|------|--------------|------|
| 绕数差=2、每畴壁每自旋每谷两条手征态 | 引言 | ✓ 📜Q |
| $k_{F,0}-k_{F,\pi}=2t/v_F$、能差 $2t$、$d=a/[2\sin(\theta/2)]$ | Sec. II | ✓ |
| $\delta Q_-=4t/v_F-Q$、$Q=0,\pm2\pi/d$ | Sec. II | ✓ |
| $\Delta_-\sim(v_F/\alpha)(V_-/v_F)^{1/(1-K_c)}$（Eq. 15） | Sec. III A（-raw 复核） | ✓ 📜Q[~] |
| $\rho_{1d}\propto T^{4K_c-3}$（无 CDW）、$T^{2K_c-3}$（有 CDW） | Sec. IV | ✓ |
| 电阻率极小值 $3/4<K_c\le1$、$T\sim\Delta_-$ | Sec. IV | ✓ |
| $K_c=1$ 线性-$T$、80 K（Xu 2019） | Sec. IV / Sec. V | ✓ |
| $\rho_{1d}=(h/2e^2)\Gamma_0\Gamma_\pi/(\Gamma_0+\Gamma_\pi)$（Eq. 20）、$\sigma_{1d}$（Eq. 17） | Sec. IV | ✓ |
| 临界线 $\tilde t^2+\tilde B^2=2V_-/(\pi v_F)$（Fig. 3 caption） | Fig. 3（-raw 复核，layout 破碎为 "π2Vv−F"） | ✓ |
| $T^*=v_F/d$、$\rho\sim A+BT^2$（$T\ll T^*$） | Sec. IV B | ✓ |
| $V_+$ 项指数 $2K_+-1$ | Sec. IV B | ✓ |

⚠️ 修正/降级：① 旧版 "$\rho(T)\propto T^{2K_c-2}$" 指数**无源**——原文为 $T^{4K_c-3}$（无 CDW）与 $T^{2K_c-3}$（有 CDW），已改正；② 旧版 "CDW 条件=谷对称弱破缺" 混淆——零温 CDW 来自**谷对称**的 $V_-$，谷破缺 $U_c,V_+$ 才驱动有限温电阻率，已在 §3.5 区分；③ 临界线 OCR 破碎（layout "π2Vv−F"），-raw 复核为 $2V_-/(\pi v_F)$。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-06 | 初读（粗读版） |
| 2026-09-08 | **按 5 块演绎结构整体重写**（应用户要求）。旧版归档 `archive/paper_review_T19_chou2021_prb.backup_20260908.md`。补：$H_0$ + 四个背散射项显式式、参数分册、8 条假设清单、推导链（Sec. II→IV）、结论分层、假设-结论依赖图、反向核对 pass。 |
| 2026-09-08 | **降级/删除**：① 旧版电阻率指数 $T^{2K_c-2}$ 无源 → 改为 $T^{4K_c-3}$/$T^{2K_c-3}$；② 旧版 "CDW 条件=谷对称弱破缺" 修正为"谷对称 $V_-$ 驱动零温 CDW"；③ 旧版 "两通道间库仑相互作用驱动自旋能隙 + 道间 CDW" 保留并精确化（自旋隙来自 SU(2) RG、CDW 来自 $V_-$ 钉住）。 |
