# EXAMPLE 3.9 Effect of Load Disturbances

Consider the system in Example 3.5, that is, an indirect self-tuning regulator with no zero cancellation. We will now make a simulation that is identical to the one shown in Fig. 3.6 except that the load disturbance will be $v(t) = 0.5$ for $t \geq 40$ . A forgetting factor $\lambda = 0.98$ has also been introduced; otherwise, the conditions are identical to those in Example 3.5. The behavior of the system is shown in Fig. 3.14. Compare Fig. 3.14 with Fig. 3.6. Figure 3.14 shows that a load disturbance may be disastrous. It follows from the discussion in Example 3.5 that the correct steady-state value will always be reached provided that

![](image/388dfc831ca3d2dad681a61824c697c9ecfdaa39cfee7eba9594eaa5bc9c78bc.jpg)  
Figure 3.14 Output and control signal when for a system with an indirect self-tuner without zero canceling when there is a load disturbance in the form of a step at the process input at time t = 40.

![](image/5b205ef8d3b631aa02d6fa110caa77bd0b396508866c89f2887620f10ae14c25.jpg)

<details>
<summary>line</summary>

| Time | a2 | a1 | b1 | b0 |
| --- | --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.2 | 0.0 |
| 20 | 0.0 | -1.5 | 0.1 | 0.05 |
| 40 | 0.0 | -1.5 | 0.1 | 0.05 |
| 60 | 0.0 | -1.5 | 0.1 | 0.05 |
| 80 | 0.0 | -1.5 | 0.1 | 0.05 |
| 100 | 0.0 | -1.5 | 0.1 | 0.05 |
</details>

Figure 3.15 Parameter estimates corresponding to Fig. 3.14.

the steps are sufficiently long. Notice that the response is strongly asymmetric. The reason for this is that the controller parameters change rapidly when the control signal changes; see Fig. 3.15, which shows the parameter estimates. Rapid changes of the estimates in response to command signals indicates that the model structure is not correct. The parameter estimates also change significantly at the step in the load disturbance. When the command signal is constant, the parameters appear to settle at constant values that are far from the true parameters.

There are many ways to deal with disturbances. The internal model principle is used in this section. An alternative is to estimate the disturbance and compensate for it in a feedforward fashion. An in-depth discussion of different methods and their advantages and disadvantages is found in Chapter 11.
