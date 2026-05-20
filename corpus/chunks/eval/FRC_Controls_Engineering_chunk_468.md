# A.1 Cascaded blocks

$$Y = (P _ {1} P _ {2}) X \tag {A.1}$$

![](image/7401ac51c1698eb06cdacf62500fce5c3fb449752d84357f2042902c8c2ef1e7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    X --> P1
    P1 --> P2
    P2 --> Y
```
</details>

Figure A.1: Cascaded blocks

![](image/353f755597281dbc4d1a3063e76f36a9b8d03e236966e364e2ba32d29380e8c2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    X --> P1["P₁P₂"]
    P1 --> Y
```
</details>

Figure A.2: Simplified cascaded blocks
