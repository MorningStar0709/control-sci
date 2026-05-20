$$H _ {1} \left(x ^ {*} (t), u ^ {*} (t), v ^ {*} (t), \psi_ {1} (t), t\right) = H _ {1} \left(x ^ {*} \left(t _ {f}\right), u ^ {*} \left(t _ {f}\right), v ^ {*} \left(t _ {f}\right), \psi_ {1} \left(t _ {f}\right), t _ {f}\right)+ \int_ {t _ {f}} ^ {t} \frac {\partial H _ {1} (x ^ {*} (\tau) , u ^ {*} (\tau) , v ^ {*} (\tau) , \psi_ {1} (\tau) , \tau)}{\partial t} d \tau . \tag {7.4.22}$$

最优控制问题 2:

$$\dot {x} = f (x, u ^ {*} (t), v, t), \quad x (t _ {0}) = x _ {0},\boldsymbol {v} \in \mathbb {V} _ {\tau_ {2}},\mathcal {S} = \left\{x (t _ {f}) \mid g (x (t _ {f}), t _ {f}) = 0 \right\},J [ u ^ {*} (\cdot), v ] = k (x ^ {*} (t _ {f}), t _ {f}) + \int_ {t _ {0}} ^ {t _ {f}} l (x (t), u ^ {*} (t), v (t), t) d t,$$

求 $v^{*}(\cdot)\in \mathcal{V}_{[t_{0},t_{f}]}$ 使 $J[u^{*},v]$ 达到极大.

最优控制问题2的Hamilton函数为

$$H _ {2} (x, u ^ {*} (t), v, \psi_ {2}, t) = - l (x, u ^ {*} (t), v, t) + \psi_ {2} ^ {\mathrm{T}} f (x, u ^ {*} (t), v, t).$$

根据7.1中定理7.1.4, 如果 $v^{*}(t), x^{*}(t)$ 是最优控制问题2的最优解, 则存在向量值函数 $\psi_{2}(t)$ 和Lagrange乘子向量 $\mu_{2}$ , 使得 $v^{*}(t), x^{*}(t), \psi_{2}(t)$ 和 $\mu_{2}$ 在区间 $[t_0, t_f]$ 上同时满足

(1)

$$
\left\{ \begin{array}{l} \dot {x} ^ {*} (t) = \left(\frac {\partial H _ {2} \left(x ^ {*} (t) , u ^ {*} (t) , v ^ {*} (t) , \psi_ {2} (t)\right) , t}{\partial \psi_ {2}}\right) ^ {\mathrm{T}}, \\ x ^ {*} \left(t _ {0}\right) = x _ {0}, \end{array} \right. \tag {7.4.23}

\left\{ \begin{array}{l} \dot {\psi} _ {2} ^ {\mathrm{T}} (t) = - \frac {\partial H _ {2} \left(x ^ {*} (t) , u ^ {*} (t) , v ^ {*} (t) , \psi_ {2} (t) , t\right)}{\partial x}, \\ \psi_ {2} ^ {\mathrm{T}} \left(t _ {f}\right) = - \frac {\partial k \left(x ^ {*} \left(t _ {f}\right) , t _ {f}\right)}{\partial x} - \mu_ {2} ^ {\mathrm{T}} \frac {\partial g \left(x ^ {*} \left(t _ {f}\right) , t _ {f}\right)}{\partial x}; \end{array} \right. \tag {7.4.24}
$$

(2) $\forall t \in \Omega(t_0, t_f; v^*)$ , 有

$$H _ {2} (x ^ {*} (t), u ^ {*} (t), v ^ {*} (t), \psi_ {2} (t), t) = \min _ {v \in \mathbf {V} _ {r _ {2}}} H _ {2} (x ^ {*} (t), u ^ {*} (t), v, \psi_ {2} (t), t); \tag {7.4.25}$$

(3) 当 $t_f$ 固定时， $\forall t \in \Omega(v^*; t_0, t_f)$ ，有

$$H _ {2} \left(x ^ {*} (t), u ^ {*} (t), v ^ {*} (t), \psi_ {2} (t), t\right) = H _ {2} \left(x ^ {*} \left(t _ {f}\right), u ^ {*} \left(t _ {f}\right), v ^ {*} \left(t _ {f}\right), \psi_ {2} \left(t _ {f}\right), t _ {f}\right)+ \int_ {t _ {f}} ^ {t} \frac {\partial H _ {2} (x ^ {*} (\tau) , u ^ {*} (\tau) , v ^ {*} (\tau) , \psi_ {2} (\tau) , \tau)}{\partial t} \mathrm{d} \tau . \tag {7.4.26}$$

现定义系统 (7.4.8) 和性能指标 (7.4.11) 的 Hamilton 函数为
