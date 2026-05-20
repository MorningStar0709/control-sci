$$s ^ {*} (3) = - \frac {1}{2} (3 + 1) = - 2.$$

To study the behavior for large k, we write

$$
\begin{array}{l} s ^ {*} (k) = - \frac {1}{2} (k + 1) \pm \frac {1}{2} \sqrt {k ^ {2} - 2 k + 1 - 4} \\ = - \frac {1}{2} (k + 1) \pm \frac {1}{2} \sqrt {(k - 1) ^ {2} - 4} \\ \end{array}
$$

![](image/c5b59baf92a042ce6cffb5985da1d8208c9a5835b18d4c058638f6ba57c66b24.jpg)

<details>
<summary>line</summary>

| Real Axis | Imag Axis |
| --- | --- |
| -1.0 | 0.0 |
| -0.5 | 0.8 |
| -0.5 | -0.8 |
</details>

Figure 5.1 Root locus plot

which, for large $k$ , becomes

$$s ^ {*} (k) \approx - \frac {1}{2} (k + 1) \pm \frac {1}{2} (k - 1) = - 1, - k$$

so that one root tends to -1, the zero of $P(s)$ , while the other tends to $-\infty$ . The locus is plotted in Figure 5.1.

To gain some insight into the nature of the Root Locus, write Equation 5.7 as

$$G (s) = - \frac {1}{k}. \tag {5.9}$$

As $G(s)$ is a complex quantity, this leads to

$$\neq G (s) = \neq - \frac {1}{k} = 1 8 0 ^ {\circ} \tag {5.10}| G (s) | = \frac {1}{k} \tag {5.11}$$

for k > 0. Equation 5.10 is the angle condition: any point s on the Root Locus is such that $\neq G(s) = 180^{\circ}$ . If a point s satisfies the angle condition, then it is a closed-loop pole for $k = 1/|G(s)|$ according to the magnitude condition, Equation 5.11.

It is sometimes useful to plot the Root Locus for $k < 0$ ; in that case, the angle condition is

$$\neq G (s) = 0 ^ {\circ}. \tag {5.12}$$

Good computer packages are now available for the Root Locus. Nevertheless, to develop insight about a specific problem, a control engineer must be able to determine the main features of the Root Locus without recourse to a computer. A number of rules have been developed to help sketch the locus. We shall now describe some of them.

Rule 1 The Root Locus branches start at the poles of $G(s)$ and end at its zeros.

From Equation 5.7, the equation

$$D (s) + k N (s) = 0$$

collapses into $D(s) = 0$ if $k = 0$ . Since the roots of $D(s)$ are the poles of $G(s)$ , those are the closed-loop poles for $k = 0$ . Writing

$$\frac {1}{k} D (s) + \frac {N (s)}{D (s)} = 0$$

we see that, for large $k$ , $s$ is such that $\frac{N(s)}{D(s)} \to 0$ . Thus, for large $k$ , the closed-loop poles tend to the roots of $N(s)$ —i.e., to the open-loop zeros—and also to infinity if $\frac{N}{D}$ is strictly proper.

Rule 2 For $k > 0$ , a point on the real axis belongs to the Root Locus if the total number of real-axis poles and zeros to its right is odd.

To show this, write the angle condition as
