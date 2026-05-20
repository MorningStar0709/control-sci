```mermaid
graph LR
    A["Target dynamics"] -->|Target velocity vector| B["Geometry"]
    B -->|LOS| C["Seeker"]
    C -->|LOS rate| D["Guidance computer"]
    D -->|Guidance command| E["Autopilot & missile dynamics"]
    E --> F["Missile velocity vector"]
    F --> B
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#cff,stroke:#333
    style F fill:#ffc,stroke:#333
```
</details>

(a) Block diagram for proportional navigation

![](image/8c5aa4af9d31adb386731042ce327f20622f02d7b19ae849edf4c869fdde9426.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["y_t"] --> B["+"]
    B --> C["y_e"]
    C --> D["1/(v_c t_go)"]
    D --> E["λ"]
    E --> F["s"]
    F --> G["λ̇"]
    G --> H["N' V_c / cos θ_h"]
    H --> I["a_{lc}"]
    I --> J["Autopilot"]
    J --> K["a_l"]
    K --> L["cos θ_h"]
    L --> M["..."]
    M --> N["∫_o^t ( ) dt"]
    N --> O["+"]
    O --> P["∫_o^t ( ) dt"]
    P --> Q["..."]
    Q --> R["..."]
    R --> S["ŷ_m(t=0)"]
    S --> T["..."]
    T --> U["Guidance system"]
    U --> V["Closing velocity multiplier"]
    V --> W["..."]
    W --> X["..."]
    X --> Y["..."]
    Y --> Z["..."]
    Z --> A
```
</details>

(b) Guidance kinematics loop   
Fig. 4.15. Schematic of a typical guidance system.

When the speedgate (to be discussed later in this section) is locked and starts tracking the Doppler video signal, a command is generated and fed to the autopilot, which switches the English bias command out of the acceleration command processor and switches in axial compensation if this has not already been accomplished by the launch plus 3 sec command. At speedgate lock, radar error commands, which have been amplified and adjusted by closing velocity in the error multiplier, command the pitch or yaw autopilot to process lateral ${ g } ^ { \prime } { \bf { s } } \left( { a } _ { n c } \right)$ . These lateral (or normal) $g ^ { \ast } \mathrm { \mathbf { s } }$ are integrated with an integrator that has been set to the proper altitude band gain. The output of this integrator is a wing command in degrees/sec, which is applied to the appropriate wing hydraulic servo system. As the missile responds to these g commands, the appropriate accelerometer senses these lateral $g ^ { \prime } \mathbf { s }$ and hence generates a signal, which is amplified and synchronously detected for direction by a comparator and is then summed with the original g command to close the accelerometer loop.

![](image/4316592d007e452c1148ebbf7e579dc8afa8ed999ca6ff734f594c06b5f3f0b8.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Target dynamics"] -->|Target velocity vector| B["Geometry"]
    B -->|LOS to target| C["Target tracking radar"]
    C -->|Target track data| D["Guidance computer"]
    D -->|Missile track data| E["Missile tracking radar"]
    E -->|LOS to missile| F["Geometry"]
    F -->|Missile velocity vector| G["Autopilot & missile dynamics"]
    G -->|Guidance commands to missile via uplink| D
```
</details>

Fig. 4.16. System block diagram for command guidance.
