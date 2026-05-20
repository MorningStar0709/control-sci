# Air-Brake System Analysis

Next, we present a simulation of the air-brake system under nominal operating conditions with a constant supply pressure $P _ { S } = 5 . 8 4 ( 1 0 ^ { 5 } )$ Pa and step brake-pedal force of 1 N (applied at time $t = 0 . 5 \ : \mathrm { s } )$ . Note that the supply pressure is 5.76 times greater than atmospheric pressure. The Simulink diagram in Fig. 11.25 shows that a 1-N pedal force produces a 0.002 m (2 mm) step displacement of the treadle valve y. Because the height of the valve opening is h = 0.002 m (2 mm), the step pedal-force input produces a step valve area of 4 mm2. Figure 11.29 shows the piston/push-rod response x(t) (in centimeters) to the step valve opening. The push rod reaches its hard-stop limit (4 cm) in less than 0.22 s. Brake chamber pressure P, shown in Fig. 11.30, exhibits an oscillatory behavior during the out-stroke phase as the push rod is displaced to the right. These pressure transients are the result of oscillations in the chamber volume, or piston velocity, which can be observed in the push-rod response x(t) shown in Fig. 11.29. When the push rod reaches its hard-stop limit of 4 cm at approximately $t = 0 . 7 1 { \mathrm { s } } ,$ , the subsequent brake chamber pressure response no longer exhibits

![](image/371a6c38a8e0d6d4f8f5531b462c4b7ba72fd4ed6698d9a45d9e4c299d3a93bf.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Brake chamber pressure P"] --> B["+"]
    C["Atmospheric pressure"] --> D["Diaphragm area"]
    D --> E["Delta-pressure force across diaphragm"]
    E --> F["F_c"]
    F --> G["+"]
    H["P_atm"] --> I["+"]
    J["F_PL"] --> K["Preload spring force"]
    K --> L["+"]
    M["Contact force Eq. (11.25)"] --> N["Saturation"]
    N --> O["Switch"]
    O --> P["F_PL"]
    P --> Q["Net force"]
    Q --> R["1/m 1/mass"]
    R --> S["x-dot"]
    S --> T["Integrator"]
    T --> U["xdot"]
    U --> V["Integrator1"]
    V --> W["0 or 1"]
    W --> X["NOT"]
    X --> Y["Logical Operator"]
    Y --> Z["1 or 0"]
    Z --> AA["X Product"]
    AA --> AB["xdot"]
    AB --> AC["Hard-stop for max stroke"]
    AC --> AD["1 x"]
    AC --> AE["2 xdot"]
    AF["S-cam load force, F_load"] --> AG["k1*u - k2*u^2"]
    AG --> AH["x"]
    AH --> AI["S-cam load force"]
    AI --> AJ["x"]
    AJ --> AK["Return spring force"]
    AK --> AL["b"]
    AL --> AM["Viscous friction coefficient"]
    AM --> AN["x dot"]
    AN --> AO["Return spring"]
    AO --> AP["k"]
    AP --> AQ["x"]
    AQ --> AR["S-cam load force, F_load"]
    AR --> AS["x"]
    AS --> AT["Piston position, x"]
```
</details>
