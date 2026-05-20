The magnitude and phase-angle curves of the lag–lead compensator just designed are shown in Figure 7–111. The open-loop transfer function of the compensated system is

$$
\begin{array}{l} G _ {c} (s) G (s) = \frac {(s + 0 . 7) (s + 0 . 1 5) 2 0}{(s + 7) (s + 0 . 0 1 5) s (s + 1) (s + 2)} \\ = \frac {1 0 (1 . 4 3 s + 1) (6 . 6 7 s + 1)}{s (0 . 1 4 3 s + 1) (6 6 . 7 s + 1) (s + 1) (0 . 5 s + 1)} \tag {7-29} \\ \end{array}
$$

The magnitude and phase-angle curves of the system of Equation (7–29) are also shown in Figure 7–111. The phase margin of the compensated system is $5 0 ^ { \circ }$ , the gain margin is 16 dB, and the static velocity error constant is 10 $\sec ^ { - 1 }$ . All the requirements are therefore met, and the design has been completed.

Figure 7–112 shows the polar plots of $G ( j \omega )$ (gain-adjusted but uncompensated open-loop transfer function) and $G _ { c } ( j \omega ) G ( j \omega )$ (compensated open-loop transfer function).The $G _ { c } ( j \omega ) G ( j \omega )$ locus is tangent to the M=1.2 circle at about $\omega = 2 \mathrm { r a d } / \mathrm { s e c } .$ . Clearly, this indicates that the compensated system has satisfactory relative stability. The bandwidth of the compensated system is slightly larger than 2 radsec.

![](image/ba2130cf89fbad749d7b01a9b95cf6cfef229cab8943036d786fcc5c05268cb6.jpg)

<details>
<summary>other</summary>

| Point Label | Re | Im |
| --- | --- | --- |
| ω = 0.15 | -6.0 | -8.0 |
| ω = 1 | -4.0 | -2.0 |
| 0.2 | -3.0 | -5.0 |
| 0.4 | -2.0 | -3.0 |
| 1 | -1.0 | -1.0 |
| 2 | -1.0 | 0.0 |
| M = 1.2 | -6.0 | 2.0 |
</details>

Figure 7–112 Polar plots of G (gain adjusted) and $G _ { c } G .$ .

Figure 7–113 Unit-step response of the compensated system (Example 7–28).   
![](image/63f3d9af4366f417643aed09d4795b066d3a0af51c18aacc83fcd1c4164aac20.jpg)

<details>
<summary>line</summary>

| t Sec | Output |
| --- | --- |
| 0 | 0.0 |
| 2 | 1.15 |
| 4 | 1.05 |
| 6 | 1.03 |
| 8 | 1.02 |
| 10 | 1.01 |
| 12 | 1.005 |
| 14 | 1.002 |
| 16 | 1.001 |
| 18 | 1.0005 |
| 20 | 1.0 |
</details>

In the following we shall examine the transient-response characteristics of the compensated system. (The gain-adjusted but uncompensated system is unstable.) The closed-loop transfer function of the compensated system is

$$\frac {C (s)}{R (s)} = \frac {9 5 . 3 8 1 s ^ {2} + 8 1 s + 1 0}{4 . 7 6 9 1 s ^ {5} + 4 7 . 7 2 8 7 s ^ {4} + 1 1 0 . 3 0 2 6 s ^ {3} + 1 6 3 . 7 2 4 s ^ {2} + 8 2 s + 1 0}$$

The unit-step and unit-ramp response curves obtained with MATLAB are shown in Figures 7–113 and 7–114, respectively.
