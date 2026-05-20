```mermaid
graph TD
    A["-y"] --> B["KT_d s"]
    B --> C["Σ"]
    C --> D["Actuator"]
    D --> E["u"]
    E --> F["Σ"]
    F --> G["e_s"]
    G --> H["1/T_t"]
    H --> I["Σ"]
    I --> J["1/s"]
    J --> K["K"]
    K --> L["K"]
    L --> C
    M["e"] --> N["K/T_i"]
    N --> O["Σ"]
    O --> P["1/T_t"]
    P --> Q["Σ"]
    Q --> R["v"]
    R --> S["Actuator"]
    S --> T["u"]
    T --> U["Σ"]
    U --> V["e_s"]
    V --> W["1/s"]
    W --> X["Σ"]
    X --> Y["1/T_t"]
    Y --> Z["Σ"]
    Z --> A
```
</details>

![](image/1ed1d96955439469c305a184c4b7490982998b3deee136616e956afe1591a48d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["-y"] --> B["KT_d s"]
    B --> C["Σ"]
    C --> D["Actuator model u"]
    D --> E["Actuator"]
    E --> F["Σ"]
    F --> G["1/s"]
    G --> H["Σ"]
    H --> I["K/T_i"]
    I --> J["Σ"]
    J --> K["1/T_t"]
    K --> L["Feedback to Σ"]
    L --> M["e_s"]
    M --> N["Feedback to Σ"]
    N --> O["Sum"]
    O --> P["v"]
    P --> Q["Actuator model u"]
    Q --> R["Actuator"]
```
</details>

Figure 8.10 Controller with antiwindup. A system in which the actuator output is measured is shown in (a) and a system in which the actuator output is estimated from a mathematical model is shown in (b).

equivalent signal can be generated from the model, as shown in Fig. 8.10(b). Fignre 8.9 shows the improved behavior with controllers having an anti-windup scheme. Antiwindup is further discussed in Sec. 9.4.
