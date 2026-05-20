```mermaid
graph LR
    A["+"] --> B["+"] --> C["10/(s+1)(s+5)"] --> D["1/s"] --> E["k"]
    E --> A
    A --> F["+ -"]
    F --> G["+ -"]
    G --> H["k"]
    H --> A
```
</details>

Figure 7–160   
Control system.

B–7–21. Consider the system defined by

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} - 1 & - 1 \\ 6. 5 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c c} 1 & 1 \\ 1 & 0 \end{array} \right] \left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right]

\left[ \begin{array}{c} y _ {1} \\ y _ {2} \end{array} \right] = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c c} 0 & 0 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right]
$$

There are four individual Nyquist plots involved in this system. Draw two Nyquist plots for the input $u _ { 1 }$ in one diagram and two Nyquist plots for the input $u _ { 2 }$ in another diagram. Write a MATLAB program to obtain these two diagrams.

B–7–25. Consider the system shown in Figure 7–162. Draw a Bode diagram of the open-loop transfer function $G ( s )$ . Determine the phase margin and gain margin with MATLAB.

![](image/4dcad47a39bb6f74ecd2833bef893c1a98b538e96c36db790f4a64ee1aa6af8e.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] --> B["20(s + 1) / (s(s² + 2s + 10) (s + 5))"]
    B --> C["G(s)"]
    C --> A
```
</details>

Figure 7–162   
Control system.

B–7–26. Consider a unity-feedback control system with the open-loop transfer function

$$G (s) = \frac {K}{s \left(s ^ {2} + s + 4\right)}$$

Determine the value of the gain K such that the phase margin is 50°. What is the gain margin with this gain K?

B–7–27. Consider the system shown in Figure 7–163. Draw a Bode diagram of the open-loop transfer function, and determine the value of the gain K such that the phase margin is 50°. What is the gain margin of this system with this gain K?

![](image/09b9796e9a69f71b342f8b02907e7d53cea40a384a113c373f54fd46f9e35ed3.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] --> B["K (s + 0.1)/(s + 0.5)"]
    B --> C["(10)/(s(s+1))"]
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

Figure 7–163 Control system.
