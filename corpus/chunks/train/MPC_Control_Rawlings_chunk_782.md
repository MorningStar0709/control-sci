Thus the set $\mathcal { U } _ { i } ( x )$ is the set of admissible u at x, and problem $\mathbb { P } _ { i } ( x )$ may be expressed as $V _ { i } ^ { 0 } ( x ) : = \operatorname* { m i n } _ { u } \{ V _ { i } ( x , u ) ~ \vert ~ u \in \mathcal { U } _ { i } ( x ) \}$ ; the set $\mathcal { U } _ { i } ( x )$ is polytopic. For each i, problem $\mathbb { P } _ { i } ( x )$ may be recognized as a standard parametric quadratic program discussed in Section 7.4. Because of the piecewise nature of $V ( \cdot )$ , we require another definition.

Definition 7.15 (Active polytope (polyhedron)). A polytope (polyhedron) $\mathbb { Z } _ { i }$ in a polytopic (polyhedral) partition $\mathcal { P } ~ = ~ \{ \mathbb { Z } _ { i } ~ | ~ i \in \mathcal { I } \}$ of a polytope (polyhedron) $\mathbb { Z }$ is said to be active at $z \in \mathbb { Z } { \mathrm { ~ i f ~ } } z = ( x , u ) \in \mathbb { Z } _ { i }$ . The index set specifying the polytopes active at $z \in \mathbb { Z }$ is

$$S (z) := \{i \in \mathcal {I} | z \in \mathbb {Z} _ {i} \}$$

A polytope $\mathbb { Z } _ { i }$ in a polytopic partition ${ \mathcal { P } } = \{ \mathbb { Z } _ { i } \mid i \in { \mathcal { I } } \}$ of a polytope Z is said to be active for problem $\mathbb { P } ( x ) )$ if $( x , u ^ { 0 } ( x ) ) \in \mathbb { Z } _ { i }$ . The index set specifying polytopes active at $( x , u ^ { 0 } ( x ) )$ is $S ^ { 0 } ( x )$ defined by

$$S ^ {0} (x) := S (x, u ^ {0} (x)) = \{i \in \mathcal {I} | (x, u ^ {0} (x)) \in \mathbb {Z} _ {i} \}$$

Because we know how to solve the “artificial” problems $\mathbb { P } _ { i } ( x ) , i \in \mathcal { I }$ that are parametric quadratic programs, it is natural to ask if we can recover the solution of the original problem $\mathbb { P } ( x )$ from the solutions to these simpler problems. This question is answered by the following proposition.

Proposition 7.16 (Solving P using $\mathbb { P } _ { i } )$ . For any $x \in { \mathcal { X } }$ , u is optimal for $\mathbb { P } ( x )$ if and only if u is optimal for $\mathbb { P } _ { i } ( x )$ for all $i \in S ( x , u )$ .
