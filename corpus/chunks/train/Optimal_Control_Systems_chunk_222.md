where, $\mathbf{P}(t)$ , the positive definite matrix, is the solution of the

![](image/a058186d5488175a4cb76178a44a9cead6862500a565e8c8bb1918c796647664.jpg)

<details>
<summary>line</summary>

| t | g₁(t) | g₂(t) |
| --- | --- | --- |
| 0 | 0.6 | 0.0 |
| 20 | 2.0 | 0.1 |
</details>

Figure 4.3 Coefficients $g_{1}(t)$ and $g_{2}(t)$ for Example 4.1

![](image/0a8b95035796af766e7e872e38b1d23775119f29fb52750618ea1c5e15cc775f.jpg)

<details>
<summary>line</summary>

| t | x₁(t) | x₂(t) |
| --- | --- | --- |
| 0 | 3.0 | 0.0 |
| 1 | 1.0 | -0.1 |
| 2 | 1.0 | 0.0 |
| 3 | 1.0 | 0.0 |
| 4 | 1.0 | 0.0 |
| 5 | 1.0 | 0.0 |
| 6 | 1.0 | 0.0 |
| 7 | 1.0 | 0.0 |
| 8 | 1.0 | 0.0 |
| 9 | 1.0 | 0.0 |
| 10 | 1.0 | 0.0 |
| 11 | 1.0 | 0.0 |
| 12 | 1.0 | 0.0 |
| 13 | 1.0 | 0.0 |
| 14 | 1.0 | 0.0 |
| 15 | 1.0 | 0.0 |
| 16 | 1.0 | 0.0 |
| 17 | 1.0 | 0.0 |
| 18 | 1.0 | 0.0 |
| 19 | 1.0 | 0.0 |
| 20 | 1.0 | -0.1 |
</details>

Figure 4.4 Optimal States for Example 4.1

![](image/dd735bce1b018d7fef313b3e62da45db5bf627f0e19af9a7d99701341c86367d.jpg)

<details>
<summary>line</summary>

| t | Optimal Control |
| --- | --- |
| 0 | -20 |
| 2 | 25 |
| 4 | 5 |
| 6 | 2 |
| 8 | 2 |
| 10 | 2 |
| 12 | 2 |
| 14 | 2 |
| 16 | 2 |
| 18 | 2 |
| 20 | -25 |
</details>

Figure 4.5 Optimal Control for Example 4.1

matrix differential Riccati equation (4.1.32)

$$
\begin{array}{l} \left[ \begin{array}{c c} \dot {p} _ {1 1} (t) & \dot {p} _ {1 2} (t) \\ \dot {p} _ {1 2} (t) & \dot {p} _ {2 2} (t) \end{array} \right] = - \left[ \begin{array}{c c} p _ {1 1} (t) & p _ {1 2} (t) \\ p _ {1 2} (t) & p _ {2 2} (t) \end{array} \right] \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right] \\ - \left[ \begin{array}{c c} 0 & - 2 \\ 1 & - 3 \end{array} \right] \left[ \begin{array}{c c} p _ {1 1} (t) & p _ {1 2} (t) \\ p _ {1 2} (t) & p _ {2 2} (t) \end{array} \right] \\ + \left[ \begin{array}{c c} p _ {1 1} (t) & p _ {1 2} (t) \\ p _ {1 2} (t) & p _ {2 2} (t) \end{array} \right] \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] \frac {1}{0 . 0 4} \left[ \begin{array}{c c} 0 & 1 \end{array} \right]. \\ \left[ \begin{array}{l l} p _ {1 1} (t) & p _ {1 2} (t) \\ p _ {1 2} (t) & p _ {2 2} (t) \end{array} \right] - \left[ \begin{array}{l l} 2 & 0 \\ 0 & 0 \end{array} \right] \tag {4.1.53} \\ \end{array}
$$

and $\mathbf{g}(t)$ , is the solution of the nonhomogeneous vector differential equation obtained from (4.1.34) as
