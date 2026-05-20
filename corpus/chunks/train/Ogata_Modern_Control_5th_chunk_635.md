$$1 + G _ {c 1} (s) G _ {p} (s) = 1 + \frac {K (s + a) ^ {2}}{s} \frac {1 0 0}{s (s + 1)}$$

Notice that the open-loop poles are located at s=0 (a double pole) and s=–1. The zeros are located at s=–a (a double zero).

In what follows, we shall use the root-locus approach to determine the values of a and K. Let us choose the dominant closed-loop poles at $s = - 5 \pm j 5$ . Then, the angle deficiency at the desired closed-loop pole at $s = - 5 + j 5$ is

$$- 1 3 5 ^ {\circ} - 1 3 5 ^ {\circ} - 1 2 8. 6 6 ^ {\circ} + 1 8 0 ^ {\circ} = - 2 1 8. 6 6 ^ {\circ}$$

The double zero at s=–a must contribute 218.66°. (Each zero must contribute 109.33°.) By a simple calculation, we find

$$a = - 3. 2 4 6 0$$

The controller $G _ { c 1 } ( s )$ is then determined as

$$G _ {c 1} (s) = \frac {K (s + 3 . 2 4 6 0) ^ {2}}{s}$$

The constant K must be determined by use of the magnitude condition. This condition is

$$\left| G _ {c 1} (s) G _ {p} (s) \right| _ {s = - 5 + j 5} = 1$$

Since

$$G _ {c 1} (s) G _ {p} (s) = \frac {K (s + 3 . 2 4 6 0) ^ {2}}{s} \frac {1 0 0}{s (s + 1)}$$

we obtain

$$K = \left| \frac {s ^ {2} (s + 1)}{1 0 0 (s + 3 . 2 4 6 0) ^ {2}} \right| _ {s = - 5 + j 5}= 0. 1 1 4 0 3$$

The controller $G _ { c 1 } ( s )$ thus becomes

$$
\begin{array}{l} G _ {c 1} (s) = \frac {0 . 1 1 4 0 3 (s + 3 . 2 4 6 0) ^ {2}}{s} \\ = \frac {0 . 1 1 4 0 3 s ^ {2} + 0 . 7 4 0 2 8 s + 1 . 2 0 1 4 8}{s} \\ = 0. 7 4 0 2 8 + \frac {1 . 2 0 1 4 8}{s} + 0. 1 1 4 0 3 s \tag {8-17} \\ \end{array}
$$

Then, the closed-loop transfer function $Y ( s ) / D ( s )$ is obtained as follows:

$$
\begin{array}{l} \frac {Y (s)}{D (s)} = \frac {G _ {p} (s)}{1 + G _ {c 1} (s) G _ {p} (s)} \\ = \frac {\frac {1 0 0}{s (s + 1)}}{1 + \frac {0 . 1 1 4 0 3 (s + 3 . 2 4 6 0) ^ {2}}{s} \frac {1 0 0}{s (s + 1)}} \\ = \frac {1 0 0 s}{s ^ {3} + 1 2 . 4 0 3 s ^ {2} + 7 4 . 0 2 8 s + 1 2 0 . 1 4 8} \\ \end{array}
$$

The response curve when $D ( s )$ is a unit-step disturbance is shown in Figure 8–67.

![](image/57e794d4f3bb8408268dc105a696be6e15785f6d82f28d89274ffda1bc51faeb.jpg)

<details>
<summary>line</summary>

| t (sec) | y_d(t) |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 1.2 |
| 1.0 | 0.4 |
| 1.5 | 0.1 |
| 2.0 | 0.05 |
| 2.5 | 0.01 |
| 3.0 | 0.0 |
| 3.5 | 0.0 |
| 4.0 | 0.0 |
</details>

Figure 8–67 Response to unitstep disturbance input.

Next, we consider the responses to reference inputs. The closed-loop transfer function $Y ( s ) / R ( s )$ is

$$\frac {Y (s)}{R (s)} = \frac {\left[ G _ {c 1} (s) + G _ {c 2} (s) \right] G _ {p} (s)}{1 + G _ {c 1} (s) G _ {p} (s)}$$

Let us define

$$G _ {c 1} (s) + G _ {c 2} (s) = G _ {c} (s)$$

Then
