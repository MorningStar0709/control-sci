<details>
<summary>flowchart</summary>

```mermaid
graph TD
    U[" U "] --> A[" 1/(s+4) "]
    A --> B[" x3 "]
    B --> C[" 1/(s+2)/(s+3) "]
    C --> D[" x2 "]
    D --> E[" Σ "]
    E --> F[" 1/s "]
    F --> G[" x1 "]
    G --> H[" Σ "]
    H --> I[" Y "]

subgraph a)
        J[" 5 "] --> E
        K[" +x1 "] --> L[" Σ "]
        M[" -"] --> N[" 5 "]
        N --> E
        O[" +x2 "] --> P[" Σ "]
        Q[" -"] --> R[" 5 "]
        R --> E
        S[" +x3 "] --> T[" Σ "]
        Uo[" U "] --> Uo[" 1/(s+10) "]
    end

subgraph b)
        Uo --> Uo
        Uo --> Uo
        Uo --> Uo
        Uo --> Uo
        Uo --> Uo
        Uo --> Uo
        Uo --> Uo
        Uo --> Uo
        Uo --> Uo
        Uo --> Uo
        Uo --> Uo
        Uo --> Uo
        Uo --> Uo
        Uo --> Uo
        Uo --> Uo
        V[" x4 "] --> T
        W[" x3 "] --> T
        X[" x2 "] --> T
        Y[" x1 "] --> T
        Z[" +"] --> AA[" Σ "]
        AB[" -"] --> AA
    end
```
</details>

图 7.86 习题 7.17 的框图

7.19 考虑传递函数：

$$G (s) = \frac {Y (s)}{U (s)} = \frac {s + 6}{s ^ {2} + 5 s + 6} \tag {7.283}$$

(a) 将式(7.283)改写为如下形式：

$$G (s) = \frac {Y (s)}{U (s)} = \frac {1}{s + 3} \left(\frac {s + 6}{s + 2}\right)$$

找出 $G(s)$ 的一种串联实现形式，即用两个一阶系统级联实现。

(b) 用 $G(s)$ 的部分分式展开式，找出 $G(s)$ 的一个并联实现。

(c) 求 $G(s)$ 的能控标准形实现。

7.20 证明系统(A, B, C, D)的脉冲响应为

$$h (t) = \boldsymbol {C e} ^ {A t} \boldsymbol {B} + D \delta (t)$$

其中： $e^{At}$ 为如下定义的矩阵指数：

$$e ^ {A t} = \left(I + A t + \frac {A ^ {2} t ^ {2}}{2 !} + \dots\right) = \sum_ {k = 0} ^ {+ \infty} \frac {A ^ {k} t ^ {k}}{k !}$$
