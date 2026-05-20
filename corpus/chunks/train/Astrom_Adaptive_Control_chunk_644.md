# EXAMPLE 11.2 Windup and how to avoid it

Consider the simple example of adaptive control in Example 3.5. The process has the transfer function

$$G (s) = \frac {1}{s (s + 1)}$$

Assume that there is an actuator that saturates when the magnitude of the control signal is 0.5. Figure 11.4 shows the behavior of the system if no precautions are taken in the controller. The figure clearly shows the detrimental effects of actuator saturation. The process runs open loop when the actuator saturates, and the output is drifting because the process has an integrator. This will also happen with a controller with fixed parameters. With an adaptive controller the saturation also causes the gain parameters ( $b_{0}$ and $b_{1}$ ) to be underestimated. The controller gain is then too high, and the system becomes unstable. Windup is thus much more serious in adaptive control than in a controller with constant gain.

![](image/1a214d362e09678114df443559672335ca915c3f9f04d8c9ee2e048085725b5a.jpg)  
Figure 11.5 Simulation of an adaptive controller for a process with a saturating actuator with a controller having windup protection. Compare with Fig. 11.4, which shows the same simulation for a system without windup protection.

Figure 11.5 shows a simulation corresponding to Fig. 11.4 when the modification (11.1) is introduced to avoid windup. In this case there are clearly no difficulties. The control signal remains within the bounds -0.5 < u < 0.5 all the time. If the control signal saturates over a longer period of time, the adaptation should be switched off.

Windup will always cause difficulties. In cases like Example 11.2 the phenomenon is serious because the process is unstable. If the controller is unstable, the control law given by Eqs. (11.1) will automatically reset the controller state with a speed corresponding to the observer dynamics.
