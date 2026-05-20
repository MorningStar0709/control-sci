# 15.1 1-DOF motion profiles

Trapezoid profiles (figure 15.1) and S-curve profiles (figure 15.2) are the most commonly used motion profiles in FRC for point-to-point movements with one degree of freedom (1 DOF). These profiles accelerate the system to a maximum velocity from rest, then decelerate it later such that the final acceleration velocity, are zero at the moment the system arrives at the desired location.

These profiles are given their names based on the shape of their velocity trajectory. The trapezoid profile has a velocity trajectory shaped like a trapezoid and the S-curve profile has a velocity trajectory shaped like an S-curve.

In the context of a point-to-point move, a full S-curve consists of seven distinct phases of motion. Phase I starts moving the system from rest at a linearly increasing acceleration until it reaches the maximum acceleration. In phase II, the profile accelerates at this maximum acceleration rate until it must start decreasing as it approaches the maximum velocity. This occurs in phase III when the acceleration linearly decreases until it reaches zero. In phase IV, the velocity is constant until deceleration begins, at which point the profiles decelerates in a manner symmetric to phases I, II and III.

![](image/2cda5f1cf4d2554d48f810de1e54b7471e85b8d55ffd4762a3f1ead1cce5006b.jpg)

<details>
<summary>line</summary>

| Time (s) | Position (m) | Velocity (m/s) | Acceleration (m/s²) |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 2.5 |
| 2 | 10 | 6 | 2.5 |
| 4 | 20 | 6 | 0 |
| 6 | 30 | 6 | 0 |
| 8 | 40 | 0 | -2.5 |
| 9 | 45 | 0 | 0 |
</details>

Figure 15.1: Trapezoid profile

![](image/d34c694377fbb977c783d9aa38680631e391c31d70bce2ace083dd22a099498e.jpg)

<details>
<summary>line</summary>

| Time (s) | Position (m) | Velocity (m/s) | Acceleration (m/s²) |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 2 | 10 | 6 | 2.5 |
| 4 | 20 | 6 | 0 |
| 6 | 30 | 6 | 0 |
| 8 | 40 | 6 | -2.5 |
| 10 | 45 | 0 | 0 |
</details>

Figure 15.2: S-curve profile
