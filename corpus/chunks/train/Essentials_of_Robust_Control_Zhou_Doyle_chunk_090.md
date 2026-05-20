# 3.8 Problems

Problem 3.1 Let $A \in \mathbb { C } ^ { n \times n }$ and $B \in \mathbb { C } ^ { m \times m }$ . Show that $X ( t ) = e ^ { A t } X ( 0 ) e ^ { B t }$ is the solution to

$$\dot {X} = A X + X B.$$

Problem 3.2 Given the impulse response, $h _ { 1 } ( t )$ , of a linear time-invariant system with model

$$\ddot {y} + a _ {1} \dot {y} + a _ {2} y = u$$

find the impulse response, $h ( t )$ , of the system

$$\ddot {y} + a _ {1} \dot {y} + a _ {2} y = b _ {0} \ddot {u} + b _ {1} \dot {u} + b _ {2} u.$$

Justify your answer and generalize your result to nth order systems.

Problem 3.3 Suppose a second order system is given by ${ \dot { x } } = A x$ . Suppose it is known that $x ( 1 ) = \left\lceil \begin{array} { c } { { 4 } } \\ { { - 2 } } \end{array} \right\rceil$ for $x ( 0 ) = { \left[ \begin{array} { l } { 1 } \\ { 1 } \end{array} \right] }$ and $x ( 1 ) = \left[ { \begin{array} { c } { 5 } \\ { - 2 } \end{array} } \right]$ for $x ( 0 ) = { \left[ \begin{array} { l } { 1 } \\ { 2 } \end{array} \right] }$ Find $x ( n )$ for $x ( 0 ) = { \left[ \begin{array} { l } { { \bar { 1 } } } \\ { 0 } \end{array} \right] }$ Can you determine $A ?$

Problem 3.4 Assume $( A , B )$ is controllable. Show that $( F , G )$ with

$$
F = \left[ \begin{array}{l l} A & 0 \\ C & 0 \end{array} \right], G = \left[ \begin{array}{l} B \\ 0 \end{array} \right]
$$

is controllable if and only if

$$
\left[ \begin{array}{c c} A & B \\ C & 0 \end{array} \right]
$$

is a full-row rank matrix.

Problem 3.5 Let $\lambda _ { i } , i = 1 , 2 , . . . , n$ be n distinct eigenvalues of a matrix $A \in \mathbb { C } ^ { n \times n }$ and let $x _ { i }$ and $y _ { i }$ be the corresponding right- and left-unit eigenvectors such that $y _ { i } ^ { * } x _ { i } = 1$ . Show that

$$y _ {i} ^ {*} x _ {j} = \delta_ {i j}, \quad A = \sum_ {i = 1} ^ {n} \lambda_ {i} x _ {i} y _ {i} ^ {*}$$

and

$$C (s I - A) ^ {- 1} B = \sum_ {i = 1} ^ {n} \frac {(C x _ {i}) (y _ {i} ^ {*} B)}{s - \lambda_ {i}}.$$

Furthermore, show that the mode $\lambda _ { i }$ is controllable iff $y _ { i } ^ { * } B \neq 0$ and the mode $\lambda _ { i }$ is observable iff $C x _ { i } \neq 0$ .

Problem 3.6 Let $( A , b , c )$ be a realization with $A \in \mathbb { R } ^ { n \times n } , \ b \in \mathbb { R } ^ { n }$ , and $c ^ { * } \in \mathbb { R } ^ { n }$ . Assume that $\lambda _ { i } ( A ) + \lambda _ { j } ( A ) \neq 0$ for all i, j. This assumption ensures the existence of $X \in \mathbb { R } ^ { n \times n }$ such that

$$A X + X A + b c = 0$$

Show that X is nonsingular if and only if (A, b) is controllable and $( c , A )$ is observable.

Problem 3.7 Compute the system zeros and the corresponding zero directions of the following transfer functions
