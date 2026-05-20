# Example 5.14

Draw the Bode Asymptotic Phase Plot for the system of Example 513, G4(s) = (s+0.1)(s+2)(s+25) $\begin{array} { r } { G _ { 4 } ( s ) = \frac { ( s + 0 . 1 ) } { ( s + 2 ) ( s + 2 5 ) } } \end{array}$

For $\omega < 0 . 1$ the two poles and zero each contributes 0◦. The zero will begin rst and contribute $+ 9 0 ^ { \circ }$ , then, as ω increases, the poles will each contribute $- 9 0 ^ { \circ }$ . Starting from the left at $\phi = 0 ^ { \circ }$ , and drawing only the step function asymptotes,

![](image/fa69723019ab877b9a3fb8dd3ff458d44908c2a610e56e2cb541ec2b13ef860d.jpg)

<details>
<summary>line</summary>

| log(w) | ∠G(jω) |
| --- | --- |
| 0.1 | 90° |
| 1 | 45° |
| 2 | 90° |
| 25 | -45° |
| 100 | -90° |
| 1000 | -90° |
| (end) | -90° |
</details>

Adding in the linear approximations   
![](image/85dbf18772fa3ab0d38f20bc40574b2903ffebd61b9091cbfe6db0b40870e7d9.jpg)

<details>
<summary>line</summary>

| log(ω) | ∠G(jω) |
| --- | --- |
| 0.1 | 45° |
| 1 | 90° |
| 2 | 45° |
| 25 | -45° |
</details>

and nally, using a bit of artistic license, the smooth curves can be drawn in:   
![](image/e4863bc2031e8355e26029892f04854bb94befdf85cb368e6551d504f566de15.jpg)

<details>
<summary>line</summary>

| log(ω) | ∠G(jω) |
| --- | --- |
| 0 | 0 |
| 0.1 | 45 |
| 1 | 90 |
| 2 | 45 |
| 10 | -45 |
| 25 | -90 |
| 100 | -90 |
| 1000 | -90 |
</details>

![](image/f58bb49ea972d8051ac5a745f0922ccbdd243eb9696a66c9454a78b5d49a373f.jpg)

<details>
<summary>line</summary>

| Parameter | Value |
| --- | --- |
| G(s) | 1/s² |
| s⁻¹ | +20 dB |
| d⁻¹ | 1/s² |
| s⁴ | 40 dB / dec |
| G(s) | 1/s² |
| s | 20 dB / dec |
| π | s² |
| π/2 | s |
| 0° | log(w) |
| -π/2 | 1/s |
| -π | 1/s² |
</details>

Figure 5.7: Bode Magnitude and Phase Plots of $G ( s ) = s ^ { n }$ . Left: The magnitude plots all pass through the point {1, 0}. Right: Each term of $s ^ { n }$ contributes $n \times 9 0 ^ { \circ }$ .
