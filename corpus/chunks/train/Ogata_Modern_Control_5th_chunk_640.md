```mermaid
graph TD
    A["R(s)"] --> B["+"]
    B --> C["G1(s)"]
    C --> D["+"]
    D --> E["G2(s)"]
    E --> F["C(s)"]
    F --> G["+"]
    G --> H["H(s)"]
    H --> B
    I["Disturbance D(s)"] --> D
    J["Noise N(s)"] --> G
```
</details>

Figure 8–74 Control system.

B–8–7. Consider the system shown in Figure 8–75. Obtain the closed-loop transfer function $C ( s ) / R ( s )$ for the reference input and the closed-loop transfer function $C ( s ) / D ( s )$ for the disturbance input. When considering $R ( s )$ as the input, assume that $D ( s )$ is zero, and vice versa.

B–8–8. Consider the system shown in Figure $8 \mathrm { - } 7 6 ( \mathrm { a } )$ , where K is an adjustable gain and $G ( s )$ and $H ( s )$ are fixed

components. The closed-loop transfer function for the disturbance is

$$\frac {C (s)}{D (s)} = \frac {1}{1 + K G (s) H (s)}$$

To minimize the effect of disturbances, the adjustable gain K should be chosen as large as possible.

Is this true for the system in Figure $8 - 7 6 ( \mathrm { b } )$ , too?

![](image/52072957a807406081b6d9bca99a3c6f1e1715c4b1e297038d17db98121f724a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> A["+"] --> G1["s"] --> A["+"] --> G2["s"] --> C["+"] --> G3["s"] --> C["s"]
    D["s"] --> C["s"]
    C["s"] --> H2["s"]
    H2["s"] --> A["+"] --> G2["s"] --> A["+"] --> G3["s"] --> C["s"]
    C["s"] --> H1["s"]
    H1["s"] --> A["+"] --> G1["s"] --> A["+"] --> G2["s"] --> A["+"] --> G3["s"] --> C["s"]
    A["+"] --> G1["s"]
    A["+"] --> G2["s"]
    A["+"] --> G3["s"]
    G1["s"] --> A["+"]
    G2["s"] --> A["+"]
    G3["s"] --> A["+"]
    H2["s"] --> A["+"]
    H1["s"] --> A["+"]
```
</details>

Figure 8–75 Control system.

![](image/29b0015c659b00f67ecc695d5552a6f6db42129e103b3eab87ed209d1d2b49f0.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    subgraph (a)
        R["s"] --> |+| Sum1
        Sum1 --> K["K"]
        K --> G["s"]
        G["s"] --> |+| Sum2
        Sum2 --> C["s"]
        D["s"] --> |+| Sum1
        Sum1 --> H["s"]
        H["s"] --> |+| Sum2
        Sum2 --> C["s"]
    end
    subgraph (b)
        R["s"] --> |+| Sum3
        Sum3 --> K["K"]
        K --> G["s"]
        G["s"] --> |+| Sum4
        Sum4 --> C["s"]
        H["s"] --> |+| Sum5
        Sum5 --> D["s"]
        D["s"] --> |+| Sum3
        Sum3 --> C["s"]
    end
```
</details>

Figure 8–76 (a) Control system with disturbance entering in the feedforward path; (b) control system with disturbance entering in the feedback path.
