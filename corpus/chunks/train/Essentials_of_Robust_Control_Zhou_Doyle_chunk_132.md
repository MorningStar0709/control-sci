$$
\left[ \begin{array}{c c} M & U \\ N & V \end{array} \right] ^ {- 1} \in \mathcal {R H} _ {\infty}
$$

This proves the equivalence of conditions 1 and 2. The equivalence of conditions 1 and 3 is proved similarly.

Conditions 4 and 5 are implied by conditions 2 and 3 from the following equation:

$$
\left[ \begin{array}{c c} \tilde {V} & - \tilde {U} \\ - \tilde {N} & \tilde {M} \end{array} \right] \left[ \begin{array}{c c} M & U \\ N & V \end{array} \right] = \left[ \begin{array}{c c} \tilde {V} M - \tilde {U} N & 0 \\ 0 & \tilde {M} V - \tilde {N} U \end{array} \right]
$$

Since the left-hand side of the above equation is invertible in $\mathcal { R } \mathcal { H } _ { \infty }$ , so is the right-hand side. Hence, conditions 4 and 5 are satisfied. We only need to show that either condition 4 or condition 5 implies condition 1. Let us show that condition 5 implies condition 1; this is obvious since

$$
\begin{array}{l} \left[ \begin{array}{c c} I & \hat {K} \\ P & I \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} I & \tilde {V} ^ {- 1} \tilde {U} \\ N M ^ {- 1} & I \end{array} \right] ^ {- 1} \\ = \left[ \begin{array}{c c} M & 0 \\ 0 & I \end{array} \right] \left[ \begin{array}{c c} \tilde {V} M & \tilde {U} \\ N & I \end{array} \right] ^ {- 1} \left[ \begin{array}{c c} \tilde {V} & 0 \\ 0 & I \end{array} \right] \in \mathcal {R H} _ {\infty} \\ \end{array}
$$

$\mathrm { i f } \left[ \begin{array} { c c } { \tilde { V } M } & { \tilde { U } } \\ { N } & { I } \end{array} \right] ^ { - 1 } \in \mathscr { R } \mathscr { H } _ { \infty }$ or if condition 5 is satisfied.

![](image/ffd3adabb4e3ba4aba110fa02f67a75ff4e3908f2a63a2c179056234f9d51944.jpg)

Combining Lemma 5.7 and Theorem 5.6, we have the following corollary.

Corollary 5.8 Let P be a proper real rational matrix and $P = N M ^ { - 1 } = \tilde { M } ^ { - 1 } \tilde { N }$ be the corresponding rcf and lcf over $\mathcal { R } \mathcal { H } _ { \infty }$ . Then there exists a controller

$$\hat {K} _ {0} = U _ {0} V _ {0} ^ {- 1} = \tilde {V} _ {0} ^ {- 1} \tilde {U} _ {0}$$

with $U _ { 0 } , V _ { 0 } , \tilde { U } _ { 0 }$ , and $\tilde { V _ { 0 } }$ in $\mathcal { R H } _ { \infty }$ such that

$$
\left[ \begin{array}{c c} \tilde {V} _ {0} & - \tilde {U} _ {0} \\ - \tilde {N} & \tilde {M} \end{array} \right] \left[ \begin{array}{c c} M & U _ {0} \\ N & V _ {0} \end{array} \right] = \left[ \begin{array}{c c} I & 0 \\ 0 & I \end{array} \right] \tag {5.13}
$$
