Figure 10.44 shows the root locus for the new PD controller with an open-loop zero at $s = - 6$ . Note that the circular part of the root locus has a larger radius compared to the previous PD design (see Fig. 10.42) and hence the real-axis break-in point has been shifted farther to the left (approximately $s = - 1 2 )$ . Consequently, the transient response will die out in less than half the time compared to the response shown in Fig. 10.43. However, the new gain setting for a fast, well-damped response is about $K = 1 1 . 4$ and therefore $K _ { P } = 6 K =$ 68.4 V/m and $K _ { D } = K = 1 1 . 4 \mathrm { V - s / m }$ . The increase in closed-loop performance comes at a price: the higher PD gains result in larger voltage commands for the actuator, which may exceed its limitations and damage the device. By this reasoning, we see that a theoretical design with a very fast response due to extremely high gains must be checked to ensure that the physical signals in the loop (voltages, forces, etc.) are realistic and within acceptable boundaries. Another practical issue is that a high derivative gain $K _ { D }$ will amplify sudden changes in the feedback error (position error $x _ { e } ,$ in this case) and produce large control signals that might damage the actuator. High-frequency noise is sometimes present in the feedback signal and hence a large D-gain will amplify the corrupted derivative information and produce an extremely large control signal.

![](image/c202b4591462114685bf39e226d69c324f6afe5632b314ddb566a3a9367ff89b.jpg)

<details>
<summary>scatter</summary>

| Point Type | X (Real Axis) | Y (Imaginary Axis) |
| --- | --- | --- |
| Open-loop plant poles | 0 | 0 |
| PD controller zero at s = -6 | -6 | 0 |
| Fast, well-damped closed-loop poles | -12 | 1.5 |
</details>

Figure 10.44 Root-locus plot for PD controller with zero at s = −6 (Example 10.12).

All of the previous examples using PD or PID controllers have demonstrated good theoretical closedloop performance. However, we should carefully reconsider the derivative control action when the reference input is a step function. Let us repeat Eq. (10.11), which presents the expression for the PID control signal

$$u (t) = K _ {P} e (t) + K _ {I} \int e (t) d t + K _ {D} \dot {e} (t) \tag {10.50}$$
