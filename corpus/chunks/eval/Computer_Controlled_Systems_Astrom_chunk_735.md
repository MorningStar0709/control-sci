# A Pole-Placement Interpretation

Simple calculations show that the characteristic equation of the closed-loop system obtained from (12.5) and (12.31) is

$$z ^ {d - 1} B ^ {*} (z) B ^ {- *} (z) C (z) = 0$$

Thus the control law of (12.31) can be interpreted as a pole-placement controller, which gives this characteristic equation.

Multiplication of (12.32) by $B^{+}$ gives the equation

$$A (z) R (z) + B (z) S (z) = z ^ {d - 1} B ^ {+} (z) B ^ {- *} (z) C (z) \tag {12.37}$$

where $R(z) = B^{+}(z)F(z)$ and $S(z) = G(z)$ . This equation is the same Diophantine equation that was used in the pole-placement design [compare with Eq. (5.22)]. The closed-loop system has poles corresponding to the observer dynamics, to the stable process zeros, and to the reflections in the unit circle of the unstable process zeros. Notice that the transfer function $B(z)/A(z)$ may be interpreted as having $d = \deg A - \deg B$ zeros at infinity. The reflections of these zeros in the unit circle also appear as closed-loop poles, which are located at the origin.

Equation (12.37) shows that the closed-loop system is of order 2n - 1 and that d - 1 of the poles are in the origin. A complete controller consisting of a full Kalman filter observer and feedback from the observed states gives a closed-loop system of order 2n. The “missing” pole is due to a cancellation of a pole at the origin in the controller. This is further discussed in Sec. 12.5.
