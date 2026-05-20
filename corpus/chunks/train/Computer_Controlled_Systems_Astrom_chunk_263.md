# A Two-Degree-of-Freedom Controller

Practical control systems often have specifications that involve both servo and regulation properties. This is traditionally solved using a two-degree-of-freedom structure, as shown in Fig. 4.12. Compare with Fig. 3.10. This configuration has the advantage that the servo and regulation problems are separated. The feedback controller $H_{fb}$ is designed to obtain a closed-loop system that is insensitive to process disturbances, measurement noise, and process uncertainties. The feedforward compensator $H_{ff}$ is then designed to obtain the desired servo properties. We will now show how to solve the servo problem in the context of state feedback.

![](image/cbcb3c4cf012f2504513e62e322de96e283cc60597f09a592d346fb89176a887.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["u_c"] --> B["H_ff"]
    B --> C["u_ff"]
    C --> D["Σ"]
    D --> E["u"]
    E --> F["Process"]
    F --> G["y"]
    G --> H["-H_fb"]
    H --> I["u_fb"]
    I --> D
```
</details>

Figure 4.12 Block diagram of a feedback system with a two-degree-of-freedom structure.

![](image/7e9970cf997aecc62983c3e7bddd5ef05d60359e3b4c89716d649cfb919b8e38.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["u_c"] --> B["Model and Feedforward Generator"]
    B --> C["x_m"]
    C --> D["Σ"]
    D --> E["L"]
    E --> F["u_fb"]
    F --> G["Σ"]
    G --> H["Process"]
    H --> I["y"]
    I --> J["Observer"]
    J --> K["x̂"]
    K --> D
    L["u_ff"] --> G
```
</details>

Figure 4.13 A two-degree-of-freedom controller based on state feedback and an observer.
