(d) globally attractive if $| \phi ( i ; x ) | _ { \mathcal { A } } \to 0 { \mathrm { ~ a s ~ } } i \to \infty$ for all $\boldsymbol { x } \in \mathbb { R } ^ { n }$ .   
(e) locally asymptotically stable if it is locally stable and locally attractive.   
(f) globally asymptotically stable if it is locally stable and globally attractive.   
(g) locally exponentially stable if there exist $\eta > 0 , c > 0$ , and $ { \boldsymbol { \gamma } } \in ( 0 , 1 )$ such that $| x | _ { \mathcal { A } } < \eta$ implies $\vert \phi ( i ; x ) \vert _ { \mathcal { A } } \leq c \vert x \vert _ { \mathcal { A } } \gamma ^ { i }$ for all $i \in \mathbb { I } _ { \geq 0 }$ .   
(h) globally exponentially stable if there exists a $c > 0$ and a $ { \boldsymbol { \gamma } } \in ( 0 , 1 )$ such that $\vert \phi ( i ; x ) \vert _ { \mathcal { A } } \leq c \vert x \vert _ { \mathcal { A } } \gamma ^ { i }$ for all $x \in \mathbb { R } ^ { n }$ , all $i \in \mathbb { I } _ { \geq 0 }$ .

It is often convenient to characterize global asymptotic stability in terms of a comparison function $\beta ( \cdot )$ .

Proposition B.8 (GAS and comparison function). Suppose A is compact (and positive invariant) and that $f ( \cdot )$ is continuous. Then A is GAS for $x ^ { + } = f ( x )$ if and only if there exists a KL function $\beta ( \cdot )$ such that, for each $\boldsymbol { x } \in \mathbb { R } ^ { n }$

$$\left| \phi (i; x) \right| _ {\mathcal {A}} \leq \beta \left(\left| x \right| _ {\mathcal {A}}, i\right) \quad \forall i \in \mathbb {I} _ {\geq 0} \tag {B.1}$$

That A is GAS for $x ^ { + } = f ( x )$ if there exists a KL function $\beta ( \cdot )$ satisfying (B.1) follows directly from the definition of a class $\mathcal { K L }$ function. The converse is harder to prove but is stated in Jiang and Wang (2002) where Proposition 2.2 establishes the equivalence of the existence of a $\mathcal { K L }$ function satisfying (2) with UGAS (uniform global asymptotic stability), and Corollary 3.3 which establishes the equivalence, when A is compact, of UGAS and GAS.

In practice, global asymptotic stability of A cannot always be achieved because of state constraints. Hence we have to extend slightly the definitions given above.

Definition B.9 (Various forms of stability (constrained)). Suppose $X \subset$ $\mathbb { R } ^ { n }$ is positive invariant for $x ^ { + } = f ( x )$ , that A is closed and positive invariant for $x ^ { + } = f ( x )$ , and that A lies in the interior of X. Then A is
