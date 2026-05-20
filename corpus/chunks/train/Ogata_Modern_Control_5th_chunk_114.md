![](image/cd7db5e34cb0ba18a184f69cbb3c54359f6c33f674102fbc6d4066c47e6fed6e.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Input device"] --> B["Error measuring device"]
    B --> C["Amplifier"]
    C --> D["Motor"]
    D --> E["Gear train"]
    E --> F["Load"]
    G["Reference input"] --> H["Input potentiometer"]
    H --> I["Output potentiometer"]
    I --> J["Feedback signal"]
    K["Reference input"] --> L["Input potentiometer"]
    L --> M["Output potentiometer"]
    N["Reference input"] --> O["Input potentiometer"]
    O --> P["Output potentiometer"]
    Q["Reference input"] --> R["Input potentiometer"]
    R --> S["Output potentiometer"]
    T["Reference input"] --> U["Input potentiometer"]
    U --> V["Output potentiometer"]
    W["Reference input"] --> X["Input potentiometer"]
    X --> Y["Output potentiometer"]
```
</details>

(a)

![](image/e2254d8bf8d0ed87d67cede08aedd78282c568dc7471d0c6cc99abaacd928cd2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> +
    + --> E["s"]
    E["s"] --> K0
    K0 --> Ev["s"]
    Ev["s"] --> K1K2
    K1K2 --> θ[s]
    θ[s] --> n
    n --> C["s"]
    C["s"] --> +
    + --> -
    - --> +
    - --> -
    -
    - --> +
```
</details>

![](image/3a69f7380d849125e5a99760c3553e9c8015b2d6f0894ff6f5d9a21af5b2cbe3.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["K/(s(Js + B))"]
    C --> D["C(s)"]
    D --> E["Feedback"]
    E --> B
```
</details>

Figure 3–29 (a) Schematic diagram of servo system; (b) block diagram for the system; (c) simplified block diagram.

Obtain the transfer function between the motor shaft angular displacement u and the error voltage $e _ { v } .$ . Obtain also a block diagram for this system and a simplified block diagram when $L _ { a }$ is negligible.

Solution. The speed of an armature-controlled dc servomotor is controlled by the armature voltage $\boldsymbol { e } _ { a } .$ . (The armature voltage $e _ { a } = K _ { 1 } e _ { v }$ is the output of the amplifier.) The differential equation for the armature circuit is

$$L _ {a} \frac {d i _ {a}}{d t} + R _ {a} i _ {a} + e _ {b} = e _ {a}$$

or

$$L _ {a} \frac {d i _ {a}}{d t} + R _ {a} i _ {a} + K _ {3} \frac {d \theta}{d t} = K _ {1} e _ {v} \tag {3-46}$$

The equation for torque equilibrium is

$$J _ {0} \frac {d ^ {2} \theta}{d t ^ {2}} + b _ {0} \frac {d \theta}{d t} = T = K _ {2} i _ {a} \tag {3-47}$$
