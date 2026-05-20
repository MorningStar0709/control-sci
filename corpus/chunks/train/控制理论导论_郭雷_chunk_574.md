$$\int_ {0} ^ {+ \infty} z ^ {\mathrm{T}} (t) z (t) \mathrm{d} t \leqslant \gamma_ {0} \int_ {0} ^ {+ \infty} w ^ {\mathrm{T}} (t) w (t) \mathrm{d} t, \tag {7.5.13}$$

或者说，对系统(7.5.12)，当A为稳定矩阵时，求使不等式(7.5.13)成立的条件.

给定 $\gamma_0 > 0$ ，对于系统(7.5.12)，取性能指标

$$J [ w (\cdot) ] = \int_ {0} ^ {+ \infty} \left[ z ^ {\mathrm{T}} (t) z (t) - \gamma_ {0} w ^ {\mathrm{T}} (t) w (t) \right] \mathrm{d} t, \quad w (t) \in L _ {2} ([ 0, + \infty); \mathbb {R} ^ {r}).$$

对于“最坏”干扰问题

$$
\left\{ \begin{array}{l} \dot {x} = A x + B w, \\ z = C x, \\ \max _ {w \in L _ {2} [ [ 0, + \infty); \mathbb {R} ^ {r} ]} J [ w (\cdot) ], \end{array} \right. \tag {7.5.14}
$$

利用7.1节中关于HJB方程的性质，可以证明使式(7.5.14)中 $J[w]$ 达到极大的 $w^{*}(x)$ 为

$$w ^ {*} (x) = \frac {1}{2 \gamma_ {0}} B ^ {\mathrm{T}} P x,$$

其中 $P$ 满足下列Riccati型矩阵代数方程：

$$P A + A ^ {\mathrm{T}} P + C ^ {\mathrm{T}} C + \frac {1}{\gamma_ {0}} P B B ^ {\mathrm{T}} P = 0. \tag {7.5.15}$$

不难证明，对于稳定矩阵 $A$ ，当(7.5.15)存在正定对称解矩阵 $P^{*}$ 时，不等式(7.5.13)成立.

其次考察 $H_{\infty}$ 控制次优问题的解。为简化书写和叙述，下面仅对系统 (7.5.8) 中 $D_{11} = 0, C_1^{\mathrm{T}} D_{12} = 0, D_{12}^{\mathrm{T}} D_{12} \stackrel{\mathrm{def}}{=} R_2$ 非奇异和 $x, w$ 皆可测 (即全息) 情况进行讨论。现在我们基于定量微分对策 (视外干扰为对策中的一方) 有关结果，讨论系统

$$
\left\{ \begin{array}{l} \dot {x} = A x + B _ {1} w + B _ {2} u, \\ z = C _ {1} x + D _ {1 2} u, \end{array} \right. \tag {7.5.16}
$$

的 $H_{\infty}$ 控制次优问题的求解.

给定 $\gamma_0 > 0$ ，取对策指标

$$J [ u, w ] = \int_ {0} ^ {+ \infty} \left[ x ^ {\mathrm{T}} (t) C _ {1} ^ {\mathrm{T}} C _ {1} x (t) + u ^ {\mathrm{T}} (t) R _ {2} u (t) - \gamma_ {0} w ^ {\mathrm{T}} (t) w (t) \right] \mathrm{d} t. \tag {7.5.17}$$

对于定量微分对策问题

$$
\left\{ \begin{array}{l} \dot {x} = A x + B _ {1} w + B _ {2} u, \\ z = C _ {1} x + D _ {1 2} u, \\ \min _ {u} \max _ {w} J [ u, w ], (u, w) \in L _ {2} ([ 0, + \infty); \mathbb {R} ^ {r _ {2}}) \times L _ {2} ([ 0, + \infty); \mathbb {R} ^ {r _ {1}}), \end{array} \right. \tag {7.5.18}
$$

利用7.4节中中关于HJI方程(7.4.54)的结论，可以证明问题(7.5.18)的反馈形式的最优策略为

$$
\left\{ \begin{array}{l} u ^ {*} (x) = - R _ {2} ^ {- 1} B _ {2} ^ {\mathrm{T}} P ^ {*} x, \\ w ^ {*} (x) = \frac {1}{\gamma_ {0}} B _ {1} ^ {\mathrm{T}} P ^ {*} x, \end{array} \right.
$$

其中 $P^{*}$ 满足Riccati型矩阵代数方程

$$P A + A ^ {\mathrm{T}} P + C _ {1} ^ {\mathrm{T}} C _ {1} + \frac {1}{\gamma_ {0}} P B _ {1} B _ {1} ^ {\mathrm{T}} P - P B _ {2} R _ {2} ^ {- 1} B _ {2} ^ {\mathrm{T}} P = 0. \tag {7.5.19}$$

不难证明，如果 $(A, C_1)$ 完全能观测，当(7.5.18)存在正定对称解矩阵 $P^*$ 时，下列两结论成立：

(1) 受干扰影响的闭环系统

$$\dot {x} = A x + B _ {1} w - B _ {2} R _ {2} ^ {- 1} B _ {2} P ^ {*} x \tag {7.5.20}$$

是内部稳定的；
