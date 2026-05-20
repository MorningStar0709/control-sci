$$\alpha_ {k} \geqslant \epsilon_ {0} > 0;\left\| \prod_ {k = m} ^ {n} E [ \alpha_ {k + 1} ^ {4} | \mathcal {F} _ {k} ] \right\| _ {1} \leqslant M \gamma^ {n - m + 1}, \quad \forall n \geqslant m \geqslant 1; \tag {9.3.9}$$

及

$$E [ \xi_ {k + 1} ^ {2} | \mathcal {F} _ {k} ] \leqslant N < \infty , \quad \forall k, \tag {9.3.10}$$

其中 $\epsilon_0, M, N$ 及 $\gamma \in (0,1)$ 是常数。则下列三个结论成立：

(i) $\left\| \prod_{k=m}^{n} \alpha_k \right\|_2 \leqslant M^{1/4} \gamma^{\frac{1}{4}(n-m+1)}, \forall n \geqslant m, \forall m \geqslant 1;$

(ii) $\sup_k E \| x_k\| < \infty ;$

(iii) $\left\{\frac{1}{x_k}\right\} \in S^0.$

证明 记

$$\beta_ {k} = E [ \alpha_ {k + 1} ^ {4} | \mathcal {F} _ {k} ], \quad Z _ {k + 1} = \left(\prod_ {i = m} ^ {k} \beta_ {i}\right) ^ {- 1} \prod_ {i = m} ^ {k} \alpha_ {i + 1} ^ {4},$$

则显然有 $Z_{k + 1} = Z_k\beta_k^{-1}\alpha_{k + 1}^4$ 于是对 $\forall k\geqslant m,$ 有

$$E Z _ {k + 1} = E \{E [ Z _ {k + 1} | \mathcal {F} _ {k} ] \} = E Z _ {k} = \dots = E Z _ {m + 1} = 1.$$

从而对 $\forall n\geqslant m$

$$
\begin{array}{l} E \prod_ {i = m} ^ {n} \alpha_ {i + 1} ^ {2} = E \sqrt {Z _ {n + 1}} \sqrt {\prod_ {i = m} ^ {n} \beta_ {i}} \\ \leqslant \sqrt {E Z _ {n + 1}} \cdot \sqrt {E \prod_ {i = m} ^ {n} \beta_ {i}} \leqslant \sqrt {M} \sqrt {\gamma^ {n - m + 1}}. \\ \end{array}
$$

故结论 (i) 成立. 而结论 (ii) 可以从 (i), 式 (9.3.8), 式 (9.3.10) 立即推出. 下面证结论 (iii).

首先假设式 (9.3.10) 中的 $N \leqslant 1$ . 此时易知

$$E \left[ \xi_ {k + 1} \mid \mathcal {F} _ {k} \right] \leqslant 1.$$

对任何 $n > m$ ，定义 $\{y_k\}$ 如下：

$$y _ {k} = \left(1 - \frac {1}{x _ {k}}\right) y _ {k - 1}, \quad y _ {m - 1} = 1, \quad k \in [ m, n ]. \tag {9.3.11}$$

于是利用式 (9.3.8) 得

$$x _ {k} y _ {k} = (x _ {k} - 1) y _ {k - 1} \leqslant (\alpha_ {k} x _ {k - 1} + \xi_ {k} - 1) y _ {k - 1},$$

记 $\gamma_{k} = E[\alpha_{k + 1}|\mathcal{F}_{k}]$ ，利用 $y_{k}\in \mathcal{F}_{k}$ ，及 $E[\xi_k|\mathcal{F}_{k - 1}]\leqslant 1$ ，从上式得

$$E \left[ x _ {k} y _ {k} \mid \mathcal {F} _ {k - 1} \right] \leqslant \gamma_ {k - 1} \left(x _ {k - 1} y _ {k - 1}\right), \quad k \geqslant m, \tag {9.3.12}$$

再记 $Z_{k} = \left(\prod_{i = m + 1}^{k - 1}\gamma_{i}\right)^{-1}x_{k}y_{k}, k\geqslant m - 1,$ 于是利用式(9.3.12）知对 $\forall k\geqslant m$

$$E [ Z _ {k} | \mathcal {F} _ {k - 1} ] \leqslant \left(\prod_ {i = m - 1} ^ {k - 2} \gamma_ {i}\right) ^ {- 1} x _ {k - 1} y _ {k - 1} = Z _ {k - 1}.$$

故

$$E Z _ {k} \leqslant E Z _ {k - 1} \leqslant \dots \leqslant E Z _ {m - 1} = E x _ {m - 1}.$$

但据结论 (ii) 知存在常数 $M_0 < \infty$ 使

$$\sup _ {m \geqslant 0} \sup _ {k \leqslant m} E Z _ {k} \leqslant M _ {0}.$$

于是利用 Schwarz 不等式及式 (9.3.9) 得
