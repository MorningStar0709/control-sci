# Example 4.5 Deadbeat control of a double integrator

Consider a double-integrator plant. It follows from Eq. (4.19) that the deadbeat control strategy is given by $u = -l_{1}x_{1} - l_{2}x_{2}$ with

$$l _ {1} = \frac {1}{h ^ {2}} \quad l _ {2} = \frac {3}{2 h}$$

If the process has the initial state $x(0) = \operatorname{col}[x_0, v_0]$ , it follows that

$$u (0) = - \frac {x _ {0}}{h ^ {2}} - \frac {3 v _ {0}}{2 h} \quad u (h) = \frac {x _ {0}}{h ^ {2}} + \frac {v _ {0}}{2 h}$$

Notice that the magnitude of the control signal increases rapidly with decreasing sampling period. Also notice that for small $h$ , the control signals $u(0)$ and $u(h)$ have opposite signs and approximately equal magnitude. The desired effect is thus obtained as a result of subtracting two large numbers. This is further illustrated in Table 4.1, which gives the control signals for $x_0 = 1$ and $v_0 = 1$ . It therefore can be expected that the deadbeat strategy is quite sensitive for small sampling periods. The output and the control signals are shown in Fig. 4.5. In this case the first sampling is at $t = 0+$ . The disturbance thus occurs immediately before the sampling.
