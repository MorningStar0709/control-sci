```mermaid
graph LR
    A["+"] --> B["Gc(s)"]
    B --> C["(2s + 1)/(s(s + 1) (s + 2))"]
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> A
```
</details>

Figure 6–112   
Control system.

B–6–23. Consider the control system shown in Figure 6–113. Design a compensator such that the unit-step response curve will exhibit maximum overshoot of 25% or less and settling time of 5 sec or less.

![](image/42ed731f9bf51dc0f8072f7bff549dd78feceb9c35b7715532138872a98cf147.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] --> B["Gc(s)"]
    B --> C["1/(s²(s+4))"]
    C --> D
    D --> E
    E --> F
```
</details>

Figure 6–113   
Control system.

B–6–24. Consider the system shown in Figure 6–114, which involves velocity feedback. Determine the values of the amplifier gain K and the velocity feedback gain $K _ { h }$ so that the following specifications are satisfied:

1. Damping ratio of the closed-loop poles is 0.5   
2. Settling time - 2 sec   
3. Static velocity error constant $K _ { v } \geq 5 0 \ \mathrm { s e c } ^ { - 1 }$   
4. $0 < K _ { h } < 1$

![](image/ee629bf6b733d796cef5a74a146cdd14059a53085e63f6c4c693d56d8e670318.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> |+| Sum1
    Sum1 --> |+| Sum2
    Sum2 --> |K/(2s+1)| A["1/s"]
    A --> C["s"]
    C --> |K_h| Sum1
    Sum1 --> |+| Sum2
```
</details>

Figure 6–114   
Control system.

B–6–25. Consider the system shown in Figure 6–115. The system involves velocity feedback. Determine the value of gain K such that the dominant closed-loop poles have a damping ratio of 0.5. Using the gain K thus determined, obtain the unit-step response of the system.

![](image/7bacf16418b3b8fcad8d0b4a33b6fa5dc89d119fdbe2ccfd42edb9e6d0c141a8.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["+"] --> C["+"] --> D["K/(s+1)(s+2)"] --> E["1/s"] --> F["C(s)"]
    F --> G["0.2"]
    G --> B
    B --> H["+"]
    H --> I["-"]
    I --> C
```
</details>

Figure 6–115 Control system.

B–6–26. Consider the system shown in Figure 6–116. Plot the root loci as a varies from 0 to q. Determine the value of a such that the damping ratio of the dominant closed-loop poles is 0.5.

![](image/4417dc3217a53d51782d29744970d2ed1ad47af56640d7bd8dc363254561675d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] --> B["s + a"]
    B --> C["2/(s²(s + 2))"]
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> A
```
</details>

Figure 6–116 Control system.
