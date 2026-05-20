# EXAMPLE 1.2 Similar open-loop responses

Consider systems with the open-loop transfer functions

$$G _ {0} (s) = \frac {4 0 0 (1 - s T)}{(s + 1) (s + 2 0) (1 + T s)}$$

with T = 0, 0.015, and 0.03. The open-loop step responses are shown in Fig. 1.6(a). Figure 1.6(b) shows the step responses for the closed-loop systems obtained with the feedback $u = u_{c} - y$ . Notice that the open-loop responses

![](image/fc70e9f7f1ba75a2396ba12964f6d5989527fdffa5fa8af83fab30e39e5d8973.jpg)

![](image/cd655ba9c910dfb98d3fef06afe24ffb9762a1fb1b337822044622485e5ab324.jpg)

<details>
<summary>line</summary>

| x | T = 0 | T = 0.05 | T = 0.03 |
| --- | --- | --- | --- |
| 10^-1 | 10^0 | 10^0 | 10^0 |
| 10^0 | 10^0 | 10^0 | 10^0 |
| 10^1 | 10^0 | 10^0 | 10^0 |
| 10^2 | 10^-2 | 10^0 | 10^0 |
| 10^3 | 10^-2 | 10^0 | 10^0 |
</details>

![](image/3409510979c9bd05a320c0fd83eb15ca1234591649f73e71fe70b8c5a39d35f4.jpg)

<details>
<summary>line</summary>

| Frequency [rad/s] | T = 0 | T = 0.015 | T = 0.03 |
| --- | --- | --- | --- |
| 0.1 | ~0 | ~0 | ~0 |
| 1 | ~0 | ~0 | ~0 |
| 10 | ~-100 | ~-150 | ~-200 |
| 100 | ~-200 | ~-250 | ~-300 |
| 1000 | ~-250 | ~-300 | ~-350 |
</details>

Figure 1.7 Bode diagrams for the process in Example 1.2. (a) The open-loop system; (b) The closed-loop system.

are very similar but that the closed-loop responses differ considerably. The frequency responses give some insight. The Bode diagrams for the open- and closed-loop systems are shown in Fig. 1.7. Notice that the frequency responses of the open-loop systems are very close for low frequencies but differ considerably in the phase at high frequencies. It is thus possible to design a controller that works well for all systems provided that the closed-loop bandwidth is chosen to be sufficiently small. At the crossover frequency chosen in the example there are, however, significant variations that show up in the Bode diagrams of the closed-loop systems in Fig. 1.7(b) and in the step responses of the closed-loop system in Fig. 1.6(b).

The examples discussed show that to judge the consequences of process variations from open-loop dynamics, it is better to use frequency responses than time responses. It is also necessary to have some information about the desired crossover frequency of the closed-loop system. Intuitively, it may be expected that a process variation that changes dynamics from unstable to stable is very severe. Example 1.1 shows that this is not necessarily the case.
