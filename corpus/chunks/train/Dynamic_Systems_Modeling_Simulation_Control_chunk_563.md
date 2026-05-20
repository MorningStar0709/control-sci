# Ultimate-gain method

A simple P-controller is used in Fig. 10.22 and the closed-loop step response is obtained with increasing gain $K _ { P }$ until sustained oscillations are observed. Figure 10.25 shows the marginally stable closed-loop response that is achieved when gain $K _ { P }$ reaches the ultimate gain setting of $K _ { U } = 4 . 1 3 4$ . The ultimate period of the sustained oscillations is $P _ { U } = 1 2 9 ~ \mathrm { s }$ . Using the Ziegler–Nichols tuning rules for the ultimate-gain method summarized in Table 10.2, we obtain

$\mathrm { P r o p o r t i o n a l \ g a i n } { : } ~ K _ { P } = 0 . 6 K _ { U } = 2 . 4 8$

Integral gain: $K _ { I } = \frac { 1 . 2 K _ { U } } { P _ { U } } = 0 . 0 3 8 5$ 1.2KU PU

$\mathrm { D e r i v a t i v e \ g a i n } { \mathrm { : } } \quad K _ { D } = 0 . 0 7 5 K _ { U } P _ { U } = 4 0$

We see that these three PID gains produced by the ultimate-gain method are very similar to the starting gains derived from the reaction-curve method. Hence, the closed-loop response will be very similar to the solid line shown in Fig. 10.24.

This example shows that either Ziegler–Nichols method can be used to obtain a good starting point for the three PID gains, after which the control engineer can observe the closed-loop response and subsequently adjust the gains to improve the response. However, it should be emphasized that some systems (plants) will not exhibit an S-shaped reaction curve to a step input or sustained oscillations with a high-gain P-controller. Consequently, the Ziegler–Nichols tuning rules may not necessarily apply to a particular plant.

![](image/f2fe14667d7a9846e2bade252b2299710965d16719a240d8301448cf259c7a77.jpg)

<details>
<summary>line</summary>

| Time, s | Tank solution pH |
| --- | --- |
| 0 | 7.0 |
| 100 | 8.7 |
| 200 | 8.7 |
| 300 | 8.7 |
| 400 | 8.7 |
| 500 | 8.7 |
| 600 | 8.7 |
</details>

Figure 10.25 Closed-loop step response with ultimate gain $K _ { U }$ (Example 10.7).
