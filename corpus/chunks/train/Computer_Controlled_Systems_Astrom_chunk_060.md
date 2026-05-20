# Example 1.4 Sampling creates new frequencies

Consider the systems for control of the disk drive arm discussed in Example 1.2. Assume that the frequency $\omega_0$ is 1 rad/s, let the sampling period be $h = 0.5 / \omega_0$ , and assume that there is a sinusoidal measurement noise with amplitude 0.1 and frequency 12 rad/s. Figure 1.10 shows interesting variables for the continuous-time system and the computer-controlled system. There is clearly a drastic difference between the systems. For the continuous-time system, the measurement noise has very little influence on the arm position. It does, however, create substantial control action with the frequency of the measurement noise. The high-frequency measurement noise is not noticeable in the control signal for the computer-controlled system, but there is also a substantial low-frequency component.

To understand what happens, we can consider Fig. 1.11, which shows the control signal and the measured signal on an expanded scale. The figure shows that there is a considerable variation of the measured signal over the sampling period and the low-frequency variation is obtained by sampling the high-frequency signal at a slow rate.

![](image/606e120bcd14c695e5b49ddd2e6dda3f2d52bafc011657501f528e5b7ea55bcc.jpg)

<details>
<summary>line</summary>

| Time | Measured output | Input |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 1 | 0.1 | 0.05 |
| 2 | -0.1 | -0.05 |
| 3 | 0.2 | -0.1 |
| 4 | -0.2 | -0.15 |
| 5 | 0.1 | -0.1 |
| 6 | -0.1 | -0.05 |
| 7 | 0.2 | 0.0 |
| 8 | -0.2 | 0.05 |
| 9 | 0.1 | 0.1 |
| 10 | -0.2 | 0.1 |
</details>

Figure 1.11 Simulation of the disk arm servo with computer control. The frequency $\omega_{0}$ is 1, the sampling period is h = 0.5, and there is a measurement noise $n = 0.1 \sin 12t$ .

We have thus made the striking observation that sampling creates signals with new frequencies. This is clearly a phenomenon that we must understand in order to deal with computer-controlled systems. At this stage we do not wish to go into the details of the theory; let it suffice to mention that sampling of a signal with frequency $\omega$ creates signal components with frequencies

$$\omega_ {\text { sampled }} = n \omega_ {s} \pm \omega \tag {1.6}$$

where $\omega_{s} = 2\pi / h$ is the sampling frequency, and $n$ is an arbitrary integer. Sampling thus creates new frequencies. This is further discussed in Sec. 7.4.

In the particular example we have $\omega_{s}=4\pi=12.57$ , and the measurement signal has the frequency 12 rad/s. In this case we find that sampling creates a signal component with the frequency 0.57 rad/s. The period of this signal is thus 11 s. This is the low-frequency component that is clearly visible in Fig. 1.11.

Example 1.4 illustrated that lower frequencies can be created by sampling. It follows from (1.6) that sampling also can give frequencies that are higher than the excitation frequency. This is illustrated in the following example.
