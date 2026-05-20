Figure 4.3 shows the response to an initial condition when an impulse disturbance has entered the system just before the sampling. In reality the disturbances of course may enter the system at any time. With a long sampling period it will then take a long time before the disturbance is detected. To illustrate this we will repeat the simulation in Fig. 4.3 but it will be assumed that the disturbance comes just after a sampling. This implies that the disturbance acts for a full sampling period before it is detected. Figure 4.4 shows the response of the system when the system is disturbed immediately after the sampling, that is, when $x(0+) = [1 - 1]^T$ . Notice the significant difference compared with Fig. 4.3. In this case the results for $N = 20$ are much better than the results for $N = 10$ . It is reasonable to choose $N$ in the range $N \approx 25$ to 75. This corresponds to $\omega h = 0.12$ to 0.36 for $\zeta = 0.707$ .

![](image/845eb6b661f76d10873992ade8b028b58f11c9ec27fd4c352a82b2125b8f9d35.jpg)

<details>
<summary>line</summary>

| x | Output |
| --- | --- |
| 0 | 1.5 |
| 1 | 1.8 |
| 2 | 1.6 |
| 3 | 1.2 |
| 4 | 0.8 |
| 5 | 0.3 |
| 6 | 0.1 |
| 7 | 0.05 |
| 8 | 0.02 |
| 9 | 0.01 |
| 10 | 0.0 |
</details>

![](image/7fe4bd20b60b5c533fa65f126d3a0739ebfdd28d98b4f067f0e273e8e409ba00.jpg)

<details>
<summary>line</summary>

| x | Input |
| --- | --- |
| 0 | -1.0 |
| 1 | -1.0 |
| 2 | 0.0 |
| 3 | 0.0 |
| 4 | 0.0 |
| 5 | 0.0 |
| 6 | 0.0 |
| 7 | 0.0 |
| 8 | 0.0 |
| 9 | 0.0 |
| 10 | 0.0 |
</details>

![](image/dc7ce37d10cbdcc6639e2220baaaec6250700c3ed030e65118e3c4526c1b6096.jpg)

<details>
<summary>line</summary>

| Time | Input |
| --- | --- |
| 0 | -2 |
| 1 | -1 |
| 2 | 0 |
| 3 | 0 |
| 4 | 0 |
| 5 | 0 |
| 6 | 0 |
| 7 | 0 |
| 8 | 0 |
| 9 | 0 |
| 10 | 0 |
</details>

![](image/10d14f4ab56ee5bb22313ec89ee7d0741b6b2e642dde6e1928fa6ad2c602e40b.jpg)

<details>
<summary>line</summary>

| Time | Input |
| --- | --- |
| 0 | -2 |
| 1 | -1 |
| 2 | 0 |
| 3 | 0 |
| 4 | 0 |
| 5 | 0 |
| 6 | 0 |
| 7 | 0 |
| 8 | 0 |
| 9 | 0 |
| 10 | 0 |
</details>

Figure 4.3 Responses of the closed-loop system in Example 4.4. The initial condition is $x^T(0) = \{1 - 1\}$ , and the parameter values are $\omega = 1$ and $\zeta = 0.707$ . The outputs obtained for $N = 5$ (dashed-dotted), $N = 10$ (dashed), and $N = 20$ (solid) are shown in (a), and the corresponding control signals are shown in (b), (c), and (d), respectively.
