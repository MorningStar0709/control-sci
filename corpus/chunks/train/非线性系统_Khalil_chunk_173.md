为应用引理5.1,需要检验 $\dot{x}=f(x)$ 原点的渐近稳定性。这个问题可以通过线性化或寻找一个李雅普诺夫函数加以解决。下面的引理说明,在一定条件下,可以用满足Hamilton-Jacobi不等式(5.28)的同一个函数V作为李雅普诺夫函数,以证明渐近稳定性。

引理5.2 假设定理5.5的假设条件在包含原点的定义域 $D \subset R^n$ 内满足， $f(x)$ 是连续可微的，且除了平凡解 $x(t) \equiv 0$ 外，方程 $\dot{x} = f(x)$ 在 $S = \{x \in D | h(x) = 0\}$ 内没有解。则 $\dot{x} = f(x)$ 的原点是渐近稳定的，且存在 $k_1 > 0$ ，使得对每个 $x_0, \| x_0 \| \leqslant k_1$ ，系统(5.26)～(5.27)是小信号有限增益 $\mathcal{L}_2$ 稳定的，其 $\mathcal{L}_2$ 增益小于或等于 $\gamma$ 。

证明: 取 $u(t) \equiv 0$ 。由式(5.28)有

$$\dot {V} (x) = \frac {\partial V}{\partial x} f (x) \leqslant - \frac {1}{2} h ^ {\mathrm{T}} (x) h (x), \forall x \in D \tag {5.37}$$

取 $r > 0$ 满足 $B_{r} = \{\| x\| \leqslant r\} \subset D$ 。下面证明 $V(x)$ 在 $B_{r}$ 内是正定的。为此，设 $\phi (t;x)$ 为方程 $\dot{x} = f(x)$ 始于 $\phi (0;x) = x\in B_r$ 内的解。由解的存在和唯一性（见定理3.1），以及解对于初始状态的连续依赖性（见定理3.4）可知，存在 $\delta >0$ ，使得对于每个 $x\in B_r$ ，解 $\phi (t;x)$ 对于所有 $t\in [0,\delta ]$ 都保持在 $D$ 内。对于 $\tau \leqslant \delta$ ，在 $[0,\tau ]$ 上对式(5.37)积分，有

$$V (\phi (\tau ; x)) - V (x) \leqslant - \frac {1}{2} \int_ {0} ^ {\tau} \| h (\phi (t; x)) \| _ {2} ^ {2} d t$$

由 $V(\phi (\tau ;x))\geqslant 0$ 得 $V(x)\geqslant \frac{1}{2}\int_0^\tau \| h(\phi (t;x))\| _2^2 dt$

现在假设存在 $\bar{x} \neq 0$ 使 $V(\bar{x}) = 0$ 。上述不等式隐含

$$\int_ {0} ^ {\tau} \| h (\phi (t; \bar {x})) \| _ {2} ^ {2} d t = 0, \forall \tau \in [ 0, \delta ] \Rightarrow h (\phi (t; \bar {x})) \equiv 0, \forall t \in [ 0, \delta ]$$

在此区间内，该解保持在 $S$ 内。由 $S$ 内的唯一解是平凡解的假设条件可得， $\phi(t; \bar{x}) \equiv 0 \Rightarrow \bar{x} = 0$ 。因此，在 $B_r$ 内 $V(x)$ 是正定的。用 $V(x)$ 作为 $\dot{x} = f(x)$ 的备选李雅普诺夫函数，由方程(5.37)和LaSalle不变性原理（见推论4.1），可得 $\dot{x} = f(x)$ 的原点是渐近稳定的。应用引理5.1即可完成证明。

例 5.12 将例 5.8 和例 5.9 的题目加以改变, 考虑系统

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - a \left(x _ {1} - \frac {1}{3} x _ {1} ^ {3}\right) - k x _ {2} + u \\ y = x _ {2} \\ \end{array}
$$

其中 $a > 0, k > 0$ 。函数 $V(x) = \alpha [a(x_1^2 / 2 - x_1^4 / 12) + x_2^2 / 2]$ 在集合 $\{|x_1| \leqslant \sqrt{6}\}$ 内是半正定的，其中 $\alpha > 0$ 。把 $V(x)$ 作为 Hamilton-Jacobi 不等式 (5.28) 的备选解，可以证明

$$\mathcal {H} (V, f, G, h, \gamma) = \left(- \alpha k + \frac {\alpha^ {2}}{2 \gamma^ {2}} + \frac {1}{2}\right) x _ {2} ^ {2}$$

重复例5.8中的证明，容易看出选择 $\alpha = \gamma = 1 / k$ ，不等式(5.28)对所有 $x\in R^2$ 成立。由于定理5.5的条件不是全局满足的，我们可以运用引理5.1研究小信号有限增益稳定性。这就需要证明无激励系统的原点是渐近稳定的，对系统在原点线性化并生成赫尔维茨矩阵即可做到。另一方面，也可以应用引理5.2，其条件在定义域 $D = \{|x_1| < \sqrt{3}\}$ 内满足，因为

$$x _ {2} (t) \equiv 0 \Rightarrow x _ {1} (t) [ 3 - x _ {1} ^ {2} (t) ] \equiv 0 \Rightarrow x _ {1} (t) \equiv 0$$

这样，可得出系统是小信号有限增益 $L_{2}$ 稳定的，且其 $L_{2}$ 增益小于或等于1/k。

△
