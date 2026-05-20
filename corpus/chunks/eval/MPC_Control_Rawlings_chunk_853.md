$$e ^ {- \int_ {0} ^ {t} \alpha (s) d s} Y (t) \leq c [ 1 - e ^ {- \int_ {0} ^ {t} \alpha (s) d s} ]$$

for all $t \in [ 0 , 1 ]$ . Hence

$$Y (t) \leq c [ e ^ {\int_ {0} ^ {t} \alpha (s) d s} - 1 ]$$

and

$$\mathcal {Y} (t) \leq c e ^ {\int_ {0} ^ {t} \alpha (s) d s}$$

for all $t \in [ 0 , 1 ]$ .

The interval [0, 1] may, of course, be replaced by $[ t _ { 0 } , t _ { f } ]$ for arbitrary $t _ { 0 } , t _ { f } \in ( - \infty , \infty )$ . Consider now the forced system described by

$$\dot {x} (t) = f (x (t), u (t), t) \text {a.e} \tag {A.19}$$

with initial condition

$$x (0) = 0$$

The period of interest is now $T : = [ 0 , 1 ]$ and $\mathbf { \ddot { a } . e . \vec { \mathbf { \mu } } \mu }$ denotes “almost everywhere on $T . ^ { \dag }$ Admissible controls u(·) are measurable and satisfy the control constraint

$$u (t) \in \Omega \text { a.e. }$$

where $\Omega \subset \mathbb { R } ^ { m }$ is compact. For convenience, we denote the set of admissible controls by

$$\mathcal {U} := \{u: T \to \mathbb {R} ^ {m} \mid u (\cdot) \text { is measurable, } u (t) \in \Omega \text { a.e. } \}$$

Clearly U is a subset of $L _ { \infty }$ . For simplicity we assume, in the sequel, that $f$ is continuous; this is not restrictive. For each u in U, x in ${ \mathbb { R } } ^ { n }$ , the function $t \mapsto f ^ { u } ( x , t ) : = f ( x , u ( t ) , t )$ is measurable so that $f ^ { u }$ satisfies the Caratheodory conditions and our previous results, Theorems A.31–A.33, apply. Our concern now is to show that, with additional assumptions, for each u in U, a solution to (A.12) or (A.13) exists on $T$ , rather than on some maximal interval that may be a subset of $T _ { \ast }$ , and that this solution is unique and bounded.

Theorem A.35 (Existence of solutions to forced systems). Suppose:

(a) f is continuous and

(b) there exists a positive constant c such that

$$\left| f \left(x ^ {\prime}, u, t\right) - f (x, u, t) \right| \leq c \left| x ^ {\prime} - x \right|$$

for all $( x , u , t ) \in \mathbb { R } ^ { n } \times \Omega \times T$ . Then, for each u in $u ,$ there exists a unique, absolutely continuous solution $x ^ { u } : T \to \mathbb { R } ^ { n }$ of (A.19) on the interval T passing through $( x _ { 0 } , 0 )$ . Moreover, there exists a constant K such that

$$| x ^ {u} (t) | \leq K$$

for all $t \in T$ , all $u \in \mathcal { U }$ .

Proof. A direct consequence of (b) is the existence of a constant which, without loss of generality, we take to be c, satisfying

(c) $| f ( x , u , t ) | \leq c ( 1 + | x | )$ for all $( x , u , t ) \in \mathbb { R } ^ { n } \times \Omega \times T$ .
