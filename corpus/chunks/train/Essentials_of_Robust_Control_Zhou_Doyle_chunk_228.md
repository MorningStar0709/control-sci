Problem 8.8 Consider the unity feedback system with $K ( s ) = 3 , G ( s ) = { \frac { 1 } { s - 2 } }$ Compute by hand $( { \mathrm { i . e . } }$ , without Matlab) a normalized coprime factorization of $G ( s )$ . Considering perturbations $\Delta _ { N }$ and $\Delta _ { M }$ of the factors of $G ( s )$ , compute by hand the stability radius , that is, the least upper bound on $\Vert \big [ \Delta _ { N } \big . \dot { \Delta _ { M } } \big ] \big \Vert _ { \infty }$ such that feedback stability is preserved.

Problem 8.9 Let a unit feedback system with a controller $K ( s ) = { \frac { 1 } { s } }$ and a nominal s plant model $P _ { o } ( s ) = \frac { s + 1 } { s ^ { 2 } + 0 . 2 s + 5 }$ . Construct a smallest destabilizing $\Delta \in \mathcal { R } \mathcal { H } _ { \infty }$ in the sense of $\| \Delta \| _ { \infty }$ for each of the following cases:

(a) $P = P _ { o } + \Delta ;$   
(b) $P = P _ { o } ( 1 + W \Delta )$ with $W ( s ) = { \frac { 0 . 2 ( s + 1 0 ) } { s + 5 0 } } ;$

$$
\mathrm{(c)} P = \frac {N + \Delta_ {n}}{M + \Delta_ {m}}, N = \frac {s + 1}{(s + 2) ^ {2}}, M = \frac {s ^ {2} + 0 . 2 s + 5}{(s + 2) ^ {2}}, \mathrm{and} \Delta = \left[ \begin{array}{l l} \Delta_ {n} & \Delta_ {m} \end{array} \right].
$$

Problem 8.10 This problem concerns the unity feedback system with controller $K ( s )$ and plant

$$
G (s) = \frac {1}{s + 1} \left[ \begin{array}{c c} 1 & 2 \\ 3 & 4 \end{array} \right].
$$

1. Take $K ( s ) = k I _ { 2 }$ (k a real scalar) and find the range of k for internal stability.

2. Take

$$
K (s) = \left[ \begin{array}{c c} k _ {1} & 0 \\ 0 & k _ {2} \end{array} \right]
$$

$( k _ { 1 } , k _ { 2 }$ real scalars) and find the region of $( k _ { 1 } , k _ { 2 } )$ in $\mathbb { R } ^ { 2 }$ for internal stability.

Problem 8.11 (Kharitonov’s Theorem) Let $a ( s )$ be an interval polynomial

$$a (s) = [ a _ {0} ^ {-}, a _ {0} ^ {+} ] + [ a _ {1} ^ {-}, a _ {1} ^ {+} ] s + [ a _ {2} ^ {-}, a _ {2} ^ {+} ] s ^ {2} + \dots .$$

Kharitonov’s theorem shows that $a ( s )$ is stable if and only if the following four Kharitonov polynomials are stable:

$$K _ {1} (s) = a _ {0} ^ {-} + a _ {1} ^ {-} s + a _ {2} ^ {+} s ^ {2} + a _ {3} ^ {+} s ^ {3} + a _ {4} ^ {-} s ^ {4} + a _ {5} ^ {-} s ^ {5} + a _ {6} ^ {+} s ^ {6} + \dotsK _ {2} (s) = a _ {0} ^ {-} + a _ {1} ^ {+} s + a _ {2} ^ {+} s ^ {2} + a _ {3} ^ {-} s ^ {3} + a _ {4} ^ {-} s ^ {4} + a _ {5} ^ {+} s ^ {5} + a _ {6} ^ {+} s ^ {6} + \dotsK _ {3} (s) = a _ {0} ^ {+} + a _ {1} ^ {+} s + a _ {2} ^ {-} s ^ {2} + a _ {3} ^ {-} s ^ {3} + a _ {4} ^ {+} s ^ {4} + a _ {5} ^ {+} s ^ {5} + a _ {6} ^ {-} s ^ {6} + \dotsK _ {4} (s) = a _ {0} ^ {+} + a _ {1} ^ {-} s + a _ {2} ^ {-} s ^ {2} + a _ {3} ^ {+} s ^ {3} + a _ {4} ^ {+} s ^ {4} + a _ {5} ^ {-} s ^ {5} + a _ {6} ^ {-} s ^ {6} + \dots$$
