# 7.3.1 Preliminaries

The parametric quadratic program $\mathbb { P } ( x )$ is defined by

$$V ^ {0} (x) = \min _ {u} \{V (x, u) | (x, u) \in \mathbb {Z} \}$$

where $\boldsymbol { x } \in \mathbb { R } ^ { n }$ and $u \in \mathbb { R } ^ { m }$ . The cost function V (·) is defined by

$$V (x, u) := (1 / 2) x ^ {\prime} Q x + u ^ {\prime} S x + (1 / 2) u ^ {\prime} R u + q ^ {\prime} x + r ^ {\prime} u + c$$

and the polyhedral constraint set Z is defined by

$$\mathbb {Z} := \{(x, u) \mid M x \leq N u + p \}$$

where $M \in \mathbb { R } ^ { r \times n } , N \in \mathbb { R } ^ { r \times m }$ and $\boldsymbol { p } \in \mathbb { R } ^ { r }$ ; thus Z is defined by r affine inequalities. Let $u ^ { 0 } ( x )$ denote the solution of $\mathbb { P } ( x )$ if it exists, i.e., if $x \in { \mathcal { X } }$ , the domain of $V ^ { 0 } ( \cdot )$ ; thus

$$u ^ {0} (x) := \arg \min _ {u} \{V (x, u) \mid (x, u) \in \mathbb {Z} \}$$

The solution $u ^ { 0 } ( x )$ is unique if $V ( \cdot )$ is strictly convex in u; this is the case if R is positive definite. Let the matrix Q be defined by

$$
\mathcal {Q} := \left[ \begin{array}{c c} Q & S ^ {\prime} \\ S & R \end{array} \right]
$$

For simplicity we assume, in the sequel:

Assumption 7.3 (Strict convexity). The matrix Q is positive definite.

Assumption 7.3 implies that both R and Q are positive definite. The cost function V (·) may be written in the form

$$V (x, u) = (1 / 2) (x, u) ^ {\prime} \mathcal {Q} (x, u) + q ^ {\prime} x + r ^ {\prime} u + c$$

where, as usual, the vector $( x , u )$ is regarded as a column vector $( x ^ { \prime } , u ^ { \prime } ) ^ { \prime }$ in algebraic expressions. The parametric quadratic program may also be expressed as

$$V ^ {0} (x) := \min _ {u} \{V (x, u) \mid u \in \mathcal {U} (x) \}$$

where the parametric constraint set $\mathcal { U } ( x )$ is defined by

$$\mathcal {U} (x) := \{u \mid (x, u) \in \mathbb {Z} \} = \{u \in \mathbb {R} ^ {m} \mid M u \leq N x + p \}$$

For each x the set $\mathcal { U } ( x )$ is polyhedral. The domain X of $V ^ { 0 } ( \cdot )$ and $u ^ { 0 } ( \cdot )$ is defined by

$$\mathcal {X} := \{x \mid \exists u \in \mathbb {R} ^ {m} \text { such that } (\mathrm{x}, \mathrm{u}) \in \mathbb {Z} \} = \{x \mid \mathcal {U} (x) \neq \emptyset \}$$

For all $( x , u ) \in \mathbb { Z }$ , let the index set $I ( x , u )$ specify the constraints that are active at $( x , u )$ , i.e.,

$$I (x, u) := \{i \in \mathbb {I} _ {1: r} \mid M _ {i} u = N _ {i} x + p _ {i} \}$$
