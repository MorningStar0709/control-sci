(a) There exists a compact set $\mathcal { O } \subseteq \mathbb { X }$ that contains the origin and is robust control invariant for $x ^ { + } = f ( x , u , w )$ so that for all $x \in \mathcal { O }$ there exists a $u \in \mathbb { U }$ such that $f ( x , u , w ) \in \mathcal { O }$ for all $w \in \mathbb { W }$ .

(b) $\rho = 0$

Assumption 3.11(a) implies the existence of a control law $\kappa _ { \mathcal { O } } : \mathcal { O } \to \mathbb { U }$ such that O is robust positive invariant for $x ^ { + } = f ( x , \kappa _ { \mathcal { O } } ( x ) , w ) , \mathrm { i . e . }$ , $f ( x , \kappa _ { \mathcal { O } } ( x ) , w ) \in \mathcal { O }$ and $\kappa _ { \mathcal { O } } ( x ) ~ \in ~ \mathbb { U }$ for all $x \in { \mathcal { O } }$ , all $w \in \mathbb { W }$ . We assume $\rho \ : = \ : 0$ for simplicity; the term $- \rho ^ { 2 } | \boldsymbol { w } | ^ { 2 }$ in $\ell ( \cdot )$ is needed in unconstrained problems to make maximization with respect to the disturbance sequence well defined and is not needed when the constraint $w \in \mathbb { W }$ is present. Accordingly, we replace $\ell ( x , u , w )$ by $\ell ( x , u )$ . Returning to the discussion in Section 3.3.2, we now assume that O has properties analogous to those of the origin in the deterministic case. Specifically we assume:

Assumption 3.12 (Properties of robust control invariant set).

(a) $\mathcal { O } \subseteq \mathbb { X } _ { f }$

(b) $V _ { f } ( x ) = 0$ for all $x \in \mathcal { O }$ .

(c) $\ell ( x , \kappa _ { \mathcal { O } } ( x ) ) = 0$ for all $x \in \mathcal { O }$ .

(d) $K _ { f } ( x ) = K _ { \mathcal { O } } ( x )$ for all $x \in \mathcal { O }$ .

(e) There exists a $\mathcal { K } _ { \infty }$ function $\alpha _ { 1 } ( \cdot )$ such that $\ell ( x , u ) \geq \alpha _ { 1 } ( | x | _ { \mathcal { O } } )$ for all $( x , u ) \in \mathbb { X } \times \mathbb { U }$ .

Since Theorem 3.10 remains true when $\rho ~ = ~ 0$ , it is possible to demonstrate, under Assumption 3.12, the assumptions of Section 3.3.2, and the assumption that $x _ { N }$ is bounded, the existence of ${ \mathcal K } _ { \infty }$ functions

$\alpha _ { 1 } ( \cdot )$ and $\alpha _ { 2 } ( \cdot )$ such that

$$
\begin{array}{l} V _ {N} ^ {0} (x) \geq \alpha_ {1} (| x | _ {\mathcal {O}}) \\ V _ {N} ^ {0} (x) \leq \alpha_ {2} (| x | _ {\mathcal {O}}) \\ \Delta V _ {N} ^ {0} (f (x, \kappa_ {N} (x), w)) \leq - \alpha_ {1} (| x | _ {\mathcal {O}}) \\ \end{array}
$$

for all $x \in \mathcal { X } _ { N } , w \ \in \ \mathbb { W }$ . These bounds differ from those in Proposition 2.19 of Chapter 2 in that |x| is replaced by $| x | _ { \mathcal { O } }$ and the term $( \rho ^ { 2 } / 2 )$ in the last bound is absent. It follows from these bounds that, as shown in Theorem B.23 of Appendix B, the invariant set O is asymptotically stable for $x ^ { + } = f ( x , \kappa _ { N } ( x ) , w ) , w \in \mathbb { W }$ with a region of attraction $x _ { N }$ .
