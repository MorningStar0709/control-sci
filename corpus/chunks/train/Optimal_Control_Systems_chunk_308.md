| k | g₁(k) | g₂(k) |
| --- | --- | --- |
| 0 | 2.0 | 0.0 |
| 1 | 2.0 | 0.0 |
| 2 | 2.0 | 0.0 |
| 3 | 2.0 | 0.0 |
| 4 | 2.0 | 0.0 |
| 5 | 2.0 | 0.0 |
| 6 | 2.0 | 0.0 |
| 7 | 2.0 | 0.0 |
| 8 | 2.0 | 0.0 |
| 9 | 2.0 | 0.0 |
| 10 | 2.0 | 0.0 |
</details>

Figure 5.14 Coefficients $g_{1}(t)$ and $g_{2}(t)$ for Example 5.6

![](image/b3a1a0d804c0d998ae72003aedd398a16fa88655a6604953d169d32f0fe5a824.jpg)

<details>
<summary>line</summary>

| k | x₁(k) | x₂(k) |
| --- | --- | --- |
| 0 | 5.0 | -1.0 |
| 1 | 2.0 | -0.5 |
| 2 | 2.0 | 0.0 |
| 3 | 2.0 | 0.2 |
| 4 | 2.0 | 0.3 |
| 5 | 2.0 | 0.3 |
| 6 | 2.0 | 0.3 |
| 7 | 2.0 | 0.3 |
| 8 | 2.0 | 0.3 |
| 9 | 2.0 | 0.3 |
| 10 | 2.0 | 0.3 |
</details>

Figure 5.15 Optimal States for Example 5.6

![](image/fcf639e7e3454032f866563241408c673d10dbbea66a378cc78ac39665d52bc9.jpg)

<details>
<summary>line</summary>

| k | Optimal Control |
| --- | --- |
| 0 | -5.0 |
| 1 | 1.0 |
| 2 | 0.2 |
| 3 | 0.1 |
| 4 | 0.1 |
| 5 | 0.1 |
| 6 | 0.1 |
| 7 | 0.1 |
| 8 | 0.1 |
| 9 | 0.1 |
</details>

Figure 5.16 Optimal Control for Example 5.6

whereas, the optimal closed-loop characteristic polynomial is [89]

$$
\begin{array}{l} \boldsymbol {\Delta} _ {c} (z) = | z \mathbf {I} - \mathbf {A} + \mathbf {B} \bar {\mathbf {L}} |, \\ = | \mathbf {I} + \mathbf {B} \bar {\mathbf {L}} [ z \mathbf {I} - \mathbf {A} ] ^ {- 1} |. | z \mathbf {I} - \mathbf {A} |, \\ = | \mathbf {I} + \bar {\mathbf {L}} [ z \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B} |. \boldsymbol {\Delta} _ {o} (z). \tag {5.6.8} \\ \end{array}
$$

From Figure 5.17, we note that

1. $-\bar{\mathbf{L}}[z\mathbf{I}-\mathbf{A}]^{-1}\mathbf{B}$ is called the loop gain matrix, and   
2. $\mathbf{I} + \bar{\mathbf{L}}[z\mathbf{I} - \mathbf{A}]^{-1}\mathbf{B}$ is termed return difference matrix.

First of all, let us note that

$$\bar {\mathbf {P}} - \mathbf {A} ^ {\prime} \bar {\mathbf {P}} \mathbf {A} = [ z ^ {- 1} \mathbf {I} - \mathbf {A} ] ^ {\prime} \bar {\mathbf {P}} [ z \mathbf {I} - \mathbf {A} ] + [ z ^ {- 1} \mathbf {I} - \mathbf {A} ] ^ {\prime} \bar {\mathbf {P}} \mathbf {A} + \mathbf {A} ^ {\prime} \bar {\mathbf {P}} [ z \mathbf {I} - \mathbf {A} ]. \tag {5.6.9}$$

Using the ARE (5.6.5) to replace the left-hand side of the previous equation, we have
