Figure C.10 shows a plot of the simulation results for y(t) and z(t) after executing the Simulink model in Fig. C.9. The two dynamic variables decay to zero from their respective initial conditions. At time t = 1 s, the step function is applied and both dynamic variables show an exponential rise to their steady-state values.

![](image/dacf73e79e775b260bea869f17635aecd602fad6dae99933cd14d968e826186c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["+"] --> B["1/0.5"]
    B --> C["1/s"]
    C --> D["y"]
    D --> E["To Workspace"]
    F["+"] --> G["3"]
    G --> H["3"]
    H --> I["0.4z"]
    I --> J["0.4"]
    J --> K["0.4z"]
    L["u(t)"] --> M["+"]
    M --> N["1/2.4"]
    N --> O["1/s"]
    O --> P["z"]
    P --> Q["To Workspace1"]
    R["16z"] --> S["16"]
    S --> T["To Workspace2"]
    U["Clock"] --> V["t"]
    V --> W["To Workspace2"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#ffc,stroke:#333
    style F fill:#fcc,stroke:#333
    style G fill:#cff,stroke:#333
    style H fill:#ffc,stroke:#333
    style I fill:#fcc,stroke:#333
    style J fill:#ffc,stroke:#333
    style K fill:#fcc,stroke:#333
    style L fill:#ffc,stroke:#333
    style M fill:#fcc,stroke:#333
    style N fill:#cff,stroke:#333
    style O fill:#ffc,stroke:#333
    style P fill:#fcc,stroke:#333
    style Q fill:#ffc,stroke:#333
    style R fill:#fcc,stroke:#333
    style S fill:#ffc,stroke:#333
    style T fill:#fcc,stroke:#333
```
</details>

Figure C.9 Simulink model for Eqs. (C.8) and (C.9) (Example C.3).   
![](image/36e61016cef84c5f5d3fe6c00b8af79922be7abda64882b9108ddb800e6a309d.jpg)

<details>
<summary>line</summary>

| Time, s | y(t) | z(t) |
| --- | --- | --- |
| 0.0 | -0.3 | 0.55 |
| 0.5 | -0.05 | 0.05 |
| 1.0 | 0.0 | 0.0 |
| 1.5 | 0.02 | 0.2 |
| 2.0 | 0.03 | 0.22 |
| 2.5 | 0.03 | 0.22 |
| 3.0 | 0.03 | 0.22 |
</details>

Figure C.10 System responses y(t) and z(t) (Example C.3).
