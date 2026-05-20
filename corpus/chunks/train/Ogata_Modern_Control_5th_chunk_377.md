<details>
<summary>line</summary>

| t Sec | Output |
| --- | --- |
| 0 | 0.0 |
| 1 | 1.5 |
| 2 | 1.2 |
| 3 | 0.9 |
| 4 | 1.0 |
| 5 | 1.0 |
| 6 | 1.0 |
| 7 | 1.0 |
| 8 | 1.0 |
| 9 | 1.0 |
| 10 | 1.0 |
</details>

The closed-loop transfer function for the compensated system becomes

$$\frac {C (s)}{R (s)} = \frac {1 1 . 2 (s + 1) (0 . 1 s + 1)}{(s + 6) s ^ {2} (0 . 1 s + 1) + 1 1 . 2 (s + 1)}$$

Figure 6–79 shows the unit-step response curve. Even though the damping ratio of the dominant closed-loop poles is 0.5, the amount of overshoot is very much higher than expected.A closer look at the root-locus plot reveals that the presence of the zero at $s = - 1$ is increasing the amount of the maximum overshoot. [In general, if a closed-loop zero or zeros (compensator zero or zeros) lie to the right of the dominant pair of the complex poles, then the dominant poles are no longer dominant.] If large maximum overshoot cannot be tolerated, the compensator zero(s) should be shifted sufficiently to the left.

In the current design, it is desirable to modify the compensator and make the maximum overshoot smaller. This can be done by modifying the lead compensator, as presented in the following second attempt.

Second Attempt: To modify the shape of the root loci, we may use two lead networks, each contributing half the necessary lead angle, which is $7 0 . 8 9 3 4 ^ { \circ } / 2 = 3 5 . 4 4 6 7 ^ { \circ }$ Let us choose the. location of the zeros at $s = - 3 .$ . (This is an arbitrary choice. Other choices such as $s = - 2 . 5$ and s=–4 may be made.)

Once we choose two zeros at $s = - 3 .$ , the necessary location of the poles can be determined as shown in Figure 6–80, or

$$
\begin{array}{l} \frac {1 . 7 3 2 0 5}{y - 1} = \tan (4 0. 8 9 3 3 4 ^ {\circ} - 3 5. 4 4 6 7 ^ {\circ}) \\ = \tan 5. 4 4 6 6 ^ {\circ} = 0. 0 9 5 3 5 \\ \end{array}
$$

which yields

$$y = 1 + \frac {1 . 7 3 2 0 5}{0 . 0 9 5 3 5} = 1 9. 1 6 5 2$$

![](image/7fc097fcf267dd9909549c056c24daa5ab3b36df5dfdc60fb07105fc2decbd24.jpg)

<details>
<summary>line</summary>

| σ | jω |
| --- | --- |
| -20 | 0 |
| -4 | 35.4467° |
| -1 | 40.89334° |
| 1.73205 | 0 |
</details>

Figure 6–80 Determination of the pole of the lead network.

Hence, the lead compensator will have the following transfer function:

$$G _ {c} (s) = K _ {c} \left(\frac {s + 3}{s + 1 9 . 1 6 5 2}\right) ^ {2}$$

The value of $K _ { c }$ can be determined from the magnitude condition as follows:

$$\left| K _ {c} \left(\frac {s + 3}{s + 1 9 . 1 6 5 2}\right) ^ {2} \frac {1}{s ^ {2}} \frac {1}{0 . 1 s + 1} \right| _ {s = - 1 + j \sqrt {3}} = 1$$

or

$$K _ {c} = 1 7 4. 3 8 6 4$$
