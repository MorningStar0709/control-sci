<details>
<summary>line</summary>

| ω in log scale | dB |
| --- | --- |
| 0 | 0 |
| bandwidth | -3 |
| ωb | -3 |
</details>

Figure 7–76 Plot of a closed-loop frequency response curve showing cutoff frequency $\omega _ { b }$ and bandwidth.

The specification of the bandwidth may be determined by the following factors:

1. The ability to reproduce the input signal.A large bandwidth corresponds to a small rise time,or fast response.Roughly speaking,we can say that the bandwidth is proportional to the speed of response. (For example, to decrease the rise time in the step response by a factor of 2, the bandwidth must be increased by approximately a factor of 2.)   
2. The necessary filtering characteristics for high-frequency noise.

For the system to follow arbitrary inputs accurately, it must have a large bandwidth. From the viewpoint of noise, however, the bandwidth should not be too large.Thus, there are conflicting requirements on the bandwidth, and a compromise is usually necessary for good design. Note that a system with large bandwidth requires high-performance components, so the cost of components usually increases with the bandwidth.

Cutoff Rate. The cutoff rate is the slope of the log-magnitude curve near the cutoff frequency.The cutoff rate indicates the ability of a system to distinguish the signal from noise.

It is noted that a closed-loop frequency response curve with a steep cutoff characteristic may have a large resonant peak magnitude, which implies that the system has a relatively small stability margin.
