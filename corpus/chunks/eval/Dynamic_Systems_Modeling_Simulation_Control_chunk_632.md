10.16 Figure P10.16 shows a closed-loop system with a PD controller. Use MATLAB and the root-locus method to design the PD controller (i.e., select gain K and zero $z _ { C } )$ so that the underdamped closed-loop roots have damping ratio $\zeta > 0 . 6 5$ and undamped natural frequency $\omega _ { n } > 1$ rad/s. Explain your steps and justify your final design with root-locus analysis.

![](image/dbeb580d4c8ac7fd5daf2b787e8311c913762ee37c65189ece60ab51f591bab5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Reference input, r(t)"] --> B((+))
    B --> C["e(t)"]
    C --> D["K(s + z_C)"]
    D --> E["u(t)"]
    E --> F["2/(s³ + 3s²)"]
    F --> G["Output, y(t)"]
    G --> H["Feedback"]
    H --> I["-"]
    I --> B
    style D fill:#f9f,stroke:#333
    style F fill:#ccf,stroke:#333
```
</details>

Figure P10.16
