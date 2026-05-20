# Solution.

First Attempt: Assume the lead compensator $G _ { c } ( s )$ to be

$$G _ {c} (s) = K _ {c} \left(\frac {s + \frac {1}{T}}{s + \frac {1}{\alpha T}}\right) \quad (0 < \alpha < 1)$$

From the given specifications, $\zeta = 0 . 5$ and $\omega _ { n } = 2 \mathrm { r a d / s e c }$ , the dominant closed-loop poles must be located at

$$s = - 1 \pm j \sqrt {3}$$

We first calculate the angle deficiency at this closed-loop pole.

$$
\begin{array}{l} \text { Angle   deficiency } = - 1 2 0 ^ {\circ} - 1 2 0 ^ {\circ} - 1 0. 8 9 3 4 ^ {\circ} + 1 8 0 ^ {\circ} \\ = - 7 0. 8 9 3 4 ^ {\circ} \\ \end{array}
$$

This angle deficiency must be compensated by the lead compensator. There are many ways to determine the locations of the pole and zero of the lead network. Let us choose the zero of the compensator at s=–1. Then, referring to Figure 6–77, we have the following equation:

$$\frac {1 . 7 3 2 0 5}{x - 1} = \tan (9 0 ^ {\circ} - 7 0. 8 9 3 4 ^ {\circ}) = 0. 3 4 6 4 1$$

![](image/70783d515ecd7176d424f56aaf80808ee42b64a8f302c86ae485f0233210a150.jpg)

<details>
<summary>line</summary>

| σ | jω |
| --- | --- |
| -1 | j1.73205 |
| 0 |  |
| -1 | 70.8934° |
| 0 |  |
| x |  |
| 19.1066° |  |
</details>

Figure 6–77 Determination of the pole of the lead network.

or

$$x = 1 + \frac {1 . 7 3 2 0 5}{0 . 3 4 6 4 1} = 6$$

Hence,

$$G _ {c} (s) = K _ {c} \frac {s + 1}{s + 6}$$

The value of $K _ { c }$ can be determined from the magnitude condition

$$K _ {c} \left| \frac {s + 1}{s + 6} \frac {1}{s ^ {2}} \frac {1}{0 . 1 s + 1} \right| _ {s = - 1 + j \sqrt {3}} = 1$$

as follows:

$$K _ {c} = \left| \frac {(s + 6) s ^ {2} (0 . 1 s + 1)}{s + 1} \right| _ {s = - 1 + j \sqrt {3}} = 1 1. 2 0 0 0$$

Thus

$$G _ {c} (s) = 1 1. 2 \frac {s + 1}{s + 6}$$

Since the open-loop transfer function becomes

$$
\begin{array}{l} G _ {c} (s) G (s) H (s) = 1 1. 2 \frac {s + 1}{(s + 6) s ^ {2} (0 . 1 s + 1)} \\ = \frac {1 1 . 2 (s + 1)}{0 . 1 s ^ {4} + 1 . 6 s ^ {3} + 6 s ^ {2}} \\ \end{array}
$$

a root-locus plot of the compensated system can be obtained easily with MATLAB by entering num and den and using rlocus command. The result is shown in Figure 6–78.

Root-Locus Plot of Compensated System   
![](image/e5eb3288beed80f0d5594d83fe77556b3fcbee472662c983f1db61d9fcfb52db.jpg)

<details>
<summary>line</summary>

| Real Axis | Imag Axis |
| --- | --- |
| -10 | 0 |
| -5 | 0 |
| 0 | 0 |
| 5 | 10 |
| 10 | -10 |
</details>

Figure 6–78 Root-locus plot of the compensated system.

Figure 6–79 Unit-step response of the compensated system.   
![](image/62fc6aa6496815e0e6fbcb001047e9443c42158e4818d25b72b81731a913207d.jpg)
