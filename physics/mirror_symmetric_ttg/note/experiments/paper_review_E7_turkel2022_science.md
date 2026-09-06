<!--
 * @Author       : paper-reading SKILL (delegated agent)
 * @Date         : 2026-09-03
 * @Description  : E7: Turkel et al. (2022) Science — msTTG 的"有序无序"：moiré 晶格重构、twiston/moiré soliton、平带共振与超导掺杂（4 块辨识结构 + 目的接口）
-->

# Paper Review: Turkel et al. (2022) — Orderly disorder in magic-angle twisted trilayer graphene

| 字段 | 内容 |
|------|------|
| **编号** | E7 |
| **标题** | Orderly disorder in magic-angle twisted trilayer graphene |
| **作者** | Simon Turkel¹, Joshua Swann¹, Ziyan Zhu², Maine Christos², K. Watanabe³, T. Taniguchi⁴, Subir Sachdev²,⁵, Mathias S. Scheurer⁶, Efthimios Kaxiras²,⁷, Cory R. Dean¹, Abhay N. Pasupathy¹,⁸*（¹Columbia, ²Harvard, ³NIMS, ⁴NIMS-MANA, ⁵IAS Princeton, ⁶Innsbruck, ⁷Harvard SEAS, ⁸Brookhaven） |
| **期刊** | Science 376 (6589), 193–199 (2022-04-08) |
| **DOI / arXiv** | 10.1126/science.abk1895（DOI 见页脚与页面元数据；arXiv 未在正文出现 → 外部来源无） |
| **类型** | 实验 — 低温 UHV STM/STS（4.8–7.2 K）+ 结构弛豫与连续模型/HF 计算对照 |
| **课题组** | STM 实验：Dean/Pasupathy（Columbia）；理论/计算合作：Sachdev/Scheurer（相互作用）、Kaxiras/Zhu（结构弛豫） |
| **PDF** | ✅ /home/wyl/project/knowledge/physics/mirror_symmetric_ttg/references/exp/Turkel 等 - 2022 - Orderly disorder in magic-angle twisted trilayer graphene.pdf |
| **精读日期** | 2026-09-03 |

> **共享知识引用**：⚠️ FRESH pack — 本项目 `note/shared/` 尚不存在，无 [PHY-*]/[METHOD-*] 锚点可用；本文自包含，通用物理（如 moiré 波长公式、连续模型）按正文内嵌处理。阅读疑问锚点待 shared 建立后回填。
>
> **文本来源说明**：权威文本 = pdftotext 主文 7 页（/tmp/msTTG_txt/E7_turkel2022.txt），含正文与图注；**不含 SI**（Materials and Methods 与 figs. S1–S17 均在 SI，正文标为 (18)）。凡数值性方法细节标 `NEEDS_VERIFICATION`。

---

## TL;DR

**本文想解决的问题**（问题句式）：真实魔角三层石墨烯（TTG）样品里，"镜面对称（AtA）堆叠 + 平带"这一理论前提是否真的存在？样品中不可避免的上下角失配（θ_TM ≠ θ_BM）会如何影响结构与电子结构——以及这种影响与"在 |ν|=2 附近观测到的超导（SC）"是什么关系？

**主结果**：
- 真实 TTG 发生强烈 moiré 晶格重构（MLR），**全域自锁定为局部镜面对称的 AtA 结构**（AAA/ABA/BAB 位点），把样品分割为均匀的魔角三角形/蜂窝 plaquette 畴（θ_I 饱和 ~1.5°）、准一维 moiré soliton（线缺陷）与点状 twiston（拓扑 moiré 缺陷）三类区域 📜Q[~]（正文 p1–2, Fig. 1）。
- 均匀魔角畴（θ=1.55°）上：CNP 处价带/导带 van Hove 奇点（VHS）分离 ~18 meV、平均 FWHM ~23 meV；只有 Hartree-Fock 重正化 + 4 meV 寿命展宽能定量复现 → 强准粒子相互作用重正化 📜Q[~]（正文 p3, Fig. 2）。
- MLR 的 θ/应变（ε）纹理造成**空间颗粒化（granular）电子结构**：soliton 上平带被应变抹平，twiston 处平带劈裂 ~40 meV；相关隙（correlated gap）只出现在 twiston/soliton 位点而非均匀 plaquette 区 📜Q[~]（正文 p4–6, Figs. 3–4）。
- 当 2≲|ν|≲3 时 plaquette 与 twiston 平带发生"平带共振"，Fermi 面 LDOS 实空间图最均匀——该掺杂窗口与输运观测的 SC 最优掺杂（2<|ν|<3, 转引 refs. 3,4）重合；作者提出 SC 相界沿掺杂轴**可能是无序驱动（disorder-driven）的** 📜Q（正文 p6）。

**结论/意义**（保留作者措辞强度）：E7 明确声称"DOS 单独不足以控制超导穹顶"（"it is thus clear that it is not the density of states alone that controls the superconducting dome"，正文 p5）；对"SC 相界无序驱动"只给 "raises the possibility"（提出可能性，非证实，正文 p6）；对相互作用重正化给 "clear evidence" / "clear signatures of electronic correlations"。实验上确立：TTG 的 moiré 无序是一种**可通过 δθ 设计、可通过 Vg 连续调节的"有序无序"**。

---

## 1. 系统辨识导览（判别表为全文唯一权威）

**黑箱三要素**：`{输入旋钮：θ_TM/θ_BM（失配角 δθ）、栅压 Vg（填充 ν）、局域 twist θ_x 与 heterostrain ε_x | 输出观测量：STM 形貌（λ、Λ、AAA 位点阵列）、局域 θ_x 图、AAA 位点 STS 谱（VHS 分离/宽度）、dI/dV 实空间 LDOS(EF) 图、相关隙 | 声称结论：MLR 全域锁定 AtA+θ≈1.5°；平带相互作用重正化；2≲|ν|≲3 平带共振使电子无序最小化并重合于 SC 最优掺杂（SC 相界或为无序驱动）}`

**四层变量图**（符号层一次钉死）：

