$$\| \delta (t, x, \psi (t, x) + v) \| _ {\infty} \leqslant \rho (t, x) + \kappa_ {0} \| v \| _ {\infty}, \quad 0 \leqslant \kappa_ {0} < 1$$

我们有

$$w ^ {T} v + w ^ {T} \delta \leqslant w ^ {T} v + \| w \| _ {1} \| \delta \| _ {\infty} \leqslant w ^ {T} v + \| w \| _ {1} [ \rho (t, x) + \kappa_ {0} \| v \| _ {\infty} ]$$

选择

$$v = - \eta (t, x) \operatorname{sgn} (w) \tag {14.40}$$

其中，对于所有 $(t,x)\in [0,\infty)\times D,\eta (t,x)\geqslant \rho (t,x) / (1 - \kappa_0),\mathrm{sgn}(w)$ 是 $p$ 维向量，其第 $i$ 个元素为 $\mathrm{sgn}(\omega_i)$ ，则 $w^{\mathrm{T}}v + w^{\mathrm{T}}\delta \leqslant -\eta \| w\| _1 + \rho \| w\| _1 + \kappa_0\eta \| w\| _1$

$$
\begin{array}{l} = - \eta (1 - \kappa_ {0}) \| w \| _ {1} + \rho \| w \| _ {1} \\ \leqslant - \rho \| w \| _ {1} + \rho \| w \| _ {1} = 0 \\ \end{array}
$$

因此,对于控制(14.40), $V(t,x)$ 沿闭环系统(14.38)轨线的导数是负定的。注意,式(14.39)和式(14.40)给出的控制律对于单输入系统 $(p=1)$ 是相同的。

由式(14.39)和式(14.40)给出的控制律是状态 $x$ 的不连续函数, 这种不连续会引发一些理论及实际中的问题。理论上必须改变控制律以避免被零除, 此外由于反馈函数对 $x$ 不是局部利普希茨的, 因此还必须更仔细地检验解的存在性和唯一性。实际情况下, 这种不连续的控制器的实现表现出抖动现象, 即由于切换器件的非理想性或运算延迟, 控制会在切换面上出现快速的波动①。我们并不试图解决所有这些问题, 而是采用一种更为简便易行的方法, 即用一个连续控制律去逼近不连续控制律, 这种逼近的推导过程对上面两种控制律是类似的。因此, 我们只给出对控制律(14.39)的连续逼近, 对(14.40)连续逼近的推导参见习题 14.21 和习题 14.22。

考虑反馈控制律 $v=\left\{\begin{aligned}-\eta(t,x)(w/\|w\|_{2}),&\quad\eta(t,x)\|w\|_{2}\geqslant\varepsilon\\-\eta^{2}(t,x)(w/\varepsilon),&\quad\eta(t,x)\|w\|_{2}<\varepsilon\end{aligned}\right.$ (14.41)

对于(14.41)，只要 $\eta(t,x)\parallel w\parallel_{2}\geqslant\varepsilon$ ，则 V 沿闭环系统(14.38)轨线的导数就是负定的。因此，只需检验 $\eta(t,x)\parallel w\parallel_{2}<\varepsilon$ 时的 $\dot{V}$ ，此时

$$
\begin{array}{l} \dot {V} \leqslant - \alpha_ {3} (\| x \| _ {2}) + w ^ {\mathrm{T}} \left[ - \eta^ {2} \cdot \frac {w}{\varepsilon} + \delta \right] \\ \leqslant - \alpha_ {3} (\| x \| _ {2}) - \frac {\eta^ {2}}{\varepsilon} \| w \| _ {2} ^ {2} + \rho \| w \| _ {2} + \kappa_ {0} \| w \| _ {2} \| v \| _ {2} \\ = - \alpha_ {3} (\| x \| _ {2}) - \frac {\eta^ {2}}{\varepsilon} \| w \| _ {2} ^ {2} + \rho \| w \| _ {2} + \frac {\kappa_ {0} \eta^ {2}}{\varepsilon} \| w \| _ {2} ^ {2} \\ \leqslant - \alpha_ {3} (\| x \| _ {2}) + (1 - \kappa_ {0}) \left(- \frac {\eta^ {2}}{\varepsilon} \| w \| _ {2} ^ {2} + \eta \| w \| _ {2}\right) \\ \end{array}
$$

其中

$$- \frac {\eta^ {2}}{\varepsilon} \| w \| _ {2} ^ {2} + \eta \| w \| _ {2}$$

一项在 $\eta \| w\| _2 = \varepsilon /2$ 处有极大值 $\varepsilon /4$ ，因此只要 $\eta (t,x)\| w\| _2 <   \varepsilon$ ，就有
