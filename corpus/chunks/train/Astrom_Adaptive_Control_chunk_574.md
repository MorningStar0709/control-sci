![](image/2e7e15d97037406ad2186f5d8536f482b58020235e8b20e8a6a3a9d31c17749c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["u_c"] --> B["State feedback controller"]
    B --> C["v"]
    C --> D["g₁(x,v)"]
    D --> E["u"]
    E --> F["Process"]
    F --> G["x"]
    G --> H["Feedback loop"]
    H --> I["g₂(x)"]
    I --> J["z"]
    J --> B
    style B fill:#f9f,stroke:#333
    style D fill:#ccf,stroke:#333
    style F fill:#cfc,stroke:#333
    style I fill:#fcc,stroke:#333
```
</details>

Figure 9.7 Block diagram of a controller based on nonlinear transformation.

A simple version of the problem also occurs in control of industrial robots. In this case the basic equation can be written as

$$J \frac {d ^ {2} \varphi}{d t ^ {2}} = T _ {e}$$

where J is the moment of inertia, $\varphi$ is an angle at a joint, and $T_{e}$ is a torque, which depends on the motor current, the torque angles, and their first two derivatives. The equations are thus in the desired form, and the nonlinear feedback is obtained by determining the currents that give the desired torque. The problem is therefore called the torque transformation.
