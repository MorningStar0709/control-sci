![](image/6a120665bda64fd609c4b558a5adf28df1cc1e2f378b85e047339d5ff8bce94e.jpg)

<details>
<summary>line</summary>

| Time, s | K_P = 0.2 V/m | K_P = 1 V/m | K_P = 5 V/m |
| --- | --- | --- | --- |
| 0 | 0.0000 | 0.0000 | 0.0000 |
| 1 | 0.0200 | 0.1850 | 0.1700 |
| 2 | 0.0600 | 0.1650 | 0.1600 |
| 3 | 0.1200 | 0.1450 | 0.1350 |
| 4 | 0.1450 | 0.1350 | 0.1250 |
| 5 | 0.1450 | 0.1250 | 0.1150 |
| 6 | 0.1350 | 0.1150 | 0.1050 |
| 7 | 0.1250 | 0.1050 | 0.0950 |
| 8 | 0.1150 | 0.0950 | 0.0850 |
| 9 | 0.1050 | 0.0850 | 0.0750 |
| 10 | 0.0950 | 0.0750 | 0.0650 |
| 11 | 0.1250 | 0.1150 | 0.1050 |
| 12 | 0.1350 | 0.1250 | 0.1150 |
| 13 | 0.1450 | 0.1350 | 0.1250 |
| 14 | 0.1350 | 0.1250 | 0.1150 |
| 15 | 0.1250 | 0.1150 | 0.1050 |
| 16 | 0.1150 | 0.1050 | 0.0950 |
| 17 | 0.1050 | 0.0950 | 0.0850 |
| 18 | 0.1250 | 0.1150 | 0.1050 |
| 19 | 0.1350 | 0.1250 | 0.1150 |
| 20 | 0.1450 | 0.1350 | 0.1250 |
| 21 | 0.1350 | 0.1250 | 0.1150 |
| 22 | 0.1250 | 0.1150 | 0.1050 |
| 23 | 0.1150 | 0.1050 | 0.0950 |
| 24 | 0.1250 | 0.1150 | 0.1050 |
| 25 | 0.1350 | 0.1250 | 0.1150 |
| 26 | 0.1450 | 0.1350 | 0.1250 |
| 27 | 0.1350 | 0.1250 | 0.1150 |
| 28 | 0.1250 | 0.1150 | 0.1050 |
| 29 | 0.1150 | 0.1050 | 0.0950 |
| 30 | 0.125 | 0.115 | 0.12 |
</details>

Figure 10.19 Closed-loop position response with P-controller (Example 10.6).

$$\text { First - order term: } \quad 0. 3 + 2 K _ {D} = 2 \zeta \omega_ {n}\text { Zeroth - order term: } \quad 2 K _ {P} = \omega_ {n} ^ {2}$$

Therefore, the freedom to adjust the PD controller gains $K _ { P }$ and $K _ { D }$ allows for independent manipulation of both the damping ratio $\zeta$ and undamped natural frequency $\omega _ { n }$ . Figure 10.20 shows the closed-loop step response using a PD controller with gains $K _ { P } = 1 6 \mathrm { V } / \mathrm { m }$ and $K _ { D } = 4 \mathrm { V } { - } \mathrm { s } / \mathrm { m }$ . Note that the transient response using PD control has greatly improved: the overshoot is relative small, and the response reaches the desired steady-state position in less than 1 s.

![](image/82d821d70d05974907fda3d5f467eca31d9c72ead5425924f05f427d8ab17d3b.jpg)

<details>
<summary>line</summary>

| Time, s | Position, x(t), m |
| --- | --- |
| 0.0 | 0.000 |
| 0.5 | 0.120 |
| 1.0 | 0.100 |
| 1.5 | 0.100 |
</details>

Figure 10.20 Closed-loop position response with PD controller (Example 10.6).

In summary, this example has demonstrated how adding a derivative control signal can improve the transient response of the closed-loop system by increasing the system damping. This particular problem did not require an integral control signal for improving the steady-state response due to the nature of the plant system dynamics.
