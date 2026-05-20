| Time | Value |
| --- | --- |
| 0 | 0 |
| 10 | 2 |
| 20 | -2 |
| 30 | 2 |
| 40 | -2 |
| 50 | 2 |
| 60 | -2 |
| 70 | 2 |
| 80 | -2 |
| 90 | 2 |
| 100 | -2 |
</details>

Figure 5.12 Simulation of the system in Example 5.7 using an adaptive controller based on Lyapunov theory. The parameter values are a = 1, b = 0.5, $a_{m} = b_{m} = 2$ , and $\gamma = 1$ . (a) Process (solid line) and model (dashed line) outputs. (b) Control signal.

for the MIT rule. The adjustment rule obtained from Lyapunov theory is simpler because it does not require filtering of the signals. Figure 5.12 shows a simulation of the system for the case $G(s) = 0.5/(s + 1)$ and $G_{m}(s) = 2/(s + 2)$ . The behavior is quite similar to that obtained with the MIT rule in Fig. 5.5. Notice, however, that arbitrary large values of the adaptation gain $\gamma$ can be used with the Lyapunov approach.

Figure 5.13 shows the parameter estimates in the simulation for different values of adaptation gain $\gamma$ . For comparison we have also shown the parameters obtained with the MIT rule.
