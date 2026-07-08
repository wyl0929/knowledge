<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-27 23:46:30
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-27 23:46:34
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/chebyshev_precision/USER_BRIEF.md
 * @Description  :
-->
<!--
Field: 切比雪夫迭代浮点精度问题
Parent: tbplas_conductivity (Kubo-Bastin 电导率)
Mode: subfield_onboarding
Domain archetype: science_technical
Created date: 2026-06-27
-->

# USER BRIEF / 本次需求说明

Last updated: 2026-06-27

## 这份文件的作用

这里保存用户对本子方向 field pack 的特殊要求。生成或更新本包中任何主体文档前都必须先读取本文件。

## 用户原始需求

> 切比雪夫迭代中的精度问题

## 当前有效要求

- 系统化记录 Kubo-Bastin 双重求和中 Chebyshev 迭代导致的浮点精度问题的完整根因分析（Phase A–M）
- 明确噪声源定位（C++ KPM Chebyshev 迭代层）、放大机制（Γ 矩阵线性增长）、收敛行为（条件收敛）
- 区分已排除假说与已确认机制，标注证据强度
- 给出实用窗口（M ≤ 2560）和修复路径优先级
- 连接到已有的 gamma_mu_sim 数值验证项目

## 内容侧重点

- 重点展开：Phase A–M 诊断链的完整逻辑（9 假说排除 → Γ·μ 随机游走 → 噪声源定位）
- 简略处理：Kubo-Bastin 公式本身的推导（见父级 `02_kubo_bastin_deep_dive.md`）
- 暂时不需要涉及：新材料的 QHE 计算、实验对比

## 写作与呈现偏好

- 语言：中文为主，关键术语保留英文
- 深度：研究级，面向已熟悉 KPM/Kubo-Bastin 的研究者
- 公式：需要精确公式和标度关系
- 图表：引用 gamma_mu_sim 项目的数值验证结果

## 与父方向的继承关系

- 继承的父方向要求：来自 `tbplas_conductivity/` 的 Kubo-Bastin 方法论
- 本子方向新增要求：聚焦浮点精度的数值分析层面
- 本子方向覆盖要求：无

## 修改记录

| 日期 | 修改内容 | 来源 |
|---|---|---|
| 2026-06-27 | 初始化子方向 USER_BRIEF | subfield_onboarding 触发 |
