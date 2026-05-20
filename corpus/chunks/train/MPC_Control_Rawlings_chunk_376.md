Choosing $V ( \cdot )$ to be the value function $V _ { N } ^ { 0 } ( \cdot )$ , we see that (a) is satisfied because $V _ { N } ^ { 0 } ( x ) = \mathrm { m i n } _ { \mu }$ max ${ \bf { w } } J _ { N } ( x , \pmb { \mu } , \mathbf { w } ) \geq J _ { N } ( x , \pmb { \mu } ^ { 0 } ( x ) , \pmb { 0 } ) \geq$ $\ell ( x , \kappa _ { N } ( x ) , 0 ) \geq ( 1 / 2 ) | x | _ { O } ^ { 2 } \geq \alpha _ { 1 } ( | x | )$ for some $\alpha _ { 1 } ( \cdot ) \in \mathcal { K } _ { \infty }$ where $\mathbf { 0 } =$ $\{ 0 , 0 , \ldots , 0 \}$ is a sequence of zeros and Q is positive definite. Also (b) is satisfied for all $\boldsymbol { x } \in \mathbb { X } _ { f }$ because $V _ { N } ^ { 0 } ( x ) \le V _ { f } ( x ) = ( 1 / 2 ) | x | _ { P _ { f } } ^ { 2 }$ where $P _ { f }$ is positive definite, yielding $V _ { N } ^ { 0 } ( x ) \leq \alpha _ { 2 } ( | x | )$ for all $x \in \mathbb { X } _ { f }$ , some $\alpha _ { 2 } ( \cdot ) \in \mathcal { K } _ { \infty }$ . The region of validity may be extended, as in Chapter 2, to $\boldsymbol { x } \in \mathcal { X } _ { N }$ if $x _ { N }$ is bounded. The stumbling block is condition (c). We have

$$\Delta V _ {N} ^ {0} (x, \kappa_ {N} (x), w) \leq - \ell (x, \kappa_ {N} (x), w)$$

for all $( x , w ) \in \mathcal { X } _ { N } \times \mathbb { W }$ . Thus $V _ { N } ^ { 0 } ( \cdot )$ has the following properties; there exist ${ \mathcal K } _ { \infty }$ functions $\alpha _ { 1 } ( \cdot )$ and $\alpha _ { 2 } ( \cdot )$ such that

$$
\begin{array}{l} V _ {N} ^ {0} (x) \geq \alpha_ {1} (| x |) \\ V _ {N} ^ {0} (x) \leq \alpha_ {2} (| x |) \\ \Delta V _ {N} ^ {0} (x, \kappa_ {N} (x), w) \leq - \ell (x, \kappa_ {N} (x), w) \leq - \alpha_ {1} (| x |) + (\rho^ {2} / 2) | w | ^ {2} \\ \end{array}
$$

for all $( x , w ) \in \mathcal { X } _ { N } \times \mathbb { W }$ if $x _ { N }$ is bounded. The last property, because of the term $( \rho ^ { 2 } / 2 ) | \boldsymbol { w } | ^ { 2 }$ , prevents us from establishing asymptotic stability of the origin: the disturbance w prevents convergence of x to the origin. We have to employ alternative notions of stability.

Finite $\ell _ { 2 }$ gain. Suppose Assumptions 3.8 and 3.9 hold. It follows from Theorem 3.10 that

$$\Delta V _ {N} ^ {0} (x, \kappa_ {N} (x), w) \leq - \ell (x, \kappa_ {N} (x), w) \tag {3.22}$$

for all $( x , w ) \in \mathcal { X } _ { N } \times \mathbb { W }$ . Let $\mathbf { x } = \{ x ( 0 ) , x ( 1 ) , x ( 2 ) , \ldots \} , x ( 0 ) = x \in { \mathcal { X } } _ { N }$ , denote any infinite sequence (state trajectory) of the closed-loop system with receding horizon control; x satisfies

$$x (i + 1) = f (x (i), \kappa_ {N} (x (i)), w (i))$$
