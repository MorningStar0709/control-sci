| Real Axis | Imaginary Axis |
| --- | --- |
| -0.5 | 0.5 |
| 0 | 0 |
| 0.5 | -1 |
| 1 | 0 |
| 0.5 | 1.2 |
| 0 | 1.3 |
| -0.5 | -0.5 |
| 0 | -1.2 |
| 0.5 | -1.3 |
| 1 | -0.5 |
| 0 | 0 |
| -0.5 | 0.5 |
| 0 | 1.2 |
| 0.5 | 1.3 |
| 1 | 0 |
| 0 | -0.5 |
| -0.5 | -0.5 |
| 0 | -1 |
| 0.5 | -1.2 |
| 1 | -1.3 |
| 0 | -1.3 |
| -0.5 | -1.3 |
| 0 | -1.3 |
| 0.5 | -1.3 |
| 1 | -1.3 |
| 0 | -1.3 |
| -0.5 | -1.3 |
| 0 | -1.3 |
| 0.5 | -1.3 |
| 1 | -1.3 |
| 0 | -1.3 |
| -0.5 | -1.3 |
| 0 | -1.3 |
| 0.5 | -1.3 |
| 1 | -1.3 |
| 0 | -1.3 |
| -0.5 | -1.3 |
| 0 | -1.3 |
| 0.5 | -1.3 |
| 1 | -1.3 |
| 0 | -1.3 (estimated) |
| 0.5 | -1.3 (estimated) |
| 1 | -1.3 (estimated) |
| 0 | -1.3 (estimated) |
| -0.5 | -1.3 (estimated) |
| 0 | -1.3 (estimated) |
| 0.5 | -1.3 (estimated) |
| 1 | -1.3 (estimated) |
| 0 | -1.3 (estimated) |
| -0.5 | -1.3 (estimated) |
| 0 | -1.3 (estimated) |
| 0.5 | -1.3 (estimated) |
| 1 | -0.5 (estimated) |
| 0 | -0.5 (estimated) |
| -0.5 | -0.5 (estimated) |
| 0 | -0.5 (estimated) |
| 0.5 | -0.5 (estimated) |
| 1 | -0.5 (estimated) |
| 0 | -0.5 (estimated) |
| -0.5 | -0.5 (estimated) |
| 0 | -0.5 (estimated) |
| 0.5 | -0.5 (estimated) |
| 1 | -0.5 (estimated) |
| 0 | -0.5 (estimated) |
|
| -0.5 | -0.5 (estimated) |
| --- | --- |
| 0 | -0.5 (estimated) |
| 0.5 | -0.5 (estimated) |
| 1 | -0.5 (estimated) |
| 0 | -0.5 (estimated) |
| -0.5 | -0.5 (estimated) |
| 0 | -0.5 (estimated) |
| 1 | -0.5 (estimated) |
| 0 | -0.5 (estimated) |
| -0.5 | -0.5 (estimated) |
| 0 | -0.5 (estimated) |
| 0.5 | -0.5 (estimated) |
| 1 | -0.5 (estimated) |
| 0 | -0.7 (estimated) |
| -0.5 | -0.7 (estimated) |
| 0 | -0.7 (estimated) |
| 0.5 | -0.7 (estimated) |
| 1 | -0.7 (estimated) |
| 0 | -0.7 (estimated) |
| -0.5 | -0.7 (estimated) |
| 0 | -0.7 (estimated) |
| 0.5 | -0.7 (estimated) |
| 1 | -0.7 (estimated) |
| 0 | -0.7 (estimated) |
| -0.5 | -0.7 (estimated) |
</details>

If we wish to draw the Nyquist plot using manually determined ranges—for example, from –2 to 2 on the real axis and from –2 to 2 on the imaginary axis—enter the following command into the computer:

$$
v = \left[ \begin{array}{c c c c} - 2 & 2 & - 2 & 2 \end{array} \right];
\text { axis } (v);
$$

or, combining these two lines into one,

$$\text { axis } ([ - 2 2 - 2 2 ]);$$

See MATLAB Program 7–6 and the resulting Nyquist plot shown in Figure 7–37.

<table><tr><td>MATLAB Program 7-6</td></tr><tr><td>% ---- Nyquist plot ----</td></tr><tr><td>num = [1];</td></tr><tr><td>den = [1 0.8 1];</td></tr><tr><td>nyquist(num,den)</td></tr><tr><td>v = [-2 2 -2 2]; axis(v)</td></tr><tr><td>grid</td></tr><tr><td>title(&#x27;Nyquist Plot of G(s) = 1/(s^2 + 0.8s + 1)&#x27;)</td></tr></table>

Figure 7–37
