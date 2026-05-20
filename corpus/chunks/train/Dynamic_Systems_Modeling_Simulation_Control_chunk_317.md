We may now run both the nonlinear and linear models and compare the responses. As previously shown, the nominal input volumetric-flow rate is $Q _ { \mathrm { i n } } ^ { * } = 0 . 0 5 \mathrm { m } ^ { 3 } / \mathrm { s }$ , and the corresponding nominal pressure is $P ^ { * } = 1 . 1 6 9 5 5 ( 1 0 ^ { 5 } ) \mathrm { N } / \mathrm { m } ^ { 2 }$ . The actual input flow rate is set to $Q _ { \mathrm { i n } } = 0 . 0 5 2 \mathrm { m } ^ { 3 } / \mathrm { s }$ , and the initial tank pressure is set at $P _ { 0 } = 1 . 1 5 ( 1 0 ^ { 5 } ) \mathrm { N } / \mathrm { m } ^ { 2 }$ , which is less than the nominal pressure. Therefore, the (constant) perturbation flow rate is $\delta Q _ { \mathrm { i n } } = 0 . 0 0 2 \ : \mathrm { m } ^ { 3 } / \mathrm { s }$ and the initial perturbation pressure is $\delta P _ { 0 } = - 1 9 5 5 \mathrm { N } / \mathrm { m } ^ { 2 }$ . Figure 6.20 presents the tank pressure responses from the nonlinear and linear Simulink models. The linear solution accurately matches the true nonlinear solution for tank pressure and underestimates the final (steady) pressure by less than $2 5 \mathrm { N } / \mathrm { m } ^ { 2 }$ . The linear solution is accurate because the perturbations are relatively small: the flow-rate perturbation is within 4% of its nominal value, while the initial pressure perturbation is less than 2% of its nominal value.

![](image/e4fab525b46a5be948e36b9d7cd7e59e8dd24a0cc9029650da0740e9efa229f4.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Q_in"] --> B["+"]
    C["Q_in_star"] --> D["-"]
    B --> E["delta-Q_in"]
    D --> F["δ-Q_in"]
    E --> G["5000 Gain, df/dQ_in"]
    F --> H["1/s Delta-P dot"]
    G --> I["+"]
    H --> J["+"]
    I --> K["Integrator"]
    J --> L["+"]
    K --> M["dP To Workspace"]
    L --> N["P To Workspace2"]
    M --> O["t Nominal pressure, P_star"]
    N --> P["P_star"]
    P --> Q["-0.008 Gain, df/dP"]
    Q --> R["+"]
    R --> S["delta-P"]
    S --> T["+"]
    T --> U["dP to Workspace"]
    V["L Clock"] --> W["t To Workspace1"]
    X["Nominal in-flow volumetric rate"] --> B
```
</details>

Figure 6.19 Simulink diagram for Example 6.8: linear tank model.
