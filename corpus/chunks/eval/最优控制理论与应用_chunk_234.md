# 11.4.2 线性定常系统 $H_{\infty}$ 最优控制问题的求解

考察如下线性定常系统：

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} \boldsymbol {w} \tag {11-24}\boldsymbol {z} = \boldsymbol {C x}$$

其中， $x \in R^{n}$ 是状态， $w \in R^{r_{2}}$ 是外干扰， $z \in R^{m_{2}}$ 是输出，A、B、C 为适当维数的常数阵。

这里的问题是:对于 $\forall w(t)\in L_{2}[0,+\infty)$ ，求使

$$\int_ {0} ^ {+ \infty} z ^ {\mathrm{T}} (t) z (t) \mathrm{d} t \leqslant \gamma_ {0} \int_ {0} ^ {+ \infty} w ^ {\mathrm{T}} (t) w (t) \mathrm{d} t \tag {11-25}$$

成立的 A, B, C 应满足的关系, 其中 $z(t)$ 是在初态为 x(0) = 0 时对应于 $w(t) \in L_{2}[0, +\infty)$ 的系统式 (11 - 24) 的输出。

令

$$J [ \boldsymbol {w} (\cdot) ] = \int_ {0} ^ {+ \infty} [ \boldsymbol {z} ^ {\mathrm{T}} (t) \boldsymbol {z} (t) - \gamma_ {0} \boldsymbol {w} ^ {\mathrm{T}} (t) \boldsymbol {w} (t) ] \mathrm{d} t, \boldsymbol {w} (t) \in L _ {2} [ 0, + \infty)$$

有如下所谓“最优干扰问题”：

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} \boldsymbol {w}z = C x\max _ {\boldsymbol {w} (\cdot) \in L _ {2} [ 0, + \infty)} J [ \boldsymbol {w} (\cdot) ] = \max _ {\boldsymbol {w} (\cdot) \in L _ {2} [ 0, + \infty)} \int_ {0} ^ {+ \infty} [ \boldsymbol {z} ^ {\mathrm{T}} (t) \boldsymbol {z} (t) - \gamma_ {0} \boldsymbol {w} ^ {\mathrm{T}} (t) \boldsymbol {w} (t) ] \mathrm{d} t$$

利用使性能指标取极大值的哈密顿-雅可比-贝尔曼方程, 直接得 $J[w(\cdot)]$ 取极大值的 w 为

$$\boldsymbol {w} ^ {*} (\boldsymbol {x}) = \frac {1}{\gamma_ {0}} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {x}$$

而 $\pmb{P}$ 满足如下Riccati代数方程：

$$\boldsymbol {P} \boldsymbol {A} + \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {C} ^ {\mathrm{T}} \boldsymbol {C} + \frac {1}{\gamma_ {0}} \boldsymbol {P} \boldsymbol {B} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {P} = \mathbf {0} \tag {11-26}$$

定理 1 给定线性定常系统(11-24)，若 A、B、C 使 Riccati 代数方程(11-26)有正定对称解时，则对事先给定的正数 $\gamma_{0}$ 有

$$\int_ {0} ^ {+ \infty} z ^ {\mathrm{T}} (t) z (t) \mathrm{d} t \leqslant \gamma_ {0} \int_ {0} ^ {+ \infty} w ^ {\mathrm{T}} (t) w (t) \mathrm{d} t, \forall w (t) \in L _ {2} [ 0, + \infty)$$

其中 $z(t)$ 是在初态为 $\pmb{x}(0) = \mathbf{0}$ 时对应于 $\pmb{w}(t) \in L_2[0, +\infty)$ 的系统输出。

下面继续讨论线性定常系统 $H_{\infty}$ 次优控制问题的求解。

为了简单起见, 在系统式(11-20)中设 $D_{11} = 0$ , $C_1^{\mathrm{T}}D_{12} = 0$ , $D_{12}^{\mathrm{T}}D_{12}\stackrel {\triangle}{=} R_2 > 0$ , 且 $\pmb{x}$ 和 $\pmb{w}$ 都可以观测。考虑此时系统(11-20)的 $H_{\infty}$ 次优控制问题的解, 即对系统
