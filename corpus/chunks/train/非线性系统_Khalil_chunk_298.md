# 10.2 无限区间上的扰动

再附加一些稳定条件,定理10.1的扰动结果可以扩展到无限时间区间 $\left[t_{0},\infty\right)$ 。在下面的定理中,要求标称系统(10.7)在原点有一个指数稳定平衡点,并应用李雅普诺夫函数估计其吸引区。为不失一般性,把原点作为平衡点,因为任何平衡点都可以通过变量代换移至原点。

定理10.2 设 $D \subset R^n$ 是包含原点的定义域, 并假设

- 对于每个紧集 $D_0 \subset D$ 以及 $(t, x, \varepsilon) \in [0, \infty) \times D_0 \times [-\varepsilon_0, \varepsilon_0]$ , $f$ 及其对 $(x, \varepsilon)$ 的直到 $N$ 阶偏导数连续且有界; 如果 $N = 1$ , $[\partial f / \partial x](t, x, \varepsilon)$ 对 $(x, \varepsilon)$ 是利普希茨的, 对 $t$ 是一致的;  
- 对 $\varepsilon \in [-\varepsilon_0, \varepsilon_0]$ , $\eta$ 及其直到 $N$ 阶导数连续；  
- 原点是标称系统(10.7)的一个指数稳定平衡点；  
- 对于 $(t, x) \in [0, \infty) \times D$ , 标称系统(10.7)存在李雅普诺夫函数 $V(t, x)$ , 满足定理 4.9 的条件, 且 $\{W_1(x) \leqslant c\}$ 是 $D$ 的一个紧子集。

则对于每个紧集 $\Omega \subset \{W_2(x) \leqslant \rho c, 0 < \rho < 1\}$ , 存在正常数 $\varepsilon^*$ , 使得对于所有 $t_0 \geqslant 0, \eta_0 \in \Omega$ 和 $|\varepsilon| < \varepsilon^*$ , 方程(10.1)和方程(10.2)有唯一解 $x(t, \varepsilon)$ , 该解在 $[t_0, \infty)$ 上一致有界, 且有

$$x (t, \varepsilon) - \sum_ {k = 0} ^ {N - 1} x _ {k} (t) \varepsilon^ {k} = O (\varepsilon^ {N})$$

其中， $O(\varepsilon^{N})$ 在 $t$ 上对于所有 $t\geqslant t_0$ 一致成立。

如果标称系统(10.7)是自治系统,则定理10.2中的集合 $\Omega$ 可以是原点吸引区的任何紧子集。这是由(逆李雅普诺夫)定理4.17得出的,因为由该定理给出的李雅普诺夫函数 $V(x)$ 有这样一种性质,即吸引区的任何紧子集都可以包含在紧集 $\{V(x) \leqslant c\}$ 内。

证明:应用定理9.1可证明,存在 $\varepsilon_{1}>0$ ,使得对于所有 $|\varepsilon|<\varepsilon_{1},x(t,\varepsilon)$ 是一致有界的,且 $x(t,\varepsilon)-x_{0}(t)$ 为 $O(\varepsilon)$ ,对于所有 $t\geqslant t_{0}$ ,对t一致。显然,对于 $\eta_{0}\in\Omega,x_{0}(t)$ 是一致有界的,且 $\lim_{t\to\infty}x_{0}(t)=0$ 。考虑线性方程(10.8),由有界输入-有界输出稳定性(见定理5.1)可知,如果 $\dot{z}=A(t)z$ 是指数稳定的且输入 $g_{k}$ 有界,则方程(10.8)的解是一致有界的。输入 $g_{k}$ 是关于 $x_{1},\cdots,x_{k-1}$ 的多项式,其系数取决于t和 $x_{0}(t)$ 。对于t的依赖性来自f的偏导数,它在D的紧子集上是有界的。由于 $x_{0}(t)$ 和多项式的系数对于所有 $t\geqslant t_{0}$ 有界,因此 $g_{k}$ 的边界可根据 $x_{1},\cdots,x_{k-1}$ 的边界得出。矩阵 $A(t)$ 由下式给出:

$$A (t) = \frac {\partial f}{\partial x} (t, x _ {0} (t), 0)$$

其中， $x_0(t)$ 是标称系统(10.7)的解。这说明作为方程(10.7)的平衡点，原点的指数稳定性保证了 $\dot{z} = A(t)z$ 的原点对于每个始于集合 $\Omega$ 的解 $x_0(t)$ 将是指数稳定的。为了理解这一点，设

$$A _ {0} (t) = \frac {\partial f}{\partial x} (t, 0, 0)$$

并写出 $A(t) = A_0(t) + [A(t) - A_0(t)] \stackrel{\mathrm{def}}{=} A_0(t) + B(t)$

所以线性系统 $\dot{z} = A(t)z$ 可以看成 $\dot{y} = A_0(t)y$ 的一个线性扰动。由于 $[\partial f / \partial x](t,x,0)$ 对于 $x$ 是利普希茨的，对于 $t$ 是一致的，故有
