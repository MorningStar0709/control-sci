# 2.4 Stability

$V _ { N } ( x , i , { \mathbf { u } } )$ also depends on the initial time i and is defined by

$$V _ {N} (x, i, \mathbf {u}) := \sum_ {k = i} ^ {i + N - 1} \ell (x (k), u (k), k) + V _ {f} (x (i + N), i + N)$$

in which $x ( k ) : = \phi ( k ; x , i , \mathbf { u } ) , \mathbf { u } = \{ u ( i ) , u ( i + 1 ) , \ldots , u ( i + N - 1 ) \}$ , and the stage cost $\ell ( \cdot )$ and terminal cost $V _ { f } ( \cdot )$ are time varying. The state and control constraints are also time varying

$$x (k) \in \mathbb {X} (k) \quad u (k) \in \mathbb {U} (k)$$

for all k. In addition, there is a time-varying terminal constraint

$$x (i + N) \in \mathbb {X} _ {f} (i + N)$$

in which i is the current time. The time-varying optimal control problem at event $( x , i )$ is $\mathbb { P } _ { N } ( x , i )$ defined by

$$\mathbb {P} _ {N} (x, i): \quad V _ {N} ^ {0} (x, i) = \min \left\{V _ {N} (x, i, \mathbf {u}) \mid \mathbf {u} \in \mathcal {U} _ {N} (x, i) \right\}$$

in which $\mathcal { U } _ { N } ( x , i )$ is the set of control sequences $\textbf { u } = \{ u ( i ) , u ( i +$ $1 ) , \ldots , u ( i + N - 1 ) ]$ } satisfying the state, control and terminal constraints, i.e.,

$$\mathcal {U} _ {N} (x, i) := \{\mathbf {u} \mid (x, \mathbf {u}) \in \mathbb {Z} _ {N} (i) \}$$

in which, for each i, $\mathbb { Z } _ { N } ( i ) \subset \mathbb { R } ^ { n } \times \mathbb { R } ^ { N m }$ is defined by

$$
\begin{array}{l} \mathbb {Z} _ {N} (i) := \left\{(x, \mathbf {u}) \mid u (k) \in \mathbb {U} (k), \quad \phi (k; x, i, \mathbf {u}) \in \mathbb {X} (k), \forall k \in \mathbb {I} _ {i, i + N - 1}, \right. \\ \left. \phi (i + N; x, i, \mathbf {u}) \in \mathbb {X} _ {f} (i + N) \right\} \\ \end{array}
$$

For each time i, the domain of $V _ { N } ^ { 0 } ( \cdot , i )$ is $\mathcal { X } _ { N } ( i )$ where

$$
\begin{array}{l} \mathcal {X} _ {N} (i) := \{x \in \mathbb {X} (i) \mid \mathcal {U} _ {N} (x, i) \neq \emptyset \} \\ = \{x \in \mathbb {R} ^ {n} \mid \exists \mathbf {u} \text {   such   that   } (x, \mathbf {u}) \in \mathbb {Z} _ {N} (i) \} \\ \end{array}
$$

which is the projection of $\mathbb { Z } _ { N } ( i )$ onto $\mathbb { R } ^ { n }$ . Our standing assumptions (2.2 and 2.3) are replaced, in the time-varying case, by

Assumption 2.25 (Continuity of system and cost; time-varying case). The functions $f ( \cdot ) , \ell ( \cdot )$ , and $V _ { f } ( \cdot )$ are continuous; for all $i \in \mathbb { I } _ { \geq 0 }$ , $f ( 0 , 0 , i ) = 0 , \ell ( 0 , 0 , i ) = 0$ , and $V _ { f } ( 0 , i ) = 0$ .
