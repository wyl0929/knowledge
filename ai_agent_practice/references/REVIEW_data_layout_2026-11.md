<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-11-01
 * @FilePath     : /knowledge/ai_agent_practice/references/REVIEW_data_layout_2026-11.md
 * @Description  : 数据资产按模型组织（而非按 phase/时间）—— 提问 / 检查内容 / 问题分析 / 改进方案
-->

# 数据资产：按模型组织，而不是按 phase（提案）

> **性质**: **提案 + 体检报告**。裁决前**不改** `data/` 目录、不删任何文件。
> **读者**: principal（裁决）+ planning（采纳后落 `data/README.md` 与 `phase-wrapup`）。
> **范围**: `data/`（5.2 GB，其中 `outputs` 4.6 GB）+ `runs/`（23 GB，645 个 LDOS 数据点 + 全部 QE 场）。
> **一句话**: 现在"按 phase 存"不是因为 phase 是好的分类，而是**因为 phase 是唯一能反查模型的索引**；把 `model_id` 写进数据后，改成**按模型检索**，但**不搬字节**（hardlink 视图 + catalog）。
> **配套文档**: Phase 侧见 [`REVIEW_phase_division_2026-11.md`](REVIEW_phase_division_2026-11.md)。

---

## 〇 问题（提问原文）

> 2. 数据管理. `data/outputs/` 中的 data 是按 phase 存放的, 导致 phase 关闭一段时间后, 忘记了要找数据是哪个 phase 生产的了. 是否应该按 **模型** 分类存放而不是按生产的时间来存放?

| # | 子问题 | 本文位置 |
|---|---|---|
| Q1 | "忘记是哪个 phase 生产的"是不是真的会发生（证据） | §2.1 |
| Q2 | 为什么会这样（根因：模型身份缺失） | §2.2 |
| Q3 | 该不该按模型分类 | §3.1–§3.2 |
| Q4 | 具体怎么改、代价多少、怎么机检 | §3.3–§3.6 |

---

## 一、检查了什么

| 检查对象 | 读了哪些部分 | 抽出什么 |
|---|---|---|
| `data/` 全树 | 目录、文件数、大小 | 5 个包的布局、体量、分组口径 |
| 包级 `README.md`（5 份：`n134_lkcf` · `r04` · `r04/r06` · `r05` · `r06`；+ 顶部 `data/README.md`） | 全文 | 包的自述来源、四元索引、数据政策 |
| `data/outputs/*/manifest.json` + `raw_manifest.json` | 结构 + 计数 + sha | 件数、字节、来源路径、重复证据 |
| `runs/*/*/meta.json`（645 个） | 全部字段 | 口径覆盖率（m/ts/rs/selection/structure/rescale）、模型指纹 |
| `runs/*/*/manifest.json`（34 份） | `data[]` / `fold_info` | QE 侧的目录、件数、能量数（QE 无 `meta.json`） |
| `data/outputs/n134/LDOS/*.txt` 与 `n134_lkcf/ldos/*/ldos.txt` | 首行表头 | 老数据的口径字段（R01/R02 无 `meta.json`，只能读头） |
| `runs/README.md` · `reports/2026-11_baseline_d060/DATA_MAP.md` | 全文 | 已有的手工索引及其过期情况 |
| `git ls-files data/` | 全量 | 进版本控制的只有元数据类文件（27 个） |
| `.gitignore` | `data/` 规则段 | 哪些文件被跟踪、哪些只在本机 |

