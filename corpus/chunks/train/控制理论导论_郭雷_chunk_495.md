此种情况对应的横截条件为 $\psi^{\mathrm{T}}(t_f) = -\mu^{\mathrm{T}}$

(2) 当 $k(x(t_f)) = 0, x(t_f)$ 的某些分量取固定值，而其余分量完全自由时，不妨令 $x(t_f)$ 的前 $m$ 个分量固定，后 $n - m$ 个分量完全自由。易知此种情况对应的横截条件为

$$\psi^ {\mathrm{T}} (t _ {f}) = [ - \mu_ {1}, - \mu_ {2}, \dots , - \mu_ {m}, \underbrace {0 , \cdots , 0} _ {n - m} ];$$

(3) 当 $k(x(t_f)) = 0$ ，且 $x(t_f)$ 的所有分量完全自由时，相应的横截条件为

$$\psi^ {\mathrm{T}} (t _ {f}) = 0.$$

下面讨论终端时刻 $t_f$ 待定情况下式 (7.1.1) 和式 (7.1.3) 的自由端点的最优控制问题。同样可通过引入 Lagrange 乘子向量值函数 $\psi(t)$ 化为求泛函 $J_3[u]$ 的极小问题，这里

$$J _ {3} [ u ] = k (x (t _ {f})) + \int_ {t _ {0}} ^ {t _ {f}} \left(l (x (t), u (t)) + \psi^ {\mathrm{T}} (t) (\dot {x} (t) - f (x (t), u (t)))\right) \mathrm{d} t. \tag {7.1.24}$$

此式与式 (7.1.5) 中 $J_{1}[u]$ 的唯一不同之处在于 $t_f$ 待定.

设 $u^{*}(t)$ 是式 (7.1.1) 和式 (7.1.3) 在 $t_f$ 自由和终端状态自由时的最优控制， $x^{*}(t)$ 是相应最优轨线， $t_f^{*}$ 为最优过渡时刻。取 $\varepsilon$ 为充分小的实数，令 $\delta u(t)$ 为定义在区间 $[t_0, t_f^* + \varepsilon \delta t]$ 上任意固定的分段连续 $r$ 维向量值函数，这里 $\delta t$ 是任意取定的实数。记

$$u (t) = u ^ {*} (t) + \varepsilon \delta u (t), \quad t \in [ t _ {0}, t _ {f} ^ {*} + \varepsilon \delta t ]. \tag {7.1.25}$$

易知 $u(\cdot) \in U_{[t_0, t_f]}$ , 这里 $t_f = t_f^* + \varepsilon \delta t$ , 且 (7.1.1) 对应于 $u(t)$ 的轨线 $x(t)$ 能表示为

$$x (t) = x ^ {*} (t) + \varepsilon \delta x (t) + \frac {\varepsilon^ {2}}{2} \delta^ {2} x (t) + o (\varepsilon^ {2}), \quad \forall t \in [ t _ {0}, t _ {f} ^ {*} + \varepsilon \delta t ], \tag {7.1.26}$$

其中 $\delta x(t)$ 满足方程 (7.1.9), $\delta^2 x(t)$ 由式 (7.1.10) 确定.

将式 (7.1.25), (7.1.26) 中的 $u(t)$ , $x(t)$ 代入 $J_{3}[u]$ , 并与 $J_{3}[u^{*}]$ 相减, 得到

$$
\begin{array}{l} \Delta J _ {3} = J _ {3} (\varepsilon) - J _ {3} (0) \stackrel {\text { def }} {=} J _ {3} [ u ] - J _ {3} [ u ^ {*} ] \\ = \varepsilon \delta J _ {3} [ u ^ {*} ] + \frac {\varepsilon^ {2}}{2} \delta^ {2} J _ {3} [ u ] + o (\varepsilon^ {2}), \tag {7.1.27} \\ \end{array}
$$

其中 $\delta J_{3}[u^{*}] \stackrel{\mathrm{def}}{=} J_{3}^{\prime}(0)$ 为 $J_{3}[u]$ 关于 $u^{*}(t)$ 的一次变分， $\delta^{2} J_{3}[u^{*}] \stackrel{\mathrm{def}}{=} J_{3}^{\prime \prime}(0)$ 为 $J_{3}[u]$ 关于 $u^{*}(t)$ 的二次变分，其表达式如下：
