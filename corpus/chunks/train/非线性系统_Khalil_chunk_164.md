此外,如果原点是全局指数稳定的,且所有假设都全局成立 $(D=R^{n},D_{u}=R^{m})$ ,则对每个 $x_{0}\in R^{n}$ ,系统(5.3)\~(5.4)为有限增益 $L_{p}$ 稳定的, $p\in[1,\infty]$ 。

证明: V 沿系统(5.3)轨线的导数满足

$$
\begin{array}{l} \dot {V} (t, x, u) = \frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x, 0) + \frac {\partial V}{\partial x} [ f (t, x, u) - f (t, x, 0) ] \\ \leqslant - c _ {3} \| x \| ^ {2} + c _ {4} L \| x \| \| u \| \\ \end{array}
$$

取 $W(t) = \sqrt{V(t,x(t))}$ ，当 $V(t,x(t))\neq 0$ 时，由 $\dot{W} = \dot{V} /(2\sqrt{V})$ 和式(5.6)得

$$\dot {W} \leqslant - \frac {1}{2} \left(\frac {c _ {3}}{c _ {2}}\right) W + \frac {c _ {4} L}{2 \sqrt {c _ {1}}} \| u (t) \|$$

当 $V(t,x(t))=0$ 时,可以验证 $^{①}$

$$D ^ {+} W (t) \leqslant \frac {c _ {4} L}{2 \sqrt {c _ {1}}} \| u (t) \| \tag {5.12}$$

因此,对于所有 $V(t,x(t))$ 的值,有

$$D ^ {+} W (t) \leqslant - \frac {1}{2} \left(\frac {c _ {3}}{c _ {2}}\right) W + \frac {c _ {4} L}{2 \sqrt {c _ {1}}} \| u (t) \|$$

由(比较)引理3.4可知, $W(t)$ 满足不等式

$$W (t) \leqslant e ^ {- t c _ {3} / 2 c _ {2}} W (0) + \frac {c _ {4} L}{2 c _ {1}} \int_ {0} ^ {t} e ^ {- (t - \tau) c _ {3} / 2 c _ {2}} \| u (\tau) \| d \tau$$

由式(5.6)得 $W(t)\leqslant e^{-tc_3 / 2c_2}W(0) + \frac{c_4L}{2c_1}\int_0^t e^{-(t - \tau)c_3 / 2c_2}\| u(\tau)\| d\tau$

容易验证 $\|x_{0}\|\leqslant r\sqrt{\frac{c_{1}}{c_{2}}}$ ， $\sup_{0\leqslant\sigma\leqslant t}\|u(\sigma)\|\leqslant\frac{c_{1}c_{3}r}{c_{2}c_{4}L}$

保证 $\| x(t)\| \leqslant r$ ；因此， $x(t)$ 在假设的定义域内。由式(5.10)，有

$$\| y (t) \| \leqslant k _ {1} e ^ {- a t} + k _ {2} \int_ {0} ^ {t} e ^ {- a (t - \tau)} \| u (\tau) \| d \tau + k _ {3} \| u (t) \| \tag {5.13}$$

其中 $k_{1} = \sqrt{\frac{c_{2}}{c_{1}}}\| x_{0}\| \eta_{1}, k_{2} = \frac{c_{4}L\eta_{1}}{2c_{1}}, k_{3} = \eta_{2}, a = \frac{c_{3}}{2c_{2}}$

设定 $y_{1}(t) = k_{1}e^{-at}, y_{2}(t) = k_{2}\int_{0}^{t}e^{-a(t - \tau)}\| u(\tau)\| d\tau ,y_{3}(t) = k_{3}\| u(t)\|$

现在假设 $u \in \mathcal{L}_{pe}^{m}, p \in [1, \infty]$ ，由例5.2的结果可容易验证

$$\left\| y _ {2 \tau} \right\| _ {\mathcal {L} _ {p}} \leqslant \frac {k _ {2}}{a} \left\| u _ {\tau} \right\| _ {\mathcal {L} _ {p}}$$

显见 $\| y_{3\tau}\|_{\mathcal{L}_p}\leqslant k_3\| u_\tau \| \mathcal{L}_p$

对于首项 $y_{1}(t)$ ，可以证明

$\| y_{1\tau}\|_{\mathcal{L}_p}\leqslant k_1\rho ,\quad \text{其中} \quad \rho = \left\{ \begin{array}{ll}1, & p = \infty \\ \left(\frac{1}{ap}\right)^{1 / p}, & p\in [1,\infty) \end{array} \right.$

这样,由三角不等式可知,当 $\gamma = k_{3} + \frac{k_{2}}{a}, \quad \beta = k_{1}\rho$
