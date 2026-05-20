In sketching curves, assume that the numerical values of $K _ { p } ,$ $K _ { i } , T _ { i }$ and, $T _ { d }$ are given as

$$K _ {p} = \text { proportional gain } = 4K _ {i} = \text { integral gain } = 2T _ {i} = \text { integral time } = 2 \secT _ {d} = \text { derivative time } = 0. 8 \sec$$

B–2–5. Figure 2–32 shows a closed-loop system with a reference input and disturbance input. Obtain the expression for the output $C ( s )$ when both the reference input and disturbance input are present.   
B–2–6. Consider the system shown in Figure 2–33. Derive the expression for the steady-state error when both the reference input $R ( s )$ and disturbance input $D ( s )$ are present.   
B–2–7. Obtain the transfer functions $C ( s ) / R ( s )$ and $C ( s ) / D ( s )$ of the system shown in Figure 2–34.

Figure 2–32 Closed-loop system.   
![](image/ab9b8062e6e75eae3fa3964f159b025ff384a5bce27f0b9ab88216566cd40290.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> |+| Sum1
    Sum1 --> Gc["Gc(s)"]
    Gc --> Gp["Gp(s)"]
    Gp --> |+| Sum2
    Sum2 --> C["s"]
    D["s"] --> |+| Sum1
    Sum1 --> Controller["Controller"]
    Controller --> Gc
    Controller --> Gp
    Gc --> Plant["Plant"]
    Gp --> Plant
```
</details>

Figure 2–33 Control system.   
![](image/3e1b9dfd0c859f17daf4f8d95a3ab0754cf86ac90a67e2de0b0e31eedec95cc1.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> A["+"] --> E["s"] --> G1["s"] --> A["+"] --> G2["s"] --> C["s"]
    D["s"] --> A["+"] --> G1["s"] --> A["+"] --> G2["s"] --> C["s"]
    C["s"] --> A["+"] --> G1["s"] --> A["+"] --> G2["s"] --> A["+"] -->|feedback| A["+"] -->|feedback| B["-"]
```
</details>

![](image/22af7d14a5dd3b1876567a794283b9ec6d7b241cdb4d7e6f40325532e3febfe3.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> A["+"]
    A --> B["Gc"]
    B --> C["+"]
    C --> D["G1"]
    D --> E["+"]
    E --> F["G2"]
    F --> G["G3"]
    G --> H["C(s)"]
    H --> I["H1"]
    I --> J["H2"]
    J --> A
    D["s"] --> K["D(s)"]
    K --> L["+"]
    L --> M["G1"]
    M --> N["+"]
    N --> O["G2"]
    O --> P["G3"]
    P --> Q["C(s)"]
    Q --> R["H1"]
    R --> S["H2"]
    S --> T["+"]
    T --> U["G1"]
    U --> V["+"]
    V --> W["G2"]
    W --> X["G3"]
    X --> Y["H1"]
    Y --> Z["H2"]
```
</details>

Figure 2–34 Control system.

B–2–8. Obtain a state-space representation of the system shown in Figure 2–35.

![](image/aef591ccebb0a8040d8572ffee9ba252a331ed7b8668f5a0a8978c231de770c1.jpg)

<details>
<summary>flowchart</summary>
