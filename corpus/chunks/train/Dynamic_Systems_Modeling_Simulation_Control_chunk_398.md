# Example 7.11

Figure 7.25 shows the measured step response of a solenoid actuator–valve system. This response has been experimentally obtained by measuring the valve displacement that results from a 38-mA current step input applied at t = 1 s [1]. Note that the valve response in Fig. 7.25 displays a very small amount of random “noise” or “chatter” because of imprecise measurements in the experimental setting. If possible, develop an approximate actuator–valve model from the experimental data.

![](image/01c75a4a146a7177f02dbc9da8022762d44b26f68d2c62b72e5f20f49ef6bbfa.jpg)

<details>
<summary>line</summary>

| Time, s | Valve position, y(t), mm |
| --- | --- |
| 0.0 | 0.0 |
| 1.0 | 0.0 |
| 1.5 | 0.35 |
| 2.0 | 0.41 |
| 2.5 | 0.43 |
| 3.0 | 0.44 |
| 3.5 | 0.44 |
| 4.0 | 0.44 |
| 4.5 | 0.44 |
| 5.0 | 0.44 |
| 5.5 | 0.44 |
| 6.0 | 0.44 |
</details>

Figure 7.25 Measured step response of an actuator–valve system (Example 7.11).

Note that the measured step response approximates an exponential rise to a constant steady-state displacement. Because the step response does not exhibit any overshoot, we can model the I/O relationship between current (input) and valve position (output) with a simple first-order linear ODE

$$\tau \dot {y} + y = a u (t)$$

where y is the valve position (mm), and u(t) is the current input (mA). Figure 7.25 shows that the steady-state position is ∼0.44 mm for a step input $u = 3 8 \mathrm { m A }$ , and therefore coefficient $a = 0 . 4 4 / 3 8 = 0 . 0 1 1 6 .$ . Figure 7.25 also shows that the valve position reaches its steady-state value with settling time $t _ { S } = 1 . 2 \ : \mathrm { s }$ , and therefore the time constant of the approximate first-order model is $\tau = t _ { S } / 4 = 0 . 3 \mathrm { s }$ . Using these numerical values, the approximate first-order model of the actuator–valve system becomes

$$0. 3 \dot {y} + y = 0. 0 1 1 6 u (t)$$

or, the first-order transfer function is

$$G (s) = \frac {0 . 0 1 1 6}{0 . 3 s + 1}$$
