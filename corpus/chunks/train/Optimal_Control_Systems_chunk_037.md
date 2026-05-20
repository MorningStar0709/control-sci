# 1.2 Optimization

Optimization is a very desirable feature in day-to-day life. We like to work and use our time in an optimum manner, use resources optimally and so on. The subject of optimization is quite general in the sense that it can be viewed in different ways depending on the approach (algebraic or geometric), the interest (single or multiple), the nature of the signals (deterministic or stochastic), and the stage (single or multiple) used in optimization. This is shown in Figure 1.4. As we notice that the calculus of variations is one small area of the big picture of the optimization field, and it forms the basis for our study of optimal control systems. Further, optimization can be classified as static optimization and dynamic optimization.

1. Static Optimization is concerned with controlling a plant under steady state conditions, i.e., the system variables are not changing with respect to time. The plant is then described by algebraic equations. Techniques used are ordinary calculus, Lagrange multipliers, linear and nonlinear programming.   
2. Dynamic Optimization concerns with the optimal control of plants under dynamic conditions, i.e., the system variables are changing with respect to time and thus the time is involved in system description. Then the plant is described by differential

![](image/270c9ce6442167f8533432a8507a8f0a5311c7eacbd4b05d681a16aa86bee3d1.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["OPTIMIZATION"] --> B["Geometric Approach"]
    A --> C["Algebraic Approach"]
    B --> D["Single Interest"]
    C --> E["Multiple Interest"]
    D --> F["Deterministic"]
    E --> G["Game Theory"]
    F --> H["Single Stage"]
    G --> I["Stochastic"]
    H --> J["Multiple Stage"]
    I --> K["Dynamic Programming"]
    J --> L["Calculus and Lagrange Multipliers"]
    J --> M["Linear and Nonlinear Programming"]
    J --> N["Functional Analysis"]
    L --> O["Calculus of Variations"]
    M --> O
    N --> O
```
</details>

Figure 1.4 Overview of Optimization

(or difference) equations. Techniques used are search techniques, dynamic programming, variational calculus (or calculus of variations) and Pontryagin principle.
