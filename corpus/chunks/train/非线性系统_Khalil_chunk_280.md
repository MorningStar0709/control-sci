$$= \frac {1}{2 c} \int_ {0} ^ {\infty} \frac {d}{d t} [ - y ^ {T} (t) y (t) ] d t = \frac {1}{2 c} [ - y ^ {T} (t) y (t) ] | _ {0} ^ {\infty}= \frac {1}{2 c} y ^ {\mathrm{T}} (0) y (0) = \frac {1}{2 c} z ^ {\mathrm{T}} z \Rightarrow c _ {1} = \frac {1}{2 c}$$

将 $P(\alpha)A(\alpha) + A^{\mathrm{T}}(\alpha)P(\alpha) = -I$ 对 $\alpha$ 的任意分量 $\alpha_{i}$ 进行偏微分，并用 $P^{\prime}(\alpha)$ 表示 $P(\alpha)$ 的

导数,则

$$P ^ {\prime} (\alpha) A (\alpha) + A ^ {T} (\alpha) P ^ {\prime} (\alpha) = - \left\{P (\alpha) A ^ {\prime} (\alpha) + \left[ A ^ {\prime} (\alpha) \right] ^ {T} P (\alpha) \right\}$$

这样, $P'(\alpha)$ 为

$$P ^ {\prime} (\alpha) = \int_ {0} ^ {\infty} \left[ e ^ {t A (\alpha)} \right] ^ {\mathrm{T}} \left\{P (\alpha) A ^ {\prime} (\alpha) + [ A ^ {\prime} (\alpha) ] ^ {\mathrm{T}} P (\alpha) \right\} \left[ e ^ {t A (\alpha)} \right] d t$$

从而可以得到 $\| P^{\prime}(\alpha)\|_{2}\leqslant \int_{0}^{\infty}k^{2}e^{-2\gamma t}2\frac{k^{2}}{2\gamma} b_{i}dt = \frac{b_{i}k^{4}}{2\gamma^{2}}\Rightarrow \mu_{i} = \frac{b_{i}k^{4}}{2\gamma^{2}}$

这样就完成了引理的证明。

应该注意到引理9.9中的集合 $\Gamma$ 不必是紧集。当 $\Gamma$ 是紧集时， $A(\alpha)$ 的边界及其偏导数都由 $A(\alpha)$ 是连续可微的假设得出。

例9.9 考虑系统

$$\dot {x} = A (\varepsilon t) x$$

其中 $\varepsilon > 0$ 。当 $\varepsilon$ 足够小时，可以把系统看成慢变系统，当 $u = \varepsilon t, \Gamma = [0, \infty)$ 时即为方程(9.38)的形式。对于所有 $u \in \Gamma$ ，原点 $x = 0$ 是一个平衡点。因此，这是当 $h(u) = 0$ 时的一个特例。假设对于所有 $\alpha \in \Gamma, \operatorname{Re}[\lambda(A(\alpha))] \leqslant -\sigma < 0, A(\alpha)$ 和 $A'(\alpha)$ 是一致有界的。这样李雅普诺夫方程(9.48)的解具有引理9.9所述的性质。把 $V(x, u) = x^{\mathrm{T}}P(u)x$ 作为 $\dot{x} = A(u)x$ 的一个备选李雅普诺夫函数，得

$$
\begin{array}{l} \dot {V} (t, x) = x ^ {\mathrm{T}} [ P (u (t)) A (u (t)) + A ^ {\mathrm{T}} (u (t)) P (u (t)) ] x + x ^ {\mathrm{T}} P ^ {\prime} (u (t)) \dot {u} (t) x \\ \leqslant - x ^ {T} x + \varepsilon c _ {5} \| x \| _ {2} ^ {2} = - (1 - \varepsilon c _ {5}) \| x \| _ {2} ^ {2} \\ \end{array}
$$

其中 $c_{5}$ 是 $\| P'(\alpha)\| _2$ 的上界。因此，对于所有 $\varepsilon < 1 / c_5$ ，原点 $x = 0$ 是 $\dot{x} = A(\varepsilon t)x$ 的一个指数稳定平衡点。
