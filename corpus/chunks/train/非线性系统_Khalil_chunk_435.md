# 14.2.2 非线性阻尼

重新考虑 $\delta(t, x, u) = \Gamma(t, x) \delta_0(t, x, u)$ 时的系统(14.30)，即

$$\dot {x} = f (t, x) + G (t, x) [ u + \Gamma (t, x) \delta_ {0} (t, x, u) ] \tag {14.47}$$

与前面一样,仍设 $f, G$ 已知, $\delta_0(t, x, u)$ 是不确定项, 函数 $\Gamma(t, x)$ 已知。假设对所有 $(t, x, u) \in [0, \infty) \times R^n \times R^p$ , $f, G, \Gamma$ 和 $\delta_0$ 对 $t$ 是分段连续的, 对 $x$ 和 $u$ 都是局部利普希茨的, 同时假设 $\delta_0$ 对所有 $(t, x, u)$ 是一致有界的。设 $\psi(t, x)$ 是一个标称稳定反馈控制律, 使标称闭环系统(14.32)的原点全局一致渐近稳定, 并且存在一个已知李雅普诺夫函数 $V(t, x)$ , 具有 $\mathcal{K}_{\infty}$ 类函数 $\alpha_1, \alpha_2$ 和 $\alpha_3$ , 对于所有 $(t, x) \in [0, \infty) \times R^n$ 满足式(14.33)和式(14.34)。如果 $\| \delta_0(t, x, u) \|$ 的上界已知, 就可以像前面那样设计控制分量 $v$ , 保证全局鲁棒稳定性。本节将证明即使 $\delta_0$ 的上界未知, 仍可设计出控制分量 $v$ , 保证闭环系统轨线的有界性。为此, 设 $u = \psi(t, x) + v$ , $V$ 沿闭环系统轨线的导数满足

$$\dot {V} = \frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} (f + G \psi) + \frac {\partial V}{\partial x} G (v + \Gamma \delta_ {0}) \leqslant - \alpha_ {3} (\| x \|) + w ^ {\mathrm{T}} (v + \Gamma \delta_ {0})$$

其中 $w^{\mathrm{T}} = [\partial V / \partial x]G$ 。取 $v = -kw\| \Gamma (t,x)\| _2^2,\quad k > 0$ (14.48)

可得 $\dot{V} \leqslant -\alpha_{3}(\|x\|) - k \|w\|_{2}^{2}\|\Gamma\|_{2}^{2} + \|w\|_{2}\|\Gamma\|_{2}k_{0}$

$k_{0}$ 是 $\| \delta_0\|$ 的(未知)上界,式中的

$$- k \| w \| _ {2} ^ {2} \| \Gamma \| _ {2} ^ {2} + \| w \| _ {2} \| \Gamma \| _ {2} k _ {0}$$

一项当 $\| w\| _2\| \Gamma \| _2 = k_0 / 2k$ 时，得最大值 $k_0^2 /4k$ ，因此有

$$\dot {V} \leqslant - \alpha_ {3} (\| x \| _ {2}) + \frac {k _ {0} ^ {2}}{4 k}$$

由于 $\alpha_{3}$ 为 $K_{\infty}$ 类函数, 因此 $\dot{V}$ 在某一球外总是负的, 根据定理 4.18, 对任意初始状态 $x(t_{0})$ , 闭环系统的解是一致有界的。李雅普诺夫再设计式 (14.48) 称为非线性阻尼, 下一个引理给出相应结论。

引理14.1 考虑系统(14.47)，并设 $\psi(t, x)$ 是标称系统(14.31)的稳定反馈控制，对于所有 $t \geqslant 0$ 和 $x \in R^n$ ，以及 $\mathcal{K}_{\infty}$ 类函数 $\alpha_{1}, \alpha_{2}$ 和 $\alpha_{3}$ ，系统的李雅普诺夫函数 $V(t, x)$ 满足式(14.33)和式(14.34)。假设不确定项 $\delta_{0}$ 对 $(t, x, u) \in [0, \infty) \times R^{n} \times R^{p}$ 是一致有界的，设 $v$ 由式(14.48)给出，并取 $u = \psi(t, x) + v$ ，则对于任意 $x(t_{0}) \in R^{n}$ ，闭环系统的解是一致有界的。

例14.7 考虑标量系统 $\dot{x} = x^{2} + u + x\delta_{0}(t)$

其中 $\delta_0(t)$ 是 $t$ 的有界函数，对于标称稳定控制 $\psi (x) = -x^{2} - x$ ，李雅普诺夫函数 $V(x) = x^{2}$ 在 $\alpha_{1}(r) = \alpha_{2}(r) = \alpha_{3}(r) = r^{2}$ 时，全局满足式(14.33)和式(14.34)。当 $k = 1$ 时，非线性阻尼分量(14.48)由 $v = -2x^{3}$ 给出，则无论有界扰动 $\delta_0$ 多大，由于存在非线性阻尼项

$-2x^{3}$ ，闭环系统

$$\dot {x} = - x - 2 x ^ {3} + x \delta_ {0} (t)$$

总存在有界解。

△
