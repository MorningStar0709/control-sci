$$H (x, u, v, \psi , t) \stackrel {\text { def }} {=} - l (x, u, v, t) + \psi^ {\mathrm{T}} f (x, u, v, t).$$

依 $H_{1}(x,u,v^{*}(t),\psi_{1},t)$ 和 $H_{2}(x,u^{*}(t),v,\psi_{2},t)$ 的定义，从方程(7.4.20)和(7.4.24)及相应的终端条件知

$$
\left\{ \begin{array}{l} \dot {\psi_ {1}} ^ {\mathrm{T}} (t) = - \psi_ {1} ^ {\mathrm{T}} (t) \frac {\partial f (x ^ {*} (t) , u ^ {*} (t) , v ^ {*} (t) , t)}{\partial x} + \frac {\partial l (x ^ {*} (t) , u ^ {*} (t) , v ^ {*} (t) , t)}{\partial x}, \\ \dot {\psi_ {2}} ^ {\mathrm{T}} (t) = - \psi_ {2} ^ {\mathrm{T}} (t) \frac {\partial f (x ^ {*} (t) , u ^ {*} (t) , v ^ {*} (t) , t)}{\partial x} + \frac {\partial l (x ^ {*} (t) , u ^ {*} (t) , v ^ {*} (t) , t)}{\partial x}, \\ \psi_ {1} ^ {\mathrm{T}} (t _ {f}) = - \frac {\partial k (x ^ {*} (t _ {f}) , t _ {f})}{\partial x} - \mu_ {1} ^ {\mathrm{T}} \frac {\partial g (x ^ {*} (t _ {f}) , t _ {f})}{\partial x}, \\ \psi_ {2} ^ {\mathrm{T}} (t _ {f}) = - \frac {\partial k (x ^ {*} (t _ {f}) , t _ {f})}{\partial x} - \mu_ {2} ^ {\mathrm{T}} \frac {\partial g (x ^ {*} (t _ {f}) , t _ {f})}{\partial x}. \end{array} \right.
$$

注意到， $\mu_1, \mu_2$ 皆是通过 $g(x^*(t_f), t_f) = 0$ 确定的。由此可知 $\mu_1 = \mu_2$ 。根据线性微分方程终值问题解的唯一性可得

$$\psi_ {1} (t) = \psi_ {2} (t), \quad \forall t \in [ t _ {0}, t _ {f} ].$$

现取 $\psi(t) \equiv \psi_1(t) (\equiv \psi_2(t))$ . 于是从 $H(x, u, v, \psi, t)$ , $H_1(x, u, v^*(t), \psi_1, t)$ 和 $H_2(x, u^*(t), v, \psi_2, t)$ 的定义即知, $\forall t \in \Omega(t_0, t_f; (u^*, v^*))$ , 有

$$
\left\{ \begin{array}{l} H (x ^ {*} (t), u ^ {*} (t), v ^ {*} (t), \psi (t), t) = H _ {1} (x ^ {*} (t), u ^ {*} (t), v ^ {*} (t), \psi_ {1} (t), t) \\ \qquad \qquad \qquad = H _ {2} (x ^ {*} (t), u ^ {*} (t), v ^ {*} (t), \psi_ {2} (t), t), \\ H (x ^ {*} (t), u, v ^ {*} (t), \psi (t), t) = H _ {1} (x ^ {*} (t), u, v ^ {*} (t), \psi_ {1} (t), t), \\ H (x ^ {*} (t), u ^ {*} (t), v, \psi (t), t) = H _ {2} (x ^ {*} (t), u ^ {*} (t), v, \psi_ {2} (t), t), \end{array} \right. \tag {7.4.27}
$$

由此从关系式 (7.4.21) 和 (7.4.25) 可知， $\forall t \in \Omega(t_0, t_f; (u^*, v^*))$ 有

$$
\begin{array}{l} \max _ {u \in \mathbf {U} _ {r _ {1}}} H (x ^ {*} (t), u, v ^ {*} (t), \psi (t), t) = H (x ^ {*} (t), u ^ {*} (t), v ^ {*} (t), \psi (t), t) \\ = \min _ {v \in \mathbf {V} _ {r 2}} H (x ^ {*} (t), u ^ {*} (t), v, \psi (t), t). \\ \end{array}
$$

由于 $\forall t\in \Omega (t_0,t_f;(u^*,v^*))$ 成立不等式
