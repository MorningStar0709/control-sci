# MATLAB Program 7–24

```matlab
num = [20];
den = [1 1 0];
w = logspace(-1,2,100);
bode(num,den,w)
title('Bode Diagram of G1(s) = 20/[s(s + 1)]') 
```

Since the specification calls for a phase margin of $5 0 ^ { \circ }$ , the additional phase lead necessary to satisfy the phase-margin requirement is 36°. A lead compensator can contribute this amount.

Noting that the addition of a lead compensator modifies the magnitude curve in the Bode diagram, we realize that the gain crossover frequency will be shifted to the right. We must offset the increased phase lag of $G _ { 1 } ( j \omega )$ due to this increase in the gain crossover frequency.Taking the shift of the gain crossover frequency into consideration, we may assume that $\phi _ { m }$ , the maximum phase lead required, is approximately $4 1 ^ { \circ } .$ . (This means that approximately $5 ^ { \circ }$ has been added to compensate for the shift in the gain crossover frequency.) Since

$$\sin \phi_ {m} = \frac {1 - \alpha}{1 + \alpha}$$

$\phi _ { m } = 4 1 ^ { \circ }$ corresponds to $\alpha = 0 . 2 0 7 7$ . Note that $\alpha = 0 . 2 1$ corresponds to $\phi _ { m } = 4 0 . 7 6 ^ { \circ }$ . Whether we choose $\phi _ { m } = 4 1 ^ { \circ } \mathrm { o r } \phi _ { m } = 4 0 . 7 6 ^ { \circ }$ does not make much difference in the final solution. Hence, let us choose $\alpha = 0 . 2 1$ .

![](image/191f296fbb82bcccd423a424acc87b1d7bbd8489e7930b4cea96f51843c6c2ed.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | Phase (deg); Magnitude (dB) |
| --- | --- |
| 0.1 | 50 |
| 1 | 0 |
| 10 | -50 |
| 100 | -100 |
</details>

Figure 7–145 Bode diagram of $G _ { 1 } ( s )$ .

Once the attenuation factor a has been determined on the basis of the required phase-lead angle, the next step is to determine the corner frequencies $\omega = 1 / T$ and $\omega = 1 / ( \alpha T )$ of the lead compensator. Notice that the maximum phase-lead angle $\phi _ { m }$ occurs at the geometric mean of the two corner frequencies, or $\omega = 1 / \big ( \sqrt { \alpha } T \big )$ .

The amount of the modification in the magnitude curve at $\omega = 1 / { \left( \sqrt { \alpha } T \right) }$ due to the inclusion of the term $( T s + 1 ) / ( \alpha T s + 1 )$ is

$$\left| \frac {1 + j \omega T}{1 + j \omega \alpha T} \right| _ {\omega = \frac {1}{\sqrt {\alpha} T}} = \left| \frac {1 + j \frac {1}{\sqrt {\alpha}}}{1 + j \alpha \frac {1}{\sqrt {\alpha}}} \right| = \frac {1}{\sqrt {\alpha}}$$

Note that

$$\frac {1}{\sqrt {\alpha}} = \frac {1}{\sqrt {0 . 2 1}} = 6. 7 7 7 8 \mathrm{dB}$$
