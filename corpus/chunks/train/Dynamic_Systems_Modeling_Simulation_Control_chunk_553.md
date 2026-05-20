Increasing the P-gain $K _ { P }$ will reduce the time constant and hence reduce the settling time $( t _ { S } = 4 \tau )$ . Using the gain $K _ { P } = 0 . 5 \mathrm { V } { - } \mathrm { s } / \mathrm { r a d }$ , we see that the time constant is $\tau = 0 . 0 0 4 5$ s and the settling time is 0.018 s. Figure 10.16 shows the closed-loop angular velocity response of the DC motor with reference command $\omega _ { \mathrm { r e f } } = 5 0$ rad/s (477.5 rpm) and three proportional gains $K _ { P } = 1 , 0 . 5$ , and 0.2 V-s/rad (the motor is starting from rest). As we increase $K _ { P } ,$ , the motor displays a faster response and achieves a steady-state speed that is closer to the 50-rad/s reference command. This trend might tempt the engineer to select an extremely large control gain for a very fast response with a small tracking error. However, a large gain will produce a large initial armature voltage $e _ { \mathrm { i n } } ( t )$ . Initially, the speed error is 50 rad/s because the motor is starting from rest and the speed command is $\omega _ { \mathrm { r e f } } = 5 0 \mathrm { r a d / s }$ . Consequently, the initial armature voltage is 50 V if the controller gain is set at $K _ { P } = 1 \mathrm { V - s / r a d } .$ . This input voltage would likely exceed the maximum allowable voltage for a small DC motor.

![](image/3ba79d1a05e77d2d04ddc47f4fdc6b5d606edd52d3e4faeecf646ce153c213cd.jpg)

<details>
<summary>line</summary>

| Time, s | DC motor speed, ω(t), rad/s (Kp = 0.2 V-s/rad) | DC motor speed, ω(t), rad/s (Kp = 0.5 V-s/rad) | DC motor speed, ω(t), rad/s (Kp = 1 V-s/rad) |
| --- | --- | --- | --- |
| 0.00 | 0 | 0 | 0 |
| 0.01 | ~45 | ~35 | ~25 |
| 0.02 | ~47 | ~40 | ~30 |
| 0.03 | ~48 | ~42 | ~35 |
| 0.04 | ~48 | ~43 | ~38 |
| 0.05 | ~48 | ~44 | ~39 |
| 0.06 | ~48 | ~44 | ~39 |
| 0.07 | ~48 | ~44 | ~39 |
| 0.08 | ~48 | ~44 | ~39 |
</details>

Figure 10.16 Closed-loop response of DC motor with P-controller (Example 10.5).

Figure 10.16 shows that a proportional controller alone cannot reduce the steady-state speed error of the motor. Furthermore, we need a controller that can provide an armature voltage signal (i.e., motor torque) even when the speed error $\omega _ { e } ( t )$ is driven to zero at steady state. A PI controller is the logical choice. The PI controller transfer function is

$$G _ {C} (s) = K _ {P} + \frac {K _ {I}}{s} = \frac {K _ {P} s + K _ {I}}{s} \tag {10.17}$$

The PI controller $G _ { C } ( s )$ has one zero at $s = - K _ { I } / K _ { P }$ and one pole at s = 0 (i.e., the integrator). Our closed-loop system with PI control is
