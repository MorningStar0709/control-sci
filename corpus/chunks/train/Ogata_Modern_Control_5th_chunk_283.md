B–5–28. If the feedforward path of a control system contains at least one integrating element, then the output continues to change as long as an error is present. The output stops when the error is precisely zero. If an external disturbance enters the system, it is desirable to have an integrating element between the error-measuring element and the point where the disturbance enters, so that the effect of the external disturbance may be made zero at steady state.

Show that, if the disturbance is a ramp function, then the steady-state error due to this ramp disturbance may be eliminated only if two integrators precede the point where the disturbance enters.

![](image/a1e8924c800856231144b39843296dc57691759ba11a4a9803f4109fd79aa8bf.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> A["+"] --> B["+"] --> C["K"] --> D["20/(s+1)(s+4)"] --> E["1/s"] --> C["s"]
    E --> F["Kh"] --> A
    A --> G["+"]
    B --> H["+"]
    G --> I["↑"]
    H --> J["↑"]
    I --> K["↓"]
    J --> L["↓"]
    K --> M["↓"]
    L --> N["↓"]
    M --> O["↓"]
    N --> P["↓"]
    O --> Q["↓"]
    P --> R["↓"]
    Q --> S["↓"]
    R --> T["↓"]
    S --> U["↓"]
    T --> V["↑"]
    U --> W["↑"]
    V --> X["↑"]
    W --> Y["↑"]
    X --> Z["↑"]
    Y --> AA["↑"]
    Z --> AB["↑"]
```
</details>

Figure 5–81 Servo system with tachometer feedback.

![](image/7aa499e65cf49b0d193c30228c882b61fff476e6db7e510d9b4e7131f0b15e7e.jpg)

<details>
<summary>text_image</summary>

6
</details>
