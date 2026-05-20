| Real Axis | Imag Axis | a |
| --- | --- | --- |
| -6 | 0 | 3 |
| -4 | 0 | 3 |
| -2 | 0 | 3 |
| 0 | 0 | 3 |
| -6 | 2 | 4 |
| -4 | 2 | 4 |
| -2 | 2 | 4 |
| 0 | 2 | 4 |
| -6 | -2 | 4.5 |
| -4 | -2 | 4.5 |
| -2 | -2 | 4.5 |
| 0 | -2 | 4.5 |
| -6 | -4 | 6 |
| -4 | -4 | 6 |
| -2 | -4 | 6 |
| 0 | -4 | 6 |
| -6 | -6 | 6 |
| -4 | -6 | 6 |
| -2 | -6 | 6 |
| 0 | -6 | 6 |
| -6 | -8 | 6 |
| -4 | -8 | 6 |
| -2 | -8 | 6 |
| 0 | -8 | 6 |
</details>

Figure 8–41

$$
\begin{array}{l} \begin{array}{l} \text { Root - locus   plots   of } \\ 5 K (s + a) ^ {2} / [ s (s + 1) \end{array} \\ (s + 5) ] \text {   when   } a = 3, \\ a = 4, a = 4. 5, \text { and } \\ a = 6. \\ \end{array}
$$

which can be simplified to

$$2 4 + 2 5 K - 3 0 K a + 5 K a ^ {2} + j (- 1 6 - 6 0 K + 2 0 K a) = 0$$

By equating the real part and imaginary part to zero, respectively, we obtain

$$2 4 + 2 5 K - 3 0 K a + 5 K a ^ {2} = 0 \tag {8-9}- 1 6 - 6 0 K + 2 0 K a = 0 \tag {8-10}$$

From Equation (8–10), we have

$$K = \frac {4}{5 a - 1 5} \tag {8-11}$$

Substituting Equation (8–11) into Equation (8–9), we get

$$a ^ {2} = 1 3$$

or a=3.6056 or –3.6056. Notice that the values of K become

$$
\begin{array}{l} K = 1. 3 2 1 0 \quad \text { for } a = 3. 6 0 5 6 \\ K = - 0. 1 2 1 1 \quad \text { for } a = - 3. 6 0 5 6 \\ \end{array}
$$

Since $G _ { c 1 } ( s )$ is in the feedforward path, the gain K should be positive. Hence, we choose

$$K = 1. 3 2 1 0, \quad a = 3. 6 0 5 6$$

Then $G _ { c 1 } ( s )$ can be given by

$$
\begin{array}{l} G _ {c 1} (s) = K \frac {(s + a) ^ {2}}{s} \\ = 1. 3 2 1 0 \frac {(s + 3 . 6 0 5 6) ^ {2}}{s} \\ = \frac {1 . 3 2 1 0 s ^ {2} + 9 . 5 2 6 0 s + 1 7 . 1 7 3 5}{s} \\ \end{array}
$$

To determine $K _ { p } , T _ { i }$ and, $T _ { d } .$ we proceed as follows:,

$$
\begin{array}{l} G _ {c 1} (s) = \frac {1 . 3 2 1 0 \left(s ^ {2} + 7 . 2 1 1 2 s + 1 3\right)}{s} \\ = 9. 5 2 6 0 \left(1 + \frac {1}{0 . 5 5 4 7 s} + 0. 1 3 8 7 s\right) \tag {8-12} \\ \end{array}
$$

Thus,

$$K _ {p} = 9. 5 2 6 0, \quad T _ {i} = 0. 5 5 4 7, \quad T _ {d} = 0. 1 3 8 7$$

To check the response to a unit-step disturbance input, we obtain the closed-loop transfer function $Y ( s ) / D ( s )$ .

$$
\begin{array}{l} \frac {Y (s)}{D (s)} = \frac {G _ {p}}{1 + G _ {c 1} G _ {p}} \\ = \frac {5 s}{s (s + 1) (s + 5) + 5 K (s + a) ^ {2}} \\ = \frac {5 s}{s ^ {3} + 1 2 . 6 0 5 s ^ {2} + 5 2 . 6 3 s + 8 5 . 8 6 7 3} \\ \end{array}
$$

The response to the unit-step disturbance input is shown in Figure 8–42. The response curve seems good and acceptable. Note that the closed-loop poles are located at $s = - 3 \pm j 2$ and $s = - 6 . 6 0 5 1$ . The complex-conjugate closed-loop poles act as dominant closed-loop poles.

$D e s i g n o f G _ { c 2 } ( s )$ We now design: $G _ { c 2 } ( s )$ to obtain the desired responses to the reference inputs. The closed-loop transfer function $Y ( s ) / R ( s )$ can be given by
