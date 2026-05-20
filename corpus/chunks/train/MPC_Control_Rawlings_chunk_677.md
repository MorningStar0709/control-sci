# Solution

For this case the largest magnitude eigenvalues of L are

$$
\left| \operatorname{eig} (L) \right| = \left[ \begin{array}{l l l l l l l} 0. 6 3 & 0. 6 3 & 0. 6 2 & 0. 6 2 & 0. 5 9 & 0. 5 9 & \dots \end{array} \right]
$$

and we see the Nash equilibrium for the noncooperative game is stable. So we have removed the first source of closed-loop instability by switching the input-output pairings of the two subsystems. There are seven states in the complete system model, and the magnitudes of the eigenvalues of the closed-loop regulator $( A + B K )$ are

$$
\left| \operatorname{eig} (A + B K) \right| = \left[ \begin{array}{c c c c c c c} 1. 0 3 & 1. 0 3 & 0. 3 7 & 0. 3 7 & 0. 7 7 & 0. 7 7 & 0. 0 4 \end{array} \right]
$$

which also gives an unstable closed-loop system. We see the distributed noncooperative regulator has destabilized a stable open-loop system. The problem with this pairing is the steady-state gains are now

$$
G (0) = \left[ \begin{array}{c c} - 0. 5 & 1. 5 \\ 1 & 0. 5 \end{array} \right]
$$

If one computes any steady-state interaction measure, such as the relative gain array (RGA), we see the new pairings are poor from a steadystate interaction perspective

$$
\mathrm{RGA} = \left[ \begin{array}{c c} 0. 1 4 & 0. 8 6 \\ 0. 8 6 & 0. 1 4 \end{array} \right]
$$

Neither pairing of the inputs and outputs is closed-loop stable with noncooperative distributed MPC.

Decentralized control with this pairing is discussed in Exercise 6.10.

![](image/f374aea8d2cede5d1b4d29d8c80f909d66b441068004a18d4716ed5efb2f9d29.jpg)
