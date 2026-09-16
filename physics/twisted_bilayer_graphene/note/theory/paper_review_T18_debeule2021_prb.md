<!--
 * @Author       : AI 精读 (理论论文五块演绎结构)
 * @Date         : 2026-08-06（粗读）→ 2026-08-20（S-REV 修正 kick 措辞）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T18_debeule2021_prb.md
 * @Description  : T18: De Beule, Dominguez & Recher 2021 — mTBG 三角散射网络的有效 Floquet 模型（理论 — 网络→周期驱动映射 + Floquet 拓扑）
-->

# Paper Review: De Beule, Dominguez & Recher (2021) — mTBG 的有效 Floquet 模型

| 字段 | 内容 |
|------|------|
| **编号** | T18 |
| **标题** | Effective Floquet model for minimally twisted bilayer graphene |
| **作者** | Christophe De Beule, Fernando Dominguez, Patrik Recher |
| **期刊** | Physical Review B 103, 195432 (2021) |
| **DOI / arXiv** | 10.1103/PhysRevB.103.195432 / arXiv:2011.12989（⚠️ arXiv 号正文未出现，标外部来源） |
| **类型** | 理论 — 散射网络 → 周期驱动（Floquet）晶格模型映射 + Floquet 拓扑（无实验数据） |
| **课题组** | De Beule (TU Braunschweig / Univ. Luxembourg)、Dominguez、Recher (TU Braunschweig) |
| **PDF / SI PDF** | ✅ `reference/pdfs/De Beule 等 - 2021 - Effective Floquet model for minimally twisted bilayer graphene.pdf`（正文 14 页 + Appendices A–D：zigzag ribbon/Floquet winding number/相图/输运） |
| **精读日期** | 2026-08-06（粗读）→ 2026-08-20（S-REV 修正）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」五块记（见 `note/shared/method/theory_paper_reading.md` §3）。理论论文无黑箱、无反推、无可辨识实验。
> **共享知识引用**：通用物理（Chalker-Coddington 网络、Floquet 理论、体-边对应、谷 Chern 数）锚点引用 `note/shared/physics/`，不复制讲义。

---

## TL;DR

**本文想解决的理论问题**：偏置下 mTBG 的低能物理由三角**定向散射网络**（每链接每谷每自旋两条手征通道，AB/BA 畴壁 + AA 节点）主导。散射网络的体-边对应**定义不清**，且缺少便于解析处理的哈密顿量描述。能否把这个网络映射成一个**有效 Floquet（周期驱动）晶格模型**，从而用标准方法得到能带与拓扑不变量？

