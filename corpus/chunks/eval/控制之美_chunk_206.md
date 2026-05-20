# 10.4.1 系统的能观测性

对于一个线性时不变系统：

$$
\frac {\mathrm{d} \boldsymbol {z} (t)}{\mathrm{d} t} = \boldsymbol {A} \boldsymbol {z} (t) + \boldsymbol {B} \boldsymbol {u} (t) \tag {10.4.1a}
$$

$$
\mathbf {y} (t) = \mathbf {C z} (t) + \mathbf {D u} (t) \tag {10.4.1b}
$$

状态能观测性的定义: 在任意给定的输入 $\boldsymbol{u}(t)$ 下, 根据有限的时间区间 $[t_0, t_1]$ (其中 $t_1$ 有限) 的输入 $\boldsymbol{u}(t)$ 和输出值 $\boldsymbol{y}(t)$ , 可以唯一确定在初始时间 $t_0$ 下的初始状态 $\boldsymbol{z}(t_0)$ , 则称系统在 $t_0$ 时刻是能观测的, 如果在任意初始时间 $t_0$ 下的初始状态 $\boldsymbol{z}(t_0)$ 都能观测, 就称系统的状态是能观测的。

状态能观测性判据：对于 $n$ 维线性时不变系统而言，它的状态能观测的充分必要条件是能观测矩阵

$$
\boldsymbol {O} = \left[ \begin{array}{l l l l l} \boldsymbol {C} & \boldsymbol {C A} & \boldsymbol {C A} ^ {2} & \dots & \boldsymbol {C A} ^ {n - 1} \end{array} \right] ^ {\mathrm{T}} \tag {10.4.2}
$$

的秩为 n，即 $\mathrm{Rank}(\mathbf{O})=n$ 。
