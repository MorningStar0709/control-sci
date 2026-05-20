# Example 7.12 Multirate systems

Consider the system shown in Fig.7.32, which has two subsystems and two samplers with periods 0.5 and 1. It is assumed that the samplers are synchronized. It is also assumed that the hold circuits are included in the subsystems. If the subsystems are sampled with period 0.5 and 0.5 is chosen as a time unit, then

![](image/e828747ff739d1bf757e8c82da4a245f1ce6ab1c54f38028cb572d8cd011d33c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Start"] -->|u1| B["S1"]
    B -->|y1| C["S2"]
    C -->|u2| D["S2"]
    D -->|y2| E["End"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#ccf,stroke:#333
    style D fill:#ccf,stroke:#333
    style E fill:#dfd,stroke:#333
```
</details>

Figure 7.32 Block diagram of a simple multirate system.

$$
\begin{array}{l} \left\{ \begin{array}{r l} x _ {1} (k + 1) & = \Phi_ {1} x _ {1} (k) + \Gamma_ {1} u _ {1} (k) \\ y _ {1} (k) & = C _ {1} x _ {1} (k) \end{array} \right. \\ \left\{ \begin{array}{r l} x _ {2} (k + 1) & = \Phi_ {2} x _ {2} (k) + \Gamma_ {2} u _ {2} (k) \\ y _ {2} (k) & = C _ {2} x _ {2} (k) \end{array} \right. \\ \end{array}
$$

The interconnection are described by

$$
\begin{array}{l} u _ {1} (k) = y _ {2} (k) \quad k = \dots - 1, 0, 1, 2, \dots \\ u _ {2} (k) = y _ {1} (k) \quad k = \dots - 1, 0, 1, 2, \dots \\ \end{array}
$$

The system is periodic with a period of two sampling intervals. A time-invariant description can be obtained by considering the system variables at even sampling periods only. Straightforward calculations give

$$
\binom {x _ {1} (2 k + 2)} {x _ {2} (2 k + 2)} = \left( \begin{array}{c c} \Phi_ {1} ^ {2} + \Gamma_ {1} C _ {2} \Gamma_ {2} C _ {1} & \Phi_ {1} \Gamma_ {1} C _ {2} + \Gamma_ {1} C _ {2} \Phi_ {2} \\ (\Phi_ {2} \Gamma_ {2} + \Gamma_ {2}) C _ {1} & \Phi_ {2} ^ {2} \end{array} \right) \binom {x _ {1} (2 k)} {x _ {2} (2 k)} \tag {7.38}
$$

This equation can be used to analyze the response of the multirate system. For example, the stability condition is that the matrix on the right-hand side of (7.38) has all its eigenvalues inside the unit disc. The values of the state variables at odd sampling periods are given by

$$
\binom {x _ {1} (2 k + 1)} {x _ {2} (2 k + 1)} = \left( \begin{array}{c c} \Phi_ {1} & \Gamma_ {1} C _ {2} \\ \Gamma_ {2} C _ {1} & \Phi_ {2} \end{array} \right) \binom {x _ {1} (2 k)} {x _ {2} (2 k)}
$$

The analysis illustrated by the example can be extended to an arbitrary number of samplers provided that the ratios of the sampling periods are rational numbers. Delayed sampling can also be handled by the methods described in Sec. 2.3.
