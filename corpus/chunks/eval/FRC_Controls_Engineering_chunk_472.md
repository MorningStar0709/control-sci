# A.5 Removing a block from a feedback loop

$$Y = P _ {1} (X \mp P _ {2} Y) \tag {A.5}$$

![](image/223ec1085725130c979a235f50e38edf47891dd8ef23c7fdb08d5a9ec7246dcb.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    X --> |+| Sum
    Sum --> P1["P₁"]
    P1 --> Y
    Y --> P2["P₂"]
    P2 --> |−| Sum
    Sum --> |±| P2
```
</details>

Figure A.9: Feedback loop

![](image/e03ed46f1be75d1ce3677c4004c8edc41f50cba4065e732672b74afe2da2399a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    X --> A["1/P2"]
    A --> B["+"]
    B --> C["P1P2"]
    C --> Y
    Y --> D["Feedback to +"]
    D --> B
```
</details>

Figure A.10: Transformed feedback loop
