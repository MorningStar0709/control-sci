Figure 3.40 depicts the guidance subsystem as having an input LOS rate $d \lambda / d t$ , an output corrective acceleration $A _ { L }$ , and a parasitic attitude loop. The direct path from $d \lambda / d t$ to $A _ { L }$ shows the mechanization of the proportional navigation law (indicated by the “closing velocity multiplier” block), with a low-pass noise filter in order to reduce the high-frequency noise, chiefly for the sake of the fin servos inside the autopilot. If only this direct path from $d \lambda / d t$ to $A _ { L }$ existed, then the guidance design would be much easier than it actually is. In the feedback path of Figure 3.40, the airframe transfer function relates the pitch rate to the lateral acceleration of the $c g$ .

![](image/7820b3e75fe8515f0bf72a06c8d88dba1fbab497ca1af4a6069efad6858f6a2c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["LOS rate λ̇"] --> B["Seeker"]
    B --> C["1 + R"]
    C --> D["+"]
    D --> E["N'VcGn cos θh"]
    E --> F["Closing-vel multiplier"]
    F --> G["G-command"]
    G --> H["Autopilot with dominant break-frequency ω₁"]
    H --> I["A_L Corrective acceleration"]
    I --> J["Airframe"]
    J --> K["τ = α/γ̇"]
    K --> L["θ̇m Pitch rate associated with nl"]
    L --> M["Seeker"]
    M --> N["εθ̇m"]
    N --> O["+"]
    O --> P["Apparent boresight error ε_APP"]
    P --> Q["ε̂"]
    Q --> R["Radome model"]
    R --> S["True boresight error ε̂"]
    S --> T["Closing velocity Vc"]
    T --> U["ε̂"]
    U --> V["Response of boresight error to pitching depends on seeker loops and refraction slope R."]
```
</details>

Fig. 3.40. The parasitic attitude loop (inside guidance kinematic loop).

The alpha over gamma dot time constant τ may be a fraction of a second at low altitude and may exceed 10 seconds at high altitude. Neglecting the feedback for a moment, it is seen that the LOS rate $d \lambda / d t$ causes the seeker to develop a boresight error signal that is multiplied by the closing velocity $V _ { c }$ and suitably filtered to form a g-command $A _ { l c }$ for the autopilot. The feedback arises because the missile must develop a pitch rate $d \theta _ { m } / d t$ , and this disturbs the gyro-stabilized seeker (if such is used) a finite amount, thus changing the boresight error $\varepsilon _ { a p p }$ . Also, during pitching motion the seeker must look through a different part of the radome with a different refraction, and this too affects the boresight error signal.
