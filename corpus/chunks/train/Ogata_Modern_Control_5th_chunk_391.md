| Real Axis | Imag Axis | Type |
| --- | --- | --- |
| -10 | 0 | Closed-loop poles |
| -8 | 7 | Closed-loop poles |
| -6 | -7 | Closed-loop poles |
| -4 | 3 | Closed-loop poles |
| -2 | -3 | Closed-loop poles |
| 0 | 0 | Closed-loop poles |
| 0 | 2 | Closed-loop poles |
| 0 | -2 | Closed-loop poles |
| 0 | -4 | Closed-loop poles |
| 0 | 0 | Closed-loop poles |
| 0 | 2 | Closed-loop poles |
| 0 | -2 | Closed-loop poles |
| 0 | -4 | Closed-loop poles |
| 0 | 0 | Closed-loop poles |
| 0 | 2 | Closed-loop poles |
| 0 | -2 | Closed-loop poles |
| 5 | 0 | Closed-loop poles |
| 5 | 2 | Closed-loop poles |
| 5 | -2 | Closed-loop poles |
| 5 | -4 | Closed-loop poles |
| 5 | 0 | Closed-loop poles |
| 5 | 2 | Closed-loop poles |
| 5 | -2 | Closed-loop poles |
| 5 | -4 | Closed-loop poles |
| 10 | 0 | Closed-loop poles |
| 10 | 2 | Closed-loop poles |
| 10 | -2 | Closed-loop poles |
| 10 | -4 | Closed-loop poles |
| 10 | 0 | Closed-loop poles |
| 10 | 2 | Closed-loop poles |
| 10 | -2 | Closed-loop poles |
| 10 | -4 | Closed-loop poles |
| 15 | 0 | Closed-loop poles |
| 15 | 2 | Closed-loop poles |
| 15 | -2 | Closed-loop poles |
| 15 | -4 | Closed-loop poles |
| 15 | 0 | Closed-loop poles |
| 15 | 2 | Closed-loop poles |
| 15 | -2 | Closed-loop poles |
| 15 | -4 | Closed-loop poles |
</details>

Figure 6–96 Root-locus plot of the compensated system.

are as follows:

$$s = - 2. 0 0 0 0 \pm j 3. 4 6 4 1s = - 7. 5 2 2 4 \pm j 6. 5 3 2 6s = - 0. 8 8 6 8$$

Now that the compensator has been designed, we shall examine the transient-response characteristics with MATLAB. The closed-loop transfer function is given by

$$\frac {C (s)}{R (s)} = \frac {8 8 . 0 2 2 7 (s + 2) ^ {2} (s + 4)}{(s + 9 . 9 1 5 8) ^ {2} s (s ^ {2} + 0 . 1 s + 4) + 8 8 . 0 2 2 7 (s + 2) ^ {2} (s + 4)}$$

Figures 6–97(a) and (b) show the plots of the unit-step response and unit-ramp response of the compensated system. These response curves show that the designed system is acceptable.

![](image/35739f8de7d6098401a8b1052f34ac0a64c99cb36b9146b9b1ed15928e005ba6.jpg)

<details>
<summary>line</summary>

| t Sec | Output |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 1.2 |
| 1.0 | 0.8 |
| 1.5 | 0.85 |
| 2.0 | 0.95 |
| 2.5 | 0.97 |
| 3.0 | 0.98 |
| 3.5 | 0.99 |
| 4.0 | 0.995 |
| 4.5 | 0.998 |
| 5.0 | 1.0 |
</details>

![](image/fb56df0c20c9bd27bd481484982f8a388dd1feaf01f71e9adcd12c267c39304c.jpg)

<details>
<summary>line</summary>

| t Sec | Input and Output |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 5 | 5 |
| 6 | 6 |
</details>

Figure 6–97   
(a) Unit-step response of the compensated system; (b) unit-ramp response of the compensated system.