```bash
# 体量
du -sh data data/inputs data/outputs; du -sh data/outputs/*/; du -sh runs runs/R07

# 重复字节（同一个文件在两个包里）
sha256sum data/outputs/r03_dw_decay/02_profile_ab_ba/ts8192/data/h1b_p430/ldos.txt \
          data/outputs/r04/1_x_ldos_waterfall/raw/1a_d060_R03_H1b/h1b_p430/ldos.txt

# 元数据覆盖率
python3 - <<'PY'
import json,glob,collections
ps=glob.glob('runs/*/*/data/*/meta.json'); c=collections.Counter()
for p in ps:
    d=json.load(open(p))
    for k in ('structure','rescale','potential'):
        if d.get(k) is not None: c[k]+=1
print(len(ps), c)
PY

# 两个变体的元数据是否可区分
grep -h 'extend_hop_mode' runs/R07/r07_R6/data/r6{m,g}_d000_ab/meta.json

# 一个 phase 的数据是否被拆到两个包
find data/outputs/r06 -maxdepth 2 -type d | sort
find data/outputs/r04/r06 -maxdepth 2 -type d | sort

# 进版本控制的数据文件
git ls-files data/ | wc -l
```

**检查边界**：只做只读扫描与 sha 对比；**没有移动、重命名、删除任何文件**；没有复核任何物理读数。

---

## 二、问题分析

### 2.1 六条证据

**证据 1｜一个结构（n134 · P4 弛豫）的数据分布在 4 个交付包**

| 包 | 内容 | 体量 |
|---|---|---|
| `data/outputs/r03_dw_decay/` | H0/H1b 剖面、方法收敛 | 62 MB |
| `data/outputs/r04/` | 16 点族 waterfall + QE heatmap（232 张）+ G1–G9 支撑组 | 1.9 GB |
| `data/outputs/r04/r06/` | **R06 的两个任务**（R2 x_L、R3 下层） | 含在 r04 内 |
| `data/outputs/r05_dos_EF/` | DOS（E_F 的输入） | 11 MB |

而 R07 的数据（8.7 GB）**根本还不在 `data/outputs`** 里 —— 它在 `runs/R07/`。

**证据 2｜同一份字节存了两遍（sha 相同）**

```
data/outputs/r03_dw_decay/02_profile_ab_ba/ts8192/data/h1b_p430/ldos.txt
data/outputs/r04/1_x_ldos_waterfall/raw/1a_d060_R03_H1b/h1b_p430/ldos.txt
  → 均为 bb0e295e8c06646a…（54 点 / 20 MB 全量重复）
```

**证据 3｜一个 phase 的包被拆到两个 phase 目录里**
R06 有 7 个任务：C1/R1/R4/R5/R7 在 `data/outputs/r06/`（5 组），而 **R2/R3 在 `data/outputs/r04/r06/`** —— 拆分理由是"同族同处，便于与 R04 一起取用"，即**按模型拆的**。这说明按模型组织的需求已经真实存在，只是以临时方式实现。

**证据 4｜包是 `runs/` 的整份副本**
`data/outputs/r06/raw_manifest.json` 自述「源 = `runs/R06/r06_<TASK>/data/**`（只读复制；`runs/` 仍是权威工作区）」：**637 件 / 1.87 GB** raw 复制，包总 2.2 GB ≈ `runs/R06` 的 2.3 GB。R04 包同理（`raw_manifest.json` 记 **690 件 / 1.69 GB**，包总 1.9 GB ≈ `runs/R04` 的 2.0 GB）。⇒ `data/outputs`（4.6 GB）里**绝大部分是第二份**。

**证据 5｜phase 一关，包就不再更新，也找不到新数据**
`data/outputs` 里**没有 R07**；R07 的 **8.7 GB** 只在 `runs/R07/`（是全 `data/outputs` 的 1.9 倍）。也就是说"找数据去 `data/outputs`"这条路径对**正在进行的 phase 直接失效**。

**证据 6｜包内的分组口径本身就有四套**

| 包 | 分组键 | 例子 |
|---|---|---|
| `n29/ n134/ n183/ n275/` | **体系尺寸 n** | `n134/LDOS/ldos_n134_d0.050_rDW_sA.txt` |
| `n134_lkcf/` | **尺寸 + 势** | 唯一把势写进名字的目录（好做法） |
| `r03_dw_decay/ r04/ r05_dos_EF/ r06/` | **phase** | `r04/1_x_ldos_waterfall/` |
| `r04/support/` | **目标编号 G1–G9** | `G5_EF_R5/` |

