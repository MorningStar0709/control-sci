# Changing the Sampling Period

The sampling period in the nominal design was chosen such that

$$\omega_ {\mathrm{obs}} h = 0. 6$$

which is according to the upper limit of the rule of thumb. Figure 5.20 shows the responses when the sampling period is changed, h = 0.1 and 1. As for the double integrator in the previous section, the controller will respond faster after load disturbances when the sampling interval is decreased. A too-long sampling interval will increase the deviation after the load disturbance. Also, the aliasing effect is seen when there is measurement noise, because no antialiasing filter is used. The example shows that the rule of thumb for the choice of sampling interval gives a sensible result.

![](image/d9243c39348712787ad29dd79626078514c0868a5a22ae3fd37ef1afe1bf673e.jpg)

<details>
<summary>line</summary>

| Time | Output | Input |
| --- | --- | --- |
| 0 | 0 | 0 |
| 5 | 1 | 1 |
| 10 | 1 | 1 |
| 15 | 1 | 1 |
| 20 | 1 | 1 |
| 25 | 1 | 1 |
| 30 | 1 | 1 |
| 35 | 1 | 1 |
| 40 | 1 | 1 |
</details>

![](image/2e3467623ba50039bf422486668b0953f7c9507f30a18018e2e7784a84631fa2.jpg)

<details>
<summary>line</summary>

| Time | Output | Input |
| --- | --- | --- |
| 0 | 0 | 0 |
| 5 | 1 | 0.5 |
| 10 | 1 | 1 |
| 15 | 0.5 | 1.5 |
| 20 | 1 | 1.5 |
| 25 | 1 | 1.5 |
| 30 | 1 | 1.5 |
| 35 | 1 | 1.5 |
| 40 | 1 | 1.5 |
</details>

Figure 5.20 Response of the pole-placement design for the harmonic oscillator for sampling intervals (a) h = 0.1 and (b) h = 1.
