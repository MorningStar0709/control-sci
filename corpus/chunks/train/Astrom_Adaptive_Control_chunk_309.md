# Summary

In this section we have shown that it is possible to construct parameter adjustment rules based on Lyapunov's stability theory. The adjustment rules obtained in this way guarantee that the error goes to zero, but it cannot be asserted that the parameters converge to their correct values. The adjustment rules obtained are similar to those obtained by the MIT rule. However, the rules are not normalized. The adjustment rules have the remarkable property that arbitrarily high adaptation gains can be used. This property depends on the strong assumptions that are made. This is discussed further in Chapter 6.

![](image/20ae6e11065a9ef592a6490cb87ee2d3bf66aa5128ce5c035d31b67b5649a329.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["u_e"] --> B["Model"]
    A --> C["Process"]
    B --> D["k_0 G(s)"]
    C --> E["kG(s)"]
    D --> F["y_m"]
    E --> G["y"]
    F --> H["Σ"]
    G --> I["+"]
    H --> J["e"]
    I --> K["+"]
    J --> L["Π"]
    K --> M["Π"]
    L --> N["-γ/s"]
    M --> O["θ"]
    N --> P["Feedback to Π"]
    O --> Q["Feedback to Π"]
```
</details>

![](image/1a48001fe8df008c853e56cb1ec1d52f0fc479326371d3260fb1b8f38824efb4.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["u_e"] --> B["Π"]
    A --> C["kG(s)"]
    C --> D["Σ"]
    D --> E["Π"]
    E --> F["-γ/s"]
    F --> G["θ"]
    G --> H["Process"]
    H --> I["y_m"]
    I --> J["Model"]
    J --> K["y_m"]
    K --> D
    D -->|e| E
    H -->|+| D
```
</details>

Figure 5.14 Block diagrams of the adaptive systems for feedforward gain compensation obtained by (a) the MIT rule and (b) the Lyapunov rule.
