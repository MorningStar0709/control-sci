# 3.2 Controllability and Observability

We now turn to some very important concepts in linear system theory.

Definition 3.1 The dynamical system described by equation (3.1) or the pair $( A , B )$ is said to be controllable if, for any initial state $x ( 0 ) = x _ { 0 } , t _ { 1 } > 0$ and final state x1, there exists a (piecewise continuous) input $u ( \cdot )$ such that the solution of equation (3.1) satisfies $x ( t _ { 1 } ) = x _ { 1 }$ . Otherwise, the system or the pair (A, B) is said to be uncontrollable.

The controllability (and the observability introduced next) of a system can be verified through some algebraic or geometric criteria.

Theorem 3.1 The following are equivalent:

(i) (A, B) is controllable.   
(ii) The matrix

$$W _ {c} (t) := \int_ {0} ^ {t} e ^ {A \tau} B B ^ {*} e ^ {A ^ {*} \tau} d \tau$$

is positive definite for any $t > 0$ .

(iii) The controllability matrix

$$
\mathcal {C} = \left[ \begin{array}{l l l l l} B & A B & A ^ {2} B & \ldots & A ^ {n - 1} B \end{array} \right]
$$

has full-row rank $o r ,$ in other words, $\begin{array} { r } {  A | \mathrm { I m } B  : = \sum _ { i = 1 } ^ { n } \mathrm { I m } ( A ^ { i - 1 } B ) = \mathbb { R } ^ { n } } \end{array}$

(iv) The matrix $[ A - \lambda I , B ]$ has full-row rank for all λ in C.   
(v) Let λ and x be any eigenvalue and any corresponding left eigenvector of $A \ ( i . e .$ , $x ^ { * } A = x ^ { * } \lambda ) ,$ then $x ^ { * } B \neq 0$ .   
(vi) The eigenvalues of $A + B F$ can be freely assigned (with the restriction that complex eigenvalues are in conjugate pairs) by a suitable choice of F .

$A = { \left\lceil \begin{array} { l l } { 2 } & { 0 } \\ { 0 } & { 2 } \end{array} \right\rceil }$ $B = { \left\lceil \begin{array} { l } { 1 } \\ { 1 } \end{array} \right\rceil }$ $x _ { 1 } = { \left\lceil \begin{array} { l } { 1 } \\ { 0 } \end{array} \right\rceil }$ $x _ { 2 } = { \left\lceil \begin{array} { l } { 0 } \\ { 1 } \end{array} \right\rceil }$

are independent eigenvectors of A and $x _ { i } ^ { * } B \neq 0 , \bar { i } = 1 , 2$ . However, this should not lead one to conclude that $( A , B )$ is controllable. In fact, $x = x _ { 1 } - x _ { 2 }$ is also an eigenvector of A and $x ^ { * } B = 0$ , which implies that $( A , B )$ is not controllable. Hence one must check for all possible eigenvectors in using criterion (v).

Definition 3.2 An unforced dynamical system ${ \dot { x } } = A x$ is said to be stable if all the eigenvalues of A are in the open left half plane; that is, $\mathrm { R e } \lambda ( { \cal A } ) < 0$ . A matrix A with such a property is said to be stable or Hurwitz.
