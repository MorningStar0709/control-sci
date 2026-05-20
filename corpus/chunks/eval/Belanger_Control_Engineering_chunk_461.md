b. Using the linearized model, compute the state variables, given:

$$\Delta T _ {C 0} (t) = \Delta T _ {H 0} (t) = 0, \Delta F _ {H} (t) = 0. 0 5 \mathrm{m} ^ {3} / \mathrm{s},\Delta F _ {C} (t) = - 0. 0 1 \mathrm{m} ^ {3} / \mathrm{s},\Delta T _ {C 1} (0) = \Delta T _ {C 2} (0) = \Delta T _ {C 3} (0) = 7 ^ {\circ} \mathrm{C},\Delta T _ {H 1} (0) = \Delta T _ {H 2} (0) = \Delta T _ {H 3} (0) = - 1 0 ^ {\circ} \mathrm{C}.$$

Simulate the observer of part (a), driven with $\Delta T_{C3}(t)$ , $\Delta F_{C}(t)$ , and $\Delta F_{H}(t)$ from the zero state, and compare the estimated and true state variables.

M

7.40 Heat exchanger Repeat Problem 7.39 for the case where the disturbance flow $\Delta F_{C}$ is not directly available. Assume that $\Delta F_{C}(t)$ is of the form $A + Be^{-t}$ , with $A$ and $B$ constants. Thus, $\Delta F_{C}(t)$ is modeled by the second-order system

$$
\dot {\mathbf {z}} = \left[ \begin{array}{c c} 0 & 0 \\ 0 & - 1 \end{array} \right] \mathbf {z}
\Delta F _ {C} (t) = z _ {1} + z _ {2}.
$$

Add these to the system description, and add the poles -.8 and -0.9 to the observer (now of order 8). In part (b), use $z_1 = -0.01$ and $z_2 = 0.01$ , and observe $\Delta F_c(t)$ in addition to the system state variables.

M

7.41 Chemical reactor A model for a chemical reactor was derived in Problem 2.9 (Chapter 2) and linearized in Problem 2.15. Often the difficulty of measuring concentration "on line" makes it necessary to remove samples from time to time for laboratory analysis. Between laboratory measurements, it is useful to estimate concentration from on-line measurements, such as temperature.

a. Suppose $\Delta T, \Delta Q$ , and $\Delta c_{A0}$ are available, with $\Delta F = \Delta T_0 = 0$ . Use the linearized model to show that $\Delta c_B$ and $\Delta c_c$ cannot be estimated by an observer.

b. It was shown in Problem 3.48 (Chapter 3) that the first two equations (for $\Delta \dot{c}_A$ and $\Delta \dot{T}$ ) constitute a minimal realization for the input $\Delta Q$ and the output $\Delta T$ . Show that this is also the case if the input $\Delta c_{A0}$ is included.

c. Design an observer to estimate the state variables $\Delta c_A$ and $\Delta T$ , with the error-system poles at $-0.8 \pm j0.8$ .
