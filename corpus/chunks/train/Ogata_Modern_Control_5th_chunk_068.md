# EXAMPLE PROBLEMS AND SOLUTIONS

A–2–1. Simplify the block diagram shown in Figure 2–17.

Solution. First, move the branch point of the path involving $H _ { 1 }$ outside the loop involving $H _ { 2 }$ , as shown in Figure 2–18(a). Then eliminating two loops results in Figure 2–18(b). Combining two blocks into one gives Figure 2–18(c).

A–2–2. Simplify the block diagram shown in Figure 2–19. Obtain the transfer function relating C(s) and $R ( s )$ .

Figure 2–17 Block diagram of a system.   
![](image/42f0d965ba9af2b2efd7f5e56e506215138bb418d5c3c75980ef85582fcce0e8.jpg)  
Figure 2–18   
Simplified block diagrams for the system shown in Figure 2–17.

Figure 2–19 Block diagram of a system.

![](image/ac61bab04b1cd5b43f659b0e9ac671e83d9c5b995959841af2c0dd9cfecc4e8a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> G1["G₁"]
    G1 --> Sum1["+"]
    Sum1 --> G2["G₂"]
    G2 --> Sum2["+"]
    Sum2 --> C["s"]
    C["s"] -->|feedback| G1
    C["s"] -->|feedback| Sum1
```
</details>

![](image/0ee3b2efa1e146db3ae60c7b12ed1648613709750011ee16cf9f43155840b315.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> G1["G₁ + 1"]
    G1 --> G2["G₂"]
    G2 --> Sum((+/-))
    Sum --> C["C(s)"]
    C -->|feedback| R["s"]
```
</details>

![](image/cc7dabf57c47fa4b65b538f1f0ad94f2b918450579825c251e780ed4a88e67f5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["G₁G₂ + G₂ + 1"]
    B --> C["C(s)"]
```
</details>

(c)   
Figure 2–20 Reduction of the block diagram shown in Figure 2–19.

Solution. The block diagram of Figure 2–19 can be modified to that shown in Figure 2–20(a). Eliminating the minor feedforward path, we obtain Figure 2–20(b), which can be simplified to Figure 2–20(c). The transfer function $C ( s ) / R ( s )$ is thus given by

$$\frac {C (s)}{R (s)} = G _ {1} G _ {2} + G _ {2} + 1$$

The same result can also be obtained by proceeding as follows: Since signal X(s) is the sum of two signals $G _ { 1 } R ( s )$ and $R ( s )$ , we have

$$X (s) = G _ {1} R (s) + R (s)$$

The output signal C(s) is the sum of $G _ { 2 } X ( s )$ and $R ( s )$ . Hence

$$C (s) = G _ {2} X (s) + R (s) = G _ {2} \left[ G _ {1} R (s) + R (s) \right] + R (s)$$

And so we have the same result as before:

$$\frac {C (s)}{R (s)} = G _ {1} G _ {2} + G _ {2} + 1$$

A–2–3. Simplify the block diagram shown in Figure 2–21. Then obtain the closed-loop transfer function $C ( s ) / R ( s )$ .
