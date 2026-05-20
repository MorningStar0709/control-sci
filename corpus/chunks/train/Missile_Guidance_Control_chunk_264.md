# Description

Pure pursuit strives to keep the vehicle’s (i.e., missile’s) heading always pointing to the target, in order to achieve the maximum killing capability:

![](image/8085cf77cba0ef9b3c019721ba2556bb6353cc195444f18e8fd2484568b108fc.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["High Altitude"] --> B["Low Altitude"]
    B --> C["Pitch plane"]
    B --> D["Yaw plane"]
    B --> E["Combined plane"]
    C --> F["Turn rate limited by maximum 22° wing deflection available"]
    D --> G["Turn rate limited by 25g maximum autopilot command"]
    E --> H["Turn rate limited by maximum 22° wing deflection available"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#cfc,stroke:#333
    style E fill:#cfc,stroke:#333
```
</details>

(a) Maximum maneuver capability.

![](image/3e5260dd11d8645f60213e2ae46bbc657f681dbf74b99c2d04d16dfb231411d9.jpg)

<details>
<summary>text_image</summary>

Y
Y'
Target
Vt
γt
r
λ
|λ - θ| ≤ 45°
vm
α
γm
u
θ
X'
X
w
Missile
0
</details>

(b) Geometry of the interception process.   
Fig. 4.10. Target interception maneuver capability and geometry.
