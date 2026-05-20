# Example 4.12 Control of the double integrator

Consider the double-integrator plant and assume that there is a process disturbance in the form of an unknown constant that is acting on the process input. Let the feedback vector L is determined as in Examples 4.2 and 4.4 with the closed-loop natural frequency $\omega = 1$ , the damping $\zeta = 0.7$ , and h = 0.44. Figure 4.16 shows the control of the double integrator when using the controller (4.64). There is first an input load disturbance at time t = 5, and then a change in the reference value to the model at t = 30. The model is designed to be twice as fast as when L is designed. The simulation shows that the regulation and servo problems can be separated and given different dynamics.

![](image/aed55005e9985604cb0ece57c9d87ef22c0484af89beff59b947620c061d850f.jpg)  
Figure 4.16 Control of the double integrator using the controller (4.64). (a) Output (solid) and model output $y_{m}$ (dots), (b) control signal, (c) disturbance v (dashed) and estimated disturbance $\hat{v}$ (solid).
