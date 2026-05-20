# 9.2 非零扰动

下面研究更为一般的情况,即不知道 $g(t,0)=0$ , 原点 x=0 可能不是扰动系统(9.1)的平衡点。此时不能再把原点作为一个平衡点研究其稳定性,也不应该期望在 t 趋于无穷时扰动系统的解趋于原点。如果扰动项 $g(t,x)$ 在某种意义上很小,则最好的结果是 $x(t)$ 毕竟有界,为一个小的边界。我们从标称系统(9.2)的原点是指数稳定的情况开始分析。

引理9.2 设 $x = 0$ 是标称系统(9.2)的一个指数稳定平衡点， $V(t, x)$ 是标称系统在 $[0, \infty) \times D$ 上满足式(9.3)至式(9.5)的一个李雅普诺夫函数，其中 $D = \{x \in R^n | \| x \| < r\}$ 。假设对于所有 $t \geqslant 0$ 和 $x \in D$ 及正常数 $\theta < 1$ ，扰动项 $g(t, x)$ 满足

$$\| g (t, x) \| \leqslant \delta < \frac {c _ {3}}{c _ {4}} \sqrt {\frac {c _ {1}}{c _ {2}}} \theta r \tag {9.10}$$

则对于所有 $\| x(t_0)\| < \sqrt{c_1 / c_2} r$ ，扰动系统(9.1)的解满足

$$\| x (t) \| \leqslant k \exp [ - \gamma (t - t _ {0}) ] \| x (t _ {0}) \|, \forall t _ {0} \leqslant t < t _ {0} + T$$

且对于某个有限的 T, 有

$$\| x (t) \| \leqslant b, \quad \forall t \geqslant t _ {0} + T$$

其中

$$k = \sqrt {\frac {c _ {2}}{c _ {1}}}, \quad \gamma = \frac {(1 - \theta) c _ {3}}{2 c _ {2}}, \quad b = \frac {c _ {4}}{c _ {3}} \sqrt {\frac {c _ {2}}{c _ {1}}} \frac {\delta}{\theta}$$

证明:用 $V(t,x)$ 作为扰动系统(9.1)的备选李雅普诺夫函数, $V(t,x)$ 沿系统(9.1)轨线的导数满足

$$
\begin{array}{l} \dot {V} (t, x) \leqslant - c _ {3} \| x \| ^ {2} + \left\| \frac {\partial V}{\partial x} \right\| \| g (t, x) \| \\ \leqslant - c _ {3} \| x \| ^ {2} + c _ {4} \delta \| x \| \\ = - (1 - \theta) c _ {3} \| x \| ^ {2} - \theta c _ {3} \| x \| ^ {2} + c _ {4} \delta \| x \|, 0 <   \theta <   1 \\ \leqslant - (1 - \theta) c _ {3} \| x \| ^ {2}, \forall \| x \| \geqslant \delta c _ {4} / \theta c _ {3} \\ \end{array}
$$

应用定理 4.18 和习题 4.51 即可完成证明。

注意引理9.2中的毕竟边界 $b$ 与扰动 $\delta$ 的上界成正比。可再次把这个结果看成在原点具有指数稳定平衡点的标称系统的鲁棒特性，因为它说明任意小(一致有界)的扰动不会导致与原点很大的稳态偏差。

例9.5 考虑二阶系统

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - 4 x _ {1} - 2 x _ {2} + \beta x _ {2} ^ {3} + d (t) \\ \end{array}
$$

其中， $\beta \geqslant 0$ 未知， $d(t)$ 是一致有界的扰动，对于所有 $t \geqslant 0$ 满足 $|d(t)| \leqslant \delta$ 。除了附加扰动条件 $d(t)$ 外，本例与例9.2研究的系统相同。同样，该系统可以看成李雅普诺夫函数为 $V(x) = x^{\mathrm{T}}Px$ 的标称线性系统的扰动，其中

$$
P = \left[ \begin{array}{l l} \frac {3}{2} & \frac {1}{8} \\ \frac {1}{8} & \frac {5}{1 6} \end{array} \right]
$$

用 $V(x)$ 作为扰动系统的备选李雅普诺夫函数，但是处理这两个扰动项 $\beta x_2^3$ 和 $d(t)$ 的方法不同，因为第一项在原点为零，而第二项不为零。计算 $V(x)$ 沿扰动系统轨线的导数，得

$$
\begin{array}{l} \dot {V} (t, x) = - \| x \| _ {2} ^ {2} + 2 \beta x _ {2} ^ {2} \left(\frac {1}{8} x _ {1} x _ {2} + \frac {5}{1 6} x _ {2} ^ {2}\right) + 2 d (t) \left(\frac {1}{8} x _ {1} + \frac {5}{1 6} x _ {2}\right) \\ \leqslant - \| x \| _ {2} ^ {2} + \frac {3}{4} \beta k _ {2} ^ {2} \| x \| _ {2} ^ {2} + \frac {\sqrt {2 9} \delta}{8} \| x \| _ {2} \\ \end{array}
$$