| 层 | 本文实例 |
|----|----------|
| **L1 旋钮 u** | 标称扭转 θ_TM、θ_BM（名义魔角 1.56°）；栅压 Vg → 诱导载流子密度 n → 带填充 ν=4n/n_s；局域 twist θ_x ~ a/√A_x；局域应变 ε_x；样品区域选择（δθ≈0.2°/0.25°/0.3°/0.05°） |
| **L2 导出量 x₁** | moiré 波长 λ_ij ~ a/θ_ij（λ~9 nm）、moiré-of-moiré 波长 Λ~a/δθ（~70 nm）；内禀角 θ_I（畴内平均）；填充因子 ν=4n/n_s（n_s=4/A, A=moiré 单胞面积）；局域填充 ν_x=nA(x)；位移场 D=Vg/2d |
| **L3 模型量 x₂** | 连续模型单粒子带（SP1：ab initio 参数；SP2：v_F 提高 30%）；自洽 HF 重正化带；4 meV 寿命展宽；结构弛豫计算（θ_TM/θ_BM 双角）；面外起伏（正/余弦叠加模型，ref. 15） |
| **固定参数（非旋钮）** | a=0.246 nm（石墨烯晶格常数）；魔角 θ~1.56°（理论, refs. 1,2）；每 moiré 带四重简并 |
| **反推量 θ̂** | 由 moiré 单胞 Voronoi 面积反推 θ_x（θ_x ~ a/√A_x）；由虚点 moiré 格矢反推 (θ_x, ε_x) 对；由 dμ/dn 台阶定位满填充 |
| **L4 观测量 y** | STM 形貌（层间重构后的 AAA 位点晶格）；STS dI/dV 谱（AAA 位点；双 Lorentzian 拟合的 VHS 能量位置与 FWHM）；Fermi 面 LDOS 实空间图及其均匀性 |

**可辨识性判别表**（每条判别 = 判据 / 排除谁 / 确立谁）：

| 判别 | 判据（数据） | 排除谁 | 确立谁 |
|------|-------------|--------|--------|
| D1 局部堆叠=AtA（镜面对称）而非刚性失配/AtB | 单层 moiré 为六角而非蜂窝格（小 λ 格在 δθ≠0 区域处处六角，AAA 亮斑被 ABA/BAB 环绕，Fig. 1D 及 fig. S7 线谱）；δθ≠0 样品中无 AtB 大畴；弛豫计算显示 top/bottom 层局域对齐强制 AtA（fig. S9E）📜Q（正文 p1–2,6） | 刚性（无弛豫）三 moiré 模型（fig. S6 预期 λ_TM、λ_BM、Λ 三套波矢）；AtB 域（ABB/AAB/BAC） | MLR 全域锁定低能（ref. 16）AtA 镜面对称构型 |
| D2 θ 无序是"有序的"（畴均匀 + 畴界缺陷），非 MATBG 式平滑起伏 | θ_I–Λ 曲线饱和于 ~1.5°（Λ≳30 nm, Fig. 1G）；θ=1.55° 均匀区直方图 SD=0.03° → δθ<0.05°；θ_x 图呈均匀三角/蜂窝 plaquette + 线（soliton）+ 点（twiston）缺陷；弛豫计算 δθ≲0.5° 时 θ_I 锁定到 θ_TM/θ_BM 较小者 📜Q（正文 p2–4,6; fig. S10） | δθ 直接转化为平滑随机的 twist 梯度无序（MATBG 情形, ref. 27）；"电子结构随 δθ 平滑起伏" | "电子颗粒（electronic grains）" 尺寸 ~Λ 由 δθ 决定的可控 moiré 无序（正文 p5） |
| D3 平带谱=相互作用重正化，非单粒子带 | CNP 处 VHS 分离 ~18 meV：SP1（ab initio 参数）同时低估分离与宽度；SP2（+30% v_F）复现分离但宽度仍 ~6× 偏小；HF 复现分离 + ~70% 宽度，再 +4 meV 寿命展宽定量复现（Fig. 2E）；D 场在可及范围几乎不改 VHS 分离/宽度（fig. S14B）📜Q（正文 p3） | 单粒子带结构 + 位移场 D 调制（SP1/SP2）；(附带排除：无附加对称破缺即够) | 强准粒子相互作用引起的带重正化；谱的 P-H 不对称由 HF 复现（fig. S16） |
| D4 相关隙局域于 MLR 缺陷区，均匀魔角区无绝缘隙 | 绿箭头相关隙只在 twiston/soliton 谱出现（Fig. 4B,C），均匀区与 plaquette 无隙（Fig. 2B, 4A, fig. S13）；整数填充附近仅弱阻态（IIR）📜Q（正文 p6） | MATBG 式全域强关联绝缘态（refs. 19,20,30–32 之 TTG 类比）；"平带隙在均匀区打开"的预期 | 关联效应本身被 MLR 空间调制；IIR 弱化可能与无隙 Dirac 带并联导电（转引 refs. 3,4）相关 |
| D5 SC 最优掺杂 ↔ 电子无序最小化（掺杂轴相界或为无序驱动） | (i) 2≲|ν|≲3 时 δc/n（twiston-plaquette 平带能量差）最小 → 平带共振（Fig. 4G）；(ii) 共振时 LDOS(EF) 实空间图最均匀（Fig. 4H/J vs 4I）→ 无序势减弱；(iii) 该窗口与输运 SC 最优掺杂 2<|ν|<3 重合（转引 refs. 3,4）；(iv) 反证：大 LDOS 出现在 ν∈[−4,4] 多处而 SC 并非处处出现 → DOS 非唯一控制因素 📜Q（正文 p5–6） | "Fermi 面 DOS 大小单独决定 SC dome" 的假设 | SC 相界沿掺杂轴可能是 disorder-driven（作者措辞：raises the possibility；且预期对 δθ≲0.5° 样品不敏感） |

> **主结果 ↔ 判别表映射**：主结果①（AtA+θ 锁定畴化）← {D1, D2}；主结果②（相互作用重正化平带）← {D3}；主结果③（相关隙局域化）← {D4}；主结果④（共振-无序最小化-最优掺杂共现）← {D5}。
>
> **分层排除注**：D1→D2 为"结构存在性 → 无序形态/维度"分层；D3→D4 为"均匀区相互作用 → 缺陷区关联调制"。作者对 D4 中"无隙 Dirac 带导致 IIR 弱化"以"可能（It is possible that…）"措辞给出，属转引 transport 图景（refs. 3,4）的解释性框架，**非本文 STS 直接证据**（STS 的 CNP 谱被平带共振对主导，未见独立 Dirac 锥 DOS 峰/谷结构）💭I。

