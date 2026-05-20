# Exercise 6.17: One variable at a time with convex step

Consider Exercise 6.15 but with the convex step for the iteration

$$
\left[ \begin{array}{c} u _ {1} ^ {p + 1} \\ u _ {2} ^ {p + 1} \end{array} \right] = w _ {1} \left[ \begin{array}{c} u _ {1} ^ {0} (u _ {2} ^ {p}) \\ u _ {2} ^ {p} \end{array} \right] + w _ {2} \left[ \begin{array}{c} u _ {1} ^ {p} \\ u _ {2} ^ {0} (u _ {1} ^ {p}) \end{array} \right] \qquad 0 \leq w _ {1}, w _ {2} \quad w _ {1} + w _ {2} = 1
$$

(a) Show that the iteration for the convex step is also of the form

$$u ^ {p + 1} = A u ^ {p} + b$$

and the A matrix and b vector for this case are

$$
A = \left[ \begin{array}{c c} w _ {2} I & - w _ {1} H _ {1 1} ^ {- 1} H _ {1 2} \\ - w _ {2} H _ {2 2} ^ {- 1} H _ {2 1} & w _ {1} I \end{array} \right] \qquad b = \left[ \begin{array}{c c} - w _ {1} H _ {1 1} ^ {- 1} & \\ & - w _ {2} H _ {2 2} ^ {- 1} \end{array} \right] \left[ \begin{array}{c} c _ {1} \\ c _ {2} \end{array} \right]
$$

(b) Show that A is stable.

(c) Show that this iteration also converges to $u ^ { * } = - H ^ { - 1 } c$ .
