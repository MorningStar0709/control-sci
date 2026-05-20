| Time, s | Piston position, x(t), cm |
| --- | --- |
| 0.0 | 30.0 |
| 0.5 | 45.0 |
| 1.0 | 45.0 |
| 1.5 | 45.0 |
</details>

Figure 11.44 Closed-loop responses of the nonlinear and linear EHA models with $X _ { \mathrm { r e f } } = 4 5$ cm and proportional gain $K _ { P } = 4 0 0 \mathrm { V / m }$ .

A second performance test for the control system is the ability to track a dynamic, periodic reference input. Figure 11.45 shows a Simulink diagram of the closed-loop control system with a sinusoidal reference input for $x _ { \mathrm { r e f } } ( t )$ (note that the nonlinear hydraulic actuator subsystem from Fig. 11.34 is included instead of the simple integrator actuator). The reference position $x _ { \mathrm { r e f } } ( t )$ is a sine function with $_ { \mathrm { a \pm 1 5 - c m } }$ amplitude about the piston’s starting position of 30 cm. Note that we could construct a linear closed-loop Simulink model using the linearized EHA plant; that is, we would replace the nonlinear EHA plant in Fig. 11.45 with the integrator model $X ( s ) / Y ( s ) = K _ { \mathrm { H A } } / s .$ .

Figure 11.46 shows the closed-loop responses of the nonlinear and linear hydraulic actuator models for the sinusoidal reference position $x _ { \mathrm { r e f } } ( t )$ with a frequency of 2 Hz. The proportional gain is $K _ { P } = 5 0 0 \mathrm { V / m }$ . Figure 11.46 clearly shows that the closed-loop frequency responses from the nonlinear and linear EHA models are indistinguishable from each other. Furthermore, the closed-loop response x(t) using proportional control exhibits significant lag with respect to the reference input. The voltage signal $e _ { \mathrm { i n } } ( t )$ oscillates between ±60 V when the P-gain is $K _ { P } = 5 0 0 \mathrm { V / m }$ and therefore increasing the gain will cause the voltage input to exceed its limits.

![](image/678e5eefd6cdb56509e62471a7fb589585805fb663337c4c5c504bbd491ed073.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Sine Wave"] -->|x_ref| B["+"]
    B --> C["Kp"]
    C --> D["e_in"]
    D --> E["Kv*wn^2(s) / (s^2 + 2*zeta*wns+wn^2)"]
    E --> F["y"]
    F --> G["x"]
    G --> H["To Workspace"]
    H --> I["xdot"]
    I --> J["To Workspace1"]
    J --> K["t"]
    K --> L["Clock"]
    L --> M["To Workspace2"]
    M --> N["x"]
    N --> O["Nonlinear hydraulic actuator (Fig. 11.34)"]
    O --> P["xDot"]
    P --> Q["x"]
    Q --> R["x"]
    R --> S["End"]
```
</details>

Figure 11.45 Closed-loop Simulink model with proportional control scheme and sinusoidal reference input.