同一棵 4.6 GB 的树里并存四种键，**没有一个是"模型"**。

### 2.2 根因：模型身份根本没有写进数据

对 `runs/` 下全部 **645 个 LDOS 数据点**的 `meta.json` 做字段覆盖统计：

| 字段 | 覆盖 | 后果 |
|---|---:|---|
| `m` / `ts` / `rs` / `selection` / `layer` | 645 / 645（100%） | 口径可查 |
| `rescale` / `rescale_center`（栅格族） | 438 / 645（67.9%） | R03 H1/H1b 与 R04 C2 的 207 个点**不知道自己属于 `auto` 还是 `manual`** |
| `structure`（init/rlxd） | 394 / 645（**61.1%**） | R03 H1/H1b、R04 C2/R6 的 251 个点**不知道自己是 init 还是 rlxd** |
| **`potential`（势函数）** | **0 / 645（0%）** | **`n134`（DRIP）与 `n134`（P4）在数据层面完全不可区分** |

**两个因此真实发生的歧义**：

1. **同名不同势**：`data/outputs/n134/` = R01 的 **DRIP+REBO** 结构产物；`data/outputs/n134_lkcf/` = R02 的 **LCBOP+KC full（P4）**。而 **R03–R07 全部使用后者的结构文件** `data/inputs/rlxd_tbg_n134.data`。目录名 `n134` 单独出现时是**歧义标签**。
2. **同任务两个模型，元数据完全相同**：R07 R6 的 `uniform_mean`（2.662241 eV）与 `uniform_gamma0`（2.7 eV）两个变体，`meta.json` 里都是 `extend_hop_mode: "nn_intra_uniform"`，**没有任何字段记录用的是哪个值**；唯一能区分的是目录前缀 `r6m_`/`r6g_` 和一个派生量 `sum_abs_intra`（866894.8 vs 879190.2）。⇒ **看数据本身认不出模型，只能靠"记得哪个任务"**。

**结论**：数据"按 phase 存"不是随便选的 —— **因为 phase 是唯一能反查模型的索引**。把模型身份写进数据，这个理由就消失了。

**旁证：手工索引已经出现了两次**

- `reports/2026-11_baseline_d060/DATA_MAP.md`（2026-10-29）：一份**按图种/按任务**手写的数据地图，第一句是"数据在哪（帮你找）"。
- `runs/README.md` §3：一份"旧 → 新路径映射"表（92 条重排登记），而且**已经过期**（只到 R06、把 R06 写成"小"，实际 2.3 GB，且没有 R07）。

### 2.3 顺带确认的量化事实

- 645 个 LDOS 点里，`(m, ts, rs)` 组合共 **19 种**，其中 `(16, 8192, 1)` 占 **430 点（66.7%）** —— 口径高度集中，说明"按口径分目录"没有必要，进 metadata 即可。
- 从 `meta.json` 能分出的模型组 **12 个**（含 7 个结构变体：`flat` · `decoupled` · `uniform` · 4 个 `dz`），但其中一组 `n134_P4_None`（251 点）是因为**旧点没有 `structure` 字段**而无法归类 —— 这 251 点只能靠 phase 反查。
- `git ls-files data/` = **27 个文件**，全是 README / manifest / scripts。⇒ 数据本身不在版本控制里，**索引是唯一可检索入口**，而索引目前按 phase 组织。

---

## 三、改进方案

### 3.1 原则：一个检索键 + 三层存储

**一个键**：`model_id`（"什么东西"），而不是时间/phase（"什么时候做的"）。
理由：你找数据时问的永远是「**哪个结构 × 哪个观测量 × 哪个 δ/能量**」，从不是「哪次和导师聊之后做的」。phase 只在复现和记账时才需要 —— 那是**字段**，不是目录。

