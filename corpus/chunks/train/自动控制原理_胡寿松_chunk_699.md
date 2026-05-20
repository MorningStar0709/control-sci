# 4. 分离特性

当用全维状态观测器提供的状态估值 x 代替真实状态 x 来实现状态反馈时,为保持系统的期望特征值,其状态反馈阵 K 是否需要重新设计? 当观测器被引入系统以后,状态反馈系统部分是否会改变已经设计好的观测器极点配置,其观测器输出反馈阵 H 是否需要重新设计?为此需要对引入观测器的状态反馈系统作进一步分析。整个系统的结构图如图 9-26 所示,是一个 2n 维的复合系统,其中

$$\boldsymbol {u} = \boldsymbol {v} - \boldsymbol {K} \boldsymbol {x} \tag {9-237}$$

状态反馈子系统动态方程为

$$\dot {x} = A x + B u = A x - B K \dot {x} + B v, \quad y = C x \tag {9-238}$$

全维状态观测器子系统动态方程为

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} \boldsymbol {u} - \boldsymbol {H} (\boldsymbol {y} - \boldsymbol {y}) = (\boldsymbol {A} - \boldsymbol {B} \boldsymbol {K} - \boldsymbol {H} \boldsymbol {C}) \boldsymbol {x} + \boldsymbol {H} \boldsymbol {C} \boldsymbol {x} + \boldsymbol {B} \boldsymbol {v} \tag {9-239}$$

故复合系统动态方程为

$$
\left[ \begin{array}{l} \dot {\boldsymbol {x}} \\ \dot {\boldsymbol {x}} \end{array} \right] = \left[ \begin{array}{c c} \boldsymbol {A} & - \boldsymbol {B K} \\ \boldsymbol {H C} & \boldsymbol {A} - \boldsymbol {B K} - \boldsymbol {H C} \end{array} \right] \left[ \begin{array}{l} \boldsymbol {x} \\ \boldsymbol {x} \end{array} \right] + \left[ \begin{array}{l} \boldsymbol {B} \\ \boldsymbol {B} \end{array} \right] \boldsymbol {v} \tag {9-240a}

\mathbf {y} = \left[ \begin{array}{l l} \mathbf {C} & \mathbf {0} \end{array} \right] \left[ \begin{array}{l} \mathbf {x} \\ \mathbf {x} \end{array} \right] \tag {9-240b}
$$

在复合系统动态方程中，不用状态估值x，而用状态误差 $(x-x)$ ，将会使分析研究更加直观方便。

由式(9-238)和式(9-239)可得

$$\dot {\boldsymbol {x}} - \dot {\boldsymbol {x}} = (\boldsymbol {A} - \boldsymbol {H C}) (\boldsymbol {x} - \boldsymbol {x}) \tag {9-241}$$

该式与 $u, v$ 无关，即 $(x - x)$ 是不可控的。不管施加什么样的控制信号，只要 $(A - HC)$ 全部特征值都具有负实部，状态误差总会衰减到零，这正是所希望的，是状态观测器所具有的重要性质。对式(9-240)引入非奇异线性变换

$$
\left[ \begin{array}{l} \boldsymbol {x} \\ \hat {\boldsymbol {x}} \end{array} \right] = \left[ \begin{array}{c c} \boldsymbol {I} _ {n} & \boldsymbol {0} \\ \boldsymbol {I} _ {n} & - \boldsymbol {I} _ {n} \end{array} \right] \left[ \begin{array}{l} \boldsymbol {x} \\ \boldsymbol {x} - \hat {\boldsymbol {x}} \end{array} \right] \tag {9-242}
$$

则有 $\begin{bmatrix} \dot{x}\\ \dot{x} -\dot{x} \end{bmatrix} = \begin{bmatrix} A - BK & BK\\ 0 & A - HC \end{bmatrix}\begin{bmatrix} x\\ x - \dot{x} \end{bmatrix} + \begin{bmatrix} B\\ 0 \end{bmatrix} v$ (9-243a)
