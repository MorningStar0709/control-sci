# 9.5 最小二乘自校正调节器

我们的控制目的是设计一个控制器使系统的输出跟踪一个给定的信号。当系统的参数未知时，控制器中的未知参数若用在线最小二乘估计值代替，则相应的控制器称为最小二乘自校正调节器。

考虑下列单输入单输出 (SISO) 随机系统

$$A (z) y _ {n} = B (z) u _ {n - 1} + w _ {n}, \qquad n \geqslant 0, \tag {9.5.1}$$

其中 $\{y_{n}\}, \{u_{n}\}$ 和 $\{w_{n}\}$ 分别是系统的输出、输入及噪声过程（不失一般性，假设 $y_{n} = w_{n} = u_{n} = 0, \forall n < 0$ ），而 $A(z)$ 和 $B(z)$ 是后移算子 $z$ 的多项式

$$
\begin{array}{l} A (z) = 1 + a _ {1} z + \dots + a _ {p} z ^ {p}, \quad p \geqslant 0, \\ B (z) = b _ {1} + b _ {2} z + \dots + b _ {q} z ^ {q - 1}, \quad q \geqslant 1, \\ \end{array}
$$

其中 $a_{i}, b_{j}$ 是未知系数，而 $p$ 和 $q$ 是系统阶数的已知上界.

引入未知参数向量

$$\theta = \left[ - a _ {1} \dots - a _ {p}, b _ {1} \dots b _ {q} \right] ^ {\mathrm{T}} \tag {9.5.2}$$

及相应的回归向量

$$\varphi_ {n} = \left[ y _ {n} \dots y _ {n - p + 1}, u _ {n} \dots u _ {n - q + 1} \right] ^ {\mathrm{T}}, \tag {9.5.3}$$

则式 (9.5.1) 可简写为 9.2 节中讨论过的回归模型

$$y _ {n + 1} = \theta^ {\mathrm{T}} \varphi_ {n} + w _ {n + 1}, \quad n \geqslant 0. \tag {9.5.4}$$

控制目的是在任何时刻 n，基于量测数据 $\{y_{0}\cdots y_{n}, u_{0}\cdots u_{n-1}\}$ 构造出反馈控制量 $u_{n}$ ，使得下述平均跟踪误差渐近达到最小：

$$J _ {n} \stackrel {\text { def }} {=} \frac {1}{n} \sum_ {i = 1} ^ {n} (y _ {i} - y _ {i} ^ {*}) ^ {2}, \tag {9.5.5}$$

其中 $\{y_i^*\}$ 是已知的被跟踪信号.

为了分析上述控制问题，引入下列典型的条件：

(A1) 噪声 $\{w_{n},\mathcal{F}_{n}\}$ 是鞅差序列 (其中 $\{\mathcal{F}_n\}$ 是一非降的子 $\sigma-$ 代数序列), 并且存在 $\beta >2$ 使

$$\sup _ {n} E \left[ \left| w _ {n + 1} \right| ^ {\beta} \mid \mathcal {F} _ {n} \right] < \infty \quad \text { a.s. }; \tag {9.5.6}$$

(A2) $B(z) \neq 0, \forall z: |z| \leqslant 1$ (最小相位条件);

(A3) $\{y_n^*\}$ 是确定性有界信号.

值得指出，条件 (A2) 一般称为最小相位条件。对控制问题 (9.5.5) 来讲，它是保证最优闭环系统内部信号稳定的必要条件 [10].

我们先分析参数 $\theta$ 已知的情形。由于 $\{w_{n}\}$ 是不可预测的白噪声，易见使问题(9.5.5)达极小的控制律应满足

$$y _ {n + 1} ^ {*} = E \left[ y _ {n + 1} \mid \mathcal {F} _ {n} \right] \tag {9.5.7}$$

或根据式 (9.5.4) 及 (A1)

$$\theta^ {\mathrm{T}} \varphi_ {n} = y _ {n + 1} ^ {*}. \tag {9.5.8}$$

由此式可将最优控制明显表为

$$u _ {n} = \frac {1}{b _ {1}} \left\{a _ {1} y _ {n} + \dots + a _ {p} y _ {n - p + 1} - b _ {2} u _ {n - 1} - \dots - b _ {q} u _ {n - q + 1} + y _ {n + 1} ^ {*} \right\}. \tag {9.5.9}$$

将此式代入式 (9.5.1)(或将式 (9.5.8) 代入式 (9.5.4)) 可得到参数 $\theta$ 已知情形下的理想闭环方程为

$$y _ {n} - y _ {n} ^ {*} - w _ {n} \equiv 0, \quad \forall n \geqslant 0. \tag {9.5.10}$$

下面考虑参数 $\theta$ 未知的情形。这时，常用的方法是用9.2节中所讨论过的递推最小二乘(LS)来给出对 $\theta$ 的估计值 $\theta_{n}$
