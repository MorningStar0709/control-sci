# 11.3 Coprime Factorization Approach

In this section, all stabilizing controller parameterization will be derived using the conventional coprime factorization approach. Readers should be familiar with the results presented in Section 5.4 of Chapter 5 before preceding further.

Theorem 11.6 Let $G _ { 2 2 } = N M ^ { - 1 } = \tilde { M } ^ { - 1 } \tilde { N }$ be the rcf and lcf of $G _ { 2 2 }$ over $\mathcal { R H } _ { \infty }$ , respectively. Then the set of all proper controllers achieving internal stability is parameterized either by

$$K = (U _ {0} + M Q _ {r}) (V _ {0} + N Q _ {r}) ^ {- 1}, \det (I + V _ {0} ^ {- 1} N Q _ {r}) (\infty) \neq 0 \tag {11.5}$$

for $Q _ { r } \in \mathcal { R } \mathcal { H } _ { \infty }$ or by

$$K = (\tilde {V} _ {0} + Q _ {l} \tilde {N}) ^ {- 1} (\tilde {U} _ {0} + Q _ {l} \tilde {M}), \det (I + Q _ {l} \tilde {N} \tilde {V} _ {0} ^ {- 1}) (\infty) \neq 0 \tag {11.6}$$

for $Q _ { l } \in \mathcal { R } \mathcal { H } _ { \infty }$ , where $U _ { 0 } , V _ { 0 } , \tilde { U } _ { 0 } , \tilde { V } _ { 0 } \in \mathcal { R } \mathcal { H } _ { \infty }$ satisfy the Bezout identities:

$$\tilde {V} _ {0} M - \tilde {U} _ {0} N = I, \quad \tilde {M} V _ {0} - \tilde {N} U _ {0} = I.$$

Moreover, $i f U _ { 0 } , V _ { 0 } , \tilde { U } _ { 0 }$ , and $\tilde { V _ { 0 } }$ are chosen such that $U _ { 0 } V _ { 0 } ^ { - 1 } = \tilde { V } _ { 0 } ^ { - 1 } \tilde { U } _ { 0 }$ ; that is,

$$
\left[ \begin{array}{c c} \tilde {V} _ {0} & - \tilde {U} _ {0} \\ - \tilde {N} & \tilde {M} \end{array} \right] \left[ \begin{array}{c c} M & U _ {0} \\ N & V _ {0} \end{array} \right] = \left[ \begin{array}{c c} I & 0 \\ 0 & I \end{array} \right]
$$

then

$$
\begin{array}{l} K = (U _ {0} + M Q _ {y}) (V _ {0} + N Q _ {y}) ^ {- 1} \\ = \left(\tilde {V} _ {0} + Q _ {y} \tilde {N}\right) ^ {- 1} \left(\tilde {U} _ {0} + Q _ {y} \tilde {M}\right) \\ = \mathcal {F} _ {\ell} (J _ {y}, Q _ {y}) \tag {11.7} \\ \end{array}
$$

where

$$
J _ {y} := \left[ \begin{array}{c c} U _ {0} V _ {0} ^ {- 1} & \tilde {V} _ {0} ^ {- 1} \\ V _ {0} ^ {- 1} & - V _ {0} ^ {- 1} N \end{array} \right] \tag {11.8}
$$

and where $Q _ { y }$ ranges over $\mathcal { R H } _ { \infty }$ such that $( I + V _ { 0 } ^ { - 1 } N Q _ { y } ) ( \infty )$ is invertible.

Proof. We shall prove the parameterization given in equation (11.5) first. Assume that K has the form indicated, and define

$$U := U _ {0} + M Q _ {r}, V := V _ {0} + N Q _ {r}.$$

Then

$$\tilde {M} V - \tilde {N} U = \tilde {M} (V _ {0} + N Q _ {r}) - \tilde {N} (U _ {0} + M Q _ {r}) = \tilde {M} V _ {0} - \tilde {N} U _ {0} + (\tilde {M} N - \tilde {N} M) Q _ {r} = I.$$

Thus K achieves internal stability by Lemma 5.7.
