# Flight Control

The dynamics of an airplane change significantly with speed, altitude, angle of attack, and so on. Control systems such as autopilots and stability augmentation systems were used early. These systems were based on linear feedback with constant coefficients. This worked well when speeds and altitudes were low, but difficulties were encountered with increasing speed and altitude. The problems became very pronounced at supersonic flight. Flight control was one of the strong driving forces for the early development of adaptive control. The following example from Ackermann (1983) illustrates the variations in dynamics that can be encountered. The variations can be even larger for aircraft with larger variations in flight regimes.

![](image/8b30f8784e0eae0704f0d915d54e377d1b90710fb7bba1e7dfbacbbcade56eda.jpg)

<details>
<summary>line</summary>

| Time | q = 0.5 | q = 0.9 | q = 1.1 | q = 2 |
| --- | --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 5 | ~1.0 | ~1.0 | ~1.0 | ~1.0 |
| 10 | ~1.0 | ~1.0 | ~1.0 | ~1.0 |
| 15 | ~0.7 | ~1.0 | ~1.0 | ~1.0 |
| 20 | ~1.0 | ~1.0 | ~1.0 | ~1.0 |
</details>

![](image/e57c281c19d4557d374a732afe051ecf40439f9308d957a70416970ab1a6ecde.jpg)

<details>
<summary>line</summary>

| Time | q = 0.9 | q = 0.5 | q = 1.1 | q = 2 |
| --- | --- | --- | --- | --- |
| 0 | 0.5 | 0.5 | 0.5 | 0.5 |
| 5 | 1.7 | 1.5 | 1.0 | 0.8 |
| 10 | 0.6 | 0.6 | 1.0 | 0.6 |
| 15 | 1.0 | 1.0 | 1.0 | 0.8 |
| 20 | 1.1 | 1.1 | 1.0 | 0.9 |
</details>

Figure 1.11 Change in reference value for different flows for the system in Example 1.5. (a) Output c and reference $c_{r}$ concentration, (b) control signal.
