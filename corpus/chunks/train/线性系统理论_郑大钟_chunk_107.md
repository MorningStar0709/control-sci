$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} t & 1 & 0 \\ 0 & 2 t & 0 \\ 0 & 0 & t ^ {2} + t \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 1 \\ 1 \end{array} \right] u, \quad J = [ 0, 2 ], t _ {0} = 0. 5
$$

通过计算,求出

$$
M _ {0} (t) = B (t) = \left[ \begin{array}{l} 0 \\ 1 \\ 1 \end{array} \right]

M _ {1} (t) = - A (t) M _ {0} (t) + \frac {d}{d t} M _ {0} (t) = \left[ \begin{array}{c} - 1 \\ - 2 t \\ - t ^ {2} - t \end{array} \right]

M _ {2} (t) = - A (t) M _ {1} (t) + \frac {d}{d t} M _ {1} (t) = \left[ \begin{array}{c} 3 t \\ 4 t ^ {2} - 2 \\ (t ^ {2} + t) ^ {2} - 2 t - 1 \end{array} \right]
$$

因为 $[M_0(t): M_1(t): M_2(t)]$ 对 $t = 1$ 的秩为3，所以系统在时刻 $t_0 = 0.5$ 是完全能控的。
