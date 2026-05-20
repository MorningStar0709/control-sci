![](image/f0687950a69971808be26f3d07ecd43b4256a472dceba050926f5ca99bdad256.jpg)

<details>
<summary>text_image</summary>

y
y=βu
y
u
y=αu
</details>

(b) $\alpha < 0$   
图 6.6 $\beta > 0$ 时的扇形区域 $[\alpha, \beta]$

定义6.2 无记忆函数 $h:[0,\infty)\times R^{P}\rightarrow R^{P}$

\- 如果 $u^{\mathrm{T}}h(t,u)\geqslant 0$ ，则函数属于扇形区域 $[0,\infty ]$ 。

\- 如果 $u^{\mathrm{T}}[h(t,u) - K_1u]\geqslant 0$ ，则函数属于扇形区域 $[K_1,\infty ]$ 。

\- 如果 $h^{\mathrm{T}}(t,u)[h(t,u) - K_2u]\leqslant 0,K_2 = K_2^{\mathrm{T}} > 0$ ，则函数属于扇形区域 $[0,K_2]$ 。

\- 如果 $[h(t,u) - K_1u]^{\mathrm{T}}[h(t,u) - K_2u] \leqslant 0$ (6.5)

$K = K_{2} - K_{1} = K^{T} > 0$ ，则函数属于扇形区域 $\left[K_{1}, K_{2}\right]$ 。

在各种情况下,对于所有 $(t,u)$ 不等式均成立。如果在某种情况下不等式是严格的,可将扇形区域写为 $(0,\infty),(K_{1},\infty),(0,K_{2})$ 或 $(K_{1},K_{2})$ 。在标量情况下,可用 $(\alpha,\beta],[\alpha,\beta)$ 或 $(\alpha,\beta)$ 表示式(6.2)的一边或两边满足严格不等式。

扇形区域 $[0, \infty]$ 对应于无源性，扇形区域 $[K_1, \infty]$ 对应于输入前馈无源性，满足 $\varphi(u) = K_1 u$ ，扇形区域 $[0, K_2], K_2 = (1 / \delta) I > 0$ 对应于严格输出无源性，满足 $\rho(y) = \delta y$ 。我们将留给读者验证（见习题6.1）在扇形区域 $[K_1, K_2]$ 内的函数，通过输入前馈与输出反馈连接，可转换为扇形区域 $[0, \infty]$ 内的函数，如图6.7所示。

![](image/62e1cb4c9a9c36f91a897e1110bcd289587e8b62b3a9d00edd831df5b715ea95.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] --> B((+))
    B --> C["K⁻¹"]
    C --> D["y = h(t,u)"]
    D --> E["+"]
    E --> F((-))
    F --> G["K₁"]
    G --> H["+"]
    H --> I["+"]
    I --> J["+"]
    J --> K["+"]
    K --> L["+"]
    L --> M["+"]
    M --> N["+"]
    N --> O["+"]
    O --> P["+"]
    P --> Q["+"]
    Q --> R["+"]
    R --> S["+"]
    S --> T["+"]
    T --> U["+"]
    U --> V["+"]
    V --> W["+"]
    W --> X["+"]
    X --> Y["+"]
    Y --> Z["+"]
    Z --> A
```
</details>

图6.7 在扇形区域 $[K_1, K_2]$ 内的函数，其中 $K = K_2 - K_1 = K^{\mathrm{T}} > 0$ ，通过输入前馈和输出反馈的连接可转换为扇形区域 $[0, \infty]$ 内的函数
