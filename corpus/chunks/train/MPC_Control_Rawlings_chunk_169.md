# Exercise 1.45: Time-varying Kalman filter

Derive formulas for the conditional densities of $x ( k ) | { \bf y } ( k - 1 )$ ) and $x ( k ) | { \bf y } ( k )$ for the time-varying linear system

$$x (k + 1) = A (k) x (k) + G (k) w (k)\mathcal {Y} (k) = C (k) x (k) + \nu (k)$$

in which the initial state, state noise and measurement noise are independently distributed as

$$x (0) \sim N (\overline {{x}} _ {0}, Q _ {0}) \qquad w (k) \sim N (0, Q) \qquad v (k) \sim N (0, R)$$
