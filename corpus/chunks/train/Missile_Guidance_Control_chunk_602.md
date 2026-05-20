It should be noted here that $\mathbf { a } _ { T }$ , also known as the specific force, accounts for aerodynamic and control forces as well. This is the quantity whose components are measured by physical accelerometers [9], [11],

$$\frac {d \mathbf {V} _ {m}}{d t} = \mathbf {a} _ {T} + \mathbf {g}, \tag {6.179}$$

where g is the gravitational acceleration vector. Figure 6.23 shows a possible indication system for (6.170) and (6.179).

The coordinate system of the missile is chosen as follows: The x-axis points downrange toward the target, the z-axis vertically, and the y-axis out of the paper, completing an orthogonal system. These axes are illustrated in Figure 6.24.

The vector for $d \mathbf { V } _ { g } / d t$ can now be expanded into three scalar equations corresponding to the three accelerometer-input axes as follows:

$$\frac {d V _ {g x}}{d t} = - a _ {T x} - Q _ {x x} V _ {g x} - Q _ {x y} V _ {g y} - Q _ {x z} V _ {g z}, \tag {6.180a}\frac {d V _ {g y}}{d t} = - a _ {T y} - Q _ {y x} V _ {g x} - Q _ {y y} V _ {g y} - Q _ {y z} V _ {g z}, \tag {6.180b}\frac {d V _ {g z}}{d t} = - a _ {T z} - Q _ {z x} V _ {g x} - Q _ {z y} V _ {g y} - Q _ {z z} V _ {g z}. \tag {6.180c}$$

![](image/5cfc506d7c5052b266284cc4ad64edf1b54c65d598fb58bc969c1bbf65602c1c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Strapdown INS"] --> B["a_T"]
    B --> C["+"]
    C --> D["1/s"]
    D --> E["V_m"]
    E --> F["1/s"]
    F --> G["r_m"]
    G --> H["Missile position"]
    I["Target position computer"] --> J["r_T (target position)"]
    J --> K["Velocity computer"]
    K --> L["V_c"]
    L --> M["+"]
    M --> N["V_g (velocity correction)"]
    N --> O["To control system"]
    P["Gravity computer"] --> Q["r_m"]
    Q --> R["+"]
    R --> S["V_m"]
    S --> T["1/s"]
    T --> U["r_m"]
    U --> V["Missile position"]
    W["g"] --> X["+"]
    X --> Y["+"]
    Y --> Z["+"]
    Z --> AA["+"]
    AA --> AB["+"]
    AB --> AC["+"]
    AC --> AD["+"]
    AD --> AE["+"]
```
</details>

Fig. 6.23. A possible indication system.

![](image/d4b4a8c877cd7bd2dcbc77df790b700db8eeae320f93a5ebb650057754f08578.jpg)

<details>
<summary>text_image</summary>

Trajectory reference plane
x Down range
y
z
</details>

Fig. 6.24. Coordinate system.

It is possible to simplify the Q terms by making the following: assumptions

$$Q _ {x x} = \text { constant (a function of range) },Q _ {y y} = 0 (\text { since the } y \text {-axis is out of the trajectory plane }),Q _ {z x} = \text { constant (a function of range) },Q _ {z z} = Q _ {x x},Q _ {x z} = Q _ {z x},Q _ {y x} = Q _ {x y} = Q _ {y z} = Q _ {z y} = 0.$$
