# Track1 ControlSci Sci-Align — 30 题证据扩展版

> **版本**：v2.0（证据扩展版） | **日期**：2026-05-13
> **赛道**：赛道一（科学数据对齐与跨模态评测赛道）
> **覆盖类型**：text 5 题 + formula 6 题 + image_formula 6 题 + table 4 题 + chart 5 题 + design 4 题
> **数据源**：`benchmark/dataset/core.json`（500 题全量集）+ `corpus/processed/`（MinerU 解析语料）+ `corpus/chunks/`（28,514 条 chunk 级证据）

---

## 案例索引

| # | 覆盖类型 | 维度 | 难度 | 控制子领域 | 题目 ID | 模型来源 | Evidence 路径 |
|:-:|:--------:|:----:|:----:|:-----------|:--------|:---------|:--------------|
| 01 | text | A | L1 | reinforcement_learning | CS-EVO-00071 | deepseek | `corpus/processed/2201.05599_Smart_Magnetic_Microrobots_Learn_to_Swim_with_Deep_Reinforce/` |
| 02 | text | A | L3 | multi_agent | CS-EVO-00746 | minimax | `corpus/processed/2204.07041_Distributed_Optimal_Control_with_Recovered_Robustness_for_Un/` |
| 03 | text | A | L4 | nonlinear | CS-EVO-00939 | mimo | `corpus/processed/2307.08762_Geometric_Extended_State_Observer_on_SE3_with_Fast_Finite_Ti/` |
| 04 | text | A | L4 | robust | CS-EVO-00293 | mimo | `corpus/processed/2204.07041_Distributed_Optimal_Control_with_Recovered_Robustness_for_Un/` |
| 05 | formula | B | L3 | robust | CS-EVO-00638 | deepseek | `corpus/processed/2202.08019_Model_Based_and_Data_Driven_Control_of_Event_and_Self_Trigg/` |
| 06 | formula | C | L2 | classical | CS-EVO-00251 | deepseek | `corpus/processed/CtlBook/` |
| 07 | formula | D | L3 | optimal/mpc | CS-EVO-00270 | deepseek | `corpus/processed/MPC_Control_Rawlings/` |
| 08 | formula | A | L3 | adaptive | CS-EVO-00228 | deepseek | `corpus/processed/2410.16691_Global_Stability_Notions_to_Enhance_the_Rigor_and_Robustness/` |
| 09 | image_formula | C | L4 | modern | CS-EVO-00242 | deepseek | `corpus/processed/2404.01155_Dynamic_Modeling_and_Stability_Analysis_for_Repeated_LVRT_Pr/` |
| 10 | image_formula | C | L2 | mpc | CS-EVO-00663 | deepseek | `corpus/processed/2203.08944_Autonomous_Wheel_Loader_Trajectory_Tracking_Control_Using_LP/` |
| 11 | image_formula | C | L4 | robust | CS-EVO-00241 | deepseek | `corpus/processed/2404.01155_Dynamic_Modeling_and_Stability_Analysis_for_Repeated_LVRT_Pr/` |
| 12 | image_formula | D | L2 | digital/robust | CS-EVO-00356 | minimax | `corpus/processed/2505.13475_Causality_for_Cyber_Physical_Systems/` |
| 13 | table | A | L3 | optimal/multi_agent | CS-EVO-00087 | deepseek | `corpus/processed/2201.05959_Master_Equation_for_Discrete_Time_Stackelberg_Mean_Field_Gam/` |
| 14 | formula | B | L3 | nonlinear/optimal | CS-EVO-00754 | minimax | `corpus/processed/控制理论导论_郭雷/` |
| 15 | table | B | L3 | adaptive | CS-EVO-00362 | deepseek | `corpus/processed/2305.17836_Data_driven_Optimal_Filtering_for_Linear_Systems_with_Unknow/` |
| 16 | chart | A | L4 | classical | CS-EVO-00461 | deepseek | `corpus/processed/Ogata_Modern_Control_5th/` |
| 17 | chart | D | L2 | classical | CS-EVO-00774 | minimax | `corpus/processed/CtlBook/` |
| 18 | chart | C | L2 | classical | CS-EVO-00644 | deepseek | `corpus/processed/线性系统理论_郑大钟/` |
| 19 | design | D | L4 | adaptive | CS-EVO-00450 | deepseek | `corpus/processed/2303.01379_Planning_and_Control_of_Uncertain_Cooperative_Mobile_Manipul/` |
| 20 | design | D | L3 | mpc | CS-EVO-00288 | mimo | `corpus/processed/MPC_Control_Rawlings/` |
| 21 | text | A | L2 | classical/sliding_mode | CS-EVO-00666 | deepseek | `corpus/processed/智能控制/` |
| 22 | formula | A | L3 | event_triggered/multi_agent | CS-EVO-00011 | deepseek | `corpus/processed/2201.02997_Performance_Analysis_of_Event_Triggered_Consensus_Control_fo/` |
| 23 | image_formula | A | L3 | classical/steady_state | CS-EVO-00815 | minimax | `corpus/processed/自动控制原理_胡寿松/` |
| 24 | image_formula | A | L4 | digital/sampled_data | CS-EVO-00377 | deepseek | `corpus/processed/Computer_Controlled_Systems_Astrom/` |
| 25 | table | A | L1 | classical/compensation | CS-EVO-00549 | deepseek | `corpus/processed/Ogata_Modern_Control_5th/` |
| 26 | table | A | L1 | classical/state_space | CS-EVO-00825 | mimo | `corpus/processed/Belanger_Control_Engineering/` |
| 27 | chart | B | L4 | classical/system_id | CS-EVO-00515 | deepseek | `corpus/processed/Dynamic_Systems_Modeling_Simulation_Control/` |
| 28 | chart | A | L3 | classical/performance | CS-EVO-00129 | deepseek | `corpus/processed/2505.13475_Causality_for_Cyber_Physical_Systems/` |
| 29 | design | C | L3 | nonlinear/stability | CS-EVO-00231 | deepseek | `corpus/processed/控制理论导论_郭雷/` |
| 30 | design | C | L2 | nonlinear/parameter_estimation | CS-EVO-00768 | minimax | `corpus/processed/2511.02717_An_unscented_Kalman_filter_method_for_real_time_input_parame/` |

---

## 第一组：概念回溯（Text，4 题）

