# 7.4.7 TERCOM Position Updating

The concept of utilizing terrain sensor data to obtain a sequence of position fixes has been under investigation since the late 1950s (see Section 7.4.1). As previously mentioned, the objective of the terrain contour matching process is to provide the vehicle’s navigation system with a measured downtrack and crosstrack vehicle position error. Consequently, the navigation system then uses the measured position error to update its estimate of the vehicle’s true geographic position. Usually, a Kalman filter is used to aid in reducing the navigation system’s errors based on the measured vehicle position error.

![](image/a9b8a2240004c81959eba5f456e4c8b52cadadce3c52fefd7decd54b39c021c6.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Vehicle sensor\n• Antenna\n• Receiver\n• Signal processor"] --> B["Correlator"]
    B --> C["Correlator"]
    C --> D["Vehicle navigation system"]
    D --> E["Reference map"]
    E --> F["Indicated position"]
    F --> D
    D --> G["Stabilization and motion compensation signals"]
    G --> A
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#cff,stroke:#333
    style F fill:#ffc,stroke:#333
    style G fill:#fcc,stroke:#333
```
</details>

Fig. 7.21. Correlation update-aided navigation system.
