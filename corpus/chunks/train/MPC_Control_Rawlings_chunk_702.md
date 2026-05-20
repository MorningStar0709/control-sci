$$
\begin{array}{l} x _ {1} ^ {+} = A _ {1} x _ {1} + \overline {{B}} _ {1 1} u _ {1} + \overline {{B}} _ {1 2} u _ {2} \quad x _ {2} ^ {+} = A _ {2} x _ {2} + \overline {{B}} _ {2 1} u _ {1} + \overline {{B}} _ {2 2} u _ {2} \\ \mathbf {u} _ {1} ^ {+} = g _ {1} ^ {p} \left(x _ {1}, x _ {2}, \mathbf {u} _ {1}, \mathbf {u} _ {2}\right) \quad \mathbf {u} _ {2} ^ {+} = g _ {2} ^ {p} \left(x _ {1}, x _ {2}, \mathbf {u} _ {1}, \mathbf {u} _ {2}\right) \\ \end{array}
$$

We have the following cost using the warm start at the next sample

$$
\begin{array}{l} V (x _ {1} ^ {+}, x _ {2} ^ {+}, \tilde {\mathbf {u}} _ {1} ^ {+}, \tilde {\mathbf {u}} _ {2} ^ {+}) = V (x _ {1}, x _ {2}, \mathbf {u} _ {1}, \mathbf {u} _ {2}) - \rho_ {1} \ell_ {1} (x _ {1}, u _ {1}) - \rho_ {2} \ell_ {2} (x _ {2}, u _ {2}) \\ + (1 / 2) \rho_ {1} x _ {1} (N) ^ {\prime} \left[ A _ {1} ^ {\prime} P _ {1 f} A _ {1} - P _ {1 f} + Q _ {1} \right] x _ {1} (N) \\ + (1 / 2) \rho_ {2} x _ {2} (N) ^ {\prime} \left[ A _ {2} ^ {\prime} P _ {2 f} A _ {2} - P _ {2 f} + Q _ {2} \right] x _ {2} (N) \\ \end{array}
$$

Using the Schur decomposition (6.19) and the constraints $S _ { j i } ^ { u \prime } x _ { j i } ( N ) =$ 0 for $i , j \in \mathbb { I } _ { 1 : 2 }$ , the last two terms can be written as

$$
\begin{array}{l} (1 / 2) \rho_ {1} x _ {1} (N) ^ {\prime} S _ {1} ^ {s} \left[ A _ {1} ^ {s ^ {\prime}} \Sigma_ {1} A _ {1} ^ {s} - \Sigma_ {1} + S _ {1} ^ {s ^ {\prime}} Q _ {1} S _ {1} ^ {s} \right] S _ {1} ^ {s ^ {\prime}} x _ {1} (N) \\ + (1 / 2) \rho_ {2} x _ {2} (N) ^ {\prime} S _ {2} ^ {s} \left[ A _ {2} ^ {s ^ {\prime}} \Sigma_ {2} A _ {2} ^ {s} - \Sigma_ {2} + S _ {2} ^ {s ^ {\prime}} Q _ {2} S _ {2} ^ {s} \right] S _ {2} ^ {s ^ {\prime}} x _ {2} (N) \\ \end{array}
$$

These terms are zero because of (6.20). Using this result and applying the iteration for the controllers gives

$$V (x _ {1} ^ {+}, x _ {2} ^ {+}, \mathbf {u} _ {1} ^ {+}, \mathbf {u} _ {2} ^ {+}) \leq V (x _ {1}, x _ {2}, \mathbf {u} _ {1}, \mathbf {u} _ {2}) - \rho_ {1} \ell_ {1} (x _ {1}, u _ {1}) - \rho_ {2} \ell_ {2} (x _ {2}, u _ {2})$$

The Lyapunov stability constraints give (see also Exercise 6.28)

$$\left| \left(\mathbf {u} _ {1}, \mathbf {u} _ {2}\right) \right| \leq 2 \max \left(d _ {1}, d _ {2}\right) \left| \left(x _ {1}, x _ {2}\right) \right| \quad \left(x _ {1}, x _ {2}\right) \in r \mathcal {B}$$

Given the cost decrease and this constraint on the size of the input sequence, we satisfy the conditions of Lemma 6.4, and conclude the solution $x ( k ) = 0$ for all k is exponentially stable on all of $x _ { N }$ if either $x _ { N }$ is compact or U is compact.
