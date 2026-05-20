5. Settling time, $t _ { s } \mathrm { : }$ The settling time is the time required for the response curve to reach and stay within a range about the final value of size specified by absolute percentage of the final value (usually 2% or 5%). The settling time is related to the largest time constant of the control system.Which percentage error criterion to use may be determined from the objectives of the system design in question.

The time-domain specifications just given are quite important, since most control systems are time-domain systems; that is, they must exhibit acceptable time responses. (This means that, the control system must be modified until the transient response is satisfactory.)

![](image/b53f28a1d32218b10f253e9b2a17e3962754d41e2c25493bb27e93f2194499d7.jpg)

<details>
<summary>line</summary>

| t | c(t) |
| --- | --- |
| t_d | 0.5 |
| t_r | 0.7 |
| t_p | 0.9 |
| t_s | 0.8 |
| Allowable tolerance | 1.0 |
| t_s | 0.9 |
| t_r | 0.8 |
| t_p | 0.7 |
| t_s | 0.6 |
| t_r | 0.5 |
| t_p | 0.4 |
| t_s | 0.3 |
| t_r | 0.2 |
| t_p | 0.1 |
| t_s | 0.05 |
</details>

Figure 5–8 Unit-step response curve showing $t _ { d } , t _ { r }$ , $t _ { p } , M _ { p }$ , and $t _ { s }$ .

Note that not all these specifications necessarily apply to any given case. For example, for an overdamped system, the terms peak time and maximum overshoot do not apply. (For systems that yield steady-state errors for step inputs, this error must be kept within a specified percentage level. Detailed discussions of steady-state errors are postponed until Section 5–8.)

A Few Comments on Transient-Response Specifications. Except for certain applications where oscillations cannot be tolerated, it is desirable that the transient response be sufficiently fast and be sufficiently damped. Thus, for a desirable transient response of a second-order system, the damping ratio must be between 0.4 and 0.8. Small values of z(that is, $\zeta < 0 . 4 )$ yield excessive overshoot in the transient response, and a system with a large value of z(that is, $\zeta > 0 . 8 )$ responds sluggishly.

We shall see later that the maximum overshoot and the rise time conflict with each other. In other words, both the maximum overshoot and the rise time cannot be made smaller simultaneously. If one of them is made smaller, the other necessarily becomes larger.
