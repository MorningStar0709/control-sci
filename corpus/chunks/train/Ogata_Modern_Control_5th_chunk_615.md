$$
\begin{array}{l} \frac {Y (s)}{R (s)} = \frac {\left(G _ {c 1} + G _ {c 2}\right) G _ {p}}{1 + G _ {c 1} G _ {p}} \\ = \frac {\left[ \frac {1 . 3 2 1 s ^ {2} + 9 . 5 2 6 s + 1 7 . 1 7 3 5}{s} + \hat {K} _ {p} (1 + \hat {T} _ {d} s) \right] \frac {5}{(s + 1) (s + 5)}}{1 + \frac {1 . 3 2 1 s ^ {2} + 9 . 5 2 6 s + 1 7 . 1 7 3 5}{s} \frac {5}{(s + 1) (s + 5)}} \\ = \frac {(6 . 6 0 5 1 + 5 \hat {K} _ {p} \hat {T} _ {d}) s ^ {2} + (4 7 . 6 3 + 5 \hat {K} _ {p}) s + 8 5 . 8 6 7 3}{s ^ {3} + 1 2 . 6 0 5 1 s ^ {2} + 5 2 . 6 3 s + 8 5 . 8 6 7 3} \\ \end{array}
$$

Zero placement. We place two zeros together with the dc gain constant such that the numerator is the same as the sum of the last three terms of the denominator. That is,

$$(6. 6 0 5 1 + 5 \hat {K} _ {p} \hat {T} _ {d}) s ^ {2} + (4 7. 6 3 + 5 \hat {K} _ {p}) s + 8 5. 8 6 7 3 = 1 2. 6 0 5 1 s ^ {2} + 5 2. 6 3 s + 8 5. 8 6 7 3$$

By equating the coefficients of $s ^ { 2 }$ terms and s terms on both sides of this last equation,

$$6. 6 0 5 1 + 5 \hat {K} _ {p} \hat {T} _ {d} = 1 2. 6 0 5 14 7. 6 3 + 5 \hat {K} _ {p} = 5 2. 6 3$$

from which we get

$$\hat {K} _ {p} = 1, \quad \hat {T} _ {d} = 1. 2$$

Therefore,

$$G _ {c 2} (s) = 1 + 1. 2 s \tag {8-13}$$

![](image/37cc5c8c7e174c1c3a56de948760fe7fcc3ec3eedf7aad29f66e010b8944ae3b.jpg)

<details>
<summary>line</summary>

| t (sec) | y₀(t) |
| --- | --- |
| 0.0 | 0.0000 |
| 0.5 | 0.0750 |
| 1.0 | 0.0300 |
| 1.5 | 0.0050 |
| 2.0 | 0.0000 |
| 2.5 | 0.0000 |
| 3.0 | 0.0000 |
</details>

Figure 8–42 Response to unitstep disturbance input.

With this controller $G _ { c 2 } ( s )$ the closed-loop transfer function, $Y ( s ) / R ( s )$ becomes

$$\frac {Y (s)}{R (s)} = \frac {1 2 . 6 0 5 1 s ^ {2} + 5 2 . 6 3 s + 8 5 . 8 6 7 3}{s ^ {3} + 1 2 . 6 0 5 1 s ^ {2} + 5 2 . 6 3 s + 8 5 . 8 6 7 3}$$

The response to the unit-step reference input becomes as shown in Figure 8–43(a).

![](image/04b769a7485c41225c431243841214d5718ab8b89840ff824d25a0f8b47a1154.jpg)

<details>
<summary>line</summary>

| t (sec) | y_r(t) |
| --- | --- |
| 0.0 | 0.0 |
| 0.2 | 1.2 |
| 0.4 | 1.15 |
| 0.6 | 1.05 |
| 0.8 | 0.98 |
| 1.0 | 0.97 |
| 1.2 | 0.98 |
| 1.4 | 0.99 |
| 1.6 | 0.995 |
| 1.8 | 1.0 |
| 2.0 | 1.0 |
</details>

![](image/9bc2fdf45eec71f78c8aaac56365744eba5471f6c4cf7e37a52cf8281fa99b91.jpg)

<details>
<summary>line</summary>

| t (sec) | y_r(t) |
| --- | --- |
| 0.0 | 0.0 |
| 0.2 | 0.2 |
| 0.4 | 0.4 |
| 0.6 | 0.6 |
| 0.8 | 0.8 |
| 1.0 | 1.0 |
| 1.2 | 1.2 |
| 1.4 | 1.4 |
| 1.6 | 1.6 |
| 1.8 | 1.8 |
| 2.0 | 2.0 |
</details>

Figure 8–43   
(a) Response to unitstep reference input; (b) response to unitramp reference input; (c) response to unit-acceleration reference input.
