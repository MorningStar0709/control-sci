# General Problems of Guidance System Design

1. Help to maximize the single-shot kill probability (SSKP) by minimizing the miss distance.

![](image/b5555332ec96a7373d932ff88736ef914b7b650f15802acb98bf637e7d7893d5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Initial conditions\n• Missile position and velocity\n• Target position and velocity\n• Euler angles"] --> B["Seeker"]
    B --> C["Target position and velocity"]
    C --> D["Seeker"]
    D --> E["Guidance"]
    E --> F["Autopilot"]
    F --> G["Equations of motion"]
    G --> H["Position Euler angles velocities"]
    D --> I["Gimbal angle"]
    I --> J["Guidance"]
    J --> K["Autopilot"]
    K --> L["Equations of motion"]
    L --> M["Position Euler angles velocities"]
    N["Atmosphere"] --> O["Dynamic pressure Mach no. static pressure"]
    P["Thrust"] --> Q["Thrust weight"]
    R["Aerodynamics"] --> S["Aerodynamic coefficients"]
    T["Actual accelerations"] --> L
    U["AOA"] --> L
    V["Loss angular rate"] --> W["Guidance"]
    X["Pitch and yaw commanded accel English bias commands"] --> K
    Y["Angular rates"] --> L
```
</details>

Fig. 3.23. A typical roll-stabilized missile guidance/kinematic loop.
