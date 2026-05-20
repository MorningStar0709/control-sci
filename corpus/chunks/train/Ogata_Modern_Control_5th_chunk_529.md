Figure 7–114 Unit-ramp response of the compensated system (Example 7–28).   
![](image/932f9e657295263765c2fb929a6aed934aaa71f2df21a72870dced337c815507.jpg)

<details>
<summary>line</summary>

| t Sec | Output |
| --- | --- |
| 0 | 0 |
| 2 | 2 |
| 4 | 4 |
| 6 | 6 |
| 8 | 8 |
| 10 | 10 |
| 12 | 12 |
| 14 | 14 |
| 16 | 16 |
| 18 | 18 |
| 20 | 20 |
</details>

Note that the designed closed-loop control system has the following closed-loop zeros and poles:

$$\text { Zeros at } s = - 0. 1 4 9 9, \quad s = - 0. 6 9 9 3\text { Poles at } s = - 0. 8 9 7 3 \pm j 1. 4 4 3 9s = - 0. 1 7 8 5, \quad s = - 0. 5 4 2 5, \quad s = - 7. 4 9 2 3$$

The pole at $s = - 0 . 1 7 8 5$ and zero at s=–0.1499 are located very close to each other. Such a pair of pole and zero produces a long tail of small amplitude in the step response, as seen in Figure 7–113. Also, the pole at s=–0.5425 and zero at s=–0.6993 are located fairly close to each other.This pair adds amplitude to the long tail.

Summary of Control Systems Design by Frequency-Response Approach. The last three sections presented detailed procedures for designing lead, lag, and lag–lead compensators by the use of simple examples. We have shown that the design of a compensator to satisfy the given specifications (in terms of the phase margin and gain margin) can be carried out in the Bode diagram in a simple and straightforward manner. It is noted that not every system can be compensated with a lead, lag, or lag–lead compensator. In some cases compensators with complex poles and zeros may be used. For systems that cannot be designed by use of the root-locus or frequencyresponse methods, the pole-placement method may be used. (See Chapter 10.) In a given design problem if both conventional design methods and the pole-placement method can be used, conventional methods (root-locus or frequency-response methods) usually result in a lower-order stable compensator. Note that a satisfactory design of a compensator for a complex system may require a creative application of all available design methods.
