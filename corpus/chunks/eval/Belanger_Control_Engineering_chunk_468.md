a. Modify the observers for use with the incremental system referred to the dc steady state $\theta_{2} = \theta_{d}$ .   
b. Write the state descriptions for the controllers formed by using the state estimate from each observer in turn, with the pole-placement control law.   
c. Compute the closed-loop zero-state responses for the two controllers.

M

7.63 Drum speed control A state feedback-feedforward system was designed in Problem 7.33 for the system of Problem 2.7 (Chapter 2). An optimal observer was designed in Problem 7.47(a).

a. Modify the observer for use with the incremental system referred to $\omega_0 = \omega_d^*$ ( $\omega_d^* = \mathrm{dc}$ steady state for the reference). Note that the ratio $R / r$ relating $\omega_0$ and $\omega_1, \omega_2$ is usually well known, so that the steady-state relationship $\omega_1^* = \omega_2^* = (R / r)\omega_0^*$ is reliable.   
b. Write the state description of the controller obtained by combining the observer and the LQ control. It is assumed that the set point $\omega_{d}(t)$ is measured.   
c. Compute the zero-state response to $\omega_{d}(t)=25-25e^{-t/\tau}$ for the value of $\tau$ found in Problem 7.33(c). Do this for both the state feedback system and the observer-based controller.

M

7.64 Heat exchanger The heat exchanger model of Problem 2.8 (Chapter 2) was linearized in Problem 2.14. The system is subjected to constant, unmeasured disturbances. A pole-placement controller was designed in Problem 7.12. The observer designed in Problem 7.39 is to be modified to include observation of the dc steady-state input $\Delta F_H^*$ .

a. Append the equation $\Delta\dot{F}_{H}^{*}=0$ to the linearized state description as in Equations 7.96 and 7.97, and, with $\Delta T_{C3}$ as the measured output, designed an observer of order 7 to estimate the incremental states and $\Delta F_{H}^{*}$ . The error-system eigenvalues are to be those of the observer of Problem 7.37, with the addition of $-5$ .   
b. Let the controller be $\Delta F_H = \Delta \widehat{F}_H^* - K \Delta \widehat{\mathbf{x}}$ , where $K$ is the gain obtained in Problem 7.12. Compute the controller transfer function $\Delta F_H / e$ , where $e = \Delta T_{C3d} - \Delta T_{C3}$ .   
c. Compute the response $\Delta T_{C3}(t)$ to (i) a $5^{\circ}\mathrm{C}$ step change in $\Delta T_{C3d}$ and (ii) a $0.01\mathrm{m}^{3}/\mathrm{s}$ step change in $\Delta F_{C}$ .
