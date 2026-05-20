Draw the Bode diagram for this open-loop transfer function. Draw also the log-magnitude-versusphase plot, and show that two M loci are tangent to the $G ( j \omega )$ locus. Finally, plot the Bode diagram for the closed-loop transfer function.

Solution. Figure 7–141 shows the Bode diagram of $G ( j \omega )$ . Figure 7–142 shows the log-magnitude-versus-phase plot of $G ( j \omega )$ . It is seen that the $G ( j \omega )$ locus is tangent to the $M = 8 – \mathrm { d B }$ locus at $\omega = 0 . 9 7$ radsec, and it is tangent to the $M = - 4 { \cdot } \mathrm { d B }$ locus at $\omega = 2 . 8 \mathrm { r a d / s e c } .$ .

![](image/d40016f268b3ce55c4dbf4a3f7ef52b922512859d5afe98b06e5c1e20667554e.jpg)

<details>
<summary>line</summary>

| ω in rad/sec | dB (solid line) | dB (dashed line) |
| --- | --- | --- |
| 0.1 | 25 | 25 |
| 0.2 | 20 | 20 |
| 0.4 | 10 | 10 |
| 1 | 0 | 0 |
| 2 | -10 | -10 |
| 4 | -30 | -30 |
| 10 | 0 | 0 |
</details>

Figure 7–141 Bode diagram of $G ( s )$ given by Equation (7–32).

Figure 7–142

Log-magnitudeversus-phase plot of G(s) given by Equation (7–32).

![](image/43840bab35296ce5393e932a3d78b9ac219716d397173ad4f6481d41797f7c2d.jpg)  
Figure 7–143 shows the Bode diagram of the closed-loop transfer function. The magnitude curve of the closed-loop frequency response shows two resonant peaks. Note that such a case occurs when the closed-loop transfer function involves the product of two lightly damped secondorder terms and the two corresponding resonant frequencies are sufficiently separated from each other. As a matter of fact, the closed-loop transfer function of this system can be written

$$
\begin{array}{l} \frac {C (s)}{R (s)} = \frac {G (s)}{1 + G (s)} \\ = \frac {9}{(s ^ {2} + 0 . 4 8 7 s + 1) (s ^ {2} + 0 . 6 1 3 s + 9)} \\ \end{array}
$$

![](image/7fe874aaccfe5a1462c6e0db3c12a55a1fffc5b84ee87ae1275b7d944c156ad4.jpg)

<details>
<summary>line</summary>

| ω in rad/sec | dB |
| --- | --- |
| 0.1 | 0 |
| 0.2 | 0 |
| 0.4 | 0 |
| 0.6 | 0 |
| 1 | 5 |
| 2 | -5 |
| 4 | -20 |
| 6 | -40 |
| 10 | -360 |
</details>

Figure 7–143   
Bode diagram of G(s)C1 + G(s)D, where G(s) is given by Equation (7–32).

Clearly, the denominator of the closed-loop transfer function is a product of two lightly damped second-order terms (the damping ratios are 0.243 and 0.102), and the two resonant frequencies are sufficiently separated.
