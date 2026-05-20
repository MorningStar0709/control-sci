# An Alternative Test

An alternative test for SPR for a system with a proper transfer function can be obtained from the proof of the Kalman-Yakubovich lemma. Write the matrix A in controllable canonical form. Solve the equations

$$
A ^ {T} P + P A = \left( \begin{array}{c c c c} q _ {1} & 0 & \dots & 0 \\ 0 & q _ {2} & \dots & 0 \\ \vdots & & & \\ 0 & 0 & \dots & q _ {n} \end{array} \right)
B ^ {T} P = C
$$

where P is a symmetric matrix. This gives $n + n(n + 1)/2$ equations for the unknown elements of P and Q. The transfer function is SPR if $q_{i} > 0$ for $i = 1, \ldots, n$ .
