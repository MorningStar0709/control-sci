Therefore, there is no reason to consider the unreachable setpoint problem further for an unconstrained linear system. Shifting the stage cost from $\ell ( x , u )$ to $\ell _ { s } ( x , u )$ provides identical control behavior and is simpler to analyze.

Hint. First define a third stage cost $l ( x , u ) = \ell ( x , u ) - \lambda ^ { \prime } ( ( I - A ) x -$ Bu), and show, for any λ, optimizing with l(x, u) as stage cost is the same as optimizing using $\ell ( x , u )$ as stage cost. Then set $\lambda =$ $\lambda _ { S } ,$ the optimal Lagrange multiplier of the steady-state optimization problem.

(b) For constrained systems, provide a simple example that shows optimizing the cost function $V ( x , { \mathbf { u } } )$ subject to

$$x ^ {+} = A x + B u \quad x (0) = x \quad x (N) = x _ {s} \quad u (k) \in \mathbb {U} \quad \text { for all } k \in \mathbb {I} _ {0: N - 1}$$

does not give the same solution as optimizing the cost function $V _ { S } ( x , { \bf u } )$ subject to the same constraints. For constrained linear systems, these problems are different and optimizing the unreachable stage cost provides a new design opportunity.
