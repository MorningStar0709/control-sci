# 2.4.2 Stabilizing Conditions: No State Constraints

To show as simply as possible that the descent property (2.17) holds if $V _ { f } ( \cdot )$ and $\mathbb { X } _ { f }$ are chosen appropriately, we consider first the case when there are no state or terminal constraints, i.e., $\mathbb { X } = \mathbb { X } _ { f } = \mathbb { R } ^ { n }$ , so that the only constraint is the control constraint. Hence $\bar { \mathcal { U } _ { N } ( x ) } = \mathbb { U } ^ { N }$ , which is independent of x. For this case, $\boldsymbol { \mathcal { X } } _ { j } = \mathbb { R } ^ { n }$ for all $j \in \{ 1 , 2 , \dots , N \}$ . Let x be any state in $\mathcal { X } _ { N } = \mathbb { R } ^ { n }$ at time 0. Then

$$V _ {N} ^ {0} (x) = V _ {N} (x, \mathbf {u} ^ {0} (x))$$

in which

$$\mathbf {u} ^ {0} (x) = \left\{u ^ {0} (0; x), u ^ {0} (1; x), \dots , u ^ {0} (N - 1; x) \right\}$$

is any minimizing control sequence. The resultant optimal state sequence is

$$\mathbf {x} ^ {0} (x) = \left\{x ^ {0} (0; x), x ^ {0} (1; x), \ldots , x ^ {0} (N; x) \right\}$$

where $x ^ { 0 } ( 0 ; x ) = x$ and $x ^ { 0 } ( 1 ; x ) = x ^ { + }$ . The successor state to x at time 0 is $x ^ { + } = f ( x , \kappa _ { N } ( x ) ) = x ^ { 0 } ( 1 ; x )$ at time 1 where $\kappa _ { N } ( x ) = u ^ { 0 } ( 0 ; x )$ , and

$$V _ {N} ^ {0} (x ^ {+}) = V _ {N} (x ^ {+}, \mathbf {u} ^ {0} (x ^ {+}))$$

in which

$$\mathbf {u} ^ {0} (x ^ {+}) = \left\{u ^ {0} (0; x ^ {+}), u ^ {0} (1; x ^ {+}), \dots , u ^ {0} (N - 1; x ^ {+}) \right\}$$

It is difficult to compare $V _ { N } ^ { 0 } ( x )$ and $V _ { N } ^ { 0 } ( x ^ { + } )$ directly, but

$$V _ {N} ^ {0} (x ^ {+}) = V _ {N} (x ^ {+}, \mathbf {u} ^ {0} (x ^ {+})) \leq V _ {N} (x ^ {+}, \widetilde {\mathbf {u}})$$

where $\widetilde { \mathbf { u } }$ is any feasible control sequence for $\mathbb { P } _ { N } ( x ^ { + } )$ , i.e., any control sequence in $\mathbb { U } ^ { N }$ . To facilitate comparison of $V _ { N } ( x ^ { + } ,  { \widetilde { \mathbf { u } } } )$ with $V _ { N } ^ { 0 } ( x ) =$ $V _ { N } ( x , { \bf u } ^ { 0 } ( x ) )$ , we choose

$$\widetilde {\mathbf {u}} = \left\{u ^ {0} (1; x), \dots , u ^ {0} (N - 1; x), u \right\}$$

where u still has to be chosen. Comparing u with $\mathbf { u } ^ { 0 } ( x )$ shows that $\widetilde { \mathbf { x } } ,$ the state sequence due to control sequence $\widetilde { \mathbf { u } } ,$ is

$$\widetilde {\mathbf {X}} = \left\{x ^ {0} (1; x), x ^ {0} (2; x), \dots , x ^ {0} (N; x), f (x ^ {0} (N; x), u) \right\}$$