### Case 01 — 强化学习算法核心控制目标

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-01 |
| **覆盖类型** | text |
| **Input** | 什么是 RUDER_MBOT_RL 算法？请写出其核心控制目标函数。 |
| **Expected behavior** | RUDER_MBOT_RL 是一种基于强化学习的移动机器人控制算法，其核心控制目标函数为 J(π) = E[∑_{t=0}^{T} γ^t r(s_t, a_t)]，其中 π 为策略，γ 为折扣因子，r 为奖励函数。 |
| **System output** | 正确识别算法类型（RL-based control）并输出标准折扣累积奖励目标函数，策略 π 在状态 s_t 下选择动作 a_t 以最大化期望累积奖励。 |
| **Evidence path** | `corpus/processed/2201.05599_Smart_Magnetic_Microrobots_Learn_to_Swim_with_Deep_Reinforce/chunk_047` 中的 RUDER_MBOT_RL 算法定义与目标函数 |
| **Pass criteria** | 正确写出目标函数 J(π) = E[∑γ^t r] 形式；识别 π 为策略、γ 为折扣因子；答案包含 T（时域）或等价表述 |
| **Related score item** | A 维（概念回溯）— 准确回忆算法定义与数学表达式 |
| **Boundary note** | 该算法为特定论文中的命名方法，非通用 RL 算法，不要求区分 on/off-policy；仅考察目标函数的基本形式 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 02 — 多智能体一致性定义

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-02 |
| **覆盖类型** | text |
| **Input** | 什么是多智能体系统的一致性（consensus）？请给出其数学定义，并说明实现一致性所需满足的系统假设条件。 |
| **Expected behavior** | 一致性指多智能体系统中所有智能体的状态在某种协议下趋于一致。数学定义：lim_{t→∞} ||x_i(t) - x_j(t)|| = 0, ∀i,j。假设条件包括：通信拓扑连通（或有向生成树）、系统模型可控/可观、控制协议设计合理。 |
| **System output** | 正确给出极限定义、拓扑连通假设、控制协议需满足的条件。 |
| **Evidence path** | `corpus/processed/2204.07041_Distributed_Optimal_Control_with_Recovered_Robustness_for_Un/chunk_010` |
| **Pass criteria** | 数学定义包含极限形式 lim||x_i - x_j||→0；提及通信拓扑条件；提及控制协议设计 |
| **Related score item** | A 维（概念回溯）— 基础定义与前提条件完整性 |
| **Boundary note** | 不要求区分 leaderless vs leader-follower；不要求证明收敛性；假设条件列出 2 条以上即通过 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 03 — 齐次 Lyapunov 函数定义

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-03 |
| **覆盖类型** | text |
| **Input** | 在非线性系统理论中，什么是齐次 Lyapunov 函数？请写出其定义。 |
| **Expected behavior** | 对于一个齐次连续向量场，齐次 Lyapunov 函数 V(x) 满足：1) V(x) 正定；2) V̇(x) 沿系统轨迹负定；3) V(x) 本身齐次：存在齐次度 d 使得 V(λ^{r1}x1, ..., λ^{rn}xn) = λ^d V(x)，其中 (r1,...,rn) 为向量场的齐次度权重。 |
| **System output** | 完整给出三个条件：正定性、导数负定性、齐次缩放性质。提及 Rosier (1992) 工作背景。 |
| **Evidence path** | `corpus/processed/2307.08762_Geometric_Extended_State_Observer_on_SE3_with_Fast_Finite_Ti/chunk_051` |
| **Pass criteria** | 三个条件全部列出；齐次性给出数学表达式 V(λ^r x) = λ^d V(x) |
| **Related score item** | A 维（概念回溯）— 定义精确性，含权重系数的细节掌握 |
| **Boundary note** | 不要求区分加权齐次与标准齐次；不要求举例说明；权重 (r1,...,rn) 不要求写出具体数值 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 04 — H∞ 范数定义

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-04 |
| **覆盖类型** | text |
| **Input** | 在控制理论中，H∞ 范数是衡量系统鲁棒性的关键指标。请写出传递函数矩阵 G(s) 的 H∞ 范数的数学定义。 |
| **Expected behavior** | ||G||_∞ = sup_{ω∈ℝ} σ_max(G(jω))，其中 σ_max 是 G(jω) 的最大奇异值。该范数量化系统在最坏频率下的最大增益。 |
| **System output** | 正确写出上确界定义，使用最大奇异值 σ_max，定义域为 ω∈ℝ。 |
| **Evidence path** | `corpus/processed/2204.07041_Distributed_Optimal_Control_with_Recovered_Robustness_for_Un/chunk_023` |
| **Pass criteria** | 定义包含 sup、σ_max、G(jω)；解释为最坏情况增益 |
| **Related score item** | A 维（概念回溯）— 鲁棒控制基础概念精确性 |
| **Boundary note** | 不要求区分 SISO/MIMO 下的不同表达；不要求解释 H∞ 控制综合步骤 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

## 第二组：公式推导与计算（Formula，5 题）

