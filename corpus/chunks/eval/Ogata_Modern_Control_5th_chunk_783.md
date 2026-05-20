```mermaid
graph TD
    u --> B
    u --> -K
    B --> add1["+"]
    add1 --> int["x"]
    int --> C
    C --> y
    y --> A
    A --> int
    int --> F["F"]
    F --> add2["+"]
    add2 --> int
    int --> Ĉ
    Ĉ --> add3["+"]
    add3 --> int
    int --> A["A"]
    A --> add4["+"]
    add4 --> int
    int --> Ĉ
    Ĉ --> add5["+"]
    add5 --> int
    int --> B["B"]
    B --> x
    x --> C
    x --> A
    x --> B
    x --> A
    x --> B
    x --> A
    style x fill:#f9f,stroke:#333
    style y fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style B fill:#fcc,stroke:#333
    style F fill:#cff,stroke:#333
    style Ĉ fill:#ffc,stroke:#333
    style A fill:#fcc,stroke:#333
    style B fill:#fff,stroke:#333
    style C fill:#fff,stroke:#333
    style D fill:#fff,stroke:#333
    style E fill:#fff,stroke:#333
    style F fill:#fff,stroke:#333
    style G fill:#fff,stroke:#333
    style H fill:#fff,stroke:#333
    style I fill:#fff,stroke:#333
    style J fill:#fff,stroke:#333
    style K fill:#fff,stroke:#333
    style L fill:#fff,stroke:#333
    style M fill:#fff,stroke:#333
    style N fill:#fff,stroke:#333
    style O fill:#fff,stroke:#333
    style P fill:#fff,stroke:#333
    style Q fill:#fff,stroke:#333
    style R fill:#fff,stroke:#333
    style S fill:#fff,stroke:#333
    style T fill:#fff,stroke:#333
    style U fill:#fff,stroke:#333
    style V fill:#fff,stroke:#333
    style W fill:#fff,stroke:#333
    style X fill:#fff,stroke:#333
    style Y fill:#fff,stroke:#333
    style Z fill:#fff,stroke:#333
```
</details>

By subtracting Equation (10–92) from Equation (10–84), we obtain

$$\dot {\mathbf {x}} _ {b} - \tilde {\dot {\mathbf {x}}} _ {b} = \left(\mathbf {A} _ {b b} - \mathbf {K} _ {e} \mathbf {A} _ {a b}\right) \left(\mathbf {x} _ {b} - \tilde {\mathbf {x}} _ {b}\right) \tag {10-93}$$

Define

$$\mathbf {e} = \mathbf {x} _ {b} - \widetilde {\mathbf {x}} _ {b} = \boldsymbol {\eta} - \widetilde {\boldsymbol {\eta}}$$

Then Equation (10–93) becomes

$$\dot {\mathbf {e}} = \left(\mathbf {A} _ {b b} - \mathbf {K} _ {e} \mathbf {A} _ {a b}\right) \mathbf {e} \tag {10-94}$$

This is the error equation for the minimum-order observer. Note that e is an (n-1)- vector.

The error dynamics can be chosen as desired by following the technique developed for the full-order observer, provided that the rank of matrix

$$
\left[ \begin{array}{c} \mathbf {A} _ {a b} \\ \mathbf {A} _ {a b} \mathbf {A} _ {b b} \\ \cdot \\ \cdot \\ \cdot \\ \mathbf {A} _ {a b} \mathbf {A} _ {b b} ^ {n - 2} \end{array} \right]
$$

is n-1. (This is the complete observability condition applicable to the minimum-order observer.)
