# Example 7.17 (dc Servo)

The dc servo of Example 7.9 is subject to a constant (but unmeasured) load torque, so as to cause the value of the dc steady-state input voltage to vary within ±.5 V. The only measurement is that of the shaft angle θ, with a precision of ±.03 rad.

(a) Set up the system equations, including $u^{*}$ as a state, as in Equations 7.96 and 7.97.   
(b) Design an optimal observer, using the weights

$$
W = \operatorname{diag} \left[ \begin{array}{c c c c} 0 & 0 & 0 & (. 5) ^ {2} \end{array} \right], \qquad V = (0. 0 3) ^ {2}.
$$

(c) Using the optimal state feedback gain $K = \begin{bmatrix} 3 & 0.8796 & 0.1529 \end{bmatrix}$ derived in Example 7.6, derive the observer-based controller and calculate its transfer function.

Solution From Equations 7.96 and 7.97, we have

$$
\frac {d}{d t} \left[ \begin{array}{c} \Delta \theta \\ \Delta \omega \\ \Delta i \\ u ^ {*} \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 0 & 0 & 4. 4 3 8 & 0 \\ 0 & - 1 2 & - 2 4 & - 2 0 \\ \hdashline 0 & 0 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} \Delta \theta \\ \Delta \omega \\ \Delta i \\ u ^ {*} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 0 \\ 2 0 \\ \hdashline 0 \end{array} \right] v.
$$

(Note the difference from Example 7.12, where the problem was to estimate the load torque; here, we estimate the constant input required to counter that torque.) Equations 7.72 and 7.73 are solved, and the observer gain is

$$
G = \left[ \begin{array}{c} \mathbf {G} _ {1} \\ - - \\ \mathbf {G} _ {2} \end{array} \right] = \left[ \begin{array}{c} 7. 1 7 4 \\ 1 9. 0 6 \\ 4. 8 2 3 \\ - - - - - \\ - 1 7. 6 7 \end{array} \right].
$$

To apply Equation 7.101, we need

$$
\begin{array}{l} A - B K - G _ {1} C = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 4. 4 3 8 \\ 0 & - 1 2 & - 2 4 \end{array} \right] - \left[ \begin{array}{l} 0 \\ 0 \\ 2 0 \end{array} \right] \left[ \begin{array}{l l l} 3 & 0. 8 7 9 6 & 0. 1 5 2 9 \end{array} \right] \\ - \left[ \begin{array}{l} 7. 1 7 4 \\ 1 9. 0 6 \\ 4. 8 2 3 \end{array} \right] \left[ \begin{array}{l l l} 1 & 0 & 0 \end{array} \right] \\ = \left[ \begin{array}{c c c} - 7. 1 7 4 & 1 & 0 \\ - 1 9. 0 6 & 0 & 4. 4 3 8 \\ - 6 4. 8 2 & - 2 9. 5 9 & - 2 7. 0 6 \end{array} \right]. \\ \end{array}
$$

From Equation 7.101, the controller, in state form, is
