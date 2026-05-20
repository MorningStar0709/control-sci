# Example 6.4 (dc Servo)

For the dc servo of Example 2.1 (Chapter 2), calculate the largest value of the gain $k$ that will satisfy the following specifications: $|T(j\omega)| \leq 2$ db, $|S(j\omega)| \leq 4$ db.

Solution From Equation 3.21 (Chapter 3),

$$P (s) = \frac {\theta}{v} = \frac {8 8 . 7 6}{s (s + 2 . 4 7 4) (s + 2 1 . 5 2 6)}.$$

Figure 6.11 shows the gain-phase loci of $P(j\omega)$ and $P^{-1}(j\omega)$ (MATLAB bode, nichols) with the Nichols chart. With $k = 1$ (0 db), the peak value of $|T|$ is about 1 db, and that of $|S|$ is 3 db. It can be seen that a gain of about 2 db will raise the

![](image/53d64141ad40fef998240cdf561fd24b7a03dacd425f00d2cb7235a802c4ab9b.jpg)

<details>
<summary>radar</summary>

| Phase (deg) | Magnitude (db) | Probability |
| --- | --- | --- |
| -250 | -40 | 0 |
| -200 | -20 | 0.25 |
| -150 | 0 | 0.5 |
| -100 | 20 | 1 |
| -50 | 30 | 3 |
| -250 | 40 | 6 |
</details>

Figure 6.11 Gain-phase plots of P and $P^{-1}$

$P$ -locus about enough to graze the 2-db contour and lower the $P^{-1}$ locus to touch the 4-db contours. By trial-and-error computation of $S(j\omega)$ and $T(j\omega)$ , the actual value is 2.75 db, or $k = 1.36$ .
