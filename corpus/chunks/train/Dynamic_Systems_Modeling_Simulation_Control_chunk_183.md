Thermal systems are generally more difficult to model compared to mechanical, electrical, or fluid systems. Temperature typically exhibits a spatial variation; that is, temperature usually varies between different points in a body. Therefore, temperature of a body could be represented as $T ( x , y , z , t )$ , which states that the temperature varies with the Cartesian coordinate location $( x , y , z )$ within the body as well as time t. Therefore, thermal systems are more accurately modeled as distributed systems, which require partial differential equations (PDEs) instead of ODEs as the modeling equations. In order to derive simplified, approximate thermal models, we assume that all points in a “thermal body” possess the same (average) temperature. This assumption allows us to derive lumped-parameter models where each “thermal body” (or thermal capacitance) has a single, uniform temperature. Therefore, our lumped-parameter thermal models are similar to our lumped-parameter fluid models, where each fluid capacitance (i.e., chamber or vessel) possesses a single pressure at each instant of time (i.e., there is no pressure variation within a fluid capacitance).

![](image/70be19550a0006e3d111535189619f75058a2b9dc77824ef343d54059498c624.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Net input enthalpy rate"] --> B["Σh_in"]
    B --> C["Thermal system boundary"]
    C --> D["Net output heat flow rate"]
    D --> E["Σq_out"]
    C --> F["Net output enthalpy rate"]
    F --> G["Σh_out"]
    H["Net input heat flow rate"] --> I["Σq_in"]
    I --> C
    style C fill:#f9f,stroke:#333
    style D fill:#ccf,stroke:#333
    style E fill:#cfc,stroke:#333
    style F fill:#fcc,stroke:#333
```
</details>

Figure 4.17 Thermal system boundary for an open system.
