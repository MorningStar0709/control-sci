# Solution

For this problem L is a $6 0 \times 6 0$ matrix $( N ( m _ { 1 } + m _ { 2 } ) )$ . The magnitudes of the largest eigenvalues are

$$
\left| \operatorname{eig} (L) \right| = \left[ \begin{array}{l l l l l l l} 1. 1 1 & 1. 1 1 & 1. 0 3 & 1. 0 3 & 0. 9 1 4 & 0. 9 1 4 & \dots \end{array} \right]
$$

The noncooperative iteration does not converge. The steady-state gains for this system are

$$
G (0) = \left[ \begin{array}{c c} 1 & 0. 5 \\ - 0. 5 & 1. 5 \end{array} \right]
$$

and we see that the diagonal elements are reasonably large compared to the nondiagonal elements. So the steady-state coupling between the two systems is relatively weak. The dynamic coupling is unfavorable, however. The response of $y _ { 1 }$ to $u _ { 2 }$ is more than four times faster than the response of $y _ { 1 }$ to $u _ { 1 }$ . The faster input is the disturbance and the slower input is used for control. Likewise the response of $y _ { 2 }$ to $u _ { 1 }$ is three times faster than the response of $y _ { 2 }$ to $u _ { 2 }$ . Also in the second loop, the faster input is the disturbance and the slower input is used for control. These pairings are unfavorable dynamically, and that fact is revealed in the instability of L and lack of a Nash equilibrium for the noncooperative dynamic regulation problem. -
