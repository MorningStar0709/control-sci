# 16.6 Problems

Problem 16.1 Consider a feedback system with $G ( s ) = { \frac { 1 } { s - 2 } }$ . Compute by hand $\epsilon _ { \mathrm { m a x } } .$ the maximum stability radius for a normalized coprime factor perturbation of $G ( s )$ .

Problem 16.2 In Corollary 16.2, find the parameterization of all $\mathcal { H } _ { \infty }$ controllers.

Problem 16.3 Let $P _ { \Delta } = ( N + \Delta _ { N } ) ( M + \Delta _ { M } ) ^ { - 1 }$ be a right coprime factor perturbed plant with a nominal plant $P = N M ^ { - 1 }$ , where $( N , M )$ is a pair of normalized right coprime factorization. Formulate the corresponding robust stabilization problem as an $\mathcal { H } _ { \infty }$ control problem and find a stabilizing controller using the $\mathcal { H } _ { \infty }$ formulas in Chapter 14. Are there any connections between this stabilizing controller and the controller obtained in this chapter for left coprime stabilization?

Problem 16.4 Let P have coprime factorizations $P = N M ^ { - 1 } = \tilde { M } ^ { - 1 } \tilde { N }$ . Then there exist $U , V , \tilde { U } , \tilde { V } \in \mathcal { H } _ { \infty }$ such that

$$
\left[ \begin{array}{c c} M & U \\ N & V \end{array} \right] \left[ \begin{array}{c c} \tilde {V} & - \tilde {U} \\ \tilde {N} & \tilde {M} \end{array} \right] = I.
$$

Furthermore, all stabilizing controllers for P can be written as

$$K = (U + M Q) (V + N Q) ^ {- 1}, \quad Q \in \mathcal {H} _ {\infty}.$$

Show that

$$
\left[ \begin{array}{c} K \\ I \end{array} \right] (I + P K) ^ {- 1} \tilde {M} ^ {- 1} = \left[ \begin{array}{c} U + M Q \\ V + N Q \end{array} \right].
$$

Suppose $P = N M ^ { - 1 } = \tilde { M } ^ { - 1 } \tilde { N }$ are normalized coprime factorizations. Show that

$$
b _ {P, K} ^ {- 1} = \left\| \left[ \begin{array}{c} U \\ V \end{array} \right] + \left[ \begin{array}{c} M \\ N \end{array} \right] Q \right\| _ {\infty} = \left\| \left[ \begin{array}{c} R + Q \\ I \end{array} \right] \right\| _ {\infty}
$$

where $R = { \cal M } ^ { \sim } U + { \cal N } ^ { \sim } V$ .

Problem 16.5 Let K be a controller that stabilizes the plant P . Show that
