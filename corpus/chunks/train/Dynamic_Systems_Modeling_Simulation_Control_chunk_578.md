# 10.6 ROOT-LOCUS METHOD

Chapter 7 and the previous sections of this chapter have illustrated that the locations of the characteristic roots (or poles) strongly influence the transient-response performance criteria such as settling time, overshoot, and oscillation frequency. Furthermore, system stability is dictated by the root locations in the complex plane: if all characteristic roots have negative real parts, then the system is BIBO stable. It is clear that knowledge of the characteristic root locations is important to the control engineer. Changing the control gains and/or adding a dynamic controller (such as a PI or PD controller) will vary the root locations and therefore adjust the transient response. Large changes in the root locations will have dramatic effects on the transient response characteristics and may lead to instability.

In the late 1940s, W. R. Evans developed a method for computing the closed-loop roots based on knowledge of the open-loop transfer function. This technique, called the root-locus method, is a graphical method that determines how the closed-loop root locations change as a single parameter (usually a gain) is varied. As we shall see, the root-locus method is a valuable tool for determining if desirable transient-response characteristics (settling time, overshoot) can be achieved by adjusting a single control gain. In cases where simple gain adjustment is inadequate, the root-locus method can also be used to design dynamic controllers (such as PI and PD controllers) that can be introduced in order to improve the closed-loop response and stability margins.

![](image/97518550cf6eed0429a2229283cfcf6d471cd3304d3c3e18120c977727c98096.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Reference input, r(t)"] --> B["+"]
    B --> C["Error, e(t)"]
    C --> D["K_P"]
    D --> E["Control signal, u(t)"]
    E --> F["1/(s(s+3))"]
    F --> G["Plant, G_P(s)"]
    G --> H["Output, y(t)"]
    H --> I["-"]
    I --> B
```
</details>

Figure 10.31 Closed-loop control system.