| 层 | 位置 | 谁写 | 能否改 | 作用 |
|---|---|---|---|---|
| **L0 生产层** | `runs/{PHASE}/{TASK}/data/**`（**现状不动**） | execution | **不可变**（关闭即冻结） | 唯一权威字节 + `sha256` + 复算路径 |
| **L1 模型层** | `data/models/{model_id}/{obs}/{grid}/{select}/**` | **生成器** | 可随时重建 | 按模型检索；**hardlink 指向 L0**，不复制字节 |
| **L2 交付层** | `data/outputs/{PHASE}/`（现状缩水）、`reports/{paper}/` | planning/装配 | 冻结 | 图 + 读数 + manifest；**不再放 raw 副本** |

> L1 与 L2 都是**派生视图**，与 `manifest.json` 同类：**禁止手写**，只由生成器产出（v4.1 §2「派生禁止落盘副本」的例外应为"生成物可落盘，但必须可重建"）。
> **L1 用 hardlink（同一文件系统）而不是 symlink**：`du` 不重复计字节、`ls`/`glob`/`find` 都能直接看到"一个模型有哪些数据"，删掉视图也不影响 L0 —— 这就是"**物理上按模型存放、字节只有一份**"的解法；跨盘时才退化为 symlink（此时 `find` 需 `-L`）。

### 3.2 `model_id` 规格

```
model_id = {n}_{potential}_{protocol}[.{variant}]

n         134 / 101 / 151 / 183 / 275 / 29 / 301
potential DRIP   （REBO2 + DRIP，R01）
          P4     （LCBOP×2 + KC-full 16.0 taper，R02 起）
          P3     （KC-z，n301 用）
protocol  init | rlxd
variant   flat（z 拉平） · decoupled（层间关断） · hopmean / hopgamma0（层内 hop 均匀化）
          · dz{±%}（层间距平移） · 以后新增的变体
```

实例（全部来自现有数据）：

| model_id | 出处任务 | 现状 |
|---|---|---|
| `n134_P4_rlxd` | R03 H1/H1b、R04 C2/R6、R06 R2/R3/R7、R07 R1/R2 | **4 个交付包**（R07 尚未归档） |
| `n134_P4_rlxd.flat` | R07 R4 | 1 个任务 |
| `n134_P4_rlxd.decoupled` | R07 R5（+ `only_layer` 单层探针） | 1 |
| `n134_P4_rlxd.hopmean` / `.hopgamma0` | R07 R6 | **元数据不可区分** |
| `n134_P4_rlxd.dz{±0.085,±0.170}`（现 4 个；r10 后 ±0.340/±0.680 共 6 个） | R07 R8 | 1 个任务 |
| `n134_P4_init` | R06 C1/R1 | 1 |
| `n101_P4_rlxd` / `n151_P4_rlxd` | R06 R4/R5/R7 | 2 |
| `n134_DRIP_rlxd`（+`init`）· `n183_DRIP_rlxd` · `n275_DRIP_rlxd` · `n29_DRIP_rlxd` | R01 | 4 个目录 |
| `n301_P3_rlxd` | R02 T10 参照 / R06 X-4 储备 | 结构输入 |

**必做的元数据补丁（3 个字段，新作业生效、存量按 phase 反查补录）**：

```json
"model_id": "n134_P4_rlxd",
"potential": {"name": "LCBOP+KC-full", "files": ["..."]},
"model_fingerprint": {"num_orb": 217084, "sum_abs_intra": 866894.796, "n_inter": 5951974}
```

`model_fingerprint` 不是装饰：`uniform_mean` 与 baseline 的 `sum_abs_intra` 恰好相同（因为它保 Σt），**只有 `uniform_gamma0` 会变** —— 这正是"指纹抓不住这个变体"的证据，所以 `variant` 必须显式写。

### 3.3 目录与 catalog

