where we have used the fact that $| a + b | \geq | a | - | b |$ . By the assumption of observability

$$\sum_ {j = k} ^ {k + N} \left| h (x (j; x (k), u)) - h (x (j; z (k), u)) \right| \geq \alpha (| x (k) - z (k) |)$$

for all k. From Lemma B.48 and the Lipschitz assumption on $h ( \cdot )$

$$
\begin{array}{l} \left| h (x (j; z (k), u)) - h (z (j; z (k), u, w)) \right| \leq \\ c \left| x (j; z (k), u) - z (j; z (k), u, w) \right| \leq c \sum_ {i = k} ^ {j - 1} c ^ {j - 1 - i} | w (i) | \\ \end{array}
$$

for all j in $\{ k + 1 , k + 2 , \ldots k + N \}$ . Hence there exists a $d \in ( 0 , \infty )$ such that the last term in (B.17) satisfies

$$\sum_ {j = k} ^ {k + N} \left| h (x (j; x (k), u)) - h (x (j; z (k), u)) \right| \leq d \| w \| _ {k - N: k}$$

Hence, (B.17) becomes

$$\alpha (| x (k) - z (k) |) \leq N \| v \| _ {k - N: k} + d \| w \| _ {k - N: k}$$

Since, by assumption, $w ( k ) \to 0$ and $\nu ( k ) \to 0$ as $k \to \infty$ , and $\alpha ( \cdot ) \in \mathcal K$ , it follows that $| x ( k ) - z ( k ) | \to 0$ as $k \to \infty$ .
