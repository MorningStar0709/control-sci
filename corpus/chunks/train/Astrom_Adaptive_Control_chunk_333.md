# Relations between Passivity and Small Gain Theorems

The small gain theorem (Theorem 5.6) and the passivity theorem (Theorem 5.8) are closely related. To investigate this connection further, we consider signal spaces that are inner product spaces and we show that the small gain theorem can be derived from the passivity theorem. We start with Fig. 5.16 and make a sequence of transformations of the feedback loop that are shown in Fig. 5.17.

Consider the closed-loop system in Fig. 5.17(a). Assume that the system $H_{1}$ is strictly output passive and that $H_{2}$ is passive. In Fig. 5.17(b) we have introduced two loops that cancel each other. The input-output relations of the encircled loops are $(I + H_{1})^{-1}H_{1}$ and $I - H_{2}$ , respectively. These two systems are shown in Fig. 5.17(c), where we have also added two loops and two gains (1/2 and 2) that cancel each other. The transfer functions of the encircled loops

a)   
![](image/f88be36870059d1972133a678fb795a529d12ce2fa3297ca3f06f91bf8a6290c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["H₁"] --> B["-H₂"]
    B --> A
```
</details>

b)   
![](image/a682d129a29b3629691a35327d15a2ebc52a8e7a01fcd8cf23a8c22054bb3580.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Σ"] --> B["H₁"]
    A --> C["-I"]
    A --> D["I"]
    A --> E["-H₂"]
    B --> F["Output"]
    C --> G["Output"]
    D --> H["Output"]
    E --> I["Output"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#ccf,stroke:#333
    style D fill:#ccf,stroke:#333
    style E fill:#ccf,stroke:#333
    style F fill:#dfd,stroke:#333
    style G fill:#dfd,stroke:#333
    style H fill:#dfd,stroke:#333
    style I fill:#dfd,stroke:#333
```
</details>

c)   
![](image/f320d3e639836c2d1d775252bf6763475a5fd3da4a55acdd923a7d0dbcaa9211.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["(I + H₁)⁻¹H₁"] --> B["2"]
    C["-I"] --> D["Σ"]
    E["I"] --> F["Σ"]
    G["I - H₂"] --> H["½"]
    D --> F
    F --> H
```
</details>

d)

![](image/67bba988d0b7df172cc20d7e7f87ec05bac39dbf0f22fc1c228d16cdbabf38f5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["S₁"] --> B["-S₂"]
    B --> A
```
</details>

Figure 5.17 Four equivalent systems.

are

$$S _ {1} = 2 \left(H _ {1} + I\right) ^ {- 1} H _ {1} - \left(I + H _ {1}\right) ^ {- 1} \left(I + H _ {1}\right) = \left(H _ {1} + I\right) ^ {- 1} \left(H _ {1} - I\right)$$

and
