Inputs A, B, C, and D are the SSR matrices</td></tr><tr><td>eig (A)</td><td>Computes the eigenvalues of square matrix A</td></tr><tr><td>step (sys)</td><td>Plots the unit-step response of the LTI system sys (created by either tf or ss)</td></tr><tr><td>[y, t] = step (sys)</td><td>Computes the unit-step output response y and simulation time t of system sys (no plot is created)</td></tr><tr><td>impulse (sys)</td><td>Plots the unit-impulse response of the LTI system sys (created by either tf or ss)</td></tr><tr><td>[y, t] = impulse (sys)</td><td>Computes the unit-impulse output response y and simulation time t of system sys (no plot is created)</td></tr><tr><td>lsim (sys, u, t)</td><td>Plots the response of the LTI system sys for an arbitrary input u corresponding to time vector t</td></tr><tr><td>[y, t] = lsim (sys, u, t)</td><td>Computes the output response y and simulation time t of system sys to arbitrary input u (no plot is created)</td></tr><tr><td>initial (sys, x0)</td><td>Plots the free response of the state-space representation model sys given the initial state vector x0</td></tr><tr><td>[y, t, x] = initial (sys, x0, t)</td><td>Computes the free response output y and states x of the state-space representation model sys given the initial state vector x0 and time vector t (no plot is created)</td></tr><tr><td>bode (sys)</td><td>Creates and draws the Bode diagram for LTI system sys (created by either tf or ss)</td></tr><tr><td>[Mag, phase] = bode (sys, w)</td><td>Computes the magnitude and phase (in deg) of the LTI system sys for input frequency w (rad/s).
No Bode diagram is drawn</td></tr><tr><td>wB = bandwidth (sys)</td><td>Computes the bandwidth frequency wB (rad/s) for LTI system sys</td></tr></table>

```txt
p = -3
-1 % vector of poles of F(s)
k = [] % no direct term because order of numF < order of denF 
```

Using the residues, the partial-fraction expansion of F(s) is

$$F (s) = \frac {- 7}{s + 3} + \frac {5}{s + 1}$$
