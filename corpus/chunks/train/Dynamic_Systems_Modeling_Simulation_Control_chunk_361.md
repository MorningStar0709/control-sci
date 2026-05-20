# Example 7.5

Consider again the solenoid actuator dynamics from Example 7.4, as shown in Fig. 7.4. Sketch the step response of the first-order solenoid model for a step voltage input, $e _ { \mathrm { i n } } ( t ) = 2 \ : \mathrm { V }$ . The system is initially at rest at time $t = 0$ , or $\cdot f ( 0 ) = 0$ .

We can derive the first-order differential equation of the solenoid model from the transfer function shown in Fig. 7.4, which relates voltage input $e _ { \mathrm { i n } } ( t )$ to electromagnetic forc $; f ,$ , and the result is

$$0. 0 0 3 \dot {f} + 1. 5 f = 1 2 e _ {\text { in }} (t) \tag {7.35}$$

![](image/62f7c1284b020e96d0b0889a866ff1e1b9759bcc0085de284fb71ae35d4d1a63.jpg)

<details>
<summary>line</summary>

| Time, s | Electromagnetic force, f(t), N |
| --- | --- |
| 0.000 | 0.0 |
| 0.002 | 8.0 |
| 0.004 | 14.0 |
| 0.006 | 15.5 |
| 0.008 | 16.0 |
| 0.010 | 16.0 |
| 0.012 | 16.0 |
| 0.014 | 16.0 |
| 0.016 | 16.0 |
</details>

Figure 7.6 Step response of the solenoid actuator for Example 7.5.

Following our procedure for sketching the first-order step response, we rewrite the first-order model in our standard form by dividing Eq. (7.35) by 1.5

$$0. 0 0 2 \dot {f} + f = 8 e _ {\text { in }} (t) \tag {7.36}$$

Therefore, the time constant is identified as $\tau = 0 . 0 0 2 \mathrm { s }$ . The solenoid will reach its steady-state force output in approximately four time constants, or $t _ { S } = 4 \tau = 0 . 0 0 8$ s. From Eq. (7.36) we see that the force reaches steady state for a 2-V step input when ${ \dot { f } } = 0 .$ , and therefore $f _ { \mathrm { s s } } = 8 \cdot 2 \ : \mathrm { V } = 1 6 \ : \mathrm { N }$ . Finally, the step response f (t) can be sketched by drawing an exponential rise from the given initial force $f ( 0 ) = 0$ to the steady-state force $f _ { \mathrm { s s } } = 1 6 \mathrm { N }$ at settling time $t _ { S } = 0 . 0 0 8 \mathrm { ~ s } .$ . Figure 7.6 presents the step response of the solenoid actuator for a 2-V step input.