### Case 05 — Ξ₀ 矩阵标量表达式计算

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-05 |
| **覆盖类型** | formula |
| **Input** | 设 n=1，所有自由矩阵为单位矩阵：S=1, N1=1, N2=1, R1=1, R2=1, P=1, Ω=1。根据定义计算 Ξ₀ 的具体标量表达式。 |
| **Expected behavior** | 当 n=1 时，L_i 为 1×7 行向量，其第 i 个分块为单位 1，其余为 0。计算各 Π 矩阵：Π₁=[L₃ᵀ, L₄ᵀ, L₂ᵀ-L₃ᵀ, L₅ᵀ+L₂ᵀ-L₃ᵀ]ᵀ (28×1)，同理计算 Π₂、Π₃、Π₄、Π₉、Π₁₀。利用 L_i 正交性化简 ΠᵀΠ 项，得到 Ξ₀ 的标量值。 |
| **System output** | 正确构造分块向量 L_i，推导所有 Π 矩阵表达式，利用正交性化简得出数值结果。 |
| **Evidence path** | `corpus/processed/2202.08019_Model_Based_and_Data_Driven_Control_of_Event_and_Self_Trigg/chunk_015` 中的定理定义与参数说明 |
| **Pass criteria** | 正确构造 L_i 分块向量；所有 Π 矩阵表达式正确；利用正交性质化简 |
| **Related score item** | B 维（多步推理）— 7 步分块矩阵运算的逐步推导 |
| **Boundary note** | 此题涉及事件触发控制的稳定性分析，Ξ₀ 是 LMI 条件中的关键矩阵；n=1 简化了问题但保留了核心推导结构 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 06 — PID 高频极点条件敏感性分析

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-06 |
| **覆盖类型** | formula |
| **Input** | 设计 PID 控制器时通常需要添加高频极点 ρ 使其成为真分式。教材建议 ρ=10×pz_max。若实际最高极点频率 pz_max_actual 是估计值 pz_max_est 的 2 倍，且使用了估计值 ρ=10×pz_max_est，试判断原结论"高频极点不影响系统响应"是否仍成立。 |
| **Expected behavior** | 不成立。原结论成立需 ρ≥10×pz_max，实际 ρ/pz_max_actual=5，不满足 10 倍条件，高频极点影响不可忽略。 |
| **System output** | 正确计算实际倍数为 5，指出 5<10，原结论失效。 |
| **Evidence path** | `corpus/processed/CtlBook/chunk_338` |
| **Pass criteria** | 计算 ρ/pz_max_actual=5；明确指出不满足 10 倍条件 |
| **Related score item** | C 维（条件敏感性）— 参数估计误差对设计结论的影响 |
| **Boundary note** | 这是一个典型的"条件边界"问题，关键不是做精确设计而是识别条件不成立；不要求给出替代设计方案 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 07 — 参数二次规划与显式 MPC

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-07 |
| **覆盖类型** | formula |
| **Input** | 教材中讨论了参数二次规划问题：min_u V(x,u)，其中 V(x,u)=½(x-u)²+u²/2，约束集 Z={(x,u)| u≥1, u+x/2≥2, u+x≥2}。系统动态 x_{k+1}=x_k+u_k。请设计基于该参数二次规划的显式 MPC 控制器，求解反馈控制律 u⁰(x)。 |
| **Expected behavior** | 无约束解 u_uc⁰(x)=x/2。分区域推导：X₁=(-∞,0] 激活约束 u≥2-x；X₂=[0,2] 激活 u≥1；X₃=[2,∞) 激活 u+x/2≥2。每个区域求解 KKT 条件得到分段仿射控制律。 |
| **System output** | 正确推导无约束解 → 识别约束激活区域 → KKT 求解 → 三个区域的分段控制律。 |
| **Evidence path** | `corpus/processed/MPC_Control_Rawlings/chunk_763` |
| **Pass criteria** | 正确给出无约束解 u=x/2；识别至少 2 个约束激活区域；给出每个区域的控制律表达式 |
| **Related score item** | D 维（开放设计）— 参数规划 → 显式 MPC 的完整设计链 |
| **Boundary note** | 此题是显式 MPC 的简化版，实际多参数规划可能涉及高维区域划分；仅考察一步预测情况 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 08 — Lyapunov 函数数学性质

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-08 |
| **覆盖类型** | formula |
| **Input** | 在定理 8 中，为了保证系统的鲁棒自适应设计，Lyapunov 函数 V 需要满足哪些数学性质？请完整列出所有条件。 |
| **Expected behavior** | V∈C¹(ℝⁿ×ℝ)，满足 V(0,z)=0 对所有 z∈ℝ 成立，且 V(ξ,z)>0 对所有 ξ≠0 和 z∈ℝ 成立。 |
| **System output** | 列出三个条件：C¹ 光滑性、原点零值、正定性（对非零 ξ 严格正）。 |
| **Evidence path** | `corpus/processed/2410.16691_Global_Stability_Notions_to_Enhance_the_Rigor_and_Robustness/chunk_035` |
| **Pass criteria** | 至少列出光滑性条件 V∈C¹；原点条件 V(0,z)=0；正定性 V(ξ,z)>0 |
| **Related score item** | A 维（概念回溯）— 定理条件完整性 |
| **Boundary note** | 隐含参数 z 的存在表明该 Lyapunov 函数适用于含参数不确定性的系统；不要求证明该条件的充分必要性 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 14 — HJB 方程非负解验证

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-14 |
| **覆盖类型** | formula |
| **Input** | 考虑非线性系统 ẋ = -x + x³ + w, z = x, f(x) = -x + x³, G(x)=1, h(x)=x, γ₀=2。试构造 J*(x)=px² 的非负解，验证其是否满足 HJB 方程(7.5.27)。 |
| **Expected behavior** | 设 J*(x)=px² (p>0)，代入 HJB 方程：∂J/∂x·f(x) + (1/2γ₀)(∂J/∂x)² + hᵀh = 0。计算结果：∂J/∂x=2px，各项代入得 2px(-x+x³) + (1/4)(2px)² + x² = 0 → 2px⁴ + (1-p)x² = 0。取 p=1 得 2x⁴=0，在 x=0 附近成立，验证 J*(x)=x² 为非负解且系统满足 L₂-增益不等式。 |
| **System output** | 完整代入 HJB 方程 → 化简 → 取 p=1 → 验证非负解存在 → 推断 L₂-增益不等式成立。 |
| **Evidence path** | `corpus/processed/控制理论导论_郭雷/chunk_576` 含 HJB 方程(7.5.27)及参数表 |
| **Pass criteria** | 正确代入 HJB 方程；化简得到 2px⁴+(1-p)x²=0；取 p=1 验证；说明 L₂-增益意义 |
| **Related score item** | B 维（多步推理）— HJB 方程代入 → 化简 → 参数辨识 → 结论推导 |
| **Boundary note** | 高阶项 2px⁴ 在小 x 邻域可忽略，验证了局部 L₂-增益性质；全局验证需额外条件 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

## 第三组：图像公式跨模态对齐（Image-Formula，4 题）

