$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} _ {1} \boldsymbol {w} + \boldsymbol {B} _ {2} \boldsymbol {u}\boldsymbol {z} = \boldsymbol {C} _ {1} \boldsymbol {x} + \boldsymbol {D} _ {1 2} \boldsymbol {u} \tag {11-27}$$

讨论其 $H_{\infty}$ 次优问题的解。

给定正数 $\gamma_0 > 0$ ，取性能指标为

$$
\begin{array}{l} J [ \boldsymbol {u} (\cdot), \boldsymbol {w} (\cdot) ] = \int_ {0} ^ {+ \infty} [ \boldsymbol {z} ^ {\mathrm{T}} (t) \boldsymbol {z} (t) - \gamma_ {0} \boldsymbol {w} ^ {\mathrm{T}} (t) \boldsymbol {w} (t) ] \mathrm{d} t \\ = \int_ {0} ^ {+ \infty} \left[ \boldsymbol {x} ^ {\mathrm{T}} (t) \boldsymbol {C} _ {1} ^ {\mathrm{T}} \boldsymbol {C} _ {1} \boldsymbol {x} (t) + \boldsymbol {u} ^ {\mathrm{T}} (t) \boldsymbol {R} _ {2} \boldsymbol {u} (t) - \gamma_ {0} \boldsymbol {w} ^ {\mathrm{T}} (t) \boldsymbol {w} (t) \right] \mathrm{d} t \tag {11-28} \\ \end{array}
$$

考察系统式(11-27)以式(11-28)为性能指标的微分对策问题,即

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} _ {1} \boldsymbol {w} + \boldsymbol {B} _ {2} \boldsymbol {u}\min _ {\boldsymbol {u} (\cdot)} \max _ {\boldsymbol {w} (\cdot)} J [ \boldsymbol {u} (\cdot), \boldsymbol {w} (\cdot) ] \tag {11-29}$$

利用哈密顿-雅可比-依萨克斯方程(简称HJI方程)，对于微分对策问题式(11-29)，可得下列函数

$$\boldsymbol {u} ^ {*} (\boldsymbol {x}) = \boldsymbol {R} _ {2} ^ {- 1} \boldsymbol {B} _ {2} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {x}\boldsymbol {w} ^ {*} (\boldsymbol {x}) = \frac {1}{\gamma_ {0}} \boldsymbol {B} _ {1} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {x}$$

使式(11-29)中的 $J[u(\cdot),w(\cdot)]$ 达到极大极小。其中， $\pmb{P}$ 满足如下Riccati代数方程：

$$\boldsymbol {P} \boldsymbol {A} + \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {C} _ {1} ^ {\mathrm{T}} \boldsymbol {C} _ {1} + \frac {1}{\gamma_ {0}} \boldsymbol {P} \boldsymbol {B} _ {1} \boldsymbol {B} _ {1} ^ {\mathrm{T}} \boldsymbol {P} - \boldsymbol {P} \boldsymbol {B} _ {2} \boldsymbol {R} _ {2} ^ {- 1} \boldsymbol {B} _ {2} ^ {\mathrm{T}} \boldsymbol {P} = \mathbf {0} \quad (1 1 - 3 0)$$

定理2 对于给定线性定常系统式(11-27)，当 $(A,C_1)$ 完全可观测时，其全状态信息情况下的 $H_{\infty}$ 次优控制问题有解，即对给定的正数 $\gamma_0$ ，状态反馈 $\pmb{u}^{*}(\pmb{x}) = -R_{2}^{-1}\pmb{B}_{2}^{\mathrm{T}}\pmb{P}^{*}\pmb{x}$ 使得系统具有如下性质：

(1) 当 w=0 时, 闭环系统 $(11-27)$ 渐近稳定。

(2) 对于给定的正数 $\gamma_0, \forall w(t) \in L_2[0, +\infty)$ 皆有

$$\int_ {0} ^ {+ \infty} z ^ {\mathrm{T}} (t) z (t) \mathrm{d} t \leqslant \gamma_ {0} \int_ {0} ^ {+ \infty} w ^ {\mathrm{T}} (t) w (t) \mathrm{d} t$$

其中 $z(t) \stackrel{\triangle}{=} [C_1 - D_{12}R_2^{-1}B_2^T P^* ]x(t)$ 是(11-27)的系统输出， $P^*$ 是Riccati代数方程(11-30)的正定对称解。
