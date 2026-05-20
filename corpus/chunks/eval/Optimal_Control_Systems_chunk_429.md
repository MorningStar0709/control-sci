# Example 7.2

Consider a second order system

$$\dot {x} _ {1} (t) = x _ {2} (t)\dot {x} _ {2} (t) = u (t), \tag {7.6.14}$$

and the performance index

$$J (u) = \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \left[ x _ {1} ^ {2} (t) + u ^ {2} (t) \right] d t, \tag {7.6.15}$$

where, time $t_f$ is free and the final state $\mathbf{x}(t_f)$ is free. The control $u(t)$ is constrained as

$$- 1 \leq u (t) \leq + 1 \quad \text { or } \quad | u (t) | \leq + 1 \text { for } t \in [ t _ {0}, t _ {f} ], \tag {7.6.16}$$

and the state $x_{2}(t)$ is constrained as

$$- 3 \leq x _ {2} (t) \leq + 3 \quad \text { or } \quad | x _ {2} (t) | \leq + 3 \text { for } t \in [ t _ {0}, t _ {f} ]. \tag {7.6.17}$$

Find the optimal control.

Table 7.1 Procedure Summary of Optimal Control Systems with State Constraints