### Case 09 — LVRT 平衡点偏导推导

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-09 |
| **覆盖类型** | image_formula |
| **Input** | 基于教材中的稳定性判据，考虑环境参数 v_G 的变化。假设标称条件下 v_G=v_G0，系统处于平衡点 (x1e0,x2e0) 且满足方程(26)。现 v_G 变化为 v_G0+Δv_G，λ₁ 和 v_LVRT 保持不变，请推导平衡点关于 v_G 的偏导数表达式。 |
| **Expected behavior** | 对(26)第一个方程求偏导得 -1.5R·∂x1e/∂v_G + 1.5ωL·∂x2e/∂v_G = 1。对第二个向量方程求偏导得 [λ₁A₁+(1-λ₁)A₂]·∂xe/∂v_G = 0。若矩阵可逆则 ∂xe/∂v_G=0，代入第一式得矛盾 1=0，说明假设不成立，λ₁ 必须随 v_G 调整。 |
| **System output** | 正确识别矛盾，指出 λ₁ 必须视为 v_G 的函数重新推导。 |
| **Evidence path** | `corpus/processed/2404.01155_Dynamic_Modeling_and_Stability_Analysis_for_Repeated_LVRT_Pr/chunk_022` 包含方程(26)-(27)的完整推导与图 3（LVRT 波形图） |
| **Pass criteria** | 写出两个偏导方程；识别矩阵可逆性假设导致的矛盾；指出 λ₁ 需随 v_G 调整 |
| **Related score item** | C 维（条件敏感性）— 参数变化下平衡点偏移与稳定性条件的满足性检验 |
| **Boundary note** | 方程(26)的具体形式在 chunk 中以 LaTeX 呈现，MinerU 正确提取为结构化公式；图 3 的 LVRT 电压波形与公式跨模态关联 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 10 — 路面摩擦系数对 LPV-MPC 的影响

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-10 |
| **覆盖类型** | image_formula |
| **Input** | 对于自主轮式装载机轨迹跟踪控制，分析路面摩擦系数变化对 LPV-MPC 控制器跟踪性能的影响，并写出考虑摩擦系数变化的车辆动力学模型中的关键参数表达式。 |
| **Expected behavior** | 摩擦系数 μ 变化影响轮胎侧偏刚度 C_f 和 C_r：C_f' = (μ/μ₀)C_f，C_r' = (μ/μ₀)C_r。MPC 状态矩阵 A(ρ) 中与侧偏刚度相关的元素线性依赖于 μ/μ₀，跟踪误差随 μ 偏离 μ₀ 增大。 |
| **System output** | 正确写出侧偏刚度修正公式，识别状态矩阵的线性依赖关系。 |
| **Evidence path** | `corpus/processed/2203.08944_Autonomous_Wheel_Loader_Trajectory_Tracking_Control_Using_LP/chunk_000` 含车辆动力学模型图和 LPV 参数调度说明 |
| **Pass criteria** | 写出 C_f' = (μ/μ₀)C_f 公式；说明 A(ρ) 依赖 μ/μ₀；指出跟踪误差随 μ 偏离增大 |
| **Related score item** | C 维（条件敏感性）— 环境参数变化对模型预测控制性能的影响分析 |
| **Boundary note** | 此题同时涉及公式推导（侧偏刚度修正）和图像信息（车辆动力学模型图），MinerU 从 PDF 中同时提取了公式和图表 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 11 — v_LVRT 变化对稳定性结论的影响

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-11 |
| **覆盖类型** | image_formula |
| **Input** | 在定理 2 中，预先给定 v_LVRT=V₀ 时系统渐近稳定。若 v_LVRT 从 V₀ 变为 V₁（V₁≠V₀），而 μ 和 P 保持不变，请分析原稳定性结论是否必然保持。 |
| **Expected behavior** | 不一定保持。稳定性依赖于方程(26)的可解性。LMI 条件(27)与 v_LVRT 无关，仅需 A₁ᵀP+PA₁+μP≺0 和 A₂ᵀP+PA₂+μP≺0。v_LVRT 变化时，平衡点和 λ₁ 需重新满足(26)，若存在新 λ₁∈[0,1] 和 xe 使(26)成立则仍稳定，否则稳定性丧失。 |
| **System output** | 完整分析了(26)的可解性依赖性，区分了(27)的 LMI 条件（与 v_LVRT 无关）和(26)的平衡点条件（受 v_LVRT 影响）。 |
| **Evidence path** | `corpus/processed/2404.01155_Dynamic_Modeling_and_Stability_Analysis_for_Repeated_LVRT_Pr/chunk_022`（与 Case 09 同源，但考察不同定理条件） |
| **Pass criteria** | 区分(26)和(27)两个条件的作用；指出 LMI 与 v_LVRT 无关；说明关键是可解性而非条件本身 |
| **Related score item** | C 维（条件敏感性）— 参数变化不改变条件结构但改变可解性 |
| **Boundary note** | 该题与 Case 09 共享同一 PDF 来源，但考察不同的定理（定理 2 vs 教材稳定性判据），展示了同一跨模态 chunk 可支撑多角度评测 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 12 — CPS 混合自动机设计

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-12 |
| **覆盖类型** | image_formula |
| **Input** | 考虑自动驾驶车辆纵向速度跟踪控制系统，集成雷达传感器（感知层）、离散数字控制器（计算层）和驱动执行器（执行层），形成 CPS 架构。请基于混合自动机 formalism 设计完整控制方案，满足：稳态速度误差 ≤0.5 m/s (t>5s)、响应时间 t_r≤1.5s、相位裕度 PM≥45°。 |
| **Expected behavior** | 选择混合自动机 H=(Q,X,Init,A,D,E,G,R)，Q={q_acc,q_cruise,q_brake}。采用串级控制：外环 PID 速度环，内环加速度环。参数整定分三步：Ziegler-Nichols 初调 → 相位裕度鲁棒整定 → 内外环带宽分离。 |
| **System output** | 完整给出混合自动机五元组定义、三个离散模式与切换守卫条件、串级控制器结构和参数整定步骤、四类验证指标。 |
| **Evidence path** | `corpus/processed/2505.13475_Causality_for_Cyber_Physical_Systems/chunk_021` 含 CPS 架构示意图、混合自动机定义 |
| **Pass criteria** | 定义混合自动机五元组；至少 2 个离散模式；串级控制结构；参数整定步骤含鲁棒性要求；验证指标覆盖动态/稳态/鲁棒性 |
| **Related score item** | D 维（开放设计）— CPS 混合自动机完整控制方案设计 |
| **Boundary note** | 该题包含了多层信息：车辆动力学微分方程（连续域）、控制器采样与模式切换（离散域）、雷达传感器约束（感知层），MinerU 的跨模态提取保障了三类信息在 chunk 中的完整呈现 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

## 第四组：表格与参数体系（Table，2 题）

### Case 13 — Stackelberg Mean Field Equilibrium 映射

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-13 |
| **覆盖类型** | table |
| **Input** | 请写出 Stackelberg mean field equilibrium 中定义的 BR_t^f 映射的数学表达式。 |
| **Expected behavior** | BR_t^f(π_t, z_{1:t}, a_{1:t-1}^l, x_{1:t}^{f,i}, σ_{t:T}^l) := arg max_{σ^f} E^{σ_{t:T}^l, σ_{t:T}^f, π_t}[∑_{n=t}^T δ^{n-t} R^f(...)]，其中 δ 为折扣因子，R^f 为 follower 奖励函数。 |
| **System output** | 正确写出 BR 映射的数学表达式，包含所有参数：leader 策略 π_t、公共噪声 z_{1:t}、leader 动作历史 a_{1:t-1}^l、follower 状态 x_{1:t}^{f,i}、leader 未来策略 σ_{t:T}^l。 |
| **Evidence path** | `corpus/processed/2201.05959_Master_Equation_for_Discrete_Time_Stackelberg_Mean_Field_Gam/chunk_010` 含 Stackelberg MFE 定义与 BR 映射表 |
| **Pass criteria** | 正确写出 BR_t^f 映射结构；包含 arg max 和期望累积奖励；包含折扣因子 δ |
| **Related score item** | A 维（概念回溯）— 多人博弈与均值场均衡定义 |
| **Boundary note** | 此为离散时间 Stackelberg 博弈的特殊情况，不要求与连续时间版本对比 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 15 — 梯度误差上界数值计算

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-15 |
| **覆盖类型** | table |
| **Input** | 给定梯度误差范数不等式 ||∇J(L)-∇J_T(L)|| ≤ 2[(κ_ξ² + C_L²(κ_ξ²+κ_ω²||H||²))/(1-ρ)]C_L²||G||·||GᵀH||*(T+1)ρ^{T+1} + ...。已知 κ_ξ=1, C_L=2, κ_ω=0.5, ||H||=1, ||G||=1, ||GᵀH||*=1, ρ=0.5。利用 (T+1)ρ^{T+1}≤√(ρ^{T+1})/(1-ρ) 和 tρ^t≤1/(1-ρ)，计算 T=10 时上界数值。 |
| **Expected behavior** | 第一项系数 A₁=96，上界 96×√(0.5¹¹)/(1-0.5) ≈ 96×0.04419 ≈ 4.24。第二项系数 A₂≈153.14，上界 153.14×0.5¹¹/0.5 ≈ 0.15。总上界 4.24+0.15=4.39，保留两位有效数字得 4.4。 |
| **System output** | 逐步计算两项系数和上界放缩，最终得出 4.4。 |
| **Evidence path** | `corpus/processed/2305.17836_Data_driven_Optimal_Filtering_for_Linear_Systems_with_Unknow/chunk_076` 含不等式推导与参数表 |
| **Pass criteria** | 第一项系数计算正确；第二项系数计算正确；上界放缩使用给定不等式；最终结果 4.4 |
| **Related score item** | B 维（多步推理）— 复杂不等式拆解 → 系数计算 → 放缩估计 → 数值汇总 |
| **Boundary note** | 该不等式来自数据驱动最优滤波的收敛性分析，参数均取自教材原文，无需额外假设 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

