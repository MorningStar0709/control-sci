# Active Damping of Oscillatory Modes

With the notch-filter design the controller makes no attempt to damp the oscillatory modes. A new design will now be done such that the servo performance is the same but the oscillations are also damped. Assume that the damping of the oscillatory modes should be changed from the open-loop damping $\zeta_{o}=0.05$ to 0.707. Further assume that the damped frequency should be the same as before. This corresponds to the continuous-time poles

$$p _ {1 2} = - 0. 7 0 7 \pm 0. 7 0 7 i$$

Let the corresponding discrete-time polynomial be denoted $A_{d}$ . Because $\deg A = 5$ the closed-loop system is of ninth order. The polynomial $A_{c}$ is the same as before and we choose the observer polynomial as $A_{o} = A_{f}A_{d}$ . The Diophantine equation (5.28) then becomes

$$A R + B S = A _ {c} A _ {d} A _ {f}$$

and the solution is obtained in the usual manner. The response of the closed-loop system is shown in Fig. 5.26. Compare Figs. 4.20 and 5.25. The servo performance is the same as before and the oscillatory modes are now damped by the controller.
