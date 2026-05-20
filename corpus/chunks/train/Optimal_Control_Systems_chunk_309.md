$$
\begin{array}{l} [ z ^ {- 1} \mathbf {I} - \mathbf {A} ] ^ {\prime} \bar {\mathbf {P}} [ z \mathbf {I} - \mathbf {A} ] + [ z ^ {- 1} \mathbf {I} - \mathbf {A} ] ^ {\prime} \bar {\mathbf {P}} \mathbf {A} + \mathbf {A} ^ {\prime} \bar {\mathbf {P}} [ z \mathbf {I} - \mathbf {A} ] \\ + \mathbf {A} ^ {\prime} \bar {\mathbf {P}} \mathbf {B} \left[ \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \mathbf {B} + \mathbf {R} \right] ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \mathbf {A} = \mathbf {Q}. \tag {5.6.10} \\ \end{array}
$$

![](image/cc77e913ae7035ea1f189026d2c99c95392bb6b8485252528998e8d75797266b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["U(z)"] --> B["[zI - A"]⁻¹B]
    B --> C["X(z)"]
    C --> D["C"]
    D --> E["Y(z)"]
    F["Plant"] --> G["+"]
    G --> H["-"]
    H --> I["L̄"]
    I --> J["Output"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#ffc,stroke:#333
    style F fill:#fff,stroke:#333
    style G fill:#fff,stroke:#333
    style H fill:#fff,stroke:#333
    style I fill:#fff,stroke:#333
    style J fill:#fff,stroke:#333
```
</details>

Figure 5.17 Closed-Loop Discrete-Time Optimal Control System

Premultiplying by $B^{\prime}[z^{-1}I-A]^{-T}$ (where for example, we define $M^{-T}$ as the transpose of $M^{-1}$ ) and postmultiplying by $[zI-A]^{-1}B$ , the previous relation becomes

$$
\begin{array}{l} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \mathbf {B} + \mathbf {B} \bar {\mathbf {P}} \mathbf {A} [ z \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B} + \mathbf {B} ^ {\prime} [ z ^ {- 1} \mathbf {I} - \mathbf {A} ] ^ {- T} \mathbf {A} ^ {\prime} \bar {\mathbf {P}} \mathbf {B} \\ + \mathbf {B} ^ {\prime} [ z ^ {- 1} \mathbf {I} - \mathbf {A} ] ^ {- T} \mathbf {A} ^ {\prime} \bar {\mathbf {P}} \mathbf {B} [ \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \mathbf {B} + \mathbf {R} ] ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \mathbf {A} [ z \mathbf {I} - \mathbf {A} ] \mathbf {B}, \\ = \mathbf {B} ^ {\prime} [ z ^ {- 1} \mathbf {I} - \mathbf {A} ] ^ {- T} \mathbf {Q} [ z \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B}. \tag {5.6.11} \\ \end{array}
$$

Using (5.6.4) in the above, we get
