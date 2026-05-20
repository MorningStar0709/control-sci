$$
H = \left[ \begin{array}{c c} A & R \\ - Q & - A ^ {*} \end{array} \right].
$$

Let

$$
\Theta (t) = \left[ \begin{array}{c c} \Theta_ {1 1} (t) & \Theta_ {1 2} (t) \\ \Theta_ {2 1} (t) & \Theta_ {2 2} (t) \end{array} \right] = e ^ {H t}.
$$

Show that

$$P (t) = (\Theta_ {2 1} (t) + \Theta_ {2 2} P _ {0}) (\Theta_ {1 1} (t) + \Theta_ {1 2} (t) P _ {0}) ^ {- 1}$$

is the solution to the following differential Riccati equation:

$$- \dot {P} (t) = A ^ {*} P (t) + P (t) A + P R P + Q, \quad P (0) = P _ {0}.$$

Problem 12.14 Let $A \in \mathbb { R } ^ { n \times n }$ , $R = R ^ { * }$ , $Q = Q ^ { * }$ . Define

$$
H = \left[ \begin{array}{c c} A & R \\ - Q & - A ^ {*} \end{array} \right].
$$

Let

$$
\Theta (t) = \left[ \begin{array}{l l} \Theta_ {1 1} (t) & \Theta_ {1 2} (t) \\ \Theta_ {2 1} (t) & \Theta_ {2 2} (t) \end{array} \right] = e ^ {H (t - T)}.
$$

Show that

$$P (t) = \Theta_ {2 1} (t) \Theta_ {1 1} ^ {- 1} (t)$$

is the solution to the following differential Riccati equation:

$$- \dot {P} (t) = A ^ {*} P (t) + P (t) A + P R P + Q, \quad P (T) = 0.$$

Problem 12.15 Suppose $G ( s ) = \left[ { \frac { A \left. B \right. } { C } } \right] \in { \mathcal { R H } } _ { \infty }$ and $\| G \| _ { \infty } < \gamma$ . Show that $A + B R ^ { - 1 } D ^ { * } C$ with $R = \gamma ^ { 2 } I - D ^ { * } D ^ { - }$ is stable. (Hint: Show $A + B ( I - \Delta D / \gamma ) ^ { - 1 } \Delta C / \gamma$ is stable for all $\Delta$ with $\| \Delta \| \leq 1 . )$
