10.26 Figure P10.26 shows the angular position control of a DC motor. The DC motor parameters are taken from Example 10.3 (inductance is neglected). Design a lead controller $G _ { C } ( s )$ for the closed-loop motor position control that meets the following criteria: (1) the steady-state error for a reference input $\theta _ { \mathrm { r e f } } ( t ) = 2 0 t$ rad is less than 0.1 rad, and (2) the phase margin is greater than $4 5 ^ { \circ }$ . Use Simulink to obtain the closed-loop response for the controller design and plot $\theta _ { \mathrm { r e f } } ( t )$ and $\theta ( t )$ on the same figure, and plot armature voltage $e _ { \mathrm { i n } } ( t )$ .

![](image/bfd6fed8319c3acbe6b3a5fdebc158cca858f748aecb1088af24ec0f4a99dc46.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Reference position (rad), θ_ref(t)"] --> B((+))
    B --> C["Position error, θ_e(t)"]
    C --> D["G_C(s)"]
    D --> E["Armature voltage, e_in(t)"]
    E --> F["400/(s(s+20.4))"]
    F --> G["Motor position (rad), θ(t)"]
    G --> H["-"]
    H --> B
```
</details>

Figure P10.26