```
data/
├── inputs/                          # 现状不动（结构/势）
├── models/                          # L1：生成物，hardlink 到 runs/，不占字节
│   ├── n134_P4_rlxd/
│   │   ├── _model.json              # model_id / 势 / 协议 / 原子数 / fingerprint / 来源
│   │   ├── ldos/
│   │   │   └── m16_ts8192_rs1_manual/          # 口径（栅格族进路径，因为跨族不可比）
│   │   │       ├── dw_p500/d000/ldos.txt -> runs/R04/r04_R6/data/r6_d000_p500/ldos.txt
│   │   │       └── dw_p500/d005/ldos.txt -> …
│   │   └── qe/
│   │       └── fold_m16/21E/d030/… -> runs/R07/r07_R1/data/r1_qe_d030/…
│   ├── n134_P4_rlxd.flat/  …
│   └── n101_P4_rlxd/  …
├── catalog.jsonl                    # 逐 dataset 一行（生成物；唯一检索入口）
├── CATALOG.md                       # 人读视图（按 model_id 分组 + 计数 + 消费者）
└── outputs/                         # L2：交付包（逐步缩为 fig+values+manifest）
```

`catalog.jsonl` 一行（字段即检索维度）：

```json
{"dataset_id":"n134_P4_rlxd/ldos/m16_ts8192_rs1_manual/dw_p500/d030",
 "model_id":"n134_P4_rlxd","observable":"ldos","grid_family":"manual","dE_meV":1.25,
 "select":{"kind":"site","uv":[0.5,0.5],"layer":2},"delta_meV":30,
 "caliber":{"m":16,"ts":8192,"rs":1,"selection":"cross_cell","extend_hop_mode":"nn_intra"},
 "path":"runs/R04/r04_R6/data/r6_d030_p500/ldos.txt","sha256_16":"…","bytes":370127,"rows":16385,
 "produced_by":{"phase":"R04","task":"R6","contract_rev":"r2"},
 "consumers":["R04/R2","R06/R2","R07/R1"],
 "status":"final"}
```

四种查法都成立：

- 按模型：`jq 'select(.model_id=="n134_P4_rlxd")' data/catalog.jsonl`
- 按任务/phase：`jq 'select(.produced_by.task=="R6")'`
- 按消费者（找孤儿 / 找影响面）：`jq 'select(.consumers|index("R07/R1"))'`
- 按口径：`jq 'select(.caliber.m==16 and .grid_family=="manual")'`

**孤儿立刻可见**：`n134_P4_rlxd/dos/…`（R05）的 `consumers` 是空数组 —— 这就是 Phase 文档 §2.3 说的"没有消费者的 phase"，以前只有人脑能发现。

### 3.4 迁移步骤（0 集群，≈1 人-日）

| # | 动作 | 产出 | 风险控制 |
|---|---|---|---|
| 1 | 写 `tools/data/catalog.py`：扫 `runs/*/*/manifest.json` + `meta.json` + `ldos.txt` 头（R01/R02 无 `meta.json`，只能读头） | `data/catalog.jsonl` + `CATALOG.md` | 只读扫描，不改任何 L0 |
| 2 | 建 `data/models/registry.yaml`：`model_id → 势文件 + 结构文件 + fingerprint`；R01/R02 的旧目录在 `LEGACY_MAP.md` 里映射 | 12–18 个 model 的权威表 | **这是唯一需要人判的一张表** |
| 3 | 生成 L1 链接树（hardlink 优先，跨 fs 时 symlink） | `data/models/**` | 先 dry-run 打印将创建的链接数；不删除任何 L0 |
| 4 | 校验：随机 200 个 L1 链接 → `sha256` 与 catalog 一致 | `values/checks_links.json` | 不一致即停 |
| 5 | **删 `data/outputs/*/**/raw/**` 的字节副本**（保留 manifest / README / scripts / fig） | `data/outputs` 4.6 GB → ≈1.0 GB（省 ≈3.6 GB） | **先跑引用组**（v4.1 O-C ①）：全仓 grep 这些路径 → 改指 L1 → 再删 → 再跑一次 |
| 6 | 给 `phase-wrapup` 加一项：关闭时把本 phase 的 dataset 追加进 catalog | 自动 | 与现有八项模板并列 |

