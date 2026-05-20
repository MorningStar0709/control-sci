# 5.2 状态模型的 $\mathcal{L}$ 稳定性

输入-输出稳定性的概念极具直观性,这就使我们能够在有限输入-有限输出稳定性的框架下,引入动力学系统的稳定性概念。在李雅普诺夫稳定性中,着重研究了平衡点的稳定性和状态变量的渐近特性。读者或许有这样的疑问，从李雅普诺夫稳定性的形式体系看输入-输出稳定性，会有什么结论。本节将介绍如何用李雅普诺夫稳定性工具建立由状态模型表示的非线性系统的L稳定性。

考虑系统

$$\dot {x} = f (t, x, u), \quad x (0) = x _ {0} \tag {5.3}y = h (t, x, u) \tag {5.4}$$

其中 $x \in R^n, u \in R^m, y \in R^q, f: [0, \infty) \times D \times D_u \to R^n$ 是关于 $t$ 的分段连续函数，且是 $(x, u)$ 的局部利普希茨函数， $h: [0, \infty) \times D \times D_u \to R^q$ 是 $t$ 的分段连续函数，且是 $(x, u)$ 的连续函数， $D \subset R^n$ 是包含 $x = 0$ 的定义域， $D_u \subset R^m$ 是包含 $u = 0$ 的定义域。对于每个固定的 $x_0 \in D$ ，方程(5.3)和方程(5.4)给出的状态模式定义了一个算子 $H$ ，它对应每个输入信号 $u(t)$ 赋予相应的输出信号 $y(t)$ 。假设 $x = 0$ 是无激励系统

$$\dot {x} = f (t, x, 0) \tag {5.5}$$

的平衡点。本节讨论的主题是:如果方程(5.5)的原点是一致渐近稳定的(或指数稳定的),那么在f和h满足一定假设条件时,对于某一信号空间L,系统(5.3)\~(5.4)就是L稳定的或小信号L稳定的。下面先就指数稳定性进行讨论,然后推广到更为一般的一致渐近稳定性的情况。

定理5.1 考虑系统(5.3)\~(5.4)，取 $r > 0, r_u > 0$ ，使得 $\{\| x\| \leqslant r\} \subset D, \{\| u\| \leqslant r_u\} \subset D_u$ 。假设

\- $x = 0$ 是系统(5.5)的指数稳定平衡点,且存在李雅普诺夫函数 $V(t,x)$ ,对所有 $(t,x)\in [0,\infty)\times D$ 及正常数 $c_{1},c_{2},c_{3}$ 和 $c_{4}$ ,满足

$$c _ {1} \| x \| ^ {2} \leqslant V (t, x) \leqslant c _ {2} \| x \| ^ {2} \tag {5.6}\frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x, 0) \leqslant - c _ {3} \| x \| ^ {2} \tag {5.7}\left\| \frac {\partial V}{\partial x} \right\| \leqslant c _ {4} \| x \| \tag {5.8}$$

\- 对于所有 $(t, x, u) \in [0, \infty) \times D \times D_u$ 和非负常数 $L, \eta_1$ 和 $\eta_2, f$ 和 $h$ 满足不等式

$$\| f (t, x, u) - f (t, x, 0) \| \leqslant L \| u \| \tag {5.9}\| h (t, x, u) \| \leqslant \eta_ {1} \| x \| + \eta_ {2} \| u \| \tag {5.10}$$

则对满足 $\| x_0\| \leqslant r\sqrt{c_1 / c_2}$ 的每个 $x_0$ ，系统(5.3）\~（5.4）是小信号有限增益 $\mathcal{L}_p$ 稳定的， $p\in [1,\infty ]$ 。特别地，当每个 $u\in \mathcal{L}_{pe}$ 满足 $\sup_{0\leqslant t\leqslant \tau}\| u(t)\| \leqslant \min \{r_u,c_1c_3r / (c_2c_4L)\}$ 时，对于所有 $\tau \in [0,\infty)$ ，输出 $y(t)$ 满足

$$\left\| y _ {\tau} \right\| _ {\mathcal {L} _ {p}} \leqslant \gamma \left\| u _ {\tau} \right\| _ {\mathcal {L} _ {p}} + \beta \tag {5.11}$$

其中 $\gamma = \eta_{2} + \frac{\eta_{1}c_{2}c_{4}L}{c_{1}c_{3}},\beta = \eta_{1}\| x_{0}\| \sqrt{\frac{c_{2}}{c_{1}}}\rho ,$ 其中 $\rho = \left\{ \begin{array}{ll}1, & p = \infty \\ \left(\frac{2c_2}{c_3p}\right)^{1 / p}, & p\in [1,\infty) \end{array} \right.$
