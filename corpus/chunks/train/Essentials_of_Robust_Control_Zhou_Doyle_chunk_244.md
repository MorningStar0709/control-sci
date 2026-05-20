```mermaid
graph TD
    A["Δ"] --> B["P0"]
    B --> C["Wp"]
    C --> D["Kn"]
    D --> E["K"]
    E --> F["u"]
    F --> G["Wdel"]
    G --> H["Δ"]
    H --> I["p1 p2"]
    I --> J["dp1 dp2"]
    J --> K["e1 e2"]
    K --> L["n1 n2"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#cff,stroke:#333
    style F fill:#ffc,stroke:#333
    style G fill:#cfc,stroke:#333
    style H fill:#fcc,stroke:#333
    style I fill:#ffc,stroke:#333
    style J fill:#cfc,stroke:#333
    style K fill:#fcc,stroke:#333
    style L fill:#ffc,stroke:#333
```
</details>

Figure 9.7: HIMAT closed-loop interconnection

The open-loop interconnection is

$$
\left[ \begin{array}{c} z _ {1} \\ z _ {2} \\ e _ {1} \\ e _ {2} \\ y _ {1} \\ y _ {2} \end{array} \right] = \hat {G} (s) \left[ \begin{array}{c} p _ {1} \\ p _ {2} \\ d _ {1} \\ d _ {2} \\ n _ {1} \\ n _ {2} \\ u _ {1} \\ u _ {2} \end{array} \right].
$$

The Simulink block diagram of this open-loop interconnection is shown in Figure 9.8.

aircraft.m   
File Edit Options Simulation Style   
![](image/3f60f6e434b369c295e45a9f55ba83427b4faed96724ef4c67002186be077042.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["1 z1"] --> B["Demux"]
    C["2 z2"] --> D["Demux"]
    E["3 e1"] --> F["Demux"]
    G["4 e2"] --> H["Demux"]
    I["5 y1"] --> J["Demux"]
    K["6 y2"] --> L["Demux"]
    B --> M["x' = Ax+Bu y = Cx+Du"]
    D --> N["x' = Ax+Bu y = Cx+Du"]
    F --> O["x' = Ax+Bu y = Cx+Du"]
    H --> P["x' = Ax+Bu y = Cx+Du"]
    J --> Q["x' = Ax+Bu y = Cx+Du"]
    L --> R["x' = Ax+Bu y = Cx+Du"]
    M --> S["State Space: Wdel"]
    N --> T["State Space: Wp"]
    O --> U["State Space: himat"]
    P --> V["State Space: Wn"]
    Q --> W["State Space: wln"]
    R --> X["State Space: wln"]
    S --> Y["Mux Mux1"]
    T --> Z["Mux Mux2"]
    U --> AA["Mux Mux3"]
    V --> AB["Mux Mux"]
    W --> AC["Mux Mux"]
    X --> AD["Mux Mux"]
    Y --> AE["1 pert1"]
    Z --> AF["2 pert2"]
    AA --> AG["3 dist1"]
    AB --> AH["4 dist2"]
    AC --> AI["5 noise1"]
    AD --> AJ["6 noise2"]
    AE --> AK["u1"]
    AF --> AL["u2"]
```
</details>

Figure 9.8: Simulink block diagram for HIMAT (aircraft.m)

The ${ \hat { G } } ( s ) = \left[ { \frac { A \mid B } { C \mid D } } \right]$ can be computed by

$$\gg [ \mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D} ] = \operatorname{linmod} \left(^ {\prime} \text { aircraft } ^ {\prime}\right)$$

which gives
