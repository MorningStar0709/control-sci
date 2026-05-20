<details>
<summary>line</summary>

| Point Type | X | Y |
| --- | --- | --- |
| Design point: K = 1780 | -50 | 0 |
| Lead controller pole-zero pair | -150 | 0 |
| Unstable | 0 | 0 |
</details>

Figure 11.54 Root locus for linearized maglev system with lead controller.

![](image/215fa6e467e0f001c2034539bdbdb8790e89894c6c7b884223a462f1ee056276.jpg)

<details>
<summary>line</summary>

| Time, s | Lead controller only | Lead + integral controller | Reference step input |
| --- | --- | --- | --- |
| 0.1 | 0.000 | 0.000 | 0.000 |
| 0.2 | 4.5 | 3.0 | 3.0 |
| 0.3 | 4.8 | 3.5 | 3.0 |
| 0.4 | 4.8 | 3.0 | 3.0 |
| 0.5 | 4.8 | 3.0 | 3.0 |
| 0.6 | 4.8 | 3.0 | 3.0 |
| 0.7 | 4.8 | 3.0 | 3.0 |
| 0.8 | 4.8 | 3.0 | 3.0 |
</details>

Figure 11.55 Closed-loop step responses of the linearized maglev system: lead controller and lead-plus-integral controller.

provides good damping as the step response reaches the 4.8-mm steady-state value in about 0.2 s after the step is applied. However, the steady-state ball position is 1.8 mm above the 3-mm reference position (note that positive z is upward; see Fig. 11.49). It is not surprising that the lead controller cannot provide zero steady-state error if we examine the closed-loop control system. Figure 11.52 shows that if the position tracking error goes to zero, then the lead controller will command zero change in source voltage $( \mathrm { i . e . , } \delta e _ { \mathrm { i n } } = 0 )$ and therefore the change in the coil current is also zero $( \mathrm { i } . \mathrm { e } . , \delta I = 0 )$ . Consequently, the maglev system is back to its original nominal operation, which causes the ball to levitate at $z ^ { * } = 0 \left( \mathrm { o r } , \right.$ , an air-gap distance of 0.024 m).

The clear solution to the steady-state tracking problem is to add an integrator to the control loop:

$$\text { Lead } + \text { integral controller: } \quad G _ {C} (s) = K \left(\frac {s + 4 0}{s + 1 6 0} + \frac {K _ {I}}{s}\right) \tag {11.80}$$
