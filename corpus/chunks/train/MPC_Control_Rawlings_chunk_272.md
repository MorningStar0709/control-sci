The next task is to show the existence of a $\beta \geq 1$ such that $x ^ { \beta } ( N ; x ) =$ $\phi ( N ; x , { \mathbf { u } } ^ { \beta } ) \ \in \ \mathbb { X } _ { f }$ for all x in some compact set, also to be determined. To proceed, let the terminal equality constrained optimal problem $\mathbb { P } _ { N } ^ { c } ( x )$ be defined by

$$V _ {N} ^ {c} (x) = \min _ {\mathbf {u}} \{J _ {N} (x, \mathbf {u}) \mid \mathbf {u} \in \mathcal {U} _ {N} ^ {c} (x) \}$$

in which $J _ { N } ( \cdot )$ and $\mathcal { U } _ { N } ^ { c } ( \cdot )$ are defined by

$$
\begin{array}{l} J _ {N} (x, \mathbf {u}) := \sum_ {i = 0} ^ {N - 1} \ell (x (i), u (i)) \\ \mathcal {U} _ {N} ^ {c} (x) := \hat {\mathcal {U}} _ {N} (x) \cap \{\mathbf {u} \mid \phi (N; x, \mathbf {u}) = 0 \} \\ \end{array}
$$

In the definition of $J _ { N } ( \cdot ) , x ( i ) : = \phi ( i ; x , \mathbf { u } )$ . Let $\mathbf { u } ^ { c }$ denote the solution of $\mathbb { P } _ { N } ^ { c } ( x )$ and let $\mathcal { X } _ { N } ^ { c } : = \{ x \in \mathbb { X } \mid \mathcal { U } _ { N } ^ { c } ( x ) \neq \emptyset \}$ denote the domain of $V _ { N } ^ { c } ( \cdot )$ . We assume that $\mathcal { X } _ { N } ^ { c }$ is compact and contains the origin in its interior. Clearly $\mathcal { U } _ { N } ^ { c } ( x ) \subseteq \hat { \mathcal { U } } _ { N } ( x )$ and $\mathcal { X } _ { N } ^ { c } \subseteq \mathcal { X } _ { N }$ . We also assume that there exists a $\mathcal { K } _ { \infty }$ function $\alpha ^ { c } ( \cdot )$ such that

$$V _ {N} ^ {c} (x) \leq \alpha^ {c} (| x |)$$

for all $x \in \mathcal { X } _ { N } ^ { c }$ ; this is essentially a controllability assumption. The value function for the modified problem $\mathbb { P } _ { N } ^ { \beta } ( x )$ satisfies

$$
\begin{array}{l} \hat {V} _ {N} ^ {\beta} (x) = J _ {N} (x, \mathbf {u} _ {N} ^ {\beta} (x)) + \beta V _ {f} (x _ {N} ^ {\beta} (N; x)) \\ \leq J _ {N} (x, \mathbf {u} _ {N} ^ {c} (x)) = V _ {N} ^ {c} (x) \leq \alpha^ {c} (| x |) \\ \end{array}
$$

for all $x \in \mathcal { X } _ { N } ^ { c }$ where the first inequality follows from the fact that $\beta V _ { f } ( x _ { N } ^ { c } ( N ; x ) ) = 0$ and $\mathbf { u } _ { N } ^ { c }$ is not optimal for $\mathbb { P } _ { N } ^ { \beta } ( x )$ ; here $x _ { N } ^ { c } ( N ; x ) : =$ $\phi ( N ; x , { \mathbf { u } } ^ { c } ( x ) )$ . Hence

$$\beta V _ {f} (x _ {N} ^ {\beta} (N; x)) \leq \alpha^ {c} (| x |)$$
