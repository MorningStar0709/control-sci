# 8.2 Approximations Based on Transfer Functions

This section assumes that a continuous-time controller is given as a transfer function, $G(s)$ . It is desired to find an algorithm for a computer so that the digital system approximates the transfer function $G(s)$ (see Fig. 8.1). This problem is interesting for implementation of both analog controllers and digital filters. The approximation may be done in many different ways. Digital implementation includes a data reconstruction, which also can be made in different ways—for example, zero- or first-order hold.

![](image/a9330fb1ef0b8aca642dce487e71b41d90abde525020076c6fbdd3abf8016db2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    u_t["u(t)"] --> A_D["A-D"]
    A_D --> {u(kh)}
    {u(kh)} --> Algorithm["Algorithm"]
    Algorithm --> {y(kh)}
    {y(kh)} --> D_A["D-A"]
    D_A --> y_t["y(t)"]
    y_t --> Clock["Clock"]
    Clock --> A_D
    style A_D fill:#f9f,stroke:#333
    style D_A fill:#f9f,stroke:#333
    style Clock fill:#ccf,stroke:#333
```
</details>

Figure 8.1 Approximating a continuous-time transfer function, $G(s)$ , using a computer.
