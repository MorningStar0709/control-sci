# 2.9 Selection of Sampling Rate

Proper selection of the sampling rate is a very important issue in computer-controlled systems. Too long a sampling period will make it impossible to reconstruct the continuous-time signal. Too short a sampling period will increase the load on the computer. The problem of sample-rate selection was touched in Sec. 1.3. The choice of the sampling period strongly depends on the purpose of the system. We will return to this question many times in the book. This section only relates the sampling-rate selection to the poles of the open-loop continuous-time system.

It is useful to characterize the sampling period with a variable that is dimension-free and that has a good physical interpretation. For oscillatory systems, it is natural to normalize with respect to the period of oscillation; for nonoscillatory systems, the rise time is a natural normalization factor.

We now introduce $N_{r}$ as the number of sampling periods per rise time,

$$N _ {r} = \frac {T _ {r}}{h}$$

where $T_{r}$ is the rise time. For first-order systems, the rise time is equal to the time constant. It is then reasonable to choose $N_{r}$ between 4 and 10. For a second-order system with damping $\zeta$ and natural frequency $\omega_{0}$ , rise time is given by

$$T _ {r} = \omega_ {0} ^ {- 1} e ^ {\varphi / \tan \varphi}$$

where $\zeta = \cos \varphi$ . For a damping around $\zeta = 0.7$ , this gives

$$\omega_ {0} h \approx 0. 2 - 0. 6$$

where $\omega_0$ is in radians per second.

Figures 2.7 and 2.9 illustrate the choice of the sampling interval for different signals. It is thus reasonable to choose the sampling period so that

$$N _ {r} = \frac {T _ {r}}{h} \approx 4 \text { to } 1 0$$

![](image/afbbd86183b3a60b38424f158ea182d3c0d427f245e2d448096cc87600540e18.jpg)

<details>
<summary>scatter</summary>

| x | y |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 2 | 1 |
| 3 | 0.5 |
| 4 | -0.8 |
| 5 | -1 |
| 6 | -0.5 |
| 7 | 0.8 |
</details>

![](image/97a197b71072f2b1875beaa562ce53e129f84568d128ec6e5307460b88aca8b0.jpg)

<details>
<summary>scatter</summary>

| x | y |
| --- | --- |
| 0 | 0 |
| 1 | 0.5 |
| 2 | 0.8 |
| 3 | 0.9 |
| 4 | 0.95 |
| 5 | 0.98 |
| 6 | 1.0 |
</details>

![](image/ec8cd35c19cb9ee63331afb7cdbc2e43fa6868cf8938f892a6722645ef0083b1.jpg)

<details>
<summary>scatter</summary>

| x | y |
| --- | --- |
| 0.0 | 0.0 |
| 1.0 | 0.8 |
| 2.0 | 0.9 |
| 3.0 | 0.6 |
| 4.0 | 0.2 |
| 5.0 | -0.8 |
| 6.0 | -0.9 |
| 7.0 | -0.5 |
| 8.0 | 0.1 |
| 9.0 | 0.7 |
| 10.0 | 1.0 |
</details>
