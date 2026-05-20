for all $( x , t ) , ( y , t )$ in U. Then, for any $( x _ { 0 } , t _ { 0 } )$ in U there exists a unique solution φ $\mathbf { \sigma } _ { \mathbf { \lambda } ^ { } } ( \cdot ; x _ { 0 } , t _ { 0 } )$ passing through $( x _ { 0 } , t _ { 0 } )$ . The function $( t , x _ { 0 } , t _ { 0 } ) \mapsto$ $\phi ( t ; x _ { 0 } , t _ { 0 } ) : \mathbb { R } \times \mathbb { R } ^ { n } \times \mathbb { R } \to \mathbb { R } ^ { n }$ is continuous in its domain E which is open.

Note that D is often $\mathbb { R } ^ { n } \times \mathbb { R }$ , in which case Theorem A.32 states that a solution $x ( \cdot )$ of $\left( \mathrm { { A . 1 4 } } \right)$ escapes, i.e., $| x ( t ) |  \infty$ as $t \setminus t _ { a }$ or $t \nearrow \ t _ { b }$ if $t _ { a }$ and $t _ { b }$ are finite; $t _ { a }$ and $t _ { b }$ are the escape times. An example of a differential equation with finite escape time is $\dot { x } = x ^ { 2 }$ which has, if $x _ { 0 } > 0 , t _ { 0 } = 0$ , a solution $x ( t ) = x _ { 0 } [ 1 - ( t - t _ { 0 } ) x _ { 0 } ] ^ { - 1 }$ and the maximal interval of existence is $( t _ { a } , t _ { b } ) = ( - \infty , t _ { 0 } + 1 / x _ { 0 } )$ .

These results, apart from absence of a control u which is trivially corrected, do not go far enough. We require solutions on an interval $[ t _ { 0 } , t _ { f } ]$ given a priori. Further assumptions are needed for this. A useful tool in developing the required results is the Bellman-Gronwall Lemma:

Theorem A.34 (Bellman-Gronwall). Suppose that $c \in ( 0 , \infty )$ and that $\alpha : [ 0 , 1 ] \to { \mathbb R } .$ + is a bounded, integrable function, and that the integrable function $y : [ 0 , 1 ] \to \mathbb { R }$ satisfies the inequality

$$y (t) \leq c + \int_ {0} ^ {t} \alpha (s) y (s) d s \tag {A.15}$$

for all $t \in [ 0 , 1 ]$ . Then

$$y (t) \leq c e ^ {\int_ {0} ^ {t} \alpha (s) d s} \tag {A.16}$$

for all $t \in [ 0 , 1 ]$ .

Note that, if the inequality in (A.15) were replaced by an equality, (A.15) could be integrated to yield (A.16).

Proof. Let the function $Y : [ 0 , 1 ] \to \mathbb { R }$ be defined by

$$Y (t) = \int_ {0} ^ {t} \alpha (s) y (s) d s \tag {A.17}$$

so that ${ \dot { Y } } ( t ) = \alpha ( t ) y ( t )$ almost everywhere on [0, 1]. It follows from (A.15) and (A.17) that:

$$y (t) \leq c + Y (t) \forall t \in [ 0, 1 ]$$

Hence

$$
\begin{array}{l} (d / d t) \left[ e ^ {- \int_ {0} ^ {t} \alpha (s) d s} Y (t) \right] = e ^ {- \int_ {0} ^ {t} \alpha (s) d s} (\dot {Y} (t) - \alpha (t) Y (t)) \\ = \left(e ^ {- \int_ {0} ^ {t} \alpha (s) d s}\right) \alpha (t) (\mathcal {Y} (t) - Y (t)) \\ \leq c \left(e ^ {- \int_ {0} ^ {t} \alpha (s) d s}\right) \alpha (t) \tag {A.18} \\ \end{array}
$$

almost everywhere on [0, 1]. Integrating both sides of (A.18) from 0 to t yields
