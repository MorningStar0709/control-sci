# EXAMPLE 1.4 Nonlinear valve

A simple feedback loop with a Proportional and Integrating (PI) controller, a nonlinear valve, and a process is shown in Fig. 1.8. Let the static valve characteristic be

$$v = f (u) = u ^ {4} \quad u \geq 0$$

Linearizing the system around a steady-state operating point shows that the incremental gain of the valve is $f'(u)$ , and hence the loop gain is proportional to $f'(u)$ . The system can perform well at one operating level and poorly at another. This is illustrated by the step responses in Fig. 1.9. The controller is tuned to give a good response at low values of the operating level. For higher values of the operating level the closed-loop system even becomes unstable. One way to handle this type of problem is to feed the control signal u through an inverse of the nonlinearity of the valve. It is often sufficient to use a fairly crude approximation (see Example 9.1). This can be interpreted as a special case of gain scheduling, which is treated in detail in Chapter 9.

![](image/90405636d7afdd318255f0ef7f0caa01d5dfe76c881748366d356659a5acd002.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["u_c"] --> B["Σ"]
    B --> C["K(1 + 1/T_i s)"]
    C --> D["u"]
    D --> E["f(.)"]
    E --> F["v"]
    F --> G["G_0(s)"]
    G --> H["y"]
    H --> I["-1"]
    I --> B
    style B fill:#f9f,stroke:#333
    style C fill:#ccf,stroke:#333
    style D fill:#cfc,stroke:#333
    style E fill:#fcc,stroke:#333
    style F fill:#cff,stroke:#333
    style G fill:#ffc,stroke:#333
    style H fill:#fff,stroke:#333
    style I fill:#fff,stroke:#333
```
</details>

Figure 1.8 Block diagram of a flow control loop with a PI controller and a nonlinear valve.

![](image/7da2b553aa22f4b7e9ed51d0235a2aed7981278fc0ebaa8c4a3555dea6f84e05.jpg)  
Figure 1.9 Step responses for PI control of the simple flow loop in Example 1.4 at different operating levels. The parameters of the PI controller are K = 0.15, $T_{i} = 1$ . The process characteristics are $f(u) = u^{4}$ and $G_{0}(s) = 1/(s + 1)^{3}$ .
