Specifications. It is desired that the closed-loop system has a response from the reference signal such that the dominating modes have a natural frequency $\omega_{m} = 0.5$ rad/s and a damping $\zeta_{m} = 0.7$ .

Choice of sampling interval. The desired model has a natural frequency $\omega_{m} = 0.5$ rad/s. Using the rule of thumb given by Eq. (4.17) gives h = 0.5 s as a reasonable choice for the sampling interval. This gives a Nyquist frequency of $\omega_{N} = \pi/h = 6$ rad/s.

In practice an antialiasing filter is necessary to avoid frequency folding of disturbances. In this first design the disturbances are disregarded and the design is done for the plant only.

![](image/820f7c87af994b1f259ad88d8527bf342bbf1389d455fa586b2ffad120683f10.jpg)

<details>
<summary>line</summary>

| x | Gain |
| --- | --- |
| 0.1 | 1.0 |
| 10 | 0.001 |
</details>

![](image/8621f13a95a8616e798fbb4df4eb9c54f4789a193d0b4cfc69cb9b31a4358d7c.jpg)

<details>
<summary>line</summary>

| Frequency, rad/s | Phase |
| --- | --- |
| 0.1 | -180 |
| 10 | -180 |
</details>

Figure 4.18 Bode plot of the flexible-robot-arm process.

Stata feedback design. It is assumed that all the states are measured. The system is of third order, which implies that three poles can be placed using the controller

$$u (k) = - L x (k) + L _ {c} u _ {c} (k) \tag {4.66}$$

Let the desired poles be specified by

$$\left(s ^ {2} + 2 \zeta_ {m} \omega_ {m} s + \omega_ {m} ^ {2}\right) (s + \alpha_ {1} \omega_ {m}) = 0 \tag {4.67}$$

This characteristic equation is transferred to sampled form with h = 0.5. The parameter $L_{c}$ is determined such that the steady-state gain from $u_{c}$ to y is unity, that is, no integrator is introduced in the controller. Figure 4.20 shows the behavior of the closed-loop system when the state-feedback controller (4.66) is used when $\alpha_{1}=2$ . The reference signal is a step at t=0 and the disturbance v is a pulse at t=25 of height -10 and a duration of 0.1 time unit.

![](image/4b9ce9d2b548d6b3a957c2a48b4908aef95e90ce8cc9b46cbc354f14f8609770.jpg)

<details>
<summary>line</summary>

| Time | Output |
| --- | --- |
| 0 | 0.0 |
| 5 | 0.15 |
| 10 | 0.05 |
| 15 | 0.12 |
| 20 | 0.06 |
| 25 | 0.11 |
| 30 | 0.07 |
| 35 | 0.13 |
| 40 | 0.08 |
| 45 | 0.12 |
| 50 | 0.09 |
| 55 | 0.11 |
| 60 | 0.08 |
| 65 | 0.10 |
| 70 | 0.09 |
| 75 | 0.10 |
</details>

Figure 4.19 Impulse response of the flexible-robot-arm process
