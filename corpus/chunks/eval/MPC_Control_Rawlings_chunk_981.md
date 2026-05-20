# Example C.3: DP applied to linear quadratic regulator

A much used example is the familiar linear quadratic regulator problem. The system is defined by

$$x ^ {+} = A x + B u$$

There are no constraints. The cost function is defined by (C.2) where

$$\ell (x, u) := (1 / 2) x ^ {\prime} Q x + (1 / 2) u ^ {\prime} R u$$

and $V _ { f } ( x ) = 0$ for all x; the horizon length is N. We assume that Q is symmetric and positive semidefinite and that R is symmetric and positive definite. The DP recursion is

$$V ^ {0} (x, i) = \min _ {u} \{\ell (x, u) + V ^ {0} (A x + B u, i + 1) \} \forall x \in \mathbb {R} ^ {n}$$

with terminal condition

$$V ^ {0} (x, N) = 0 \forall x \in \mathbb {R} ^ {n}$$

Assume that $V ^ { 0 } ( \cdot , i + 1 )$ is quadratic and positive semidefinite and, therefore, has the form

$$V ^ {0} (x, i + 1) = (1 / 2) x ^ {\prime} P (i + 1) x$$

where $P ( i + 1 )$ is symmetric and positive semidefinite. Then

$$V ^ {0} (x, i) = (1 / 2) \min _ {u} \left\{x ^ {\prime} Q x + u ^ {\prime} R u + (A x + B u) ^ {\prime} P (i + 1) (A x + B u) \right\}$$

The right-hand side of the last equation is a positive definite function of u for all x, so that it has a unique minimizer given by

$$\kappa (x, i) = K (i) x \quad K (i) := - \left(B ^ {\prime} P (i + 1) B + R\right) ^ {- 1} B ^ {\prime} P (i + 1)$$

Substituting $u = K ( i ) x$ in the expression for $V ^ { 0 } ( x , i )$ yields

$$V ^ {0} (x, i) = (1 / 2) x ^ {\prime} P (i) x$$

where P (i) is given by:

$$P (i) = Q + K (i) ^ {\prime} R K (i) - A ^ {\prime} P (i + 1) B \left(B ^ {\prime} P (i + 1) B + R\right) ^ {- 1} B ^ {\prime} P (i + 1) A$$

Hence $V ^ { 0 } ( \cdot , i )$ is quadratic and positive semidefinite if $V ^ { 0 } ( \cdot , i + 1 )$ is. But $V ^ { 0 } ( \cdot , N )$ , defined by

$$V ^ {0} (x, N) := (1 / 2) x ^ {\prime} P (N) x = 0 \quad P (N) := 0$$

is symmetric and positive semidefinite. By induction $V ^ { 0 } ( \cdot , i )$ is quadratic and positive semidefinite (and $P ( i )$ is symmetric and positive semidefinite) for all $i \in \{ 0 , 1 , \ldots , N \}$ . Substituting $K ( i ) = - ( B ^ { \prime } P ( i +$ $1 ) B + R ) ^ { - 1 } B ^ { \prime } P ( i + 1 ) A$ in the expression for $P ( i )$ yields the more familiar matrix Riccati equation

$$P (i) = Q + A ^ {\prime} P (i + 1) A - A ^ {\prime} P (i + 1) B \left(B ^ {\prime} P (i + 1) B + R\right) ^ {- 1} B P (i + 1) A$$

\-
