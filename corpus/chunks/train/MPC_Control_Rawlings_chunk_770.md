Proof. This Proposition appears as Proposition C.9 in Appendix C where a proof is given. 

In our case $\mathcal { U } ( x ) , x \in \mathcal { X }$ , is polyhedral and is defined by

$$\mathcal {U} (x) := \{\nu \in \mathbb {R} ^ {m} \mid M \nu \leq N x + p \} \tag {7.2}$$

so $\nu \in \mathcal { U } ( x )$ if and only if, for all $u \in { \mathcal { U } } ( x ) , \nu - u \in { \mathcal { U } } ( x ) - \{ u \} : =$ $\{ \nu - u \mid \nu \in \mathcal { U } ( x ) \}$ . With $h : = \nu - u$

$$
\mathcal {U} (x) - \{u \} = \left\{h \in \mathbb {R} ^ {m} \left| \begin{array}{l l} M _ {i} h \leq 0, & i \in I (x, u) \\ M _ {j} h <   N _ {j} x + p _ {j} - M _ {j} u, & j \in \mathbb {I} _ {1: r} \setminus I (x, u) \end{array} \right. \right\}
$$

since $M _ { i } u = N _ { i } x + p _ { i }$ for all $i \in I ( x , u )$ . For each $z = ( x , u ) \in \mathbb { Z }$ , let $C ( x , u )$ denote the cone of first-order feasible variations of $u ; C ( x , u )$ is defined by

$$C (x, u) := \{h \in \mathbb {R} ^ {m} \mid M _ {i} h \leq 0, i \in I (x, u) \}$$

Clearly

$$\mathcal {U} (x) - \{u \} = C (x, u) \cap \{h \in \mathbb {R} ^ {m} \mid M _ {i} h < N _ {i} x + p _ {i} - M _ {i} u, i \in \mathbb {I} _ {1: r} \backslash I (x, u) \}$$

so that ${ \mathcal { U } } ( x ) - \{ u \} \subseteq C ( x , u )$ ; for any $( x , u ) \in \mathbb { Z } ,$ , any $h \in C ( x , u )$ , there exists an $\alpha > 0$ such that $u + \alpha h \in { \mathcal { U } } ( x )$ . Proposition 7.6 may be expressed as: u is optimal for $\mathrm { m i n } _ { u } \{ V ( x , u ) \mid u \in \mathcal { U } ( x ) \}$ if and only if

$$u \in \mathcal {U} (x) \text { and } \langle \nabla_ {u} V (x, u), h \rangle \geq 0 \quad \forall h \in \mathcal {U} (x) - \{u \}$$

We may now state a modified form of Proposition 7.6:

Proposition 7.7 (Optimality conditions in terms of polar cone). Suppose for each $x \in { \mathcal { X } } , u \mapsto V ( x , \cdot )$ is convex and differentiable, and $\mathcal { U } ( x )$ is defined by (7.2). Then u is optimal for $\operatorname* { m i n } _ { u } \{ V ( x , u ) \mid u \in \mathcal { U } ( x ) \}$ if and only if

$$u \in \mathcal {U} (x) \text { and } \langle \nabla_ {u} V (x, u), h \rangle \geq 0 \quad \forall h \in C (x, u)$$
