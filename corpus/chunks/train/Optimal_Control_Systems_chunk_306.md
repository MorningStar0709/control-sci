```mermaid
graph TD
    subgraph Plant
        u*(k) --> B
        B --> adder
        adder --> z^-1
        z^-1 --> x*(k)
    end
    subgraph Closed-Loop Optimal Controller
        adder --> Lg(k)g(k+1)
        Lg(k)g(k+1) --> g(k+1)
        Lg(k) --> Lg(k)
        Lg(k) --> L(k)
    end
    subgraph Off-Line Simulation of P(k) and g(k)
        g(k+1) --> Adder
        Lg(k) --> Adder
        Adder --> z^-1
        z^-1 --> x*(k)
    end
    z^-1 --> Adder
    Adder --> y*(k)
    style Plant fill:#f9f,stroke:#333
    style Closed-Loop Optimal Controller fill:#ccf,stroke:#333
    style Off-Line Simulation of P(k) and g(k) fill:#cfc,stroke:#333
    note right of Z^k
        Desired z(k)
    end
```
</details>

Figure 5.12 Implementation of Discrete-Time Optimal Tracker
