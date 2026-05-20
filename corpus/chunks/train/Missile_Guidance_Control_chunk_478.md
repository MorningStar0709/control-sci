# Current Aircraft Condition Initialization for Weapon Trajectory Integration.

Current aircraft conditions are used as inputs to the weapon delivery trajectory integration. This input is then adjusted to compensate for (1) data age, and (2) time delay between release command and actual release of the weapon. Then the data are predicted ahead 1.5 times the time between trajectory solutions to minimize bias of the reference solution during the time period it will be used. A coordinate transformation is required before doing the trajectory integration.

Weapon Trajectory Integration. The weapon trajectory integration computes the path of the bomb from release point to the burst altitude. This integration is accomplished in a reference coordinate system in which the X-axis is along the aircraft ground track, the Z-axis is up, and the Y -axis is such as to make a right-hand coordinate system. A recurrent third-order Runge–Kutta technique is the numerical integration algorithm used for the weapon trajectory integration. The weapon trajectory integration includes the effects of (1) weapon ballistics, (2) lateral and vertical offset and roll rate, (3) nonstandard atmosphere, (4) weapon separation effects, (5) measured and predicted wind structure, (6) Coriolis accelerations, and (7) gravitational variation. Furthermore, the results of the integration provide (a) horizontal bomb range components in the reference coordinate system, and (b) the partial derivatives of bomb range with respect to variation in flight parameters.

![](image/f32f6ee585e45f7641df36d2ebf52a09fde0a36f55343935d89e31b4d5440536.jpg)

<details>
<summary>line</summary>

| Mach number | Actual data | Curve fit |
| --- | --- | --- |
| 0.84 | 0.18 | 0.18 |
| 1.05 | 0.53 | 0.53 |
| 1.14 | 0.53 | 0.53 |
| 2.5 | 0.42 | 0.42 |
</details>

Fig. 5.27. Coefficient of drag versus Mach number for Mk 82.
