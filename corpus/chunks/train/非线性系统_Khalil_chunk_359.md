# 12.4 线性化积分控制

本节首先设计状态反馈积分控制器,然后考虑输出反馈积分控制器。我们需要设计控制律 $u = \gamma(x, \sigma, e)$ ，以便在点 $(x_{\mathrm{ss}}, \sigma_{\mathrm{ss}})$ 稳定前面讨论的状态模型（12.18）～（12.19），其中 $u_{\mathrm{ss}} = \gamma(x_{\mathrm{ss}}, \sigma_{\mathrm{ss}}, 0)$ 。由于要用到线性化，故考虑形如

$$u = - K _ {1} x - K _ {2} \sigma - K _ {3} e \tag {12.20}$$

的线性反馈控制律。把控制律(12.20)代入式(12.18)和式(12.19)，可得到闭环系统

$$\dot {x} = f \left(x, - K _ {1} x - K _ {2} \sigma - K _ {3} (h (x, w) - r), w\right) \tag {12.21}\dot {\sigma} = h (x, w) - r \tag {12.22}$$

方程(12.21)和方程(12.22)的平衡点 $(\bar{x},\bar{\sigma})$ 满足方程

$$0 = f (\bar {x}, \bar {u}, w)0 = h (\bar {x}, w) - r\bar {u} = - K _ {1} \bar {x} - K _ {2} \bar {\sigma}$$

通过假设平衡方程(12.16)\~(12.17)在我们希望的区域内有唯一解 $(x_{ss},u_{ss})$ ，可推出 $\bar{x}=x_{ss}$ 和 $\bar{u}=u_{ss}$ 。选择 $K_{2}$ 为非奇异的，可保证方程

$$u _ {\mathrm{ss}} = - K _ {1} x _ {\mathrm{ss}} - K _ {2} \sigma_ {\mathrm{ss}}$$

有唯一解 $\sigma_{ss}$ 。下面的任务是稳定平衡点 $(x_{\mathrm{ss}}, \sigma_{\mathrm{ss}})$ 。在 $(x_{\mathrm{ss}}, \sigma_{\mathrm{ss}})$ 对闭环系统 (12.21) \~ (12.22) 线性化，得

$$\dot {\xi} _ {\delta} = (\mathcal {A} - \mathcal {B K}) \xi_ {\delta}$$

其中 $\xi_{\delta} = \left[ \begin{array}{l}x - x_{\mathrm{ss}}\\ \sigma -\sigma_{\mathrm{ss}} \end{array} \right],\quad \mathcal{A} = \left[ \begin{array}{ll}A & 0\\ C & 0 \end{array} \right],\quad \mathcal{B} = \left[ \begin{array}{ll}B\\ 0 \end{array} \right],\quad \mathcal{K} = \left[ \begin{array}{ll}K_1 + K_3C & K_2 \end{array} \right]$

$$A = \left. \frac {\partial f}{\partial x} (x, u, w) \right| _ {x = x _ {\mathrm{ss}}, u = u _ {\mathrm{ss}}}, \quad B = \left. \frac {\partial f}{\partial u} (x, u, w) \right| _ {x = x _ {\mathrm{ss}}, u = u _ {\mathrm{ss}}}, \quad C = \left. \frac {\partial h}{\partial x} (x, w) \right| _ {x = x _ {\mathrm{ss}}}$$

矩阵 A, B 和 C 一般取决于 v。现在假设 $(A, B)$ 是可控的（或可稳定的），并且 $^{①}$

$$
\operatorname{rank} \left[ \begin{array}{l l} A & B \\ C & 0 \end{array} \right] = n + p \tag {12.23}
$$

那么 $(\mathcal{A},\mathcal{B})$ 也是可控的(或可稳定的)②。设计与 $w$ 无关的 $\mathcal{K}$ ，使得 $\mathcal{A} - \mathcal{B}\mathcal{K}$ 对于所有 $v\in D_v$ 都是赫尔维茨矩阵③，对于任何此类设计，矩阵 $K_{2}$ 都将是非奇异的④。这样， $(x_{\mathrm{ss}},\sigma_{\mathrm{ss}})$ 就是闭环系统(12.21)\~(12.22)的指数稳定平衡点,并且所有始于吸引区内的解,都随t趋于无穷而逼近该平衡点。因此,当t趋于无穷时, $y(t)-r$ 趋于零。注意,在 $(x_{\mathrm{ss}},u_{\mathrm{ss}})$ 的稳定中可取 $K_{3}=0$ ,或者可以用它作为一个额外的自由度来提高性能。

总之,假设 $(A,B)$ 是稳定的,且满足秩条件(12.23),则状态反馈控制可取为
