# 8.3.1 Additive Uncertainty

We assume that the model uncertainty can be represented by an additive perturbation:

$$\boldsymbol {\Pi} = P + W _ {1} \Delta W _ {2}.$$

Theorem 8.4 Let $\mathbf { I I } = \{ P + W _ { 1 } \Delta W _ { 2 } \colon \Delta \in \mathcal { R } \mathcal { H } _ { \infty } \}$ and let K be a stabilizing controller for the nominal plant P . Then the closed-loop system is well-posed and internally stable for all $\| \Delta \| _ { \infty } < 1$ if and only $i f \parallel W _ { 2 } K S _ { o } W _ { 1 } \parallel _ { \infty } \leq 1$ .

Proof. Let $\Pi = P + W _ { 1 } \Delta W _ { 2 } \in \Pi$ . Then

$$
\left[ \begin{array}{c c} I & K \\ - \Pi & I \end{array} \right] ^ {- 1}

= \left[ \begin{array}{c c} (I + K S _ {o} W _ {1} \Delta W _ {2}) ^ {- 1} S _ {i} & - K S _ {o} (I + W _ {1} \Delta W _ {2} K S _ {o}) ^ {- 1} \\ (I + S _ {o} W _ {1} \Delta W _ {2} K) ^ {- 1} S _ {o} (P + W _ {1} \Delta W _ {2}) & S _ {o} (I + W _ {1} \Delta W _ {2} K S _ {o}) ^ {- 1} \end{array} \right]
$$

is well-posed and internally stable if $( I + \Delta W _ { 2 } K S _ { o } W _ { 1 } ) ^ { - 1 } \in \mathcal { R } \mathcal { H } _ { \infty }$ since

$$\det (I + K S _ {o} W _ {1} \Delta W _ {2}) = \det (I + W _ {1} \Delta W _ {2} K S _ {o}) = \det (I + S _ {o} W _ {1} \Delta W _ {2} K)= \det (I + \Delta W _ {2} K S _ {o} W _ {1}).$$

But $( I + \Delta W _ { 2 } K S _ { o } W _ { 1 } ) ^ { - 1 } \in \mathcal { R } \mathcal { H } _ { \infty }$ is guaranteed if $\| \Delta W _ { 2 } K S _ { o } W _ { 1 } \| _ { \infty } < 1$ (small gain theorem). Hence $\| W _ { 2 } K S _ { o } W _ { 1 } \| _ { \infty } \leq 1$ is sufficient for robust stability.

To show the necessity, note that robust stability implies that

$$K (I + \Pi K) ^ {- 1} = K S _ {o} (I + W _ {1} \Delta W _ {2} K S _ {o}) ^ {- 1} \in \mathcal {R H} _ {\infty}$$

for all admissible ∆. This, in turn, implies that

$$\Delta W _ {2} K (I + \Pi K) ^ {- 1} W _ {1} = I - (I + \Delta W _ {2} K S _ {o} W _ {1}) ^ {- 1} \in \mathcal {R H} _ {\infty}$$

for all admissible $\Delta .$ . By the small gain theorem, this is true for all $\Delta \in \mathcal { R } \mathcal { H } _ { \infty }$ with $\| \Delta \| _ { \infty } < 1$ only if $\begin{array} { r } { \left\| \boldsymbol { W } _ { 2 } \boldsymbol { K } \boldsymbol { S } _ { o } \boldsymbol { W } _ { 1 } \right\| _ { \infty } \leq 1 } \end{array}$ . ✷

![](image/f4749fd3aa1c143cfb13cda3b7e92b55c74052b70019156ac24552de8930cf4b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    r --> |−| A
    A --> K
    K --> P
    P --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> g
    g --> e
    d_m -.-> C
    W2 --> z
    Δ --> w
    W1 --> D
    Wd --> d
    d̃ --> G
    G --> F
    y --> E
```
</details>

Figure 8.10: Output multiplicative perturbed systems
