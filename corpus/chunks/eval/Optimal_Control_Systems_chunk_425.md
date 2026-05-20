$$
u ^ {*} (t) = \left\{ \begin{array}{l l} - 1, & \text {if} \quad x ^ {*} (t) <   + \frac {1}{2 a} <   0, \\ + 1, & \text {if} \quad x ^ {*} (t) > - \frac {1}{2 a} > 0, \\ - 2 a x ^ {*} (t), & \text {if} \quad x ^ {*} (t) > - \frac {1}{2 a} > 0, \\ - 2 a x ^ {*} (t), & \text {if} \quad x ^ {*} (t) <   + \frac {1}{2 a} <   0, \\ 0, & \text {if} \quad x ^ {*} (t) = 0 \end{array} \right. \tag {7.5.58}
$$

and the implementation of the energy-optimal control law is shown in Figure 7.42.

Further, for a combination of time-optimal and fuel-optimal control systems and other related problems with control constraints, see excellent texts [6, 116].

![](image/af1946d3090255ab48c0d7a9bfcf38f1bd2e6fdaaaa5e93db5c573c324dc6bb2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["u*(t)"] --> B["+"]
    B --> C["∫"]
    C --> D["x*(t)"]
    D --> E["a"]
    E --> F["+1/2a"]
    F --> G["-1/2a"]
    G --> H["+1"]
    H --> I["-1"]
    I --> J["+"]
    J --> K["+"]
    K --> L["x*(t)"]
    L --> M["+1/2a"]
    M --> N["-1/2a"]
    N --> O["+1"]
    O --> P["-1"]
    P --> Q["+"]
    Q --> R["x*(t)"]
    R --> S["+1/2a"]
    S --> T["-1/2a"]
    T --> U["+1"]
    U --> V["-1"]
```
</details>

Figure 7.42 Implementation of Energy-Optimal Control Law
