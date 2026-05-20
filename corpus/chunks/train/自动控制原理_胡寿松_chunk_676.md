$$\dot {\boldsymbol {x}} _ {o} = \hat {\boldsymbol {A}} _ {1 1} \boldsymbol {x} _ {o} + \hat {\boldsymbol {B}} _ {1} \boldsymbol {u}, \quad \boldsymbol {y} _ {1} = \hat {\boldsymbol {C}} _ {1} \boldsymbol {x} _ {o} = \boldsymbol {y} \tag {9-206}$$

不可观测子系统动态方程为

$$\dot {\boldsymbol {x}} _ {\bar {o}} = \hat {\boldsymbol {A}} _ {2 1} \boldsymbol {x} _ {o} + \hat {\boldsymbol {A}} _ {2 2} \boldsymbol {x} _ {\bar {o}} + \hat {\boldsymbol {B}} _ {2} \boldsymbol {u}, \quad \boldsymbol {y} _ {2} = \mathbf {0} \tag {9-207}$$

系统的结构方块图如图 9-22 所示。

![](image/1d204b76360bd9f6f8f812df3a85405cb475de99b4233b76d41e6336c710f47e.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["u"] --> B["\hat{B}_1"]
    A --> C["\hat{B}_2"]
    B --> D["+"]
    C --> E["+"]
    D --> F["○"]
    E --> G["+"]
    F --> H["\dot{x}_o"]
    G --> I["\dot{x}_{\bar{o}}"]
    H --> J["I/s"]
    I --> K["I/s"]
    J --> L["x_o"]
    K --> M["x_o"]
    L --> N["\hat{C}_1"]
    M --> N
    N --> O["y"]
    P["\hat{A}_{11}"] --> Q["\hat{A}_{21}"]
    P --> R["\hat{A}_{22}"]
    Q --> S[x_{\bar{o}}
    R --> T[x_{\bar{o}}
```
</details>

图 9-22 可观测性规范分解方块图

设 $\hat{\mathbf{A}} = \mathbf{T}\mathbf{A}\mathbf{T}^{-1} = \left[ \begin{array}{cc} \hat{\mathbf{A}}_{11} & \mathbf{0} \\ \hline \hat{\mathbf{A}}_{21} & \hat{\mathbf{A}}_{22} \end{array} \right], \quad \hat{\mathbf{B}} = \mathbf{T}\mathbf{B} = \left[ \begin{array}{c} \hat{\mathbf{B}}_1 \\ \hline \hat{\mathbf{B}}_2 \end{array} \right]$

$$
\hat {\boldsymbol {C}} = \boldsymbol {C} \boldsymbol {T} ^ {- 1} = \left[ \begin{array}{c c c} & \hat {\boldsymbol {C}} _ {1} & \boldsymbol {0} \end{array} \right]
$$

与可控性规范分解相类似，称系统 $(\hat{A},\hat{B},\hat{C})$ 为系统 $(A,B,C)$ 的可观测规范分解。可观测性规范分解也有与可控性规范分解相类似的分析与结论。

例 9-20 试将例 9-19 所示系统按可观测性进行分解。

解 系统的可观测性矩阵为

$$
\mathbf {V} = \left[ \begin{array}{l} \mathbf {c c c} \\ \mathbf {c c c} & \mathbf {A} & 2 \\ \mathbf {c c c} ^ {2} \end{array} \right] = \left[ \begin{array}{l l l} 1 & - 1 & 1 \\ 2 & - 3 & 2 \\ 4 & - 7 & 4 \end{array} \right]
\operatorname{rank} V = 2 < n = 3
$$

故系统不可观测。从可观测性矩阵中选取两个线性无关行向量[1 -1 1]和[2 -3 2]，再选取一个与之线性无关的行向量[0 0 1]，构成非奇异变换矩阵

$$
\boldsymbol {T} = \left[ \begin{array}{c c c} 1 & - 1 & 1 \\ 2 & - 3 & 2 \\ 0 & 0 & 1 \end{array} \right]
$$

计算变换后各矩阵

$$
\boldsymbol {T} ^ {- 1} = \left[ \begin{array}{c c c} 3 & - 1 & - 1 \\ 2 & - 1 & 0 \\ 0 & 0 & 1 \end{array} \right], \quad \boldsymbol {T A T} ^ {- 1} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ - 2 & 3 & 0 \\ - 5 & 3 & 2 \end{array} \right]

\boldsymbol {T} \boldsymbol {b} = \left[ \begin{array}{l} 1 \\ 2 \\ \dots \\ 1 \end{array} \right], \quad c \boldsymbol {T} ^ {- 1} = \left[ \begin{array}{l l l l} 1 & 0 & 0 \end{array} \right]
$$

可观测子系统动态方程为

$$
\dot {\pmb {x}} _ {o} = \left[ \begin{array}{l l} 0 & 1 \\ - 2 & 3 \end{array} \right] \pmb {x} _ {o} + \left[ \begin{array}{l} 1 \\ 2 \end{array} \right] u, \quad y _ {1} = [ 1 \quad 0 ] \pmb {x} _ {o} = y
$$

不可观测子系统动态方程为

$$\dot {x} _ {o} = [ - 5 \quad 3 ] x _ {o} + 2 x _ {o} + u, \quad y _ {2} = 0$$
