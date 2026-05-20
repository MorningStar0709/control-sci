```mermaid
graph LR
    A["Reference input, r(t)"] --> B((+))
    B --> C["e(t)"]
    C --> D["\frac{K(s + z_L)}{s + p_L}"]
    D --> E["\frac{0.1}{s(s + 1) (s + 6)}"]
    E --> F["Output, y(t)"]
    F --> G["-"]
    G --> B
    style B fill:#f9f,stroke:#333
    style E fill:#ccf,stroke:#333
```
</details>

Figure P10.22

10.23 Figure P10.23 shows the Bode diagram of an open-loop transfer function G(s)H(s) that is part of a closedloop control system. The open-loop transfer function contains a lead controller with a control gain setting of K = 2, which corresponds to the Bode diagram in Fig. P10.23. Estimate the gain and phase margins and the control gain $K _ { \mathrm { m s } }$ that drives the closed-loop system to the point of marginal stability.

![](image/b3328dc8d477faee709a5baa7742adf5417eaa62c3200d0ea1967addc0234765.jpg)

<details>
<summary>line</summary>

| Frequency, ω, rad/s | Magnitude, dB |
| --- | --- |
| 0.1 | 20 |
| 1 | 0 |
| 10 | -60 |
</details>

![](image/d87018cfe25e22644ce4ebaa7603bf8a5261338f5632706328506b8e2aac7525.jpg)

<details>
<summary>line</summary>

| Frequency, ω, rad/s | Phase, deg |
| --- | --- |
| 0.1 | -90 |
| 1 | -180 |
| 10 | -270 |
</details>

Figure P10.23
