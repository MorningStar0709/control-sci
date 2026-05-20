$$x (t) = x (t _ {0}) \exp \left(\int_ {t _ {0}} ^ {t} \frac {- 1}{1 + \tau} d \tau\right) = x (t _ {0}) \frac {1 + t _ {0}}{1 + t}$$

由于 $|x(t)|\leqslant|x(t_{0})|,\forall t\geqslant t_{0}$ ，显然原点是稳定的。实际上，给定任意的 $\varepsilon>0$ ，可选择一个 $\delta$ 与 $t_{0}$ 无关，很明显

$$x (t) \to 0, \text {当} t \to \infty$$

因此，由定义4.1可知原点是渐近稳定的。但要注意， $x(t)$ 关于初始时间 $t_0$ 并不一致收敛于原点。回顾 $x(t)$ 收敛于原点的定义：给定任意 $\varepsilon > 0$ ，存在 $T = T(\varepsilon, t_0) > 0$ ，使对于所有 $t \geqslant t_0 + T$ ，都有 $|x(t)| < \varepsilon$ 。这一论述尽管对于每个 $t_0$ 都成立，但不能选择独立于 $t_0$ 的常数 $T$ 。

因此,需要改进定义4.1,以强调原点的稳定性与初始时间 $t_{0}$ 的关系,即我们所关心的改进定义是原点的稳定性和渐近稳定性对初始时刻的一致性①。

定义4.4 对于方程(4.15)的平衡点 $x = 0$

\- 如果对于每个 $\varepsilon > 0$ ，存在 $\delta = \delta(\varepsilon, t_0) > 0$ ，满足

$$\| x (t _ {0}) \| < \delta \Rightarrow \| x (t) \| < \varepsilon , \quad \forall t \geqslant t _ {0} \geqslant 0 \tag {4.16}$$

则平衡点是稳定的。

\- 如果对于每个 $\varepsilon > 0$ ，存在 $\delta = \delta(\varepsilon) > 0$ 与 $t_0$ 无关，且满足式(4.16)，则平衡点是一致稳定的。

\- 如果平衡点不稳定,那么它就是非稳定的。

\- 如果平衡点是稳定的,且存在一个正常数 $c = c(t_0)$ , 对于所有 $\|x(t_0)\| < c$ , 满足当 $t$ 趋于无穷时 $x(t)$ 趋于零, 则平衡点是渐近稳定的。

\- 如果它是一致稳定的,且存在独立于 $t_0$ 的正常数 $c$ , 满足对于所有 $\|x(t_0)\|<c, x(t)$ 趋于零, 当 $t$ 趋于无穷时 $x(t)$ 对 $t_0$ 一致趋于零。即, 对于每个 $\eta>0$ , 存在 $T=T(\eta)>0$ , 满足

$$\| x (t) \| < \eta , \quad \forall t \geqslant t _ {0} + T (\eta), \forall \| x \left(t _ {0}\right) \| < c \tag {4.17}$$

则平衡点是一致渐近稳定的。

\- 如果它是一致稳定的, 可选择一个 $\delta(\varepsilon)$ , 使 $\lim_{\varepsilon \to \infty} \delta(\varepsilon) = \infty$ , 并且对于每对正数 $\eta$ 和 $c$ , 存在 $T = T(\eta, c) > 0$ , 满足

$$\| x (t) \| < \eta , \quad \forall t \geqslant t _ {0} + T (\eta , c), \forall \| x (t _ {0}) \| < c \tag {4.18}$$

则平衡点是全局一致渐近稳定的。

下面的引理给出用K类函数和KL类函数定义的一致稳定性和一致渐近稳定性,与上述定义是等价的,且更为明确。

引理 4.5 对于方程(4.15)的平衡点 x=0,

\- 当且仅当存在一个 $\kappa$ 类函数 $\alpha$ 和独立于 $t_0$ 的正常数 $c$ , 满足

$$\| x (t) \| \leqslant \alpha \left(\| x \left(t _ {0}\right) \|\right), \quad \forall t \geqslant t _ {0} \geqslant 0, \forall \| x \left(t _ {0}\right) \| < c \tag {4.19}$$

时,平衡点是一致稳定的。

\- 当且仅当存在一个KL类函数 $\beta$ 和独立于 $t_0$ 的正常数 $c$ , 满足

$$\| x (t) \| \leqslant \beta (\| x \left(t _ {0}\right) \|, t - t _ {0}), \forall t \geqslant t _ {0} \geqslant 0, \forall \| x \left(t _ {0}\right) \| < c \tag {4.20}$$

时，平衡点是一致渐近稳定的。

\- 当且仅当不等式(4.20)对于任意初始状态 $x(t_0)$ 都成立时，平衡点是全局一致渐近稳定的。

证明: 见附录 C.6。

从引理 4.5 可以看出, 在自治系统中, 定义 4.1 对稳定性和渐近稳定性的每条定义都是指存在满足不等式(4.19)和不等式(4.20)的K类函数和KL类函数。这是因为对于自治系统, 原点的稳定性和原点的渐近稳定性对于初始时刻 $t_{0}$ 是一致的。
