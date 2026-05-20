$$
\operatorname{sat} (y) = \left\{ \begin{array}{l l} y, & | y | \leqslant 1 \\ \operatorname{sgn} (y), & | y | > 1 \end{array} \right.
$$

$\varepsilon$ 为正常数。符号函数和饱和函数如图14.7所示。 $\operatorname {sat}(s / \varepsilon)$ 的线性部分的斜率为 $1 / \varepsilon$ ，要较好地逼近符号函数，要求有较小的 $\varepsilon$ 。极限情况下，即当 $\varepsilon$ 趋于零时，饱和函数 $\operatorname {sat}(s / \varepsilon)$ 近似为符号函数 $\operatorname {sgn}(s)$ 。为分析连续滑模控制器的性能，我们采用函数 $V = (1 / 2)s^2$ 来检验其到达阶段的特性。当 $|s|\geqslant \varepsilon$ 时，即在边界层 $\{|s|\leqslant \varepsilon \}$ 外时，函数 $V = (1 / 2)s^2$ 的导数满足不等式

$$\dot {V} \leqslant - g _ {0} \beta_ {0} | s |$$

因此只要 $|s(0)| > \varepsilon, |s(t)|$ 就是严格递减的，直到在有限时间内到达集合 $\{|s| \leqslant \varepsilon\}$ ，之后便一直保持在其内。在边界层内有 $\dot{x}_1 = -a_1 x_1 + s$

其中 $|s|\leqslant\varepsilon$ 。 $V_{1}=(1/2)x_{1}^{2}$ 的导数满足

$$\dot {V} _ {1} = - a _ {1} x _ {1} ^ {2} + x _ {1} s \leqslant - a _ {1} x _ {1} ^ {2} + | x _ {1} | \varepsilon \leqslant - (1 - \theta_ {1}) a _ {1} x _ {1} ^ {2}, \quad \forall | x _ {1} | \leqslant \frac {\varepsilon}{a _ {1} \theta_ {1}}$$

其中 $0 < \theta_{1} < 1$ 。因此，轨线在有限时间内到达集合 $\Omega_{\varepsilon} = \{|x_1| \leqslant \varepsilon / (a_1\theta_1), |s| \leqslant \varepsilon\}$ 。通常情况下我们不需要稳定原点，但通过减小 $\varepsilon$ ，用一个可以减小的最终边界，使系统达到毕竟有界性。再次考虑单摆方程，看这种情况下在 $\Omega_{\varepsilon}$ 内发生了什么。在边界层 $\{|s| \leqslant \varepsilon\}$ 内，控制律简化为线性反馈控制律 $u = -ks / \varepsilon$ ，闭环系统

$$\dot {x} _ {1} = x _ {2}\dot {x} _ {2} = - \left(g _ {0} / \ell\right) \sin \left(x _ {1} + \delta_ {1}\right) - \left(k _ {0} / m\right) x _ {2} - \left(k / m \ell^ {2} \varepsilon\right) \left(a _ {1} x _ {1} + x _ {2}\right)$$

有唯一的平衡点 $(\bar{x}_1,0)$ ，其中 $\bar{x}_1$ 满足方程

$$\varepsilon m g _ {0} \ell \sin (\bar {x} _ {1} + \delta_ {1}) + k a _ {1} \bar {x} _ {1} = 0$$

且当 $\varepsilon$ 较小时可近似为 $\bar{x}_1 \approx -(\varepsilon mg_0\ell / ka_1) \sin \delta_1$ 。进行变量代换

$$y _ {1} = x _ {1} - \bar {x} _ {1}, \quad y _ {2} = x _ {2}$$

可得 $\dot{y}_{1} = y_{2}$

$$\dot {y} _ {2} = - \sigma \left(y _ {1}\right) - \left(\frac {k _ {0}}{m} + \frac {k}{m \ell^ {2} \varepsilon}\right) y _ {2}$$

则将原平衡点移动到了原点,上式中

$$\sigma \left(y _ {1}\right) = \left(g _ {0} / \ell\right) \left[ \sin \left(y _ {1} + \bar {x} _ {1} + \delta_ {1}\right) - \sin \left(\bar {x} _ {1} + \delta_ {1}\right) \right] + \left(k a _ {1} / m \ell^ {2} \varepsilon\right) y _ {1}$$

以 $\tilde{V}=\int_{0}^{y_{1}}\sigma(s)ds+(1/2)y_{2}^{2}$

作为备选李雅普诺夫函数,可以证明当 $k/\varepsilon > m\ell g_{0}/a_{1}$ 时
