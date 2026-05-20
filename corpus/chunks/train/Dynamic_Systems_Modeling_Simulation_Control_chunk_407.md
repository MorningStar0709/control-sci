# 7.15 Figure P7.15 shows a linear third-order system and a linear first-order system. Analytically and numerically show that the first-order transfer function $G _ { 2 } ( s )$ is an excellent low-order approximate model of the thirdorder system $G _ { 1 } ( s )$ . Use MATLAB or Simulink for the numerical comparison.

![](image/a5093993932000e3aea2138ef7cb8d5ac14036b10f2b17b101295d45463869eb.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["u(t)"] --> B["72/(s³ + 20.2s² + 124s + 24)"]
    B --> C["y(t)"]
    D["G₁(s)"] --> B
```
</details>

![](image/50585ed2c5440b664457b4931e0f844fcc9b524f6cf88b1ed7ca37036edf06b8.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["u(t)"] --> B["0.6/(s + 0.2)"]
    B --> C["y(t)"]
    D["G₂(s)"] --> B
```
</details>

Figure P7.15
