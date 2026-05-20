其中用到不等式 $|2x_{1} + 5x_{2}| \leqslant \| x\|_{2}\sqrt{4 + 25}$

及 $k_{2}$ 为 $\left|x_{2}\right|$ 的上界。假设 $\beta \leqslant 4(1 - \zeta) / 3k_2^2$ ，其中 $0 < \zeta < 1$ ，则

$$\dot {V} (t, x) \leqslant - \zeta \| x \| _ {2} ^ {2} + \frac {\sqrt {2 9} \delta}{8} \| x \| _ {2} \leqslant - (1 - \theta) \zeta \| x \| _ {2} ^ {2}, \quad \forall \| x \| _ {2} \geqslant \mu = \frac {\sqrt {2 9} \delta}{8 \zeta \theta}$$

这里, $0 < \theta < 1$ 。如在例(9.2)中所见, $\left|x_{2}\right|^{2}$ 在 $\Omega_{c}$ 上有界,为 $96c / 29$ 。因此,如果 $\beta \leqslant 0.4(1 - \zeta)c$ 且 $\delta$ 很小,使得 $\mu^2\lambda_{\max}(P) < c$ ,则 $B_{\mu} \subset \Omega_{c}$ ,且所有始于 $\Omega_{c}$ 内的轨线在所有未来时刻仍保持在 $\Omega_{c}$ 内。而且,定理4.18的条件在 $\Omega_{c}$ 内满足,因此扰动系统的解是一致毕竟有界的,为

$$b = \frac {\sqrt {2 9} \delta}{8 \zeta \theta} \sqrt {\frac {\lambda_ {\max} (P)}{\lambda_ {\min} (P)}}$$

对于更一般的情况,即当原点 x=0 是标称系统(9.2)的一个一致渐近稳定平衡点,而不是指数稳定平衡点时,可以用同样的方法分析扰动系统。

引理9.3 设 $x = 0$ 是标称系统(9.2)的一个一致渐近稳定平衡点， $V(t, x)$ 是标称系统的一个李雅普诺夫函数，在 $[0, \infty) \times D$ 上满足不等式①

$$\alpha_ {1} (\| x \|) \leqslant V (t, x) \leqslant \alpha_ {2} (\| x \|) \tag {9.11}\frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x) \leqslant - \alpha_ {3} (\| x \|) \tag {9.12}\left\| \frac {\partial V}{\partial x} \right\| \leqslant \alpha_ {4} (\| x \|) \tag {9.13}$$

其中 $D = \{x\in R^n\mid \| x\| < r\}$ ， $\alpha_{i}(\cdot)$ 是K类函数， $i = 1,2,3,4$ 。假设扰动项 $g(t,x)$ 对于所有 $t\geqslant 0$ 和 $x\in D$ 以及正常数 $\theta < 1$ ，满足一致有界

$$\| g (t, x) \| \leqslant \delta < \frac {\theta \alpha_ {3} \left(\alpha_ {2} ^ {- 1} \left(\alpha_ {1} (r)\right)\right)}{\alpha_ {4} (r)} \tag {9.14}$$

则对于所有 $\| x(t_0)\| < \alpha_2^{-1}(\alpha_1(r))$ ，扰动系统(9.1)的解 $x(t)$ 满足

$$\| x (t) \| \leqslant \beta (\| x \left(t _ {0}\right) \|, t - t _ {0}), \quad \forall t _ {0} \leqslant t < t _ {0} + T$$

和

$$\| x (t) \| \leqslant \rho (\delta), \quad \forall t \geqslant t _ {0} + T$$

其中 $\beta$ 是 $\mathcal{KL}$ 类函数， $T$ 有限， $\rho$ 是 $\delta$ 的 $\mathcal{K}$ 类函数，定义为

$$\rho (\delta) = \alpha_ {1} ^ {- 1} \left(\alpha_ {2} \left(\alpha_ {3} ^ {- 1} \left(\frac {\delta \alpha_ {4} (r)}{\theta}\right)\right)\right)$$

证明:以 $V(t,x)$ 作为扰动系统(9.1)的备选李雅普诺夫函数, $V(t,x)$ 沿系统(9.1)轨线的导数满足
