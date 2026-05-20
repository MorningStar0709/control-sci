Figure 5.15 Outputs of the system with the controller obtained for h = 0.2 when the process gain is changed. (a) k = 0.4, (b) k = 0.8, (c) k = 1.2, and (d) k = 2.5.

whose Bode diagram is shown in Fig. 5.16 for systems with sampling periods 0.2 and 1. Figure 5.16 gives a good insight into the behavior of the system. The loop-transfer function has a phase lag of $-270^{\circ}$ at low frequencies. The controllers provide a significant phase lead to obtain a stable closed-loop system. Notice that the phase curves of the two systems are almost the same for low frequencies. The phase of the system with sampling period h = 1 does, however, decrease more rapidly after the maximum. With h = 1 the phase margin is $\varphi_{m} = 42^{\circ}$ ; and the closed-loop system is stable for $0.53 \leq k \leq 3.03$ . For h = 0.2 the corresponding values are $\varphi_{m} = 57^{\circ}$ and stability of the closed-loop system is obtained for $0.25 \leq k \leq 4$ , which explains the differences in robustness for systems with different sampling rates.

![](image/234acee737bb571cad51b273778b3a3bd4c712a1b1bc9bfaacb9495c55ce534d.jpg)

<details>
<summary>line</summary>

| x | Gain (Solid Line) | Gain (Dashed Line) |
| --- | --- | --- |
| 0.1 | ~100 | ~100 |
| 1 | ~1 | ~1 |
| 10 | ~0.01 | ~0.01 |
</details>

![](image/ffd64b0cfc59d171d821974a18e3c8009dda5a8d2008c2050fff014cb7130143.jpg)

<details>
<summary>line</summary>

| Frequency, rad/s | Phase (Solid Line) | Phase (Dashed Line) |
| --- | --- | --- |
| 0.1 | -250 | -240 |
| 1 | -150 | -130 |
| 10 | -280 | -260 |
</details>

Figure 5.16 Bode diagram for the loop-transfer functions L of the systems with sampling periods h = 0.2 (dashed line) and h = 1 (solid line).

![](image/ea426341d9ff782435bc0a71a1b65ccf9b7af9644111596335847ce3490c712d.jpg)

<details>
<summary>line</summary>

| Frequency, rad/s | Gain (Solid Line) | Gain (Dashed Line) |
| --- | --- | --- |
| 0.01 | ~0.001 | ~0.001 |
| 0.1 | ~0.1 | ~0.05 |
| 1 | ~1 | ~1 |
| 10 | ~1 | ~1 |
</details>

Figure 5.17 Amplitude curve for the sensitivity function S for systems with sampling periods h = 0.2 (dashed) and h = 1 (solid line).
