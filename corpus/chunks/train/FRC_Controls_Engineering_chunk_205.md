# 7.7.4 Pole placement vs LQR

This example uses the following continuous second-order model for a CIM motor (a DC motor).

$$
\mathbf {A} = \left[ \begin{array}{c c} - \frac {b}{J} & \frac {K _ {t}}{J} \\ - \frac {K _ {e}}{L} & - \frac {R}{L} \end{array} \right] \quad \mathbf {B} = \left[ \begin{array}{c} 0 \\ \frac {1}{L} \end{array} \right] \quad \mathbf {C} = \left[ \begin{array}{c c} 1 & 0 \end{array} \right] \quad \mathbf {D} = \left[ \begin{array}{c} 0 \end{array} \right]
$$

Figure 7.9 shows the response using various discrete pole placements and using LQR with the following cost matrices.

$$
\mathbf {Q} = \left[ \begin{array}{c c} \frac {1}{2 0 ^ {2}} & 0 \\ 0 & 0 \end{array} \right] \quad \mathbf {R} = \left[ \frac {1}{1 2 ^ {2}} \right]
$$

With Bryson’s rule, this means an angular velocity tolerance of 20 rad/s, an infinite current tolerance (in other words, we don’t care what the current does), and a voltage tolerance of 12 V.

Notice with pole placement that as the current pole moves toward the origin, the control effort becomes more aggressive.

![](image/82d5727e2df0e230d84e804593fa0ffc21ab447e25431a6716d852a83753cc0a.jpg)

<details>
<summary>line</summary>

| Time (s) | Angular Velocity (rad/s) - Reference | Angular Velocity (rad/s) - Pole placement at (0.5+0j) and (0.1+0j) | Angular Velocity (rad/s) - Pole placement at (0.4+0j) and (0.1+0j) | Angular Velocity (rad/s) - LQR at (0.175+0.21j) and (0.175-0.21j) | Current (A) - Reference | Current (A) - Pole placement at (0.5+0j) and (0.1+0j) | Current (A) - Pole placement at (0.4+0j) and (0.1+0j) | Current (A) - LQR at (0.175+0.21j) and (0.175-0.21j) | Input (V) - Pole placement at (0.5+0j) and (0.1+0j) | Input (V) - Pole placement at (0.4+0j) and (0.1+0j) | Input (V) - LQR at (0.175+0.21j) and (0.175-0.21j) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 200 | 200 | 200 | 200 | 0 | 120 | 120 | 120 | 12 | 12 | 12 |
| 0.005 | 200 | 200 | 200 | 200 | 0 | 80 | 80 | 80 | 8 | 8 | 8 |
| 0.010 | 200 | 200 | 200 | 200 | 0 | 30 | 30 | 30 | 3 | 3 | 3 |
| 0.015 | 200 | 200 | 200 | 200 | 0 | 15 | 15 | 15 | 1 | 1 | 1 |
| 0.020 | 200 | 200 | 200 | 200 | 0 | 5 | 5 | 5 | 5 | 5 | 5 |
| 0.025 | 200 | 200 | 200 | 200 | 0 | 4 | 4 | 4 | 4 | 4 | 4 |
</details>

Figure 7.9: Second-order CIM motor response with pole placement and LQR
