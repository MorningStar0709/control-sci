$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = f (t) + b u; \\ y = x _ {1} \end{array} \right. \left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = f \left(x _ {1}, x _ {2}\right) + b u; \\ y = x _ {1} \end{array} \right.

\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = f (x _ {1}, x _ {2}, t, w (t)) + b u \\ y = x _ {1} \end{array} \right.
$$

的状态和被扩张的状态是没有什么区别的。实际上，在这里不需要假定函数 $(x_{1},x_{2},t,w(t))$ 是连续的还是不连续的，是已知的还是未知的，只要它在过程进程中的实时作用量 $a(t)=f(x_{1}(t),x_{2}(t),t,w(t))$ 是有界的，并参数b已知，我们总可以选择适当的参数 $\beta_{01},\beta_{02},\beta_{03}$ ，使得扩张状态观测器(4.3.5)都能很好地实时估计对象的状态 $x_{1}(t),x_{2}(t)$ 和被扩张的状态 $x_{3}(t)$ 。因此扩张状态观测器(4.3.5)是独立于描述对象传递关系的函数f的具体形式的。

如果我们假定作用于系统的加加速度 $\dot{x}_3(t) = w(t)$ 是常值 $\dot{x}_3(t) = w_0$ ，那么系统(4.3.4）与系统(4.3.5）的误差方程为

$$
\left\{ \begin{array}{l l} \dot {e} _ {1} = e _ {2} - \beta_ {0 1} e _ {1}, & e _ {1} = z _ {1} - y \\ \dot {e} _ {2} = e _ {3} - \beta_ {0 2} | e _ {1} | ^ {\frac {1}{2}} \text {sign} (e _ {1}), & e _ {2} = z _ {2} - x _ {2} \\ \dot {e} _ {3} = w _ {0} - \beta_ {0 3} | e _ {1} | ^ {\frac {1}{4}} \text {sign} (e _ {1}), & e _ {3} = z _ {3} - x _ {3} \end{array} \right. \tag {4.3.10}
$$

当这个系统进入稳态时,方程右端全收敛于零

$$
\left\{ \begin{array}{l} e _ {2} - \beta_ {0 1} e _ {1} = 0, \\ e _ {3} - \beta_ {0 2} | e _ {1} | ^ {\frac {1}{2}} \operatorname{sign} (e _ {1}) = 0 \\ w _ {0} - \beta_ {0 3} | e _ {1} | ^ {\frac {1}{4}} \operatorname{sign} (e _ {1}) = 0 \end{array} \right. \tag {4.3.11}
$$

因此误差系统的稳态误差为

$$\left| e _ {1} \right| = \left(\frac {w _ {0}}{\beta_ {0 3}}\right) ^ {4}, \left| e _ {2} \right| = \beta_ {0 1} \left(\frac {w _ {0}}{\beta_ {0 3}}\right) ^ {4}, \left| e _ {3} \right| = \beta_ {0 2} \left(\frac {w _ {0}}{\beta_ {0 3}}\right) ^ {2} \tag {4.3.12}$$

只要 $\beta_{03}$ 足够大于 $w_{0}$ ，这些估计误差都会足够小。

扩张状态观测器(4.3.5)中的 $z_{3}(t)$ 能够很好地跟踪开环系统加速度的实时作用量 $a(t)=f(x_{1}(t),x_{2}(t),t,w(t))$ 的根本原因，是只要系统满足能观测性条件，那么不管加速度是什么形式，只要它是在起作用，那么其作用必定会反映在系统的输出上，就有可能从系统输出信息中提炼出其作用量。扩张状态观测器(4.3.5)就是从系统输出中提炼出系统加速度的实时作用量 $a(t)=f(x_{1}(t),x_{2}(t),t,w(t))$ 的一种具体办法。有了这个被扩张的状态 $x_{3}(t)$ 的估计值 $z_{3}(t)$ ，只要参数b已知，控制量可以取成

$$u = u _ {0} - \frac {z _ {3} (t)}{b} \quad \text {或} \quad u = \frac {u _ {0} - z _ {3} (t)}{b} \tag {4.3.13}$$

即控制量中补偿被扩张的状态 $x_{3}(t)$ 的估计 $z_{3}(t)$ ，就能使对象变成

$$
\left\{ \begin{array}{l} x _ {1} = x _ {2} \\ \dot {x} _ {2} = f (x _ {1}, x _ {2}) + b \left(u _ {0} - \frac {z _ {3} (t)}{b}\right) \Rightarrow \\ y = x _ {1} \end{array} \right.
