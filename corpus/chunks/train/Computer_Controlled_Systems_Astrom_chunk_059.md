# Aliasing

One property of the time-varying nature of computer-controlled systems was illustrated in Fig. 1.4. We will now illustrate another property that has far-reaching consequences. Stable linear time-invariant systems have the property that the steady-state response to sinusoidal excitations is sinusoidal with the frequency of the excitation signal. It will be shown that computer-controlled systems behave in a much more complicated way because sampling will create signals with new frequencies. This can drastically deteriorate performance if proper precautions are not taken.

![](image/42259e1883ce6ce5c686e01fd0db5e448acb16dbe2f6fe4d9d524b851bfd8706.jpg)

<details>
<summary>line</summary>

| Time | Output | Measured output | Input |
| --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.0 |
| 10 | 0.0 | 0.0 | 0.0 |
| 20 | 0.0 | 0.0 | 0.0 |
</details>

![](image/2ae0051340e40b5dfdde7f49490d2a898a2f973564fa339ec69770c9436999d7.jpg)

<details>
<summary>line</summary>

| Time | Output | Measured output | Input |
| --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.0 |
| 5 | 0.15 | 0.15 | -0.05 |
| 10 | -0.1 | -0.1 | 0.05 |
| 15 | 0.15 | 0.15 | -0.05 |
| 20 | -0.1 | -0.1 | 0.05 |
| 25 | 0.15 | 0.15 | -0.05 |
</details>

Figure 1.10 Simulation of the disk arm servo with analog and computer control. The frequency $\omega_{0}$ is 1, the sampling period is h = 0.5, and there is a measurement noise $n = 0.1 \sin 12t$ . (a) Continuous-time system; (b) sampled-data system.
