$$\underline {{{s}}} = \underline {{{s + 1}}} = 1 8 0 ^ {\circ}, \quad \underline {{{s + 2}}} = 0 ^ {\circ}$$

and

$$- \underline {{s}} - \underline {{s + 1}} - \underline {{s + 2}} = - 3 6 0 ^ {\circ}$$

Figure 6–3 Control system.   
![](image/574acf71f741a813e97878898fac4e1d9e9904cfb6b948bd0a5899479c1f7433.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["K/(s(s+1)(s+2))"]
    C --> D["C(s)"]
    D --> E["Feedback"]
    E --> B
```
</details>

It can be seen that the angle condition is not satisfied. Therefore, the negative real axis from –1 to –2 is not a part of the root locus. Similarly, if a test point is located on the negative real axis from –2 to –q, the angle condition is satisfied. Thus, root loci exist on the negative real axis between 0 and –1 and between –2 and –q.

2. Determine the asymptotes of the root loci. The asymptotes of the root loci as s approaches infinity can be determined as follows: If a test point s is selected very far from the origin, then

$$\lim _ {s \rightarrow \infty} G (s) = \lim _ {s \rightarrow \infty} \frac {K}{s (s + 1) (s + 2)} = \lim _ {s \rightarrow \infty} \frac {K}{s ^ {3}}$$

and the angle condition becomes

$$- 3 \underline {{s}} = \pm 1 8 0 ^ {\circ} (2 k + 1) \quad (k = 0, 1, 2, \dots)$$

or

$$\text { Angles of asymptotes } = \frac {\pm 1 8 0 ^ {\circ} (2 k + 1)}{3} \quad (k = 0, 1, 2, \dots)$$

Since the angle repeats itself as k is varied, the distinct angles for the asymptotes are determined as $6 0 ^ { \circ } , - 6 0 ^ { \circ }$ , and 180°. Thus, there are three asymptotes. The one having the angle of 180° is the negative real axis.

Before we can draw these asymptotes in the complex plane, we must find the point where they intersect the real axis. Since

$$G (s) = \frac {K}{s (s + 1) (s + 2)}$$

if a test point is located very far from the origin, then G(s) may be written as

$$G (s) = \frac {K}{s ^ {3} + 3 s ^ {2} + \cdots}$$

For large values of s, this last equation may be approximated by

$$G (s) \div \frac {K}{(s + 1) ^ {3}} \tag {6-5}$$

A root-locus diagram of G(s) given by Equation (6–5) consists of three straight lines. This can be seen as follows: The equation of the root locus is

$$\left\lfloor \frac {K}{(s + 1) ^ {3}} = \pm 1 8 0 ^ {\circ} (2 k + 1) \right.$$

or

$$- 3 \underline {{\text { s+1 }}} = \pm 1 8 0 ^ {\circ} (2 k + 1)$$

which can be written as

$$\underline {{s + 1}} = \pm 6 0 ^ {\circ} (2 k + 1)$$

By substituting s=s+jv into this last equation, we obtain
