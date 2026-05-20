![](image/2453891fcb086c0849399659f5f5c631a0d7cf95660a1a6c738030f3f9f12343.jpg)

<details>
<summary>line</summary>

| ω | Exact curve | G(jω) |
| --- | --- | --- |
| 0.2 | ~35 | ~15 |
| 0.4 | ~25 | ~10 |
| 0.6 | ~20 | ~5 |
| 0.8 | ~15 | ~0 |
| 1.0 | ~10 | ~-5 |
| 2.0 | ~0 | ~-10 |
| 4.0 | ~-10 | ~-15 |
| 6.0 | ~-15 | ~-20 |
| 8.0 | ~-20 | ~-25 |
| 10.0 | ~-25 | ~-30 |
</details>

![](image/b845b9c50c1ccef6372c8120ccf48afd686f84c1a067aaad5e7b0e644b0a58f1.jpg)

<details>
<summary>line</summary>

| ω | φ (Curve ①) | φ (Curve ②) | φ (Curve ③) | φ (Curve ④) | φ (Curve ⑤) |
| --- | --- | --- | --- | --- | --- |
| 0.2 | ~0° | ~0° | ~0° | ~0° | ~-180° |
| 0.4 | ~0° | ~0° | ~0° | ~0° | ~-180° |
| 0.6 | ~0° | ~0° | ~0° | ~0° | ~-180° |
| 0.8 | ~0° | ~0° | ~0° | ~0° | ~-180° |
| 1.0 | ~0° | ~0° | ~0° | ~0° | ~-180° |
| 2.0 | ~-90° | ~-90° | ~-90° | ~-90° | ~-270° |
| 4.0 | ~-180° | ~-180° | ~-180° | ~-180° | ~-270° |
| 6.0 | ~-270° | ~-270° | ~-270° | ~-270° | ~-270° |
| 8.0 | ~-270° | ~-270° | ~-270° | ~-270° | ~-270° |
| 10.0 | ~-270° | ~-270° | ~-270° | ~-270° | ~-270° |
</details>

Figure 7–11 Bode diagram of the system considered in Example 7–3.

Minimum-Phase Systems and Nonminimum-Phase Systems. Transfer functions having neither poles nor zeros in the right-half s plane are minimum-phase transfer functions, whereas those having poles and/or zeros in the right-half s plane are nonminimum-phase transfer functions. Systems with minimum-phase transfer functions are called minimum-phase systems, whereas those with nonminimum-phase transfer functions are called nonminimum-phase systems.

For systems with the same magnitude characteristic, the range in phase angle of the minimum-phase transfer function is minimum among all such systems, while the range in phase angle of any nonminimum-phase transfer function is greater than this minimum.

It is noted that for a minimum-phase system, the transfer function can be uniquely determined from the magnitude curve alone. For a nonminimum-phase system, this is not the case. Multiplying any transfer function by all-pass filters does not alter the magnitude curve, but the phase curve is changed.

Consider as an example the two systems whose sinusoidal transfer functions are, respectively,

$$G _ {1} (j \omega) = \frac {1 + j \omega T}{1 + j \omega T _ {1}}, \quad G _ {2} (j \omega) = \frac {1 - j \omega T}{1 + j \omega T _ {1}}, \quad 0 < T < T _ {1}$$
