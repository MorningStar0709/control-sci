# Design Parameters

Several parameters must be chosen in the design procedure:

- The model transfer function $B_{m} / A_{m}$ ,   
• The observer polynomial $A_{0}$ ,   
• The degrees of polynomials R, S, and T, and   
• The polynomials $P_{1}$ , $P_{2}$ , and Q.

Many different model-reference adaptive systems can be obtained by different choices of the design parameters. A popular choice of the polynomials is $P_{1} = A_{m}, P_{2} = A_{o}$ , and $Q = A_{o}A_{m}$ .

![](image/9e79213d2b8c29b7e4c9187d54644603abc890f0df4082f669c7d43b048c0c43.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["u"] --> B["Filter"]
    C["y"] --> B
    B --> D["-P1φ"]
    D --> E["Π"]
    E --> F["u"]
    F --> G["B/A"]
    G --> H["y+"]
    H --> I["Σ"]
    I --> J["e"]
    J --> K["Q/P"]
    K --> L["e_f"]
    L --> M["Σ"]
    M --> N["ε"]
    N --> O["Π"]
    O --> P["γ/s"]
    P --> Q["θ"]
    Q --> R["Σ"]
    R --> S["η"]
    S --> T["b₀Q/A₀Aₘ"]
    T --> U["1/P₁u"]
    U --> V["φ"]
    V --> W["Π"]
    W --> X["θ^T"]
    X --> Y["Process"]
    Y --> Z["y_m"]
    Z --> AA["Model"]
    AA --> AB["y_m"]
```
</details>

Figure 5.21 Block diagram of a model-reference adaptive system for a SISO system.
