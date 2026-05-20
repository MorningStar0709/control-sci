$$J ^ {*} (x ^ {*} (t) + \Delta x (t), t + \Delta t) - J ^ {*} (x ^ {*} (t), t) + \int_ {t} ^ {t + \Delta t} l (x (s), v) \mathrm{d} s \geqslant 0.$$

利用 $l(x,u)$ 的连续性和 $J^{*}(x,t)$ 的可微性知， $\forall v\in \mathbb{U}_r$ 有

$$\frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial t} \Delta t + \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x} \Delta x (t) + l (x ^ {*} (t), v) \Delta t + o (\Delta t) \geqslant 0.$$

将式 (7.1.59) 右端代入上式并除以 $\Delta t$ 后得到

$$\frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial t} + \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x} f (x ^ {*} (t), v) + l (x ^ {*} (t), v) + o (1) \geqslant 0.$$

在上式中令 $\Delta t \to 0$ , 可知 $\forall t \in \Omega(t_0, t_f; u^*)$ , 有

$$\frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial t} + \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x} f (x ^ {*} (t), v) + l (x ^ {*} (t), v) \geqslant 0, \quad \forall v \in \mathbb {U} _ {r}. \tag {7.1.60}$$

联合等式 (7.1.57) 和不等式 (7.1.60) 可知， $\forall t \in \Omega(t_0, t_f; u^*)$ ，有

$$
\begin{array}{l} \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial t} + \min _ {v \in U _ {r}} \left\{\frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x} f (x ^ {*} (t), v) + l (x ^ {*} (t), v) \right\} \\ = \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial t} + \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x} - f (x ^ {*} (t), u ^ {*} (t)) + l (x ^ {*} (t), u ^ {*} (t)) = 0, \tag {7.1.61} \\ \end{array}
$$

并且

$$J ^ {*} (0, t _ {f} ^ {*}) = 0. \tag {7.1.62}$$

由于 $J^{*}(x,t)$ 的可微性，并且 $\forall \Delta t_f\neq 0$ ，有 $J(0,t_f^* +\Delta t_f) = 0,$ 可知

$$\frac {\partial J ^ {*} (0 , t _ {f} ^ {*})}{\partial t _ {f}} = 0. \tag {7.1.63}$$

通常称

$$
\left\{ \begin{array}{l} \frac {\partial J}{\partial t} + \min _ {u \in U _ {r}} \left\{\frac {\partial J}{\partial x} f (x, u) + l (x, u) \right\} = 0, \\ J (0, t _ {f}) = 0 \end{array} \right. \tag {7.1.64}
$$

为所述带边值条件的连续过程的Hamilton-Jacobi-Bellman(HJB)方程，简称Bellman方程.

由此可见式 (7.1.52), (7.1.53) 和 (7.1.54) 的最优过程 $(x^{*}(t), u^{*}(t))$ 和 $t$ 时刻以 $x^{*}(t)$ 为初态的最优指标值 $J^{*}(x^{*}(t), t)$ 满足带边值的 Bellman 方程 (7.1.64).

注7.1.4 当 $x(t_f)$ 自由时，可以证明式(7.1.52)，(7.1.54)的最优过程 $(x^{*}(t), u^{*}(t))$ 和 $t$ 时刻以 $x^{*}(t)$ 为初态的最优指标值 $J^{*}(x^{*}(t), t)$ 满足带边值条件的Bellman方程

$$
\left\{ \begin{array}{l} \frac {\partial J}{\partial t} + \min _ {u \in \mathbf {U} _ {r}} \left\{\frac {\partial J}{\partial x} f (x, u) + l (x, u) \right\} = 0, \\ J (x (t _ {f}), t _ {f}) = 0. \end{array} \right.
$$

注7.1.5 当性能指标(7.1.54)中含有非积分项 $k(x(t_f))$ 时，有如下Bellman方程：
