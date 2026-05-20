$$
\begin{array}{l} x (k + 1) = F x (k) + G y (k) + K \left(u (k) - C x (k) - D y (k)\right) \\ = (F - K C) x (k) + (G - K D) y (k) + K u (k) \\ = F _ {0} x (k) + G _ {0} y (k) + K u (k) \\ \end{array}
$$

If the system of (9.8), and (9.9) is observable, the matrix K can always be chosen so that $F_{0} = F - KC$ has prescribed eigenvalues inside the unit disc. Notice that this equation is analogous to (9.5). By applying the same arguments as for the controller with an explicit observer, the control law becomes

$$
\begin{array}{l} \begin{array}{r l} x (k + 1) & = F _ {0} x (k) + G _ {0} y (k) + K u (k) \\ y (k) & = \cot (G _ {0} (k) + D _ {0} (k)) \end{array} \tag {9.10} \\ u (k) = \operatorname{sat} \bigl (C x (k) + D y (k) \bigr) \\ \end{array}
$$

The saturation function is chosen to correspond to the actual saturation in the actuator. A comparison with the case of an explicit observer shows that (9.10) corresponds to an observer with dynamics given by the matrix $F_{0}$ . The system of (9.10) is also equivalent to (9.2) for small signals. A block diagram of the controller with antireset windup compensation is shown in Fig. 9.6.

![](image/6c0704dbad6a318e1bb05b02178f6e1c727767b9d9649ba2d52bb04f5323c594.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    y --> G
    G --> Σ
    Σ --> q⁻¹
    q⁻¹ --> C
    C --> Σ
    Σ --> u
    D --> Σ
    F --> Σ
    x --> C
    x --> Σ
    Σ --> u
    u --> D
    u --> F
    u --> K
    u --> G-KD
    G-KD --> Σ
    Σ --> q⁻¹
    q⁻¹ --> C
    C --> Σ
    Σ --> v
    v --> sat
    sat --> u
    u --> F-KC
    F-KC --> Σ
    Σ --> F
    F --> D
    D --> Σ
```
</details>

Figure 9.6 Block diagram of the controller (9.2) and the modification in (9.10) that avoids windup.
