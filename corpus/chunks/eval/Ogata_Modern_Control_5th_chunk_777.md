$$
\left[ \begin{array}{c} \dot {\widetilde {x}} _ {1} \\ \dot {\widetilde {x}} _ {2} \end{array} \right] = \left[ \begin{array}{c c} - 1 6 & 1 \\ - 9 3. 6 & - 3. 6 \end{array} \right] \left[ \begin{array}{c} \widetilde {x} _ {1} \\ \widetilde {x} _ {2} \end{array} \right] + \left[ \begin{array}{c} 1 6 \\ 8 4. 6 \end{array} \right] y

u = - [ 2 9. 6 \quad 3. 6 ] \left[ \begin{array}{c} \widetilde {x} _ {1} \\ \widetilde {x} _ {2} \end{array} \right]
$$

The system, as a whole, is of fourth order. The characteristic equation for the system is

$$\left| s \mathbf {I} - \mathbf {A} + \mathbf {B K} \right| \left| s \mathbf {I} - \mathbf {A} + \mathbf {K} _ {e} \mathbf {C} \right| = (s ^ {2} + 3. 6 s + 9) (s ^ {2} + 1 6 s + 6 4)= s ^ {4} + 1 9. 6 s ^ {3} + 1 3 0. 6 s ^ {2} + 3 7 4. 4 s + 5 7 6 = 0$$

The characteristic equation can also be obtained from the block diagram for the system shown in Figure 10–14(b). Since the closed-loop transfer function is

$$\frac {Y (s)}{R (s)} = \frac {7 7 8 . 2 s + 3 6 9 0 . 7}{(s ^ {2} + 1 9 . 6 s + 1 5 1 . 2) (s ^ {2} - 2 0 . 6) + 7 7 8 . 2 s + 3 6 9 0 . 7}$$

the characteristic equation is

$$
\begin{array}{l} (s ^ {2} + 1 9. 6 s + 1 5 1. 2) (s ^ {2} - 2 0. 6) + 7 7 8. 2 s + 3 6 9 0. 7 \\ = s ^ {4} + 1 9. 6 s ^ {3} + 1 3 0. 6 s ^ {2} + 3 7 4. 4 s + 5 7 6 = 0 \\ \end{array}
$$

As a matter of course, the characteristic equation is the same for the system in state-space representation and in transfer-function representation.

Finally, we shall obtain the response of the system to the following initial condition:

$$
\mathbf {x} (0) = \left[ \begin{array}{c} 1 \\ 0 \end{array} \right], \qquad \mathbf {e} (0) = \left[ \begin{array}{c} 0. 5 \\ 0 \end{array} \right]
$$

Referring to Equation (10–70), the response to the initial condition can be determined from

$$
\left[ \begin{array}{c} \dot {\mathbf {x}} \\ \dot {\mathbf {e}} \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} - \mathbf {B K} & \mathbf {B K} \\ \mathbf {0} & \mathbf {A} - \mathbf {K} _ {e} \mathbf {C} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} \\ \mathbf {e} \end{array} \right], \qquad \left[ \begin{array}{c} \mathbf {x} (0) \\ \mathbf {e} (0) \end{array} \right] = \left[ \begin{array}{c} 1 \\ 0 \\ 0. 5 \\ 0 \end{array} \right]
$$

A MATLAB Program to obtain the response is shown in MATLAB Program 10–9.The resulting response curves are shown in Figure 10–15.
