# 2.4 稳定性

本节讨论微分方程解的稳定性问题，主要参考书为[4],[7],[9],[10],[13],[14],[16]等.

考察标准的一阶微分方程

$$\frac {\mathrm{d} x}{\mathrm{d} t} = f (t, x), \qquad x \in \mathbb {R} ^ {n} \tag {2.4.1}$$

的解的稳定性问题．这里记号 x, f 的意义与 2.2 中相同．假设 $f(\cdot,\cdot):[0,+\infty)\times\mathbb{R}^{n}\longrightarrow\mathbb{R}^{n}$ 是连续可微向量值函数，记为 $f(\cdot,\cdot)\in C(J\times\mathbb{R}^{n},\mathbb{R}^{n})$ .

下面先给出几个稳定性定义.

如果 $f(t, a) = 0, \forall t \geqslant 0$ , 则称 $x = a$ 为方程 (2.4.1) 的平衡解.

定义2.4.1 如果对于任意给定的正数 $\varepsilon$ ，存在正数 $\delta$ ，使当 $|x_0 - a| < \delta$ 时，微分方程(2.4.1)的以 $(0, x_0)$ 为初值的解 $\varphi(t; 0, x_0)$ 在区间 $0 \leqslant t < +\infty$ 上存在，并且满足不等式

$$| \varphi (t; 0, x _ {0}) - a | < \varepsilon , \qquad \forall t \geqslant 0, \tag {2.4.2}$$

则称方程 (2.4.1) 的平衡解 $x = a$ 是 (局部) 稳定的。否则，称微分方程 (2.4.1) 的平衡解 $x = a$ 是不稳定的。

定义2.4.2 如果微分方程(2.4.1)的平衡解 $x = a$ 是稳定的，并且存在正数 $\sigma$ ，使得当 $|x_0 - a| < \sigma$ 时，有

$$\lim _ {t \rightarrow + \infty} | \varphi (t; 0, x _ {0}) - a | = 0, \tag {2.4.3}$$

则称微分方程 (2.4.1) 的平衡解 $x = a$ 是 (局部) 渐近稳定的.

定义2.4.3 如果微分方程(2.4.1)的平衡解 $x = a$ 是稳定的，并且对一切 $x_0$ 有 $\lim_{t\to \infty}\varphi (t;0,x_0) = a,$ 则称方程(2.4.1)的平衡解是全局渐近稳定的.

定义2.4.4 对微分方程(2.4.1)的平衡解 $x = a$ ，如果存在 $\alpha > 0$ ，对任意给的 $\varepsilon > 0$ ，存在 $\delta(\varepsilon) > 0$ ，使得当 $|x_0 - a| < \delta(\varepsilon)$ 时成立

$$\left| \varphi (t; 0, x _ {0}) - a \right| \leqslant \varepsilon \mathrm{e} ^ {- \alpha t}, \quad \forall t \geqslant 0,$$

则称微分方程 (2.4.1) 的平衡解是指数稳定的.

如果对任意给定的 $\delta > 0$ , 存在 $\alpha = \alpha(\delta) > 0$ 及 $M = M(\delta) > 0$ , 使得当 $|x_0 - a| < \delta$ 时成立

$$\left| \varphi (t; 0, x _ {0}) - a \right| < M (\delta) \mathrm{e} ^ {- \alpha t}, \quad \forall t \geqslant 0,$$

则称微分方程 (2.4.1) 的平衡解 $x = a$ 是全局指数稳定的.

定义2.4.5 假设 $\varphi(t)$ 是微分方程(2.4.1)在区间 $0 \leqslant t < +\infty$ 上的一个解。如果对于任意给定的正数 $\varepsilon$ ，存在正数 $\delta > 0$ ，使得当 $|\varphi(0) - x_0| < \delta$ 时，微分方程(2.4.1)的解 $\varphi(t; 0, x_0)$ 在区间 $0 \leqslant t < +\infty$ 上存在，并且

$$\left| \varphi (t; 0, x _ {0}) - \varphi (t) \right| < \varepsilon , \quad \forall t \geqslant 0, \tag {2.4.4}$$

则称方程 (2.4.1) 的解 $\varphi(t)$ 是稳定的。否则，就称方程 (2.4.1) 的解 $\varphi(t)$ 是不稳定的。

定义2.4.6 如果微分方程(2.4.1)的解 $\varphi(t)$ 是稳定的，并且对一切满足不等式 $|x_0 - \varphi(0)| < \delta$ 的 $x_0$ ，相应的解 $\varphi(t;0,x_0)$ 满足

$$\lim _ {t \rightarrow + \infty} | \varphi (t; 0, x _ {0}) - \varphi (t) | = 0, \tag {2.4.5}$$

则称方程 (2.4.1) 的解 $\varphi(t)$ 是渐近稳定的.

例2.4.1 考察二维向量微分方程
