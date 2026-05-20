# Solution

Figure 9.11 shows the Nyquist plot (MATLAB dnyquist). There are two open-loop poles within the unit circle $P = 2$ , and we need two closed-loop poles within the unit circle $Z = 2$ , so N = 0 for stability. The two real-axis crossings are at -0.444 and 4, respectively, so for stability we need

$$
\begin{array}{l} - \frac {1}{k} <   - 0. 4 4 4 \quad \text { or } \quad k <   2. 2 5 \\ - \frac {1}{k} > 4 \quad \text { or } \quad k > - 0. 2 5. \\ \end{array}
$$

![](image/638a78962682882089734b713667e70159ebae5a9c62675ed4df08986c0b1f20.jpg)

<details>
<summary>line</summary>

| Real Axis | Imaginary Axis |
| --- | --- |
| -0.5 | 0 |
| 1.5 | -2.5 |
| 4 | 0 |
</details>

Figure 9.11 Discrete time Nyquist plot for Example 9.11

The rules for counting encirclements from Bode plots are the same as in continuous time, with the proviso that $\omega = \pi/T_{s}$ , the highest frequency plotted, is equivalent to $\omega = \infty$ in continuous time. A real-axis crossing at $\omega = \pi/T_{s}$ (there will always be one) is counted as one crossing, not two.

Poles on the unit circle are dealt with by indenting to the outside. Since the phase decreases on the semicircle, its map is a large, clockwise semicircle (or circle, if the pole is a multiple pole). Another way to see this is to note that the contour takes a $90^{\circ}$ right turn when entering the semicircle; hence its map must do the same. If the mapping of the entry point to the indentation is in the top half of the complex plane (phase between $0^{\circ}$ and $180^{\circ}$ ), the real-axis crossing will take place on the far right; it will take place on the far left if the entry point maps into a point on the bottom half.