> **[前提与限定]**（判别结论的适用范围）：
> - **噪声/扰动**：T=4.8–7.2 K；调制电压 Vmod=0.5–2 mV（各图注）；每条谱为同一位点 10 次平均（Fig. 2 caption）；全文无背景 LDOS 数值、无测量误差棒；唯一的"±"是填充记号 n~±2，非误差棒。VHS 拟合（双 Lorentzian）细节在 SI（NEEDS_VERIFICATION）。
> - **判别性扫轴**：Vg 扫到 ν≈±4（图 4 纵轴以 n≈±4×10¹² cm⁻² 计，Fig. 4H–J 标注 n=+3.4/−0.3/−3.7×10¹² cm⁻²）；温度仅 4.8↔7.2 K（谱无显著变化, fig. S13），**未达 SC Tc 低温**；D 场轴只在 SI 检验（fig. S14B, 效果可忽略）；δθ 只在离散样品区比较（0.2°/0.25°/0.3°/<0.05°），未系统扫描 δθ 连续轴。
> - **候选集 M 边界**：结构上只比较"刚性三 moiré / AtA+MLR / AtB"；电子结构上只比较 SP1/SP2/HF；**集外未排除**：e-ph 配对机制（仅以 refs. 22,23 转引讨论）、其它对称破缺序（只以 HF 无对称破缺版本论证）、配对对称性（只推断 spin-triplet 受无序敏感, refs. 33,34 + 5）。SC 存在性本身是转引 transport（refs. 3,4,5），本文样品未共测 SC（💭I 封闭世界风险：跨样品/跨文献作 doping 轴对照）。
> - **理论/计算边界**：弛豫计算正确给出 plaquette/soliton/twiston 定性图景但**不能预测三者相对尺寸**（作者自述：或因其忽略面外起伏与 top-bottom 层间耦合，正文 p6）；单轴应变仅加在中层（refs. 25,26），作者自认低估真实 ε 效应（正文 p5）。

三层标注：📜Q = 原文事实（附位置）｜推导｜📊F = 读图估算｜💭I = 推断。**不确定度（正交轴）**：[±] 原文误差棒 / [~] 原文无误差棒 / [读图] 图提取·色标·图内标注 / [相对] 仅相对量。**全文无传统测量误差棒数值**（见更正日志）。所有数字经 pdftotext + grep 反向核对（见文末 pass）。

---

## 2. 结果与机制（按论文自身论证结构组织）

### 2.1 结构层：moiré of moiré 与 MLR——AtA 全域锁定 + θ 均匀畴化

- **两个 moiré 尺度**：STM 形貌（Fig. 1D）可见双层 moiré λ~9 nm 与 moiré-of-moiré Λ~70 nm 两种波长；λ_ij~a/θ_ij、Λ~a/δθ（δθ≡|θ_TM−θ_BM|），a=0.246 nm 📜Q[~]（正文 p1）。该区 δθ~a/Λ≈0.2°，与 SC 器件中测得的 ~0.3° 失配几乎相同 📜Q[~]（正文 p1, 转引 ref. 4）。
- **相内=AtA，失相=AtB**：两 moiré 同相处 TM-AA 叠于 BM-AA → 局部镜面对称 AtA（"A-twist-A"，含 AAA/ABA/BAB 位点）；失相处 → AtB（ABB/AAB/BAC），AtB 与 AtA 仅差顶层平移 📜Q（正文 p1）。AtB 预期为蜂窝 moiré 格、AtA 为六角格（Fig. 1B 面外起伏模型, ref. 15）。
- **MLR 全域锁 AtA**：在 δθ≠0 的样品里**找不到 AtB 大畴** → 重构在 moiré 尺度发生并把系统推向低能 AtA 构型；图 1D 中 AAA 位点位置呈周期性弯曲（warping）以强制 AtA 📜Q（正文 p1–2）。
- **θ 被"锁"到均匀值**：局域 twist θ_x~a/√A_x（A_x=以 x 为中心的 moiré 单胞面积）图（Fig. 1E,F）显示均匀三角畴（蓝色）被点状 θ 奇点（红色）包围；对 Λ≳30 nm，畴内平均角 θ_I 饱和到 ~1.5°，与 Λ 无关（Fig. 1G）📜Q[~]（正文 p2）。弛豫计算：δθ≲0.5° 时 θ_I 锁定到 θ_TM、θ_BM 中较小者（低角界面耦合更强, fig. S10）→ TTG 用额外的 twist 自由度"吸收"θ 不均匀性 📜Q（正文 p2）。
- **三类 MLR 特征区**（δθ~0.25° 区，θ̄=1.55°，Fig. 3A）：plaquette（蜂窝排列的均匀畴，θ_x~1.5°）— moiré soliton（分隔 plaquette 的准一维畴界，θ~1.6°、高应变）— twiston（soliton 网络节点上的点状拓扑缺陷，θ~1.8°）📜Q[~]（正文 p4）。图内标注 (θ,ε) 对 [读图·图内标注·重建]：B/twiston 1.8°/0.2%，C/soliton 1.6°/0.5%，D/plaquette 1.5°/0.1%；三区中仅 soliton 强烈破缺 C₃ 旋转对称，与局域异质应变 ε_x≳0.5% 一致 📜Q[~]（正文 p4）。连续模型对照组 (θ,ε)=(1.45°,0%)/(1.6°,0.55%)/(1.8°,0%)（Fig. 3F 图注）。
- **弛豫计算复现**：θ_TM=1.5°、θ_BM=1.69° 算例（Fig. 3G）自发分成不同局部角补丁，直方图三峰（plaquette/soliton/twiston, Fig. 3H）与实验一致 📜Q[读图·图注]（正文 p6 + Fig. 3 caption）；失配被"旋转进样品平面"成为角纹理。

### 2.2 电子结构层（均匀畴）：平带 VHS 对 + 相互作用重正化

- 均匀单 moiré 区（θ=1.55°，FOV 250 nm²，twist 直方图 SD=0.03° → δθ<0.05°，接近输运器件尺度）📜Q（正文 p2）。AAA 位点 STS（7.2 K，每谱 10 次平均）：CNP 处谱由部分交叠的 CB/VB 平带共振对主导；更高能软肩 = 远处带（remote band）边缘 📜Q（正文 p3）。
- **VHS 提取**：每平带在动量空间有鞍点 → DOS van Hove 奇点；双 Lorentzian 拟合：CNP 处 CB–VB VHS 分离 ~18 meV、平均 FWHM ~23 meV 📜Q[~]（正文 p3）。
- **门压依赖**：Vg 翻转使两 VHS 间谱权重转移；平带掺杂到 Fermi 面时变窄，FWHM 最小 ~15 meV（ν~±2, Fig. 2C）；VHS 分离随远离 CNP 增加且电子/空穴不对称（Fig. 2D）📜Q[~]（正文 p3）。
- **判别性计算**：SP1（ab initio 隧穿参数）低估分离与宽度；SP2（单层 v_F 提 30%）复现分离但宽度仍偏小 ~6×；**自洽 HF（无附加对称破缺）复现分离 + 约 70% 宽度，4 meV 寿命展宽补足余量**（Fig. 2E）📜Q[相对]（正文 p3）。D 场在实验可及范围不改 VHS 分离/宽度（fig. S14B）→ 排除 D 的单粒子带效应解释，确立相互作用重正化。
- **P-H 不对称**：CB 在所有掺杂下都比 VB 宽；μ 穿 VHS 的填充在电子/空穴侧不同——空穴侧 ~ν=−2.5 附近（近空穴母态）、电子侧 ≤ν~1 已穿过（HF 复现, fig. S16）。作者推断空穴母态 Fermi 面 DOS 增强或贡献于空穴侧 SC dome 的鲁棒性 📜Q[~]（正文 p5）。

