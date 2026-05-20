# (1) 由差分方程建立动态方程

在经典控制理论中离散系统通常用差分方程或脉冲传递函数来描述。单输入-单输出线性定常离散系统差分方程的一般形式为

$$
\begin{array}{l} y (k + n) + a _ {n - 1} y (k + n - 1) + \dots + a _ {1} y (k + 1) + a _ {0} y (k) \\ = b _ {n} u (k + n) + b _ {n - 1} u (k + n - 1) + \dots + b _ {1} u (k + 1) + b _ {0} u (k) \tag {9-64} \\ \end{array}
$$

式中，k 表示 kT 时刻；T 为采样周期； $y(k)$ ， $u(k)$ 分别为 kT 时刻的输出量和输入量； $a_{i}, b_{i} (i = 0, 1, 2, \cdots, n, \text{且 } a_{n} = 1)$ 为表征系统特性的常系数。考虑初始条件为零时的 z 变换关系有

$$\mathcal {L} [ y (k) ] = Y (z), \quad \mathcal {L} [ y (k + i) ] = z ^ {i} Y (z)$$

对式（9-64）两端取 $z$ 变换并加以整理可得

$$
\begin{array}{l} G (z) = \frac {Y (z)}{U (z)} = \frac {b _ {n} z ^ {n} + b _ {n - 1} z ^ {n - 1} + \cdots + b _ {1} z + b _ {0}}{z ^ {n} + a _ {n - 1} z ^ {n - 1} + \cdots + a _ {1} z + a _ {0}} \\ = b _ {n} + \frac {\beta_ {n - 1} z ^ {n - 1} + \cdots + \beta_ {1} z + \beta_ {0}}{z ^ {n} + a _ {n - 1} z ^ {n - 1} + \cdots + a _ {1} z + a _ {0}} = b _ {n} + \frac {N (z)}{D (z)} \tag {9-65} \\ \end{array}
$$

$G(z)$ 称为脉冲传递函数，式(9-65)与式(9-15)在形式上相同，故连续系统动态方程的建立方法可用于离散系统。例如，在 $N(z) / D(z)$ 的串联分解中，引入中间变量 $Q(z)$ 则有

$$z ^ {n} Q (z) + a _ {n - 1} z ^ {n - 1} Q (z) + \dots + a _ {1} z Q (z) + a _ {0} Q (z) = U (z)Y (z) = \beta_ {n - 1} z ^ {n - 1} Q (z) + \dots + \beta_ {1} z Q (z) + \beta_ {0} Q (z)$$

设 $X_{1}(z) = Q(z)$

$$
X _ {2} (z) = z Q (z) = z X _ {1} (z)
\begin{array}{c} \bullet \\ \bullet \\ \bullet \end{array}
X _ {n} (z) = z ^ {n - 1} Q (z) = z X _ {n - 1} (z)
$$

则 $z^{n}Q(z)=-a_{0}X_{1}(z)-a_{1}X_{2}(z)-\cdots-a_{n-1}X_{n}(z)+U(z)$

$$Y (z) = \beta_ {0} X _ {1} (z) + \beta_ {1} X _ {2} (z) + \dots + \beta_ {n - 1} X _ {n} (z)$$

利用 $z$ 反变换关系

$$\mathscr {L} ^ {- 1} \left[ X _ {i} (z) \right] = x _ {i} (k)\mathcal {L} ^ {- 1} \left[ z X _ {i} (z) \right] = x _ {i} (k + 1)$$

可得动态方程为

$$
x _ {1} (k + 1) = x _ {2} (k)x _ {2} (k + 1) = x _ {3} (k)
\begin{array}{c} \bullet \\ \bullet \\ \bullet \end{array}
x _ {n - 1} (k + 1) = x _ {n} (k)x _ {n} (k + 1) = - a _ {0} x _ {1} (k) - a _ {1} x _ {2} (k) - \dots - a _ {n - 1} x _ {n} (k) + u (k)y (k) = \beta_ {0} x _ {1} (k) + \beta_ {1} x _ {2} (k) + \dots + \beta_ {n - 1} x _ {n} (k)
$$

向量-矩阵形式为

$$
\left[ \begin{array}{c} x _ {1} (k + 1) \\ x _ {2} (k + 1) \\ \vdots \\ x _ {n - 1} (k + 1) \\ x _ {n} (k + 1) \end{array} \right] = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & & \vdots \\ 0 & 0 & 0 & \dots & 1 \\ - a _ {0} & - a _ {1} & - a _ {2} & \dots & - a _ {n - 1} \end{array} \right] \left[ \begin{array}{c} x _ {1} (k) \\ x _ {2} (k) \\ \vdots \\ x _ {n - 1} (k) \\ x _ {n} (k) \end{array} \right] + \left[ \begin{array}{c} 0 \\ 0 \\ \vdots \\ 0 \\ 1 \end{array} \right] u (k) \tag {9-66a}
