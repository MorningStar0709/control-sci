| t Sec | Compensated system | Uncompensated system |
| --- | --- | --- |
| 35.0 | 35.0 | 35.0 |
| 35.5 | 35.5 | 35.5 |
| 36.0 | 36.0 | 36.0 |
| 36.5 | 36.5 | 36.5 |
| 37.0 | 37.0 | 37.0 |
| 37.5 | 37.5 | 37.5 |
| 38.0 | 38.0 | 38.0 |
| 38.5 | 38.5 | 38.5 |
| 39.0 | 39.0 | 39.0 |
| 39.5 | 39.5 | 39.5 |
| 40.0 | 40.0 | 40.0 |
</details>

Figure 6–85   
(a) Unit-step responses of the compensated and uncompensated systems; (b) unitramp responses of both systems; (c) unit-ramp responses showing steady-state errors.

A–6–16. Consider a unity-feedback control system whose feedforward transfer function is given by

$$G (s) = \frac {1 0}{s (s + 2) (s + 8)}$$

Design a compensator such that the dominant closed-loop poles are located at $s = - 2 \pm j 2 { \sqrt { 3 } }$ and the static velocity error constant $K _ { v }$ is equal to $8 0 \ \mathrm { s e c ^ { - 1 } }$ .

Solution. The static velocity error constant of the uncompensated system is $\begin{array} { r } { K _ { v } = \frac { 1 0 } { 1 6 } = 0 . 6 2 5 } \end{array}$ . Since $K _ { v } = 8 0$ is required, we need to increase the open-loop gain by 128. (This implies that we need a lag compensator.) The root-locus plot of the uncompensated system reveals that it is not possible to bring the dominant closed-loop poles to $- 2 \pm j 2 \sqrt { 3 }$ by just a gain adjustment alone. See Figure 6–86. (This means that we also need a lead compensator.) Therefore, we shall employ a lag–lead compensator.

Let us assume the transfer function of the lag–lead compensator to be

$$G _ {c} (s) = K _ {c} \left(\frac {s + \frac {1}{T _ {1}}}{s + \frac {\beta}{T _ {1}}}\right) \left(\frac {s + \frac {1}{T _ {2}}}{s + \frac {1}{\beta T _ {2}}}\right)$$

where $K _ { c } = 1 2 8 .$ . This is because

$$K _ {v} = \lim _ {s \rightarrow 0} s G _ {c} (s) G (s) = \lim _ {s \rightarrow 0} s K _ {c} G (s) = K _ {c} \frac {1 0}{1 6} = 8 0$$

and we obtain $K _ { c } = 1 2 8$ . The angle deficiency at the desired closed-loop pole $s = - 2 + j 2 { \sqrt { 3 } }$ is

$$\text { Angle deficiency } = - 1 2 0 ^ {\circ} - 9 0 ^ {\circ} - 3 0 ^ {\circ} + 1 8 0 ^ {\circ} = - 6 0 ^ {\circ}$$

The lead portion of the lag–lead compensator must contribute $6 0 ^ { \circ } .$ . To choose $T _ { 1 }$ we may use the graphical method presented in Section 6–8.

![](image/4ff501d9056a2e3eac3fa878ba436462c6cbb71c79dbee45723570d5024bb70a.jpg)

<details>
<summary>scatter</summary>

| Point Type | Real Axis | Imag Axis |
| --- | --- | --- |
| Desired closed-loop pole | -3 | 3 |
| Complex conjugate closed-loop pole | -2 | -4 |
</details>

Figure 6–86 Root-locus plot of G(s) = 10 Cs(s + 2)(s + 8)D.
