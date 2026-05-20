$$
\begin{array}{l} \dot {E} _ {\lambda} (t) = \int_ {\partial \Omega} (\dot {y} + \lambda y) \frac {\partial y}{\partial \nu} \mathrm{d} \sigma - \int_ {\Omega} ((b - \lambda) | \dot {y} | ^ {2} + \lambda | \nabla y | ^ {2}) \mathrm{d} x \\ = - \int_ {\Omega} ((b - \lambda) | \dot {y} | ^ {2} + \lambda | \nabla y | ^ {2}) d x \stackrel {\text { def }} {=} - G _ {\lambda} (t). \\ \end{array}
$$

依据 Poincaré 不等式，存在常数 K > 0 使得

$$\int_ {\Omega} \varphi^ {2} \mathrm{d} x \leqslant K \int_ {\Omega} | \nabla \varphi | ^ {2} \mathrm{d} x, \quad \forall \varphi \in H _ {0} ^ {1} (\Omega).$$

于是对于任意 $\varepsilon > 0$ ，有

$$
\begin{array}{l} \lambda \int_ {\Omega} (2 y \dot {y} + b y ^ {2}) \mathrm{d} x \leqslant \varepsilon \lambda \int_ {\Omega} y ^ {2} \mathrm{d} x + \frac {\lambda}{\varepsilon} \int_ {\Omega} \dot {y} ^ {2} \mathrm{d} x + \lambda b _ {2} K \int_ {\Omega} | \nabla y | ^ {2} \mathrm{d} x \\ \leqslant K \lambda (\varepsilon + b _ {2}) \int_ {\Omega} | \nabla y | ^ {2} d x + \frac {\lambda}{\varepsilon} \int_ {\Omega} \dot {y} ^ {2} d x. \\ \end{array}
$$

现在令

$$\alpha_ {1} = \min \left\{1 - 2 \lambda / \varepsilon , 1 - 2 K \lambda (\varepsilon + b _ {2}) \right\},\alpha_ {2} = \min \left\{1 + 2 \lambda / \varepsilon , 1 + 2 K \lambda (\varepsilon + b _ {2}) \right\},\beta_ {1} = 2 \min \{\lambda , b _ {1} - \lambda \}, \quad \beta_ {2} = 2 \max \{\lambda , b _ {1} + \lambda \}.$$

设 $\lambda, \varepsilon$ 很小，并且 $\lambda / \varepsilon$ 也很小，使得 $\alpha_{1}, \alpha_{2}, \beta_{1}, \beta_{2}$ 均为正数。于是我们得到

$$\alpha_ {1} E (t) \leqslant E _ {\lambda} (t) \leqslant \alpha_ {2} E (t),\beta_ {1} E (t) \leqslant G _ {\lambda} (t) \leqslant \beta_ {2} E (t).$$

这样，从引理 10.4.2 可知，系统 (10.5.2) 指数衰减.

例10.5.2（波方程的耗散边界反馈镇定） 考虑带耗散边界反馈的波方程

$$\ddot {y} (x, t) - \Delta y (x, t) = 0, \quad x \in \Omega , t > 0, \tag {10.5.3}y (s, t) = 0, \quad [ s, t ] \in \Gamma_ {0} \times \mathbb {R}, \tag {10.5.4}\partial_ {\nu} y (s, t) = - \ell \dot {y} (s, t), \quad [ s, t ] \in \Gamma_ {1} \times \mathbb {R}, \tag {10.5.5}y (x, 0) = y _ {0} (x), \quad \dot {y} (x, 0) = y _ {1} (x), \quad x \in \Omega , \tag {10.5.6}$$

其中 $\Omega \subset \mathbb{R}^N$ 为具有充分光滑边界 $\Gamma$ 的有界开区域， $\nu$ 表示其边界 $\Gamma$ 上的外法向单位向量， $\partial_{\nu} = \partial / \partial \nu$ 为法向导数， $\Gamma_0, \Gamma_1$ 为 $\Gamma$ 的一分割，即满足 $\Gamma = \Gamma_0 \cup \Gamma_1, \Gamma_0 \cap \Gamma_1 = \varnothing$ ，假定 $\ell: \Gamma_1 \to \mathbb{R}$ 为 $C^\infty$ 函数，满足

$$\min _ {\Gamma_ {1}} \{\ell \} \geqslant M _ {1} > 0.$$
