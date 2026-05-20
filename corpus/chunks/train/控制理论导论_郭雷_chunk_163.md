$$\boldsymbol {x} ^ {\mathrm{T}} (t) \left(\boldsymbol {A} ^ {\mathrm{T}} (t) + \boldsymbol {A} (t)\right) \boldsymbol {x} (t) \leqslant \lambda^ {+} (t) \boldsymbol {x} ^ {\mathrm{T}} (t) \boldsymbol {x} (t), \quad \forall t \geqslant t _ {0}.$$

由于

$$\frac {\mathrm{d}}{\mathrm{d} t} (x ^ {\mathrm{T}} (t) x (t)) = \frac {\mathrm{d}}{\mathrm{d} t} | x (t) | ^ {2} = x ^ {\mathrm{T}} (A ^ {\mathrm{T}} (t) + A (t)) x (t),$$

所以有

$$\frac {\mathrm{d}}{\mathrm{d} t} | x (t) | ^ {2} \leqslant \lambda^ {+} (t) | x (t) | ^ {2}. \tag {2.4.15}$$

从 $t_0$ 到 $t$ 积分上不等式 (2.4.15) 得到

$$
\begin{array}{l} | x (t) | ^ {2} \leqslant | x (t _ {0}) | ^ {2} \mathrm{e} ^ {\int_ {t _ {0}} ^ {t} \lambda^ {+} (s) d s} \\ \leqslant | x (t _ {0}) | ^ {2} \mathrm{e} ^ {- h (t - t _ {0})}, \quad \forall t \geqslant t _ {0}. \\ \end{array}
$$

由此得

$$\lim _ {t \rightarrow + \infty} x (t) = 0,$$

即微分方程 (2.4.11) 的零 (平衡) 解是渐近稳定的.

定常微分方程具有对时间的“平移性”，即如果 $x(t)$ 是定常微分方程的解， $a$ 为任意固定实数，那么 $x(t + a)$ 仍是它的解。所以我们总可以把初始时刻取为零。但是对于时变微分方程，情况很不一样，其稳定性与初始时刻有关。这里我们仅对线性时变微分方程作一些介绍。

定义2.4.9 如果对于任给的 $\varepsilon > 0$ ，存在仅依赖于 $\varepsilon$ 而与初始时刻 $t_0$ 无关的正数 $\delta = \delta(\varepsilon)$ ，使当 $|x_0| < \delta$ 时，成立

$$\left| x (t; t _ {0}, x _ {0}) \right| < \varepsilon , \quad \forall t \geqslant t _ {0},$$

则称微分方程 (2.4.11) 的零平衡解是一致稳定的.

如果微分方程 (2.4.11) 的零平衡解是一致稳定的，并且对于任意 $\eta > 0, t_0 \geqslant 0$ ，存在与 $\eta$ 和 $t_0$ 无关的 $\delta_1 > 0$ ，和仅依赖于 $\eta$ 的正数 $T(\eta)$ ，使得当 $|x_0| < \delta_1$ 时，成立不等式

$$\left| x (t; t _ {0}, x _ {0}) \right| < \eta , \quad \forall t \geqslant t _ {0} + T (\eta),$$

则称微分方程 (2.4.1) 的零平衡解是一致渐近稳定的.

由一致渐近稳定性的定义直接得出，当 $|x_0| < \delta_1$ 时，有

$$\lim _ {t \rightarrow + \infty} x (t; t _ {0}, x _ {0}) = 0.$$

定义 2.4.10 线性时变微分方程 (2.4.11) 的零平衡解称为按指数稳定的 (简称为指数稳定的), 如果存在正数 M, $\alpha$ , 使得微分方程 (2.4.11) 的解 $x(t; t_{0}, x_{0})$ 满足

$$\left| x (t; t _ {0}, x _ {0}) \right| \leqslant M \left| x _ {0} \right| \mathrm{e} ^ {- \alpha (t - t _ {0})}, \quad \forall t \geqslant t _ {0}. \forall x _ {0} \in \mathbb {R}.$$

正数 $\alpha$ 称为微分方程 (2.4.11) 的衰减度。衰减度是表征线性微分方程 (2.4.11) 的解趋于其零平衡解的快、慢程度的一个量。

定理2.4.6 为了线性时变微分方程(2.4.11)的平衡解 $x = 0$ 一致渐近稳定，充分必要条件是存在正数 $M, \alpha,$ 使得微分方程(2.4.11)的状态转移矩阵 $\Phi(t; t_0)$ 满足

$$\| \Phi (t; t _ {0}) \| \leqslant M \mathrm{e} ^ {- \alpha (t - t _ {0})}, \quad \forall t \geqslant t _ {0}. \tag {2.4.16}$$

证明 充分性. 方程 (2.4.11) 的解 $x(t; t_0, x_0)$ 可表示为

$$x (t; t _ {0}, x _ {0}) = \Phi (t; t _ {0}) x _ {0},$$

所以有
