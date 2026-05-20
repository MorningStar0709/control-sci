a. Add a feedforward control such that, up to 4 rad/s, the magnitude of the disturbance frequency response is at most -10 db. (The pertinent transfer functions were calculated in Problem 3.18, Chapter 3.)   
b. Obtain the disturbance step responses with and without feedforward, using the linearized model.

6.33 Blending tank In Problem 3.47 (Chapter 3), the linearized equations of Problem 2.13 (Chapter 2) were transformed to diagonal form, with $\Delta \ell$ and $\Delta C$ as the state variables. Use the numerical values of Problem 2.13.

a. Design a PID control for the composition, with $\Delta F_{A}$ as the input. The bandwidth is to be 4 rad/min with a phase margin of $50^{\circ}$ .   
b. For the level loop, use $\Delta F_0$ as the control variable and $\Delta F_A$ as the disturbance input. Design a pure-gain feedback for a closed-loop time constant of 5 s, and add a feedforward to cancel out the disturbance.   
c. Using the linearized model, simulate to obtain the closed-loop responses to unit steps in the set points to $\Delta \ell$ and $\Delta C$ .   
d. Using the full nonlinear model, simulate as in part (c) for steps of increasing amplitudes. What can you conclude about the range of validity of the linear model?

6.34 Chemical reactor In Problem 6.27, a PI controller was designed for the linearized model of the chemical reactor. The major disturbance in this application is $\Delta F$ , the change in flow rate.

a. Add a feedforward control to the design to increase the disturbance response bandwidth to 2.5 rad/s.   
b. For the linearized model, simulate the response to a step disturbance.

6.35 Maglev In Problem 6.10, two SISO loops were designed to control a $2 \times 2$ system with interacting variables. It may be asserted that the influence of $\Delta u_{LD}$ on $\Delta y$ is minimal, but that may not be said of the influence of $\Delta u_{GD}$ on $\Delta \theta$ . One way to take care of this is to consider $\Delta u_{GD}$ as a disturbance input affecting $\Delta \theta$ .

a. Design a feedforward control to nullify some of the effect of $\Delta u_{GD}$ on $\Delta \theta$ .   
b. Repeat parts (b) and (c) of Problem 6.10.
