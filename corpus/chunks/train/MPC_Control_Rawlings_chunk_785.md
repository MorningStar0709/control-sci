where $V _ { x } ( w , u ) : = V _ { i } ( w , u )$ for all $i \in S ^ { 0 } ( x )$ and is, therefore, a positive definite quadratic function of $( x , u )$ . The notation $V _ { x } ^ { 0 } ( \boldsymbol { w } )$ denotes the fact that the parameter in the parametric problem $\mathbb { P } _ { x } ( \boldsymbol { w } )$ is now w but the data for the problem, namely $( E _ { x } , F _ { x } , g _ { x } )$ , is derived from the solution $u ^ { 0 } ( x )$ of $\mathbb { P } ( x )$ and is, therefore, x-dependent. Problem $\mathbb { P } _ { x } ( \boldsymbol { w } )$ is a simple equality constrained problem in which the cost $V _ { x } ( \cdot )$ is quadratic and the constraints $E _ { x } u = F _ { x } w + g _ { x }$ are linear. Let $V _ { x } ^ { 0 } ( \boldsymbol { w } )$ denote the value of $\mathbb { P } _ { x } ( \boldsymbol { w } )$ and $u _ { x } ^ { 0 } ( w )$ its solution. Then

$$V _ {x} ^ {0} (w) = (1 / 2) w ^ {\prime} Q _ {x} w + r _ {x} ^ {\prime} w + s _ {x}u _ {x} ^ {0} (w) = K _ {x} w + k _ {x} \tag {7.17}$$

where $Q _ { x } , r _ { x } , s _ { x } , K _ { x }$ and $k _ { x }$ are easily determined. It is easily seen that $u _ { x } ^ { 0 } ( x ) = u ^ { 0 } ( x )$ so that $u _ { x } ^ { 0 } ( x )$ is optimal for $\mathbb { P } ( x )$ . Our hope is that $u _ { x } ^ { 0 } ( w )$ is optimal for $\mathbb { P } ( \boldsymbol { w } )$ for all w in some neighborhood $R _ { x }$ of x. We now show this is the case.

Proposition 7.17 (Optimality of $u _ { x } ^ { 0 } ( w )$ in $R _ { x } )$ . Let x be an arbitrary point in X. Then,

(a) $u ^ { 0 } ( w ) = u _ { x } ^ { 0 } ( w )$ and $V ^ { 0 } ( w ) = V _ { x } ^ { 0 } ( w )$ for all w in the set $R _ { x }$ defined by

$$
R _ {x} := \left\{w \in \mathbb {R} ^ {n} \Big | \begin{array}{c} u _ {x} ^ {0} (w) \in \mathcal {U} _ {i} (w) \forall i \in S ^ {0} (x) \\ - \nabla_ {u} V _ {i} (w, u _ {x} ^ {0} (w)) \in C _ {i} ^ {*} (x, u ^ {0} (x)) \forall i \in S ^ {0} (x) \end{array} \right\}
$$

(b) $R _ { x }$ is a polytope

(c) $\boldsymbol { x } \in R _ { x }$
