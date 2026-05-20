(i) $( C , A )$ is detectable.   
(ii) The matrix $\left[ \begin{array} { l } { A - \lambda I } \\ { C } \end{array} \right]$ has full-column rank for all Reλ ≥ 0.   
(iii) For all λ and x such that Ax = λx and $\mathrm { R e } \lambda \geq 0 ,$ , Cx 6= 0.   
(iv) There exists a matrix L such that $A + L C$ is Hurwitz.   
(v) $( A ^ { * } , C ^ { * } )$ is stabilizable.

The conditions (iv) and (v) of Theorems 3.1 and 3.3 and the conditions (ii) and (iii) of Theorems 3.2 and 3.4 are often called Popov-Belevitch-Hautus (PBH) tests. In particular, the following definitions of modal controllability and observability are often useful.

Definition 3.6 Let λ be an eigenvalue of A or, equivalently, a mode of the system. Then the mode λ is said to be controllable (observable) if $x ^ { * } B \neq 0 \ ( C x \neq 0 )$ for all left (right) eigenvectors of A associated with λ; that is, $x ^ { * } A = \lambda x ^ { * } \ ( A x = \lambda x )$ and $0 \neq x \in \mathbb { C } ^ { n }$ . Otherwise, the mode is said to be uncontrollable (unobservable).

It follows that a system is controllable (observable) if and only if every mode is controllable (observable). Similarly, a system is stabilizable (detectable) if and only if every unstable mode is controllable (observable).
