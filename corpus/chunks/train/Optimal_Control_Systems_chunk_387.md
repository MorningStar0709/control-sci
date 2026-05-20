# 7.2 TOC of a Double Integral System

Here we examine the time-optimal control (TOC) of a classical double integral system. This simple example demonstrates some of the important features of the TOC system [6].

![](image/8bae8a34f57f6e24af4a6cd45501396c7b5e894b6fdfa848427f7be7e7755f8a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["x*(t)"] --> B["Algorithm"]
    B --> C["-h[x*(t)"]]
    C --> D["Relay"]
    D --> E["u*(t)"]
    E --> F["\dot{x}(t)=Ax(t)+Bu(t)"]
    F --> G["x*(t)"]
    G --> H["Plant"]
    style A fill:#f9f,stroke:#333
    style H fill:#f9f,stroke:#333
```
</details>

Figure 7.6 Closed-Loop Structure for Time-Optimal Control System
