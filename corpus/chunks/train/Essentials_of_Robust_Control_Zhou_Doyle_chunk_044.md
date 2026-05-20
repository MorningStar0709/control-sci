```mermaid
graph LR
    z --> G
    G --> w
    w --> u
    u --> K
    K --> y
    y --> G
```
</details>

Chapter 10 considers robust stability and performance for systems with multiple sources of uncertainties. We show that an uncertain system is robustly stable and satisfies some $\mathcal { H } _ { \infty }$ performance criterion for all $\Delta _ { i } \in \mathcal { R } \mathcal { H } _ { \infty }$ with $\| \Delta _ { i } \| _ { \infty } < 1$ if and only if the structured singular value $( \mu )$ of the corresponding interconnection model is no greater than 1.

![](image/d85139d7fb08b91b79fd1f96c51100885f34e4176a0661d666111eaf959688bc.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["nominal system"] --> B["Δ₁"]
    A --> C["Δ₂"]
    A --> D["Δ₃"]
    A --> E["Δ₄"]
    B --> F
    C --> G
    D --> H
    E --> I
```
</details>

Chapter 11 characterizes in state-space all controllers that stabilize a given dynamical system $G ( s )$ . For a given generalized plant

$$
G (s) = \left[ \begin{array}{l l} G _ {1 1} (s) & G _ {1 2} (s) \\ G _ {2 1} (s) & G _ {2 2} (s) \end{array} \right] = \left[ \begin{array}{c c c} A & B _ {1} & B _ {2} \\ \hline C _ {1} & D _ {1 1} & D _ {1 2} \\ C _ {2} & D _ {2 1} & D _ {2 2} \end{array} \right]
$$

we show that all stabilizing controllers can be parameterized as the transfer matrix from y to u below where F and L are such that $A + L C _ { 2 }$ and $A + B _ { 2 } F$ are stable and where $Q$ is any stable proper transfer matrix.

![](image/dc51e2b8cb64053f09539f699c68c4df177ed057f9ad43f6f7b48b65b637f924.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    z --> G
    w --> G
    G --> y
    y --> C2
    y --> D22
    y --> A
    y --> F
    C2 --> ∫
    ∫ --> B2
    B2 --> y1
    y1 --> Q
    Q --> -L
    -L --> C2
    C2 --> A
    A --> ∫
    ∫ --> B2
    B2 --> F
    F --> y1
    y1 --> C2
    C2 --> -
```
</details>

Chapter 12 studies the stabilizing solution to an algebraic Riccati equation (ARE). A solution to the following ARE

$$A ^ {*} X + X A + X R X + Q = 0$$

is said to be a stabilizing solution if $A + R X$ is stable. Now let

$$
H := \left[ \begin{array}{c c} A & R \\ - Q & - A ^ {*} \end{array} \right]
$$

and let X (H) be the stable H invariant subspace and

$$
\mathcal {X} _ {-} (H) = \mathrm{Im} \left[ \begin{array}{l} X _ {1} \\ X _ {2} \end{array} \right],
$$
