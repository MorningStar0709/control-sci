7.60 Servo, simplified model The dc servo of Problem 2.4 (Chapter 2) is subjected to an unmeasured constant torque disturbance. The output angle $\theta$ is to be regulated to a value $\theta_{d}$ . This requires a constant input $u^{*}$ , whose value depends on the load torque.

a. Write, as in Equations 7.96 and 7.97, equations for the incremental state, and append $\dot{u}^{*} = 0$ .   
b. Assume that $\theta$ and $\omega$ are measured without noise, and design a reduced-order observer of order 1 to estimate $u^{*}$ . The error system should have an eigenvalue of $-8$ . (There are many solutions for the observer gain.)   
c. With $u = \widehat{u}^* - K[\frac{\Delta\theta}{\Delta\omega}]$ , where $K$ is the state feedback gain of Problem 7.10, write the state description of the controller.   
d. Write the controller in transfer-function form $u / \Delta \theta$ , using the fact that $\Delta \omega(s) = s\Delta \theta(s)$ . Write $u / e$ , where $e = \theta_d - \theta$ .

M

7.61 Servo with flexible shaft An optimal LQ control law for the servo model of Problem 2.5 (Chapter 2) was designed in Problem 7.22. An optimal observer was designed in Problem 7.46. The observer is also valid when applied to the incremental system, defined with respect to a dc steady state $\theta_{2} = \theta_{d}$ . With $\theta_{2}, \omega_{2}$ , and $i$ as measurements, it is necessary to know the dc steady-state values of those quantities and of the input $v$ in order to generate $\Delta\theta_{2}, \Delta\omega_{2}, \Delta i$ , and $\Delta v$ . Fortunately, it was shown in Problem 7.21 that, except for $\theta_{2}$ , these variables all have zero steady state.

a. Write the state descriptions of the controller formed from the observer of Problem 7.46 with the LQ gain of Problem 7.22.   
b. In transfer-function form, the input is of the form $v = H_{1}e + H_{2}\omega_{2} + H_{3}i$ , with $e = \theta_{d} - \theta_{2}$ . Compute $H_{1}, H_{2}$ , and $H_{3}$ .   
c. Compute the closed-loop zero-state responses for a unit step $\theta_{d} = 1$ rad with (i) state feedback and (ii) the observer-based control system.

M

7.62 Servo with flexible shaft For the servo of Problem 2.5 (Chapter 2), a pole-placement control law was designed in Problem 7.11, and two reduced-order observers, of orders 4 and 2, respectively, in Problem 7.51.