### 2.3 无序的电子学：θ/ε 纹理 → 颗粒化电子结构

- 不同 MLR 区域 LDOS 差异大：plaquette（低 θ≈1.45°）谱 ≈ 均匀 TTG；soliton 上平带强度被逐步抹平至几乎不可辨（强应变 TTG 特征）；进一步增大 θ_x（ε_x 减小）平带恢复但劈裂 ~40 meV ≈ 未应变 θ~1.8° 计算 📜Q[~]（正文 p5）。
- **结论性表述**：局部电子结构由 MLR 给出的局域 (θ_x, ε_x) 决定；TTG 的 twist 无序**不像 MATBG 那样造成平滑随机起伏，而是形成电子颗粒（electronic grains），颗粒尺寸由 δθ 直接决定 → "内禀可控的 moiré 无序"** 📜Q（正文 p5）。图 1D inset 的 LDOS(EF) 图已示 MLR 引起的电子不均匀性 📜Q（Fig. 1 caption）。

### 2.4 关联层：相关隙局域化 + 平带共振（2≲|ν|≲3）

- 满填充标定：dμ/dn 阶梯式跃升处 = 满填充；四重简并 → n_s=4/A（A=moiré 单胞面积）；因 A(x) 随位置变 → 定义局域填充 ν_x=nA(x)；面积加权平均 n̄ 近似 transport 观测量（fig. S8C）📜Q（正文 p6）。
- **均匀区无隙、缺陷区有隙**：关联诱导绝缘态通常表现为以 μ 为中心的谱隙随掺杂生灭；**与 MATBG 强绝缘体相反，TTG 在整数填充附近只有弱阻态（IIR）**；均匀魔角区未观测到隙（Fig. 2B, 4A, fig. S13），隙只在 twiston/soliton 谱上于整数填充附近出现（Fig. 4B,C 绿箭头）→ 单粒子解释不了 → "confined to particular regions of the MLR" 的相关签名 📜Q（正文 p6）。IIR 未长成绝缘体可能因**无隙 Dirac 带提供并联导电通路**（转引 refs. 3,4；💭I：Dirac 带未在本文 STS 中直接辨出）。
- **平带共振**：掺杂同时移动 plaquette 与 twiston 平带（因 A(x) 差异 → 填充速率不同）；两套平带在某个 n 窗口最大重叠（Fig. 4D,E 模型：plaquette 1.45° 超晶格填到 n_P=2.4 时共振 [图注]）；实验上 twiston/plaquette 谱在 |ν|~2.5 共振（Fig. 4F [图注]）；定量判据 δc/n（twiston 与 plaquette 平带能量差, Fig. 4G）在 **2≲|ν|≲3** 取极小 → 共振，与输运 SC 最优掺杂 2<|ν|<3 大致重合；共振填充位于 plaquette 与 twiston VHS 之间 → "SC 被 VHS 夹住"与 transport 一致 📜Q[~]（正文 p6）。
- **共振 → 实空间无序最小化**：CNP 时 LDOS(EF) 图强烈无序（Fig. 4I, δθ~0.3° 同 SC 器件 ref. 4；plaquette 横向 ~50 nm ≈ SC 相干长度, 转引 refs. 3,4）；调向共振（电子侧 n=+3.4×10¹²、空穴侧 n=−3.7×10¹² cm⁻² [读图·图内标注]）后 LDOS 图显著变均匀（Fig. 4H,J）→ 无序势被削弱 📜Q[~]（正文 p6）。

### 2.5 收束：DOS 不是 SC 的唯一控制量；相界或为 disorder-driven

- 大 LDOS 出现在 ν∈[−4,4] 的多个填充（Fig. 2F），而 transport 中 SC 只在 |ν|=2 附近（最优 2<|ν|<3）→ "not the density of states alone" 📜Q（正文 p5）。谱的 P-H 不对称 vs transport SC dome 的近似 P-H 对称 → 有额外因素决定 SC 相界 📜Q（正文 p5）。
- 平带共振 + 无序最小化 + SC 最优掺杂三者共现 → "raises the possibility that the superconducting phase boundary along the doping axis is disorder driven" 📜Q（正文 p6）；若真，则对 SC 序参量对称性有影响（spin-triplet 对这类无序敏感, refs. 33,34；高场 reentrant SC 与其兼容, ref. 5）。作者明确：确认此假说需要直接测量无序对 SC 的影响（未来工作：经 δθ 控制 moiré 缺陷密度）📜Q（正文 p6–7）。

---

## 3. 实验方法

### 3.1 器件
- "cut and stack" 法制备三层石墨烯；电接触用预置 graphite finger + Field's metal 焊料（fig. S1）📜Q（正文 p1）。石墨背栅施加 Vg；D=Vg/2d（d=介电厚度）📜Q（正文 p3）。hBN 晶体由 K. Watanabe/T. Taniguchi 提供（致谢），但**具体封装/栅结构、掺杂换算参数在 SI**（未含于本文本）→ `NEEDS_VERIFICATION`。STM 测量环境：超高真空，4.8–7.2 K 📜Q（正文 p1）。

### 3.2 结构与掺杂标定
- 局域 twist 角：由 AAA 位点 Voronoi 图胞面积反推 θ_x~a/√A_x（a=0.246 nm）（Fig. 1 caption）📜Q；(θ_x, ε_x) 对由虚线 moiré 格矢提取（Fig. 3 caption）📜Q；θ_I 为各三角畴内 twist 平均（Fig. 1G，误差棒=畴内 θ 分布的 1 SD，非测量误差）📜Q（Fig. 1 caption）。
- 填充标定：ν=4n/n_s、n_s=4/A、局域 ν_x=nA(x)、满填充由 dμ/dn 台阶判定（见 §2.4）📜Q；n̄ 面积加权平均 ≈ transport 观测量（fig. S8C）📜Q（正文 p6）。
- 面外起伏模型：AtA/AtB 起伏按局域双层堆叠的正弦函数叠加估算（ref. 15, Fig. 1B caption）📜Q。

