# Exercise 5.15 (Linear quadratic optimal tracking)

For completeness, we consider a slightly more general form of the linear quadratic regulator. The standard LQR derivation attempts to drive the system to zero. Consider now the problem:

$$u ^ {*} := \underset {u: [ 0, T ] \rightarrow \mathbb {R} ^ {m}} {\operatorname{argmin}} J (u) \tag {340}$$

subject to (341)

$$\dot {x} (t) = A x (t) + B u (t), \quad x (0) = x _ {0} \tag {342}$$

where

$$
\begin{array}{l} J (u) := \left(x (T) - x _ {d} (T)\right) ^ {T} Q _ {f} \left(x (T) - x _ {d} (T)\right) \\ + \int_ {0} ^ {T} \left((x (t) - x _ {d} (t)) ^ {T} Q (x (t) - x _ {d} (t)) + (u (t) - u _ {d} (t)) ^ {T} R (u (t) - u _ {d} (t))\right) d t \tag {343} \\ \end{array}
$$

$Q _ { f } = Q _ { f } ^ { T } \ge 0$ (positive semidefinite), $Q = Q ^ { T } \geq 0$ (positive semidefinite), $R =$ $R ^ { T } > 0$ (positive definite).

Find a formulation of an optimal policy and the corresponding HJB equation (similar to the Riccati equation) using the sufficient condition.

Hint: consider a candidate of value functions of the following form

$$\hat {V} (x, t) = x ^ {T} S _ {2} (t) x + s _ {1} ^ {T} (t) x + s _ {0} (t), \quad S _ {2} (t) = S _ {2} (t) ^ {T} > 0, \quad s _ {1} (t) \in \mathbb {R} ^ {n}, \quad s _ {0} (t) \in \mathbb {R}. \tag {344}$$
