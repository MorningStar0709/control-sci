$$\dot {V} \leqslant - \alpha_ {3} (\| x \| _ {2}) + \frac {\varepsilon (1 - \kappa_ {0})}{4}$$

另一方面，当 $\eta (t,x)\parallel w\parallel_{2}\geqslant \varepsilon$ 时， $\dot{V}$ 满足

$$\dot {V} \leqslant - \alpha_ {3} (\| x \| _ {2}) \leqslant - \alpha_ {3} (\| x \| _ {2}) + \frac {\varepsilon (1 - \kappa_ {0})}{4}$$

这样,无论 $\eta(t,x)\parallel w\parallel_{2}$ 为何值,不等式

$$\dot {V} \leqslant - \alpha_ {3} (\| x \| _ {2}) + \frac {\varepsilon (1 - \kappa_ {0})}{4}$$

都成立。取 $r > 0$ ，使 $B_{r}\subset D$ ，选择 $\varepsilon < 2\alpha_{3}(\alpha_{2}^{-1}(\alpha_{1}(r)) / (1 - \kappa_{0})$ ，并设 $\mu = \alpha_3^{-1}(\varepsilon (1 - \kappa_0) / 2)$ $<  \alpha_{2}^{-1}(\alpha_{1}(r))$ ，则

$$\dot {V} \leqslant - \frac {1}{2} \alpha_ {3} (\| x \| _ {2}), \quad \forall \mu \leqslant \| x \| _ {2} < r$$

运用定理 4.18 可推出下面的定理,该定理说明闭环系统的解是一致毕竟有界的,其最终边界是 $\varepsilon$ 的 K 类函数。

定理14.3 考虑系统(14.30)，设 $D \subset R^n$ 是包含原点的定义域，且 $B_r = \{\|x\|_2 \leqslant r\} \subset D, \psi(t,x)$ 是标称系统(14.31)的稳定反馈控制律，其李雅普诺夫函数 $V(t,x)$ 在2范数下对于所有 $t \geqslant 0$ 和 $x \in D$ 满足式(14.33)和式(14.34)，该系统还具有 $\kappa$ 类函数 $\alpha_1, \alpha_2$ 和 $\alpha_3$ 。假设不确定项 $\delta$ 对于所有 $t \geqslant 0$ 和 $x \in D$ ，在2范数下满足式(14.35)。设 $v$ 由式(14.41)给出，并选择 $\varepsilon < 2\alpha_3(\alpha_2^{-1}(\alpha_1(r))) / (1 - \kappa_0)$ ，则对于任意 $\|x(t_0)\|_2 < \alpha_2^{-1}(\alpha_1(r))$ ，总存在一个有限时间 $t_1$ ，使闭环系统(14.38)的解满足

$$\left\| x (t) \right\| _ {2} \leqslant \beta \left(\left\| x \left(t _ {0}\right) \right\| _ {2}, t - t _ {0}\right), \quad \forall t _ {0} \leqslant t < t _ {1} \tag {14.42}\| x (t) \| _ {2} \leqslant b (\varepsilon), \quad \forall t \geqslant t _ {1} \tag {14.43}$$

其中， $\beta$ 为 $\kappa L$ 类函数， $b$ 为 $\kappa$ 类函数，其定义为

$$b (\varepsilon) = \alpha_ {1} ^ {- 1} (\alpha_ {2} (\mu)) = \alpha_ {1} ^ {- 1} (\alpha_ {2} (\alpha_ {3} ^ {- 1} (\varepsilon (1 - \kappa_ {0}) / 2)))$$

如果所有假设都全局成立，且 $\alpha_{1}$ 属于 $K_{\infty}$ 类函数，则式(14.42)和式(14.43)对任何初态 $x(t_{0})$ 都成立。
