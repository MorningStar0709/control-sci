# Theorem 10.2.1 — Pose exponential.

$$
^ G \left[ \begin{array}{c} \Delta x \\ \Delta y \\ \Delta \theta \end{array} \right] = \left[ \begin{array}{c c c} \cos \theta & - \sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1 \end{array} \right] ^ {R} \left[ \begin{array}{c c c} \frac {\sin \Delta \theta}{\Delta \theta} & \frac {\cos \Delta \theta - 1}{\Delta \theta} & 0 \\ \frac {1 - \cos \Delta \theta}{\Delta \theta} & \frac {\sin \Delta \theta}{\Delta \theta} & 0 \\ 0 & 0 & 1 \end{array} \right] ^ {R} \left[ \begin{array}{c} \Delta x \\ \Delta y \\ \Delta \theta \end{array} \right] (1 0. 3)
$$

where G denotes global coordinate frame and R denotes robot’s coordinate frame.

For sufficiently small $\Delta \theta \colon$

$$\frac {\sin \Delta \theta}{\Delta \theta} = 1 - \frac {\Delta \theta^ {2}}{6} \quad \frac {\cos \Delta \theta - 1}{\Delta \theta} = - \frac {\Delta \theta}{2} \quad \frac {1 - \cos \Delta \theta}{\Delta \theta} = \frac {\Delta \theta}{2} \tag {10.4}$$

$\Delta x$ change in pose’s x $\Delta y$ change in pose’s y

$\Delta \theta$ change in pose’s θ θ starting angle in global coordinate frame

This change in pose can be added directly to the previous pose estimate to update it.

Figures 10.1 through 10.4 show the pose estimation errors of forward Euler odometry and pose exponential odometry for a feedforward S-curve trajectory (dt = 20 ms).

The highest errors for the 9.0 m by 5.0 m trajectory are 3.145 cm in x, 1.075 cm in y, and −0.757 deg in heading. The difference would be even more noticeable for paths with higher curvatures and longer durations. The error returns to near zero in this case because the curvature is symmetric, so the second half cancels the error accrued in the first half.

![](image/141379e66463f074e448fcb4a697a60659feab788a0ad31f2aaf965d39ee9398.jpg)

<details>
<summary>line</summary>

| X position (m) | Y position (m) |
| --- | --- |
| 1.0 | 13.0 |
| 2.0 | 13.5 |
| 4.0 | 14.5 |
| 6.0 | 15.5 |
| 8.0 | 16.5 |
| 10.0 | 17.5 |
</details>

Figure 10.1: Pose estimation comparison (y vs x)

![](image/c4c27740a31a7990dfae05cd08891710264ab1f3ecd3f7f555faf3b46a02f89c.jpg)

<details>
<summary>line</summary>

| Time (s) | Forward Euler | Pose exponential |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 1.0 | 3.0 | 0.0 |
| 2.0 | 3.0 | 0.0 |
| 3.0 | 3.0 | 0.0 |
| 4.0 | 0.0 | 0.0 |
</details>

Figure 10.2: Pose estimation comparison (x error vs time)

Using a smaller update period somewhat mitigates the forward Euler pose estimation error. However, there are bigger sources of error like turning scrub on skid steer robots that should be dealt with before odometry numerical accuracy.
