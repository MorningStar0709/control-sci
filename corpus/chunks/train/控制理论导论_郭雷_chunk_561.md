# 对策过程的“最优性原理”和Hamilton-Jacobi-Issacs方程

定量微分对策过程的最优性原理指的是：最优对策过程的任何最后一段都是最优的。为简化叙述和简化书写，这里仅对定常情况下一类特殊定量微分对策过程进行讨论。于是我们考察

$$\dot {x} = f (x, u, v), \qquad x (0) = x _ {0} \in \mathbb {R} ^ {n}, \tag {7.4.30}(u, v) \in \mathbb {U} _ {r _ {1}} \times \mathbb {V} _ {r _ {2}} \subseteq \mathbb {R} ^ {r _ {1}} \times \mathbb {R} ^ {r _ {2}}, \tag {7.4.31}\mathcal {S} = \mathbb {R} ^ {n}, \tag {7.4.32}J [ u (\cdot), v ] = \int_ {0} ^ {t _ {f}} l (x (t), u (t), v (t)) \mathrm{d} t, \tag {7.4.33}$$

其中 $t_f > 0$ 固定， $f(x, u, v)$ 和 $l(x, u, v)$ 的假设同前，并取容许策略集 $\mathcal{W}_{[0, t_f]}$ .

令 $(u^{*}(t), v^{*}(t))$ 为对策过程 (7.4.30)\~(7.4.33) 的最优策略， $x^{*}(t)$ 是相应的最优轨线。于是最优对策过程 $(u^{*}(t), v^{*}(t), x^{*}(t))$ 满足鞍点条件

$$J [ u ^ {*}, v ] \leqslant J [ u ^ {*}, v ^ {*} ] \leqslant J [ u, v ^ {*} ], \quad \forall (u (t), v (t)) \in \mathcal {W} _ {[ 0, t _ {f} ]}, \tag {7.4.34}$$

利用鞍点条件，用反证法能够证明，对所论定量微分对策过程，其最优性原理成立，即设 $(u^{*}(t), v^{*}(t))$ 为 $[0, t_{f}]$ 上 $x(0) = x_0$ 的最优策略。任取 $\tilde{t} \in [0, t_{f}]$ ，当把 $(u^{*}(t), v^{*}(t))$ 限制在 $[\tilde{t}, t_{f}]$ 上时，它是 $[\tilde{t}, t_{f}]$ 上以 $\tilde{x} = x^{*}(\tilde{t})$ 为初始条件的最优策略。设 $\forall x_0 \in \mathbb{R}^n$ ，式 (7.4.30)\~(7.4.33) 的最优策略 $(u^{*}(t), v^{*}(t))$ 存在。记 $J^{*}(x_0, 0) \stackrel{\mathrm{def}}{=} J[u^{*}, v^{*}]$ 。显然有 $J^{*}(x(t_{f}), t_{f}) = 0$ 。下面总假设标量函数 $J^{*}(x, t) \in C^{1}$ ，且其混合导数连续。

任取 $x_0 \in \mathbb{R}^n$ , 令 $(u^*(t), v^*(t), x^*(t))$ 是式 (7.4.30)\~ (7.4.33) 的最优对策过程. 任取时刻 $t \in (0, t_f)$ , 依“最优性原理”有

$$
\begin{array}{l} J ^ {*} (x _ {0}, 0) = \int_ {0} ^ {t _ {f}} l \left(x ^ {*} (\tau), u ^ {*} (\tau), v ^ {*} (\tau)\right) d \tau \\ = \int_ {0} ^ {t} l (x ^ {*} (\tau), u ^ {*} (\tau), v ^ {*} (\tau)) \mathrm{d} \tau + J ^ {*} (x ^ {*} (t), t). \\ \end{array}
$$

在上式两端对 $t$ 求导得

$$0 = l \left(x ^ {*} (t), u ^ {*} (t), v ^ {*} (t)\right) + \frac {\partial J ^ {*} \left(x ^ {*} (t) , t\right)}{\partial t} + \frac {\partial J ^ {*} \left(x ^ {*} (t) , t\right)}{\partial x} f \left(x ^ {*} (t), u ^ {*} (t), v ^ {*} (t)\right). \tag {7.4.35}$$

另一方面，任取 $t \in \Omega(0, t_f; (u^*, v^*)), \Delta t > 0$ 和 $(\bar{u}, \dot{v}) \in \mathbb{U}_{r_1} \times \mathbb{V}_{r_2}$ . 设系统 (7.4.30) 按以下方式进行对策：

(1) 在区间 $[0, t]$ 上，以 $x(0) = x_0$ 为初值按 $(u^*(t), v^*(t))$ 进行对策，即

$$\dot {x} ^ {*} (s) = f \left(x ^ {*} (s), u ^ {*} (s), v ^ {*} (s)\right), \quad s \in [ 0, t ], \quad x ^ {*} (0) = x _ {0},$$

其对策值为 $\int_0^t l(x^* (s),u^* (s),v^* (s))\mathrm{d}s;$
