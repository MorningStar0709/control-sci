$$
\begin{array}{l} \int_ {t _ {0}} ^ {t} \gamma (\tau) d \tau = \int_ {t _ {0}} ^ {T} \gamma (\tau) d \tau + \int_ {T} ^ {t} \gamma (\tau) d \tau \\ \leqslant \int_ {0} ^ {T} \gamma (\tau) d \tau + \varepsilon_ {1} (t - T) + \varepsilon_ {1} \Delta \leqslant \varepsilon_ {1} (t - t _ {0}) + \eta \\ \end{array}
$$

在上述引理的第一种情况下, 当 $\varepsilon = 0$ 时, 条件(9.20) 成立。而在第二种情况下, 当 $\varepsilon$ 为任意小时, 式(9.20) 成立。因此在这两种情况下, 条件(9.21) 总是成立的, 且扰动系统(9.2) 的原点是指数稳定的。引理的第三种情况是, 当 t 变得足够大时, 为 $\gamma(t)$ 的移动平均设定了一个边界。如果该边界足够小, 则扰动系统(9.2) 的原点将是指数稳定的。☐

例9.6 考虑线性系统

$$\dot {x} = [ A (t) + B (t) ] x$$

其中 $A(t)$ 和 $B(t)$ 是连续的，且 $A(t)$ 在 $[0, \infty)$ 上有界。假设原点是标称系统

$$\dot {x} = A (t) x$$

的一个指数稳定平衡点,且当 t 趋于无穷时 $B(t)$ 趋于零。由定理 4.12 可知,存在一个二次李雅普诺夫函数 $V(t,x)=x^{\mathrm{T}}P(t)x$ ,全局满足式(9.3)至式(9.5)。扰动项 $B(t)x$ 满足不等式

$$\| B (t) x \| \leqslant \| B (t) \| \| x \|$$

由于当 t 趋于无穷时， $\|B(t)\|$ 趋于零，由推论 9.1 和引理 9.5 的第二种情况可知，原点是扰动系统的全局指数稳定平衡点。

当 $\int_0^\infty \| B(t)\| dt <   \infty$ （见习题9.15）和 $\int_0^\infty \| B(t)\| ^2 dt <   \infty$ （见习题9.16）时，可得出与上例相似的结论。

在非零扰动的情况下,也就是当 $\delta(t) \neq 0$ 时,下面的引理给出当 t 趋于无穷时关于 $x(t)$ 的渐近特性的几个结论。

引理9.6 假设满足引理9.4的条件，用 $x(t)$ 表示扰动系统(9.1)的解。

1. 如果对于某一正常数 $\beta$ ，有

$$\int_ {t _ {0}} ^ {t} e ^ {- \alpha (t - \tau)} \delta (\tau) d \tau \leqslant \beta , \forall t \geqslant t _ {0}$$

则 $x(t)$ 是一致毕竟有界的，其最终边界为

$$b = \frac {c _ {4} \rho \beta}{2 c _ {1} \theta}$$

其中 $\theta \in (0,1)$ 是任意常数。

2. 如果 $\lim_{t\to \infty}\delta (t) = \delta_{\infty} > 0$

则 $x(t)$ 是一致毕竟有界的, 其最终边界为

$$b = \frac {c _ {4} \rho \delta_ {\infty}}{2 \alpha c _ {1} \theta}$$

其中 $\theta\in(0,1)$ 是任意常数。

3. 如果 $\lim_{t\to \infty}\delta (t) = 0$ ，则 $\lim_{t\to \infty}x(t) = 0$ 。

如果引理9.4的条件全局满足,则前述各点对于任意初始状态 $x(t_{0})$ 都成立。

证明:所有三种情况很容易由不等式(9.23)得出。在前两种情况下,运用性质:如果 $u(t)=w(t)+a,a>0$ 和 $\lim_{t\to\infty}w(t)=0$ ,则 $u(t)$ 是毕竟有界的,其最终边界为 $a/\theta,\theta<1$ 为任意正数。这就是因为存在一个有限时间 T,使得当所有 t>T 时, $|w(t)|\leqslant a(1-\theta)/\theta$ 。在后两种情况下,运用性质:如果 $u(t)=\int_{t_{0}}^{t}\exp(-\alpha(t-\tau))w(\tau)d\tau$ ,其中 $w(t)$ 有界,且 $\lim_{t\to\infty}w(t)=w_{\infty}$ ,则 $\lim_{t\to\infty}u(t)=w_{\infty}/\alpha$ 。 $^{①}$
