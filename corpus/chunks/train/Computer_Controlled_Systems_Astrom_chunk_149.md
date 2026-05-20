# Example 2.19 Pole-zero variation with sampling interval

Consider the system

$$G (s) = \frac {1}{(s + 1) (s ^ {2} + s + 1)} \tag {2.38}$$

Figure 2.10 shows the step response of the system. Assume that the system is sampled with period h. Figure 2.11 shows how the poles and zeros of the sampled-data system vary with the sampling period. Sampling intervals close to zero give three poles close to 1. Further, the continuous time system has a pole excess of 3. This implies that the zeros for short sampling intervals are close to the roots of

$$z ^ {2} + 4 z + 1 = 0$$

See Table 2.4. The poles and zeros approach the origin when the sampling interval is increased. The sampled-data system has a stable inverse if h > 2.24. The rules of thumb for the choice of the sampling interval give that a reasonable choice is h = 0.5. Compare with Figure 2.10.

![](image/9ce43cc4d54d9b7699ec2094a2356ad291a627ff9c6b0d3616927f0bc646bd13.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 0 | 0 |
| 5 | 1 |
| 10 | 1 |
| 15 | 1 |
</details>

Figure 2.10 Step response of the system (2.38).