### 3.3 测量（STM/STS）
- 形貌（恒流模式；高度起伏主导 → 用 moiré 格对称性判 AtA/AtB）与 dI/dV 谱/图（LDOS ∝ dI/dV）。VHS 用双 Lorentzian 拟合并提取位置与 FWHM 📜Q（正文 p3）。常用设定：Vset=300 mV、Iset=120–150 pA、Vmod=0.5–2 mV（Fig. 1D/2B/2F/4 各 caption）📜Q。STS 温度 7.2 K，冷却至 4.8 K 谱无显著变化（fig. S13）📜Q（正文 p3）。
- 微分导数：满填充信号 dμ/dn 由谱（gate series）的台阶式跃升识别（图 4A,C 黄箭头）📜Q。

### 3.4 计算对照（理论模型与方法）
- **连续模型单粒子**：refs. 1,2,17 的 TTG 连续模型；SP1 用 ab initio 导出的层间/层内隧穿参数（ref. 13）；SP2 将单层 v_F 提高 ~30% 📜Q（正文 p3）。异质应变处理：单轴应变仅施于中层以保持镜面对称（refs. 25,26），作者自认低估真实 ε 效应（正文 p5）。
- **相互作用**：CNP 处自洽 HF（refs. 7,18，无附加对称破缺）→ 带重正化 + 4 meV 寿命展宽（正文 p3）；掺杂依赖的相互作用计算（含 D 场）超出本文范围（正文 p3，作者自述"primarily experimental work"）。
- **结构弛豫**：双角 (θ_TM, θ_BM) 体系的 MLR 弛豫计算（ref. 28；算例 θ_TM=1.5°/θ_BM=1.69°），结果见 figs. S9/S10 与 Fig. 3G/H（正文 p2,6）。

---

## 4. 关键数据（提取链 + 验证链 + 不确定度标注）

> **不确定度总声明**：全文无传统误差棒数值；[~] 表原文 ≈ 给定；[读图] 表来自图/图注/图内标注（含两栏版式重建，见更正日志）；分布型数字（0.03°、Fig.1G 误差棒）是角度分布宽度而非测量误差。

**表 A — 结构/MLR 参数**

| 量 | 值 | 来源等级 | 出处 |
|---|---|---|---|
| 石墨烯晶格常数 a | 0.246 nm | 📜Q[~] | 正文 p1 |
| 双层 moiré 波长 λ | ~9 nm | 📜Q[~] | 正文 p1, Fig. 1D |
| moiré-of-moiré 波长 Λ | ~70 nm | 📜Q[~] | 正文 p1, Fig. 1D |
| 图 1D 区角度失配 δθ~a/Λ | ~0.2° | 📜Q[~]（推导式在原文） | 正文 p1 |
| SC 器件（ref. 4）失配 | ~0.3° | 📜Q[~]（E7 转引） | 正文 p1 |
| 名义魔角（refs. 1,2 理论） | ~1.56° | 📜Q[~]（转引） | 正文 p1 |
| θ_I 饱和值（Λ≳30 nm） | ~1.5° | 📜Q[~] | 正文 p2, Fig. 1G |
| 均匀区（Fig. 2A）twist 直方图 SD | 0.03° → δθ<0.05° | 📜Q[~] | 正文 p2 |
| Fig. 3A 区空间平均 twist | θ̄=1.55°（δθ~0.25°） | 📜Q[~] | 正文 p4 |
| plaquette 典型 θ / 模型 θ | ~1.45–1.5° / (1.45°, 0%) | 📜Q[~] / 📜Q[图注] | 正文 p5 / Fig. 3F |
| soliton θ / ε（图内标注） | 1.6° / 0.5%；正文 ε_x≳0.5% | 📊F[读图·图内标注]；📜Q[~] | Fig. 3C 标注；正文 p4 |
| twiston θ / ε（图内标注） | 1.8° / 0.2% | 📊F[读图·图内标注] | Fig. 3B 标注 |
| plaquette ε（图内标注） | 0.1% | 📊F[读图·图内标注] | Fig. 3D 标注 |
| 模型对照组 (θ,ε) 第三组 | (1.8°, 0%) | 📜Q[图注] | Fig. 3F caption |
| 弛豫算例 θ_TM / θ_BM | 1.5° / 1.69° | 📜Q[图注] | Fig. 3G caption |
| 共振区 plaquette 横向尺寸 | ~50 nm ≈ SC 相干长度 | 📜Q[~]（相干长度转引 refs. 3,4） | 正文 p6 |
| θ 锁定适用上限 | δθ≲0.5° | 📜Q[~] | 正文 p2,6（fig. S10） |
| 均匀区 FOV / Fig. 3A inset FFT 面积 | 250 nm² / 320 nm² | 📜Q | 正文 p2 / Fig. 3 caption |

**表 B — 谱学/电子结构数据**

| 量 | 值 | 来源等级 | 出处 |
|---|---|---|---|
| CNP：CB–VB VHS 分离 | ~18 meV | 📜Q[~]（双 Lorentzian 拟合） | 正文 p3 |
| CNP：VHS 平均 FWHM | ~23 meV | 📜Q[~] | 正文 p3 |
| FWHM 随掺杂最小 | ~15 meV @ ν~±2 | 📜Q[~] | 正文 p3, Fig. 2C |
| 高 θ（twiston, ε→0）平带劈裂 | ~40 meV ≈ θ~1.8° 未应变计算 | 📜Q[~] | 正文 p5 |
| SP2 宽度 vs 实验 | 仍偏小 ~6× | 📜Q[相对] | 正文 p3 |
| HF 复现宽度占比 | ~70%，+4 meV 展宽定量复现 | 📜Q[相对][~] | 正文 p3 |
| SP2 v_F 增强 | ~30% | 📜Q[相对] | 正文 p3 |
| μ 穿 VHS 的填充（P-H 不对称） | 空穴 ~ν−2.5；电子 ≤ν~1 | 📜Q[~]（原文记 n） | 正文 p5 |
| 相关隙出现位置 | 仅 twiston/soliton，整数填充附近 | 📜Q | 正文 p6, Fig. 4B,C |
| 共振填充窗口 | 2≲|ν|≲3（模型 n_P=2.4；实验 ~|ν|2.5） | 📜Q[~] + 📜Q[图注] | 正文 p6 / Fig. 4 caption |
| LDOS(EF) 共振载流子密度 | 电子 n=+3.4×10¹² cm⁻²；空穴 n=−3.7×10¹² cm⁻²；CNP 图 n=−0.3×10¹² cm⁻² | 📊F[读图·图内标注] | Fig. 4H–J 标注 |
| 满填充密度 | n_s=4/A；ν=4n/n_s | 📜Q（公式在原文） | 正文 p6 |
| SC 相关 doping（transport 转引） | |ν|=2 附近；最优 2<|ν|<3 | 📜Q（E7 转引 refs. 3,4） | 正文 p5 |
| TTG 首代器件 Tc（转引） | 最高 2.9 K | 📜Q（E7 转引 refs. 3,4 语境） | 正文 p1 |

