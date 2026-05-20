# Example 5.11

Plot the Nyquist locus for $L(s) = k / (s + 1)^3$ . For what values of $k$ is the closed-loop system stable?

Solution We have

$$L ^ {\prime} (j \omega) = \frac {1}{(j \omega + 1) ^ {3}}.$$

The behavior of $L'(j\omega)$ at $\omega = 0$ and $\omega \to \infty$ is easily established:

$$L ^ {\prime} (j 0) = 1\lim _ {\omega \rightarrow \infty} | L ^ {\prime} (j \omega) | = 0\lim _ {\omega \rightarrow \infty} \neq L ^ {\prime} (j \omega) = - 2 7 0 ^ {\circ}.$$

It will soon become apparent that the real-axis crossing points are key quantities. Clearly, $L(j\omega)$ is real if

$$\operatorname{Im} L ^ {\prime} (j \omega) = 0.$$

Here,

$$
\begin{array}{l} L ^ {\prime} (j \omega) = \frac {1}{- j \omega^ {3} - 3 \omega^ {2} + 3 j \omega + 1} \\ = \frac {(1 - 3 \omega^ {2}) + j (\omega^ {3} - 3 \omega)}{(1 - 3 \omega^ {2}) ^ {2} + (\omega^ {3} - 3 \omega) ^ {2}}. \\ \end{array}
$$

We see that $\operatorname{Im} L'(j\omega) = 0$ if

$$\omega^ {3} - 3 \omega = 0$$

or

$$\omega = 0 \pm \sqrt {3}.$$

At $\omega = 0$ , $L'(j\omega) = 1$ , obviously a real-axis point. At $\omega = \sqrt{3}$ ,

$$L ^ {\prime} (j \sqrt {3}) = \frac {(1 - 9)}{(1 - 9) ^ {3}} = - \frac {1}{8}.$$

![](image/2bffbeea7e08925e5fd41ef05d01dc749ffb85427abf43511a1983c54fb45036.jpg)

<details>
<summary>line</summary>

| Real | Imaginary |
| --- | --- |
| -0.2 | 0.4 |
| 0.0 | 0.0 |
| 0.2 | -0.4 |
| 0.4 | -0.6 |
| 0.6 | -0.4 |
| 0.8 | 0.0 |
| 1.0 | 0.4 |
</details>

Figure 5.16 The Nyquist plot

The locus is plotted in Figure 5.16 (MATLAB nyquist). Figure 5.17 (MATLAB bode) shows the Bode plots for $L'(j\omega)$ .

At $\omega = 0$ , $L'(j\omega) = 1$ (0 db and $0^{\circ}$ of phase). As $\omega$ increases, the phase becomes more and more negative, so the locus moves clockwise; the magnitude decreases, so the locus moves toward the origin. The negative real axis is crossed at $-\frac{1}{8}$ , which occurs for $\omega = \sqrt{3}$ . The locus tends to the origin as $\omega \to 0$ , and approaches it at an angle of $-270^{\circ}$ .

To assess stability, we must count encirclements of the point $(- \frac{1}{k}, 0)$ by the locus $L'(j\omega)$ . For stability, it is necessary that $N = 0$ , since $P = 0$ [L(s) has no RHP poles]. The point $(- \frac{1}{k}, 0)$ will not be encircled if either (i) $(- \frac{1}{k}, 0)$ lies to the left of $(- \frac{1}{8}, 0)$ or (ii) $(- \frac{1}{k}, 0)$ lies to the right of $(1, 0)$ . Therefore, stability follows if either

$$- \frac {1}{k} < - \frac {1}{8} \quad \text { or } \quad k < 8, \quad k > 0$$

or
