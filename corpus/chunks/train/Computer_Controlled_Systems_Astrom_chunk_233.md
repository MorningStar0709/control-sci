These examples show that even if we take a discrete-system point of view by only considering what happens at the sampling instants, it is necessary to keep the time-varying nature of sampled systems in mind to make the correct assessment of the results. Particular care should be given to simulations used to assess the performance of the systems. To investigate the effect of the sampling period it is useful to consider cases in which disturbances are introduced both immediately before and immediately after the sampling instants. The differences can be quite noticeable, as is indicated by a comparison of Figs. 4.3 and 4.4. Based on the simulations performed we suggest that the sampling period be chosen as

$$\omega h = 0. 1 \text { to } 0. 6 \tag {4.17}$$

where $\omega$ is the desired natural frequency of the closed-loop system. Longer sampling periods can be used in those rare cases in which the sampling can be synchronized to the disturbances.

![](image/156cb9bd7ee75cdc4f3b05f6e3ecfb7f822388494e22ea292d8c52fda3168577.jpg)

<details>
<summary>line</summary>

| x | Output (Solid) | Output (Dashed) | Output (Dotted) |
| --- | --- | --- | --- |
| 0 | 1.0 | 1.5 | 2.0 |
| 1 | 1.8 | 2.2 | 2.8 |
| 2 | 1.5 | 2.5 | 3.0 |
| 3 | 1.0 | 2.0 | 2.5 |
| 4 | 0.5 | 1.0 | 1.5 |
| 5 | 0.2 | 0.5 | 0.8 |
| 6 | 0.1 | 0.2 | 0.4 |
| 7 | 0.05 | 0.1 | 0.2 |
| 8 | 0.02 | 0.05 | 0.1 |
| 9 | 0.01 | 0.02 | 0.05 |
| 10 | 0.0 | 0.0 | 0.0 |
</details>

![](image/10f413f42185ffcf3a63845651f0a2f0b566c4428dc814098f82472b3a23da6a.jpg)

<details>
<summary>line</summary>

| x | Input |
| --- | --- |
| 0 | 0 |
| 1 | -1 |
| 2 | -2 |
| 3 | -1 |
| 4 | 0 |
| 5 | 0 |
| 6 | 0 |
| 7 | 0 |
| 8 | 0 |
| 9 | 0 |
| 10 | 0 |
</details>

![](image/39c39610da0a4801764164991050a5efc46d2612908b785507bc09e8f9156a66.jpg)

<details>
<summary>line</summary>

| Time | Input |
| --- | --- |
| 0 | 0 |
| 1 | -2 |
| 2 | -2 |
| 3 | -1 |
| 4 | 0 |
| 5 | 0 |
| 6 | 0 |
| 7 | 0 |
| 8 | 0 |
| 9 | 0 |
| 10 | 0 |
</details>

![](image/53cb4be5d778c8732b74d0694c9145693e913ad6b949af349e8bfcf250e0fade.jpg)

<details>
<summary>line</summary>

| Time | Input |
| --- | --- |
| 0 | 0 |
| 1 | -2 |
| 2 | -1 |
| 3 | 0 |
| 4 | 0 |
| 5 | 0 |
| 6 | 0 |
| 7 | 0 |
| 8 | 0 |
| 9 | 0 |
| 10 | 0 |
</details>

Figure 4.4 Responses of the closed-loop system in Example 4.4. The initial condition is $x^T(0+) = [1 \quad 1]$ , and the parameter values are $\omega = 1$ and $\zeta = 0.707$ . The outputs obtained for $N = 5$ (dashed-dotted), $N = 10$ (dashed), and $N = 20$ (solid) are shown in (a), and the control signals are shown in (b), (c), and (d), respectively. The disturbance is immediately after the first sampling. Notice the significant difference compared to Fig. 4.3.
