# EXAMPLE 10.1 An industrial robot arm

A simple model of a robot arm is used in this example. The transfer function from the control input (motor current I) to measurement output (motor angular velocity $\omega$ ) is

$$G _ {p} (s) = \frac {k _ {m} \left(J _ {a} s ^ {2} + d s + k\right)}{J _ {a} J _ {m} s ^ {3} + d \left(J _ {a} + J _ {m}\right) s ^ {2} + k \left(J _ {a} + J _ {m}\right) s}$$

![](image/2bff0e8313b1e08e685c9d4f34d008a634d32361d8209c9c25f7f03d4dbb88b7.jpg)  
Figure 10.2 Bode plots for the robot arm in Example 10.1 for $J_{o} = 0.0002$ and $J_{o} = 0.002$ .

with $J_{a} \in [0.0002, 0.002]$ , $J_{m} = 0.002$ , d = 0.0001, k = 100, and $k_{m} = 0.5$ . The moment of inertia $J_{a}$ of the robot arm varies with the arm angle. Bode plots of the plant gain for the extreme values of the arm inertia $J_{a}$ are given in Fig. 10.2. The purpose of the control system is to control the angular velocity step responses at various arm angles. The aim is to get a closed-loop system with a bandwidth between 15 and 40 Hz. The disturbance rejection specification has been set to 6 dB. A feedback compensator that satisfies the specifications is

$$G _ {f b} (s) = \frac {1 2 5 (1 + s / 5 0) (1 + s / 3 0 0)}{s (1 + s / 8 0 0) (1 + s / 5 0 0 0)}$$

This compensator is essentially a PI controller with a lead filter. The final prefilter has the transfer function

$$G _ {f f} (s) = \frac {1 + s / 1 0 0 0}{(1 + s / 2 6) (1 + s / 2 0 0) (1 + s / 2 0 0)}$$

Simulated responses are shown in Figs. 10.3 and 10.4.

To make a comparison, an adaptive controller is also designed for the process. In this particular problem the essential uncertainty is in one parameter only, the moment of inertia. It is then natural to try to make a special adaptive design in which only this parameter is estimated.

![](image/bf8fd363c46b276c78818e2372891bdd7393256184f222fb9304db96bdadef78.jpg)  
Figure 10.3 Simulation of the step response with the arm inertia $J_{a} = 0.0002$ for the robust system.

![](image/b2ce484619c09e94dc469f50542328140a96ac86549d71fbb294bfdab5dacf39.jpg)

<details>
<summary>line</summary>

| Time | u_c | u |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.1 | 1.0 | 0.7 |
| 0.2 | 1.0 | -0.1 |
| 0.3 | 1.0 | 0.0 |
| 0.4 | 1.0 | 0.0 |
| 0.5 | 1.0 | 0.0 |
| 0.6 | 1.0 | 0.0 |
</details>

Figure 10.4 Simulation of the step response with the arm inertia $J_{u} = 0.002$ for the robust system.

The adaptive controller is designed on the basis of a simplified model. If we neglect the elasticity in the robot arm, the system can be described by