## 第五组：图表与频域分析（Chart，3 题）

### Case 16 — 映射定理与 Nyquist 稳定判据

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-16 |
| **覆盖类型** | chart |
| **Input** | 对于反馈控制系统，闭环特征函数为 F(s)=1+G(s)H(s)。试写出基于映射定理的系统稳定条件，并用 N 和 P 表示，同时解释 N 和 P 的含义。 |
| **Expected behavior** | 稳定条件 N = -P。P 是开环传递函数 G(s)H(s) 在右半 s 平面的极点数（计入重数）；N 是当 s 沿 Nyquist 围线顺时针绕行一周时 F(s) 在 F(s) 平面上顺时针包围原点的次数。由映射定理 N = Z - P，Z 为 F(s) 在右半 s 平面的零点数（闭环极点数）。稳定需 Z=0，故 N = -P。 |
| **System output** | 正确给出 N=-P，解释 N 为 F(s) 包围原点次数，P 为右半平面开环极点数。 |
| **Evidence path** | `corpus/processed/Ogata_Modern_Control_5th/chunk_455` 含 Nyquist 图例和映射定理推导 |
| **Pass criteria** | 写出 N=-P；解释 N 为 F(s) 顺时针包围原点次数；解释 P 为右半平面开环极点数；提及映射定理 N=Z-P |
| **Related score item** | A 维（概念回溯）— Nyquist 稳定判据的数学基础 |
| **Boundary note** | 此题涉及 Nyquist 图的阅读能力——需要理解 s 平面围线与 F(s) 平面映射之间的几何关系，MinerU 从教材 PDF 中成功提取了 Nyquist 图并保留了图题与正文的对应关系 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 17 — 根轨迹法比例控制器设计

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-17 |
| **覆盖类型** | chart |
| **Input** | 系统开环传递函数 G(s)=10/(s(s+3)(s+6))，设计比例控制器 C(s)=K，使上升时间<0.5s、稳态误差≤5%、相位裕度≥45°。请基于根轨迹的幅值条件和角度条件说明设计过程。 |
| **Expected behavior** | 建模：L(s)=K·10/(s(s+3)(s+6))。选择根轨迹法因其直观显示 K 变化对闭环极点的影响。设计：①确定期望极点区域使 ζ≥0.6、ω_n≥4 rad/s；②在候选极点 s₀ 计算角度贡献 ∑∠(s₀-z_i)-∑∠(s₀-p_i)=180°；③幅值条件 |K·10/∏|s₀-p_i||=1 求 K；④Bode 图验证 PM≥45°。 |
| **System output** | 完整给出建模、方法选择理由、四步设计流程、验证指标（阶跃响应仿真 + 稳态误差计算 + Bode 图验证）。 |
| **Evidence path** | `corpus/processed/CtlBook/chunk_206` 含根轨迹图、幅值/角度条件公式 |
| **Pass criteria** | 正确写出 L(s)=K·10/(s(s+3)(s+6))；使用角度条件和幅值条件；给出 K 的数值设计步骤；包含验证指标 |
| **Related score item** | D 维（开放设计）— 经典控制根轨迹法全过程设计 |
| **Boundary note** | 此题结合了根轨迹图的视觉阅读（极点位置）和公式推导（幅值/角度条件），是典型的"图文共现"评测场景 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 18 — 多项式矩阵的秩计算

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-18 |
| **覆盖类型** | chart |
| **Input** | 给定多项式矩阵 Q(s)=[[s+1,0],[0,s-2]] 和 R(s)=[[s,1],[0,1]]，计算 rank Q(s)R(s)，验证不等式 rank Q(s)R(s) ≤ min(rank Q(s), rank R(s)) 是否严格成立。 |
| **Expected behavior** | Q(s)R(s) = [[s(s+1), s+1],[0, s-2]]。det(Q(s)R(s)) = s(s+1)(s-2) 不恒为零，故 rank=2。rank Q(s)=2，rank R(s)=2，min=2，不等式取等号，非严格。 |
| **System output** | 正确计算矩阵乘积、计算行列式、判断秩、验证不等式。 |
| **Evidence path** | `corpus/processed/线性系统理论_郑大钟/chunk_245` |
| **Pass criteria** | 矩阵乘法正确；行列式计算正确；秩判断正确；不等式验证正确 |
| **Related score item** | C 维（条件敏感性）— 多项式矩阵秩的条件判断 |
| **Boundary note** | 此题中的 s 为多项式变量，非数值计算；考察的是多项式矩阵的代数性质，而非频域分析 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

## 第六组：开放设计（Design，2 题）

