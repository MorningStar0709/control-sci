# Example 6.11

A system has the open loop transfer function (CP H(s)):

$$G (s) = \frac {3 . 9 \times 1 0 ^ {4}}{(s + 1) (s + 2 2) (s + 1 0 0)}$$

Use the Bode magnitude and phase plots to check the closed loop stability.

Drawing the Bode plots,

![](image/340ae3727722a937635559b3d24f7ff0935c1bd5d2b6ff6bf3661df40e239cdd.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 20 |
| 10 | 22 |
| 100 | -40 |
| 1000 | -60 |
</details>

We rst identify the point where the BAMP crosses 0dB (magnitude = 1), then we nd the phase angle by reading the phase plot at the same frequency (about 10.5 rad/sec). This is illustrated graphically by a vertical line dropping down from the 0dB axis to the phase plot. Reading that value we get a phase angle of about 120◦. This is well short of $1 8 0 ^ { \circ }$ so the system is stable.

Another way to evaluate stability is to look at where the phase curve crosses $1 8 0 ^ { \circ }$ and evaluate gain. In this case we nd that the phase curve crosses $1 8 0 ^ { \circ }$ at about $\omega = 6 0$ . Going straight up from the phase to the magnitude curve, we nd the magnitude at $\omega = 6 0$ is about −16dB, also indicating a stable system.