**表 C — 测量条件（captions 提取）**

| 量 | 值 | 来源等级 | 出处 |
|---|---|---|---|
| 测量温度 | 4.8–7.2 K（STS 主体 7.2 K） | 📜Q | 正文 p1,3 |
| Vset / Iset / Vmod | 300 mV / 120–200 pA / 0.5–2 mV（各图不同） | 📜Q[图注] | Figs. 1D, 2B, 2F, 4 |
| Fig. 2B 栅压范围（轴） | −6 V 至 +6 V | 📊F[读图·轴] | Fig. 2B 轴标注 |
| STS 每条谱平均 | 10 次（单 AAA 位点） | 📜Q[图注] | Fig. 2 caption |

**验证链（互验/旋钮依赖）**
- 结构互验：实验形貌（Fig. 1E,F；3A）↔ 弛豫计算（fig. S9E, Fig. 3G,H trimodal）定性互验（作者自述相对尺寸不吻合）📜Q。
- 电子结构互验：实验 VHS 分离/宽度 ↔ SP1/SP2/HF 三计算（Fig. 2E）——判别性对照的核心；D 场负对照（fig. S14B）📜Q。
- 掺杂轴验证：dμ/dn 满填充标定（局域 n_s=4/A）→ ν_x=nA(x) → n̄↔transport n（fig. S8C）；LDOS 均匀化（Fig. 4H–J）↔ δc/n 极小（Fig. 4G）↔ 输运 SC dome（转引 refs. 3,4）三者 doping 轴对齐 📜Q。
- 温度负对照：4.8 K vs 7.2 K 谱不变（fig. S13）📜Q。
- 跨区一致性：θ 直方图 SD=0.03°（δθ<0.05° 均匀区）vs θ̄=1.55°±θ 纹理（δθ=0.25°/0.3° 区）——θ 均匀性随 δθ 的"可控无序"主线的两极 📜Q[~]。

---

## 5. 主要结论

1. **结构自稳定于镜面对称魔角构型**：真实 TTG 经 MLR 全域重构为局部 AtA（镜面对称）构型，θ_I 被锁定在 ~1.5°（名义魔角 1.56° 附近），plaquette 畴尺度可达 ~50 nm（量级同 SC 相干长度）——首次给出理论所依赖的"镜面对称堆叠"的直接实空间证据（尽管以 AtA 为主、非完美全域）📜Q。
2. **魔角平带存在强相互作用重正化**：均匀区 VHS 分离/宽度只有 HF + 4 meV 展宽可复现；单粒子计算系统性失配 → "clear evidence for a pronounced band renormalization…caused by strong quasiparticle interactions" 📜Q（正文 p3, 措辞为 evidence）。
3. **相关态被 MLR 空间调制**：相关隙只在 twiston/soliton 出现，均匀魔角区无隙、无 MATBG 式强绝缘体（只有 IIR）📜Q。
4. **电子无序随掺杂可调**：TTG 的 moiré 无序是"电子颗粒"型（尺寸由 δθ 定），且 Vg 可系统性调节其强度——LDOS 在平带共振（2≲|ν|≲3）时最均匀 📜Q。
5. **SC 相界（doping 轴）或为无序驱动**：DOS 大小不单独决定 SC dome；共振-无序最小化-最优掺杂共现 "raises the possibility that the superconducting phase boundary along the doping axis is disorder driven"（提出可能性，非证明）；顺带给出序参量对称性推论空间（spin-triplet 敏感于该无序）📜Q（正文 p6–7）。

---

## 6. 局限与未解决

1. **SC 与结构/谱学未在同一样品共测**：本文样品无 transport SC 测量，doping 轴对照是跨样品、跨文献（refs. 3,4）的空间相关论证；"共振掺杂≈SC 最优掺杂"本质是相关而非因果（💭I 封闭世界风险，作者亦承认需直接测量无序对 SC 的影响才能确认，正文 p6–7）。
2. **方法细节与多数数值证据在 SI**：Materials and Methods、figs. S1–S17（含器件堆叠细节、VHS 拟合流程、fig. S14B D 场负对照、fig. S16 HF P-H 复现、fig. S8C 局域填充统计图）不在本文提取文本内 → 本文未逐项核对，`NEEDS_VERIFICATION`。
3. **无误差棒**：全文数值为 ~/≈，无测量不确定度；唯一分布量 SD=0.03° 与 Fig. 1G 误差棒为角度/θ_I 分布宽而非测量误差；VHS 拟合误差未给。
4. **Dirac 带未获直接谱学证据**："无隙 Dirac 带并联通路"解释 IIR 弱化时引用 transport（refs. 3,4）；本文 STS 的 CNP 谱由平带共振对主导，未见被独立辨出的 Dirac 锥 DOS 签名（💭I：或因 AAA 位点局域探测、能量窗口/温度所致，需验证）。
5. **温度窗口窄**：仅 4.8–7.2 K，远未达 SC Tc；相关隙的低温演化未测。
6. **理论对照的近似边界**：弛豫计算不能预测三区相对尺寸（作者归因于忽略面外起伏与顶/底耦合）；应变模型只在中层加单轴应变、低估真实 ε；掺杂依赖的相互作用计算（含 D 场）未做（作者自述 out of scope）。
7. **均匀性结论的统计基础有限**：LDOS 均匀化论证基于单个 ~250–320 nm² FOV 与有限 doping 采样；δθ 连续性未系统扫描（"可控无序"主张的普适性待 δθ 系列实验）。
8. **候选集未穷尽**：只与刚性-AtA/AtB 结构模型及 SP1/SP2/HF 电子模型对照；e-ph、配对对称性、其它关联序未直接检验。

---

## 7. 与其他工作的关系（跨论文对标，仅 E7 文本内引述/自身比较）

