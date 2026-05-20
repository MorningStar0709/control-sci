# EXAMPLE 2–1

Consider the system shown in Figure 2–13(a). Simplify this diagram.

By moving the summing point of the negative feedback loop containing $H _ { 2 }$ outside the positive feedback loop containing $H _ { 1 } ,$ , we obtain Figure 2–13(b). Eliminating the positive feedback loop, we have Figure 2–13(c).The elimination of the loop containing $H _ { 2 } / G _ { 1 }$ gives Figure 2–13(d). Finally, eliminating the feedback loop results in Figure 2–13(e).

![](image/860a6998a5c136cc03b14f0862f8eb6ca70f77e1de68496f98310e752d9195c3.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R --> |+| A["+"]
    A --> |+| B["+"]
    B --> G1["G₁"]
    G1 --> |+| C["+"]
    C --> G2["G₂"]
    G2 --> G3["G₃"]
    G3 --> C
    H1["H₁"] --> C
    H2["H₂"] --> C
```
</details>

![](image/7bf0aaef2c36d2869750014d3878567297af7dece25c27368c2c5548b2177d59.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    R --> |+| A["+"]
    A --> |-| B["+"]
    B --> |+| C["+"]
    C --> G1["G1"]
    G1 --> G2["G2"]
    G2 --> G3["G3"]
    G3 --> C
    H1 --> |+| C
    H2["G1"] --> G1
    H2 --> G3
```
</details>

![](image/71add5d04c5c74d2eb3800a2eacabf1787251e90a0a250330267e9a513eed6b2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R --> |+| A["+"]
    A --> |-| B["+"]
    B --> C["G1G2/(1-G1G2H1)"]
    C --> D["G3"]
    D --> C
    D --> E["H2/G1"]
    E --> A
```
</details>

![](image/1731ef5d4d6356770a94106f690a6ebc94b783ab0c1a95d063b73695346ada71.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R --> |+ -| A["Transfer Function"]
    A --> B["G1G2G3 / (1 - G1G2H1 + G2G3H2)"]
    B --> C["C"]
    C --> A
```
</details>

![](image/d76e19e7f68eb29eca76f399033590f84990b082f51909d477b6ee0fd9434a3a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R"] --> B["\frac{G_1G_2G_3}{1 - G_1G_2H_1 + G_2G_3H_2 + G_1G_2G_3}"]
    B --> C["C"]
```
</details>

Figure 2–13 (a) Multiple-loop system; (b)–(e) successive reductions of the block diagram shown in (a).

Notice that the numerator of the closed-loop transfer function $C ( s ) / R ( s )$ is the product of the transfer functions of the feedforward path. The denominator of $C ( s ) / R ( s )$ is equal to

$$1 + \sum (\text { product of the transfer functions around each loop })= 1 + \left(- G _ {1} G _ {2} H _ {1} + G _ {2} G _ {3} H _ {2} + G _ {1} G _ {2} G _ {3}\right)= 1 - G _ {1} G _ {2} H _ {1} + G _ {2} G _ {3} H _ {2} + G _ {1} G _ {2} G _ {3}$$

(The positive feedback loop yields a negative term in the denominator.)
