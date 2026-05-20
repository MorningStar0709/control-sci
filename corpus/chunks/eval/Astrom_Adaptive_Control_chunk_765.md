# Rudder Roll Damping System

On many ships it is desirable to reduce the rolling motion. Conventional roll damping systems on large naval ships use active fins or active as well as passive tanks. These systems are expensive to install, especially for retrofits. A third approach to roll damping is to use the rudder for roll damping as well as for maneuvering. High-frequency movements of the rudder damp the rolling without influencing the mean value of the heading of the ship. Such a system can be inexpensive, since it can easily be connected to the ordinary steering system. One such system, Roll-Nix, has been developed by SSPA Maritime Consulting in Gothenburg, Sweden. The system is also marketed by Hyde Marine Systems in Cleveland, Ohio. A block diagram of the system is shown in Fig. 12.15. Roll-Nix includes an adaptive Kalman filter, an adaptive course-keeping autopilot (optional), a high-gain turning controller (optional), and an adaptive roll damping controller. The first three parts are similar to those described for the Steermaster 2000 autopilot.

![](image/ec30e93a1cf12673b39180fdd5f3f96285cda1cbd01f8c81b64d8ce5547987ca.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Steering gear"] -->|Rudder| B["Ship"]
    B --> C["Roll-Nix"]
    C --> D["Adaptive Kalman filter"]
    C --> E["Adaptive autopilot"]
    C --> F["Turning regulator"]
    C --> G["Adaptive roll damping"]
    B --> H["Helm"]
    H --> I["Speed"]
    I --> J["Course"]
    J --> K["Roll rate"]
    K --> L["Course set-point"]
    M["Wind Waves Currents"] --> B
    N["Rudder command"] --> A
```
</details>

Figure 12.15 Block diagram of the Roll-Nix roll damping system. (With courtesy of SSPA Maritime Consulting AB.)
