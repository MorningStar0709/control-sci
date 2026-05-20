# 2.4 Stability

bounded and, hence, so is the set $x _ { 1 }$ . Suppose, for some $j > 0$ , the set $\mathcal { Z } _ { j - 1 }$ is bounded; then its projection onto the set $\boldsymbol { \mathcal { X } } _ { j - 1 }$ is bounded and so is the set $\mathcal { Z } _ { j } = f _ { \mathbb { Z } } ^ { - 1 } ( \mathcal { X } _ { j } )$ . Thus the set $\chi _ { j }$ is bounded. By induction $\chi _ { j }$ is bounded for all $j \in \mathbb { I } _ { \geq 0 }$ .

When $f ( \cdot )$ is linear, i.e., $f ( x , u ) = A x + B u$ , then $f _ { \mathbb { Z } } ^ { - 1 } ( \cdot )$ is bounded on bounded sets if A is nonsingular. The matrix A is always nonsingular when A and B are obtained by sampling a continuous time system ${ \dot { x } } =$ $A _ { c } x + B _ { c } \ i$ u with u constant between sampling instants. In this case $A =$ $\exp ( A _ { c } \Delta )$ and $\begin{array} { r } { B = \int _ { 0 } ^ { \Delta } \exp ( A _ { c } ( \Delta - s ) ) B d s } \end{array}$ so that $A$ is invertible. To show that $f _ { \mathbb { Z } } ^ { - 1 } ( \cdot )$ is bounded on bounded sets, let X be an arbitrary bounded set in $\mathbb { R } ^ { n }$ and let $x ^ { \prime }$ be an arbitrary point $x ^ { \prime } \in X$ . Then $f ^ { - 1 } ( x ^ { \prime } ) ~ =$ $\{ ( x , u ) \ | \ A x + B u = x ^ { \prime } \}$ . Any $( x , u )$ in $f ^ { - 1 } ( x ^ { \prime } )$ satisfies $x = A ^ { - 1 } x ^ { \prime } -$ $A ^ { - 1 } B u$ so that x lies in the bounded set $A ^ { - 1 } X \oplus ( - A ^ { - 1 } B \mathbb { U } )$ and u lies in the bounded set U. Hence both $f ^ { - 1 } ( X )$ and $f _ { \mathbb { Z } } ^ { - 1 } ( X )$ lie in the bounded set $A ^ { - 1 } X \oplus ( - A ^ { - 1 } B )$ . A similar result holds for nonlinear systems. If $f ( \cdot )$ is obtained by sampling a continuous time system $\dot { x } = f _ { c } ( x , u )$ with period $\Delta$ and u constant between sampling instants, then $f ( \cdot )$ is defined by

$$f (x, u) = x + \int_ {0} ^ {\Delta} f _ {c} (x (s), u) d s$$

where $x ( s )$ is the solution of $\dot { x } = f _ { c } ( x , u )$ at time s if x is the state at time zero and u is the constant input in the interval $[ 0 , \Delta ]$ .

Proposition 2.21 (Properties of discrete time system). Suppose that

(a) $f _ { c } ( \cdot )$ is continuous.

(b) There exists a positive constant c such that

$$\left| f _ {c} \left(x ^ {\prime}, u\right) - f _ {c} (x, u) \right| \leq c \left| x ^ {\prime} - x \right| \quad \forall x, x ^ {\prime} \in \mathbb {R} ^ {n}, u \in \mathbb {U}$$

Then $f ( \cdot )$ and $f _ { \mathbb { Z } } ^ { - 1 } ( \cdot )$ are bounded on bounded sets.
