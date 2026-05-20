# Example 4.7

For $P(s) = (-s + 1) / [(-s + 2)(s + 3)]$ , design a $T(s)$ such that: (i) the interpolation conditions are satisfied; (ii) $T(0) = 1$ ; (iii) $T(s)$ has all its poles as multiple poles at $s = -a$ , $a > 0$ ; and (iv) the order of $T(s)$ is the least required to ensure a proper $F(s)$ . Calculate $F(s)$ .

Solution The pole excess of $P(s)$ is 1, so we might try

$$T (s) = \frac {k}{(s + a)}.$$

Clearly, this will not do: we can satisfy (ii) by setting $k = a$ , but we have no freedom left to satisfy $T(2) = 1$ and $T(1) = 0$ . Try

$$T (s) = \frac {k (s + b) (s - 1)}{(s + a) ^ {3}}$$

which incorporates the condition $T(1) = 0$ .

We must have

$$T (0) = \frac {- k b}{a ^ {3}} = - 1T (2) = \frac {k (2 + b) (+ 1)}{(2 + a) ^ {3}} = 1$$

so that

$$+ 2 k + k b = + 2 k - a ^ {3} = (2 + a) ^ {3}$$

or

$$k = a ^ {3} + 3 a ^ {2} + 6 a + 4b = \frac {- a ^ {3}}{a ^ {3} + 3 a ^ {2} + 6 a + 4}.$$

Then

$$
\begin{array}{l} S = 1 - T \\ = \frac {s ^ {3} + (3 a - k) s ^ {2} + (3 a ^ {2} + k - k b) s + a ^ {3} + k b}{(s + a) ^ {3}} \\ = \frac {s ^ {3} + (3 a - k) s ^ {2} + (3 a ^ {2} + k + a ^ {3}) s + a ^ {3} - a ^ {3}}{(s + a) ^ {3}} \\ = \frac {s ^ {3} - (a ^ {3} + 3 a ^ {2} + 3 a + 4) s ^ {2} + (2 a ^ {3} + 6 a ^ {2} + 6 a + 4) s}{(s + a) ^ {3}}. \\ \end{array}
$$

$S(s)$ has a zero at $s = 2$ and is factored as

$$S (s) = \frac {s (s - 2) (s - c)}{(s + a) ^ {3}}$$

where $c = a^3 + 3a^2 + 3a + 2$ .

![](image/93f4f4ae42cfe5b6c76d98266bf0b3596fa37a4e2b4aaaa46fb054160d1675f6.jpg)

![](image/2aa11c215bb3628690287962dc630a447b425d441d3b3df4520bc789a98fc4a5.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | Magnitude (dB) for a=0.5 | Magnitude (dB) for a=1 | Magnitude (dB) for a=5 |
| --- | --- | --- | --- |
| 0.1 | 16 | 5 | -10 |
| 1 | 22 | 17 | 10 |
| 10 | 5 | 0 | 24 |
| 100 | 0 | 0 | 8 |
</details>

Figure 4.19 Sensitivity and complementary sensitivity

The controller is

$$
\begin{array}{l} F (s) = \frac {T}{P S} = \frac {k (s + b) (s - 1)}{s (s - c) (s - 2)} \frac {(s - 2) (s + 3)}{(s - 1)} \\ = \frac {k (s + b) (s + 3)}{s (s - c)} \\ \end{array}
$$

where

$$k = a ^ {3} + 3 a ^ {2} + 6 a + 4b = \frac {- a ^ {3}}{k}c = a ^ {3} + 3 a ^ {2} + 3 a + 2.$$

Figure 4.19 shows the magnitude of $S(j\omega)$ and $T(j\omega)$ for $a = 0.5, 1,$ and 5. Obviously, the performance is quite poor. We shall soon see why this plant is so difficult to control.
