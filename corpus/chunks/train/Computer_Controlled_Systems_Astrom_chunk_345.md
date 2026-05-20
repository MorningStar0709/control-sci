# Influence of Antialiasing Filter

Figure 5.18 indicates that a significant amount of measurement noise is injected into the system. A properly designed antialiasing filter can reduce this. The filter will, however, introduce extra dynamics into the system. The closed-loop system will be unstable when the nominal controller is used because of the phase lag of the antialiasing filter. The filter dynamics should thus be considered when designing the controller. This will be discussed in detail in Chapter 7. Bessel filters are commonly used as antialiasing filters. One of their nice properties is that their dynamics can be approximated with a time delay, which simplifies the design and reduces the order of the controller. A sixth-order Bessel filter is approximated as a delay of $\tau = 2.7 / \omega_B$ . The filter bandwidth is chosen as $\omega_B = 2\pi$ , which gives $\tau = 0.43$ . To incorporate the delay it is necessary to increase the order of the controller such that $\deg R = \deg S = \deg T = 5$ . Figure 5.21 shows the response with an antialiasing filter when the design is made by approximating the filter by a delay. The measurement noise, which is a discrete-time white-noise sequence with a sampling period of 0.01, starts at $t = 30$ . A comparison with Fig. 5.20 shows that the fluctuations of the control signal due to measurement noise are reduced substantially. The filter, however, will increase the deviation after the load disturbance because of the additional dynamics.

![](image/adfe1087f04bcc3f507a32afe825078f2a4e504a0c7d7b3c2a89653fd0fd1bae.jpg)

<details>
<summary>line</summary>

| Time | Output |
| --- | --- |
| 0 | 0 |
| 5 | 1 |
| 10 | 1 |
| 15 | 0.5 |
| 20 | 1 |
| 25 | 1 |
| 30 | 1 |
| 35 | 1 |
| 40 | 1 |
</details>

![](image/a95cb8b471ea22e3d36ea92a7aa960015c35d699ac80ba90fe266491f444afa9.jpg)

<details>
<summary>line</summary>

| Time | Input |
| --- | --- |
| 0 | 0 |
| 5 | 1 |
| 10 | 1 |
| 15 | 2 |
| 20 | 1 |
| 25 | 1 |
| 30 | 1 |
| 35 | 2 |
| 40 | 1 |
</details>

Figure 5.21 Response of pole-placement design when using an antialiasing filter. Output and input when the filter is approximated with a delay in the design.
