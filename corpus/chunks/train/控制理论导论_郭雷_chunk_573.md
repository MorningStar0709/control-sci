其中状态变量 $x \in \mathbb{R}^n$ ，被调变量 $z \in \mathbb{R}^{m_1}$ ，量测变量 $y \in \mathbb{R}^{m_2}$ ，控制输入变量 $u \in \mathbb{R}^{r_2}$ ，外干扰输入变量 $w \in \mathbb{R}^{r_1}$ ，A, $B_1, B_2, C_1, C_2, D_{11}, D_{12}$ 和 $D_{21}$ 皆为具有适当行列数的常矩阵。

系统 (7.5.8) 的 $H_{\infty}$ 控制问题是指：求控制规律 $u = u(\cdot)$ ，它具有如下性质：

(1) 使相应于 (7.5.8) 的闭环系统内部稳定，指当 $w = 0$ 时，闭环系统

$$\dot {x} = A x + B _ {2} u (\cdot) \tag {7.5.9}$$

是渐近稳定的：

(2) 对于 $L_{2}([0, +\infty); \mathbb{R}^{r_{1}})$ 中任意 $w(t)$ , 受干扰闭环系统

$$\dot {x} = A x + B _ {1} w (t) + B _ {2} u (\cdot) \tag {7.5.10}$$

的零初态响应 $z_{c}(t) = C_{1}x(t) + D_{11}w(t) + D_{12}u(\cdot)$ 满足

$$\int_ {0} ^ {+ \infty} z _ {c} ^ {\mathrm{T}} (t) z _ {c} (t) \mathrm{d} t \leqslant \mathcal {G} _ {2 c} \int_ {0} ^ {+ \infty} w ^ {\mathrm{T}} (t) w (t) \mathrm{d} t, \tag {7.5.11}$$

且 $\mathcal{G}_{2c}$ 是使上式成立的最小常数，而 $x(t)$ 是式(7.5.10)以 $x(0) = 0$ 为初值的解.

$$\mathcal {G} _ {2 c} \stackrel {\mathrm{def}} {=} \sup _ {w (\cdot) \in L _ {2} [ [ 0, + \infty); \mathbb {R} ^ {r _ {1}} ]} \frac {\int_ {0} ^ {+ \infty} z _ {c} ^ {\mathrm{T}} (t) z _ {c} (t) \mathrm{d} t}{\int_ {0} ^ {+ \infty} w ^ {\mathrm{T}} (t) w (t) \mathrm{d} t}, \text {称为系统(7.5.8)的} L _ {2 ^ {-}} \text {增益}.$$

不等式 (7.5.11) 可以认为是在所设计的控制器 $u(\cdot)$ 作用下，闭环系统对外部干扰可抑制能力的一种刻划。

注7.5.3 控制 $u(\cdot)$ 可以是状态 $x$ 的向量值函数 $u(x)$ , 可以是量测输出 $y$ 的向量值函数 $u(y)$ , 亦可是待设计的动态系统的状态 (或输出) $\theta$ 的向量值函数 $u(\theta)$ , 待设计的动态系统称为动态补偿器.

时域中 $H_{\infty}$ 控制设计中，求满足(1)和(2)的控制器 $u(\cdot)$ 的问题称为“最优问题”，其中涉及求最小的 $\mathcal{G}_{2c}$ 问题。可以证明，对于系统(7.5.8)，在一定条件下，最小的 $\mathcal{G}_{2c}$ 存在，但不易求得。用 $H_{\infty}$ 控制方法设计控制系统时，常采用根据设计要求来给定增益 $\gamma$ ，也就是“次优问题”。

给定 $\gamma_0 > 0$ ，求具有下列性质的控制规律：

(1) 使相应于式 (7.5.8) 的闭环系统 (7.5.9) 内部稳定;

(2) $\forall w(\cdot) \in L_2([0, +\infty); \mathbb{R}^{r_1})$ , 相应于式 (7.5.8) 受外干扰的闭环系统 (7.5.10) 的零初态响应 $z_c(t)$ 满足

$$\int_ {0} ^ {+ \infty} z _ {c} ^ {\mathrm{T}} (t) z _ {c} (t) \mathrm{d} t \leqslant \gamma_ {0} \int_ {0} ^ {+ \infty} w ^ {\mathrm{T}} (t) w (t) \mathrm{d} t.$$

时域 $H_{\infty}$ 控制问题的次优解. 首先考察稳定系统对外干扰的抑制问题. 系统

$$
\left\{ \begin{array}{l} \dot {x} = A x + B w, \\ z = C x \end{array} \right. \tag {7.5.12}
$$

中 $x, z$ 分别是适当维数的状态和被调输出， $w$ 为外干扰， $A, B, C$ 为相应阶的常矩阵， $A$ 为稳定矩阵.

这里的问题是：给定 $\gamma_0 > 0, \forall w(\cdot) \in L_2([0, +\infty); \mathbb{R}^{r_1})$ ，系统 (7.5.12) 的零初态响应 $z(t)$ 是否满足或在什么条件下满足不等式
