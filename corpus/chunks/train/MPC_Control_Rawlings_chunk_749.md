# Exercise 6.27: The constrained two-variable special case

Consider the special case of Exercise 6.26 with $M = 2$

$$\min _ {u _ {1}, u _ {2}} V (u _ {1}, u _ {2}) \quad \text { subject to } \quad u _ {1} \in \mathbb {U} _ {1} \quad u _ {2} \in \mathbb {U} _ {2}$$

in which V is a strictly positive quadratic function. Assume that the feasible region is convex and nonempty and denote the unique optimal solution as $( u _ { 1 } ^ { * } , u _ { 2 } ^ { * } )$ having cost $V ^ { * } = V ( u _ { 1 } ^ { * } , u _ { 2 } ^ { * } )$ . Consider the two one-variable-at-a-time optimization problems at iteration k

$$u _ {1} ^ {p + 1} = \arg \min _ {u _ {1}} V (u _ {1}, u _ {2} ^ {p}) \quad u _ {2} ^ {p + 1} = \arg \min _ {u _ {2}} V (u _ {1} ^ {p}, u _ {2})\text { subject to } u _ {1} \in \mathbb {U} _ {1} \quad \text { subject to } u _ {2} \in \mathbb {U} _ {2}$$

We know from Exercise 6.15 that taking the full step in the unconstrained problem with M = 2 achieves a cost decrease. We know from Exercise 6.19 that taking the full step for an unconstrained problem with $M \ge 3$ does not provide a cost decrease in general. We know from Exercise 6.26 that taking a reduced step in the constrained problem for all M achieves a cost decrease. That leaves open the case of a full step for a constrained problem with $M = 2$ .

Does the full step in the constrained case for $M = 2$ guarantee a cost decrease? If so, prove it. If not, provide a counterexample.
