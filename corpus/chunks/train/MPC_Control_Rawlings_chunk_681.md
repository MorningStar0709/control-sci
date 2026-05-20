$$
\min _ {\mathbf {u} _ {1}} V (x _ {1} (0), x _ {2} (0), \mathbf {u} _ {1}, \mathbf {u} _ {2})
\text { s.t. } \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] ^ {+} = \left[ \begin{array}{c c} A _ {1} & 0 \\ 0 & A _ {2} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} \overline {{B}} _ {1 1} \\ \overline {{B}} _ {2 1} \end{array} \right] u _ {1} + \left[ \begin{array}{c} \overline {{B}} _ {1 2} \\ \overline {{B}} _ {2 2} \end{array} \right] u _ {2}
$$

Note that this form is identical to the noncooperative form presented previously if we redefine the terms (noncooperative -→ cooperative)

$$
\begin{array}{l} x _ {1} \to \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] \quad A _ {1} \to \left[ \begin{array}{c c} A _ {1} & 0 \\ 0 & A _ {2} \end{array} \right] \quad \overline {{B}} _ {1 1} \to \left[ \begin{array}{c} \overline {{B}} _ {1 1} \\ \overline {{B}} _ {2 1} \end{array} \right] \quad \overline {{B}} _ {1 2} \to \left[ \begin{array}{c} \overline {{B}} _ {1 2} \\ \overline {{B}} _ {2 2} \end{array} \right] \\ Q _ {1} \to \left[ \begin{array}{c c} \rho_ {1} Q _ {1} & 0 \\ 0 & \rho_ {2} Q _ {2} \end{array} \right] \qquad R _ {1} \to \rho_ {1} R _ {1} \quad P _ {1 f} \to \left[ \begin{array}{c c} \rho_ {1} P _ {1 f} & 0 \\ 0 & \rho_ {2} P _ {2 f} \end{array} \right] \\ \end{array}
$$

Any computational program written to solve either the cooperative or noncooperative optimal control problem can be used to solve the other.

Eliminating states $\mathbf { X } _ { 2 }$ . An alternative implementation is to remove states $x _ { 2 } ( k ) , k \geq 1$ from player one’s optimal control problem by substituting the dynamic model of system two. This implementation reduces the size of the dynamic model because only states $x _ { 1 }$ are retained. This reduction in model size may be important in applications with many players. The removal of states $x _ { 2 } ( k ) , k \geq 1$ also introduces linear terms into player $\mathrm { o n e ^ { \prime } s }$ objective function. We start by using the dynamic model for $x _ { 2 }$ to obtain
