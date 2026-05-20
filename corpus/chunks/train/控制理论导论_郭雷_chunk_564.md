利用鞍点条件(7.4.34)的右方不等式,采用类似方法可以得到, $\forall t\in\Omega(0,t_{f};(u^{*},v^{*}))$

$$\frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial t} + \max _ {v \in \mathbf {V} _ {r _ {2}}} \min _ {u \in \mathbb {U} _ {r _ {1}}} \left\{\frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x} f (x ^ {*} (t), u, v) + l (x ^ {*} (t), u, v) \right\} \geqslant 0. \tag {7.4.39}$$

联合不等式 (7.4.38) 和 (7.4.39)，并利用等式 (7.4.35) 可得， $\forall t \in \Omega(0, t_f; (u^*, v^*))$

$$
\begin{array}{l} \begin{array}{l} \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial t} + \min _ {u \in \mathbb {U} _ {r _ {1}}} \max _ {v \in \mathbb {V} _ {r _ {2}}} \left\{\frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x} f (x ^ {*} (t), u, v) + l (x ^ {*} (t), u, v) \right\} \\ = \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial t} + \max _ {v \in \mathbb {V} _ {r _ {2}}} \min _ {u \in \mathbb {U} _ {r _ {1}}} \left\{\frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x} f (x ^ {*} (t), u, v) + l (x ^ {*} (t), u, v) \right\} \end{array} \tag {7.4.40} \\ = \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial t} + \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x} f (x ^ {*} (t), u ^ {*} (t), v ^ {*} (t)) + l (x ^ {*} (t), u ^ {*} (t), v ^ {*} (t)) \\ = 0. \\ \end{array}
$$

此外，

$$J ^ {*} (x ^ {*} (t _ {f}), t _ {f}) = 0. \tag {7.4.41}$$

下列带终端条件的方程

$$
\left\{ \begin{array}{l} \frac {\partial J (x , t)}{\partial t} + \min _ {u \in \mathbb {U} _ {r _ {1}}} \max _ {v \in \mathbb {V} _ {r _ {2}}} \left\{\frac {\partial J (x , t)}{\partial x} f (x, u, v) + l (x, u, v) \right\} = 0, \\ J (x (t _ {f}), t _ {f}) = 0, \end{array} \right. \tag {7.4.42}
$$

称为Hamilton-Jacobi-Issacs方程(简称HJI方程).

式 (7.4.40) 和 (7.4.41) 表明，定量微分对策过程 (7.4.8)\~(7.4.11) 的最优策略 $(u^{*}(t), v^{*}(t))$ ，最优轨线 $x^{*}(t)$ ，和 $t$ 时刻以 $x^{*}(t)$ 为初态的最优对策值 $J^{*}(x^{*}(t), t)$ 同时满足 HJI 方程 (7.4.42).
