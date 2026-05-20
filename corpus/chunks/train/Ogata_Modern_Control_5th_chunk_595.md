```mermaid
graph LR
    A["Reference input R(s)"] --> B["+"]
    B --> C["PID controller"]
    C --> D["+"]
    D --> E["Plant Gp(s)"]
    E --> F["Output Y(s)"]
    F --> G["Noise N(s)"]
    G --> H["Observed signal B(s)"]
    H --> I["-"]
    I --> B
    J["Disturbance D(s)"] --> D
```
</details>

![](image/d60665a461fe5ac3d78f5fcb3473e462275d89801817d2bc0972e5546f83d4d9.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> A["+"] --> E["s"] --> B["-"] --> C["1"]
    E["s"] --> D["1/(Ti*s)"] --> A
    E["s"] --> E
    E["s"] --> F["Td*s"] --> G["+"] --> Kp["Kp"] --> U["s"] --> Gp["Gp(s)"] --> Y["s"]
    U["s"] --> Gp
    Gp --> N["s"]
    N["s"] --> O["+"] --> Kp
    Kp --> O
    O --> P["+"] --> D["s"]
    D["s"] --> P
    P --> Q["D(s)"]
```
</details>

Figure 8–25

(a) PID-controlled system;

(b) equivalent block diagram.

Figure 8–26 PI-D-controlled system.   
![](image/9265e047fd34695dcbbd8b958dfa7c6f0471f07be62fa4cda7e070d0aeb10aca.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> A["+"] --> E["s"] --> B["1/Ti s"] --> C["+"] --> Kp["Kp"] --> U["s"] --> Gp["Gp(s)"] --> Y["s"]
    Y["s"] --> N["s"] --> B["s"] --> Tds["Tds"] --> C
    D["s"] --> Gp
    U["s"] --> Gp
    Gp --> Y["s"]
    style A fill:#f9f,stroke:#333
    style B fill:#f9f,stroke:#333
    style C fill:#f9f,stroke:#333
    style D fill:#f9f,stroke:#333
    style E fill:#ccf,stroke:#333
    style F fill:#ccf,stroke:#333
    style G fill:#ccf,stroke:#333
    style H fill:#cfc,stroke:#333
    style I fill:#cfc,stroke:#333
    style J fill:#cfc,stroke:#333
    style K fill:#cfc,stroke:#333
    style L fill:#cfc,stroke:#333
    style M fill:#cfc,stroke:#333
    style N fill:#cfc,stroke:#333
```
</details>

Notice that in the absence of the disturbances and noises, the closed-loop transfer function of the basic PID control system [shown in Figure 8–25(b)] and the PI-D control system (shown in Figure 8–26) are given, respectively, by

$$\frac {Y (s)}{R (s)} = \left(1 + \frac {1}{T _ {i} s} + T _ {d} s\right) \frac {K _ {p} G _ {p} (s)}{1 + \left(1 + \frac {1}{T _ {i} s} + T _ {d} s\right) K _ {p} G _ {p} (s)}$$

and

$$\frac {Y (s)}{R (s)} = \left(1 + \frac {1}{T _ {i} s}\right) \frac {K _ {p} G _ {p} (s)}{1 + \left(1 + \frac {1}{T _ {i} s} + T _ {d} s\right) K _ {p} G _ {p} (s)}$$

It is important to point out that in the absence of the reference input and noises, the closed-loop transfer function between the disturbance D(s) and the output Y(s) in either case is the same and is given by
