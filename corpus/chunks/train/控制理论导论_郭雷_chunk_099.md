\left\{ \begin{array}{l} \dot {x} _ {3} (t) = u _ {3} (t), \\ y _ {2} (t) = - x _ {3} (t) + x _ {2} (t). \end{array} \right. \tag {1.7.13}
$$

首先，研究子系统(1.7.12)的状态观测器。这是一个二阶系统，它的量测输出是一维的，故增益系数只有两个，设为 $g_{1}$ 和 $g_{2}$ 。这时，系统的观测器方程应为

$$
\left[ \begin{array}{c} \dot {x} _ {1 e} (t) \\ \dot {x} _ {2 e} (t) \end{array} \right] = \left[ \begin{array}{c c} - g _ {1} & \mu \\ - g _ {2} - \mu & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1 e} (t) \\ x _ {2 e} (t) \end{array} \right] + \left[ \begin{array}{c} u _ {1} (t) \\ u _ {2} (t) \end{array} \right] + \left[ \begin{array}{c} g _ {1} \\ g _ {2} \end{array} \right] y _ {1} (t).
$$

现在决定增益常数 $g_{1}$ 和 $g_{2}$ . 观测器的特征多项式为

$$
f (\lambda) = \det {\left[ \begin{array}{l l} \lambda + g _ {1} & - \mu \\ \mu + g _ {2} & \lambda \end{array} \right]} = \lambda^ {2} + g _ {1} \lambda + \mu (\mu + g _ {2}).
$$

如果希望这个观测器的极点为 $\alpha \pm \beta j$ ( $\alpha, \beta > 0$ ), 那么又有

$$f (\lambda) = \lambda^ {2} + 2 \alpha \lambda + \alpha^ {2} + \beta^ {2} = \lambda^ {2} + g _ {1} \lambda + \mu^ {2} + \mu g _ {2}.$$

由此可见，

$$g _ {1} = 2 \alpha , \quad g _ {2} = \frac {1}{\mu} [ (\alpha^ {2} + \beta^ {2}) - \mu^ {2} ].$$

于是子系统 (1.7.12) 的观测器就设计出来了.

然后，研究子系统(1.7.13)的观测器。在这个子系统中， $x_{2}(t)$ 不能量测，今用子系统(1.7.12)的观测器得到的 $x_{2e}(t)$ 代替它。于是子系统(1.7.13)又可写成

$$
\left\{ \begin{array}{l} \dot {x} _ {3} (t) = u _ {3} (t), \\ y _ {2} (t) - x _ {2 e} (t) = - x _ {3} (t), \end{array} \right. \tag {1.7.14}
$$

而相应的子系统的观测器方程为

$$\dot {x} _ {3 e} (t) = - g _ {3} x _ {3 e} (t) + u _ {3} (t) + g _ {3} \left(y _ {2} (t) - x _ {2 e} (t)\right),$$

这里要求 $g_{3} > 0$

将两个子系统的观测器组合在一起得出

$$
\left\{ \begin{array}{l} \dot {x} _ {1 e} (t) = - g _ {1} x _ {1 e} (t) + \mu x _ {2 e} (t) + u _ {1} (t) + g _ {1} y _ {1} (t), \\ \dot {x} _ {2 e} (t) = - (g _ {2} + \mu) x _ {1 e} (t) + u _ {2} (t) + g _ {2} y (t), \\ \dot {x} _ {3 e} (t) = - g _ {3} x _ {3 e} (t) - g _ {3} x _ {2 e} (t) + u _ {3} (t) + g _ {3} y _ {2} (t). \end{array} \right.
$$

今证上述三个方程组成原系统的一个状态观测器。事实上，令

$$e _ {i} (t) = x _ {i e} (t) - x _ {i} (t), \quad i = 1, 2, 3,$$

于是得出

$$
\left[ \begin{array}{c} \dot {e} _ {1} (t) \\ \dot {e} _ {2} (t) \\ \dot {e} _ {3} (t) \end{array} \right] = \left[ \begin{array}{c c c} - g _ {1} & \mu & 0 \\ - (\mu + g _ {2}) & 0 & 0 \\ 0 & - g _ {3} & - g _ {3} \end{array} \right] \left[ \begin{array}{c} e _ {1} (t) \\ e _ {2} (t) \\ e _ {3} (t) \end{array} \right].
$$

显然

$$
\det \left[ \begin{array}{c c c} \lambda + g _ {1} & - \mu & 0 \\ \mu + g _ {2} & \lambda & 0 \\ 0 & g _ {3} & \lambda + g _ {3} \end{array} \right] = (\lambda + g _ {3}) (\lambda^ {2} + g _ {1} \lambda + \mu (\mu + g _ {2})).
$$
