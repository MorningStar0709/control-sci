Design Step 1: We design $G _ { c } ( s )$ to satisfy the requirements on the response to the stepdisturbance input $D ( s )$ . In this design stage, we assume that the reference input is zero.

Suppose that we assume that $G _ { c } ( s )$ is a PID controller of the form

$$G _ {c} (s) = \frac {K (s + \alpha) (s + \beta)}{s}$$

Then the closed-loop transfer function $Y ( s ) / D ( s )$ becomes

$$
\begin{array}{l} \frac {Y (s)}{D (s)} = \frac {1 0}{s (s + 1) + 1 0 G _ {c}} \\ = \frac {1 0}{s (s + 1) + \frac {1 0 K (s + \alpha) (s + \beta)}{s}} \\ = \frac {1 0 s}{s ^ {2} (s + 1) + 1 0 K (s + \alpha) (s + \beta)} \\ \end{array}
$$

Note that the presence of $" s \mathrm { \Delta }$ in the numerator of $Y ( s ) / D ( s )$ assures that the steady-state response to the step disturbance input is zero.

Let us assume that the desired dominant closed-loop poles are complex conjugates and are given by

$$s = - a \pm j b$$

and the remaining closed-loop pole is real and is located at

$$s = - c$$

Note that in this problem there are three requirements. The first requirement is that the response to the step disturbance input damp out quickly.The second requirement is that the maximum overshoot in the response to the unit-step reference input be between 19% and 2% and the settling time be less than 1 sec. The third requirement is that the steady-state errors in the responses to both the ramp and acceleration reference inputs be zero.

A set (or sets) of reasonable values of a, b, and c must be searched using a computational approach. To satisfy the first requirement, we choose the search region for a, b, and c to be

$$2 \leq a \leq 6, \quad 2 \leq b \leq 6, \quad 6 \leq c \leq 1 2$$

This region is shown in Figure 8–34. If the dominant closed-loop poles $s = - a \pm j b$ are located anywhere in the shaded region, the response to a step disturbance input will damp out quickly. (The first requirement will be met.)

Notice that the denominator of $Y ( s ) / D ( s )$ can be written as

$$
\begin{array}{l} s ^ {2} (s + 1) + 1 0 K (s + \alpha) (s + \beta) \\ = s ^ {3} + (1 + 1 0 K) s ^ {2} + 1 0 K (\alpha + \beta) s + 1 0 K \alpha \beta \\ = (s + a + j b) (s + a - j b) (s + c) \\ = s ^ {3} + (2 a + c) s ^ {2} + \left(a ^ {2} + b ^ {2} + 2 a c\right) s + \left(a ^ {2} + b ^ {2}\right) c \\ \end{array}
$$

![](image/bfc296e4bc417b6c5ffe9d711e5ca284494a144577ba0b0325b8133541fb2f46.jpg)

<details>
<summary>scatter</summary>

| Region | σ Range | jω Range |
| --- | --- | --- |
| a | -10 to -2 | -j6 to j6 |
| c | -10 to -2 | -j2 to -j6 |
</details>

Figure 8–34   
Search regions for a, b, and c.
