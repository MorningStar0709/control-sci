不等式(4.47)保证了对于任意有界输入 $u(t)$ ，状态 $x(t)$ 都有界。而且，随着 $t$ 增加，状态 $x(t)$ 是毕竟有界的，为 $\mathcal{K}$ 类函数 $\sup_{t\geqslant t_0}\| u(t)\|$ 。利用不等式(4.47)可证明如果 $u(t)$ 随t 趋于无穷而趋于零, 则 $x(t)$ 也随 t 趋于无穷而趋于零 $^{①}$ , 我们将其作为习题留给读者(见习题 4.58)。由于 $u(t) \equiv 0$ , 式 (4.47) 简化为

$$\| x (t) \| \leqslant \beta (\| x (t _ {0}) \|, t - t _ {0})$$

输入-状态稳定性是指无激励系统(4.45)的原点是全局一致渐近稳定的。输入-状态稳定性的概念是对初始状态和输入为任意大的全局情况定义的。习题4.60提出了这一概念的局部定义。

下面的类李雅普诺夫定理给出了输入-状态稳定性的一个充分条件②。

定理 4.19 设 $V:[0,\infty)\times R^{n}\rightarrow R$ 是连续可微函数, 满足

$$\alpha_ {1} (\| x \|) \leqslant V (t, x) \leqslant \alpha_ {2} (\| x \|) \tag {4.48}\frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x, u) \leqslant - W _ {3} (x), \forall \| x \| \geqslant \rho (\| u \|) > 0 \tag {4.49}$$

$\forall (t,x,u)\in [0,\infty)\times R^n\times R^m$ ，其中 $\alpha_{1}$ 和 $\alpha_{2}$ 是 $\mathcal{K}_{\infty}$ 类函数， $\rho$ 是 $\mathcal{K}$ 类函数， $W_{3}(x)$ 是 $R^n$ 上的连续正定函数。则系统(4.44)是输入-状态稳定的， $\gamma = \alpha_1^{-1}\circ \alpha_2\circ \rho$

证明:通过运用定理4.18的全局定义,发现解 $x(t)$ 存在且满足

$$\| x (t) \| \leqslant \beta (\| x (t _ {0}) \|, t - t _ {0}) + \gamma \left(\sup _ {\tau \geqslant t _ {0}} \| u (\tau) \|\right), \forall t \geqslant t _ {0} \tag {4.50}$$

由于当 $t_0 \leqslant \tau \leqslant t$ 时， $x(t)$ 仅取决于 $u(\tau)$ ，在 $[t_0, t]$ 上取式(4.50)右边的上确界，即得式(4.47) $^{③}$ 。

下一引理是关于全局指数稳定性(定理4.14)的逆李雅普诺夫定理的一个直接结果。

引理4.6 假设 $f(t, x, u)$ 对于 $(x, u)$ 是连续可微的，且是全局利普希茨的，对 $t$ 一致。如果无激励系统(4.45)在原点 $x = 0$ 处有全局指数稳定的平衡点，那么系统(4.44)是输入-状态稳定的。

证明:把系统(4.44)看成无激励系统(4.45)的扰动。逆李雅普诺夫定理4.14说明,无激励系统(4.45)有一个李雅普诺夫函数 $V(t,x)$ ，全局满足定理的各不等式。由于f的一致全局利普希茨性，扰动项对于所有 $t\geqslant t_{0}$ 和所有 $(x,u)$ 都满足式(4.46)。V关于系统(4.44)的导数满足

$$
\begin{array}{l} \dot {V} = \frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x, 0) + \frac {\partial V}{\partial x} [ f (t, x, u) - f (t, x, 0) ] \\ \leqslant - c _ {3} \| x \| ^ {2} + c _ {4} \| x \| L \| u \| \\ \end{array}
$$

对于较大的 $\| x\|$ ，为了用 $-c_{3}\| x\|^{2}$ 项控制 $c_{4}L\| x\| \| u\|$ 一项，把前面的不等式重写为

$$\dot {V} \leqslant - c _ {3} (1 - \theta) \| x \| ^ {2} - c _ {3} \theta \| x \| ^ {2} + c _ {4} L \| x \| \| u \|\| x (\sigma) \| \leqslant \beta (\| x (t _ {0}) \|, \sigma - t _ {0}) + \gamma \left(\sup _ {t _ {0} \leqslant \tau \leqslant T} \| u (\tau) \|\right), \forall t _ {0} \leqslant \sigma \leqslant T$$

则令, $\sigma=T=t_{0}$

其中 $0 < \theta < 1$ 。那么对于所有 $(t, x, u)$ ，有
