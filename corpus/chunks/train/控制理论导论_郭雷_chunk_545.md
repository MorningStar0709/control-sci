$$
\begin{array}{l} \bar {P} (t) = \lim _ {t _ {f} \rightarrow + \infty} P (t; t _ {f}, 0) \\ = \lim _ {t _ {f} \rightarrow + \infty} P (t; \bar {t} _ {f}, P (\bar {t} _ {f}; t _ {f}, 0)) \\ = P (t; \bar {t} _ {f}, \lim _ {t _ {f} \rightarrow + \infty} P (\bar {t}; t _ {f}, 0)) \\ = P (t; \bar {t} _ {f}, \bar {P} (\bar {t} _ {f})) \geqslant 0, \quad \forall t \in [ t _ {0}, + \infty). \\ \end{array}
$$

上式表明 $\bar{P}(t)$ 是方程 (7.3.10) 中矩阵微分方程的非负定对称解矩阵.

定理7.3.2 对于线性控制系统(7.3.1). 如果系统(7.3.1)在每个时刻 $t \geqslant 0$ 都是完全能控的，则系统(7.3.1)在性能指标(7.3.19)下的最优控制存在唯一，且最优控制综合函数 $u(x, t)$ 为

$$u (x, t) = - R ^ {- 1} (t) B ^ {\mathrm{T}} (t) \bar {P} (t) x, \tag {7.3.22}$$

这里矩阵值函数 $\bar{P}(t)$ 由引理7.3.1中关系式(7.3.21)给出.

证明 对任一 $x_0 \in \mathbb{R}^n$ ，由假设知，最优控制问题 (7.3.1)，(7.3.19) 的容许控制集 $\mathcal{U}_{[t_0, +\infty)}$ 非空。不难证明最优控制的存在唯一性。下面证明式 (7.3.22) 中 $u(x,t)$ 是最优控制综合函数。事实上，将式 (7.3.22) 代入式 (7.3.1) 得到闭环系统

$$\dot {x} = A (t) x + B (t) u (x, t). \tag {7.3.23}$$

式 (7.3.23) 在 $t_0$ 时刻以 $x_0$ 为初态的轨线记为 $x(t)$ , 它在 $[t_0, +\infty)$ 确定. 记

$$u (t) = - R ^ {- 1} (t) B ^ {\mathrm{T}} (t) \bar {P} (t) x (t). \tag {7.3.24}$$

式 (7.3.19) 中相应于 $(u(t), x(t))$ 的性能指标值 $J[u; +\infty]$ 由下式规定：

$$
\begin{array}{l} J [ u; + \infty ] = \frac {1}{2} \int_ {t _ {0}} ^ {+ \infty} [ x ^ {\mathrm{T}} (t) Q (t) x (t) + u ^ {\mathrm{T}} (t) R (t) u (t) ] \mathrm{d} t \\ \stackrel {\text { def }} {=} \lim _ {t _ {f} \rightarrow + \infty} \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \left[ x ^ {\mathrm{T}} (t) Q (t) x (t) + u ^ {\mathrm{T}} (t) R (t) u (t) \right] \mathrm{d} t \\ = \lim _ {t _ {f} \rightarrow + \infty} J [ u; t _ {f} ]. \\ \end{array}
$$

不难看到 $J[u; +\infty] < \infty$ 。事实上，注意到 $u(t)$ 的表示式和 $\bar{P}(t)$ 满足方程 (7.3.10) 中 Riccati 方程，能够得到

$$\frac {\mathrm{d}}{\mathrm{d} t} \left(\frac {1}{2} x ^ {\mathrm{T}} (t) \bar {P} (t) x (t)\right) = - \frac {1}{2} \left(x ^ {\mathrm{T}} (t) Q (t) x (t) + u ^ {\mathrm{T}} (t) R (t) u (t)\right),$$

$\forall t_f \in [t_0, +\infty)$ , 从 $t_0$ 到 $t_f$ 积分上式得

$$\frac {1}{2} \left(x ^ {\mathbf {T}} (t _ {f}) \bar {P} (t _ {f}) x (t _ {f}) - x _ {0} ^ {\mathbf {T}} \bar {P} (t _ {0}) x _ {0}\right) = - J [ u; t _ {f} ],$$

由此可见

$$J [ u; t _ {f} ] \leqslant \frac {1}{2} x _ {0} ^ {\mathrm{T}} \tilde {P} (t _ {0}) x _ {0}.$$

于是我们有

$$J [ u; + \infty ] \leqslant \frac {1}{2} x _ {0} ^ {\mathrm{T}} \bar {P} (t _ {0}) x _ {0} < \infty . \tag {7.3.25}$$

另一方面，对任意固定 $t_f$ ，根据定理7.3.1，系统(7.3.1)\~(7.3.4)中的最优性能指标值 $J^{*}(x_{0},t_{0};t_{f})$ 为
