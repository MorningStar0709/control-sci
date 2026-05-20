# 习题 7.3

7.3.1 对于一阶系统

$$
\left\{ \begin{array}{l l} \dot {x} = - x + u, & x \in \mathbb {R}, u \in \mathbb {R}, \\ x (0) = x _ {0}, \end{array} \right.
$$

和性能指标

$$J [ u ] = \frac {1}{2} \int_ {0} ^ {2} [ x ^ {2} (t) + u ^ {2} (t) ] \mathrm{d} t.$$

试求出最优控制，最优轨线和最优性能指标值.

7.3.2 考察线性定常系统

$$
\left\{ \begin{array}{l} \dot {x} = A x + B u, \\ x (0) = x _ {0}, \end{array} \right.
$$

和性能指标

$$J [ u ] = \frac {1}{2} x ^ {\mathrm{T}} (t _ {f}) x (t _ {f}) + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} u ^ {\mathrm{T}} (t) u (t) \mathrm{d} t,$$

其中 $x \in \mathbb{R}^n, u \in \mathbb{R}^r, A \in \mathbb{R}^{n \times n}, B \in \mathbb{R}^{n \times r}, t_f (> t_0)$ 给定．假设 $(A, B)$ 完全能控．试证明该系统使 $J[u]$ 取极小的控制存在唯一，并求出其最优控制综合函数的形式.

7.3.3 对二阶系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} + \sqrt {2} u _ {1}, \\ \dot {x} _ {2} = \sqrt {2} u _ {2}, \end{array} \right.
$$

和性能指标

$$
J [ u ] = \frac {1}{2} \int_ {0} ^ {\infty} \left(\left[ x _ {1} (t), x _ {2} (t) \right] \left[ \begin{array}{l l} 2 & 0 \\ 0 & 2 \end{array} \right] \left[ \begin{array}{l} x _ {1} (t) \\ x _ {2} (t) \end{array} \right] + \left[ u _ {1} (t), u _ {2} (t) \right] \left[ \begin{array}{l} u _ {1} (t) \\ u _ {2} (t) \end{array} \right]\right) d t,
$$

试求出该系统的最优调节器并讨论最优闭环系统的渐近稳定性.
