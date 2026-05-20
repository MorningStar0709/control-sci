# 最优策略的必要条件 —— 双方极值原理

定量微分对策问题指寻求容许控制策略 $(u^{*}(t), v^{*}(t))$ ，使得

$$J [ u ^ {*}, v ] \leqslant J [ u ^ {*}, v ^ {*} ] \leqslant J [ u, v ^ {*} ], \quad (u, v) \in \mathcal {W} _ {[ t _ {0}, t _ {f} ]}.$$

不等式 (7.4.12) 可以拆成两个最优控制问题，即

$$J [ u ^ {*}, v ] \leqslant J [ u ^ {*}, v ^ {*} ], \quad \forall v (t) \in \mathcal {V} _ {[ t _ {0}, t _ {f} ]}, \tag {7.4.13}J [ u ^ {*}, v ^ {*} ] \leqslant J [ u, v ^ {*} ], \quad \forall u (t) \in \mathcal {U} _ {[ t _ {0}, t _ {f} ]}. \tag {7.4.14}$$

因此，当最优策略 $(u^{*}(t), v^{*}(t))$ 存在时，可以利用7.1中的极大值原理和相应的极小值原理分别得出 $u^{*}(\cdot), v^{*}(\cdot)$ 满足的必要条件.

最优控制问题 1:

$$\dot {x} = f (x, u, v ^ {*} (t), t), \quad x \left(t _ {0}\right) = x _ {0}, \tag {7.4.15}u \in \mathbb {U} _ {r _ {1}}, \tag {7.4.16}\mathcal {S} = \left\{x (t _ {f}) | g (x (t _ {f}), t _ {f}) = 0 \right\}. \tag {7.4.17}J [ u, v ^ {*} ] = k (x \left(t _ {f}\right), t _ {f}) + \int_ {t _ {0}} ^ {t _ {f}} l (x (t), u (t), v ^ {*} (t), t) d t, \tag {7.4.18}$$

求 $u^{*}(\cdot)\in \mathcal{U}_{[t_{0},t_{f}]}$ 使 $J[u,v^{*}]$ 达到极小.

最优控制问题1的Hamilton函数为

$$H _ {1} (x, u, v ^ {*} (t), \psi_ {1}, t) = - l (x, u, v ^ {*} (t), t) + \psi_ {1} ^ {\mathrm{T}} f (x, u, v ^ {*} (t), t).$$

根据7.1中定理7.1.4, 如果 $(u^{*}(t), x^{*}(t))$ 是最优控制问题1的最优解, 则存在向量值函数 $\psi_{1}(t)$ 和Lagrange乘子向量 $\mu_{1}$ , 使得 $u^{*}(t), x^{*}(t), \psi_{1}(t)$ 和 $\mu_{1}$ 在区间 $[t_0, t_f]$ 上同时满足

(1)

$$
\left\{ \begin{array}{l} \dot {x} ^ {*} (t) = \left(\frac {\partial H _ {1} \left(x ^ {*} (t) , u ^ {*} (t) , v ^ {*} (t) , \psi_ {1} (t) , t\right)}{\partial \psi_ {1}}\right) ^ {\mathrm{T}}, \\ x ^ {*} \left(t _ {0}\right) = x _ {0}, \end{array} \right. \tag {7.4.19}

\left\{ \begin{array}{l} \dot {\psi} _ {1} ^ {\mathrm{T}} (t) = - \frac {\partial H _ {1} \left(x ^ {*} (t) , u ^ {*} (t) , v ^ {*} (t) , \psi_ {1} (t) , t\right)}{\partial x}, \\ \psi_ {1} ^ {\mathrm{T}} \left(t _ {f}\right) = - \frac {\partial k \left(x ^ {*} \left(t _ {f}\right) , t _ {f}\right)}{\partial x} - \mu_ {1} ^ {\mathrm{T}} \frac {\partial g \left(x ^ {*} \left(t _ {f}\right) , t _ {f}\right)}{\partial x}; \end{array} \right. \tag {7.4.20}
$$

(2) $\forall t \in \Omega(t_0, t_f; u^*)$ , 有

$$H _ {1} (x ^ {*} (t), u ^ {*} (t), v ^ {*} (t), \psi_ {1} (t), t) = \max _ {u \in \mathbb {U} _ {r _ {1}}} H _ {1} (x ^ {*} (t), u, v ^ {*} (t), \psi_ {1} (t), t); \tag {7.4.21}$$

(3) 当 $t_f$ 固定时， $\forall t \in \Omega(u^*; t_0, t_f]$ 有
