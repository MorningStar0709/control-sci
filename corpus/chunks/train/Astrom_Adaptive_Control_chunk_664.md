Since only the process gain is unknown, we will estimate only the parameter b. In the simulation we will also assume that the gain varies sinusoidally between the values 0.1 and 1.9 with the period 400. In Fig. 11.8 we show a simulation of the system when the command signal is a square wave with period 50, there is measurement noise with the standard deviation 0.02, and the forgetting factor is $\lambda = 0.95$ . Notice that the gain variation is clearly noticeable in the shape of the control signal, which changes significantly over one step. Figure 11.8 shows that the estimated gain lags the true gain. The forgetting factor is $\lambda = 0.95$ , and the sampling period is h = 0.5. The time constant associated with the exponential forgetting is then $T_{f} = 10$ s, which is a crude estimate of the time lag in the estimator. Notice also that the lag is different for increasing and decreasing gains, a feature that indicates the nonlinear nature of the problem. The forgetting factor can be decreased to reduce the tracking lag. The estimates will then have more variation. To illustrate this, we simulate the same system as in Fig. 11.8 with different forgetting factors. The results are shown in Fig. 11.9. The figure shows that the forgetting factor $\lambda = 0.95$ is too large because the systematic tracking error is too large. The forgetting factor $\lambda = 0.1$ , on the other hand, is too small, and the systematic error is small, but the random component is large. In this particular case the value $\lambda = 0.7$ is a reasonable compromise. The reason for the low value of $\lambda$ is that the parameter variations are quite rapid.

![](image/60561a8da7c9c16440a276db7fc9e44b0b0e897cca9faf484d15118ca5af2332.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 0 | 0.0 |
| 200 | ~0.0 |
| 400 | ~0.0 |
| 600 | ~0.0 |
| 800 | ~0.0 |
| 1000 | ~0.0 |
</details>

![](image/d2ec7d4888b13968592aee686462623fc6c259c2c77813a63c36b6ac1ff1f4ec.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 0 | 0.0 |
| 200 | ~0.0 |
| 400 | ~0.0 |
| 600 | ~0.0 |
| 800 | ~0.0 |
| 1000 | ~0.0 |
</details>

![](image/3200ddaaaf0af029fc14f4e61fe5ff74a4bda05910d94a36b954a3cfff7e0efe.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 0 | 0.0 |
| 200 | -0.2 |
| 400 | 0.3 |
| 600 | -0.1 |
| 800 | 0.3 |
| 1000 | -0.1 |
</details>

Figure 11.9 Parameter tracking error $\bar{b} = h - \hat{b}$ for different forgetting factors: (a) $\lambda = 0.1$ ; (b) $\lambda = 0.7$ ; (c) $\lambda = 0.95$ .
