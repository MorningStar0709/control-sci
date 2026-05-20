# 7.5 Parametric Piecewise Quadratic Programming

The parametric quadratic program $\mathbb { P } ( x )$ is defined, as before, by

$$V ^ {0} (x) = \min _ {u} \{V (x, u) \mid (x, u) \in \mathbb {Z} \} \tag {7.14}$$

where $x \in \mathcal { X } \subset \mathbb { R } ^ { n }$ and $u \in \mathbb { R } ^ { m }$ , but now the cost function $V ( \cdot )$ is assumed to be continuous, strictly convex, and piecewise quadratic on a polytopic partition ${ \mathcal { P } } = \{ \mathbb { Z } _ { i } \mid i \in { \mathcal { I } } \}$ of the set Z so that

$$V (z) = V _ {i} (z) = (1 / 2) z ^ {\prime} \mathcal {Q} _ {i} z + s _ {i} ^ {\prime} z + c _ {i}$$

for all $z \in \mathbb { Z } _ { i }$ , all $i \in { \mathcal { I } }$ where I is an index set. In (7.14), the matrix $Q _ { i }$ and the vector $s _ { i }$ have the structure

$$
\mathcal {Q} _ {i} = \left[ \begin{array}{c c} Q _ {i} & S _ {i} ^ {\prime} \\ S _ {i} & R _ {i} \end{array} \right] \qquad s _ {i} = \left[ \begin{array}{c} q _ {i} \\ r _ {i} \end{array} \right]
$$

so that for all $i \in { \mathcal { I } }$

$$V _ {i} (x, u) = (1 / 2) x ^ {\prime} Q _ {i} x + u ^ {\prime} S _ {i} x + (1 / 2) u ^ {\prime} R _ {i} u + q _ {i} ^ {\prime} x + r _ {i} ^ {\prime} u + c$$

For each x, the function $u \mapsto V _ { i } ( x , u )$ is quadratic and depends on x. The constraint set Z is defined, as above, by

$$\mathbb {Z} := \{(x, u) \mid M u \leq N x + p \}$$

Let $u ^ { 0 } ( x )$ denote the solution of $\mathbb { P } ( x )$ , i.e.,

$$u ^ {0} (x) = \arg \min _ {u} \{V (x, u) \mid (x, u) \in \mathbb {Z} \}$$

The solution $u ^ { 0 } ( x )$ is unique if $V ( \cdot )$ is strictly convex in u at each x; this is the case if each $R _ { i }$ is positive definite. The parametric piecewise quadratic program may also be expressed, as before, as

$$
\begin{array}{l} V ^ {0} (x) = \min _ {u} \{V (x, u) \mid u \in \mathcal {U} (x) \} \\ u ^ {0} (x) = \arg \min _ {u} \{V (x, u) \mid u \in \mathcal {U} (x) \} \\ \end{array}
$$

where the parametric constraint set $\mathcal { U } ( x )$ is defined by

$$\mathcal {U} (x) := \{u \mid (x, u) \in \mathbb {Z} \} = \{u \mid M u \leq N x + p \}$$

Let $\boldsymbol { x } \subset \mathbb { R } ^ { n }$ be defined by

$$\mathcal {X} := \{x \mid \exists u \text { such that } (x, u) \in \mathbb {Z} \} = \{x \mid \mathcal {U} (x) \neq \emptyset \}$$

The set X is the domain of $V ^ { 0 } ( \cdot )$ and of $u ^ { 0 } ( \cdot )$ and is thus the set of points x for which a feasible solution of P(x) exists; it is the projection of Z, which is a set in (x, u)-space, onto x-space as shown in Figure 7.1. We make the following assumption in the sequel.
