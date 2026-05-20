Determine the controllers $G _ { c 1 } ( s )$ and $G _ { c 2 } ( s )$ such that, for the step disturbance input, the response shows a small amplitude and approaches zero quickly (in a matter of 1 to 2 sec). For the response to the unit-step reference input, it is desired that the maximum overshoot be 20% or less and the settling time 1 sec or less. For the ramp reference input and acceleration reference input, the steady-state errors should be zero.

B–8–15. Consider the two-degrees-of-freedom control system shown in Figure 8–82. Design controllers $G _ { c 1 } ( s )$ and $G _ { c 2 } ( s )$ such that the response to the step disturbance input shows a small amplitude and settles to zero quickly (in 1 to 2 sec) and the response to the step reference input exhibits 25% or less maximum overshoot and the settling time is less than 1 sec.The steady-state error in following the ramp reference input or acceleration reference input should be zero.

![](image/3fd8804b6c03c40f866b108fa4a6f98eb4b0d115ece3727b88c0447bcdd1e233.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> |+| A["+"]
    A --> Gc1["Gc1(s)"]
    Gc1 --> |+| B["+"]
    B --> U["s"]
    D["s"] --> |+| C["+"]
    C --> Gp["Gp(s)"]
    Gp --> Y["s"]
    Y["s"] --> |+| A
    U["s"] --> |+| B
    B --> Gc2["Gc2(s)"]
    Gc2 --> |+| A
```
</details>

Figure 8–81 Two-degrees-of-freedom control system.

![](image/3663ee15fedec28bcc84ef5f205aa9502c5df8621231eb9ba20fa556550c480a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["R(s)"] --> A["+"] --> C1["C₁(s)"] --> A2["+"] --> D["D(s)"] --> B["1/s²"] --> Y["Y(s)"]
    C1 --> A2
    A2 --> C2["C₂(s)"] --> B
    B --> C2
```
</details>

Figure 8–82 Two-degrees-of-freedom control system.

![](image/a0dc3022936143228bffeb31c78cf87223d6a1d11920033a710299b1cf861c7b.jpg)

<details>
<summary>text_image</summary>

9
</details>
