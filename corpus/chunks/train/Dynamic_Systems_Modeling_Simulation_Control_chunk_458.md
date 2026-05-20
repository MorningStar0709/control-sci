As a check, note that at time $t = 0 , y ( 0 ) = 0 . 0 0 2 3 - 0 . 0 0 1 8 - 0 . 0 0 0 5 = 0$ as expected (i.e., zero initial conditions). Figure 8.7 shows the 2-V step response computed using Eq. (8.60). Note that the slope of the response at time t = 0 is zero $( \mathrm { i . e . , j } ( 0 ) = 0 )$ as specified in the problem statement. The steady-state value is clearly $y ( \infty ) =$ 0.0023 m (or 2.3 mm), which is the residue $a _ { 1 }$ because the other three terms involve an exponential decay to zero at steady state. We can obtain the steady-state valve position by applying the final-value theorem to Eq. (8.53), which yields $2 0 0 , 0 0 0 / ( 5 0 0 \times 1 7 5 , 0 0 0 ) = 0 . 0 0 2 3$ . In Example 7.4 we computed the DC gain of the transfer function (i.e., evaluating G(s) with $s = 0 )$ to find the same steady-state response to the 2-V step input. The reader should note that the DC gain method is an application of the final-value theorem when the input is a constant.

Finally, the reader should note that the step response in Fig. 8.7 can be quickly sketched by using the methods presented in Chapter 7: determine the transient-response characteristics from the roots (poles) of the solenoid’s first-order transfer function $G _ { 1 } ( s ) ( \mathrm { i } . { \mathrm { e } } .$ ., compute time constant ??) and the spool valve’s second-order transfer function $G _ { 2 } ( s )$ (i.e., compute $\zeta$ and $\omega _ { n } )$ . From these values we can estimate settling time, percent overshoot, period of oscillation, and so on (see Table 7.4). The steady-state value of the step response is easily determined from the DC gain of the product of the two transfer functions $G _ { 1 } ( s )$ and $G _ { 2 } ( t )$ .

![](image/e46fb1740c8181faf3815ae6bc60b56b0955ee0b37157c62955e7cf73b00595a.jpg)

<details>
<summary>line</summary>

| Time, s | Spool-valve position, y(t), m (×10⁻³) |
| --- | --- |
| 0.000 | 0.000 |
| 0.005 | 1.500 |
| 0.010 | 2.500 |
| 0.015 | 2.300 |
| 0.020 | 2.250 |
| 0.025 | 2.300 |
| 0.030 | 2.300 |
| 0.035 | 2.300 |
| 0.040 | 2.300 |
</details>

Figure 8.7 Step response of spool valve (Example 8.13).
