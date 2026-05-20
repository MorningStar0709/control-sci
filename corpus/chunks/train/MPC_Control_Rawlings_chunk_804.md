# Exercise 7.6: Cost function in constrained linear control problem

Show that $| x | _ { p } , p \ = \ 1$ and $p \ = \ \infty$ , may be expressed as max ${ } _ { j } \{ s _ { j } ^ { \prime } x ~ | ~ j \in { \cal J } \}$ and determine $s _ { i } , i \in I$ for the two cases $p = 1$ and $p \ : = \ : \infty$ . Hence show that the optimal control problem in Section 7.8 may be expressed as

$$V _ {N} ^ {0} (x) = \min _ {\mathbf {v}} \left\{V _ {N} (x, \mathbf {v}) \mid \mathbf {M v} \leq \mathbf {N x} + \mathbf {p} \right\}$$

where, now, v is a column vector whose components are $u ( 0 ) , u ( 1 ) , \ldots , u ( N - 1 )$ , $\ell _ { x } ( 0 ) , \ell _ { x } ( 1 ) , \ldots , \ell _ { x } ( N ) , \ell _ { u } ( 0 ) , \ell _ { u } ( 1 ) , \ldots , \ell _ { u } ( N - 1 )$ and $f ;$ the cost $V _ { N } ( x , { \bf v } )$ is now defined by

$$V _ {N} (x, \mathbf {v}) = \sum_ {i = 0} ^ {N - 1} \left(\ell_ {x} (i) + \ell_ {u} (i)\right) + f$$

Finally, $\mathbf { M } \mathbf { v } \leq \mathbf { N } x + \mathbf { p }$ now specifies the constraints u $\iota ( i ) \in \mathbb { U }$ and $x ( i ) \in \mathbb { X } , | R u ( i ) | _ { p } \leq$ $\ell _ { u } ( i ) , | Q x ( i ) | _ { p } \leq \ell _ { x } ( i ) , i = 0 , 1 , \ldots , N - 1 , x ( N ) \in \mathbb { X } _ { f } |$ , and $| Q _ { f } x ( N ) | \leq f$ . As before, $\mathbf { x } ^ { + } = \mathbf { F } \mathbf { x } + \mathbf { G } \mathbf { u }$ .
