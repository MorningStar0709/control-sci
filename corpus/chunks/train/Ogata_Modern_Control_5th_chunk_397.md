B–6–15. Determine the values of K, andT1, $T _ { 2 }$ of the system shown in Figure 6–105 so that the dominant closed-loop poles have the damping ratio $\zeta = 0 . 5$ and the undamped natural frequency $\omega _ { n } = 3 \mathrm { r a d / s e c } .$ .

![](image/eb0d5c0f478193e00ba38df384eb249ff8c6f68a1e1754fd56c2c051788eb1dd.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R --> |+| Sum
    Sum --> K["K (T₁s + 1)/(T₂s + 1)"]
    K --> |10/(s(s + 1))| C
    C --> |feedback| Sum
```
</details>

Figure 6–105 Control system.

B–6–16. Consider the control system shown in Figure 6–106. Determine the gain K and time constant T of the controller $G _ { c } ( s )$ such that the closed-loop poles are located at $s = - 2 \pm j 2$ .

![](image/0e8e64d75e0e41d90b16c1c587fe350b0016ee6812e8bd6a2d068d53cfc4aba3.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] --> B["K(Ts + 1)"]
    B --> C["1/(s(s + 2))"]
    C --> D["Output"]
    D --> E["G(s)"]
    E --> F["Feedback"]
    F --> A
```
</details>

Figure 6–106 Control system.

B–6–17. Consider the system shown in Figure 6–107. Design a lead compensator such that the dominant closed-loop poles are located at $s = - 2 \pm j 2 { \sqrt { 3 } }$ Plot the unit-step re-. sponse curve of the designed system with MATLAB.

![](image/9d2fd3757beb71bf63be730137ab8aa45458b9ec0ac1612f72ae3a1d4cd3e84d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] --> B["Gc(s)"]
    B --> C["(5)/(s(0.5s+1))"]
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> A
```
</details>

Figure 6–107 Control system.

B–6–18. Consider the system shown in Figure 6–108. Design a compensator such that the dominant closed-loop poles are located at $s = - 1 \pm j 1$ .

![](image/394fba8dd9e3048779b130655ba8fc7c91554b048e3d82402a56421493e8ce38.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] --> B["Gc(s)"]
    B --> C["1/s²"]
    C --> D["Output"]
    D --> E["Feedback Loop"]
    E --> A
    style A fill:#f9f,stroke:#333
    style C fill:#ccf,stroke:#333
    style E fill:#cff,stroke:#333
```
</details>

Figure 6–108 Control system.

B–6–19. Referring to the system shown in Figure 6–109, design a compensator such that the static velocity error constant $K _ { v } \operatorname { i s } \bar { 2 0 } \sec ^ { - 1 }$ without appreciably changing the original location $( s = - 2 \pm j 2 { \sqrt { 3 } } )$ of a pair of the complex-conjugate closed-loop poles.
