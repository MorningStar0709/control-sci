(1) 存在连续函数 $\omega(\cdot, \cdot): (0, a] \times \mathbb{R}_+ \to \mathbb{R}_+$ , 并且存在 $[0, a]$ 上的连续函数 $r(t)$ , 它在 $(0, a)$ 上可微, $\dot{r}_+(0)$ 存在, 并满足

$$\dot {r} (t) = \omega (t, r (t)), \quad r (0) = 0, \quad \dot {r} _ {+} (0) = 0;$$

(2) 向量值函数 $f(t, x)$ 在 $\pi(a, b) = \{(t, x) | |t| \leqslant a, |x - x_0| \leqslant b\}$ 上连续，且满足

$$\left| f (t, x _ {1}) - f (t, x _ {2}) \right| \leqslant \omega (t, | x _ {1} - x _ {2} |), \quad \forall (t, x _ {1}), (t, x _ {2}) \in \pi (a, b),$$

则式 (2.2.19) 满足初始条件 $x(0) = x_0$ 的解在区间 $[-h, h]$ 上存在唯一，其中 $h = \min(a, b/M), M = \max_{(t, x) \in \pi(a, b)} |f(t, x)|$ .

从定理2.2.6知本定理中满足初始条件 $x(0) = x_0$ 的解在区间 $[-h, h]$ 上存在，其解的唯一性证明见文献[6].

定理2.2.9(Osgood)[2] 设标量函数 $\varphi(r)$ 在 $0 < r \leqslant a$ 上连续, 且 $\lim_{\varepsilon \to 0_+} \int_{\varepsilon}^{a} \frac{\mathrm{d}\tau}{\varphi(\tau)} = +\infty$ . 如果 $f(t,x)$ 满足

$$| f (t, x _ {1}) - f (t, x _ {2}) | \leqslant \varphi (| x _ {1} - x _ {2} |), \quad \forall (t, x _ {1}), (t, x _ {2}) \in \Omega_ {n + 1}, \tag {2.2.27}$$

则 $\forall (t_0, x_0) \in \Omega_{n+1}$ , 微分方程 (2.2.19) 满足初始条件 $x(t_0) = x_0$ 的解最多只有一个.

证明 设 $x_{1}(t), x_{2}(t)$ 是微分方程 (2.2.19) 满足初始条件 $x(t_{0}) = x_{0}$ 的两个解。令 $(\alpha, \beta)(\alpha < \beta)$ 是 $x_{1}(t), x_{2}(t)$ 共同定义的区间。记 $z(t) = x_{1}(t) - x_{2}(t)$ 。注意到 $z(t_{0}) = 0$ ，所以 $\{t \mid z(t) = 0\} \neq \varnothing$ ，记

$$\underline {{{t}}} = \inf \{t \mid z (t) = 0 \}, \quad \bar {t} = \sup \{t \mid z (t) = 0 \}.$$

如果 $\overline{t} < \beta$ ，则根据 $z(t)$ 的连续性和 $\overline{t}$ 的定义知 $z(\overline{t}) = 0$ ，并且

$$z (t) \neq 0, \quad \forall t \in (\bar {t}, \beta). \tag {2.2.28}$$

由此可得

$$D _ {+} | z (t) | \leqslant | \dot {z} (t) | \leqslant | f (t, x _ {1} (t)) - f (t, x _ {2} (t)) | \leqslant \varphi (| z (t) |). \tag {2.2.29}$$

考察标量微分方程

$$\frac {\mathrm{d} r (t)}{\mathrm{d} t} = \varphi (r (t)). \tag {2.2.30}$$

可以证明，当 $\lim_{\varepsilon \to 0}\int_{\varepsilon}^{a}\frac{\mathrm{d}r}{\varphi(r)} = +\infty$ 时，微分方程(2.2.30)满足 $r(0) = 0$ 的唯一解为 $r(t)\equiv 0$

根据定理2.2.3, 得

$$| z (t) | \leqslant r (t) = 0 \quad \forall t \in (\bar {t}, \beta),$$

与式 (2.2.28) 矛盾，从而 $\bar{t} = \beta$ 。同理可证 $\underline{t} = \alpha$ 。于是定理得证。

不难验证，当取 $k > 0, 0 < r \leqslant a$ 时， $kr, kr|\log r|, kr|\log |\log r||$ 等等，皆是具有定理2.2.9中性质的特殊的 $\varphi(r)$ .
