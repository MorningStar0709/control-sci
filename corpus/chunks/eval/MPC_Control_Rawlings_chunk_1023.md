# Exercise C.5: Lagrange multipliers and minmax

Consider the constrained optimization problem

$$\min _ {x \in \mathbb {R} ^ {n}} V (x) \quad \text { subject to } g (x) = 0 \tag {C.30}$$

in which $V : \mathbb { R } ^ { n }  \mathbb { R }$ and $g : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ . Introduce the Lagrange multiplier $\lambda \in \mathbb { R } ^ { m }$ and Lagrangian function $L ( x , \lambda ) = V ( x ) - \lambda ^ { \prime } g ( x )$ and consider the following minmax problem

$$\min _ {x \in \mathbb {R} ^ {n}} \max _ {\lambda \in \mathbb {R} ^ {m}} L (x, \lambda)$$

Show that if $( x _ { 0 } , \lambda _ { 0 } )$ is a solution to this problem with finite $L ( x _ { 0 } , \lambda _ { 0 } )$ , then $x _ { 0 }$ is also a solution to the original constrained optimization (C.30).
