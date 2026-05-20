# C. 7 证明定理 4.16

用一个引理,即 Massera 引理,构造李雅普诺夫函数的方法已很成熟,现在我们给出并证明 Massera 引理。

引理 C.1 设 $g:[0,\infty)\rightarrow R$ 是正的连续严格递减函数, 当 t 趋于无穷时, $g(t)$ 趋于零。另设 $h:[0,\infty)\rightarrow R$ 是一个正的连续非减函数, 则存在一个函数 $G(t)$ , 满足

- $G(t)$ 及其导数 $G'(t)$ 是对于所有 $t \geqslant 0$ 都有定义的 $\kappa$ 类函数。  
- 对于当 $t \geqslant 0$ 时，满足 $0 \leqslant u(t) \leqslant g(t)$ 的任意连续函数 $u(t)$ ，存在与 $u$ 无关的正常数 $k_{1}$ 和 $k_{2}$ ，满足

$$\int_ {0} ^ {\infty} G (u (t)) d t \leqslant k _ {1}; \quad \int_ {0} ^ {\infty} G ^ {\prime} (u (t)) h (t) d t \leqslant k _ {2}$$

证明:由于 $g(t)$ 是严格递减的,故可选取序列 $t_{n}$ ,使

$$g (t _ {n}) \leqslant \frac {1}{n + 1}, n = 1, 2, \dots$$

我们利用该序列定义函数 $\eta(t)$ :

(a) $\eta(t_{n})=1/\eta$

(b) 在 $t_{n}$ 和 $t_{n+1}$ 之间, $\eta(t)$ 是线性的。

(c) 在区间 $0 < t \leqslant t_1$ 内, 有 $\eta(t) = (t_1/t)^p$ , 其中 $p$ 为正整数, 选择 $p$ 足够大, 使导数 $\eta'(t)$ 在 $t_1$ 处有一个正跳变, 即 $\eta'(t_1^-) < \eta'(t_1^+)$ 。

函数 $\eta(t)$ 是严格递减的, 且对于 $t \geqslant t_1$ , 有 $g(t) < \eta(t)$ 。当 $t \to 0^+$ 时, $\eta(t)$ 变为无界的。 $\eta(t)$ 的反函数, 记为 $\eta^{-1}(s)$ , 是严格递减函数, 当 $s \to 0^+$ 时变为无界的。显然, 对于任意非负函数 $u(t) \leqslant g(t)$ , 有

$$\eta^ {- 1} (u (t)) \geqslant \eta^ {- 1} (g (t)) > \eta^ {- 1} (\eta (t)) = t, \forall t \geqslant t _ {1}$$

定义 $H(s) = \frac{\exp[-\eta^{-1}(s)]}{h(\eta^{-1}(s))}, s\geqslant 0$

由于 $\eta^{-1}$ 是连续的, 且 h 为正, 因此 $H(s)$ 在 $0 < s < \infty$ 上连续, 而当 $s \to 0^{+}$ 时, $\eta^{-1}(s) \to \infty$ , 故 $H(s)$ 是定义在 $[0, \infty)$ 上的 K 类函数, 因此积分

$$G (r) = \int_ {0} ^ {r} H (s) d s$$

存在,且 $G(r)$ 和 $G'(r)=H(r)$ 都是 $[0,\infty)$ 上的 K 类函数。现在设 $u(t)$ 是连续非负函数,满足 $u(t)\leqslant g(t)$ ,有

$$G ^ {\prime} (u (t)) = \frac {\exp [ - \eta^ {- 1} (u (t)) ]}{h (\eta^ {- 1} (u (t)))} \leqslant \frac {e ^ {- t}}{h (t)}, \forall t \geqslant t _ {1}$$

因此 $\int_{t_1}^{\infty} G'(u(t)) h(t) dt \leqslant \int_{t_1}^{\infty} e^{-t} \leqslant 1$

和 $\int_0^\infty G'(u(t))h(t)dt\leqslant \int_0^{t_1}G'(g(t))h(t)dt + 1\leqslant k_2$

这说明引理中的第二个积分是有界的。对于第一个积分,有

$$\int_ {t _ {1}} ^ {\infty} G (u (t)) d t = \int_ {t _ {1}} ^ {\infty} \int_ {0} ^ {u (t)} \frac {\exp [ - \eta^ {- 1} (s) ]}{h (\eta^ {- 1} (s))} d s d t \leqslant \int_ {t _ {1}} ^ {\infty} \int_ {0} ^ {\eta (t)} \frac {\exp [ - \eta^ {- 1} (s) ]}{h (0)} d s d t$$

当 $0 \leqslant s \leqslant \eta(t)$ 时，有 $-\eta^{-1}(s) \leqslant -t$

因此，当 $t \geqslant t_1$ 时，有 $\int_{0}^{\eta(t)} \frac{\exp[-\eta^{-1}(s)]}{h(0)} ds \leqslant \int_{0}^{\eta(t)} \frac{e^{-t}}{h(0)} ds = \frac{e^{-t}}{h(0)} \eta(t) \leqslant \frac{e^{-t}}{h(0)}$
