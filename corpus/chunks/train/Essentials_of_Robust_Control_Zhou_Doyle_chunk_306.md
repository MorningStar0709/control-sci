Next, we shall establish the precise relationship between the preceding all stabilizing controller parameterization and the state-space parameterization in the last section. The following theorem follows from some algebraic manipulation.

Theorem 11.8 Let the doubly coprime factorizations of $G _ { 2 2 }$ be chosen as

$$
\left[ \begin{array}{c c} M & U _ {0} \\ N & V _ {0} \end{array} \right] = \left[ \begin{array}{c c} A + B _ {2} F & B _ {2} \quad - L \\ \hline F & I \quad 0 \\ C _ {2} + D _ {2 2} F & D _ {2 2} \quad I \end{array} \right]

\left[ \begin{array}{c c} \tilde {V} _ {0} & - \tilde {U} _ {0} \\ - \tilde {N} & \tilde {M} \end{array} \right] = \left[ \begin{array}{c c c} A + L C _ {2} & - (B _ {2} + L D _ {2 2}) & L \\ \hline F & I & 0 \\ C _ {2} & - D _ {2 2} & I \end{array} \right]
$$

where F and L are chosen such that $A + B _ { 2 } F$ and $A + L C _ { 2 }$ are both stable. Then $J _ { y }$ can be computed as

$$
J _ {y} = \left[ \begin{array}{c c c} A + B _ {2} F + L C _ {2} + L D _ {2 2} F & - L & B _ {2} + L D _ {2 2} \\ \hline F & 0 & I \\ - (C _ {2} + D _ {2 2} F) & I & - D _ {2 2} \end{array} \right].
$$

Remark 11.3 Note that $J _ { y }$ is exactly the same as the J in Theorem 11.4 and that $K _ { 0 } : = U _ { 0 } V _ { 0 } ^ { - 1 }$ is an observer-based stabilizing controller with

$$
K _ {0} := \left[ \begin{array}{c c} A + B _ {2} F + L C _ {2} + L D _ {2 2} F & - L \\ \hline F & 0 \end{array} \right].
$$

![](image/690cccbb8e90646a9f4b0b49afbffe4a5073a04a3f53bb461cb5cc87e0c5db9d.jpg)
