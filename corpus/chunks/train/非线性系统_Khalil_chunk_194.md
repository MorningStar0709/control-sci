# 6.4 $\mathcal{L}_2$ 稳定性和李雅普诺夫稳定性

本节将研究无源系统 $\dot{x} = f(x, u)$ (6.18)

$$y = h (x, u) \tag {6.19}$$

的 $L_{2}$ 稳定性和李雅普诺夫稳定性,其中 $f:R^{n}\times R^{p}\rightarrow R^{n}$ 是局部利普希茨的, $h:R^{n}\times R^{p}\rightarrow R^{p}$ 是连续的,且 $f(0,0)=0,h(0,0)=0$ 。

引理6.5 如果系统(6.18)\~(6.19)是严格输出无源的,且对于某个 $\delta > 0, u^{\mathrm{T}}y \geqslant \dot{V} + \delta y^{\mathrm{T}}y$ , 则系统是有限增益 $\mathcal{L}_2$ 稳定的,且其 $\mathcal{L}_2$ 增益小于或等于 $1 / \delta$ 。

证明:存储函数 $V(x)$ 的导数满足

$$
\begin{array}{l} \dot {V} \leqslant u ^ {\mathrm{T}} y - \delta y ^ {\mathrm{T}} y = - \frac {1}{2 \delta} (u - \delta y) ^ {\mathrm{T}} (u - \delta y) + \frac {1}{2 \delta} u ^ {\mathrm{T}} u - \frac {\delta}{2} y ^ {\mathrm{T}} y \\ \leqslant \frac {1}{2 \delta} u ^ {\mathrm{T}} u - \frac {\delta}{2} y ^ {\mathrm{T}} y \\ \end{array}
$$

两边在 $[0,\tau]$ 范围内积分,得

$$\int_ {0} ^ {\tau} y ^ {\mathrm{T}} (t) y (t) d t \leqslant \frac {1}{\delta^ {2}} \int_ {0} ^ {\tau} u ^ {\mathrm{T}} (t) u (t) d t - \frac {2}{\delta} [ V (x (\tau)) - V (x (0)) ]$$

因此有 $\| y_{\tau}\|_{\mathcal{L}_2}\leqslant \frac{1}{\delta}\| u_\tau \|_{\mathcal{L}_2} + \sqrt{\frac{2}{\delta} V(x(0))}$

其中用到 $V(x) \geqslant 0$ 和 $\sqrt{a^{2} + b^{2}} \leqslant a + b, a$ 和 b 是非负数。

□

引理6.6 如果系统(6.18)\~(6.19)是无源的,其正定存储函数为 $V(x)$ ,则 $\dot{x} = f(x,0)$ 的原点是稳定的。

证明: 取 V 作为 $\dot{x}=f(x,0)$ 的备选李雅普诺夫函数, 则 $\dot{V}\leqslant0$ 。

为证明 $\dot{x}=f(x,0)$ 在原点的渐近稳定性,需要证明 $\dot{V}$ 是负定的,或应用不变原理。在下面的引理中,我们通过考虑当 y=0 时 $\dot{V}=0$ 的情况应用不变原理,然后对 u=0 时方程(6.18)的所有解要求附加性质 $y(t)\equiv0\Rightarrow x(t)\equiv0$ (6.20)

同样,除平凡解 $x(t) \equiv 0$ 外, $\dot{x} = f(x,0)$ 的解都不可能保持在 $S = \{x \in R^{n} \mid h(x,0) = 0\}$ 内。式(6.20)的性质可以解释为可观测性条件。回顾线性系统

$$\dot {x} = A x, \quad y = C x$$

其可观测性等价于 $y(t) = Ce^{At}x(0)\equiv 0\Leftrightarrow x(0) = 0\Leftrightarrow x(t)\equiv 0$

为便于参考,定义式(6.20)为系统的一个可观测性性质。

定义6.5 对于系统(6.18)\~(6.19)，如果除平凡解 $x(t)\equiv 0$ 外，方程 $\dot{x} = f(x,0)$ 没有其他解能保持在 $S = \{x\in R^n\mid h(x,0) = 0\}$ 内，则该系统是零状态可观测的。

引理6.7 考虑系统(6.18)\~(6.19)，如果系统是严格无源的，或输出严格无源且零状态是可观测的，则 $\dot{x}=f(x,0)$ 的原点是渐近稳定的。此外，如果存储函数是径向无界的，则原点是全局渐近稳定的。

证明: 假设系统是严格无源的, 并设 $V(x)$ 是其存储函数。则 u=0 时, $\dot{V}$ 满足不等式 $\dot{V} \leqslant -\psi(x)$ , 这里 $\psi(x)$ 是正定的。我们可以利用这个不等式证明 $V(x)$ 是正定的。特别是对任意的 $x \in R^{n}$ , 方程 $\dot{x} = f(x, 0)$ 有一个解 $\phi(t; x)$ , 在 t=0 时刻始于 x 并定义在某个区间 $[0, \delta]$ 内。对于不等式 $\dot{V} \leqslant -\psi(x)$ , 两边积分得
