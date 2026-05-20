$$E \beta_ {\infty} (a, b) = \lim _ {N \rightarrow \infty} E \beta_ {N} (a, b) \leqslant \frac {\sup _ {N} E \xi_ {N} ^ {+} + | a |}{b - a} < \infty .$$

从式 (4.2.5) 知 $P(\beta_N(a, b) = \infty) > 0$ , 这和上式相矛盾, 所以

$$P (\xi^ {*} = \xi_ {*}) = 1,$$

即 $\xi_{k}$ 收敛到某一极限 $\xi$ .

现证 $E|\xi| < \infty$ . 用 Fatou 引理,

$$
\begin{array}{l} E \xi^ {+} = E \lim _ {k \rightarrow \infty} \inf \xi_ {k} ^ {+} \leqslant \lim _ {k \rightarrow \infty} \inf E \xi_ {k} ^ {+} \leqslant \sup _ {k} E \xi_ {k} ^ {+} <   \infty , \\ E \xi^ {-} = E \lim _ {k \rightarrow \infty} \inf _ {\xi_ {k} ^ {-}} \leqslant \lim _ {k \rightarrow \infty} \inf _ {\xi_ {k} ^ {-}} \leqslant \sup _ {k} E \xi_ {k} ^ {-} \\ = \sup _ {k} (E \xi_ {k} ^ {+} - E \xi_ {k}) \leqslant \sup _ {k} (E \xi_ {k} ^ {+} - E \xi_ {1}) <   \infty , \\ \end{array}
$$

上面用了下鞅性质 $E\xi_1 \leqslant E\xi_k, \forall k \geqslant 1$ . 所以 $E|\xi| < \infty$ .

推论4.2.2 若 $(\xi_k, \mathcal{F}_k)$ 为非负上鞅或非正下鞅，则

$$\lim _ {k \to \infty} \xi_ {k} = \xi \qquad {\mathrm{a.s.}} \quad {\text {且}} \quad E | \xi | < \infty .$$

证明 若 $(\xi_k, \mathcal{F}_k)$ 为非正下鞅，则 $E\xi_k^+ = 0$ 。那么推论直接从定理4.2.4得出。若 $(\xi_k, \mathcal{F}_k)$ 为非负上鞅，则 $(- \xi_k, \mathcal{F}_k)$ 为非正下鞅。

推论 4.2.3 若 $(\xi_{k}, \mathcal{F}_{k})$ 为鞅且 $\sup_{k} E|\xi_{k}| < \infty$ ，则 $\lim_{k \to \infty} \xi_{k} = \xi$ a.s. 且 $E|\xi| < \infty$ .

证明 由于 $(\xi_k, \mathcal{F}_k)$ 是鞅，所以 $E\xi_k = E\xi_1, \forall k.$ 因此

$$E | \xi_ {k} | = E \xi_ {k} ^ {+} + E \xi_ {k} ^ {-} = 2 E _ {k} ^ {+} - E \xi_ {k} = 2 E \xi_ {k} ^ {+} - E \xi_ {1}.$$

所以

$$\sup _ {k} E \xi_ {k} ^ {+} = \frac {1}{2} \sup _ {k} (E | \xi_ {k} | - E \xi_ {1}) = \frac {1}{2} \sup _ {k} E | \xi_ {k} | - \frac {1}{2} E \xi_ {1} < \infty . \tag {4.2.6}$$

由于鞅也是下鞅，那么从式(4.2.6)及定理4.2.5直接得出推论.
