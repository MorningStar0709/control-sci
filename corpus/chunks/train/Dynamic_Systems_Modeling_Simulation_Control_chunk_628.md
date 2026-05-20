# 10.4 Figure P10.4 shows a closed-loop control system.

![](image/e2db4b02f2f6bb997c433ee7dc531f658cd2a6d3b9788fcd768b293db5d67463.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Reference input, r(t)"] --> B((+))
    B --> C["K_P"]
    C --> D["2/(s+1)"]
    D --> E["Output, y(t)"]
    E --> F["6/(s+6)"]
    F --> G["-"]
    G --> B
    D --> H["Plant"]
    H --> E
```
</details>

Figure P10.4

a. Compute the controller gain $K _ { P }$ so that the undamped natural frequency of the closed-loop system is $\omega _ { n } = 4 \mathrm { r a d / s }$ .   
b. Compute the controller gain $K _ { P }$ so that the damping ratio of the closed-loop system is $\zeta = 0 . 7$   
c. Compute the steady-state output for a step reference input $r ( t ) ~ = ~ 4 U ( t )$ and controller gain $K _ { P } = 2 .$ .
