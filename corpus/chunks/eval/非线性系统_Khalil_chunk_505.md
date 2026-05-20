因此在区间 $[0, T_2]$ 到达定义 $\tilde{V}(x)$ 的上确界。重复前面对 $g(x)$ 的讨论，可以证明 $\tilde{V}(x)$ 在 $H$ 上是利普希茨的。由于 $\tilde{V}(0) = 0$ ，由式(C.27)可得对于所有 $x \in R_A$ ， $\tilde{V}(x)$ 是连续的。

接下来证明 $\tilde{V}(x(t))$ 沿方程(C.13)的解是递减的。由于 $\tilde{V}(x)$ 只是局部利普希茨的，因此沿方程(C.13)的解的导数可由

$$\dot {\tilde {V}} (x) = \lim _ {h \rightarrow 0 ^ {+}} \sup \frac {1}{h} [ \tilde {V} (\phi (h; x)) - \tilde {V} (x) ] \tag {C.28}$$

计算。当 $x \neq 0$ 时，取 $r > \omega(x)$ ，根据 $\mathcal{KL}$ 类函数的性质，可找到定义在 $0 < \rho < \infty$ 和 $0 < r < \infty$ 上的函数 $\gamma_r(\rho)$ ，使得对于每个固定的 $r, \gamma_r(\rho)$ 对 $\rho$ 是连续递减的，而对于每个固定的 $\rho, \gamma_r(\rho)$ 对$r$ 是递增的，且对于所有 $0 < \rho < \infty$ ，有 $4\beta (r,\gamma_r(\rho))\leqslant \alpha^{-1}(\rho /2)$ 。设 $h_0$ 对于所有 $t\in [0,h_0]$ 满足 $\omega (\phi (t;x))\geqslant (1 / 2)\omega (x)$ ，并选取 $h\in [0,h_0]$ ，则

$$\tilde {V} (\phi (h; x)) = \sup _ {t \geqslant 0} \left\{g (\phi (t; \phi (h; x))) \frac {1 + 2 t}{1 + t} \right\} = \sup _ {t \geqslant 0} \left\{g (\phi (t + h; x)) \frac {1 + 2 t}{1 + t} \right\}$$

利用 $g(\phi (t + h;x))\frac{1 + 2t}{1 + t}\leqslant 2\omega (\phi (t + h;x))\leqslant 2\beta (\omega (x),t + h) <   2\beta (r,t + h)$

可看出对于所有 $t + h \geqslant \gamma_r(\omega(x))$ ，有

$$g (\phi (t + h; x)) \frac {1 + 2 t}{1 + t} \leqslant \frac {1}{2} \alpha^ {- 1} \left(\frac {1}{2} \omega (x)\right) \leqslant \frac {1}{2} \alpha^ {- 1} (\omega (\phi (h; x))) \leqslant \frac {1}{2} \tilde {V} (\phi (h; x))$$

因此在某个时刻 $t'$ 到达定义 $\tilde{V} (\phi (h;x))$ 的下确界，使得 $t' + h\leqslant \gamma_r(\omega (x))$ ，故

$$
\begin{array}{l} \tilde {V} (\phi (h; x)) = g \left(\phi \left(t ^ {\prime} + h; x\right)\right) \frac {1 + 2 t ^ {\prime}}{1 + t ^ {\prime}} \\ = g \left(\phi \left(t ^ {\prime} + h; x\right)\right) \frac {1 + 2 t ^ {\prime} + 2 h}{1 + t ^ {\prime} + h} \left[ 1 - \frac {h}{(1 + 2 t ^ {\prime} + 2 h) (1 + t ^ {\prime})} \right] \\ \leqslant \tilde {V} (x) \left[ 1 - \frac {h}{2 [ 1 + \gamma_ {r} (\omega (x) ] ^ {2}} \right] \\ \end{array}
$$

设定 $\eta_r(s) = \frac{\alpha^{-1}(s)}{2[1 + \gamma_r(s)]^2}$

当 $s > 0, \eta_r(0) = 0$ 时，容易验证 $\eta_r(s)$ 是 $\mathcal{K}_{\infty}$ 类函数，且

$$\dot {\tilde {V}} (x) \leqslant - \eta_ {r} (\omega (x))$$

由于前述不等式对于所有 $r > \omega(x)$ 成立, 因此对于 $\bar{\eta}(s) = \sup_{r > s} \eta_r(s)$ 也成立, 即对于所有 $x \neq 0$ , 有 $\dot{V}(x) \leqslant -\bar{\eta}(\omega(x))$ 。定义

$$\eta (s) = \int_ {2 s} ^ {2 s + 1} \eta_ {r} (s) d r$$

$s > 0$ ，且 $\eta (0) = 0$ ，则 $\eta (s)$ 是 $[0,\infty)$ 上的连续正定函数，且 $\eta (s)\leqslant \overline{\eta} (s)$ ，由此可得