### Case 19 — 自适应控制方案完整设计

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-19 |
| **覆盖类型** | design |
| **Input** | 基于教材中的自适应控制框架，设计一个针对具有参数不确定性和未知有界干扰的系统的自适应控制方案，要求系统状态跟踪给定参考信号，稳态误差<0.01，调整时间<2秒。 |
| **Expected behavior** | 建模为严格反馈形式，含不确定参数 θ 和干扰 d。控制器采用反步法，设计虚拟控制律和实际控制律 u，引入自适应律在线估计未知参数和干扰。Lyapunov 函数 V 的设计使其导数负定，参数 K_f, K_v, Γ 根据收敛速度和鲁棒性要求选取。 |
| **System output** | 完整给出：系统建模（严格反馈形式）→ 反步法控制器设计 → 自适应律推导 → Lyapunov 稳定性分析 → 参数选取理由 → 验证指标（跟踪误差指数衰减、稳态误差由辨识精度决定、调整时间由 K_f/K_v 特征值决定）。 |
| **Evidence path** | `corpus/processed/2303.01379_Planning_and_Control_of_Uncertain_Cooperative_Mobile_Manipul/chunk_076` 含自适应控制框架和 Lyapunov 分析 |
| **Pass criteria** | 建模为严格反馈形式；采用反步法或等价方法；设计自适应律；Lyapunov 稳定性证明；给出参数选择依据 |
| **Related score item** | D 维（开放设计）— 自适应控制完整方案 |
| **Boundary note** | 此题为无标准答案的开放设计题，评分基于设计完整性和推理链连贯性而非特定控制律形式 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 20 — 基于 CLF 的 MPC 方案设计

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-20 |
| **覆盖类型** | design |
| **Input** | 设计一个 MPC 方案，用于一个具有全局控制 Lyapunov 函数（CLF）的非线性系统，以实现渐近稳定性。系统有输入约束 |u|≤u_max 和状态约束 |x|≤x_max，要求响应时间<5秒，稳态误差为零。 |
| **Expected behavior** | 建模：x_{k+1}=f(x_k,u_k)，CLF V(x) 满足 V(f(x,u))-V(x) ≤ -l(x,u)。MPC 设计：预测时域 N，控制时域 M≤N，优化问题 min J = ∑_{k=0}^{N-1} l(x_k,u_k) + V_f(x_N)，约束含系统模型、输入/状态约束。终端代价 V_f(x)=V(x) 保证稳定性。参数 Q,R 为正定矩阵，N 根据响应时间/采样时间选择。 |
| **System output** | 给出系统建模 → CLF 性质 → MPC 优化问题形式（目标函数 + 约束）→ 参数选择（Q,R,N） → 稳定性验证（Lyapunov 论证）→ 性能指标（响应时间<5s，稳态误差为零）。 |
| **Evidence path** | `corpus/processed/MPC_Control_Rawlings/chunk_249` 含 CLF 定义与 MPC 稳定性定理 |
| **Pass criteria** | 写出系统模型；利用 CLF 性质；构建 MPC 优化问题（含约束）；说明终端代价保证稳定性；给出参数选择理由 |
| **Related score item** | D 维（开放设计）— MPC 控制器全流程设计 |
| **Boundary note** | CLF 假设降低了 MPC 稳定性分析的复杂度，实际应用中 CLF 的构造本身可能是另一层挑战 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---



---

## 第七组：扩展案例（第 7-10 组，10 题）

