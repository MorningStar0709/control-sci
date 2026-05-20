```mermaid
graph TD
    yd --> R
    R --> sum1
    sum1 --> u
    u --> P
    P --> sum2
    sum2 --> y
    y --> v
    v --> sum3
    sum3 --> sum1
    sum1 --> F
    F --> sum2
    sum2 --> d
```
</details>

Figure 4.31 An alternate 2-DOF structure

4.36 Figure 4.32 shows yet another 2-DOF structure.

a. Show that, if R, F, and P are minimally realized, the system is controllable from the inputs $y_{d}$ , $v_{1}$ , and $v_{2}$ , and observable from the outputs y, $z_{1}$ , and $z_{2}$ .   
b. Calculate as functions of $R, P, P^{-1}, T$ , and $S$ the elements of the $3 \times 3$ matrix transfer function with inputs and outputs as in part (b).   
c. Show that the system is internally stable if, and only if, T, S, PS, $P^{-1}T$ , and R are stable.

![](image/77f63c9f9c5a0843cf17f13b32eb8ec17209c24e4ad227d101b3f616294a8cb2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    yd --> +1["+"]
    +1 --> F["F"]
    F --> +2["+"]
    +2 --> P["P"]
    P --> y
    y --> +3["+"]
    +3 --> v2["v2"]
    v1 --> +2
    z1 --> P
    z2 --> +2
    R --> F
    +2 --> +2
    +2 --> +3
```
</details>

Figure 4.32 An alternate 2-DOF structure
