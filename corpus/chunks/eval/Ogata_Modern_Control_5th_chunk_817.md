$$
\mathbf {Q} = \left[ \begin{array}{c c c} q _ {1 1} & 0 & 0 \\ 0 & q _ {2 2} & 0 \\ 0 & 0 & q _ {3 3} \end{array} \right], \qquad R = 1, \qquad \mathbf {x} = \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] = \left[ \begin{array}{c} y \\ \dot {y} \\ \ddot {y} \end{array} \right]
$$

Figure 10–39 Control system.   
![](image/6d138399eb9e304e63647fa58581013434154ca152793a700bc95e30be13fde2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    r --> |+| A["+"]
    A --> B["k1"]
    B --> C["+"]
    C --> D["u"]
    D --> E["ẋ = Ax + Bu"]
    E --> F["y = Cx"]
    F --> y["x1"]
    y --> G["x2"]
    G --> H["k2"]
    H --> I["k3"]
    I --> J["x3"]
    J --> C
    C --> K["u"]
    K --> L["+"]
    L --> M["k1"]
    M --> N["+"]
    N --> O["u"]
    O --> P["ẋ = Ax + Bu"]
    P --> Q["y = Cx"]
    Q --> R["y = x1"]
```
</details>

To get a fast response, $q _ { 1 1 }$ must be sufficiently large compared with $q _ { 2 2 } , q _ { 3 3 }$ , and R. In this problem, we choose

$$q _ {1 1} = 1 0 0, \quad q _ {2 2} = q _ {3 3} = 1, \quad R = 0. 0 1$$

To solve this problem with MATLAB, we use the command

$$K = \operatorname{lqr} (A, B, Q, R)$$

MATLAB Program 10–22 yields the solution to this problem.
