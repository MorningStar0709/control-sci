The time constant for this first-order I/O equation is $\tau = L _ { 0 } / R$ . Because resistance is fixed at 3 Ω, the time constant ?? will increase at a quadratic rate with N. Hence, a strong electromagnet (large N) will result in a large time constant and consequently a slow current response. The slow current response slows down the buildup of electromagnetic force, which in turn slows down the response of the armature–valve mass. The back-emf coefficient $K = d L / d x$ also slows down the current response of the solenoid. Equation (11.14) shows that dL∕dx is proportional to inductance $L _ { 0 }$ , and therefore stronger electromagnets enhance the back-emf effect. Figure 11.21 displays the solenoid coil current response for designs with $N = 6 0 , 8 0 .$ , and 100. All three cases show a “dip” in the current response before reaching the steady-state value, which is due to the back-emf voltage induced by the high velocity of the armature during the out-stroke phase. However, the solenoid with N = 60 shows the fastest current response to the step voltage input, and therefore this solenoid design reaches its steady-state electromagnetic force sooner than any other design. A large electromagnetic force is important during the initial out-stroke phase because it is important to accelerate the mass. However, the magnitude of the steady-state electromagnetic force is not important as it ultimately is balanced by the return spring when x = 2 mm.

Figures 11.18–11.20 indicate that the best solenoid design has about 60 coil turns. Several more Simulink simulations were run, where N varied from 52 to 64 turns in increments of 2, and it was found that $N = 5 8$ provided the fastest valve response. Table 11.3 summarizes the characteristics and performance metrics of the best solenoid design.

![](image/4b3cde69b20d40b359ac6a65a8d945c6a243c4f717f443e8cb99dc11f6e3b028.jpg)

<details>
<summary>line</summary>

| Time, s | N = 60 | N = 80 | N = 100 |
| --- | --- | --- | --- |
| 0.00 | 0.0 | 0.0 | 0.0 |
| 0.02 | 4.0 | 3.8 | 3.5 |
| 0.04 | 4.0 | 3.9 | 3.9 |
| 0.06 | 4.0 | 3.95 | 3.95 |
| 0.08 | 4.0 | 3.95 | 3.95 |
| 0.10 | 4.0 | 3.95 | 3.95 |
</details>

Figure 11.21 Solenoid current I(t) for N = 60, 80, and 100 turns.

Table 11.3 Optimal Solenoid Design Characteristics

<table><tr><td>Solenoid Characteristic</td><td>Value</td></tr><tr><td>Number of turns,  $N$ </td><td>58</td></tr><tr><td>Initial inductance,  $L_0$ </td><td>0.0066 H</td></tr><tr><td>Force/back-emf constant,  $K$ </td><td>1.128 N/A $^2$ </td></tr><tr><td>Return spring constant,  $k$ </td><td>3510.4 N/m</td></tr><tr><td>Settling time,  $t_S$ </td><td>0.02 s</td></tr><tr><td>Percent overshoot</td><td>3.2%</td></tr></table>
