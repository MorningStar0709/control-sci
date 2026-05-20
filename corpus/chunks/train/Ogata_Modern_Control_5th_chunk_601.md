$$
\begin{array}{l} \frac {Y (s)}{D (s)} = \frac {G _ {p}}{1 + \left(G _ {c 1} + G _ {c 2}\right) G _ {p}} = \frac {K \frac {A (s)}{B (s)}}{1 + \frac {\alpha s + \beta + \gamma s ^ {2}}{s} \frac {K}{B (s)}} \\ = \frac {s K A (s)}{s B (s) + (\alpha s + \beta + \gamma s ^ {2}) K} \\ \end{array}
$$

Because of the presence of s in the numerator, the response $y ( t )$ to a step disturbance input approaches zero as t approaches infinity, as shown below. Since

$$Y (s) = \frac {s K A (s)}{s B (s) + (\alpha s + \beta + \gamma s ^ {2}) K} D (s)$$

if the disturbance input is a step function of magnitude d, or

$$D (s) = \frac {d}{s}$$

and assuming the system is stable, then

$$
\begin{array}{l} y (\infty) = \lim _ {s \rightarrow 0} s \left[ \frac {s K A (s)}{s B (s) + (\alpha s + \beta + \gamma s ^ {2}) K} \right] \frac {d}{s} \\ = \lim _ {s \rightarrow 0} \frac {s K A (0) d}{s B (0) + \beta K} \\ = 0 \\ \end{array}
$$

Figure 8–32 Typical response curve to a step disturbance input.   
![](image/0555e3c685dca127cf96d628a16fad67b3b5424713149f67e662f357cad7f441.jpg)

<details>
<summary>line</summary>

| t | y |
| --- | --- |
| 0 | 0 |
| >0 | Peak |
</details>

The response $y ( t )$ to a step disturbance input will have the general form shown in Figure 8–32.

Note that $Y ( s ) / R ( s )$ and $Y ( s ) / D ( s )$ are given by

$$\frac {Y (s)}{R (s)} = \frac {G _ {c 1} G _ {p}}{1 + \left(G _ {c 1} + G _ {c 2}\right) G _ {p}}, \quad \frac {Y (s)}{D (s)} = \frac {G _ {p}}{1 + \left(G _ {c 1} + G _ {c 2}\right) G _ {p}}$$

Notice that the denominators of $Y ( s ) / R ( s )$ and $Y ( s ) / D ( s )$ are the same. Before we choose the poles of $Y ( s ) / R ( s )$ , we need to place the zeros of $Y ( s ) / R ( s )$ .

Zero Placement. Consider the system

$$\frac {Y (s)}{R (s)} = \frac {p (s)}{s ^ {n + 1} + a _ {n} s ^ {n} + a _ {n - 1} s ^ {n - 1} + \cdots + a _ {2} s ^ {2} + a _ {1} s + a _ {0}}$$

If we choose $p ( s )$ as

$$p (s) = a _ {2} s ^ {2} + a _ {1} s + a _ {0} = a _ {2} \left(s + s _ {1}\right) \left(s + s _ {2}\right)$$

that is, choose the zeros $s = - s _ { 1 }$ and $s = - s _ { 2 }$ such that, together with $_ { a _ { 2 } , }$ , the numerator polynomial $p ( s )$ is equal to the sum of the last three terms of the denominator polynomial—then the system will exhibit no steady-state errors in response to the step input, ramp input, and acceleration input.

Requirement Placed on System Response Characteristics. Suppose that it is desired that the maximum overshoot in the response to the unit-step reference input be between arbitrarily selected upper and lower limits—for example,

$$2 \% < \text { maximum overshoot } < 10 \%$$
