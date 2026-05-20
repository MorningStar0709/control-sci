$$
T = \left[ \begin{array}{l l} I & \tilde {P} \\ 0 & I \end{array} \right]
$$

Hence $\left\| E _ { 1 1 } \right\| _ { \infty } \le \left\| E \right\| _ { \infty } = 2 \sigma _ { N }$ , which is the desired result.

The remainder of the proof is achieved by using the order reduction by one-step results and by noting that $G _ { k } ( s ) = \left[ { \frac { A _ { 1 1 } \left. B _ { 1 } \right. } { C _ { 1 } } } \right]$ B1 obtained by the “kth” order partitioning is internally balanced with balanced Gramian given by

$$\Sigma_ {1} = \mathrm{diag} (\sigma_ {1} I _ {s _ {1}}, \sigma_ {2} I _ {s _ {2}}, \ldots , \sigma_ {k} I _ {s _ {k}})$$

Let $E _ { k } ( s ) = G _ { k + 1 } ( s ) - G _ { k } ( s )$ for $k = 1 , 2 , \ldots , N - 1$ and let $G _ { N } ( s ) = G ( s )$ . Then

$$\overline {{{\sigma}}} \left[ E _ {k} (j \omega) \right] \leq 2 \sigma_ {k + 1}$$

since $G _ { k } ( s )$ is a reduced-order model obtained from the internally balanced realization of $G _ { k + 1 } ( s )$ and the bound for one-step order reduction holds.

Noting that

$$G (s) - G _ {r} (s) = \sum_ {k = r} ^ {N - 1} E _ {k} (s)$$

by the definition of $E _ { k } ( s )$ , we have

$$\overline {{{{\sigma}}}} \left[ G (j \omega) - G _ {r} (j \omega) \right] \leq \sum_ {k = r} ^ {N - 1} \overline {{{{\sigma}}}} \left[ E _ {k} (j \omega) \right] \leq 2 \sum_ {k = r} ^ {N - 1} \sigma_ {k + 1}$$

This is the desired upper bound.

A useful consequence of the preceding theorem is the following corollary.

Corollary 7.12 Let $\sigma _ { i } , i = 1 , \ldots , N$ be the Hankel singular values of $G ( s ) \in \mathcal { R } \mathcal { H } _ { \infty }$ . Then

$$\left\| G (s) - G (\infty) \right\| _ {\infty} \leq 2 \left(\sigma_ {1} + \dots + \sigma_ {N}\right)$$

The above bound can be tight for some systems.

Example 7.4 Consider an nth-order transfer function

$$G (s) = \sum_ {i = 1} ^ {n} \frac {b _ {i}}{s + a _ {i}},$$

with $a _ { i } > 0$ and $b _ { i } > 0$ . Then $\begin{array} { r } { \left. G ( s ) \right. _ { \infty } = G ( 0 ) = \sum _ { i = 1 } ^ { n } b _ { i } / a _ { i } } \end{array}$ and $G ( s )$ has the following state-space realization:

$$
G = \left[ \begin{array}{c c c c c} - a _ {1} & & & & \sqrt {b _ {1}} \\ & - a _ {2} & & & \sqrt {b _ {2}} \\ & & \ddots & & \vdots \\ & & & - a _ {n} & \sqrt {b _ {n}} \\ \hline \sqrt {b _ {1}} & \sqrt {b _ {2}} & \dots & \sqrt {b _ {n}} & 0 \end{array} \right]
$$

and the controllability and observability Gramians of the realization are given by

$$P = Q = \left[ \frac {\sqrt {b _ {i} b _ {j}}}{a _ {i} + a _ {j}} \right]$$

It is easy to see that $\sigma _ { i } = \lambda _ { i } ( P ) = \lambda _ { i } ( Q )$ and
