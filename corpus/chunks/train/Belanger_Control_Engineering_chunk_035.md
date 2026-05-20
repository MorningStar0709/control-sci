1. $x_{1}(0) = 1.5 \, \text{m}, x_{2}(0) = .75 \, \text{m}, v_{1}(0) = v_{2}(0) = 0, u(t) = y_{R}(t) = 0, 0 \leq t \leq 5 \, \text{s}$ . This shows the transient behavior of the system. The result (MATLAB command step) is given in Figure 2.5.   
2. Initial conditions are the final conditions in 1, i.e., the steady-state equilibrium. The road has a rectangular bump of height 0.15 m and length 2 m. Assume $u(t) = 0$ . Simulate for $0 \leq t \leq 5$ s, with t = 0 being the time at which the vehicle just hits the bump, for a vehicle speed of 30 km/h. It is easily seen that $y_{R}(t)$ is a rectangular pulse of height 0.15 m and duration 2.0/V, where V is the speed in meters per second. The results (MATLAB command lsim) are shown in Figure 2.6.   
3. Initial conditions are steady-state equilibrium; $0 \leq t \leq 5$ s; the road height is described by the signal $\sum_{n=0}^{4} 0.1 \sin(5 + 4n)t$ . This signal is meant to

![](image/30eeb7f88d16b3b787d2ea55f910070169b8dd16cf30378f310642554fd78d79.jpg)

<details>
<summary>line</summary>

| Time(s) | x1 | x2 |
| --- | --- | --- |
| 0.0 | 1.2 | 0.6 |
| 0.5 | 1.3 | 0.6 |
| 1.0 | 1.2 | 0.6 |
| 1.5 | 1.1 | 0.6 |
| 2.0 | 1.1 | 0.6 |
| 2.5 | 1.1 | 0.6 |
| 3.0 | 1.1 | 0.6 |
| 3.5 | 1.1 | 0.6 |
| 4.0 | 1.1 | 0.6 |
| 4.5 | 1.1 | 0.6 |
| 5.0 | 1.1 | 0.6 |
</details>

Figure 2.6 Time responses for the active suspension system: Responses to a pulse

![](image/87b48e358b307c384a4ea7e8f1a0e1b5ad47ae58c62402ecf12c85b359689f36.jpg)

<details>
<summary>line</summary>

| Time(s) | x1 | x2 |
| --- | --- | --- |
| 0.0 | 1.2 | 0.6 |
| 0.5 | 1.1 | 0.4 |
| 1.0 | 1.0 | 0.6 |
| 1.5 | 1.1 | 0.3 |
| 2.0 | 1.0 | 0.7 |
| 2.5 | 1.1 | 0.6 |
| 3.0 | 1.0 | 0.5 |
| 3.5 | 1.1 | 0.8 |
| 4.0 | 1.0 | 0.6 |
| 4.5 | 1.1 | 0.9 |
| 5.0 | 1.0 | 0.2 |
</details>

Figure 2.7 Time responses for the active suspension system: Response to a sum of sinusoids

approximate a random process by summing harmonically unrelated sinusoids. The results (MATLAB command lsim) are given in Figure 2.7.
