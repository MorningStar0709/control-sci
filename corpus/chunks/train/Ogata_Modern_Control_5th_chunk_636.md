$$
\begin{array}{l} \frac {Y (s)}{R (s)} = \frac {G _ {c} (s) G _ {p} (s)}{1 + G _ {c 1} (s) G _ {p} (s)} \\ = \frac {1 0 0 s G _ {c} (s)}{s ^ {3} + 1 2 . 4 0 3 s ^ {2} + 7 4 . 0 2 8 s + 1 2 0 . 1 4 8} \\ \end{array}
$$

To satisfy the requirements on the responses to the ramp reference input and acceleration reference input, we use the zero-placement approach. That is, we choose the numerator of $Y ( s ) / R ( s )$ to be the sum of the last three terms of the denominator, or

$$1 0 0 s G _ {c} (s) = 1 2. 4 0 3 s ^ {2} + 7 4. 0 2 8 s + 1 2 0. 1 4 8$$

from which we get

$$
\begin{array}{l} G _ {c} (s) = \frac {0 . 1 2 4 0 3 s ^ {2} + 0 . 7 4 0 2 8 s + 1 . 2 0 1 4 8}{s} \\ = 0. 7 4 0 2 8 + \frac {1 . 2 0 1 4 8}{s} + 0. 1 2 4 0 3 s \tag {8-18} \\ \end{array}
$$

Hence, the closed-loop transfer function $Y ( s ) / R ( s )$ becomes as

$$\frac {Y (s)}{R (s)} = \frac {1 2 . 4 0 3 s ^ {2} + 7 4 . 0 2 8 s + 1 2 0 . 1 4 8}{s ^ {3} + 1 2 . 4 0 3 s ^ {2} + 7 4 . 0 2 8 s + 1 2 0 . 1 4 8}$$

The response curves to the unit-step reference input, unit-ramp reference input, and unitacceleration reference input are shown in Figures $8 \mathrm { - } 6 8 ( \mathrm { a } )$ , (b), and (c), respectively.The maximum

![](image/2710a3020e9ebfb049f9791d6f81b4bf4195b5811e9fc639640731a317d7dae4.jpg)

<details>
<summary>line</summary>

| t (sec) | y_r(t) |
| --- | --- |
| 0.0 | 0.0 |
| 0.2 | 1.25 |
| 0.5 | 1.0 |
| 1.0 | 0.98 |
| 1.5 | 1.0 |
| 2.0 | 1.0 |
| 2.5 | 1.0 |
| 3.0 | 1.0 |
</details>

(a)   
Figure 8–68   
(a) Response to unitstep reference input; (b) response to unitramp reference input; (c) response to unit-acceleration reference input.

![](image/b8701994d638d9560e4d9632789901ba0eb0f2066cd3c9ed410ae579eb26722d.jpg)

<details>
<summary>line</summary>

| t (sec) | y_r(t) |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.5 |
| 1.0 | 1.0 |
| 1.5 | 1.5 |
| 2.0 | 2.0 |
| 2.5 | 2.5 |
| 3.0 | 3.0 |
</details>

(b)

![](image/a01c32a3f281371a2c46f05c42c16ed4bec400a19815a0df47165e558cc9f8af.jpg)

<details>
<summary>line</summary>

| t (sec) | y_r(t) |
| --- | --- |
| 0.0 | 0.0 |
| 0.4 | 0.1 |
| 0.6 | 0.2 |
| 1.0 | 0.5 |
| 1.4 | 1.0 |
| 1.8 | 1.6 |
| 2.0 | 2.0 |
</details>

(c)   
Figure 8–68 (continued)

overshoot in the unit-step response is approximately 25% and the settling time is approximately 1.2 sec. The steady-state errors in the ramp response and acceleration response are zero. Therefore, the designed controller given by Equation (8–18) is satisfactory.Gc(s)

Finally, we determine $G _ { c 2 } ( s )$ Noting that.

$$G _ {c 2} (s) = G _ {c} (s) - G _ {c 1} (s)$$
