$$\left| (x, \mathbf {u}) \right| \leq | x | + | \mathbf {u} | \leq | x | + d ^ {\prime} | x | \leq \left(1 + d ^ {\prime}\right) | x |$$

which gives $| x | \geq c ^ { \prime } \left| ( x , \mathbf { u } ) \right|$ with $c ^ { \prime } = 1 / ( 1 + d ^ { \prime } ) > 0$ . Hence, there exists $a _ { 3 } = c ( c ^ { \prime } ) ^ { 2 }$ such that $V ( x ^ { + } , { \bf u } ^ { + } ) - V ( x , { \bf u } ) \le - a _ { 3 } \vert ( x , { \bf u } ) \vert ^ { 2 }$ for all $x \in \mathcal { X } _ { N }$ . Therefore the extended state (x, u) satisfies the standard conditions of an exponential stability Lyapunov function (see Theorem B.14 in Appendix B) with $a _ { 1 } = a , a _ { 2 } = b , a _ { 3 } = c ( c ^ { \prime } ) ^ { 2 } , \sigma = 2$ for $( x , \mathbf { u } ) \in$ $\mathcal { X } _ { N } \times \mathbb { U } ^ { N }$ (case (a)) or $\mathcal { X } _ { N } \times \bar { \mathbb { U } } \mathrm { ~ ( c a s e ~ ( b ) ) ~ }$ . Therefore for all $x ( 0 ) \in \mathcal { X } _ { N }$ , $k \geq 0 _ { : }$ ,

$$\left| (x (k), \mathbf {u} (k)) \right| \leq \alpha \left| (x (0), \mathbf {u} (0)) \right| \gamma^ {k}$$

in which $\alpha > 0$ and $0 < \gamma < 1$ .

Finally we remove the input sequence and establish that the origin for the state (rather than the extended state) is exponentially stable for the closed-loop system. We have for all $x ( 0 ) \in \mathcal { X } _ { N }$ and $k \geq 0$

$$
\begin{array}{l} | x (k) | \leq | (x (k), \mathbf {u} (k)) | \leq \alpha | (x (0), \mathbf {u} (0)) | \gamma^ {k} \\ \leq \alpha (| x (0) | + | \mathbf {u} (0) |) \gamma^ {k} \leq \alpha (1 + d ^ {\prime}) | x (0) | \gamma^ {k} \\ \leq \alpha^ {\prime} | x (0) | \gamma^ {k} \\ \end{array}
$$

in which $\alpha ^ { \prime } = \alpha ( 1 + d ^ { \prime } ) > 0$ , and we have established exponential stability of the origin on the feasible set $x _ { N }$ .

We also consider later in the chapter the effects of state estimation error on the closed-loop properties of distributed MPC. For analyzing stability under perturbations, the following lemma is useful. Here e plays the role of estimation error.

Lemma 6.5 (Exponential stability with mixed powers of norm). Consider a dynamic system

$$(x ^ {+}, e ^ {+}) = f (x, e)$$

with a zero steady-state solution, $f ( 0 , 0 ) = ( 0 , 0 )$ . Assume there exists a function $V : \mathbb { R } ^ { n + m }  \mathbb { R } _ { \ge 0 }$ that satisfies the following for all $( x , e ) \in$ $\mathbb { R } ^ { n } \times \mathbb { R } ^ { m }$

$$a (| x | ^ {\sigma} + | e | ^ {\gamma}) \leq V ((x, e)) \leq b (| x | ^ {\sigma} + | e | ^ {\gamma}) \tag {6.6}V (f (x, e)) - V ((x, e)) \leq - c (| x | ^ {\sigma} + | e | ^ {\gamma}) \tag {6.7}$$
