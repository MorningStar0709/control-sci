Solving this equation for the smallest positive value of v, we obtain

$$\omega = 2. 4 4 8 2$$

Substituting $\omega = 2 . 4 4 8 2$ into $G ( j \omega )$ , we obtain

$$G (j 2. 4 4 8 2) = \frac {K}{1 + 2 . 4 4 8 2 ^ {2}} (\cos 1. 9 5 8 6 - 2. 4 4 8 2 \sin 1. 9 5 8 6) = - 0. 3 7 8 K$$

The critical value of K for stability is obtained by letting $G ( j 2 . 4 4 8 2 )$ equal –1. Hence,

$$0. 3 7 8 K = 1$$

or

$$K = 2. 6 5$$

Figure 7–126 shows the Nyquist or polar plots of $2 . 6 5 e ^ { - 0 . 8 j \omega } / ( 1 + j \omega )$ and $2 . 6 5 / ( 1 + j \omega )$ . The firstorder system without transport lag is stable for all values of K, but the one with a transport lag of 0.8 sec becomes unstable for $K > 2 . 6 5$ .

![](image/8b5b3f26aea85e72848040824d23744fd55c11ae648a9bbc39047ca619cbc7eb.jpg)

<details>
<summary>other</summary>

| Point Label | Re | Im |
| --- | --- | --- |
| ω = 2.45 | -1 | 1 |
| ω = 2 | 0 | 1 |
| ω = 1.5 | 1 | 1 |
| ω = 1 | 2 | 1 |
| ω = 0.5 | 3 | 1 |
| Point 1 | 4 | 1 |
| Point 2 | 6 | 1 |
| Point 3 | 8 | 1 |
| Point 4 | 10 | 1 |
| Point 5 | 12 | 1 |
| Point 6 | 14 | 1 |
| Point 7 | 16 | 1 |
| Point 8 | 18 | 1 |
| Point 9 | 20 | 1 |
| Point 10 | 22 | 1 |
| Point 11 | 24 | 1 |
| Point 12 | 26 | 1 |
| Point 13 | 28 | 1 |
| Point 14 | 30 | 1 |
| Point 15 | 32 | 1 |
| Point 16 | 34 | 1 |
| Point 17 | 36 | 1 |
| Point 18 | 38 | 1 |
| Point 19 | 40 | 1 |
| Point 20 | 42 | 1 |
| Point 21 | 44 | 1 |
| Point 22 | 46 | 1 |
| Point 23 | 48 | 1 |
| Point 24 | 50 | 1 |
| Point 25 | 52 | 1 |
| Point 26 | 54 | 1 |
| Point 27 | 56 | 1 |
| Point 28 | 58 | 1 |
| Point 29 | 60 | 1 |
| Point 30 | 62 | 1 |
| Point 31 | 64 | 1 |
| Point 32 | 66 | 1 |
| Point 33 | 68 | 1 |
| Point 34 | 70 | 1 |
| Point 35 | 72 | 1 |
| Point 36 | 74 | 1 |
| Point 37 | 76 | 1 |
| Point 38 | 78 | 1 |
| Point 39 | 80 | 1 |
| Point 40 | 82 | 1 |
| Point 41 | 84 | 1 |
| Point 42 | 86 | 1 |
| Point 43 | 88 | 1 |
| Point 44 | 90 | 1 |
| Point 45 | 92 | 1 |
| Point 46 | 94 | 1 |
| Point 47 | 96 | 1 |
| Point 48 | 98 | 1 |
| Point 49 | 100 | 1 |
| Point 50 | - | -0.5 |
The chart displays a closed loop in the complex plane defined by the equation y = (2.65/(1 + jω)). The x-axis is labeled 'Re' and the y-axis is labeled 'Im'. The points are labeled with their respective ω values. There is no additional data series present in this image.
</details>

Figure 7–126

Polar plots of

$$2. 6 5 e ^ {- 0. 8 j \omega} / (1 + j \omega)$$

and $2 . 6 5 / ( 1 + j \omega )$ .

A–7–11. Consider a unity-feedback system with the following open-loop transfer function:

$$G (s) = \frac {2 0 \left(s ^ {2} + s + 0 . 5\right)}{s (s + 1) (s + 1 0)}$$

Draw a Nyquist plot with MATLAB and examine the stability of the closed-loop system.
