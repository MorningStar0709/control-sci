$$
\begin{array}{l} T _ {k} \leqslant \frac {1}{q} [ \beta y _ {k - 1} + \eta_ {k} ] ^ {q} + \frac {1}{s} \\ \leqslant \frac {1}{q} [ (1 + \epsilon) (\beta y _ {k - 1}) ^ {q} + M \eta_ {k} ^ {q} ] + \frac {1}{s} \\ \leqslant \epsilon_ {0} \left[ \frac {1}{q} y _ {k - 1} ^ {q} + \frac {1}{s} \right] + \frac {M}{q} \eta_ {k} ^ {q} + \frac {1}{s} \\ \leqslant \epsilon_ {0} T _ {k - 1} + \frac {M}{q} \eta_ {k} ^ {q} + \frac {1}{s}, \\ \end{array}
$$

从而

$$
\begin{array}{l} x _ {k} + T _ {k} \leqslant \alpha_ {k} x _ {k - 1} + \xi_ {k} + \epsilon_ {0} T _ {k - 1} + \frac {M}{q} \eta_ {k} ^ {q} + \frac {1}{s} \\ \leqslant \alpha_ {k} (x _ {k - 1} + T _ {k - 1}) + \xi_ {k} + \frac {M}{q} \eta_ {k} ^ {q} + \frac {1}{s}. \\ \end{array}
$$

据此利用命题9.3.3知 $\left\{\frac{1}{x_k + T_k}\right\} \in S^0$ ，但 $y_k \leqslant T_k$ ，所以必有 $\left\{\frac{1}{x_k + y_k}\right\} \in S^0$ 。证毕。

最后我们给出一个简单的但却很有用的结论.

命题9.3.4 设 $a_{k} \geqslant 1$ ，若对某 $h > 0$ 由下式定义的序列：

$$s _ {k} \stackrel {\mathrm{def}} {=} \sum_ {j = (k - 1) h} ^ {k h - 1} a _ {j}, \quad k \geqslant 0$$

满足 $\left\{\frac{1}{s_k}\right\} \in S^0$ ，则必有 $\left\{\frac{1}{a_k}\right\} \in S^0$ .

证明 设

$$E \prod_ {k = m} ^ {n} \left(1 - \frac {1}{s _ {k}}\right) \leqslant M \lambda^ {n - m + 1}, \quad \forall n \geqslant m, \forall m \geqslant 0.$$

不妨认为 $n - m > h$ ，再设 $i,j$ 是满足下式的整数：

$$i h \leqslant n < (i + 1) h, \quad (j - 1) h < m \leqslant j h.$$

于是

$$
\begin{array}{l} E \prod_ {k = m} ^ {n} \left(1 - \frac {1}{a _ {k}}\right) \leqslant E \prod_ {k = j h} ^ {i h} \left(1 - \frac {1}{a _ {k}}\right) \\ \leqslant E \prod_ {t = j} ^ {i} \left(1 - \frac {1}{a _ {t h}}\right) \leqslant E \prod_ {k = j} ^ {i} \left(1 - \frac {1}{s _ {t + 1}}\right) \\ \leqslant M \lambda^ {i - j + 1} \leqslant M [ \lambda^ {1 / h} ] ^ {h (i - j) + h} \leqslant M [ \lambda^ {1 / h} ] ^ {n - h - m - h + h} \\ \leqslant M \lambda^ {- 1 - (1 / h)} [ \lambda^ {1 / h} ] ^ {n - m + 1}. \\ \end{array}
$$

命题证毕.

利用上述关于 $S^0$ 的部分讨论，我们可以证明当随机矩阵序列 $\{F_k, \mathcal{F}_k\}$ (其中 $F_k \in \mathbb{R}^{d \times d}, d \geqslant 1$ ) 满足 $0 \leqslant F_k \leqslant I$ 时，对 $\{F_k\} \in S_p$ 的验证可以简单地用 $\{\lambda_k\} \in S^0$ 来保证，其中 $(h > 0$ 为某整数)

$$\lambda_ {k} \stackrel {\text { def }} {=} \lambda_ {\min} \left\{E \left[ \frac {1}{1 + h} \sum_ {i = k h + 1} ^ {(k + 1) h} F _ {i} | \mathcal {F} _ {k h} \right] \right\}. \tag {9.3.15}$$

为此，先证两个引理.

引理9.3.1 设 $\{F_k, \mathcal{F}_k\}$ 是适应的随机矩阵序列，且满足 $0 \leqslant F_k \leqslant I$ ，则有
