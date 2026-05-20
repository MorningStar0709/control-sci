其中 $\theta_{1}$ 和 $\theta_{2}$ 是未知参数，对于某个已知边界 $a$ 和 $b$ 满足 $|\theta_1| \leqslant a$ 和 $|\theta_2| \leqslant b$ ，系统取式(14.66)的形式，其中 $\delta_{1} = \theta_{1}x_{1}\sin x_{2}, \delta_{2} = \theta_{2}x_{2}^{2}$ 。函数 $\delta_{1}$ 全局满足不等式 $|\delta_{1}| \leqslant a|x_{1}|$ ，函数 $\delta_{2}$ 在 $|x_{2}| \leqslant \rho$ 时满足不等式 $|\delta_{2}| \leqslant b\rho |x_{2}|$ 。首先考虑系统

$$\dot {x} _ {1} = x _ {2} + \theta_ {1} x _ {1} \sin x _ {2}$$

取 $x_{2} = \phi_{1}(x_{1}) = -k_{1}x_{1}, V_{1}(x_{1}) = x_{1}^{2} / 2$ ，得

$$\dot {V} _ {1} = x _ {1} \phi_ {1} (x _ {1}) + \theta_ {1} x _ {1} ^ {2} \sin x _ {2} \leqslant - (k _ {1} - a) x _ {1} ^ {2}$$

选择 $k_{1} = 1 + a$ ，为运用反步法，通过变量代换 $z_{2} = x_{2} + (1 + a)x_{1}$ ，将系统重写为

$$\dot {x} _ {1} = - (1 + a) x _ {1} + \theta_ {1} x _ {1} \sin x _ {2} + z _ {2}\dot {z} _ {2} = \psi_ {1} (x) + \psi_ {2} (x, \theta) + u$$

其中 $\psi_{1} = x_{1} + (1 + a)x_{2},\quad \psi_{2} = (1 + a)\theta_{1}x_{1}\sin x_{2} + \theta_{2}x_{2}^{2}$

以 $V_{c} = (x_{1}^{2} + z_{2}^{2}) / 2$ 作为复合李雅普诺夫函数，可得

$$\dot {V} _ {c} \leqslant - x _ {1} ^ {2} + z _ {2} [ x _ {1} + \psi_ {1} (x) + \psi_ {2} (x, \theta) + u ]$$

取 $u = -x_{1} - \psi_{1}(x) - kz_{2}$

得 $\dot{V}_{c}\leqslant-x_{1}^{2}+z_{2}\psi_{2}(x,\theta)-kz_{2}^{2}$

$$\leqslant - x _ {1} ^ {2} + a (1 + a) \left| x _ {1} \right| \left| z _ {2} \right| + b x _ {2} ^ {2} \left| z _ {2} \right| - k z _ {2} ^ {2}$$

在集合 $\Omega_{c}=\{x\in R^{2}\mid V_{c}(x)\leqslant c\}$

内，有 $|x_{2}|\leqslant\rho,\rho$ 与c有关 $^{①}$ 。把分析限定在 $\Omega_{c}$ 内，可得

$$\dot {V} _ {c} \leqslant - x _ {1} ^ {2} + a (1 + a) | x _ {1} | | z _ {2} | + b \rho | z _ {2} - (1 + a) x _ {1} | | z _ {2} | - k z _ {2} ^ {2}\leqslant - x _ {1} ^ {2} + (1 + a) (a + b \rho) | x _ {1} | | z _ {2} | - (k - b \rho) z _ {2} ^ {2}$$

选择 $k > b\rho + (1 + a)^{2}(a + b\rho)^{2}/4$

保证了原点是指数稳定的 $\Omega_{c}$ ，包含于吸引区内 $^{②}$ 。由于对任意 c>0，选择足够大的 k，前述不等式成立，因此反馈控制可实现半全局稳定。

例14.14 再次考虑例14.13中的系统

$$\dot {x} _ {1} = x _ {2} + \theta_ {1} x _ {1} \sin x _ {2}\dot {x} _ {2} = \theta_ {2} x _ {2} ^ {2} + x _ {1} + u$$

其中 $|\theta_1| \leqslant a, |\theta_2| \leqslant b$ 。例14.13中为满足线性增长不等式(14.67)，把分析限定在一个紧集中，因此只能实现半全局稳定。本例通过将反步法与李雅普诺夫再设计相结合，实现全局稳定。前面的分析与上例相同，本例从

$$\dot {V} _ {c} \leqslant - x _ {1} ^ {2} + z _ {2} [ x _ {1} + \psi_ {1} (x) + \psi_ {2} (x, \theta) + u ]$$

开始分析。在例14.13中，用 $u = -x_{1} - \psi_{1}(x) - kz_{2}$ 和高增益 $k$ 处理不确定项，这要求非

线性项 $x_{2}^{2}$ 以线性项 $\rho |x_2|$ 为界。本例取

$$u = - x _ {1} - \psi_ {1} (x) - k z _ {2} + v, \quad k > 0$$

其中，控制分量 $v$ 为待设计分量。则

$$\dot {V} _ {c} \leqslant - x _ {1} ^ {2} - k z _ {2} ^ {2} + z _ {2} [ \psi_ {2} (x, \theta) + v ]$$