### Case 21 — 请写出本控制系统中滑模面s的数学表达式，并说明参数c的作用。...

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-21 |
| **覆盖类型** | text |
| **Input** | 请写出本控制系统中滑模面s的数学表达式，并说明参数c的作用。 |
| **Expected behavior** | 滑模面s的定义为 s = c e + de/dt，其中 e = x₁ - x_d 为位置跟踪误差，de/dt = x₂ - dx_d 为速度跟踪误差，c 为正的常数（本例中 c=15）。c 决定了滑模面的收敛速度，c 越大，误差收敛越快，但可能增大控制输入。 |
| **System output** | 正确给出 s = ce + ė 形式，解释 e 为跟踪误差、c 控制收敛速度。 |
| **Evidence path** | `corpus/processed/智能控制/` — 对应 chunk: 智能控制_chunk_307 |
| **Pass criteria** | 写出 s = ce + ė 形式；说明 e 为位置跟踪误差；说明 c 越大收敛越快 |
| **Related score item** | A 维（概念回溯）— 滑模控制基本定义 |
| **Boundary note** | 不要求推导滑模可达性条件；不要求给出等效控制律 u_eq；仅考察滑模面的定义结构 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 22 — 请写出基于状态的事件触发机制中，触发条件(9)的数学表达式，并说明各符号的含义。...

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-22 |
| **覆盖类型** | formula |
| **Input** | 请写出基于状态的事件触发机制中，触发条件(9)的数学表达式，并说明各符号的含义。 |
| **Expected behavior** | 触发条件为 (e_i(t))² ≥ η_i(∑_{j∈N_i^I} (x_i(t) - x_j(t)))²，其中 0 < η_i < 1，e_i(t) = x_i(t_kⁱ) - x_i(t) 是测量误差，x_i(t) 是代理 i 当前时刻的状态，x_j(t) 是邻居代理 j 的当前状态，N_i^I 是代理 i 的邻居集。 |
| **System output** | 正确写出触发条件不等式形式，解释 e_i(t) 为测量误差、η_i 为阈值参数、N_i^I 为邻居集。 |
| **Evidence path** | `corpus/processed/2201.02997_Performance_Analysis_of_Event_Triggered_Consensus_Control_fo/` — 对应 chunk: 2201.02997_Performance_Analysis_of_Event_Triggered_Consensus_Control_fo_chunk_010 |
| **Pass criteria** | 写出平方不等式形式；解释 e_i(t) 为测量误差；解释 η_i 的取值范围 (0,1) |
| **Related score item** | A 维（概念回溯）— 事件触发机制核心条件 |
| **Boundary note** | 不要求区分 CS-ETM 和 S-ETM 的差异；不要求证明 Zeno 行为排除；η_i 的取值可以是一个统一常量而非每个代理不同 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 23 — 在转子绕线机控制系统中，已知系统为 I 型系统。请写出系统对单位斜坡输入响应的稳态误差表达式，并给出...

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-23 |
| **覆盖类型** | image_formula |
| **Input** | 在转子绕线机控制系统中，已知系统为 I 型系统。请写出系统对单位斜坡输入响应的稳态误差表达式，并给出速度误差系数 K_v 的定义及其与稳态误差的关系。 |
| **Expected behavior** | 系统对单位斜坡输入响应的稳态误差表达式为 e(∞) = 1/K_v。速度误差系数 K_v 的定义式为 K_v = lim_{s→0} sG(s)，其中 G(s) 为开环传递函数。稳态误差与 K_v 成反比：要使稳态误差小于 10%，需满足 K_v ≥ 10。 |
| **System output** | 正确写出 e(∞) = 1/K_v；给出 K_v 定义为 lim sG(s)；说明反比关系。 |
| **Evidence path** | `corpus/processed/自动控制原理_胡寿松/` — 对应 chunk: 自动控制原理_胡寿松_chunk_368 |
| **Pass criteria** | 写出 e(∞) = 1/K_v；给出 K_v 定义；说明 K_v 越大误差越小 |
| **Related score item** | A 维（概念回溯）— 稳态误差与系统型别的关系 |
| **Boundary note** | 该题关联转子绕线机控制系统原理图（Chunk 中嵌有 6 张电路/系统图），需跨模态理解系统型别；不要求区分单位斜坡与加速度输入的差异 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 24 — 请写出采样保持电路的微分方程（式 7.24），并解释为什么它是一个线性时变系统。...

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-24 |
| **覆盖类型** | image_formula |
| **Input** | 请写出采样保持电路的微分方程（式 7.24），并解释为什么它是一个线性时变系统。 |
| **Expected behavior** | 微分方程为 C·dy(t)/dt = (u(t) - y(t))/R · m(t)，其中 m(t) 是调制函数，在开关闭合时为 1，断开时为 0。该方程是线性的，但因 m(t) 随时间变化，系数 m(t)/R 和输入项 u(t)·m(t)/R 均依赖于时间，故系统是线性时变的。 |
| **System output** | 正确写出微分方程，指出 m(t) 的时变性导致系统为 LTV。 |
| **Evidence path** | `corpus/processed/Computer_Controlled_Systems_Astrom/` — 对应 chunk: Computer_Controlled_Systems_Astrom_chunk_447 |
| **Pass criteria** | 写出含 m(t) 的微分方程；指出 m(t) 随时间变化；判定为 LTV 并说明原因 |
| **Related score item** | A 维（概念回溯）— 采样保持的数学模型与 LTV 性质 |
| **Boundary note** | 该题涉及采样保持电路图（Chunk 含 2 张电路原理图），需要理解 m(t) 作为开关调制函数的行为；不要求求解微分方程 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 25 — 请写出超前补偿器（lead compensator）的传递函数标准形式，并说明参数 α 和 T 的取...

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-25 |
| **覆盖类型** | table |
| **Input** | 请写出超前补偿器（lead compensator）的传递函数标准形式，并说明参数 α 和 T 的取值范围与物理意义。 |
| **Expected behavior** | 超前补偿器的传递函数标准形式为 G_c(s) = K_c (s + 1/T)/(s + 1/(αT))，其中 0 < α < 1，T > 0。参数 α 决定补偿器的最大相位超前量 φ_max = arcsin((1-α)/(1+α))，T 与零点位置有关。参数 K_c 为补偿器增益，用于保证系统稳态精度。 |
| **System output** | 正确写出传递函数标准形式；说明 α ∈ (0,1)；说明 α 与最大相位超前的单调关系。 |
| **Evidence path** | `corpus/processed/Ogata_Modern_Control_5th/` — 对应 chunk: Ogata_Modern_Control_5th_chunk_332 |
| **Pass criteria** | 写出 G_c(s) = K_c(s+1/T)/(s+1/(αT))；说明 0<α<1；说明 φ_max 与 α 的关系 |
| **Related score item** | A 维（概念回溯）— 超前补偿器的参数体系 |
| **Boundary note** | 该题关联超前补偿器的 Bode 图（Chunk 含 4 张幅频/相频曲线图）；不要求推导相位超前量的计算公式 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 26 — 根据定理 7.2，状态反馈控制系统的可控性与开环系统的可控性之间存在什么关系？请用一句话精确陈述该定...

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-26 |
| **覆盖类型** | table |
| **Input** | 根据定理 7.2，状态反馈控制系统的可控性与开环系统的可控性之间存在什么关系？请用一句话精确陈述该定理。 |
| **Expected behavior** | 一个由状态反馈控制的系统，当且仅当其开环系统是可控的时，该闭环系统才是可控的。 |
| **System output** | 精确复述定理：状态反馈不改变系统的可控性。 |
| **Evidence path** | `corpus/processed/Belanger_Control_Engineering/` — 对应 chunk: Belanger_Control_Engineering_chunk_375 |
| **Pass criteria** | 精确表述"当且仅当"关系；说明状态反馈不改变可控性 |
| **Related score item** | A 维（概念回溯）— 状态反馈与可控性的关系定理 |
| **Boundary note** | 不要求证明该定理；不要求区分可控性与可稳性；该定理仅适用于线性时不变系统 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 27 — 根据表中滑阀对 12N 阶跃力（施加于 t=0.02s）的响应数据，估算该二阶系统的阻尼比 ζ 和无...

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-27 |
| **覆盖类型** | chart |
| **Input** | 根据表中滑阀对 12N 阶跃力（施加于 t=0.02s）的响应数据，估算该二阶系统的阻尼比 ζ 和无阻尼自然频率 ω_n。响应数据：稳态值 1.700，峰值 2.000，峰值时间距阶跃施加 0.01s。 |
| **Expected behavior** | 超调量 M_P = (2.000 - 1.700)/1.700 = 0.1765。由 M_P = e^{-ζπ/√(1-ζ²)} 得 ln(0.1765) = -ζπ/√(1-ζ²)，解得 ζ ≈ 0.5（精确 0.503）。峰值时间 t_p = 0.03 - 0.02 = 0.01s，由 t_p = π/(ω_n√(1-ζ²)) 得 ω_n = π/(t_p√(1-ζ²)) ≈ 363 rad/s。 |
| **System output** | 正确计算超调量 M_P = 0.1765；通过 M_P 反推 ζ ≈ 0.5；通过 t_p 和 ζ 计算 ω_n ≈ 363 rad/s。 |
| **Evidence path** | `corpus/processed/Dynamic_Systems_Modeling_Simulation_Control/` — 对应 chunk: Dynamic_Systems_Modeling_Simulation_Control_chunk_292 |
| **Pass criteria** | M_P 计算正确；ζ 推导正确（≈0.5）；ω_n 推导正确（≈363 rad/s） |
| **Related score item** | B 维（多步推理）— 从阶跃响应数据反推系统参数 |
| **Boundary note** | 该题关联滑阀响应数据表（Chunk 含 2 张响应曲线图），需要从图表中读取峰值和峰值时间；阻尼比计算结果在一定精度范围内（0.45-0.55）均可接受 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 28 — 请写出控制系统性能指标——时间乘绝对误差积分（ITAE）的数学表达式，并说明各符号的含义。...

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-28 |
| **覆盖类型** | chart |
| **Input** | 请写出控制系统性能指标——时间乘绝对误差积分（ITAE）的数学表达式，并说明各符号的含义。 |
| **Expected behavior** | ITAE = ∫₀^∞ t·|e(t)| dt，其中 t 为时间变量，e(t) = r(t) - y(t) 为设定点 r(t) 与过程变量 y(t) 之间的偏差。ITAE 对后期误差赋予较大权重，因此其最优系统超调量小、振荡衰减快。 |
| **System output** | 正确写出 ITAE 积分表达式；解释 e(t) 为跟踪误差；说明 t 的权重作用。 |
| **Evidence path** | `corpus/processed/2505.13475_Causality_for_Cyber_Physical_Systems/` — 对应 chunk: 2505.13475_Causality_for_Cyber_Physical_Systems_chunk_065 |
| **Pass criteria** | 写出 ITAE = ∫t|e|dt 形式；说明 e(t) 为误差信号；解释时间加权意义 |
| **Related score item** | A 维（概念回溯）— 性能指标定义与特征 |
| **Boundary note** | 该题关联 CPS 架构示意图（Chunk 含 2 张系统架构图），ITAE 是该系统中的性能评估指标之一；不要求比较 ITAE 与 IAE/ISE 的差异 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 29 — 给定方程 ẍ + ẋ³ + f(x) = 0，其中 f(x) 满足 x·f(x) > 0（x ≠ 0...

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-29 |
| **覆盖类型** | design |
| **Input** | 给定方程 ẍ + ẋ³ + f(x) = 0，其中 f(x) 满足 x·f(x) > 0（x ≠ 0）且 f(0)=0，已知该系统的零解是渐近稳定的。若将 f(x) 改为 f(x) = -x，其他条件不变，试分析此时零解的稳定性是否仍保持？并解释原因。 |
| **Expected behavior** | 不保持。原系统选 V = ½ẋ² + ∫₀ˣ f(s)ds 为正定 Lyapunov 函数，V̇ = -ẋ⁴ ≤ 0，通过不变集原理得渐近稳定。当 f(x) = -x 时，方程变为 ẍ + ẋ³ - x = 0，在原点附近线性化为 ẍ - x = 0，特征根 s = ±1，有正实部特征根，故原点不稳定。 |
| **System output** | 正确识别条件变化导致稳定性丧失；用 Lyapunov 直接法和线性化两种方法分析。 |
| **Evidence path** | `corpus/processed/控制理论导论_郭雷/` — 对应 chunk: 控制理论导论_郭雷_chunk_179 |
| **Pass criteria** | 识别 f(x) 符号变化导致系统性质改变；使用 Lyapunov 或线性化方法分析；得出"不保持→不稳定"的正确结论 |
| **Related score item** | C 维（条件敏感性）— 非线性项符号变化对稳定性的根本影响 |
| **Boundary note** | 该题来自控制理论导论教材的 Lyapunov 稳定性章节；两种分析方法（Lyapunov 法和线性化法）均可，不要求同时使用 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |

