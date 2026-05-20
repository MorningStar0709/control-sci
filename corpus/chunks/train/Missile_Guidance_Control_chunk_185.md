Variation of dynamic pressure with flight conditions also alters the pitch/yaw autopilot characteristics, as in the roll autopilot, from the one extreme of fast response with minimum stability at high dynamic pressures to the other extreme of relatively slow response with maximum stability at low dynamic pressures. This effect can be minimized by providing altitude gain switching, which permits a prelaunch selection of the proper launch logic as a function of launch altitude and target altitude. This launch logic is used to determine the proper in-flight switching, which occurs as the missile goes from midcourse to terminal phase. In addition, an in-flight course correction command called English bias (for a discussion of English bias, see Section 3.6) is processed by the pitch/yaw autopilot to correct for a missile launch at other than the desired lead angle. Because missile acceleration and slowdown during the boost and glide phases of flight affect the missile lead angle for proper intercept, axial compensation provides lateral commands to the pitch/yaw autopilot in order to adjust the lead angle. From the time the flight control pressure (e.g., hydraulic) is up, pitch or yaw stabilization is obtained by sensing pitch or yaw rates with the pitch or yaw rate gyros, respectively. A block diagram mechanization of a conventional pitch/yaw autopilot is shown in Figure 3.36.

![](image/c1a844cb39ba451da1a1bcfc405b63b39febe33db87be6f6a313eb7de63ecdea.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["A1c"] -->|+| B["+"]
    B --> C["K13"]
    C -->|+| D["+"]
    D --> E["Integrator (K11/T11S)"]
    E -->|+| F["+"]
    F --> G["G12"]
    G --> H["Fin angle δ"]
    H --> I["G1"]
    I --> J["A1L Acceleration at cg"]
    J --> K["Accelerometer"]
    K --> L["G7 ≡ 1"]
    L --> M["A1a"]
    M --> N["G3"]
    N --> O["G1 ≡ G2"]
    O --> P["Airframe"]
    P --> Q["G6"]
    Q --> R["Rate gyro"]
    R --> S["G3"]
    S --> T["Airframe"]
    T --> U["G8 (1 + τ8S)"]
    U --> V["Syn. stab. loop"]
    V --> W["K9"]
    W --> X["Accelerometer loop"]
    X --> Y["Acceleration command"]
```
</details>

Fig. 3.36. The pitch/yaw autopilot.
