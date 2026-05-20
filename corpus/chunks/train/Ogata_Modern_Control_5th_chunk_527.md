| ω in rad/sec | dB (G) | dB (Gc) | dB (GcG) | Phase Angle (°) |
| --- | --- | --- | --- | --- |
| 0.01 | 60 | 0 | 0 | 0 |
| 0.02 | 50 | -5 | -5 | -5 |
| 0.04 | 40 | -10 | -10 | -10 |
| 0.1 | 30 | -15 | -15 | -15 |
| 0.2 | 20 | -20 | -20 | -20 |
| 0.4 | 10 | -25 | -25 | -25 |
| 0.6 | 5 | -30 | -30 | -30 |
| 1 | 0 | -35 | -35 | -35 |
| 2 | -5 | -40 | -40 | -40 |
| 4 | -10 | -45 | -45 | -45 |
| 6 | -15 | -50 | -50 | -50 |
| 10 | -20 | -55 | -55 | -55 |
</details>

Recall that for the lead compensator the maximum phase-lead angle $\phi _ { m }$ is given by Equation (7–25), where a is $1 / \beta$ in the present case. By substituting $\alpha = 1 / \beta$ in Equation (7–25), we have

$$\sin \phi_ {m} = \frac {1 - \frac {1}{\beta}}{1 + \frac {1}{\beta}} = \frac {\beta - 1}{\beta + 1}$$

Notice that $\beta = 1 0$ corresponds to $\phi _ { m } = 5 4 . 9 ^ { \circ }$ . Since we need a $5 0 ^ { \circ }$ phase margin, we may choose $\beta = 1 0 .$ . (Note that we will be using several degrees less than the maximum angle, 54.9°.) Thus,

$$\beta = 1 0$$

Then the corner frequency $\omega = 1 / \beta T _ { 2 }$ (which corresponds to the pole of the phase-lag portion of the compensator) becomes v=0.015 radsec. The transfer function of the phase-lag portion of the lag–lead compensator then becomes

$$\frac {s + 0 . 1 5}{s + 0 . 0 1 5} = 1 0 \left(\frac {6 . 6 7 s + 1}{6 6 . 7 s + 1}\right)$$

The phase-lead portion can be determined as follows: Since the new gain crossover frequency is v=1.5 radsec, from Figure 7–111, G(j1.5) is found to be 13 dB. Hence, if the lag–lead compensator contributes –13 dB at v=1.5 radsec, then the new gain crossover frequency is as desired. From this requirement, it is possible to draw a straight line of slope 20 dBdecade, passing through the point (1.5 radsec, –13 dB). The intersections of this line and the 0-dB line and –20-dB line determine the corner frequencies. Thus, the corner frequencies for the lead portion are $\omega = 0 . 7$ radsec and $\omega = 7 ~ \mathrm { r a d / s e c }$ . Thus, the transfer function of the lead portion of the lag–lead compensator becomes

$$\frac {s + 0 . 7}{s + 7} = \frac {1}{1 0} \left(\frac {1 . 4 3 s + 1}{0 . 1 4 3 s + 1}\right)$$

Combining the transfer functions of the lag and lead portions of the compensator, we obtain the transfer function of the lag–lead compensator. Since we chose $K _ { c } = 1$ , we have

$$G _ {c} (s) = \left(\frac {s + 0 . 7}{s + 7}\right) \left(\frac {s + 0 . 1 5}{s + 0 . 0 1 5}\right) = \left(\frac {1 . 4 3 s + 1}{0 . 1 4 3 s + 1}\right) \left(\frac {6 . 6 7 s + 1}{6 6 . 7 s + 1}\right)$$
