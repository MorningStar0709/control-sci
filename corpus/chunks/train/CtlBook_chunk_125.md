# Example 5.1

Find the poles of the transfer function and use the partial fraction expansion and the computer to evaluate the step response output, Y (s).

$$G (s) = \frac {Y (s)}{X (s)} = \frac {1}{(s ^ {2} + 1 3 s + 3 0)}$$

By either simple factoring or use of the quadratic formula,

$$G (s) = \frac {1}{(s + 3) (s + 1 0)}$$

Thus the poles of G(s) are s = {−3, −10}. To add a step input to the system, we multiply by

$$U (s) = 1 / s$$

giving the output Y (s):

$$Y (s) = U (s) G (s) = \frac {1}{s (s + 3) (s + 1 0)}$$

The partial fraction expansion is

$$G (s) = A _ {1} / s + A _ {2} / (s + 3) + A _ {3} / (s + 1 0)$$

Solving for A1, A2, A3,

$$A _ {1} = 1 / 3 0 \quad A _ {2} = - 1 / 2 1 \quad A _ {3} = 1 / 7 0$$

Applying the inverse transforms for $\textstyle { \frac { 1 } { s } }$ and $\frac { A } { ( s + a ) }$ ,

$$g (t) = 0. 0 3 3 3 u (t) - 0. 0 4 7 6 e ^ {- 3 t} + 0. 0 1 4 3 e ^ {- 1 0 t}$$

Plotting the function g(t) by computer (Left):

![](image/2fa79049c37a14815401e356f9321e64a05d3ef26777af5507a6c3e2121ff402.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0.0 | 0.0000 |
| 0.5 | 0.0250 |
| 1.0 | 0.0300 |
| 1.5 | 0.0330 |
| 2.0 | 0.0340 |
| 2.5 | 0.0345 |
| 3.0 | 0.0348 |
| 3.5 | 0.0349 |
| 4.0 | 0.0350 |
</details>

![](image/446603468cda1700ad8f8e8bfbf5bb97fafbe7c1a3042583d17f542f1eed828b.jpg)

<details>
<summary>line</summary>

| t | u(t)/30 | Full Step Response, g(t) | -1/70e^-(-10t) | -1/21e^-(-3t) |
| --- | --- | --- | --- | --- |
| 0.0 | 0.03 | 0.01 | 0.01 | -0.05 |
| 0.2 | 0.03 | 0.015 | 0.005 | -0.03 |
| 0.4 | 0.03 | 0.02 | 0.00 | -0.01 |
| 0.6 | 0.03 | 0.025 | 0.00 | 0.0 |
| 0.8 | 0.03 | 0.03 | 0.00 | 0.0 |
| 1.0 | 0.03 | 0.03 | 0.00 | 0.0 |
| 1.2 | 0.03 | 0.03 | 0.00 | 0.0 |
| 1.4 | 0.03 | 0.03 | 0.00 | 0.0 |
| 1.6 | 0.03 | 0.03 | 0.00 | 0.0 |
| 1.8 | 0.03 | 0.03 | 0.00 | 0.0 |
| 2.0 | 0.03 | 0.03 | 0.00 | 0.0 |
</details>

Note that g(t) has three components, $0 . 0 3 3 3 u ( t ) , \ - 0 . 0 4 7 6 e ^ { - 3 t } , \ + 0 . 0 1 4 3 e ^ { - 1 0 t }$ . Plotting them separately (Right), we see how they combine to create the response