- **MATBG（反面对照, 同文内比较）**：MATBG SC 出现在多个整数填充（ref. 21: Lu et al., Nature 574, 653, 2019）而 TTG 只在 |ν|=2 邻域（refs. 3,4）；MATBG 有强关联绝缘体（refs. 19 Kerelsky、20 Xie、30 Jiang、31 Choi）而 TTG 只有 IIR；MATBG twist 无序为平滑随机型（ref. 27: Zondiner et al., Nature 582, 203, 2020）而 TTG 为颗粒型——E7 全文的判别基准即 MATBG。📜Q（E7 引述, 未核对各原文）。
- **TTG transport 同代工作（本文 doping 轴基准）**：ref. 3 = Park, Cao et al., Nature 590, 249 (2021)；ref. 4 = Hao et al., Science 371, 1133 (2021)——SC 于 |ν|=2 附近、最优 2<|ν|<3、近似 P-H 对称 dome；ref. 5 = Cao, Park et al., Nature 595, 526 (2021)——高场 reentrant SC / 量子干涉。E7 把 transport 测得的 dome、相干长度与 δθ~0.3° 失配作为对照锚。📜Q（转引）。
- **TTG 理论谱系**：魔角预言 refs. 1 (Khalaf et al., PRB 100, 085109, 2019)、2 (Li-Wu-MacDonald, arXiv:1907.12338)——θ~1.56° 两套平带；相关序预言 refs. 7 (Christos-Sachdev-Scheurer)、8 (Fischer et al., npj QM 7, 5, 2022)、9 (Qin-MacDonald, PRL 127, 097001, 2021)；HF/连续模型方法与 ab initio 参数 refs. 13,17,18；MLR 能量学 ref. 16 (Carr et al., Nano Lett. 20, 3030, 2020)；弛豫方法 ref. 28 (Zhu et al., PRB 101, 224107, 2020)；应变对平带影响 refs. 25 (Bi-Yuan-Fu, PRB 100, 035448, 2019)、26 (Rubio-Verdú et al., Nat. Phys. 18, 196, 2022)。
- **与"DOS→e-ph SC"图景的关系**：E7 明确反驳把高 DOS 直接当作 TTG SC 判据（"not the density of states alone"），但保留 refs. 22 (Lian-Wang-Bernevig)、23 (Wu-Hwang-Das Sarma) 关于 DOS 增强支持 e-ph SC 的 MATBG 图景作为对照背景 📜Q（正文 p5）。
- **无序与配对对称性**：引 refs. 33 (Scheurer-Samajdar, PRR 2, 033062, 2020)、34 (Anderson, 1959) 论证无序敏感序参量（spin-triplet 方向）与 ref. 5 reentrant SC 兼容——把"无序"提升为配对对称性判别杠杆的设想 📜Q（正文 p6–7）。

---

## 8. 对后续研究的影响

1. **结构观测量纲**：确立"θ 直方图 SD + Voronoi AAA 网格 + plaquette/soliton/twiston 分类 + δc/n(ν)"为一套可复用的 STM 表征协议；"twiston""moiré soliton"成为 TTG/多层 moiré 的标准词汇（本文定义：点状拓扑 moiré 缺陷 / 准一维畴界）。
2. **对项目假说（flat+Dirac 高可调性→SC）的限定**：SC 掺杂窗口同时要求平带共振与无序最小化——后续理论/实验须把 moiré 无序当作与 DOS 并列的轴；"Dirac 带并联通路→IIR 弱化"为该假说中 Dirac 角色的实验旁证需求点（见目的接口 Q3）。
3. **可执行预言**：δθ 是设计旋钮——"通过 δθ 可控调 moiré 缺陷密度 → 检验 SC 对非磁杂质/无序的敏感性与配对对称性"（作者明示的 future work 路线）；δθ≲0.5° 内 SC 最优 doping 基本不变。
4. **计算对标靶点**：任何 TTG 平带计算应能复现 CNP VHS 分离 ~18 meV / FWHM ~23 meV（含 4 meV 展宽换算）；MLR 应变/θ 纹理须进真实器件模型（见 §9）。
5. **谱学细节资产**：P-H 不对称（CB 恒宽于 VB）+ HF 复现 → 对局域填充-带结构映射（μ 穿 VHS 位置空穴 −2.5 vs 电子 ~1）的后续 STS 研究是参照系。

---

## 9. 理论模型映射（供计算对标）

| 本文量 | 计算侧对应 | 备注 |
|---|---|---|
| 名义 twist θ（魔角 ~1.56°） | 计算主参数；实际样品 θ_x 展布 1.45°–1.8°（plaquette 1.45–1.5 / soliton ~1.6 / twiston ~1.8） | 真实器件需按 θ 纹理而非单 θ 建模（颗粒尺寸 ~Λ~a/δθ） |
| heterostrain ε_x（soliton ε≳0.5%） | 应变项（仅中层单轴 → 保守下限） | 应变抹平平带、C₃ 破缺；strain 尺度 ε~0.1–0.55% |
| 平带 VHS 分离 / FWHM（CNP 18/23 meV；最小 15 meV @|ν|~2） | 带宽/鞍点能量差对标；宽度含 ~4 meV 展宽（寿命） | HF 无对称破缺 + 展宽即够；勿需额外序 |
| 平带共振窗口 2≲|ν|≲3（n_P=2.4 模型值） | 局域 ν_x=nA(x)：plaquette vs twiston 平带相对位移的交叉点 | 计算"δc/n(ν)"极小 = 共振判据，可作预言输出 |
| 相关隙位置（仅 twiston/soliton） | 局域填充-关联强度映射（缺陷区高 ε/高 θ） | 均匀区无隙 → 均匀畴平带关联弱于 MATBG |
| P-H 不对称（CB>VB 宽；μ 穿 VHS: 空穴 −2.5 / 电子 ~1） | 粒子-空穴不对称带结构/填充依赖自能 | 与近似 P-H 对称的 SC dome 并存 → "额外因素"（无序/应变） |
| LDOS(EF) 均匀性（CNP 无序 → 共振均匀） | 无序势强度随填充演化；可对标 σxx 相关输运 | 掺杂轴上的"电子无序可调性"是本文核心新变量 |
| 观测量接口 | AAA 位点 dI/dV（LDOS）；双 Lorentzian VHS 拟合输出；θ_x~a/√A_x 反推 | 计算输出 ↔ STS 的直接比对量 |
| 位移场 D=Vg/2d | 单粒子带调制弱（fig. S14B: 可及 D 无效）→ 本文 doping 轴效应主要来自填充而非 D | 计算勿把 Vg 效应主要建模为 D |

---

## 目的接口（随项目增删，不进入正文）

**项目背景**：msTTG（3 层，顶/底对齐、中层转 θ）；导师假说：平带 + Dirac 锥共存 → 高可调性 → 超导。本文角色 = 无序/关联竞争如何作用、与 SC 掺杂关系（E7 属"实验证据 + 结构-电子学图景"）。

