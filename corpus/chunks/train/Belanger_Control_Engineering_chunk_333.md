# Lag Compensation: Root Locus Viewpoint

As shown by Equation 6.28, the lag compensator is of the form

$$G _ {c} (s) = k \frac {\alpha T s + 1}{T s + 1}, \quad \alpha = 1 / (1 + k _ {1}) < 1.$$

When $G_{c}(s)$ is cascaded with the plant, the loop gain $L(s)$ acquires a real pole at -1/T and a real zero at $-1/\alpha T$ . Now T is relatively large compared to the plant time constants, because the lag is meant to act at frequencies well below the plant bandwidth. This means that the pole-zero pair introduced by $G_{c}$ will be relatively close to the origin.

Figure 6.21 shows the pole-zero pair and a piece of the root locus before the introduction of the lag compensator. Let $s^*$ be a point on the original locus for the plant $P(s)$ , and suppose that it is a closed-loop pole for some gain $k^*$ . Then, by Root Locus definitions,

$$\neq P (s ^ {*}) = 1 8 0 ^ {\circ} \tag {6.31}k ^ {*} = - \frac {1}{P (s ^ {*})}. \tag {6.32}$$

![](image/cce562a6628a254c16d1e1ca10e000d3850d0e18f5392c26bdb2177405621c47.jpg)

<details>
<summary>line</summary>

| Time (s) | Angle (rad) |
| --- | --- |
| 0 | 0 |
| 1 | 0.017 |
| 2 | 0.031 |
| 3 | 0.032 |
| 4 | 0.031 |
| 5 | 0.031 |
| 6 | 0.031 |
| 7 | 0.031 |
| 8 | 0.031 |
</details>

![](image/d816e0ed377f924d4651052bd59e8dae6e9eda7572ff516122ab84166ae3267e.jpg)

<details>
<summary>line</summary>

| Time (s) | Angle (rad) |
| --- | --- |
| 0 | 0.0000 |
| 2 | 0.0300 |
| 4 | 0.0250 |
| 6 | 0.0200 |
| 8 | 0.0175 |
| 10 | 0.0150 |
| 12 | 0.0135 |
| 14 | 0.0125 |
| 16 | 0.0115 |
| 18 | 0.0105 |
| 20 | 0.0100 |
</details>

Figure 6.19 Disturbance response, pure gain, and lag compensation, dc servo

![](image/cd1ae2566c1c08820aa1703f31d69b6053ab4adf7e760b75534f0ad0060bac42.jpg)

<details>
<summary>line</summary>

| Time (s) | Angle (rad) |
| --- | --- |
| 0 | 0 |
| 2 | 1.1 |
| 4 | 1.05 |
| 6 | 1.03 |
| 8 | 1.02 |
| 10 | 1.01 |
| 12 | 1.01 |
| 14 | 1.01 |
| 16 | 1.01 |
| 18 | 1.01 |
| 20 | 1.01 |
</details>

Figure 6.20 Set-point step response, dc servo

![](image/bf7443be160857169fcdcb1b95c08872bb7f04ffa42ba0944be423ff514d4954.jpg)

<details>
<summary>text_image</summary>

s*
θp
θt
-1/αT -1/T
</details>

Figure 6.21 Root locus view of lag compensation

With the compensator in place, $s^{*}$ will be a point on the new Root Locus if

$$\neq G _ {c} (s ^ {*}) P (s ^ {*}) = \neq G _ {c} (s ^ {*}) + \neq P (s ^ {*}) = 1 8 0 ^ {\circ}$$

or, since

$$\neq P (s ^ {*}) = 1 8 0 ^ {\circ},\neq G _ {c} (s ^ {*}) = 0. \tag {6.33}$$

But, from Figure 6.21,

$$\not \prec G _ {c} (s ^ {*}) = \theta_ {z} - \theta_ {p}.$$
