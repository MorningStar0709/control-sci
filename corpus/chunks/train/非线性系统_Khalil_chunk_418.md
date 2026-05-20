$$
\begin{array}{l} \dot {\eta} = f _ {a} (\eta , \phi (\eta) + s) \\ \dot {s} _ {i} = \Delta_ {i} (t, x) - \frac {g _ {i} (x) \beta (x)}{\varepsilon} s _ {i}, 1 \leqslant i \leqslant p \\ \end{array}
$$

由(逆李雅普诺夫)定理4.14可知,存在李雅普诺夫函数 $V_{0}(\eta)$ ,在 $\eta=0$ 的某个邻域 $N_{\eta}$ 内满足

$$
\begin{array}{l} c _ {1} \| \eta \| _ {2} ^ {2} \leqslant V _ {0} (\eta) \leqslant c _ {2} \| \eta \| _ {2} ^ {2} \\ \frac {\partial V _ {0}}{\partial \eta} f _ {a} (\eta , \phi (\eta)) \leqslant - c _ {3} \| \eta \| _ {2} ^ {2} \\ \left\| \frac {\partial V _ {0}}{\partial \eta} \right\| _ {2} \leqslant c _ {4} \| \eta \| _ {2} \\ \end{array}
$$

由 $f_{a}$ 和 $\Delta$ 的光滑性，以及当 $|\Delta_i(t,x)|\leqslant g_i(x)\varrho (x)$ 时， $\varrho (0) = 0$ ，可得在 $(\eta ,\xi) = (0,0)$ 的某一邻域内，有

$$
\begin{array}{l} \left\| f _ {a} (\eta , \phi (\eta) + s) - f _ {a} (\eta , \phi (\eta)) \right\| _ {2} \leqslant k _ {1} \| s \| _ {2} \\ \| \Delta \| _ {2} \leqslant k _ {2} \| \eta \| _ {2} + k _ {3} \| s \| _ {2} \\ \end{array}
$$

选择足够小的 $\varepsilon$ 使 $\Omega_{\varepsilon} \subset N_{\eta}$ 和 $\Omega_{\varepsilon} \subset N$ 。利用李雅普诺夫函数

$$W = V _ {0} (\eta) + \frac {1}{2} \sum_ {i = 1} ^ {p} s _ {i} ^ {2}$$

可以证明 $\dot{W} \leqslant -c_{3}\| \eta \|_{2}^{2} + c_{4}k_{1}\| \eta \|_{2}\| s\|_{2} + k_{2}\| \eta \|_{2}\| s\|_{2} + k_{3}\| s\|_{2}^{2} - \frac{\beta_{0}g_{0}}{\varepsilon}\| s\|_{2}^{2}$

选择足够小的 $\varepsilon$ ，可使上式右边在 $\Omega_{\varepsilon}$ 内负定。证明的其余部分显而易见，在此省略。

上述证明的基本思想是,在边界层内,当 $\varepsilon$ 较小时,控制 $v_{i} = -\beta(x)s_{i}/\varepsilon$ 用做高增益反馈控制。通过选择足够小的 $\varepsilon$ ,高增益反馈可以稳定原点。似乎可以把高增益反馈控制用于整个空间,但在 s 远离零点时,控制幅度会过高。

前面强调了滑模控制对匹配的不确定性的鲁棒性,对于未匹配的不确定性,其鲁棒性如何呢?假设方程(14.1)修改为

$$\dot {x} = f (x) + B (x) [ G (x) E (x) u + \delta (t, x, u) ] + \delta_ {1} (x) \tag {14.18}$$

通过式(14.3)的变量代换,系统变为

$$
\begin{array}{l} \dot {\eta} = f _ {a} (\eta , \xi) + \delta_ {a} (\eta , \xi) \\ \dot {\xi} = f _ {b} (\eta , \xi) + G (x) E (x) u + \delta (t, x, u) + \delta_ {b} (\eta , \xi) \\ \end{array}
$$

其中 $\left[ \begin{array}{l}\delta_{a}\\ \delta_{b} \end{array} \right] = \frac{\partial T}{\partial x}\delta_{1}$

匹配不确定项 $\delta$ 加了一项 $\delta_{b}$ ，其作用只是改变 $\Delta_i / g_i$ 的上界。 $\delta_{a}$ 一项是未匹配的不确定项，它

在滑动流形上把降阶系统变为

$$\dot {\eta} = f _ {a} (\eta , \phi (\eta)) + \delta_ {a} (\eta , \phi (\eta))$$
