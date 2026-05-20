$$\boldsymbol {M} (t _ {1}, t _ {0}) \boldsymbol {x} _ {0} = \int_ {t _ {0}} ^ {t _ {1}} \boldsymbol {\Phi} ^ {\mathrm{T}} (t, t _ {0}) \boldsymbol {C} ^ {\mathrm{T}} (t) y (t) \mathrm{d} t, \tag {1.3.12}$$

其中 $x_0$ 是系统在 $t_0$ 时刻的状态。假设对任意 $t_1 > t_0, M(t_1, t_0)$ 都是奇异的，那么由式 (1.3.12) 知，对任意固定的 $t_1 > t_0$ ，利用时间间隔 $[t_0, t_1]$ 上的量测 $y(t)$ ，都不能唯一决定系统在 $t_0$ 时刻的状态 $x_0$ , 而这与系统在 $t_0$ 时刻完全能观测矛盾. 因此, 至少存在某时刻 $t_1$ , 使得 $M(t_1, t_0)$ 是非奇异的, 因而它是正定的.

矩阵 $M(t_{1}, t_{0})$ 称为系统 $(A(t), B(t), C(t))$ 的能观测性矩阵.

从系统的能控性矩阵 $W(t_{1}, t_{0})$ 和能观测性矩阵 $M(t_{1}, t_{0})$ 的结构来看，它们在形式上有某些类似之处。因此，系统的能控性和能观测性之间应该有某种联系，这种联系就是对偶原理。能控性、能观测性和对偶原理的概念是卡尔曼 (Kalman) 提出的。为了讨论对偶原理，首先引入系统 $(A(t), B(t), C(t))$ 的对偶系统

$$
\left\{ \begin{array}{l} \dot {x} _ {\mathrm{d}} (t) = - \boldsymbol {A} ^ {\mathrm{T}} (t) x _ {\mathrm{d}} (t) + \boldsymbol {C} ^ {\mathrm{T}} (t) v (t), \\ z (t) = \boldsymbol {B} ^ {\mathrm{T}} (t) x _ {\mathrm{d}} (t). \end{array} \right. \tag {1.3.13}
$$

其中 $x_{\mathrm{d}}(t)$ 是对偶系统 $(-A^{\mathrm{T}}(t), C^{\mathrm{T}}(t), B^{\mathrm{T}}(t))$ 的维状态变量，也叫做系统 $(A(t), B(t), C(t))$ 的状态变量 $x(t)$ 的协态变量， $v(t)$ 是控制输入变量， $z(t)$ 是量测输出变量。下面的定理就是对偶原理。

定理 1.3.5 系统 $(A(t), B(t), C(t))$ 在 $t_{0}$ 时刻完全能控的充要条件是它的对偶系统 $(-A^{\mathrm{T}}(t), C^{\mathrm{T}}(t), B^{\mathrm{T}}(t))$ 在 $t_{0}$ 时刻完全能观测。系统 $(A(t), B(t), C(t))$ 在 $t_{0}$ 时刻完全能观测的充要条件是它的对偶系统 $(-A^{\mathrm{T}}(t), C^{\mathrm{T}}(t), B^{\mathrm{T}}(t))$ 在 $t_{0}$ 时刻完全能控。

证明 首先令 $\Psi(t, t_0)$ 为对偶系统 $(-A^{\mathrm{T}}(t), C^{\mathrm{T}}(t), B^{\mathrm{T}}(t))$ 的状态转移矩阵，那么依定义有

$$\dot {\boldsymbol {\Psi}} (t, t _ {0}) = - \boldsymbol {A} ^ {\mathrm{T}} (t) \boldsymbol {\Psi} (t, t _ {0}), \quad \boldsymbol {\Psi} (t _ {0}, t _ {0}) = \boldsymbol {I} _ {n}. \tag {1.3.14}$$

现说明 $\Psi(t, t_0)$ 与系统 $(A(t), B(t), C(t))$ 的状态转移矩阵 $\Phi(t, t_0)$ 之间的关系。研究矩阵 $\Psi(t_0, t)$ 所满足的微分方程。由于 $\Psi^{\mathrm{T}}(t_0, t) \Psi^{\mathrm{T}}(t, t_0) = I_n$ ，两边对 $t$ 求导得

$$\dot {\boldsymbol {\Psi}} ^ {\mathrm{T}} (t _ {0}, t) \boldsymbol {\Psi} ^ {\mathrm{T}} (t, t _ {0}) + \boldsymbol {\Psi} ^ {\mathrm{T}} (t _ {0}, t) \dot {\boldsymbol {\Psi}} ^ {\mathrm{T}} (t, t _ {0}) = 0.$$

将式 (1.3.14) 代入上式得

$$\dot {\boldsymbol {\Psi}} ^ {T} (t _ {0}, t) = \boldsymbol {A} (t) \boldsymbol {\Psi} ^ {T} (t _ {0}, t).$$

注意到

$$\boldsymbol {\Psi} ^ {T} (t _ {0}, t _ {0}) = \boldsymbol {I} _ {n},$$

由常微分方程解的唯一性定理可知，
