![](image/ab77114326036e2195b61294fe15a99a859f14b0ef9c4f1be234a9cc917f9dfb.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> A["+"] --> G1["G₁"] --> B["+"] --> G2["G₂"] --> C["+"] --> G3["G₃"] --> G4["G₄"] --> C["s"]
    C["s"] --> H1["H₁"] --> A
    C["s"] --> H2["H₂"] --> B
    C["s"] --> H3["H₃"] --> B
    B --> A
    B --> G2
    B --> G3
    B --> G4
```
</details>

Figure 2–21 Block diagram of a system.

![](image/7cf177d2c0c42eb15a576b61f50e3963e3c397bb5d97310c408d07d073dbc67c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    R["s"] --> |+| Sum1
    Sum1 --> |+| G1["G1"]
    G1 --> G2["G2"]
    G2 --> |+| Sum2
    Sum2 --> G3["G3"]
    G3 --> G4["G4"]
    G4 --> C["s"]
    C["s"] --> |−| H1["H1"]
    H1 --> |+| Sum1
    H2["H2"] --> |−| Sum2
    H3["H3"] --> |+| Sum1
    Sum1 --> |+| G1
    Sum1 --> |+| G2
    Sum1 --> |+| G3
    Sum1 --> |+| G4
    G1 --> |−| H1
    G2 --> |−| H2
    G3 --> |−| H3
    G4 --> |−| H3
    H1 --> |−| Sum2
    H2 --> |−| Sum2
    H3 --> |−| Sum2
```
</details>

![](image/80050f0c798ee2ddeb8aeb1bc3da7dc0cacf1364664cec6114e3de88a402ae78.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> |+| Sum
    Sum --> G1["G1 G2 / (1 + G1 G2 H1)"]
    G1 --> G3["G3 G4 / (1 + G3 G4 H2)"]
    G3 --> C["s"]
    C --> |−| Sum
    H3["H3 / G1 G4"] --> Sum
```
</details>

Figure 2–22 Successive reductions of the block diagram shown in Figure 2–21.

![](image/ff76751e316225a6eaeef37293b9b0549ea7ee10ff311624c3b885b8678ee9e5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["Block: G1 G2 G3 G4 / (1 + G1 G2 H1 + G3 G4 H2 - G2 G3 H3 + G1 G2 G3 G4 H1 H2)"]
    B --> C["C(s)"]
```
</details>

Solution. First move the branch point between $G _ { 3 }$ and $G _ { 4 }$ to the right-hand side of the loop containing $G _ { 3 } , G _ { 4 }$ , and $H _ { 2 }$ . Then move the summing point between $G _ { 1 }$ and $G _ { 2 }$ to the left-hand side of the first summing point. See Figure 2–22(a). By simplifying each loop, the block diagram can be modified as shown in Figure 2–22(b). Further simplification results in Figure 2–22(c), from which the closed-loop transfer function $C ( s ) / R ( s )$ is obtained as

$$\frac {C (s)}{R (s)} = \frac {G _ {1} G _ {2} G _ {3} G _ {4}}{1 + G _ {1} G _ {2} H _ {1} + G _ {3} G _ {4} H _ {2} - G _ {2} G _ {3} H _ {3} + G _ {1} G _ {2} G _ {3} G _ {4} H _ {1} H _ {2}}$$

A–2–4. Obtain transfer functions $C ( s ) / R ( s )$ and $C ( s ) / D ( s )$ of the system shown in Figure 2–23.

Solution. From Figure 2–23 we have
