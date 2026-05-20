(e) 对系统 $\dot{x}_1 = -x_1 - x_2^3, \quad \dot{x}_2 = -x_2 - x_3^3 - u, \quad \dot{x}_3 = x_1^2 - x_3 + u, \quad y = x_2$

设计一个稳定输出反馈控制器。

14.48 考虑 p 输入 -p 输出系统 $\dot{x} = f(x, u)$ , $y = h(x)$

其中 f 是局部利普希茨的, h 连续可微, $f(0,0)=0$ , $h(0)=0$ 。假设系统

$$\dot {x} = f (x, u), \quad \dot {y} = \frac {\partial h}{\partial x} f (x, u) \stackrel {\mathrm{def}} {=} \tilde {h} (x, u)$$

是无源的, 输出为 $\dot{y}$ , 具有径向无界的正定存储函数 $V(x)$ , 即 $\dot{V} \leqslant u^{T} \dot{y}$ , 且是零状态可观测的。设 $z_{i}$ 是线性传递函数 $b_{i}s/(s + a_{i})$ 的输出, $y_{i}$ 为其输入, $a_{i}$ 和 $b_{i}$ 是正常数。

(a) 用 $V(x) + \sum_{i=1}^{p} (k_i / 2b_i) z_i^2$ 作为备选李雅普诺夫函数, 证明输出反馈控制律 $u_i = -k_i z_i$ , $1 \leqslant i \leqslant p$ , $k_i > 0$ , 使原点全局稳定。

(b) 用 $V(x) + \sum_{i=1}^{p} (1/b_i) \int_{0}^{z_i} \phi_i(\sigma)$ 作为备选李雅普诺夫函数, 其中 $\phi_i$ 是局部利普希茨函数, 满足 $\phi_i(0) = 0$ , 且对于所有 $\sigma \neq 0$ , 有 $\sigma \phi_i(\sigma) > 0$ 。证明输出反馈控制律 $u_i = -\phi_i(z_i), 1 \leqslant i \leqslant p$ , 使原点稳定。 $\phi_i$ 在什么条件下, 该控制律能够实现全局稳定?

(c) 将(a)中的结果用于角度 $\theta = \delta_{1}$ 处, 全局稳定单摆方程

$$m \ell \ddot {\theta} + m g \sin \theta = u$$

采用取自 $\theta$ ，而不是取自 $\dot{\theta}$ 的反馈。

14.49 考虑系统(14.85)\~(14.86)，并假设 $u = \gamma (x)$ 是局部利普希茨的状态反馈控制，使原点全局稳定。设 $\hat{x}$ 是由观测器(14.87)给出的状态估计。证明如果输入为 $v$ 的系统

$$\dot {x} = A x + g (C x, \gamma (x - v))$$

是输入-状态稳定的,则输出反馈控制律 $u = \gamma(\hat{x})$ 可全局稳定闭环系统(14.85)\~(14.86)的原点 $(x = 0, \hat{x} = 0)$ 。

14.50 验证当 $\varepsilon$ 足够小时, 14.5.3 节中的输出反馈控制器可重现状态反馈控制器的性能, 特别证明在输出反馈下闭环系统具有指数稳定平衡点 $(z, e_{0}, e, \hat{e}) = (0, \bar{e}_{0}, 0, 0)$ 。

下面七个习题给出了几个实例研究。

14.51 电流控制的感应电机模型为①

$$
\begin{array}{l} J \dot {\omega} = k _ {t} (\lambda_ {a} i _ {b} - \lambda_ {b} i _ {a}) - T _ {L} \\ \dot {\lambda} _ {a} = - \frac {R _ {r}}{L _ {r}} \lambda_ {a} - p \omega \lambda_ {b} + \frac {R _ {r} M}{L _ {r}} i _ {a} \\ \dot {\lambda} _ {b} = - \frac {R _ {r}}{L _ {r}} \lambda_ {b} + p \omega \lambda_ {a} + \frac {R _ {r} M}{L _ {r}} i _ {b} \\ \end{array}
$$
