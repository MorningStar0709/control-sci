If: (i) $\ell ( z , \nu ) = ( 1 / 2 ) | z | _ { O } ^ { 2 } + ( 1 / 2 ) | \nu | _ { R } ^ { 2 }$ in which Q and R are positive definite, (ii) the terminal cost $V _ { f } ( z ) = ( 1 / 2 ) | z | _ { P _ { f } } ^ { 2 }$ in which $P _ { f }$ is positive definite, (iii) Assumption 3.14 holds, and (iv) the terminal cost $V _ { f } ( \cdot )$ and terminal constraint set $\mathbb { Z } _ { f }$ satisfy the stability Assumptions 2.12 and 2.13, and $\left( \mathbf { v } \right) \mathbf { \mathcal { Z } } _ { N }$ is compact, then there exist constants $c _ { 1 }$ and $c _ { 2 }$ such that (3.33)–(3.35) become

$$\bar {V} _ {N} ^ {0} (z) \geq c _ {1} | z | ^ {2} \quad \forall z \in \mathcal {Z} _ {N} \tag {3.36}\Delta \bar {V} _ {N} ^ {0} (z) \leq - c _ {1} | z | ^ {2} \quad \forall z \in \mathcal {Z} _ {N} \tag {3.37}\bar {V} _ {N} ^ {0} (z) \leq c _ {2} | z | ^ {2} \quad \forall z \in \mathcal {Z} _ {N} \tag {3.38}$$

Hence the origin is exponentially stable for the nominal system $z ^ { + } =$ $A z + B \bar { \kappa } _ { N } ( z )$ with a region of attraction $\mathcal { Z } _ { N } , \mathrm { i . e . }$ ., there exists a $c > 0$ and a $\gamma \in \mathsf { \Gamma } ( 0 , 1 )$ such that $| z ( i ) | \ \leq \ c | z ( 0 ) | \gamma ^ { i }$ for all $i \in \mathbb { I } _ { \geq 0 }$ . Since $x ( i ) = z ( i ) + e ( i )$ where $e ( i ) \in S _ { K } ( \infty )$

$$\left| x (i) \right| _ {S _ {K} (\infty)} = d (z (i) + e (i), S _ {K} (\infty)) \leq d (z (i) + e (i), e (i)) = | z (i) |$$

Hence, for all $i \in \mathbb { I } _ { \geq 0 }$ ,

$$| x (i) | _ {S _ {K} (\infty)} \leq c | z (0) | \gamma^ {i}$$

Let $\mathcal { A } \subset \mathbb { R } ^ { n } \times \mathbb { R } ^ { n }$ be defined as follows

$$\mathcal {A} := S _ {K} (\infty) \times \{0 \}$$

so that, with $| ( x , z ) | : = | x | + | z | ,$ ,

$$| (x, z) | _ {\mathcal {A}} = | x | _ {S _ {K} (\infty)} + | z |$$

It follows from the previous discussion that the state $( x , z )$ of the composite system satisfies

$$\left| (x (i), z (i)) \right| _ {\mathcal {A}} = \left| x (i) \right| _ {S _ {K} (\infty)} + \left| z (i) \right| \leq 2 c | z (0) | y ^ {i} \leq 2 c y ^ {i} | (x (0), z (0)) | _ {\mathcal {A}}$$

for all $i \in \mathbb { I } _ { \geq 0 }$ since $| z ( 0 ) | \leq | x ( 0 ) | _ { S _ { K } ( \infty ) } + | z ( 0 ) | = | ( x ( 0 ) , z ( 0 ) ) | _ { \mathcal { A } }$ . We have proved:

Proposition 3.15 (Exponential stability of tube-based MPC). The set $\mathcal { A } : = S _ { K } ( \infty ) \times \{ 0 \}$ is exponentially stable with a region of attraction $( \mathcal { Z } _ { N } \oplus S _ { K } ( \infty ) ) \times \mathcal { Z } _ { N }$ for the composite system (3.29) and (3.30).

Proposition 3.15 remains true if $S _ { K } ( \infty )$ is replaced by S where $S \supset$ $S _ { K } ( \infty )$ is robust positive invariant for $e ^ { + } = A _ { K } e + w , w \in \mathbb { W }$ . The tubebased model predictive controller is formally described by the following algorithm in which i denotes current time.
