$$
\begin{array}{l} (T (t) T (\tau) x) (s) = \frac {1}{\sqrt {\pi t}} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- (s - \sigma) ^ {2} / t} \mathrm{d} \sigma \frac {1}{\sqrt {\pi \tau}} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- (\sigma - \xi) ^ {2} / \tau} x (\xi) \mathrm{d} \xi \\ = \frac {1}{\pi \sqrt {t \tau}} \int_ {- \infty} ^ {\infty} x (\xi) \mathrm{d} \xi \int_ {- \infty} ^ {\infty} \exp \left(- (\sigma - \xi) ^ {2} / \tau - (s - \sigma) ^ {2} / t\right) \mathrm{d} \sigma \\ = \frac {1}{\pi \sqrt {t \tau}} \int_ {- \infty} ^ {\infty} x (\xi) d \xi \int_ {- \infty} ^ {\infty} \exp \left(- \mu^ {2} / \tau - (s - \xi - \mu) ^ {2} / t\right) d \mu \\ = \frac {1}{\sqrt {\pi (t + \tau)}} \int_ {- \infty} ^ {\infty} \exp \left(- (s - \xi) ^ {2} / (t + \tau)\right) x (\xi) d \xi \\ = (T ^ {\prime} (t + \tau) x) (s). \\ \end{array}
$$

剩下只需证明 $T(t)$ 在 $t = 0$ 的强连续性．注意到

$$(T (t) x) (s) - x (s) = \frac {1}{\sqrt {\pi}} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \sigma^ {2}} [ x (s - \sigma \sqrt {t}) - x (s) ] \mathrm{d} \sigma ,$$

故依据Fubini定理有

$$\| T (t) x - x \| \leqslant \frac {1}{\sqrt {\pi}} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \sigma^ {2}} \mathrm{d} \sigma \int_ {- \infty} ^ {\infty} | x (s - \sigma \sqrt {t}) - x (s) | \mathrm{d} s.$$

但

$$\int_ {- \infty} ^ {\infty} | x (s - \sigma \sqrt {t}) - x (s) | \mathrm{d} s \leqslant 2 \| x \|,$$

并且对于固定的 $\sigma$

$$\lim _ {t \rightarrow \infty} \int_ {- \infty} ^ {\infty} | x (s - \sigma \sqrt {t}) - x (s) | \mathrm{d} s = 0.$$

因此，根据Lebesgue控制收敛定理，我们得到

$$\lim _ {t \downarrow 0} \| T (t) x - x \| = 0, \quad \forall x \in L ^ {1} (- \infty , \infty).$$

例5.3.5 设 $\{e_n\}$ 是可分Hilbert空间 $H$ 中的规范直交基，而 $\{\lambda_n\}$ 是一复数序列。那么对于任意固定的 $t \geqslant 0$ ，线性算子 $T(t)$

$$T (t) x = \sum_ {n = 1} ^ {\infty} \mathrm{e} ^ {\lambda_ {n} t} (x, e _ {n}) e _ {n}, \quad \forall x \in H \tag {5.3.3}$$

有界的充分必要条件是，对于每一 $t \geqslant 0, \{\mathrm{e}^{\lambda_n t}\}$ 是一有界数列。显然后者等价于

$$\sup \left\{\operatorname{Re} \lambda_ {n} \mid n \geqslant 1 \right\} < \infty . \tag {5.3.4}$$

在条件 (5.3.4) 之下，我们有

$$
\begin{array}{l} T (t) T (s) x = \sum_ {n = 1} ^ {\infty} \mathrm{e} ^ {\lambda_ {n} t} (T (s) x, e _ {n}) e _ {n} \\ = \sum_ {n = 1} ^ {\infty} \mathrm{e} ^ {\lambda_ {n} t} \left(\sum_ {k = 1} ^ {\infty} \mathrm{e} ^ {\lambda_ {k} s} (x, e _ {k}) e _ {k}, e _ {k}\right) e _ {n} \\ = \sum_ {n = 1} ^ {\infty} \mathrm{e} ^ {\lambda_ {n} t} \mathrm{e} ^ {\lambda_ {n} s} (x, e _ {n}) e _ {n} = T (t + s) x, \quad \forall x \in H, \\ \end{array}
$$
