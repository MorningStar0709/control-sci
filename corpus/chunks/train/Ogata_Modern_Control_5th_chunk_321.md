$$K > \frac {(s + 3) (s ^ {2} + 2 s + 2)}{s + 2} \Bigg | _ {s = 0} = 3$$

Figure 6–31 Root-locus plot for the positive-feedback system with

$$
\begin{array}{l} G (s) = K (s + 2) / \\ \left[ (s + 3) \left(s ^ {2} + 2 s + 2\right) \right], \\ H (s) = 1. \\ \end{array}
$$

![](image/e2274c863f8612debdadd23a740098eb7853b7b57b4cb33a7053f7bc9281f654.jpg)

<details>
<summary>line</summary>

| σ | jω |
| --- | --- |
| -5 | j2 |
| -4 | j2 |
| -3 | j1 |
| -2 | j1 |
| -1 | j1 |
| 0 | -j1 |
| 1 | -j2 |
| 2 | -j2 |
</details>

one real root enters the right-half s plane. Hence, for values of K greater than 3, the system becomes unstable. (For $K > 3 ,$ the system must be stabilized with an outer loop.)

Note that the closed-loop transfer function for the positive-feedback system is given by

$$
\begin{array}{l} \frac {C (s)}{R (s)} = \frac {G (s)}{1 - G (s) H (s)} \\ = \frac {K (s + 2)}{(s + 3) \left(s ^ {2} + 2 s + 2\right) - K (s + 2)} \\ \end{array}
$$

To compare this root-locus plot with that of the corresponding negative-feedback system, we show in Figure 6–32 the root loci for the negative-feedback system whose closedloop transfer function is

$$\frac {C (s)}{R (s)} = \frac {K (s + 2)}{(s + 3) \left(s ^ {2} + 2 s + 2\right) + K (s + 2)}$$

Table 6–2 shows various root-locus plots of negative-feedback and positive-feedback systems. The closed-loop transfer functions are given by

$$
\begin{array}{l} \frac {C}{R} = \frac {G}{1 + G H}, \\ \frac {C}{R} = \frac {G}{1 - G H}, \\ \end{array}
$$

![](image/b1ec4469324fd66a3fff2254c695a1592ccf13d23b4d4daef9f636ad392cd793.jpg)

<details>
<summary>line</summary>

| σ | jω |
| --- | --- |
| -2 | -j1 |
| -1 | j1 |
| -3 | j2 |
| -4 | j3 |
| -5 | j4 |
</details>

Figure 6–32 Root-locus plot for the negative-feedback system with

$$
\begin{array}{l} G (s) = K (s + 2) / \\ \bigl [ (s + 3) \bigl (s ^ {2} + 2 s + 2 \bigr) \bigr ], \\ H (s) = 1. \\ \end{array}
$$

where GH is the open-loop transfer function. In Table 6–2, the root loci for negativefeedback systems are drawn with heavy lines and curves, and those for positive-feedback systems are drawn with dashed lines and curves.

Table 6–2 Root-Locus Plots of Negative-Feedback and Positive-Feedback Systems
