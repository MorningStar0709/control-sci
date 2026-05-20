$$
\begin{array}{l} (1 + h) \lambda_ {m} = \lambda_ {\min} \left\{E \left[ \sum_ {k = m h + 1} ^ {(m + 1) h} F _ {k} | \mathcal {F} _ {m h} \right] \right\} \geqslant \lambda_ {\min} \left\{E \left[ \sum_ {k = m h + 1 + M} ^ {(m + 1) h} F _ {k} | \mathcal {F} _ {m h} \right] \right\} \\ \geqslant \lambda_ {\min} \left\{E \left[ \sum_ {k = m h + 1 + M} ^ {(m + 1) h} F _ {k} \right] \right\} - \left\| E \left[ \sum_ {k = m h + 1 + M} ^ {(m + 1) h} F _ {k} \mid \mathcal {F} _ {m h} \right] - E \left[ \sum_ {k = m h + 1 + M} ^ {(m + 1) h} F _ {k} \right] \right\| \\ \geqslant \delta - (h - M) \frac {2 d \delta}{4 (2 h _ {0} + 1) d} \\ = \delta - \frac {\delta}{2} = \frac {\delta}{2} > 0. \\ \end{array}
$$

因此，我们实际上已证明了

$$\{\lambda_ {k} \} \in S ^ {0},$$

即 (iii) 成立证毕.

在自适应算法的分析中，经常遇到下列类型的随机差分方程

$$x _ {k + 1} = (I - \mu F _ {k}) x _ {k},$$

其中 $\mu \in (0,1)$ 称为算法步长 (stepsize), 当信号变化较慢时, $\mu$ 一般可以取得较小. 我们感兴趣的问题是: 若上式 $L_{p}$ 指数稳定, 则其收敛速度是如何依赖于 $\mu$ 的. 这一问题的研究对算法性能的分析是很关键的. 为此我们进一步引进几个记号.

1) 设 $p \geqslant 1$ , $F \stackrel{\mathrm{def}}{=} \{F_i\}$ . 记

$$M _ {p} = \left\{F: \sup _ {i} \| S _ {i} ^ {(T)} \| _ {p} = o (T), \quad \text { as } \quad T \to \infty \right\},$$

其中

$$S _ {i} ^ {(T)} \stackrel {\text { def }} {=} \sum_ {j = i T} ^ {(i + 1) T - 1} (F _ {j} - E [ F _ {j} ]);$$

2) 对任何 $d \times d$ 维随机矩阵序列 $F = \{F_k\}$ 及任何实数 $p \geqslant 1, \mu^* \in (0,1), L_p-$ 指数稳定族 $S_p(\mu^*)$ 由下式定义：

$$S _ {p} (\mu^ {*}) = \left\{F: \left\| \prod_ {j = i + 1} ^ {k} (I - \mu F _ {j}) \right\| _ {p} \leqslant M (1 - \mu \alpha) ^ {k - i}, \forall \mu \in (0, \mu^ {*} ], \right.\forall k \geqslant i \geqslant 0, \text {其中} M > 0 \text {和} \alpha \in (0, 1) \text {是常数} \Bigg \};$$

3) 类似地，平均指数稳定族 $S(\mu^{*})$ 由下式所定义：

$$S (\mu^ {*}) = \left\{F: \left\| \prod_ {j = i + 1} ^ {k} (I - \mu E (F _ {j})) \right\| \leqslant M (1 - \mu \alpha) ^ {k - i}, \forall \mu \in (0, \mu^ {*} ], \right.\forall k \geqslant i \geqslant 0, \text {其中} M > 0 \text {及} \alpha \in (0, 1) \text {是常数} \Bigg \}.$$

为方便起见，我们还进一步记

$$\bar {S} _ {p} \stackrel {\text { def }} {=} \bigcup_ {\mu^ {*} \in (0, 1)} S _ {p} (\mu^ {*}), \quad \bar {S} \stackrel {\text { def }} {=} \bigcup_ {\mu^ {*} \in (0, 1)} S (\mu^ {*}).$$

一般来讲，研究 $\bar{S}$ 要比研究 $\bar{S}_p$ 容易很多。下面的两个“随机平均定理”将说明 $\bar{S}$ 和 $\bar{S}_p$ 的关系。由于证明较长，在此省略。

定理9.3.7[22] 设随机矩阵序列 $\{F_k\} \in M_2$ ，则有

$$\{F _ {k} \} \in \bar {S} _ {2} \Rightarrow \{F _ {k} \} \in \bar {S}.$$

定理9.3.8[24] 设 $\{F_k\}$ 是随机矩阵序列，则

$$\{F _ {k} \} \in \bar {S} \Rightarrow \{F _ {k} \} \in \bar {S} _ {p}, p \geqslant 1$$

的充分条件是

1) 存在正常数 $\varepsilon, M, K$ 使得对任何 $n \geqslant 1$ 都有

$$E \left[ \exp \left(\varepsilon \sum_ {i = 1} ^ {n} \| F _ {j _ {i}} \|\right) \right] \leqslant M \exp (K n),$$

其中 $0 \leqslant j_{1} < j_{2} < \cdots < j_{n}$ 是任意 n 个整数；

2) 存在常数 $M > 0$ 及非降函数 $g(T)$ 满足， $g(T) = o(T), T \to \infty$ ，使对任何固定的 $T$ 及小的 $\mu > 0$ 有

$$E \left[ \exp \left(\mu \sum_ {j = i + 1} ^ {n} \| S _ {j} ^ {(T)} \|\right) \right] \leqslant M \exp \{[ \mu g (T) + o (\mu) ] (n - i) \},$$

其中 $S_{j}^{(T)}$ 由前述定义.

定理 9.3.8 说明在一定条件下，随机矩阵乘积的指数收敛性可以用相应的确定性矩阵乘积的指数收敛性来保证.
