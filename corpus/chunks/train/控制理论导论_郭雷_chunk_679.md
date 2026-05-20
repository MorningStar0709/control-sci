$$E A _ {n} x _ {n + 1} \leqslant E A _ {n - 1} x _ {n} \leqslant \dots \leqslant E A _ {m - 1} x _ {m} = 1.$$

从而

$$
\begin{array}{l} E \prod_ {i = m} ^ {n} (1 - \beta_ {i + 1}) = E x _ {n + 1} \leqslant E \sqrt {x _ {n + 1}} \\ \leqslant E \sqrt {x _ {n + 1} A _ {n}} \cdot \sqrt {A _ {n} ^ {- 1}} \leqslant \sqrt {E (x _ {n + 1} A _ {n}) E A _ {n} ^ {- 1}} \\ \leqslant \sqrt {E A _ {n} ^ {- 1}} \leqslant \left\{E \prod_ {i = m} ^ {n} (1 - \alpha_ {i}) \right\} ^ {1 / 2} \leqslant \sqrt {M} (\sqrt {\lambda}) ^ {n - m + 1}, \\ \end{array}
$$

其中 $M > 0, \lambda \in [0,1)$ 是常数。这说明 $\{\beta_k\} \in S^0$

在一般情形 $\alpha_{k} \in [0,1]$ 下，利用单调收敛定理知

$$\lim _ {\epsilon \rightarrow 1 ^ {-}} E \prod_ {k = m} ^ {n} (1 - \epsilon \alpha_ {k}) \leqslant M \lambda^ {n - m + 1}.$$

于是存在 $0 < \epsilon^{*} < 1$ 使 $\forall \epsilon \in (\epsilon^{*}, 1)$ 有

$$E \prod_ {k = m} ^ {n} (1 - \epsilon \alpha_ {k}) \leqslant 2 M \lambda^ {n - m + 1}.$$

但 $\epsilon \alpha_{k} \in (0,1)$ , 故利用刚证得的事实知

$$E \prod_ {k = m} ^ {n} (1 - \epsilon \beta_ {k + 1}) \leqslant \sqrt {2 M} (\sqrt {\lambda}) ^ {n - m + 1}.$$

但是 $\epsilon \beta_{k + 1} \leqslant \beta_{k + 1}, \forall \epsilon \in (\epsilon^{*}, 1)$ , 所以有 $\beta \in S^0$ . 证毕

推论9.3.1 设 $\{\alpha_{k},\mathcal{F}_{k}\}$ 是适应序列 $\alpha_{k}\in [0,1]$ . 若存在某整数 $h > 0$ 使

$$\{E [ \alpha_ {k + h} | \mathcal {F} _ {k} ] \} \in S ^ {0},$$

则必有 $\{\alpha_k\} \in S^0$ .

命题9.3.2 设 $\{\alpha_k\} \in S^0, \alpha_k \leqslant \alpha^* < 1$ ，其中 $\alpha^*$ 是常数，则对任何 $\epsilon \in (0,1)$ ，有 $\{\epsilon \alpha_k\} \in S^0$ .

证明 设常数 $\lambda \in (0,1), M > 0$ 使

$$E \prod_ {k = m + 1} ^ {n} (1 - \alpha_ {k}) \leqslant M \lambda^ {n - m}, \quad \forall n \geqslant m > 0.$$

于是在下述不等式

$$1 - x \leqslant (1 - d x) ^ {(1 - t) / d}, \quad d > 1, 0 \leqslant d x \leqslant t < 1$$

中取 $x = \epsilon \alpha_{k}, d = \frac{1}{\epsilon}$ 得

$$
\begin{array}{l} E \prod_ {k = m + 1} ^ {n} (1 - \epsilon \alpha_ {k}) \leqslant E \left[ \prod_ {k = m + 1} ^ {n} (1 - \alpha_ {k}) ^ {(1 - \alpha^ {*}) \epsilon} \right] \\ \leqslant \left\{E \prod_ {k = m + 1} ^ {n} (1 - \alpha_ {k}) \right\} ^ {(1 - \alpha^ {*}) \epsilon} \leqslant (M \lambda^ {n - m}) ^ {(1 - \alpha^ {*}) \epsilon}. \\ \end{array}
$$

因此命题得证.

命题9.3.3 设 $\{x_{k},\mathcal{F}_{k}\}$ 是适应序列， $x_{k}\geqslant 1$ 且

$$x _ {k + 1} \leqslant \alpha_ {k + 1} x _ {k} + \xi_ {k + 1}, \quad k \geqslant 0, E x _ {0} ^ {2} < \infty , \tag {9.3.8}$$

其中 $\{\alpha_k, \mathcal{F}_k\}$ 及 $\{\xi_k, \mathcal{F}_k\}$ 是非负适应序列并满足条件
