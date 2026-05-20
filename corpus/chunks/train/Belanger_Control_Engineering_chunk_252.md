# Example 5.6 (dc Servo)

Draw the Root Locus for the dc servo of Example 2.1 (Chapter 2). Select the gain so that the complex closed-loop poles are those of a second-order Butterworth filter.

Solution From Equation 3.25, the open-loop transfer function is

$$\frac {\theta}{v} = \frac {8 8 . 7 6}{s (s + 2 1 . 5 7 6) (s + 2 . 4 2 4)}.$$

Figure 5.4 illustrates the construction of the Root Locus, starting with the pole-zero plot. The rules are applied as follows.

Rule 2: Real-axis portions are -2.424 to 0, and left of -21.576.

![](image/74df117d5135569340849d3e44ccdd53f4babd82bacf830a21a036fa1e160041.jpg)

<details>
<summary>line</summary>

| Real | Imaginary |
| --- | --- |
| -22 | 0 |
| -3 | 0 |
| -1 | 0 |
| 0 | 0 |
| 0 | 7 |
| 0 | -7 |
</details>

Figure 5.4 Root locus plot, dc servo

Rule 3:

$$
\begin{array}{l} \sigma = \frac {(0 - 2 1 . 5 7 6 - 2 . 4 2 4) - 0}{3 - 0} = - 8. 0 0 0 \\ \neq s = + \frac {1 8 0 ^ {\circ} \pm k 3 6 0 ^ {\circ}}{0 - 3} \\ = - 6 0 ^ {\circ} \mp k 1 2 0 ^ {\circ} \\ = - 6 0 ^ {\circ}, + 6 0 ^ {\circ}, - 1 8 0 ^ {\circ}. \\ \end{array}
$$

The asymptotes are drawn in Figure 5.4.

The asymptotes are drawn in Figure 2. Rule 1: The three branches emanate from the poles and go to the three "zeros" at infinity along the asymptotes. This requires that the branches starting at 0 and -2.424 meet and break away from the real axis, in order to head along the asymptotes at $\pm 60^{\circ}$ .

The $j$ -axis crossing points of the Root Locus are obtained from the Routh criterion. The locus crosses the $j$ -axis when the gain takes the marginal stability value. As was shown in Example 5.3, that gain is 14.400 and results in a pair of roots at $\pm j7.298$ . Clearly, the points $\pm j7.298$ are closed-loop poles for $k = 14.400$ , so they belong to the Root Locus.

Figure 5.4 shows the Root Locus (MATLAB rlocus). Figure 5.5 shows the portion of the Root Locus near the origin. The poles of a Butterworth transfer function of order 2 lie on radial lines at $\pm 45^{\circ}$ from the negative real axis, so the poles lie where these lines intersect the Root Locus, at $s^{*} = -1.15 \pm j1.15$ . The gain required to place the poles there is calculated from the magnitude condition Equation 5.11:

![](image/0e690e72b0e461d846ca2b0d904f04fe69fe448a5a81c8ccde4627aba0922b0a.jpg)

<details>
<summary>line</summary>

| Real | Imaginary |
| --- | --- |
| -2.5 | 0 |
| -1.5 | 0 |
| -1.0 | 0 |
| -0.5 | 0 |
| 0 | 0 |
</details>

Figure 5.5 Root locus near the origin, dc servo

$$
\begin{array}{l} k = \frac {1}{| P (s) |} \\ = \left| \frac {s ^ {*} (s ^ {*} + 2 1 . 5 7 6) (s ^ {*} + 2 . 4 2 4)}{8 8 . 7 6} \right| \\ = 0. 6 5 7. \\ \end{array}
$$

Most computer packages will also calculate this. (MATLAB rlocfind)
