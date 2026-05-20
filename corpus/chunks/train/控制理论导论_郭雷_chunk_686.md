$$
\begin{array}{l} E x _ {m} ^ {\mathrm{T}} F _ {i _ {1}} \dots F _ {i _ {k}} x _ {m} \leqslant E \| x _ {m} ^ {\mathrm{T}} F _ {i _ {1}} ^ {1 / 2} \| \| F _ {i _ {1}} ^ {1 / 2} F _ {i _ {2}} \dots F _ {i _ {k}} ^ {1 / 2} \| \| F _ {i _ {k}} ^ {1 / 2} x _ {m} \| \\ \leqslant E \left\| x _ {m} ^ {\mathrm{T}} F _ {i _ {1}} ^ {1 / 2} \right\| \cdot \left\| F _ {i _ {k}} ^ {1 / 2} x _ {m} \right\| \leqslant \left\{E \left\| x _ {m} ^ {\mathrm{T}} F _ {i _ {i}} ^ {1 / 2} \right\| ^ {2} \cdot E \left\| F _ {i _ {k}} ^ {1 / 2} x _ {m} \right\| ^ {2} \right\} ^ {1 / 2} \\ = \left\{E (x _ {m} ^ {\mathrm{T}} F _ {i _ {1}} x _ {m}) E (x _ {m} ^ {\mathrm{T}} F _ {i _ {k}} x _ {m}) \right\} ^ {1 / 2} \leqslant \max _ {m h + 1 \leqslant i \leqslant (m + 1) h} E (x _ {m} ^ {\mathrm{T}} F _ {i} x _ {m}) \leqslant \rho_ {m}. \\ \end{array}
$$

进一步，利用式(9.3.25)有

$$
\begin{array}{l} \frac {1}{2} > E \left\| \prod_ {i = m h + 1} ^ {(m + 1) h} (I - F _ {i}) \right\| \geqslant E x _ {m} ^ {\mathrm{T}} \prod_ {i = m h + 1} ^ {(m + 1) h} (I - F _ {i}) x _ {m} \\ = 1 - \sum_ {k = 1} ^ {h} \sum_ {m h + 1 \leqslant i _ {1} <   \dots <   i _ {k} \leqslant (m + 1) h} E \left(x _ {m} ^ {\mathrm{T}} F _ {i _ {1}} \dots F _ {i _ {k}} x _ {m}\right) \\ \geqslant 1 - \sum_ {k = 1} ^ {h} \sum_ {m h + 1 \leqslant i _ {1} <   \dots <   i _ {k} \leqslant (m + 1) h} \rho_ {m} = 1 - \sum_ {k = 1} ^ {h} \binom {h} {k} \rho_ {m}. \\ \end{array}
$$

上式意味着

$$\rho_ {m} \geqslant \frac {1}{2 \sum_ {k = 1} ^ {h} \binom {h} {k}}.$$

因此定理 9.3.6 证毕.

推论 9.3.3 设 $\{F_{k}, k \geqslant 0\}$ 是 $\phi-$ 混合随机矩阵序列， $F_{k} \in R^{d \times d}, 0 \leqslant F_{k} \leqslant I.$ 则下列三个性质等价：

(i) $\{F_k\} \in S_1$ ;

(ii) 存在某整数 $h_0 > 0$ 使

$$\delta \stackrel {\mathrm{def}} {=} \inf _ {m} \lambda_ {\min} \left\{\sum_ {i = m h _ {0} + 1} ^ {(m + 1) h _ {0}} E F _ {i} \right\} > 0;$$

(iii) 存在整数 $h > 0$ 使 $\{\lambda_k\} \in S^0$ , 其中 $\lambda_k$ 由 (9.3.15) 所定义, 而 $\mathcal{F}_k \stackrel{\mathrm{def}}{=} \sigma \{F_i, i \leqslant k\}$ .

证明 定理 9.3.5 证明了 (iii)⇒(i)，而定理 9.3.6 证明了 (i)⇒(ii). 因此我们只需证明 (ii)⇒(iii).

设 $\{F_k\}$ 的混合速度为 $\phi(k)$ , 利用 $\phi-$ 混合的性质 (4.3.11) 知对任何 $t, k$ , 有

$$\| E [ F _ {t + k} | \mathcal {F} _ {t} ] - E F _ {t + k} \| \leqslant 2 d \phi (k). \tag {9.3.26}$$

由于 $\phi (k)\to 0,$ 故可找到整数 $M > 0$ 使

$$\phi (k) \leqslant \frac {\delta}{4 (2 h _ {0} + 1) d}, \quad \forall k \geqslant M. \tag {9.3.27}$$

现令 $h = M + 2h_0 + 1$ ，于是利用(ii)及假设条件 $F_{i}\geqslant 0$ 易见

$$\lambda_ {\min} \left\{\sum_ {k = m h + 1 + M} ^ {(m + 1) h} E F _ {k} \right\} \geqslant \delta , \quad \forall m \geqslant 0. \tag {9.3.28}$$

最后，综合式(9.3.25)～式(9.3.27)得到对任何 $m \geqslant 0$ 有
