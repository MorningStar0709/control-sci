4. Since the lag compensator tends to integrate the input signal, it acts approximately as a proportional-plus-integral controller. Because of this, a lag-compensated system tends to become less stable. To avoid this undesirable feature, the time constant T should be made sufficiently larger than the largest time constant of the system.

5. Conditional stability may occur when a system having saturation or limiting is compensated by use of a lag compensator.When the saturation or limiting takes place in the system, it reduces the effective loop gain. Then the system becomes less stable and unstable operation may even result, as shown in Figure 7–108. To avoid this, the system must be designed so that the effect of lag compensation becomes significant only when the amplitude of the input to the saturating element is small. (This can be done by means of minor feedback-loop compensation.)

![](image/80f48076db17d1154fccd1bc2d63b03001c508434e03bc8a7cf7d7f02cdd4732.jpg)

<details>
<summary>line</summary>

| ω in rad/sec | Large gain (dB) | Small gain (dB) |
| --- | --- | --- |
| 0.7 | 30 | -180 |
| 1 | 20 | -180 |
| 2 | 10 | -180 |
| 4 | 0 | -180 |
| 6 | -10 | -180 |
| 8 | -20 | -180 |
| 10 | -30 | -180 |
| 20 | -40 | -180 |
</details>

Figure 7–108 Bode diagram of a conditionally stable system.
