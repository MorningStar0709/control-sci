a. Compute the LQ gain matrix for the same performance index as in Problem 7.22, but with $Q_{33} \Delta \omega_0^2$ replaced by $Q_{33}[\Delta \omega_0(t) - z(t)]^2$ , where $z(t) = -25e^{-t / \tau}$ and incremental quantities are defined with respect to the steady state $\omega_0 = 25 \mathrm{rad/s}$ . Use your design of Problem 7.23 for the $Q$ 's and $R$ 's, and $\tau = 10 \mathrm{s}$ .   
b. Compute the response for zero initial state. Check the constrained variables $u_{1}, u_{2}, \Delta_{1}$ , and $\Delta_{2}$ against their limits. Go back to part (a) and repeat for other values of $\tau$ until a value is found where the constraints are just met. Give $\tau$ and the control law.

![](image/968c9d601985611aa790843a329b970f7d1a4429071bfc07cec1c02e54036a0e.jpg)

7.34 Drum speed control We wish to design a disturbance feedforward control for the drum speed control.

a. Calculate the dc steady-state input and state variables for $\omega_0 = \omega_d$ , $T_0 = T_0^*$ , and $\Delta_1^* = \Delta_2^*$ . Express $u_1^*$ and $u_2^*$ as functions of $\omega_d$ and $T_0^*$ .

b. Compute the steady state for $\omega_0 = 25$ rad/s and $T_0 = 0$ . Apply a step torque $T_0 = 10^4$ Nm, and calculate the response for the LQ control of Problem 7.23. Leave $u_1^*$ and $u_2^*$ unchanged; i.e., do not use disturbance feedforward. Note the peak values of $\Delta_1$ and $\Delta_2$ and the response $\omega_0(t)$ .

c. Repeat part (b), but with disturbance feedforward; i.e., apply step changes to $u_1^*$ and $u_2^*$ corresponding to the expressions derived in part (a). Compare the responses with those of part (b).

![](image/307677fd3b36dfead29698e4c06cacd9f69f375e9e354c8b00d011742a39fc89.jpg)

7.35 Blending tank The blending tank model of Problem 2.7 (Chapter 2) was linearized about a given dc steady state in Problem 2.13.

a. Using the linearized model, calculate the changes in $\Delta F_0^*$ and $\Delta F_A^*$ in the dc steady-state inputs that cancel out steady-state disturbance change $\Delta F_B^*$ . Express $\Delta F_0^*$ and $\Delta F_A^*$ as functions of $\Delta F_B^*$ , and show that the application of this linear feedforward law will cancel out the effect of the disturbance, not only as the steady state but in the transient state as well.

b. Let $\Delta C_{Ad}(t) = \Delta C_{Ad}^{*}(1 - e^{-t / 50})$ , with $\Delta F_B = 0$ . Solve for the optimal LQ gain, with
