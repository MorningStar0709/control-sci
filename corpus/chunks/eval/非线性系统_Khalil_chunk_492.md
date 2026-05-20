# C. 2 证明引理 3.4

上右导数 $D^{+}v(t)$ 定义为 $D^{+}v(t) = \lim \sup_{h\to 0^{+}}\frac{v(t + h) - v(t)}{h}$

其中实数序列 $\{x_{n}\}$ 的 $\limsup_{n\to \infty}$ （上极限）是实数 $y$ ，满足下面两个条件：

- 对于每个 $\varepsilon > 0$ ，存在一个整数 $N$ ，使得 $n > N$ ，即 $x_{n} < \gamma + \varepsilon$ ；  
- 给定 $\varepsilon > 0$ 和 $m > 0$ , 存在一个整数 $n > m$ , 使得 $x_{n} > y - \varepsilon$ 。

第一条是指序列的所有项最终都小于 $y + \varepsilon$ ，第二条指序列中有无限多项大于 $y - \varepsilon$ 。lim sup 的性质之一是，如果对于 $n = 1, 2, \cdots$ ，有 $z_{n} \leqslant x_{n}$ ，则 $\limsup_{n \to \infty} z_{n} \leqslant \limsup_{n \to \infty} x_{n}^{①}$ 。由此可知，如果 $|v(t + h) - v(t)| / h \leqslant g(t, h), \forall h \in (0, b)I$ 和 $\lim_{h \to 0^{+}} g(t, h) = g_{0}(t)$ ，则 $D^{+}v(t) \leqslant g_{0}(t)$ 。

为了证明引理 3.4, 考虑微分方程

$$\dot {z} = f (t, z) + \lambda , \quad z (t _ {0}) = u _ {0} \tag {C.5}$$

$\lambda$ 为正常数。在任意紧区间 $[t_0, t_1]$ ，由定理3.5可得，对于任意 $\varepsilon > 0$ ，存在 $\delta > 0$ ，使得当 $\lambda < \delta$ 时，方程(C.5)有定义在 $[t_0, t_1]$ 上的唯一解 $z(t, \lambda)$ ，且

$$\left| z (t, \lambda) - u (t) \right| < \varepsilon , \quad \forall t \in [ t _ {0}, t _ {1} ] \tag {C.6}$$

结论1:对于所有 $t \in [t_{0}, t_{1}]$ ，有 $v(t) \leqslant z(t, \lambda)$ 。

该结论可用反证法证明。设结论不成立，那么有时间 $a, b \in (t_0, t_1]$ ，使得 $v(a) = z(a, \lambda)$ 及 $v(t) > z(t, \lambda)$ ，这里 $a < t \leqslant b$ ，因此有

$$v (t) - v (a) > z (t, \lambda) - z (a, \lambda), \quad \forall t \in (a, b ]$$

这表明

$$D ^ {+} v (a) \geqslant \dot {z} (a, \lambda) = f (a, z (a, \lambda)) + \lambda > f (a, v (a))$$

而上式与不等式 $D^{+}v(t)\leqslant f(t,v(t))$ 矛盾。

结论2:对于所有 $t \in [t_{0}, t_{1}]$ ，有 $v(t) \leqslant u(t)$ 。

同样,这个结论也用反证法证明。设结论不成立,那么存在 $a \in (t_{0}, t_{1}]$ , 使得 $v(a) > u(a)$ , 取 $\varepsilon = [v(a) - u(a)] / 2$ , 并利用式(C.6)可得

$$v (a) - z (a, \lambda) = v (a) - u (a) + u (a) - z (a, \lambda) \geqslant \varepsilon$$

这与结论1相矛盾。

因此,可以证明 $v(t) \leqslant u(t)$ , $t \in [t_{0}, t_{1}]$ 。由于不等式在每个紧区间都是成立的,因此对于所有 $t \geqslant t_{0}$ , 不等式也是成立的。如果情况不是这样,我们设 $T < \infty$ 是不等式不成立的第一时刻,对于所有 $t \in [t_{0}, T)$ , 有 $v(t) \leqslant u(t)$ , 且由连续性,有 $v(T) = u(T)$ , 故可以将不等式扩展到区间 $[T, T + \Delta] (\Delta > 0)$ , 这与 T 为不等式不成立的第一时刻的假设相矛盾。证毕。☐
