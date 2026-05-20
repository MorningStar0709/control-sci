# 6.1 $H_{\infty}$ 控制基本设计问题

考虑一个用传递函数阵 $G(s) \in RH_{\infty}^{n \times m}$ 来描述的线性定常系统，并记其输入输出信号分别为 $u \in \mathbb{R}^m$ 和 $y \in \mathbb{R}^n$ ，相应的 Laplace 变换为 $U(s)$ 和 $Y(s)$

$$Y (s) = G (s) U (s), \tag {6.1.1}$$

或者

$$y (t) = \mathcal {L} ^ {- 1} \{G (s) \} * u (t), \tag {6.1.2}$$

其中 $\mathcal{L}^{-1}\{\cdot\}$ 表示拉氏逆变换， $x(t)*y(t)$ 表示时域信号 $x(t)$ 和 $y(t)$ 的卷积。本章在不引起混淆的情况下，简记 $y = G(s)u$ 。

定义6.1.1 传递函数阵 $G(s) \in RH_{\infty}^{n \times m}$ 的 $H_{\infty}$ 范数定义如下：

$$\| G (\cdot) \| _ {\infty} = \sup _ {- \infty < \omega < + \infty} \bar {\sigma} \{G (\mathrm{j} \omega) \}, \tag {6.1.3}$$

其中 $\bar{\sigma}\{\cdot\}$ 表示复矩阵 $G(\mathrm{j}\omega)$ 的最大奇异值．对于标量系统，即 $n = m = 1$ 时，有

$$\| G (\cdot) \| _ {\infty} = \sup _ {- \infty < \omega < + \infty} | G (\mathrm{j} \omega) |. \tag {6.1.4}$$

对于线性系统来讲，所谓 $H_{\infty}$ 控制问题，就是以传递函数的 $H_{\infty}$ 范数来作为设计指标的控制问题。因此，为了有效地利用 $H_{\infty}$ 控制理论来解决实际工程问题，首先应该理解 $H_{\infty}$ 范数的特征。下面介绍 $H_{\infty}$ 范数的三个性质。

由于 $G(s) \in RH_{\infty}^{n \times m}$ 是在 $s$ 闭右半平面解析的有理函数阵，故对于 $u \in L^2(\mathbb{R}_+; \mathbb{R}^m)$ ，由式 (6.1.2) 有 $y \in L^2(\mathbb{R}_+; \mathbb{R}^n)$ 。这就意味着，任何一个稳定的线性系统都可以看做是输入信号空间 $L^2 (\mathbb{R}_+;\mathbb{R}^m)$ 到输出信号空间 $L^2 (\mathbb{R}_+;\mathbb{R}^n)$ 的一个算子．为简单起见，我们令 $L_{m}^{2} = L^{2}(\mathbb{R}_{+};\mathbb{R}^{m}),L_{n}^{2} = L^{2}(\mathbb{R}_{+};\mathbb{R}^{n})$ ，并且 $L_{m}^{2}$ 和 $L_{n}^{2}$ 中的范数都记作 $\| \cdot \| _2$ ，用算子 $\Gamma_G:L_m^2\to L_n^2$ 来表示传递函数阵为 $G(s)$ 的系统，并且用相应的诱导范数来作为该算子的范数．于是有如下结论：

引理6.1.1 设 $G(s) \in RH_{\infty}^{n \times m}$ , 则有

$$\| \Gamma_ {G} \| = \sup _ {u \neq 0, u \in L _ {m} ^ {2}} \frac {\| y \| _ {2}}{\| u \| _ {2}} = \| G (\cdot) \| _ {\infty}. \tag {6.1.5}$$

证明 根据 Parseval 恒等式可知， $\| u(\cdot)\|_2 = \| U(\cdot)\|_2, \| y(\cdot)\|_2 = \| Y(\cdot)\|_2$ 。所以有

$$
\begin{array}{l} \| y \| _ {2} ^ {2} = \| Y (\cdot) \| _ {2} ^ {2} = \frac {1}{2 \pi} \int_ {- \infty} ^ {+ \infty} \| G (\mathrm{j} \omega) U (\mathrm{j} \omega) \| ^ {2} \mathrm{d} \omega \\ \leqslant \frac {1}{2 \pi} \sup _ {\omega} \bar {\sigma} ^ {2} \{G (\mathrm{j} \omega) \} \int_ {- \infty} ^ {+ \infty} \| U (\mathrm{j} \omega) \| ^ {2} \mathrm{d} \omega \\ = \| G (\cdot) \| _ {\infty} ^ {2} \| u (\cdot) \| _ {2} ^ {2}. \\ \end{array}
$$

因此

$$\frac {\| y \| _ {2}}{\| u \| _ {2}} \leqslant \| G (\cdot) \| _ {\infty}, \quad \forall u \in L _ {m} ^ {2}. \tag {6.1.6}$$

下面我们证明上式右端是上确界．为叙述简便，只考虑 $G(s)$ 为标量的情况．考察标量信号
