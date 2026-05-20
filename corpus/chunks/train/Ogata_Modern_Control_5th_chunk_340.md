![](image/e4a02f110e9265135bced1df0e4ed09bc42f22e6329ac7c387167dcf0f37973b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] --> B["Gc(s)"]
    B --> C["G(s)"]
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
```
</details>

Figure 6–47 Control system.

$$G (s) = \frac {1 . 0 6}{s (s + 1) (s + 2)}$$

The root-locus plot for the system is shown in Figure 6–48(b). The closed-loop transfer function becomes

$$
\begin{array}{l} \frac {C (s)}{R (s)} = \frac {1 . 0 6}{s (s + 1) (s + 2) + 1 . 0 6} \\ = \frac {1 . 0 6}{(s + 0 . 3 3 0 7 - j 0 . 5 8 6 4) (s + 0 . 3 3 0 7 + j 0 . 5 8 6 4) (s + 2 . 3 3 8 6)} \\ \end{array}
$$

The dominant closed-loop poles are

$$s = - 0. 3 3 0 7 \pm j 0. 5 8 6 4$$

The damping ratio of the dominant closed-loop poles is $\zeta = 0 . 4 9 1$ The undamped natural. frequency of the dominant closed-loop poles is 0.673 radsec.The static velocity error constant is 0.53 sec–1.

It is desired to increase the static velocity error constant $K _ { v }$ to about 5 sec–1 without appreciably changing the location of the dominant closed-loop poles.

To meet this specification, let us insert a lag compensator as given by Equation (6–19) in cascade with the given feedforward transfer function. To increase the static velocity error constant by a factor of about 10, let us choose $\beta = 1 0$ and place the zero and pole of the lag compensator at s=–0.05 and s=–0.005, respectively.The transfer function of the lag compensator becomes

$$G _ {c} (s) = \hat {K} _ {c} \frac {s + 0 . 0 5}{s + 0 . 0 0 5}$$

![](image/8d5fb4c32d23dd7206a5169371ead873ce038e6db77bbe7af1f4e2b4e03a1346.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["+"] --> B["1.06/(s(s+1)(s+2))"]
    B --> C["σ"]
    D["Closed-loop poles"] --> E["jω"]
    E --> F["j2"]
    E --> G["j1"]
    E --> H["-j1"]
    E --> I["-j2"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#ffc,stroke:#333
    style F fill:#fcc,stroke:#333
    style G fill:#fcc,stroke:#333
    style H fill:#fcc,stroke:#333
    style I fill:#fcc,stroke:#333
    style J fill:#fff,stroke:#333
```
</details>

Figure 6–48   
(a) Control system;   
(b) root-locus plot.

Figure 6–49   
Compensated system.   
![](image/71d6d67e2a7a0f4cf0443fb2127f6c40e50a3cce3736335904c1120a137a6146.jpg)

<details>
<summary>flowchart</summary>
