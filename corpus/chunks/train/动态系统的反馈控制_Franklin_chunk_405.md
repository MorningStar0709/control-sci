# 例 7.6 状态变量形式的软盘驱动器

对例 2.4 的微分方程，试求它的状态变量形式，其中输出为 $\theta_{2}$ 。

解答。定义状态矢量为

$$
\boldsymbol {x} = \left[ \begin{array}{l l l l} \theta_ {1} & \dot {\theta} _ {1} & \theta_ {2} & \dot {\theta} _ {2} \end{array} \right] ^ {\mathrm{T}}
$$

然后，对 $\ddot{\theta}_{1}$ 和 $\ddot{\theta}_{2}$ 求解式(2.17)和式(2.18)，写成更明显的状态变量形式，求解矩阵为

$$
\mathbf {A} = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ - \frac {k}{I _ {1}} & - \frac {b}{I _ {1}} & \frac {k}{I _ {1}} & \frac {b}{I _ {1}} \\ 0 & 0 & 0 & 1 \\ \frac {k}{I _ {2}} & \frac {b}{I _ {2}} & - \frac {k}{I _ {2}} & - \frac {b}{I _ {2}} \end{array} \right]

\begin{array}{l} \boldsymbol {B} = \left[ \begin{array}{c} 0 \\ \frac {1}{I _ {1}} \\ 0 \\ 0 \end{array} \right] \\ \boldsymbol {C} = \left[ \begin{array}{c c c c} 0 & 0 & 1 & 0 \end{array} \right] \\ D = 0 \end{array}
$$

当微分方程包含输入 u 的导数时，处理的难度就会增加。7.4 节将介绍处理这种情况的方法。
