As noted above, 23 sets of variables a, b, and c satisfy the requirement. Unit-step response curves of the system with any of the 23 sets are about the same.The unit-step response curve with

$$a = 4. 2, \qquad b = 2, \qquad c = 1 2$$

is shown in Figure $8 { - } 3 5 ( \mathrm { a } )$ . The maximum overshoot is 18.96% and the settling time is 0.85 sec. Using these values of a, b, and c, the desired closed-loop poles are located at

$$s = - 4. 2 \pm j 2, \quad s = - 1 2$$

Using these closed-loop poles, the denominator of $Y ( s ) / D ( s )$ becomes

$$s ^ {2} (s + 1) + 1 0 K (s + \alpha) (s + \beta) = (s + 4. 2 + j 2) (s + 4. 2 - j 2) (s + 1 2)$$

or

$$s ^ {3} + (1 + 1 0 K) s ^ {2} + 1 0 K (\alpha + \beta) s + 1 0 K \alpha \beta = s ^ {3} + 2 0. 4 s ^ {2} + 1 2 2. 4 4 s + 2 5 9. 6 8$$

![](image/0c112774729d9b674f8e5471239c7c0f22ba8dde37405491774571e43300b0a0.jpg)

<details>
<summary>line</summary>

| t (sec) | Output |
| --- | --- |
| 0.0 | 0.0 |
| 0.2 | 1.2 |
| 0.5 | 1.0 |
| 1.0 | 1.0 |
| 1.5 | 1.0 |
| 2.0 | 1.0 |
| 2.5 | 1.0 |
| 3.0 | 1.0 |
| 3.5 | 1.0 |
| 4.0 | 1.0 |
</details>

(a)

![](image/318915fcf10b6c5c7eb86d2db57e76169605968a0423d032deb82be1535add3a.jpg)

<details>
<summary>line</summary>

| t (sec) | Output |
| --- | --- |
| 0.0 | 0.0000 |
| 0.2 | 0.0650 |
| 0.4 | 0.0600 |
| 0.6 | 0.0450 |
| 0.8 | 0.0250 |
| 1.0 | 0.0100 |
| 1.2 | 0.0050 |
| 1.4 | 0.0020 |
| 1.6 | 0.0010 |
| 1.8 | 0.0005 |
| 2.0 | 0.0002 |
| 2.2 | 0.0001 |
| 2.4 | 0.0001 |
| 2.6 | 0.0001 |
| 2.8 | 0.0001 |
| 3.0 | 0.0001 |
| 3.2 | 0.0001 |
| 3.4 | 0.0001 |
| 3.6 | 0.0001 |
| 3.8 | 0.0001 |
| 4.0 | 0.0001 |
</details>

(b)   
Figure 8–35

(a) Response to unitstep reference input

(a=4.2, b=2, c=12);

(b) response to unit-step disturbance input

(a=4.2, b=2, c=12).

By equating the coefficients of equal powers of s on both sides of this last equation, we obtain

$$1 + 1 0 K = 2 0. 41 0 K (\alpha + \beta) = 1 2 2. 4 41 0 K \alpha \beta = 2 5 9. 6 8$$

Hence

$$K = 1. 9 4, \quad \alpha + \beta = \frac {1 2 2 . 4 4}{1 9 . 4}, \quad \alpha \beta = \frac {2 5 9 . 6 8}{1 9 . 4}$$

Then $G _ { c } ( s )$ can be written as

$$
\begin{array}{l} G _ {c} (s) = K \frac {(s + \alpha) (s + \beta)}{s} \\ = \frac {K [ s ^ {2} + (\alpha + \beta) s + \alpha \beta ]}{s} \\ = \frac {1 . 9 4 s ^ {2} + 1 2 . 2 4 4 s + 2 5 . 9 6 8}{s} \\ \end{array}
$$

The closed-loop transfer function $Y ( s ) / D ( s )$ becomes

$$
\begin{array}{l} \frac {Y (s)}{D (s)} = \frac {1 0}{s (s + 1) + 1 0 G _ {c}} \\ = \frac {1 0}{s (s + 1) + 1 0 \frac {1 . 9 4 s ^ {2} + 1 2 . 2 4 4 s + 2 5 . 9 6 8}{s}} \\ = \frac {1 0 s}{s ^ {3} + 2 0 . 4 s ^ {2} + 1 2 2 . 4 4 s + 2 5 9 . 6 8} \\ \end{array}
$$
