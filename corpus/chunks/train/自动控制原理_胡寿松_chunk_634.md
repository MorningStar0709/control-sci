# 2. 可观测性

可观测性表征了状态可由输出完全反映的性能,所以应同时考虑系统的状态方程和输出方程

$$\dot {\boldsymbol {x}} (t) = \boldsymbol {A} (t) \boldsymbol {x} (t) + \boldsymbol {B} (t) \boldsymbol {u} (t), \quad t \in T, \tag {9-77a}\mathbf {y} (t) = \mathbf {C} (t) \mathbf {x} (t) + \mathbf {D} (t) \mathbf {u} (t), \quad \mathbf {x} \left(t _ {0}\right) = \mathbf {x} _ {0} \tag {9-77b}$$

其中， $A(t)$ ， $B(t)$ ， $C(t)$ 和 $D(t)$ 分别为 $(n \times n)$ ， $(n \times p)$ ， $(q \times n)$ 和 $(q \times p)$ 的满足状态方程解的存在唯一性条件的时变矩阵。式(9-77a) 状态方程的解为

$$\boldsymbol {x} (t) = \boldsymbol {\Phi} (t, t _ {0}) \boldsymbol {x} _ {0} + \int_ {t _ {0}} ^ {T} \boldsymbol {\Phi} (t, \tau) \boldsymbol {B} (\tau) \boldsymbol {u} (\tau) d \tau \tag {9-78}$$

其中 $\Phi(t,t_{0})$ 为系统的状态转移矩阵。将式(9-78)代入式(9-77b)输出方程，可得输出响应为

$$\mathbf {y} (t) = \boldsymbol {C} (t) \boldsymbol {\Phi} (t, t _ {0}) \boldsymbol {x} _ {0} + \boldsymbol {C} (t) \int_ {t _ {0}} ^ {\mathrm{T}} \boldsymbol {\Phi} (t, \tau) \boldsymbol {B} (\tau) \boldsymbol {u} (\tau) \mathrm{d} \tau + \boldsymbol {D} (t) \boldsymbol {u} (t) \tag {9-79}$$

在研究可观测性问题时, 输出 y 和输入 u 均假定为已知, 只有初始状态 $x_{0}$ 是未知的。因此, 若定义

$$\mathbf {y} (t) \triangleq \mathbf {y} (t) - \mathbf {C} (t) \int_ {t _ {0}} ^ {\mathrm{T}} \boldsymbol {\Phi} (t, \tau) \boldsymbol {B} (\tau) \mathbf {u} (\tau) \mathrm{d} \tau - \boldsymbol {D} (t) \mathbf {u} (t)$$

则式(9-79)可写为

$$\mathbf {y} (t) = \boldsymbol {C} (t) \boldsymbol {\Phi} \left(t, t _ {0}\right) \boldsymbol {x} _ {0} \tag {9-80}$$

这表明可观测性即是 $x_0$ 可由 $\mathbf{y}$ 完全估计的性能。由于 $\bar{\mathbf{y}}$ 和 $x_0$ 可取任意值，所以这又等价于研究 $\pmb{u} = \pmb{0}$ 时由 $\pmb{y}$ 来估计 $x_0$ 的可能性，即研究零输入方程

$$\dot {\boldsymbol {x}} (t) = \boldsymbol {A} (t) \boldsymbol {x} (t), \quad \boldsymbol {x} \left(t _ {0}\right) = \boldsymbol {x} _ {0}, \quad t _ {0}, t \in T _ {t} \tag {9-81a}\mathbf {y} (t) = \mathbf {C} (t) \mathbf {x} (t) \tag {9-81b}$$

的可观测性。式(9-79)成为

$$\mathbf {y} (t) = \mathbf {C} (t) \boldsymbol {\Phi} (t, t _ {0}) \mathbf {x} _ {0} \tag {9-82}$$

下面基于式(9-81)给出系统可观测性的有关定义。

系统完全可观测 对于式(9-81)所示线性时变系统,如果取定初始时刻 $t_0 \in T_t$ ,存在一个有限时刻 $t_1 \in T_t, t_1 > t_0$ ,对于所有 $t \in [t_0, t_1]$ ,系统的输出 $y(t)$ 能唯一确定状态向量的初值 $x(t_0)$ ,则称系统在 $[t_0, t_1]$ 内是完全可观测的,简称系统可观测。如果对于一切 $t_1 > t_0$ 系统都是可观测的,则称系统在 $[t_0, \infty)$ 内完全可观测。

系统不可观测 对于式(9-81)所示线性时变系统,如果取定初始时刻 $t_0 \in T_t$ ,存在一个有限时刻 $t_1 \in T_t, t_1 > t_0$ ,对于所有 $t \in [t_0, t_1]$ ,系统的输出 $y(t)$ 不能唯一确定所有状态的初值 $x_i(t_0), i = 1, 2, \cdots, n$ ,即至少有一个状态的初值不能被 $y(t)$ 确定,则称系统在时间区间 $[t_0, t_1]$ 内是不完全可观测的,简称系统不可观测。
