# Exercise 1.16: Method of Lagrange multipliers

Consider the objective function $V ( x ) = ( 1 / 2 ) x ^ { \prime } H x + h ^ { \prime } x$ and optimization problem

$$\min _ {x} V (x) \tag {1.57}$$

subject to

$$D x = d$$

in which $H > 0 , x \in \mathbb { R } ^ { n } , d \in \mathbb { R } ^ { m } , m < n , \mathrm { i . e }$ ., fewer constraints than decisions. Rather than partially solving for x using the constraint and eliminating it, we make use of the method of Lagrange multipliers for treating the equality constraints (Fletcher, 1987; Nocedal and Wright, 1999).

In the method of Lagrange multipliers, we augment the objective function with the constraints to form the Lagrangian function, L

$$L (x, \lambda) = (1 / 2) x ^ {\prime} H x + h ^ {\prime} x - \lambda^ {\prime} (D x - d)$$

in which $\lambda \in \mathbb { R } ^ { m }$ is the vector of Lagrange multipliers. The necessary and sufficient conditions for a global minimizer are that the partial derivatives of L with respect to x and λ vanish (Nocedal and Wright, 1999, p. 444), (Fletcher, 1987, p.198,236)
