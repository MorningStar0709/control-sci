# 11.3 无限区间上的奇异扰动

定理 11.1 仅适用于 $O(1)$ 的时间区间, 从定理的证明很容易理解这一点。具体来说, 式(C.81)证明了

$$\| x (t, \varepsilon) - \bar {x} (t) \| \leqslant \varepsilon k _ {3} [ 1 + t _ {1} - t _ {0} ] \exp [ L _ {6} (t _ {1} - t _ {0}) ]$$

对于任意有限的 $t_1$ ，上述的估计是 $O(\varepsilon)$ ，但是对于所有 $t \geqslant t_0$ ，它对 $t$ 又不是一致地为 $O(\varepsilon)$ 。为说明后者，需要证明

$$\| x (t, \varepsilon) - \bar {x} (t) \| \leqslant \varepsilon k, \quad \forall t \in [ t _ {0}, \infty)$$

上式附加一些稳定性条件可以成立。下面的定理要求降阶系统(11.5)在原点有一个指数稳定平衡点,并且通过李雅普诺夫函数估计其吸引区。

定理11.2 考虑奇异扰动问题(11.6)～(11.7)，并设 $z = h(t,x)$ 是方程(11.3)的孤立根。假设对于所有 $[t,x,z - h(t,x),\varepsilon ]\in [0,\infty)\times D_x\times D_y\times [0,\varepsilon_0]$

其中定义域 $D_{x} \subset R^{n}$ 和 $D_{y} \subset R^{m}$ 都包含各自相应的原点，有下述条件成立：

- 在 $D_{x} \times D_{y}$ 的任何紧子集上, 函数 $f$ 和 $g$ 及其关于 $(x, z, \varepsilon)$ 的一阶偏导数, 以及 $g$ 关于 $t$ 的一阶偏导数都是连续且有界的, 函数 $h(t, x)$ 和雅可比矩阵 $[\partial g(t, x, z, 0) / \partial z]$ 对其自变量的一阶偏导数有界, 且 $[\partial f(t, x, h(t, x), 0) / \partial x]$ 对于 $x$ 是利普希茨的, 对于 $t$ 是一致的, 初始数据 $\xi(\varepsilon)$ 和 $\eta(\varepsilon)$ 是 $\varepsilon$ 的光滑函数。  
- 原点是降阶系统(11.5)的指数稳定平衡点,对于 $(t,x)\in[0,\infty)\times D_{x}$ 存在李雅普诺夫函数 $V(t,x)$ 满足定理4.9的条件,且 $\{W_{1}(x)\leqslant c\}$ 是 $D_{x}$ 的一个紧子集。  
- 原点是边界层系统(11.14)的一个指数稳定平衡点,对于 $(t,x)$ 是一致的。设 $R_{y}\subset D_{y}$ 是方程(11.13)的吸引区,且 $\Omega_{y}$ 是 $R_{y}$ 的一个紧子集。

则对于每个紧集 $\Omega_x\subset \{W_2(x)\leqslant \rho c,0 < \rho < 1\}$ ，存在一个正常数 $\varepsilon^{*}$ ，使得对于所有 $t_0\geqslant 0$ $\xi_0\in \Omega_x,\eta_0 - h(t_0,\xi_0)\in \Omega_y$ 和 $0 <   \varepsilon <  \varepsilon^{*}$ ，奇异扰动问题(11.6）\~（11.7）在 $[t_0,\infty)$ 上有唯一解 $x(t,\varepsilon),z(t,\varepsilon)$ ，且当 $t\in [t_0,\infty)$ 时，

$$x (t, \varepsilon) - \bar {x} (t) = O (\varepsilon) \tag {11.23}z (t, \varepsilon) - h (t, \bar {x} (t)) - \hat {y} (t - t _ {0} / \varepsilon) = O (\varepsilon) \tag {11.24}$$

一致成立,其中 $\bar{x}(t)$ 和 $\hat{y}(\tau)$ 是降阶问题(11.8)和边界层问题(11.13)的解。此外对于任意给定 $t_{b}>t_{0}$ ，存在 $\varepsilon^{**}\leqslant\varepsilon^{*}$ ，使得对于 $t\in[t_{b},\infty)$ ，只要 $\varepsilon<\varepsilon^{**}$ ，则有

$$z (t, \varepsilon) - h (t, \bar {x} (t)) = O (\varepsilon) \tag {11.25}$$

一致成立。

◇

证明: 见附录 C.18。

□

如果降阶系统(11.5)是自治的,则定理11.2中的集合 $\Omega_{x}$ 可以是其吸引区的任何紧子集,这是由逆李雅普诺夫定理4.17得出的,它给出一个李雅普诺夫函数 $V(x)$ ,使得吸引区的任何紧子集都在紧集 $\{V(x)\leqslant c\}$ 内。

例 11.8 对于例 11.3 中的电路, 考虑奇异扰动问题
