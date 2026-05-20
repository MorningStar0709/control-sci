# 7.5.2 Integral Feedback

It is not always easy to measure the dc component of a disturbance, and model inaccuracies will always lead to some error in the feedforward gains. Fortunately, there is a way around these difficulties, at the (slight) cost of introducing a few more state variables. We write

$$\dot {\mathbf {x}} = A \mathbf {x} + B \mathbf {u} + \Gamma \mathbf {w} \tag {7.47}$$

and append m integrators,

$$\dot {\mathbf {z}} = C \mathbf {x} - \mathbf {y} _ {d}. \tag {7.48}$$

Equations 7.47 and 7.48 are combined as

$$
\left[ \begin{array}{l} \dot {\mathbf {x}} \\ \dot {\mathbf {z}} \end{array} \right] = \left[ \begin{array}{l l} A & 0 \\ C & 0 \end{array} \right] \left[ \begin{array}{l} \mathbf {x} \\ \mathbf {z} \end{array} \right] + \left[ \begin{array}{l} B \\ 0 \end{array} \right] \mathbf {u} + \left[ \begin{array}{l} \Gamma \\ 0 \end{array} \right] \mathbf {w} + \left[ \begin{array}{l} 0 \\ I \end{array} \right] \mathbf {y} _ {d}. \tag {7.49}
$$

We proceed to establish conditions under which this composite system is controllable from the input u.

■ Theorem 7.7 Let $(A, B)$ be controllable. The system $([A\ 0\ 0], [B\ 0])$ is controllable if, and only if, the original system $(A, B, C)$ has no transmission zeros at the origin.

Proof: The composite $A$ matrix is block triangular, so its eigenvalues are the eigenvalues of $A$ , denoted by $s_1, s_2, \ldots$ , plus $m$ eigenvalues at $s = 0$ . Let $\mathbf{w}_1^T, \mathbf{w}_2^T, \ldots$ be the left eigenvectors of $A$ . Then

$$
[ \mathbf {w} _ {i} ^ {T} \quad 0 ] \left[ \begin{array}{l l} A & 0 \\ C & 0 \end{array} \right] = [ \mathbf {w} _ {i} ^ {T} A \quad 0 ] = s _ {i} [ \mathbf {w} _ {i} ^ {T} \quad 0 ]
$$

and $[\mathbf{w}_i^T\quad 0]$ is an eigenvector of $[ \begin{array}{cc}A & 0\\ C & 0 \end{array} ]$ corresponding to the mode $s_i$ .

![](image/dc1860215bf5f3a4e195a4634ea3e6b2d83d6fa5f76edad4fe1e843b786420bc.jpg)

<details>
<summary>line</summary>

| Time(s) | Force (kN) |
| --- | --- |
| 0 | 120 |
| 5 | 118 |
| 10 | 115 |
| 15 | 110 |
| 20 | 105 |
| 25 | 100 |
| 30 | 98 |
</details>

![](image/afba31e438ade4d4b059fdf96073f3d03439261ae97b9a3a091cfe2cd054b1bf.jpg)

<details>
<summary>line</summary>

| Time(s) | Velocity (m/s) - Solid Line | Velocity (m/s) - Dashed Line |
| --- | --- | --- |
| 0 | 0 | 0 |
| 5 | 4 | 2 |
| 10 | 6 | 4 |
| 15 | 8 | 5 |
| 20 | 10 | 7 |
| 25 | 12 | 8 |
| 30 | 14 | 9 |
</details>

![](image/41ce44d43f38064953cc828d2cf34e360cd3c4e6d6a16b38bf3c7a1155f47d9c.jpg)
