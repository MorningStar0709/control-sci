# EXAMPLE 6.14 Moving-average self-tuner

Consider an integrator with a time delay $\tau$ . (Compare Example 4.6.) For the time delay $\tau < h$ the system is described by

$$A (q) = q (q - 1)B (q) = (h - \tau) q + \tau = (h - \tau) (q + b) = (h - \tau) B ^ {\prime}C (q) = q (q + c)$$

where

$$b = \frac {\tau}{h - \tau} \quad \text { and } \quad | c | < 1$$

The system is minimum-phase, $|b| < 1$ , when $\tau < h/2$ . Moving-average controllers of different orders will now be analyzed. (Compare Section 4.2.)

Case 1 (d = 1)

The minimum-variance strategy obtained through

$$A R + (h - \tau) B ^ {\prime} S = B ^ {\prime} C$$

giving

$$R (q) = q + bS (q) = \frac {1 + c}{h - \tau} q$$

is the only possibility to get a moving average of order zero. Since the process zero is canceled, it is necessary for stability that the system be minimum-phase. The characteristic equation of K in Eq. (6.83) is in this case

$$(\lambda + 1) \left(\lambda + \frac {1}{1 - b c}\right) = 0$$

Since $|b|$ and $|c|$ are both less than 1, it follows that the eigenvalues of $K$ are both negative.

Case 2 $(d = 2)$

Since B is of first order and C is of second order, there are several possibilities to get an output that is a moving-average process. We get the following combinations:

$$
\begin{array}{l} \text { Case } \quad B ^ {+} \\ 2 (\mathrm{a}) \quad q + b \quad \text { Minimum   variance } \\ 2 (b) \quad q + b \quad \text { Deadbeat } \\ 2 (c) \quad 1 \quad \text { Moving   average } \\ \end{array}
$$

To investigate the equilibria, first notice that Cases 2(a) and 2(b) can give stable equilibria only if $b < 1$ (i.e., $\tau < h / 2$ ).

Case 2(a) corresponds to the minimum-variance controller. The characteristic equation of the matrix K is

$$\lambda^ {2} - \lambda (b + c + \frac {c}{1 - b c}) + \frac {b c}{1 - b c} = 0$$

![](image/0bf5908e7c07dd10c770f75532f4387a4263787dfbe6f4248aa305a79c42f176.jpg)

<details>
<summary>other</summary>

| x | y |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.5 |
| 1.0 | 1.0 |
| 1.5 | 0.5 |
| 2.0 | 0.0 |
| 2.5 | -0.5 |
| 3.0 | -1.0 |
| 3.5 | -0.5 |
| 4.0 | 0.0 |
</details>

![](image/8ff3bf82ee5155012de7822550d9dc1f982c2e9b5ffaf3c1445938463cfbee6f.jpg)

<details>
<summary>line</summary>

| s̄₀ | r̄₁ |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.5 |
| 1.0 | 1.0 |
| 1.5 | 1.5 |
| 2.0 | 2.0 |
| 2.5 | 2.5 |
| 3.0 | 3.0 |
| 3.5 | 3.5 |
| 4.0 | 4.0 |
</details>