---

### Case 30 — 在非线性 2-DOF 系统的参数估计问题中，对比表 1（有位移测量）和图 5 描述的结果（无位移测量...

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | T1-30 |
| **覆盖类型** | design |
| **Input** | 在非线性 2-DOF 系统的参数估计问题中，对比表 1（有位移测量）和图 5 描述的结果（无位移测量），分析参数 k₂ 的估计方法对测量条件变化的敏感性。当真实刚度系数 k₂ = 3.0 时，有位移测量时 k₂ 估计值稳定在 3.0，无位移测量时估计值收敛至约 4.4~4.5。请判断：在无位移测量条件下，基于观测器的参数估计方法是否能准确识别 k₂？并说明敏感性来源。 |
| **Expected behavior** | 在无位移测量条件下，基于观测器的参数估计方法无法准确识别 k₂，产生了约 47%~50% 的稳态估计误差。敏感性来源：参数估计依赖系统的可观测性条件。当位移测量可用时，状态观测器可精确重构系统位移和速度，进而通过逆动力学准确估计等效刚度系数。当位移测量缺失时，观测器仅依赖力/加速度等间接信息重构状态，导致状态重构误差传播至参数辨识环节，使 k₂ 估计值偏离真实值。 |
| **System output** | 正确判断"无法准确识别"；解释可观测性变化导致的状态重构误差传播机制。 |
| **Evidence path** | `corpus/processed/2511.02717_An_unscented_Kalman_filter_method_for_real_time_input_parame/` — 对应 chunk: 2511.02717_An_unscented_Kalman_filter_method_for_real_time_input_parame_chunk_023 |
| **Pass criteria** | 判断"无法准确识别"；说明可观测性条件变化；解释误差传播路径 |
| **Related score item** | C 维（条件敏感性）— 测量条件对参数估计精度的根本性影响 |
| **Boundary note** | 该题关联表 1（有位移测量结果）和图 5（无位移测量结果），Chunk 含 14 张图表；不需要理解 UKF 的完整原理，仅需关注可观测性条件变化的影响 |
| **Quality checks** | ✅ 字段完整性 | ✅ Evidence 可追溯 | ✅ Reasoning chain 完整性 |


---


## 扩展后统计（30 题）

### 类型分布

| 类型 | 数量 | 占比 | 对应 Case |
|:-----|:----:|:----:|:----------|
| text（概念回溯） | 5 | 17% | 01-04, 21 |
| formula（公式推导/计算） | 6 | 20% | 05-08, 14, 22 |
| image_formula（图像公式跨模态） | 6 | 20% | 09-12, 23-24 |
| table（表格/参数体系） | 4 | 13% | 13, 15, 25-26 |
| chart（图表/频域分析） | 5 | 17% | 16-18, 27-28 |
| design（开放设计） | 4 | 13% | 19-20, 29-30 |

### 维度分布

| 维度 | 数量 | 占比 |
|:----:|:----:|:----:|
| A（概念回溯） | 14 | 47% |
| B（多步推理） | 4 | 13% |
| C（条件敏感性） | 7 | 23% |
| D（开放设计） | 5 | 17% |

### 难度分布

| 难度 | 数量 | 占比 |
|:----:|:----:|:----:|
| L1 | 3 | 10% |
| L2 | 7 | 23% |
| L3 | 12 | 40% |
| L4 | 8 | 27% |

### 模型来源分布

| 模型来源 | 数量 | 占比 |
|:--------:|:----:|:----:|
| deepseek | 20 | 67% |
| minimax | 6 | 20% |
| mimo | 4 | 13% |

### 控制子领域覆盖

| 子领域 | 数量 | 占比 |
|:------|:----:|:----:|
| classical | 8 | 27% |
| robust | 5 | 17% |
| optimal/mpc | 5 | 17% |
| nonlinear | 6 | 20% |
| adaptive | 3 | 10% |
| multi_agent | 3 | 10% |
| digital/modern | 3 | 10% |
| reinforcement_learning | 2 | 7% |
| other（system_id/compensation/steady_state） | 3 | 10% |

### 三个检查项统计

| 检查项 | 通过数 | 通过率 |
|:------|:------:|:------:|
| 字段完整性检查 | 30/30 | 100% |
| Evidence 可追溯 | 30/30 | 100% |
| Reasoning chain 完整性 | 30/30 | 100% |

------

## 数据来源清单

所有 30 题的 Input 和 Expected behavior 均来自 `benchmark/dataset/core.json`（500 题核心评测集），Evidence path 指向 `corpus/processed/` 下对应的 MinerU 解析目录和 `corpus/chunks/` 下的 chunk 文件。验证方式：

```bash
# 验证 30 题均存在于 core.json
conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/dataset/core.json')); target=['CS-EVO-00071','CS-EVO-00746','CS-EVO-00939','CS-EVO-00293','CS-EVO-00638','CS-EVO-00251','CS-EVO-00270','CS-EVO-00242','CS-EVO-00663','CS-EVO-00461','CS-EVO-00774','CS-EVO-00356','CS-EVO-00228','CS-EVO-00754','CS-EVO-00241','CS-EVO-00450','CS-EVO-00087','CS-EVO-00288','CS-EVO-00362','CS-EVO-00644','CS-EVO-00666','CS-EVO-00011','CS-EVO-00815','CS-EVO-00377','CS-EVO-00549','CS-EVO-00825','CS-EVO-00515','CS-EVO-00129','CS-EVO-00231','CS-EVO-00768']; ids=[q['id'] for q in d['questions']]; found=[i for i in target if i in ids]; print(f'Found {len(found)}/30')"

# 验证 evidence chunk 文件存在
conda run -n myenv python "scripts/validate_t1_chunks.py"
```

*本样例包所有数据均基于真实评测题目和 MinerU 解析结果，每个 case 均可独立验证。数据可追溯性详见 `docs/submissions/shared/DATA-TRACE.md`。*
