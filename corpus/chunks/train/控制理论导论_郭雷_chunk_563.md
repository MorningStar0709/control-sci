$$
\begin{array}{l} J [ u ^ {*}, \bar {v} ] \leqslant J [ u ^ {*}, v ^ {*} ] = J ^ {*} (x _ {0}, t) \\ = \int_ {0} ^ {t} l (x ^ {*} (s), u ^ {*} (s), v ^ {*} (s)) d s + J ^ {*} (x ^ {*} (t), t). \\ \end{array}
$$

于是从不等式 (7.4.36) 不难得到

$$\int_ {t} ^ {t + \Delta t} l (\bar {x} (s), u ^ {*} (s), \bar {v} (s)) \mathrm{d} s + J ^ {*} (x _ {1} ^ {*} (t + \Delta t), t + \Delta t) - J ^ {*} (x ^ {*} (t), t) \leqslant 0.$$

显然存在 $s_1 \in (t, t + \Delta t)$ , 使 $x_1^*(t + \Delta t) = x^*(t) + f(\bar{x}(s_1), u^*(s_1), \bar{v})\Delta t$ , 代入以上不等式得到

$$
\begin{array}{l} \int_ {t} ^ {t + \Delta t} l (\bar {x} (s), u ^ {*} (s), \bar {v}) d s + J ^ {*} (x ^ {*} (t) + f (\bar {x} (s _ {1}), u ^ {*} (s _ {1}), \bar {v}) \Delta t, t + \Delta t) \\ - J ^ {*} (x ^ {*} (t), t) \leqslant 0. \tag {7.4.37} \\ \end{array}
$$

当 $\Delta t$ 充分小时，利用连续性可得

$$\int_ {t} ^ {t + \Delta t} l (\bar {x} (s), u ^ {*} (s), \bar {v}) \mathrm{d} s = l (x (s ^ {\prime}), u ^ {*} (s ^ {\prime}), \bar {v}) \Delta t,$$

其中 $s' \in (t, t + \Delta t)$ . 由于 $J^{*}(x, t) \in C^{1}$ , 我们有

$$
\begin{array}{l} J ^ {*} \left(x ^ {*} (t) + f (\bar {x} \left(s _ {1}\right), u ^ {*} \left(s _ {1}\right), \bar {v}) \Delta t, t + \Delta t\right) - J ^ {*} \left(x ^ {*} (t), t\right) \\ = \frac {\partial J ^ {*} (x ^ {*} (t) + \theta f (\bar {x} (s _ {1}) , u ^ {*} (s _ {1}) , \bar {v}) \Delta t)}{\partial x} \cdot f (\bar {x} (s _ {1}), u ^ {*} (s _ {1}), \bar {v}) \\ + \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial t} \Delta t + o (\Delta t) \\ \end{array}
$$

其中 $\theta=\mathrm{diag}\left\{\theta_{1},\theta_{2},\cdots,\theta_{n}\right\},0<\theta_{i}<1,i=1,2,\cdots,n.$

注意当 $\Delta t \to 0$ 时， $s_1 \to t, s' \to t, u^*(s_1) \to u^*(t), u^*(s') \to u^*(t)$ ，从而利用 $\frac{\partial J^*(x,t)}{\partial x}$ 的连续性，在不等式 (7.4.37) 两端让 $\Delta t \to 0$ 取极限得到

$$l (x ^ {*} (t), u ^ {*} (t), \bar {v}) + \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x} f (x ^ {*} (t), u ^ {*} (t), \bar {v}) + \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial t} \leqslant 0.$$

特别地，有

$$\max _ {v \in \mathbf {V} _ {r _ {2}}} \left\{l (x ^ {*} (t), u ^ {*} (t), v) + \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x} f (x ^ {*} (t), u ^ {*} (t), v) + \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial t} \right\} \leqslant 0.$$

显然， $\forall t\in \Omega (0,t_f;(u^*,v^*))$ 成立

$$\frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial t} + \min _ {u \in \mathbf {U} _ {r _ {1}}} \max _ {v \in \mathbf {V} _ {r _ {2}}} \left\{\frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x} f (x ^ {*} (t), u, v) + l (x ^ {*} (t), u, v) \right\} \leqslant 0. \tag {7.4.38}$$