> 第 3–5 步不触碰 `runs/`：**生产层永远只有一份**，`sha256` 与 manifest 引用全部保持有效。

### 3.5 为什么不直接 `mv` 成模型目录

| 顾虑 | 说明 |
|---|---|
| **引用会全断** | manifest / REPORT / KNOWN 里写的是 `runs/...` 路径；`raw_manifest.json` 存的是相对包路径 + sha。搬家 = 大面积死链（v4.1 O-C ①） |
| **模型分类本身会变** | R07 的 `flat` 现在叫"变体"，将来可能成为新基线；`decoupled` 可能是"模型"也可能是一次对照。搬一次就得再搬一次 |
| **23 GB 搬动的风险 vs 0 科学收益** | hardlink 已经让"按模型存放"在 `ls`/`glob` 层面成立 |
| **不可变性是当前唯一的防篡改机制** | L0 冻结 + sha 是"读到的就是算出来的"的唯一保证 |

### 3.6 机检（可落到 `tools/checks/`）

| 检查 | 规则 | 反例样本（必须先证明能抓到） |
|---|---|---|
| `DATA_MODEL_ID` | L0 每个 `meta.json` 必须含 `model_id` 且 ∈ registry | 现有 645 个点全部命中（存量豁免，新作业生效） |
| `DATA_MODEL_VARIANT` | `extend_hop_mode` 以 `_uniform`/`_decoupled`/`_flat` 结尾时，必须同时有 `variant` 字段 | **R07 R6 的 `uniform_mean` vs `uniform_gamma0`** |
| `DATA_LINK_INTEGRITY` | L1 每个链接可解析且 sha 一致 | 断链 / 被改过的源文件 |
| `DATA_PACK_NO_RAW` | `data/outputs/*/` 下不得出现 >100 件的 `raw/` 目录 | 现状 r04（**690 件 / 1.69 GB**）与 r06（**637 件 / 1.87 GB**） |
| `DATA_ORPHAN` | `consumers == []` 的 dataset 报 🟡（不阻塞） | R05 的 DOS |

---

## 四、需要 principal 裁决的 2 件事

| # | 决定 | 选项 | 建议 |
|---|---|---|---|
| 1 | 数据是否改为「模型视图 + catalog」 | 三层（L0/L1/L2）/ 只做 catalog 不建视图 / 全搬 | **三层**（搬字节 = 断引用，不推荐） |
| 2 | 是否删除 `data/outputs` 里的 raw 副本 | 删（省 ≈3.6 GB，4.6 → ≈1.0 GB）/ 保留 | **删**（`runs/` 是权威，删前跑引用组） |

---

## 五、附：本文用到的关键数字

| 数字 | 值 |
|---|---|
| `data/` 总量 | 5.2 GB（`inputs` 632 MB + `outputs` 4.6 GB） |
| `runs/` 总量 | 23 GB（R02 9.9 · R04 2.0 · R06 2.3 · R07 8.7） |
| `data/outputs` 各包 | r04 1.9 GB · r06 2.2 GB · n* 483 MB（n134 273 + n134_lkcf 60 + n183 63 + n275 43 + n29 44）· r03 62 MB · r05 11 MB |
| 包内 raw 副本 | r04 690 件 / 1.69 GB · r06 637 件 / 1.87 GB |
| 重复字节 | R03 H1b 54 点 / 20 MB（sha 相同） |
| LDOS 数据点 | 645（`meta.json` 口径） |
| 字段覆盖 | `structure` 61.1% · 栅格族 67.9% · **`potential` 0%** |
| 口径组合 | 19 种；`(16,8192,1)` 占 430 点（66.7%） |
| 进 git 的数据文件 | 27 个（全是 README / manifest / scripts） |
| 可回收空间 | ≈3.6 GB |
