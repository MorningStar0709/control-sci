因为 $g_{3} > 0$ ，并且 $\lambda^2 + g_1\lambda + \mu(\mu + g_2)$ 的零点为 $-\alpha \pm \beta j (\alpha > 0)$ ，所以矩阵

$$
\left[ \begin{array}{c c c} - g _ {1} & \mu & 0 \\ - (\mu + g _ {2}) & 0 & 0 \\ 0 & - g _ {3} & - g _ {3} \end{array} \right]
$$

是稳定的，从而必有

$$\lim _ {t \rightarrow \infty} e _ {i} (t) = 0.$$

这表明组合起来的两个子系统观测器确是原系统的状态观测器.

这样做可以简化问题，便于参数选择。但是必须注意，不是所有系统的观测器都能这样拆成两个子系统分别设计的。

例1.7.1 研究了设计所给系统的状态观测器的问题。这里有一个状态变量就是系统的量测输出，也就是说，这个状态变量是直接可以量测的，为得到系统的状态估计，只要再估计出另一个状态变量就可以了。这样，相应的系统可改写成

$$
\left\{ \begin{array}{l} \dot {x} _ {2} (t) = u (t) + y (t), \\ z (t) = x _ {2} (t). \end{array} \right.
$$

这里 $z(t) = \dot{x}_1(t) - u_1(t) = \dot{y}(t) - u_1(t)$ . 在这个系统中，新的量测变量为 $z(t)$ ，用它可设计出观测器

$$\dot {x} _ {2 e} (t) = - g x _ {2 e} (t) + u _ {2} (t) + y (t) + g z (t).$$

只要 $g > 0$ ，就有 $\lim_{t\to \infty}(x_{2e}(t) - x_2(t)) = 0$ 。将 $z(t)$ 的表达式代到观测器方程中去，得出

$$\dot {x} _ {2 e} (t) = - g x _ {2 e} (t) + \left(u _ {2} (t) - g u _ {1} (t)\right) + y (t) + g \dot {y} (t).$$

在这个观测器方程中，用到了量测数据的导数，这在物理上是不可实现的。为此令

$$w (t) = x _ {2 e} (t) - g y (t),$$

于是

$$\dot {w} (t) = - g w (t) + \left(u _ {2} (t) - g u _ {1} (t)\right) + \left(1 - g ^ {2}\right) y (t).$$

这时系统的状态观测器方程为

$$
\left\{ \begin{array}{l} x _ {1 e} (t) = y (t), \\ x _ {2 e} (t) = w (t) + g y (t), \\ \dot {w} (t) = - g w (t) + (u _ {2} (t) - g u _ {1} (t)) + (1 - g ^ {2}) y (t). \end{array} \right.
$$

这个观测器比原来系统的观测器少了一阶，所以称它为原系统的降阶观测器：就这个例子中所给的系统来说，降阶观测器的阶数不能再降低了，这样的观测器称为极小阶观测器.

下面对一般系统讨论极小阶观测器问题.

已知定常线性系统 (1.6.1). 假设 $\operatorname{rank} C = m$ . 令

$$
\boldsymbol {A} = \left[ \begin{array}{l l} \boldsymbol {A} _ {1 1} & \boldsymbol {A} _ {1 2} \\ \boldsymbol {A} _ {2 1} & \boldsymbol {A} _ {2 2} \end{array} \right], \quad \boldsymbol {B} = \left[ \begin{array}{l} \boldsymbol {B} _ {1} \\ \boldsymbol {B} _ {2} \end{array} \right], \quad \boldsymbol {C} = \left[ \begin{array}{l l} \boldsymbol {C} _ {1} & \boldsymbol {C} _ {2} \end{array} \right],
$$

其中 $A_{11}, A_{22}, B_1, C_1$ 分别为 $m \times m, (n - m) \times (n - m), m \times r, m \times m$ 矩阵，而 $A_{12}, A_{21}, B_2, C_2$ 为相应阶数的矩阵。不失一般性，设 $\operatorname{rank} C_1 = m$ ，还可假设 $C = [I_m - 0]$ 。否则，经坐标变换

$$\overline {{{x}}} = P x,$$

总可以将 $C$ 化成这种形式，这里

$$
\boldsymbol {P} = \left[ \begin{array}{c c} \boldsymbol {C} _ {1} & \boldsymbol {C} _ {2} \\ 0 & \boldsymbol {I} _ {n - m} \end{array} \right].
$$

于是，系统(1.6.1)可写成
