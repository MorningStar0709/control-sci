Assumption 7.14 (Continuous, piecewise quadratic function). The function V (·) is continuous, strictly convex, and piecewise quadratic on the polytopic partition $\mathcal { P } = \{ \mathbb { Z } _ { i } \ | \ i \in \mathcal { I } : = \mathbb { I } _ { 1 : q } \}$ of the polytope $\mathbb { Z }$ in $\mathbb { R } ^ { n } \times \mathbb { R } ^ { m }$ ; $V ( x , u ) = V _ { i } ( x , u )$ where $V _ { i } ( \cdot )$ is a positive definite quadratic function of $( x , u )$ for all $( x , u ) \in \mathbb { Z } _ { i }$ , all $i \in { \mathcal { I } }$ , and $q$ is the number of constituent polytopes in ${ \mathcal { P } } .$

The assumption of continuity places restrictions on the quadratic functions $V _ { i } ( \cdot ) , i \in \mathcal { I }$ . For example, we must have $V _ { i } ( z ) = V _ { j } ( z )$ for all $z \in \mathbb { Z } _ { i } \cap \mathbb { Z } _ { j }$ . Assumption 7.14 implies that the piecewise quadratic programming problem $\mathbb { P } ( x )$ satisfies the hypotheses of Theorem C.34 so that the value function $V ^ { 0 } ( \cdot )$ is continuous. It follows from Assumption 7.14 and Theorem C.34 that $V ^ { 0 } ( \cdot )$ is strictly convex and continuous and that the minimizer $u ^ { 0 } ( \cdot )$ is continuous. Assumption 7.14 implies that $Q _ { i }$ is positive definite for all $i \in { \mathcal { I } }$ . For each $x ,$ , let the set $\mathcal { U } ( x )$ be defined by

$$\mathcal {U} (x) := \{u \mid (x, u) \in \mathbb {Z} \}$$

Thus $\mathcal { U } ( x )$ is the set of admissible u at x, and $\mathbb { P } ( x )$ may be expressed in the form $V ^ { 0 } ( x ) = \operatorname* { m i n } _ { u } \{ V ( x , u ) \mid u \in \mathcal { U } ( x ) \}$ .

For each $i \in { \mathcal { I } }$ , we define an “artificial” problem $\mathbb { P } _ { i } ( x )$ as follows

$$
\begin{array}{l} V _ {i} ^ {0} (x) := \min _ {u} \left\{V _ {i} (x, u) \mid (x, u) \in \mathbb {Z} _ {i} \right\} \\ u _ {i} ^ {0} (x) := \arg \min _ {u} \left\{V _ {i} (x, u) \mid (x, u) \in \mathbb {Z} _ {i} \right\} \\ \end{array}
$$

The cost $V _ { i } ( x , u )$ in the above equations may be replaced by $V ( x , u )$ since $V ( x , u ) = V _ { i } ( x , u )$ in $\mathbb { Z } _ { i }$ . The problem is artificial because it includes constraints (the boundaries of $\mathbb { Z } _ { i } )$ that are not necessarily constraints of the original problem. We introduce this problem because it helps us to understand the solution of the original problem. For each $i \in \mathbb { I } _ { 1 : p }$ , let the set $\mathcal { U } _ { i } ( x )$ be defined as follows

$$\mathcal {U} _ {i} (x) := \{u \mid (x, u) \in \mathbb {Z} _ {i} \}$$
