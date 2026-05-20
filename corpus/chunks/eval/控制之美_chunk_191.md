# 10.2.2 系统能控性的定义与判据

线性时不变系统的状态空间方程一般形式为

$$
\frac {\mathrm{d} z (t)}{\mathrm{d} t} = A z (t) + B u (t) \tag {10.2.2a}
$$

$$
\mathbf {y} (t) = \mathbf {C z} (t) + \mathbf {D u} (t) \tag {10.2.2b}
$$

状态能控性定义: 对于系统(式(10.2.2))而言, 如果存在着输入 $u(t)$ , 可以在有限的时间区间 $[t_0, t_1]$ (其中 $t_1$ 有限) 内, 将系统的状态变量从初始状态 $z(t_0)$ 转移到终端状态 $z(t_1)$ , 那么就称状态 $z(t_0)$ 是能控的状态。如果在任意的初始时间 $t_0$ 下的初始状态 $z(t_0)$

都能控,就称系统的状态是能控的。需要指出,如果系统的状态 $z(t)$ 能控,根据式(10.2.2b),系统的输出 $y(t)$ 也一定能控。

状态能控性判据：对于 $n$ 维线性时不变系统（式(10.2.2)）而言，它的状态能控的充分必要条件是能控矩阵

$$
\boldsymbol {C} _ {\circ} = \left[ \begin{array}{l l l l l} \boldsymbol {B} & \boldsymbol {A B} & \boldsymbol {A} ^ {2} \boldsymbol {B} & \dots & \boldsymbol {A} ^ {n - 1} \boldsymbol {B} \end{array} \right] \tag {10.2.3}
$$

的秩为 n，即 $\mathrm{Rank}(C_{0})=n$ 。
