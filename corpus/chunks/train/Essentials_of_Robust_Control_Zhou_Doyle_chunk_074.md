Definition 3.3 The dynamical system of equation (3.1), or the pair $( A , B )$ , is said to be stabilizable if there exists a state feedback $u = F x$ such that the system is stable $( \mathrm { i . e . , } A + B F$ is stable).

It is more appropriate to call this stabilizability the state feedback stabilizability to differentiate it from the output feedback stabilizability defined later.

The following theorem is a consequence of Theorem 3.1.

Theorem 3.2 The following are equivalent:

(i) $( A , B )$ is stabilizable.   
(ii) The matrix $[ A - \lambda I , B ]$ has full-row rank for all $\mathrm { R e } \lambda \geq 0$ .   
(iii) For all λ and x such that $x ^ { * } A = x ^ { * } \lambda$ and Reλ $\geq 0 , x ^ { * } B \neq 0$ .   
(iv) There exists a matrix F such that $A + B F$ is Hurwitz.

We now consider the dual notions: observability and detectability of the system described by equations (3.1) and (3.2).

Definition 3.4 The dynamical system described by equations (3.1) and (3.2) or by the pair $( C , A )$ is said to be observable if, for any $t _ { 1 } > 0$ , the initial state $x ( 0 ) = x _ { 0 }$ can be determined from the time history of the input $u ( t )$ and the output $y ( t )$ in the interval of $[ 0 , t _ { 1 } ]$ . Otherwise, the system, or $( C , A )$ , is said to be unobservable.

Theorem 3.3 The following are equivalent:

(i) $( C , A )$ is observable.

(ii) The matrix

$$W _ {o} (t) := \int_ {0} ^ {t} e ^ {A ^ {*} \tau} C ^ {*} C e ^ {A \tau} d \tau$$

is positive definite for any $t > 0$ .

(iii) The observability matrix

$$
\mathcal {O} = \left[ \begin{array}{c} C \\ C A \\ C A ^ {2} \\ \vdots \\ C A ^ {n - 1} \end{array} \right]
$$

has full-column rank or $\textstyle \bigcap _ { i = 1 } ^ { n } \operatorname { K e r } ( C A ^ { i - 1 } ) = 0$

(iv) The matrix $\left[ \begin{array} { l } { A - \lambda I } \\ { C } \end{array} \right]$ has full-column rank for all λ in C.

(v) Let λ and y be any eigenvalue and any corresponding right eigenvector of A $( i . e . ,$ $A y = \lambda y ) ,$ ; then $C y \neq 0$ .

(vi) The eigenvalues of $A + L C$ can be freely assigned (with the restriction that complex eigenvalues are in conjugate pairs) by a suitable choice of L.

(vii) $( A ^ { * } , C ^ { * } )$ is controllable.

Definition 3.5 The system, or the pair (C, A), is detectable if $A + L C$ is stable for some L.

Theorem 3.4 The following are equivalent:
