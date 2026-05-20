# Integrator Windup

A controller with integral action combined with an actuator that becomes saturated can give some undesirable effects. If the control error is so large that the integrator saturates the actuator, the feedback path will be broken, because the actuator will remain saturated even if the process output changes. The integrator, being an unstable system, may then integrate up to a very large value. When the error is finally reduced, the integral may be so large that it takes considerable time until the integral assumes a normal value again. This effect is called integrator windup. The effect is illustrated in Fig. 8.9.

There are several ways to avoid integrator windup. One possibility is to stop updating the integral when the actuator is saturated. Another method is illustrated by the block diagram in Fig. 8.10(a). In this system an extra feedback path is provided by measuring the actuator output and forming an error signal $(e_s)$ as the difference between the actuator output $(u_c)$ and the controller output $(v)$ and feeding this error back to the integrator through the gain $1 / T_t$ . The error signal $e_s$ is zero when the actuator is not saturated. When the actuator is saturated the extra feedback path tries to make the error signal $e_s$ equal zero. This means that the integrator is reset, so that the controller output is at the saturation limit. The integrator is thus reset to an appropriate value with the time constant $T_t$ , which is called the tracking-time constant. The advantage with this scheme for antiwindup is that it can be applied to any actuator, that is, not only a saturated actuator but also an actuator with arbitrary characteristics, such as a dead zone or an hysteresis, as long as the actuator output is measured. If the actuator output is not measured, the actuator can be modeled and an

![](image/ecb7d9e6be2576ef2e2a206acf2e1d7a6a70ab46e850c43a605dab676802ad00.jpg)

<details>
<summary>line</summary>

| Time | Output | Input |
| --- | --- | --- |
| 0 | 0 | 0.1 |
| 20 | 2 | -0.1 |
| 40 | 1 | 0 |
| 60 | 1 | -0.1 |
| 80 | 1 | 0 |
</details>

Figure 8.9 Illustration of integrator windup. The dashed lines show the response with an ordinary PID-controller. The solid lines show the improvement with a controller having antiwindup.

![](image/553a2c22c109b0937823fdea3bf1e2d3aa47db6036e3dce3cda66ac3b69972f3.jpg)

<details>
<summary>flowchart</summary>
