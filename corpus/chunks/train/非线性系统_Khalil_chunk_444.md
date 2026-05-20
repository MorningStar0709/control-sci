注意到 $|\psi_2(x,\theta)|\leqslant a(1 + a)|x_1| + bx_2^2$

取 $v=\left\{\begin{aligned}-\eta(x)\operatorname{sgn}(z_{2}),&\quad\eta(x)|z_{2}|\geqslant\varepsilon\\-\eta^{2}(x)z_{2}/\varepsilon,&\quad\eta(x)|z_{2}|<\varepsilon\end{aligned}\right.$

其中对于 $\eta_0 > 0$ 和 $\varepsilon > 0$ ，有 $\eta(x) = \eta_0 + a(1 + a)|x_1| + bx_2^2$ 。当 $\eta(x)|z_2| \geqslant \varepsilon$ 时，

$$z _ {2} [ \psi_ {2} (x, \theta) + v ] \leqslant | \psi_ {2} | | z _ {2} | - \eta | z _ {2} | \leqslant 0$$

当 $\eta (x)|z_2| < \varepsilon$ 时， $z_{2}[\psi_{2}(x,\theta) + v] \leqslant |\eta ||z_{2}| - \frac{\eta^{2}z_{2}^{2}}{\varepsilon} \leqslant \frac{\varepsilon}{4}$

因此,有 $\dot{V}_{c}\leqslant-x_{1}^{2}-kz_{2}^{2}+\frac{\varepsilon}{4}$

该不等式表明,在一个有限时间区间内,对于某个 $k_{0}>0$ ,状态x进入半径为 $r=k_{0}\sqrt{\varepsilon}$ 的球 $B_{r}$ 内。在 $B_{r}$ 内对于某个 $\rho_{1}>0$ ,有

$$| \psi_ {2} (x, \theta) | \leqslant a (1 + a) | x _ {1} | + b r | x _ {2} | \leqslant \rho_ {1} (| x _ {1} | + | z _ {2} |)$$

$\rho_{1}$ 与 $\varepsilon$ 无关。在球 $B_{r}$ 与边界层 $\{\eta (x)|z_2| < \varepsilon \}$ 的相交部分，有

$$
\begin{array}{l} \dot {V} _ {c} \leqslant - x _ {1} ^ {2} - k z _ {2} ^ {2} + \rho_ {1} | x _ {1} | | z _ {2} | + \rho_ {1} | z _ {2} | ^ {2} - \frac {\eta_ {0} ^ {2} z _ {2} ^ {2}}{\varepsilon} \\ = - \frac {1}{2} x _ {1} ^ {2} - k z _ {2} ^ {2} - \left[ \frac {1}{2} x _ {1} ^ {2} - \rho_ {1} | x _ {1} | | z _ {2} | + \left(\frac {\eta_ {0} ^ {2}}{\varepsilon} - \rho_ {1}\right) z _ {2} ^ {2} \right] \\ \end{array}
$$

通过选择足够小的 $\varepsilon$ 可使方括号内的项为非负，因此

$$\dot {V} _ {c} \leqslant - \frac {1}{2} x _ {1} ^ {2} - k z _ {2} ^ {2}$$

并且原点是全局渐近稳定的。

总结本节内容,我们发现只要满足某一非奇异条件,反步法就可用于多输入系统中,即所谓分块反步法。考虑系统

$$\dot {\eta} = f (\eta) + G (\eta) \xi \tag {14.68}\dot {\xi} = f _ {a} (\eta , \xi) + G _ {a} (\eta , \xi) u \tag {14.69}$$

其中， $\eta \in R^n, \xi \in R^m, u \in R^m, m$ 可大于1。假设 $f, f_a, G$ 和 $G_a$ （已知函数）是在所讨论的定义域内的光滑函数， $f$ 和 $f_a$ 在原点为零，且 $G_a$ 是 $m \times m$ 阶非奇异矩阵。进一步假设方程(14.68)可通过光滑状态反馈控制律 $\xi = \phi(\eta), \phi(0) = 0$ 实现稳定，且已知一个李雅普诺夫函数 $V(\eta)$ （光滑，正定），对于某个正定函数 $W(\eta)$ ，满足不等式

$$\frac {\partial V}{\partial \eta} [ f (\eta) + G (\eta) \phi (\eta) ] \leqslant - W (\eta)$$

以 $V_{c} = V(\eta) + \frac{1}{2} [\xi -\phi (\eta)]^{\mathrm{T}}[\xi -\phi (\eta)]$

作为整个系统的备选李雅普诺夫函数,可得
