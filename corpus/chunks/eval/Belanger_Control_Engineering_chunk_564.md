$$
\widehat {\mathbf {x}} (k) = \widehat {\mathbf {x}} (k - 1) + \frac {T _ {s}}{2} A \widehat {\mathbf {x}} (k) + \frac {T _ {s}}{2} A \widehat {\mathbf {x}} (k - 1) + \frac {T _ {s}}{2} B \widehat {\mathbf {e}} (k) + \frac {T _ {s}}{2} B \widehat {\mathbf {e}} (k - 1)
\begin{array}{l} \widehat {\mathbf {x}} (k) = \left(I - \frac {T _ {s}}{2} A\right) ^ {- 1} \left(I + \frac {T _ {s}}{2} A\right) \widehat {\mathbf {x}} (k - 1) + \left(I - \frac {T _ {s}}{2} A\right) ^ {- 1} \frac {T _ {s}}{2} B \widehat {\mathbf {e}} (k) \\ + \left(I - \frac {T _ {s}}{2} A\right) ^ {- 1} \frac {T _ {s}}{2} B \widehat {\mathbf {e}} (k - 1) \\ \end{array}
\widehat {\mathbf {u}} (k) = C \widehat {\mathbf {x}} (k) + D \widehat {\mathbf {e}} (k). \tag {9.41}
$$

(For sufficiently small $T_{s}$ , $[I - (T_{s}/2)A]^{-1}$ exists.)

![](image/7f4f1197b533df2f72aeab1a26f715384d1e65b5bd45cbc57d97d76e47eea9f5.jpg)

<details>
<summary>line</summary>

| Time (s) | θ (deg) |
| --- | --- |
| 0.0 | 0.0 |
| 0.2 | 0.2 |
| 0.4 | 0.6 |
| 0.6 | 1.0 |
| 0.8 | 1.1 |
| 1.0 | 1.1 |
| 1.2 | 1.0 |
| 1.4 | 1.0 |
| 1.6 | 1.0 |
| 1.8 | 1.0 |
| 2.0 | 1.0 |
</details>

![](image/c221b2b20517a5c45bed50be07d38b435f2f92aaa44efbe48ef3a7c6ae8ebd07.jpg)

<details>
<summary>line</summary>

| Time (s) | θ (deg) |
| --- | --- |
| 0.0 | 0.0 |
| 0.2 | 0.2 |
| 0.4 | 0.7 |
| 0.6 | 1.1 |
| 0.8 | 1.3 |
| 1.0 | 1.25 |
| 1.2 | 1.1 |
| 1.4 | 0.95 |
| 1.6 | 0.9 |
| 1.8 | 0.95 |
| 2.0 | 1.0 |
</details>

Figure 9.18 Step response for Example 9.14, $T_{s} = 0.05$ s

This is not in state form because of the term $\widehat{\mathbf{e}}(k)$ on the RHS. However, it is in a form that can be implemented on a computer.