- **Q1（实验）：twiston/moiré soliton 无序如何产生空间颗粒化电子结构？Fermi 面 DOS 均匀性与超导掺杂的关系？** → MLR 把 δθ 失配转译为"有序无序"：plaquette（θ≈1.45–1.5°, ε≈0.1%）/soliton（θ≈1.6°, ε≳0.5%, 平带被抹平、C₃ 破缺）/twiston（θ≈1.8°, ε≈0.2%, 平带劈裂 ~40 meV）三类区各自 (θ,ε) → 各自 LDOS，形成由 δθ 定尺寸（~Λ）的电子颗粒（§2.1, 2.3, 表 A/B）；实验上"颗粒间平带失配 δc/n"在 2≲|ν|≲3 取极小 → Fermi 面 LDOS(EF) 实空间最均匀（图 4H–J），与 transport 的 SC 最优掺杂 2<|ν|<3 重合（转引 refs. 3,4）→ DOS 均匀性（即无序最小化）是该窗口的实验特征（§2.4, D5）。
- **Q3（证据强度）：无序/关联竞争如何影响超导，对假说证据链有何限定？** → 本文给出**结构性限定而非直接证据**：(i) 大 DOS 出现在 ν∈[−4,4] 多处而 SC 只在 |ν|=2 邻域 → "DOS 单独不控制 SC dome"（对"高 DOS→SC"朴素链的否定）；(ii) SC 相界 doping 轴可能是 disorder-driven（"raises the possibility"，需直接无序-SC 实验确认）；(iii) 均匀魔角区无相关隙而缺陷区有隙、IIR 弱化被归因于无隙 Dirac 带并联（后者转引 transport 图景，本文 STS 未直接辨识 Dirac 锥）→ 支持"flat+Dirac 共存"作为 IIR 弱化机制的可检验推论，但把超导证据链从"结构→SC"改写为"结构→(共振+无序最小化)→SC"（§2.5、§5 结论 3/5、§6 局限第 1 与第 4 条）。
- **增量价值**：同族笔记中首篇给出 msTTG **实空间结构-电子学-关联的自洽图像**（全域 AtA 锁定、θ 锁定 ~1.5°、无序颗粒化与可调性），并把"无序"确立为与 DOS 并列的 SC 掺杂轴判据；报告/Phase S 取用 §2.1–2.5 与表 A–C 的核心数字（注意全部无误差棒，SC 数值为转引）。

---

## 反向核对 pass (2026-09-03)

对 /tmp/msTTG_txt/E7_turkel2022.txt 逐项 grep（`grep -o`/`grep -n`），全部命中：

- 结构量：`0.246`✓ `9 nm`✓ `70 nm`✓ `0.2°`✓ `0.25°`✓ `0.3°`✓（两处）`1.56`✓（正文+Fig.1 caption）`1.55`✓ `1.5°`✓（Fig.1G/正文）`1.45`✓ `1.8°`✓ `1.69`✓ `0.03°`✓ `0.05`✓（δθ<0.05°）`0.5%`✓ `0.55%`✓ `0.1%`✓ `50 nm`✓（两处）`30 nm`✓（Λ≳30nm 处渲染为 "L ≳ 30nm"）`250-nm`✓ `320-nm`✓ `2.9 K`✓
- 谱学量：`~18`✓ `23 meV`✓ `15 meV`✓ `40 meV`✓ `4 meV`✓ `70% of their widths`✓ `~30%`✓ `factor of ~6`✓ `2.4`✓（Fig.4 caption n_P=2.4）`2.5`✓（"at jnj e 2:5"=≈2.5, Fig.4 caption）`2 ≲ jnj ≲ 3`✓ `2 < jnj < 3`✓ `jnj ¼ 2`✓（=2）`–2.5`✓（"n ~ –2.5"）`n ~ 1`✓（电子侧穿 VHS）
- 密度/图注：`3.4x10`✓ `3.7x10`✓ `-0.3x10`✓（Fig.4H–J 图内标注）`ns = 4/A`✓ `4.8 to 7.2`✓ `7.2 K`✓ `4.8 K`✓
- 图注条件：`300 mV`✓ `120 pA`✓ `150 pA`✓ `200 pA`✓ `2 mV`✓ `1 mV`✓ `0.5 mV`✓
- 全文 `±` 仅命中 "n ~ ±2"（填充记号，非误差棒）→ 据此在全文声明"无传统误差棒"。
- 图中标注重建（两栏版式）已在正文以 📊F[读图·图内标注·重建] 显式标注：Fig.3B–D 的 (θ,ε) 对、Fig.4H–J 的 n 值、Fig.2B 栅压 −6/+6 V 轴（`-6`/`+6` 命中）。
- ⚠️ 未核对项：SI（figs. S1–S17、Materials and Methods、references 39–53）不在提取文本内 → 表 C 之外的任何方法数值均未反向核对，标 `NEEDS_VERIFICATION`；引用其他论文的转引数值（Tc 2.9 K、SC 掺杂窗口、相干长度、MATBG 行为）仅按 E7 文本引述处理，未核对 refs. 3,4,5 原文（如需进报告核心结论须回查原论文）。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-09-03 | 初始版本（全新笔记，无既往 review 可对照）。 |
| 2026-09-03 | 提取版式：Science 两栏交错使个别符号变形（"0:5°""1:55°""jnj ¼ 2""e 2:5"≈≈2.5、θ̄=1.55° 渲染为 "1:55°"）→ 均按上下文与 grep 命中还原为 1.55°/0.5°/≈2.5 等；无源数字风险由反向核对 pass 覆盖。 |
| 2026-09-03 | 图内标注（Fig. 3B–D 的 θ/ε 对、Fig. 4H–J 的 n 值、Fig. 2B 栅压范围）来自两栏错排重建 → 全部降级为 📊F[读图·图内标注·重建]，不进报告核心量化结论。 |
| 2026-09-03 | 转引与自测分离：Tc=2.9 K、SC 最优掺杂 2<|ν|<3、|ν|=2、相干长度~50 nm 属 E7 转引输运文献（refs. 3,4,5）→ 标 📜Q(转引)，非 E7 测量。 |
| 2026-09-03 | 无±未声明：全文唯一 "±" 为填充记号 "n~±2"；Fig. 1G 误差棒与 0.03° SD 为分布宽度 → 已在正文 §1/§4 声明"全文无传统测量误差棒数值"。 |
| 2026-09-03 | SI 未含：fig. S14B（D 场负对照）、fig. S16（HF P-H 复现）、fig. S8C、拟合/封装细节仅按正文提及转述 → 未作数值引用，方法细节标 NEEDS_VERIFICATION。 |
