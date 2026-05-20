# 7.2.3 Engineering Implementation of Control Law

Figure 7.11 shows the implementation of the optimal control law (7.2.26).

1. If the system is initially at $(x_{1}, x_{2}) \in R_{-}$ , then $x_{1} > -\frac{1}{2} x_{2}|x_{2}|$ , which means $z > 0$ and hence the output of the relay is $u^{*} = -1$ .

2. On the other hand, if the system is initially at $(x_{1}, x_{2}) \in R_{+}$ , then $x_{1} < -\frac{1}{2}x_{2}|x_{2}|$ , which means z < 0 and hence the output of the relay is $u^{*} = +1$ .

![](image/fa51c935b4f7232430f12dc3ce3e2a3105d24fe9933457c33313b6eaa12147da.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["u*(t)"] --> B["∫"]
    B --> C["x2*(t)"]
    C --> D["∫"]
    D --> E["x1*(t)"]
    F["Plant"] --> B
    G["Relay"] --> H["+1/−1"]
    H --> I["-1"]
    I --> J["z"]
    J --> K["+"]
    K --> L["0.5x2*|x2*|<br>x1*(t)"]
    L --> M["Function Generator"]
    M --> D
    style F fill:#f9f,stroke:#333
    style G fill:#f9f,stroke:#333
    style H fill:#ccf,stroke:#333
    style I fill:#ccf,stroke:#333
    style J fill:#cfc,stroke:#333
    style K fill:#fcc,stroke:#333
    style L fill:#fcc,stroke:#333
    style M fill:#ffc,stroke:#333
    style_N["Closed-Loop Time-Optimal Controller"] --> O["+1/−1"]
    O --> P["-z"]
    P --> Q["+"]
    Q --> R["z"]
    R --> S["+"]
```
</details>

Figure 7.11 Closed-Loop Implementation of Time-Optimal Control Law

Let us note that the closed-loop (feedback) optimal controller is non-linear (control $u^{*}$ is a nonlinear function of $x_{1}^{*}$ and $x_{2}^{*}$ ) although the system is linear. On the other hand, we found in Chapters 3 and 4 for unconstrained control, the optimal control $u^{*}$ is a linear function of the state $x^{*}$ .
