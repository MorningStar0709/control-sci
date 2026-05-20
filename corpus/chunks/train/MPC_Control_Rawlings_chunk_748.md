# Exercise 6.26: Constrained optimization of M variables

Consider an optimization problem with M variables and uncoupled constraints

$$\min _ {u _ {1}, u _ {2}, \dots , u _ {M}} V (u _ {1}, u _ {2}, \dots , u _ {M}) \quad \text { subject to } \quad u _ {l} \in \mathbb {U} _ {j} \quad j = 1, \dots , M$$

in which V is a strictly convex function. Assume that the feasible region is convex and nonempty and denote the unique optimal solution as $( u _ { 1 } ^ { * } , u _ { 2 } ^ { * } , \ldots , u _ { M } ^ { * } )$ having cost $V ^ { * } = V ( u _ { 1 } ^ { * } , \ldots , u _ { M } ^ { * } )$ . Denote the M one-variable-at-a-time optimization problems at iteration k

$$z _ {j} ^ {p + 1} = \arg \min _ {u _ {j}} V (u _ {1} ^ {p}, \dots , u _ {j}, \dots , u _ {M} ^ {p}) \quad \text { subject to } u _ {j} \in \mathbb {U} _ {j}$$

Then define the next iterate to be the following convex combination of the previous and new points

$$u _ {j} ^ {p + 1} = \alpha_ {j} ^ {p} z _ {j} ^ {p + 1} + (1 - \alpha_ {j} ^ {p}) u _ {j} ^ {p} \quad j = 1, \dots , M\varepsilon \leq \alpha_ {j} ^ {p} < 1 \quad 0 < \varepsilon \quad j = 1, \dots , M, \quad p \geq 1\sum_ {j = 1} ^ {M} \alpha_ {j} ^ {p} = 1, \quad p \geq 1$$

Prove the following results.

(a) Starting with any feasible point, $( u _ { 1 } ^ { 0 } , u _ { 2 } ^ { 0 } , \ldots , u _ { M } ^ { 0 } )$ , the iterations $( u _ { 1 } ^ { p } , u _ { 2 } ^ { p } , \ldots , u _ { M } ^ { p } )$ are feasible for $p \geq 1$ .

(b) The objective function decreases monotonically from any feasible initial point

$$V (u _ {1} ^ {p + 1}, \dots , u _ {M} ^ {p + 1}) \leq V (u _ {1} ^ {p}, \dots , u _ {M} ^ {p}) \quad \forall u _ {l} ^ {0} \in \mathbb {U} _ {j}, j = 1, \dots , M, \quad p \geq 1$$

(c) The cost sequence $V ( u _ { 1 } ^ { p } , u _ { 2 } ^ { p } , \ldots , u _ { M } ^ { p } )$ converges to the optimal cost $V ^ { * }$ from any feasible initial point.

(d) The sequence $( u _ { 1 } ^ { p } , u _ { 2 } ^ { p } , \ldots , u _ { M } ^ { p } )$ converges to the optimal solution $( u _ { 1 } ^ { * } , u _ { 2 } ^ { * } , \ldots , u _ { M } ^ { * } )$ from any feasible initial point.
