# Geometric Interpretation

The least-squares problem can be interpreted as a geometric problem in $R^t$ , where $t$ is the number of observations. Figure 2.2 illustrates the situation with two parameters and three observations. The vectors $\varphi^1$ and $\varphi^2$ spans a plane if they are linearly independent. The predicted output $\hat{Y}$ lies in the plan spanned by $\varphi^1$ and $\varphi^2$ . The error $\mathcal{E} = Y - \hat{Y}$ is smallest when $\mathcal{E}$ is orthogonal to this plane. In the general case, Eq. (2.4) can be written as

$$
\left( \begin{array}{c} {\varepsilon (1)} \\ {\varepsilon (2)} \\ {\vdots} \\ {\varepsilon (t)} \end{array} \right) = \left( \begin{array}{c} {y (1)} \\ {y (2)} \\ {\vdots} \\ {y (t)} \end{array} \right) - \left( \begin{array}{c} {\varphi_ {1} (1)} \\ {\varphi_ {1} (2)} \\ {\vdots} \\ {\varphi_ {1} (t)} \end{array} \right) \theta_ {1} - \dots - \left( \begin{array}{c} {\varphi_ {n} (1)} \\ {\varphi_ {n} (2)} \\ {\vdots} \\ {\varphi_ {n} (t)} \end{array} \right) \theta_ {n}
$$

or

$$\mathcal {E} = Y - \varphi^ {1} \theta_ {1} - \varphi^ {2} \theta_ {2} - \dots - \varphi^ {n} \theta_ {n}$$

where $\varphi^{i}$ are the columns of the matrix $\Phi$ . The least-squares problem can thus be interpreted as the problem of finding constants $\theta_{1},\ldots,\theta_{n}$ such that the vector Y is approximated as well as possible by a linear combination of the vectors $\varphi^{1},\varphi^{2},\ldots,\varphi^{n}$ . Let $\hat{Y}$ be the vector in the span of $\varphi^{1},\varphi^{2},\ldots,\varphi^{n}$ , which is the best approximation, and let $E=Y-\hat{Y}$ . The vector E is smallest when it is orthogonal to all vectors $\varphi^{i}$ . This gives

![](image/814be080b10e4d0a223dd7174f6a6b9a7b698e50b114c5e39f9d8598f27b7d58.jpg)

<details>
<summary>text_image</summary>

Y
E
φ²
θ₂φ²
Ŷ
θ₁φ¹
φ¹
</details>

Figure 2.2 Geometric interpretation of the least-squares estimate.

$$\left(\varphi^ {i}\right) ^ {T} \left(Y - \theta_ {1} \varphi^ {1} - \theta_ {2} \varphi^ {2} - \dots - \theta_ {n} \varphi^ {n}\right) = 0 \quad i = 1, \dots , t$$

which is identical to the normal equation (2.5). The vector $\theta$ is unique if the vectors $\varphi^{1},\varphi^{2},\ldots,\varphi^{n}$ are linearly independent.