**主结果**：① 把单个散射节点映射为三能级系统（trimer）的时间演化，再由三组 trimer 的周期开关序列重构整个网络 → **Floquet 紧束缚模型**（$U_F=T_3 S T_2 S T_1 S$）📜Q；② 单通道网络有金属/平庸绝缘体/**反常 Floquet 绝缘体（AFI）** 三相，能隙只能靠破坏 $C_2T$（时间反演或面内反演）打开，AFI 由 Floquet 绕数 $W=\pm1$ 表征 📜Q；③ 双通道网络（mTBG 实况）中**道间耦合可在不破坏 $C_2T$ 的情况下打开能隙** → **谷 AFI（VAFI）**，边缘携带一对对向传播的手征模，总绕数为零、仅在无谷间散射时稳健 📜Q；④ 磁输运给出 AFI 相量子化电导 $e^2/h$（每谷每自旋），并在手征 zigzag 区重现网络模型的 Aharonov-Bohm 振荡 📜Q。

**结论/意义**：为 mTBG 畴壁网络提供了**哈密顿量形式的有效模型**（相比原子论方法：每 moiré 单胞 $\sim10^4(\theta°)^{-2}$ 个原子），并给出 VAFI 这一"总拓扑平庸但谷拓扑非平庸"的新相。⚠️ 作者自述：**保守 $C_2T$ 的 VAFI 在真实 mTBG 中很可能难以实现**（实验与理论都表明网络在很宽参数范围保持金属性）。

---

## 1. 模型白箱（理想系统 + 假设清单）

### 1.1 散射网络 + trimer 哈密顿量（单节点）

研究对象 = 每谷每自旋的三角定向散射网络（AB/BA 畴壁为链接、AA 区域为节点，手征通道在节点散射，两谷取向相反）📜Q。核心思想：**节点散射 $\leftrightarrow$ trimer 时间演化** $b=Sa \leftrightarrow \psi(t)=U(t,0)\psi(0)$，$U=e^{-iH_0t/\hbar}$ 📜Q（Eq. (2)）。

- **$C_3$ 对称 S 矩阵**：$S=\begin{pmatrix}s_l & s_r & s_f\\ s_f & s_l & s_r\\ s_r & s_f & s_l\end{pmatrix}$（Eq. (1)），$|s_f|^2=P_f$、$|s_l|^2=P_l$、$|s_r|^2=P_r$ 为前向/左偏/右偏概率；电流守恒 $S^\dagger S=1_3$ → $P_f+P_r+P_l=1$ 📜Q。$C_2T$ 对称时单参数化：$s_r=s_l=\sqrt{P_d}$、$s_f=e^{-i\alpha}\sqrt{P_f}$、$\cos\alpha=-\sqrt{P_d/4P_f}$，$1/9\le P_f\le 1$ 📜Q。
- **trimer 哈密顿量**：$H_0=J\begin{pmatrix}0 & e^{i\phi} & e^{-i\phi}\\ e^{-i\phi} & 0 & e^{i\phi}\\ e^{i\phi} & e^{-i\phi} & 0\end{pmatrix}$（Eq. (3)），$J\ge0$，$3\phi$ 为三角 plaquette 通量；谱 $E_n=2J\cos(\phi+2\pi n/3)$、本征态 $\psi_n=\tfrac{1}{\sqrt3}(\eta^n,\eta^{-n},1)^t$、$\eta=e^{i2\pi/3}$（Eq. (4)）📜Q。
- **映射参数**：$s_l=g(\theta_1,\theta_2)$、$s_r=g(\theta_1,\theta_2-2\pi/3)$、$s_f=g(\theta_1,\theta_2+2\pi/3)$，$g(\theta_1,\theta_2)=\tfrac13(e^{-i\theta_1}+2e^{i\theta_1}\cos\theta_2)$（Eq. (5)）；$\theta_1=\tfrac23Jt\cos\phi/\hbar$、$\theta_2=\sqrt3\,Jt\sin\phi/\hbar$（Eq. (6)）📜Q。偏转概率 $P_l=\tfrac19[3+4\cos(2\theta_1)\cos\theta_2+2\cos(2\theta_2)]$（Eq. (7)），$P_f,P_r$ 由 $\theta_2\to\theta_2\pm2\pi/3$ 得 📜Q。

### 1.2 参数分册

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | 散射参数 $P_f,P_l,P_r$（或 $Jt,\phi$）；双通道的 $P_{f1},P_{f2},\varphi,P_{d1}-P_{d2}$；磁通 $\Phi/\Phi_0$ |
| **导出量（由旋钮+常数算出）** | $\theta_1=\tfrac23Jt\cos\phi/\hbar$、$\theta_2=\sqrt3Jt\sin\phi/\hbar$、$\hbar\omega=2\pi\hbar v/(3l)\approx100\,\theta°$ meV、Floquet 算符 $U_F=T_3ST_2ST_1S$、quasienergy 谱、Floquet 绕数 $W$ |
| **模型内部量（解的性质）** | quasienergy 带 $\varepsilon_{mn}(k)$、DOS、边缘模、电导 $G$、相图（金属/平庸/AFI/VAFI） |
| **固定常数** | $v$=通道速度（取石墨烯体费米速度）、$l$=链接长度（取 moiré 晶格常数）、$e/h$ |
| **预言量（可检验）** | AFI 量子化电导 $e^2/h$、AB 振荡、VAFI 边缘模、外场下临界场以上的 AFI |

> 无"反推量 θ̂"层。**符号防混**：$\phi$（trimer 通量相位，Eq. (3)）≠ $\varphi$（双通道 S 矩阵的相位移动，Eq. (35)）；$P_f$（前向概率）≠ $P_{f1},P_{f2}$（双通道道内/道间前向概率）；$\theta_1,\theta_2$ 是**散射映射参数**（非几何扭角 $\theta$）。

### 1.3 显式假设清单

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **网络模型有效**：费米面在隙内、低能物理仅由三角谷霍尔态网络给出，畴壁态与其他态分离 | 模型 | 📜Q（引言） |
| A2 | **无谷间散射**（moiré 花样在原子间尺度缓变） | 模型 | 📜Q |
| A3 | **散射参数近似能量无关**（在 $\hbar\omega\approx100\,\theta°$ meV 能标上常数） | 模型 | 📜Q |
| A4 | **$C_3$ 对称**（单节点 S 矩阵）；$C_2T$ 对称（mTBG 额外对称，正文主设） | 模型 | 📜Q |
| A5 | **Floquet 截断**：数值取 8 个谐波（$m=-8,\dots,8$）保证收敛 | 数值 | 📜Q |
| A6 | **磁长 $\gg$ 节点散射区**（磁通仅以传播段 Peierls 相位进入，不改节点 S 矩阵） | 磁输运 | 📜Q |
| A7 | **双通道 S 矩阵非最一般**（设两通道道内散射概率相等、道间左右偏转概率相等） | 模型 | 📜Q（作者自述） |

---

## 2. 推导链（顺论文演绎顺序）

### 2.0 总览

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 模型层 | Sec. II A | 单节点散射 | trimer $H_0$（Eq. 3） | A4 | $C_3$ |
| 推导层 | Sec. II B | trimer + 三角晶格 | 三步骤周期驱动 $U_F$（Eq. 18） | A1、A4 | 定向网络 |
| 推导层 | Sec. II C/D | Floquet 哈密顿量 | quasienergy 谱 + 相图（金属/平庸/AFI） | A5、Floquet 定理 | 单通道 |
| 边界层 | Sec. II D | $C_2/T$ 关系 | 谷间散射参数约束（Eq. 30/31）+ 绕数 | A2 | 谷解耦 |
| 推导层 | Sec. III | 双轨道 trimer | 双通道 S 矩阵 + VAFI | A7 | 双通道 |
| 推导层 | Sec. IV | Floquet 格林函数 | 电导 $G$（Eq. 38）+ AB 振荡 | A6、Landauer | 磁输运 |

### 2.1 单节点 → trimer（Sec. II A）

输入=$C_3$ S 矩阵（Eq. 1）；输出=trimer $H_0$ 及其谱（Eq. 3/4）📜Q。$U(t)=e^{-iH_0t/\hbar}$ 与 $S$ 的识别（Eq. 2）给出 Eq. (5)–(7)。$C_2T$ 对称（$s_r=s_l$）对应 $\theta_2=(n+1/3)\pi$；$\theta_2=\pi/3$ 时 $s_f=-\tfrac13\cos\theta_1-i\sin\theta_1$、$s_r=s_l=\tfrac23\cos\theta_1$，与 Efimkin-MacDonald 的 S 矩阵幺正等价 📜Q。映射 $(\theta_1,\theta_2)\to(P_r,P_l)$ 是 onto 但非一对一（需指定 $\theta_1$ 符号）📜Q。

### 2.2 网络 → 三步骤周期驱动（Sec. II B）

- **分解**：网络分解为三组不相交节点 → 三角 trimer 晶格（晶格矢量 $e_1=\sqrt3 l(0,1)$、$e_2=\sqrt3 l(\sqrt3/2,-1/2)$（Eq. (9)），晶格常数 $\sqrt3 l$）📜Q。
- **三段驱动**：$H(k,t)=H_1$（$0<t<T/3$）、$H_2$（$T/3<t<2T/3$）、$H_3$（$2T/3<t<T$）（Eq. (8)）；$U_1=S$（Eq. (10)）、$H_2(k)$（Eq. 11，$z=Je^{i\phi}$、$e_3=-(e_1+e_2)$）、$U_2=T_3T_2ST_1$（Eq. 12，$T_1=\mathrm{diag}(e^{ik\cdot l_2},e^{ik\cdot l_1},e^{ik\cdot l_3})$ 等，$l_{1,2}=l(-1/2,\pm\sqrt3/2)$、$l_3=-(l_1+l_2)$）、$H_3$（Eq. 16）、$U_3=T_3ST_3^\dagger$（Eq. 17）📜Q。
- **Floquet 算符**：$U_F(k)=T_3ST_2ST_1S$（Eq. 18）📜Q。网络取向由开关序列固定（自然破缺时间反演）；交换第二、三步即反转取向（反转谷）📜Q。
- 对应验证：$P_l=1$（$\theta_1=\theta_2=0$）→ 闭合轨道→平带绝缘体；$P_f=1$（$\theta_1=0,\theta_2=-2\pi/3$）→ 三组沿 $-l_j$ 传播的 1D 手征模→金属 📜Q（Fig. 4）。

### 2.3 quasienergy 谱与单通道相图（Sec. II C/D）

- Floquet 定理 → $\psi_k(t)=e^{-i\varepsilon_kt/\hbar}\sum_m e^{im\omega t}\psi_{km}$（Eq. 19）、$\hbar\omega=2\pi/T$；Floquet 哈密顿量 $H_{mm'}$（Eq. 21–23）📜Q。$\hbar\omega=2\pi\hbar v/(3l)\approx100\,\theta°$ meV（Eq. 25），$T=3l/v$ 📜Q。
- 每个 trimer 三 site → 每能量周期三条带；能隙在 $\bar\Gamma$ 点打开当 $P_f=P_r$（$\theta_2=n\pi$）或 $P_f=P_l$（$\theta_2=(n-1/3)\pi$）、$P_{l,r}\in[1/9,1/3]$（Eq. 28 附近）📜Q。带接触一般二次型（Fig. 5a），$C_2T$ 守恒时为线性 Dirac 节点且对称保护（Fig. 5b）📜Q。
- **相图**（Fig. 2）：一金属 + 两绝缘相，由渗流线 $P_r=P_l$（$C_2T$ 守恒）分开 📜Q。zigzag ribbon（宽 $(3N-1)l/2$）谱显示 $P_r\sim1$ 时边缘有逆时针手征模（AFI，$W=1$）、$P_l\sim1$ 时边缘局域（平庸，$W=0$）（Fig. 6）📜Q。
- **绕数**（附录 B）：$W[P_l=1]=0$、$W[P_r=1]=1$；反向取向 $W'[P_l=1]=-1$、$W'[P_r=1]=0$ 📜Q。$C_2$ 守恒但 $T$ 破缺：$W=\mathrm{sgn}(P_r-P_l)$；$T$ 守恒但 $C_2$ 破缺：总绕数=0，但可定义两个非零谷绕数 📜Q。$C_2/T$ 对谷散射参数的关系（Eq. 30/31）给出：$T$ 破缺+$C_2$ 守恒时两谷相必互补（一谷平庸、一谷 AFI）📜Q。

### 2.4 双通道网络与 VAFI（Sec. III）

- 双轨道 trimer（每 site 两轨道）有 11 参数，解析不可控 → 改为**从目标 S 矩阵数值反解** $H_0/\hbar\omega=\tfrac{3i}{2\pi}\log S$（Eq. 34）📜Q。
- 双通道 $C_3$+$C_2T$ S 矩阵（Eq. 35/36）：$s_f=\begin{pmatrix}e^{i(\varphi+\chi)}\sqrt{P_{f1}} & -\sqrt{P_{f2}}\\ -\sqrt{P_{f2}} & -e^{-i(\varphi+\chi)}\sqrt{P_{f1}}\end{pmatrix}$、$s_r=\begin{pmatrix}e^{i\varphi}\sqrt{P_{d1}} & \sqrt{P_{d2}}\\ -\sqrt{P_{d2}} & -e^{-i\varphi}\sqrt{P_{d1}}\end{pmatrix}$、$s_l=(s_r)^t$，$P_{f1}+P_{f2}+2(P_{d1}+P_{d2})=1$；相对相位 $2\varphi+\pi$、$\cos\chi=(P_{d2}-P_{d1})/2\sqrt{P_{f1}P_{d1}}$ 📜Q。四个唯象散射参数 $P_{f1},P_{f2},\varphi,P_{d1}-P_{d2}$；后取 $P_d=P_{d1}=P_{d2}$ 📜Q。
- **无前向散射（$s_f=0$）**：仅参数 $\varphi$。$\varphi=(n+1/2)\pi$ 极限→局域平带（Fig. 8a）；$\varphi=n\pi$ 极限→三组 1D 手征 zigzag（ZZ）模（Fig. 8b），quasienergy $\varepsilon_{mj}(k)=\hbar\omega(m/2+3k\cdot l_j/4\pi)$、DOS$=4/\sqrt3\hbar\omega l^2$（每谷每自旋）、速度=组成模之半 📜Q。有隙相**恒为 AFI**，能隙由道间耦合打开、不破坏 $C_2T$ 📜Q。
- **前向散射效应**：相边界解析（$P_{f1}=0$）$P_{f2}|_{E_g=0}=1-(2\sin\varphi)^{-2}$（Eq. 37）；$\varphi=\pm\pi/2$ 时边界恒在 $P_f=3/4$；AFI 相占据 $\pi/6<|\varphi|<5\pi/6$（$P_{f1}=0$，Fig. 9）📜Q。
- **VAFI**：两谷同时承载在给定边缘对向传播的反常边缘模；总绕数意义下拓扑平庸，但由**谷绕数** $(1,-1)\sim(0,0)$ 表征（Table I）；只要边缘在原子间尺度平滑（无谷间散射），边缘承载每自旋一对谷手征模 📜Q。⚠️ mTBG 中边缘构型不明、一般边缘很可能使 VAFI 边缘模开隙 📜Q。

### 2.5 磁输运（Sec. IV）

- 两终端电导 $G=(4e^2/h)\mathrm{Tr}_\omega[\Gamma_L G_0^r\Gamma_R G_0^a]$（Eq. 38），$G_0^r=(\varepsilon-H_0-\Sigma_R^a-\Sigma_L^a)^{-1}$、$\Gamma_i=2\mathrm{Im}[\Sigma_i^a]$ 📜Q。单通道 AFI 相有边界时**量子化电导 $e^2/h$（每谷每自旋）**，体周期边界时电导→0 📜Q（Fig. 13a）。
- 磁场 $B=Be_z$ → 传播段增加 Peierls 相位 → 新驱动步骤（Eq. 39–43），$\theta_P(x)=\pi\Phi x/(\Phi_0 l/2)$（Eq. 40）、$\Phi=B\sqrt3 l^2/2$（moiré 单胞磁通）📜Q。散射参数改 $\theta_1=\tfrac{J}{\hbar\omega}\tfrac{\pi}{2}\cos\phi$、$\theta_2=\tfrac{J}{\hbar\omega}\tfrac{\pi}{\sqrt3}\sin\phi$（Eq. 44）📜Q。
- **Aharonov-Bohm 振荡**：$G(\Phi/\Phi_0)$ 在 moiré 单胞穿过整数磁通量子时共振（ZZ 区 $\varphi=0$），重现网络模型结果 📜Q（Fig. 13b）。

---

## 3. 结论清单（分层）

### 3.1 定理式主张（数学/拓扑论证的产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 网络↔Floquet 等价 | 三角定向散射网络 = 三步骤周期驱动的 trimer 晶格（$U_F=T_3ST_2ST_1S$） | A1、A4 |
| 单通道能隙开法 | 能隙只能靠破缺 $C_2T$ 打开；$C_2T$ 守恒则 Dirac 节点对称保护 | A4 |
| 绕数 | 单通道 $W=\mathrm{sgn}(P_r-P_l)$（$C_2$ 守恒+$T$ 破缺）；$T$ 守恒+$C_2$ 破缺则总 $W=0$ 但谷绕数非零 | A2 |
| VAFI 拓扑性质 | 双通道 VAFI 总绕数平庸、仅谷绕数保护，无谷间散射时稳健 | A2 |

### 3.2 估算（经验/近似，非严格定理）

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| Floquet 能标 | $\hbar\omega=2\pi\hbar v/(3l)\approx100\,\theta°$ meV | A3 | 📜Q[~] |
| 相界（双通道） | $P_{f2}|_{E_g=0}=1-(2\sin\varphi)^{-2}$；$\varphi=\pm\pi/2$ 时 $P_f=3/4$ | A7 | 📜Q[~] |
| AFI 相范围 | $\pi/6<|\varphi|<5\pi/6$（$P_{f1}=0$） | A7 | 📜Q[~] |
| 原子数对比 | 每 moiré 单胞 $\sim10^4(\theta°)^{-2}$ 个原子（网络/Floquet 模型的计算优势） | 引言 | 📜Q[~] |

### 3.3 预言（可检验性 → §5.1）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| 外场破 $C_2T$ 时高于临界场普遍出现 AFI 相 | "one expects ... to arise generically" 📜Q | 中——非局域输运 |
| 保守 $C_2T$ 的 VAFI 在真实 mTBG 中**很可能难以实现** | "most likely very challenging to realize" 📜Q | —（作者自述负向） |
| Floquet 方案可在光学晶格/光子晶体中实现 | "can in principle also be realized" 📜Q | 弱——类比平台 |

### 3.4 内部验证（自洽核对）

1. **绕数↔有限系统互验**：解析 $W[P_l=1]=0$、$W[P_r=1]=1$（附录 B 计算）与 zigzag ribbon 谱（Fig. 6：$P_r\sim1$ 有手征边缘模、$P_l\sim1$ 局域）一致 📜Q。
2. **边缘稳健性**：AFI 边缘态对改变边缘 hopping 常数稳健（作者 "verified ... robust"）📜Q。
3. **AB 振荡↔网络模型互验**：磁输运 $G(\Phi/\Phi_0)$ 共振重现 De Beule 2020（ref 32）散射网络结果 📜Q。

### 3.5 概念区分（分类）

| 区分 | 依据 | 结论 |
|---|---|---|
| 金属 / 平庸绝缘体 / AFI | 能隙是否打开 + 绕数 $W$（0 vs ±1）📜Q | 单通道三相 |
| AFI vs 平庸（体-边对应） | Floquet 绝缘体的体-边对应**良定义**（对比散射网络**不定义**）📜Q | 本文动机之一 |
| 单通道 vs 双通道能隙机制 | 破 $C_2T$ vs 道间耦合（不破 $C_2T$）📜Q | 双通道是 mTBG 实况 |
| 谷 AFI vs 强拓扑 | 总绕数 0（谷绕数 $(1,-1)$）vs 总绕数非零 📜Q | VAFI 是弱（谷）保护 |

---

## 4. 假设-结论依赖图

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性（作者如何对待） |
|---|---|---|---|
| A1 网络模型有效 | 费米面离开隙 / 畴壁态与其他态混 | 整个 Floquet 映射失效 | 引言定性前提，未在本文化验 💭I |
| A2 无谷间散射 | 边缘原子尺度粗糙/谷间散射 | VAFI 边缘模开隙、拓扑保护消失 | 作者自述 VAFI "only protected as long as intervalley scattering absent" 📜Q |
| A4 $C_2T$ 守恒 | 磁场/面内反演破缺 | 单通道能隙机制改变（外场下普遍 AFI） | 作者用作外场预言 📜Q |
| A7 双通道 S 矩阵简化 | 释放 $P_{f1}\ne P_{f2}$ 等 | 相图定量边界移动 | 作者自述"非最一般 S 矩阵" 📜Q |
| A3 散射参数能量无关 | 离开 $\hbar\omega$ 能标 | Floquet 描述失效 | 作者声明适用前提 📜Q |
| A5 8 谐波截断 | 磁输运需更多谐波 | 收敛性 | 作者声明磁输运需增加近一个数量级谐波 📜Q |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（本文预言的实验靶标）

- AFI 边缘模 → 非局域输运测量（作者 "could then be probed by nonlocal transport measurements"）📜Q；
- 量子化电导 $e^2/h$（每谷每自旋）与 AB 振荡 → 磁输运 📜Q。

### 5.2 设计原则（Floquet 方案的类比平台）

光子晶体 / 光学晶格中可"裁剪 S 矩阵"（控制 trimer 间 hopping）实现网络物理 📜Q（作者 "can in principle"）。

### 5.3 后续文献修正（时间倒挂，💭I）

- 本文是 **De Beule 2020 PRL（T15，本文 ref 32）** 的直接后续：T15 给出双通道网络 S 矩阵，本文把它映射为 Floquet 哈密顿量并首次处理双通道的**拓扑**。
- 与 **Tsim 2020（T12，本文 ref 31）** 的 ZZ 模一致：本文 $\varphi=n\pi$ 极限复现 TZM 的三组 1D 手征 zigzag 模。
- 与 **Efimkin-MacDonald 2018（T09，本文 ref 23）**：单通道 $C_2T$ 网络的 S 矩阵与其幺正等价。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| VAFI 难实现 | 保守 $C_2T$ 的 VAFI 在真实 mTBG 很可能难实现（网络通常金属） | 📜Q（作者自述） |
| 一般边缘会开隙 | mTBG 边缘构型不明，generic edge 可能使 VAFI 边缘模开隙 | 📜Q |
| 双通道 S 矩阵非最一般 | 对称简化假设 | 📜Q（作者自述） |
| 散射参数能量无关 | $\hbar\omega\approx100\,\theta°$ meV 内近似，非严格 | 📜Q |
| 无相互作用/弛豫 | 未考虑电子-电子相互作用与晶格弛豫 | 💭I（原文未讨论） |

## 7. 与其他工作的关系（跨论文对标）

| 工作 | 关系 |
|------|------|
| De Beule 2020 PRL 125, 096402 (ref 32, =T15) | **直接引用**——双通道网络 S 矩阵来源 + AB 振荡结果对照 📜Q |
| Efimkin & MacDonald 2018 (ref 23, =T09) | 单通道 $C_2T$ 网络 S 矩阵（$s_r=s_l$）与其幺正等价 📜Q |
| Tsim 2020 (ref 31, =T12) / Fleischmann 2020 (ref 30) | 手征 zigzag 模 📜Q |
| Chalker-Coddington 1988 (ref 29) | 定向散射网络模型起源 📜Q |
| Rudner 2013 (ref 41) | Floquet 绕数定义来源 📜Q |
| Delplace 2020 (ref 38) / Potter-Chalker-Gurarie 2020 (ref 44) | 网络↔Floquet 映射的既有工作 📜Q |

> ⚠️ Phase S 外部对标（**非本文引用**，时间倒挂 💭I）见 §5.3。

## 8. 对后续研究的影响

- 为 mTBG 畴壁网络提供**哈密顿量形式**的有效模型（标准方法可处理：绕数、ribbon 谱、格林函数输运）📜Q。
- 提出 **VAFI（谷反常 Floquet 绝缘体）** 这一"总拓扑平庸、谷拓扑非平庸"的新相，连接反常 Floquet 拓扑与谷物理 📜Q。
- 与光学晶格/光子晶体类比，为驱动系统复现网络物理提供蓝图 📜Q。

## 9. 理论模型映射（供 TBPM / 输运计算对标）

| 映射 | 说明 |
|------|------|
| 网络 → trimer 晶格 | $U_F=T_3ST_2ST_1S$ 是 TBPM/Floquet 直接可解对象 📜Q |
| $\hbar\omega=2\pi\hbar v/(3l)\approx100\,\theta°$ meV | 网络能标→驱动频率，连接 $\theta$ 与 Floquet 参数 📜Q |
| 绕数 $W$ → 体-边对应 | AFI 相 $W=\pm1$ ↔ 边缘手征模数 📜Q |
| $G=(4e^2/h)\mathrm{Tr}_\omega[...]$ | Floquet 格林函数输运，对应 NEGF/散射矩阵计算 💭I（[PHY-LB]） |

---

## Phase S 目的接口（引用式）

- **Q1（edge state 如何表征）**：AFI/VAFI 边缘模的表征靶标 = zigzag ribbon 谱的手征边缘模 + 量子化电导 $e^2/h$（每谷每自旋）+ 非局域输运 📜Q。
- **Q2（理论如何解释）**：把 mTBG 畴壁网络**映射为 Floquet 紧束缚模型**，用 Floquet 绕数/谷绕数解释边缘拓扑——散射网络的体-边对应不清问题被 Floquet 哈密顿量描述解决 📜Q。
- **Q3（理论↔实验对应）**：$\hbar\omega\approx100\,\theta°$ meV ↔ 扭角能标；$e^2/h$ 量子化平台 ↔ 磁输运；AB 振荡 ↔ 磁通/周期对照 📜Q。

> **增量价值**：与 T15（散射网络统一理论）分工——T15 是**散射 S 矩阵**框架，本文是其**Floquet 哈密顿量**升级（首次处理双通道拓扑 + 给出 VAFI）；比 T15 多 = Floquet 绕数/谷绕数 + 磁输运量子化电导；少 = 无 T15 的 $\varphi\in[0,\pi/2]$ 连续扫描细节。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` 提取到 `/tmp/T18.txt`，逐项 grep 核对：**全部数字命中原文**——

| 数字 | grep 命中位置 | 结论 |
|------|--------------|------|
| $\hbar\omega=2\pi\hbar v/(3l)\approx100\,\theta°$ meV（Eq. 25） | Sec. II C | ✓ 📜Q[~] |
| 8 谐波（$m=-8,\dots,8$）、$\gamma/\hbar\omega=0.005$ | Sec. II C / Fig. 5 | ✓ |
| $1/9\le P_f\le1$、$P_{l,r}\in[1/9,1/3]$ | Sec. II A / II C | ✓ |
| $W=\pm1$、$W=\mathrm{sgn}(P_r-P_l)$、$W[P_l=1]=0$、$W[P_r=1]=1$ | Sec. II D / Appendix B | ✓ |
| $(P_r,P_l)=(0.6,0.2)$、$W=15\sqrt3l$、$L=8.5l$、$W\gg L$ | Fig. 6/13 | ✓ |
| $e^2/h$（每谷每自旋）、$G=4e^2/h$ 公式 | Sec. IV | ✓ |
| $P_{f2}\vert_{E_g=0}=1-(2\sin\varphi)^{-2}$、$P_f=3/4$、$\pi/6<\vert\varphi\vert<5\pi/6$ | Sec. III B / Fig. 9 | ✓ |
| $\varphi=\pi/2,P_{f1}=0,P_{f2}=0.3$；$\varphi=\pi/4,P_{f1}=P_{f2}=0.1$ | Fig. 11 | ✓ |
| ZZ 模 DOS$=4/\sqrt3\hbar\omega l^2$、速度=半 | Sec. III A | ✓ |
| 磁输运 $\theta_1=\tfrac{J}{\hbar\omega}\tfrac{\pi}{2}\cos\phi$（Eq. 44）、$\theta_P(x)=\pi\Phi x/(\Phi_0 l/2)$（Eq. 40）、$\Phi=B\sqrt3l^2/2$ | Sec. IV | ✓ |
| $\sim10^4(\theta°)^{-2}$ 原子 | 引言 | ✓ |

⚠️ 修正/降级：① 保留旧版"周期驱动（Floquet）"措辞、弃"周期踢动"（grep "kick"=0、"Floquet" 57 处）——已在更正日志登记；② 本文**未**用 Chern 数（用 Floquet 绕数 + 谷绕数），引言"valley Chern number ±2"是引文背景，不属本文推导。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-06 | 初读（粗读版） |
| 2026-08-20 | **S-REV 修正**：§2/Q2 "周期踢动" → "周期驱动（Floquet）"。原文为网络映射到周期驱动 Floquet 系统（grep "Floquet"=57、"kick"=0），"踢（kick）" 系 AI 自由翻译。 |
| 2026-09-08 | **按 5 块演绎结构整体重写**（应用户要求）。旧版归档 `archive/paper_review_T18_debeule2021_prb.backup_20260908.md`。补：trimer $H_0$ + S 矩阵显式式、参数分册（含符号防混 $\phi$/$\varphi$/$P_f$/$P_{f1}$）、7 条假设清单、推导链（Sec. II→IV）、结论分层、假设-结论依赖图、反向核对 pass。 |
| 2026-09-08 | **降级/删除**：旧版 "Floquet 能带给出网络的完整色散，自动包含拓扑边缘态" 过强——改为"绕数↔有限系统互验"（内部验证）；"与连续模型和 TB 结果一致，计算成本大幅降低" 无源（原文未做连续模型/TB 直接对照，仅原子数对比），已删。 |
