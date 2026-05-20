This is a relation between the open-loop $\Delta_o(s)$ and closed-loop $\Delta_c(s)$ characteristic polynomials. From Figure 4.10, we note that

1. $-\bar{\mathbf{K}}[s\mathbf{I}-\mathbf{A}]^{-1}\mathbf{B}$ is called the loop gain matrix, and   
2. $I + \bar{K}[sI - A]^{-1}B$ is termed return difference matrix.

![](image/b06a7485c0289cff9d2e58141e7f7df2de3bb5df2ada433e39f3ff2a24be92c5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["U(s)"] --> B["[sI - A"]⁻¹B]
    B --> C["X(s)"]
    D["Plant"] --> E["+"]
    E --> F["\overline{K} = R⁻¹B' \overline{P}"]
    F --> G["Closed-Loop Optimal Controller"]
    G --> H["-"]
    H --> E
```
</details>

Figure 4.10 Optimal Closed-Loop Control in Frequency Domain

To derive the desired factorization result, we use the matrix ARE (4.5.4). Let us rewrite the ARE as

$$- \bar {\mathbf {P}} \mathbf {A} - \mathbf {A} ^ {\prime} \bar {\mathbf {P}} + \bar {\mathbf {P}} \mathbf {B} \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} = \mathbf {Q}. \tag {4.5.8}$$

First adding and subtracting $s\bar{P}, s = j\omega$ to the previous ARE, we get

$$\bar {\mathbf {P}} [ s \mathbf {I} - \mathbf {A} ] + [ - s \mathbf {I} - \mathbf {A} ^ {\prime} ] \bar {\mathbf {P}} + \bar {\mathbf {K}} ^ {\prime} \mathbf {R} \bar {\mathbf {K}} = \mathbf {Q}. \tag {4.5.9}$$

Next, premultiplying by $\mathbf{B}^{\prime}\Phi^{\prime}(-s)$ and post multiplying by $\Phi(s)\mathbf{B}$ , the previous equation becomes

$$
\begin{array}{l} \mathbf {B} ^ {\prime} \boldsymbol {\Phi} ^ {\prime} (- s) \bar {\mathbf {P}} \mathbf {B} + \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \boldsymbol {\Phi} (s) \mathbf {B} + \mathbf {B} ^ {\prime} \boldsymbol {\Phi} ^ {\prime} (- s) \bar {\mathbf {K}} ^ {\prime} \mathbf {R} \bar {\mathbf {K}} \boldsymbol {\Phi} (s) \mathbf {B} \\ = \mathbf {B} ^ {\prime} \boldsymbol {\Phi} ^ {\prime} (- s) \mathbf {Q} \boldsymbol {\Phi} (s) \mathbf {B} \tag {4.5.10} \\ \end{array}
$$

where, we used

$$\boldsymbol {\Phi} (s) = [ s \mathbf {I} - \mathbf {A} ] ^ {- 1}; \quad \boldsymbol {\Phi} ^ {\prime} (- s) = [ - s \mathbf {I} - \mathbf {A} ^ {\prime} ] ^ {- 1}. \tag {4.5.11}$$

Finally, using $\bar{K} = R^{-1}B'\bar{P} \longrightarrow \bar{K}' = \bar{P}BR^{-1} \longrightarrow \bar{P}B = \bar{K}'R$ and adding R to both sides of (4.5.10), we have the desired factorization result as
