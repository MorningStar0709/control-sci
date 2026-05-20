# A.10 Sequences

Let the set of nonnegative integers be denoted by $ { \mathbb { I } } _ { \geq 0 }$ . A sequence is a function from $ { \mathbb { I } } _ { \geq 0 }$ into $\mathbb { R } ^ { n }$ . We denote a sequence by the set of its values, $\{ x _ { i } \mid i \in \mathbb { I } _ { \geq 0 } \}$ . A subsequence of $\{ x _ { i } \mid i \in \mathbb { I } _ { \geq 0 } \}$ is a sequence of the form $\{ x _ { i } \mid i \in K \}$ , where K is an infinite subset of $ { \mathbb { I } } _ { \geq 0 }$ .

A sequence $\{ x _ { i } \mid i \in \mathbb { I } _ { \geq 0 } \}$ in $\mathbb { R } ^ { n }$ is said to converge to a point $\hat { x }$ if lim $\vert { \boldsymbol { i } } _ { i \to \infty } \left. { \boldsymbol { x } } _ { i } - { \hat { \boldsymbol { x } } } \right. = 0 , \mathrm { i . e . , }$ , if, for all $\delta > 0$ , there exists an integer k such that $| x _ { i } - { \hat { x } } | \leq \delta$ for all $i \geq k ;$ ; we write $x _ { i } \to { \hat { x } }$ as $i  \infty$ to denote the fact that the sequence $\{ x _ { i } \}$ converges to xˆ. The point xˆ is called a limit of the sequence $\{ x _ { i } \}$ . A point $x ^ { * }$ is said to be an accumulation point of a sequence $\{ x _ { i } \mid i \in \mathbb { I } _ { \geq 0 } \}$ in $\mathbb { R } ^ { n }$ , if there exists an infinite subset $K \subset \mathbb { I } _ { \geq 0 }$ such that $x _ { i } \to x ^ { * }$ as $i \to \infty , i \in K$ in which case we say $x _ { i } \stackrel { K } {  } x ^ { * } . ^ { 5 }$

Let $\{ x _ { i } \}$ be a bounded infinite sequence in R and let the S be the set of all accumulation points of $\{ x _ { i } \}$ . Then S is compact and lim sup $x _ { i }$ is the largest and lim inf $x _ { i }$ the smallest accumulation point of $\{ x _ { i } \}$ :

$$
\begin{array}{l} \underset {i \to \infty} {\text { lim   sup }} x _ {i} := \max \{x \mid x \in S \}, \text { and } \\ \underset {i \to \infty} {\text { lim   inf }} x _ {i} := \min \{x \mid x \in S \} \end{array}
$$

Theorem A.3 (Bolzano-Weierstrass). Suppose $X \subset \mathbb { R } ^ { n }$ is compact and $\{ x _ { i } \mid i \in \mathbb { I } _ { \geq 0 } \} \subseteq X$ . Then $\{ x _ { i } \mid i \in \mathbb { I } _ { \geq 0 } \}$ must have at least one accumulation point.

From Exercise A.7, it follows that the accumulation point postulated by Theorem A.3 lies in X. In proving asymptotic stability we need the following property of monotone sequences.
