Sketch the constant-gain loci for K=1, 2, 5, 10, and 20 on the s plane.

B–6–11. Consider the system shown in Figure 6–101. Plot the root loci with MATLAB. Locate the closed-loop poles when the gain K is set equal to 2.

![](image/7e16a5719e400de6ebbdbf73116cb42fb9a5eb7d6136bacf38536c53f0cb76c8.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["+"] --> B["K(s+1)/s(s²+2s+6)"]
    B --> C["1/(s+1)"]
    C --> A
```
</details>

Figure 6–101   
Control system.

B–6–12. Plot root-locus diagrams for the nonminimum-phase systems shown in Figures 6–102(a) and (b), respectively.

![](image/8afcabd71b81869f1e3b0bb453c68f5641d930478772222d815982f74cefb56d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] --> B["+"]
    B --> C["K(s-1)/(s+2)(s+4)"]
    C --> D["G₁(s)"]
    D --> A
```
</details>

(a)

![](image/fb8fdbd127fa8ae40854583d2bd8c46d3034587db0bdbfa2cbb990e0a7f6ee96.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] --> B["Block"]
    B --> C["G2(s)"]
    C --> A
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
```
</details>

(b)   
Figure 6–102 (a) and (b) Nonminimum-phase systems.

B–6–13. Consider the mechanical system shown in Figure 6–103. It consists of a spring and two dashpots. Obtain the transfer function of the system. The displacement $x _ { i }$ is the input and displacement $x _ { o }$ is the output. Is this system a mechanical lead network or lag network?

![](image/7198616b3a545e6716fbcd17ed5ca0dc17e204520ae03e503d0d8c33e4badd95.jpg)

<details>
<summary>text_image</summary>

b₂
k
b₁
xᵢ
xₒ
n.
</details>

Figure 6–103 Mechanical system

B–6–14. Consider the system shown in Figure 6–104. Plot the root loci for the system. Determine the value of K such that the damping ratio $\zeta$ of the dominant closed-loop poles is 0.5. Then determine all closed-loop poles. Plot the unitstep response curve with MATLAB.

![](image/e02941b71fda7cf8efb23860465c53981b6a1f030c34c917e8484dcdd45de575.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] --> B["\frac{K}{s(s² + 4s + 5)}"]
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> I
    I --> J
    J --> K
    K --> L
    L --> M
    M --> N
    N --> O
    O --> P
    P --> Q
    Q --> R
    R --> S
    S --> T
    T --> U
    U --> V
    V --> W
    W --> X
    X --> Y
    Y --> Z
    Z --> A
```
</details>

Figure 6–104 Control system.
