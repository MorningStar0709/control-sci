# 9.4 无限区间上解的连续性

在 3.2 节中讨论了状态方程的解对初始状态和参数的连续依赖性, 特别是定理 3.4, 在感兴趣的区域和在 $\|g(t,x)\|\leqslant\delta$ 条件下研究了标称系统

$$\dot {x} = f (t, x) \tag {9.26}$$

和扰动系统 $\dot{x}=f(t,x)+g(t,x)$ (9.27)

用 Gronwall-Bellman 不等式可以发现, 如果 $y(t)$ 和 $z(t)$ 分别是标称系统和扰动系统具有明确定义的解, 则

$$\| y (t) - z (t) \| \leqslant \| y (t _ {0}) - z (t _ {0}) \| \exp [ L (t - t _ {0}) ] + \frac {\delta}{L} \left\{\exp [ L (t - t _ {0}) ] - 1 \right\} \tag {9.28}$$

其中， $L$ 是 $f$ 的利普希茨常数。该边界仅在紧时间区间上成立，因为当 $t$ 趋于无穷时，指数项 $\exp[L(t - t_0)]$ 趋于无界。事实上，这个边界仅在一个时间区间 $[t_0, t_1]$ 上有效，这里 $t_1$ 要小得合理，因为对于 $t_1$ 很大的情况，边界将太大以至于没有任何作用。这并不奇怪，因为在3.2节中并没有对系统施加任何稳定性条件。在这一节中，要运用引理9.4计算方程(9.26)和方程(9.27)的两个解之间误差的边界，对于所有 $t \geqslant t_0$ ，该误差边界对于 $t$ 都是一致成立的。

定理9.1 设 $D \subset R^n$ 是包含原点的定义域, 并假设

\- 对于所有 $(t, x) \in [0, \infty) \times D_0$ 及每个紧集 $D_0 \subset D, f(t, x)$ 及其对 $x$ 的一阶偏导数对于 $x$ 是连续、有界且利普希茨的，对于 $t$ 是一致的；

\- $g(t,x)$ 对于 $t$ 分段连续，对于 $x$ 是局部利普希茨的，且有

$$\| g (t, x) \| \leqslant \delta , \forall (t, x) \in [ 0, \infty) \times D \tag {9.29}$$

\- 原点 $x = 0$ 是标称系统(9.26)的一个指数稳定平衡点；

\- 对于标称系统(9.26)，存在一个李雅普诺夫函数 $V(t,x)$ ，对于 $(t,x) \in [0,\infty) \times D$ 满足定理4.9的条件，且 $\{W_1(x) \leqslant c\}$ 是 $D$ 的一个紧子集。

设 $y(t)$ 和 $z(t)$ 分别表示标称系统(9.26)和扰动系统(9.27)的解，则对于每个紧集 $\Omega \subset \{W_2(x) \leqslant \rho c, 0 < \rho < 1\}$ ，存在与 $\delta$ 无关的正常数 $\beta, \gamma, \eta, \mu$ 和 $k$ ，使得如果 $y(t_0) \in \Omega, \delta < \eta$ 和 $\|z(t_0) - y(t_0) \| < \mu$ ，则对于所有 $t \geqslant t_0 \geqslant 0$ ，解 $y(t)$ 和 $z(t)$ 是一致有界的，且

$$\| z (t) - y (t) \| \leqslant k e ^ {- \gamma \left(t - t _ {0}\right)} \| z \left(t _ {0}\right) - y \left(t _ {0}\right) \| + \beta \delta \tag {9.30}$$

◇

当原点指数稳定时,要求李雅普诺夫函数 V 满足一致渐近稳定性的条件,而不是(更为严格的)指数稳定条件,这就给出了不太保守的集合 $\Omega$ 的估计值。当标称系统(9.26)是自治系统时,函数 V 由逆李雅普诺夫定理4.17确定,且集合 $\Omega$ 可以是吸引区的任意紧子集。指数稳定性只局部用于当误差 $z(t)-y(t)$ 充分小的情况。

证明： $V$ 沿扰动系统(9.27)轨线的导数，对于所有 $x\in \{W_1(x)\leqslant c\}$ 满足

$$\dot {V} = \frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x) + \frac {\partial V}{\partial x} g (t, x) \leqslant - W _ {3} (x) + k _ {1} \delta$$

其中 $k_{1}$ 是 $\partial V / \partial x$ 在 $\{W_1(x)\leqslant c\}$ 上的上界。设 $k_{2} > 0$ 是在紧集 $\Lambda = \{W_1(x)\leqslant c$ 和 $W_{2}(x) <   c\}$ 上 $W_{3}(x)$ 的极小值。则

$$\dot {V} \leqslant - \frac {1}{2} W _ {3} (x) - \frac {1}{2} k _ {2} + k _ {1} \delta \leqslant - \frac {1}{2} W _ {3} (x), \forall x \in \Lambda , \forall \delta \leqslant \frac {k _ {2}}{2 k _ {1}}$$
