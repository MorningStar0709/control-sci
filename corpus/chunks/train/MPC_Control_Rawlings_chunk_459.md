This result can be established directly using the Hautus lemma and is left as an exercise. This lemma and the duality variables allows us to translate stability conditions for infinite horizon regulation problems into stability conditions for full information estimation problems and vice versa. For example, the following is a basic theorem covering convergence of Riccati equations in the form that is useful in establishing exponential stability of regulation as discussed in Chapter 1.

Theorem 4.10 (Riccati iteration and regulator stability). Given (A, B) stabilizable, (A, C) detectable, $Q > 0 , R > 0 , P f \geq 0 $ , and the discrete

Riccati equation

$$
\begin{array}{l} \Pi (k - 1) = C ^ {\prime} Q C + A ^ {\prime} \Pi (k) A - \\ A ^ {\prime} \Pi (k) B \left(B ^ {\prime} \Pi (k) B + R\right) ^ {- 1} B ^ {\prime} \Pi (k) A, \quad k = N, \dots , 1 \\ \end{array}
\Pi (N) = P _ {f}
$$

Then

(a) There exists $\Pi \geq 0$ such that for every $P _ { f } \geq 0$

$$\lim _ {k \to - \infty} \Pi (k) = \Pi$$

and Π is the unique solution of the steady-state Riccati equation

$$\Pi = C ^ {\prime} Q C + A ^ {\prime} \Pi A - A ^ {\prime} \Pi B (B ^ {\prime} \Pi B + R) ^ {- 1} B ^ {\prime} \Pi A$$

among the class of positive semidefinite matrices.

(b) The matrix A + BK in which

$$K = - (B ^ {\prime} \Pi B + R) ^ {- 1} B ^ {\prime} \Pi A$$

is a stable matrix.

Bertsekas (1987, pp.59–64) provides a proof for a slightly different version of this theorem. Exercise 4.13 explores translating this theorem into the form that is useful for establishing exponential convergence of full information estimation.
