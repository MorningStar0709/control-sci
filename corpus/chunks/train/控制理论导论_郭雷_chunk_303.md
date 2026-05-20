$$E \beta (0, b) \leqslant \frac {E \xi_ {N}}{b}. \tag {4.2.2}$$

定义 $\xi_0 = 0$

$$
\eta_ {k} = \left\{ \begin{array}{l l} {0, \qquad \text {如} \tau_ {m - 1} <   k \leqslant \tau_ {m}, \text {且} m \text {为奇数},} \\ {1, \qquad \text {如} \tau_ {m - 1} <   k \leqslant \tau_ {m}, \text {且} m \text {为偶数}.} \end{array} \right.
$$

如 $m$ 为偶数，那么从 $\tau_{m-1}$ 到 $\tau_m$ 轨线 $\xi_k$ 穿越 $(0, b)$ 一次。因此

$$\sum_ {k = \tau_ {m - 1} + 1} ^ {\tau_ {m}} \eta_ {k} (\xi_ {k} - \xi_ {k - 1}) = \sum_ {k = \tau_ {m - 1} + 1} ^ {\tau_ {m}} (\xi_ {k} - \xi_ {k - 1}) = \xi_ {\tau_ {m}} - \xi_ {\tau_ {m} - 1} \geqslant \xi_ {\tau_ {m}} \geqslant b,$$

所以

$$\sum_ {k = 1} ^ {N} \eta_ {k} (\xi_ {k} - \xi_ {k - 1}) \geqslant b \beta (0, b). \tag {4.2.3}$$

注意到 $\tau_{k}$ 是Markov时间，并且

$$\{\eta_ {k} = 1 \} = \bigcup_ {m \geqslant 1} \left\{\{\tau_ {2 m - 1} < k \} \bigcap \{\tau_ {2 m} < k \} ^ {c} \right\},$$

所以 $\{\eta_k = 1\}$ 对 $\mathcal{F}_{k - 1}$ 可测.

对式 (4.2.3) 取期望然后用式 (4.1.23) 得

$$
\begin{array}{l} b E \beta (0, b) \leqslant E \sum_ {k = 1} ^ {N} \eta_ {k} \left(\xi_ {k} - \xi_ {k - 1}\right) = \sum_ {k = 1} ^ {N} \int_ {\{\eta_ {k} = 1 \}} \left(\xi_ {k} - \xi_ {k - 1}\right) d P \\ = \sum_ {k = 1} ^ {N} \int_ {\{\eta_ {k} = 1 \}} E [ (\xi_ {k} - \xi_ {k - 1}) | \mathcal {F} _ {k - 1} ] d P \\ = \sum_ {k = 1} ^ {N} \int_ {\left\{\eta_ {k} = 1 \right\}} \left[ E \left(\xi_ {k} \mid \mathcal {F} _ {k - 1}\right) - \xi_ {k - 1} \right] d P \\ \leqslant \sum_ {k = 1} ^ {N} \int_ {\Omega} [ E (\xi_ {k} | \mathcal {F} _ {k - 1}) - \xi_ {k - 1} ] \mathrm{d} P. \\ \end{array}
$$

上面最后一个不等式因为 $(\xi_k, \mathcal{F}_k)$ 是下鞅，上式右端等于 $\sum_{k=1}^{N}(E\xi_k - E\xi_{k-1}) = E\xi_N$ 。由此便得式 (4.2.2).

定理 4.2.5 (Doob) 设 $(\xi_{k}, \mathcal{F}_{k})$ 为下鞅，且 $\sup_{k} E\xi_{k}^{+} < \infty$ a.s., 那么存在随机变量 $\xi, E|\xi| < \infty$ , 使

$$\lim _ {k \rightarrow \infty} \xi_ {k} = \xi , \quad \text { a . s . }$$

证明 记

$$\limsup _ {k \to \infty} \xi_ {k} \stackrel {\text { def }} {=} \xi^ {*}, \quad \liminf _ {k \to \infty} \xi_ {k} \stackrel {\text { def }} {=} \xi_ {*}.$$

反设

$$P (\xi^ {*} > \xi_ {*}) > 0. \tag {4.2.4}$$

那么当 $a$ 和 $b$ 取遍有理数时

$$(\xi^ {*} > \xi_ {*}) = \bigcup_ {a < b} (\xi^ {*} > b > a > \xi_ {*}).$$

从式 (4.2.4) 知必存在有理数 $a$ 及 $b$ , 使

$$P \left(\xi^ {*} > b > a > \xi_ {*}\right) > 0. \tag {4.2.5}$$

用 $\beta_{N}(a,b)$ 表示 $(\xi_k,\mathcal{F}_k), k \geqslant N$ 穿越 $(a,b)$ 的次数，用定理4.2.4知

$$E \beta_ {N} (a, b) \leqslant \frac {E \xi_ {N} ^ {+} + | a |}{b - a}.$$

记

$$\beta_ {\infty} (a, b) = \lim _ {N \rightarrow \infty} \beta_ {N} (a, b).$$

由单调收敛定理知
