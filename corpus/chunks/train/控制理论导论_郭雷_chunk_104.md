为保证由上述方程给定的系统成为一个观测器，只要 $g_{1} > 0$ 即可， $g_{2}$ 可任意选取。为了简单起见，取 $g_{2} = 0$ ，于是得出

$$
\left\{ \begin{array}{l} \overline {{{x}}} _ {2 e} (t) = z _ {c} (t) + g _ {1} y _ {1} (t), \\ \dot {z} _ {c} (t) = - \mu g _ {1} z _ {c} (t) - g _ {1} u _ {1} (t) + u _ {3} (t) - \mu g _ {1} ^ {2} y _ {1} (t) - g _ {1} \mu y _ {2} (t), \end{array} \right. \tag {1.7.24}
$$

这就是系统 (1.7.21) 的极小阶观测器方程。将它代回原系统有

$$
\left[ \begin{array}{l} x _ {1 e} (t) \\ x _ {2 e} (t) \\ x _ {3 e} (t) \end{array} \right] = \left[ \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{l} y _ {1} (t) \\ y _ {2} (t) \\ \overline {{x}} _ {2 e} (t) \end{array} \right],
$$

即

$$
\left\{ \begin{array}{l} x _ {1 e} = y _ {1} (t), \\ x _ {2 e} = g _ {1} y _ {1} (t) + y _ {2} (t) + z _ {c} (t), \\ x _ {3 e} = g _ {1} y _ {1} (t) + z _ {c} (t), \end{array} \right.
$$

其中 $z_{c}(t)$ 满足方程(1.7.24)， $x_{1e}(t), x_{2e}(t)$ 和 $x_{3e}(t)$ 分别是 $x_{1}(t), x_{2}(t)$ 和 $x_{3}(t)$ 的渐近估计状态变量.

按照极小阶观测器的设计方法所得到的观测器系统是一阶的，这比分成两个子系统单独设计还要简单.
