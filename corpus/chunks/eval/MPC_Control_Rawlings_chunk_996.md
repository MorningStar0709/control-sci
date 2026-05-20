# C.2.6 Constraint Set Defined by Inequalities

We now consider the case when the set U is specified by a set of differentiable inequalities:

$$U := \{u \mid g _ {i} (u) \leq 0 \forall i \in \mathcal {I} \} \tag {C.22}$$

where, for each $i \in \mathcal I$ , the function $g _ { i } : \mathbb { R } ^ { m }  \mathbb { R }$ is differentiable. For each $u \in U$

$$\mathcal {I} ^ {0} (u) := \{i \in \mathcal {I} \mid g _ {i} (u) = 0 \}$$

is the index set of active constraints. For each $u \in U$ , the set $\mathcal { F } _ { U } ( u )$ of feasible variations for the linearized set of inequalities; $\mathcal { F } _ { U } ( u )$ is defined by

$$\mathcal {F} _ {U} (u) := \{h \mid \langle \nabla g _ {i} (u), h \rangle \leq 0 \forall i \in \mathcal {I} ^ {0} (u) \} \tag {C.23}$$

The set $\mathcal { F } _ { U } ( u )$ is a closed, convex cone and is called a cone of first order feasible variations in Bertsekas (1999) because h is a descent direction for $g _ { i } ( u )$ for all $i \in \mathcal { I } ^ { 0 } ( u ) , \mathrm { i . e . } , g _ { i } ( u + \lambda h ) \le 0$ for all λ sufficiently small. When U is polyhedral, the case discussed in C.2.3, $g _ { i } ( u ) \ = \ \langle a _ { i } , u \rangle \ -$ $b _ { i }$ and $\nabla g _ { i } ( u ) \ = \ a _ { i }$ so that ${ \mathcal { F } } _ { U } ( u ) ~ = ~ \{ h ~ \ | ~ \ \langle a _ { i } , h \rangle ~ \leq ~ 0 ~ \forall i \in \ \mathcal { I } ^ { 0 } ( u ) \}$ which was shown in Proposition C.11 to be the tangent cone $\mathcal { T } _ { U } ( u )$ . An important question whether $\mathcal { F } _ { U } ( u )$ is the tangent cone $\mathcal { T } _ { U } ( u )$ for a wider class of problems because, if ${ \mathcal { F } } _ { U } ( u ) = { \mathcal { T } } _ { U } ( u )$ , a condition of optimality of the form in (C.20) may be obtained. In the example in Figure $\operatorname { C } . 8 , \mathcal { F } _ { U } ( u )$ is the horizontal axis $\{ h \in \mathbb { R } ^ { 2 } \mid h _ { 2 } = 0 \}$ whereas $\mathcal { T } _ { U } ( u )$ is the half-line $\{ h \in \mathbb { R } ^ { 2 } \mid h _ { 1 } \geq 0 , h _ { 2 } = 0 \}$ so that in this case, $\mathcal { F } _ { U } ( u ) \neq \mathcal { T } _ { U } ( u )$ . While $\mathcal { F } _ { U } ( u )$ is always convex, being the intersection of a set of half-spaces, the tangent cone $\mathcal { T } _ { U } ( u )$ is not necessarily convex as Figure C.6b shows. The set U is said to be quasiregular at $u \in U$ if ${ \mathcal { F } } _ { U } ( u ) = { \mathcal { T } } _ { U } ( u )$ is which case u is said to be a quasiregular point Bertsekas (1999). The next result, due to Bertsekas (1999), shows that $\mathcal { F } _ { U } ( u ) = \mathcal { T } _ { U } ( u )$ , i.e., U is quasiregular at u, when a certain constraint qualification is satisfied.
