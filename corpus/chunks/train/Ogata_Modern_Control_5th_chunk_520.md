Note that the new gain crossover frequency is decreased from approximately 1 to 0.5 radsec. This means that the bandwidth of the system is reduced.

To further show the effects of lag compensation,the log-magnitude-versus-phase plots of the gainadjusted but uncompensated system $G _ { 1 } ( j \omega )$ and of the compensated system $G _ { c } ( j \omega ) G ( j \omega )$ are shown in Figure 7–105.The plot of $G _ { 1 } ( j \omega )$ clearly shows that the gain-adjusted but uncompensated system is unstable. The addition of the lag compensator stabilizes the system. The plot of $G _ { c } ( j \omega ) G ( j \omega )$ is tangent to the $M = 3$ dB locus. Thus, the resonant peak value is 3 dB, or 1.4, and this peak occurs at $\omega = 0 . 5 \mathrm { r a d / s e c } .$ .

Compensators designed by different methods or by different designers (even using the same approach) may look sufficiently different. Any of the well-designed systems, however, will give similar transient and steady-state performance. The best among many alternatives may be chosen from the economic consideration that the time constants of the lag compensator should not be too large.

Figure 7–105 Log-magnitudeversus-phase plots of $G _ { 1 }$ (gain-adjusted but uncompensated open-loop transfer function) and $G _ { c } G$ (compensated openloop transfer function).   
![](image/94790c08253dc4f414c92bd92ae7240cbaef45a08be0a569e5c33ab3deaafc55.jpg)

Finally, we shall examine the unit-step response and unit-ramp response of the compensated system and the original uncompensated system without gain adjustment. The closed-loop transfer functions of the compensated and uncompensated systems are

$$\frac {C (s)}{R (s)} = \frac {5 0 s + 5}{5 0 s ^ {4} + 1 5 0 . 5 s ^ {3} + 1 0 1 . 5 s ^ {2} + 5 1 s + 5}$$

and

$$\frac {C (s)}{R (s)} = \frac {1}{0 . 5 s ^ {3} + 1 . 5 s ^ {2} + s + 1}$$

respectively. MATLAB Program 7–14 will produce the unit-step and unit-ramp responses of the compensated and uncompensated systems.The resulting unit-step response curves and unit-ramp response curves are shown in Figures 7–106 and 7–107, respectively. From the response curves we find that the designed system satisfies the given specifications and is satisfactory.

```matlab
MATLAB Program 7-14
