# A.2 Combining blocks in parallel

$$Y = P _ {1} X \pm P _ {2} X \tag {A.2}$$

![](image/98f552119c10d86ccbdb05528fd5cc92e56384adfc99d7d8c619d9d022d28b19.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    X --> P1["P₁"]
    X --> P2["P₂"]
    P1 --> Sum((+))
    P2 --> Sum
    Sum --> Y
    Sum --> ±[±]
```
</details>

Figure A.3: Parallel blocks

![](image/aa66270cc6a2162d5119b3d9fb792fc30a81e26edea555f5c25c1af9dce8a628.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    X --> P1[" P₁ ± P₂ "]
    P1 --> Y
```
</details>

Figure A.4: Simplified parallel blocks
