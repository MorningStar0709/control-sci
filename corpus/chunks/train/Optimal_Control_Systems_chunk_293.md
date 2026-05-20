# 5.4 Steady-State Regulator System

![](image/5a1397247fc82881a3160f15b29db7c7b98f0c84be2939a408bfbf5c6d5db870.jpg)

<details>
<summary>line</summary>

| k | Optimal control |
| --- | --- |
| 0 | -4.2 |
| 1 | -1.0 |
| 2 | 0.0 |
| 3 | 0.1 |
| 4 | 0.0 |
| 5 | 0.0 |
| 6 | 0.0 |
| 7 | 0.0 |
| 8 | 0.0 |
| 9 | 0.0 |
| 10 | 0.0 |
</details>

Figure 5.8 Implementation of Optimal Control for Example 5.4

Now, we will show that the solution $\mathbf{P}(k)$ to the Riccati equation (5.3.20) can be obtained in terms of the eigenvalues and eigenvectors of the Hamiltonian matrix H.

Let us first define

$$
\mathbf {J} = \left[ \begin{array}{c c} 0 & \mathbf {I} \\ - \mathbf {I} & 0 \end{array} \right] \quad \text { such   that } \quad \mathbf {J} ^ {- 1} = - \mathbf {J}. \tag {5.4.17}
$$

Now, using (5.4.13), (5.4.14) and (5.4.17), it is a simple thing to show that

$$\mathbf {H} ^ {\prime} \mathbf {J} \mathbf {H} = \mathbf {J}. \tag {5.4.18}$$

By premultiplying and postmultiplying (5.4.18) with $H^{-1}$ and $J^{-1}$ , respectively, we have

$$\mathbf {H} ^ {\prime} \mathbf {J} = \mathbf {J} \mathbf {H} ^ {- 1}, \quad \mathbf {J} ^ {- 1} \mathbf {H} ^ {\prime} \mathbf {J} = \mathbf {H} ^ {- 1} \tag {5.4.19}$$

and using (5.4.17), we get

$$\mathbf {H} ^ {- 1} = - \mathbf {J} \mathbf {H} ^ {\prime} \mathbf {J}. \tag {5.4.20}$$

Now, substituting for the quantities on the right hand side of the previous equation, we have

$$
\mathbf {H} ^ {- 1} = \left[ \begin{array}{c c} \mathbf {A} + \mathbf {E A} ^ {- T} \mathbf {Q} & - \mathbf {E A} ^ {- T} \\ - \mathbf {A} ^ {- T} \mathbf {Q} & \mathbf {A} ^ {- T} \end{array} \right] \tag {5.4.21}
$$

where, $\mathbf{A}^{-T}$ is the transpose of $\mathbf{A}^{-1}$ . Now, let us show that if $\mu$ is an eigenvalue of $\mathbf{H}$ , then $1 / \mu$ is also the eigenvalue of $\mathbf{H}$ . First, if $\mu$ is an eigenvalue with a corresponding eigenvector $[f,g]'$ , then

$$
\left[ \begin{array}{c c} \mathbf {A} ^ {- 1} & \mathbf {A} ^ {- 1} \mathbf {E} \\ \mathbf {Q} \mathbf {A} ^ {- T} & \mathbf {A} ^ {\prime} + \mathbf {Q} \mathbf {A} ^ {- 1} \mathbf {E} \end{array} \right] \left[ \begin{array}{l} f \\ g \end{array} \right] = \mu \left[ \begin{array}{l} f \\ g \end{array} \right] \tag {5.4.22}
$$

and rearranging, we have
