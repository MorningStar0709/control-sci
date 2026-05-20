# A.3 Removing a block from a feedforward loop

$$Y = P _ {1} X \pm P _ {2} X \tag {A.3}$$

![](image/0b268cae8b494d2ec7b783b8707bd0121a211cb2fde76d69a90ecb338758afff.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    X --> P1["P₁"]
    X --> P2["P₂"]
    P1 --> Sum((+))
    P2 --> Sum
    Sum --> Y["Y"]
    P1 -->|±| Sum
```
</details>

Figure A.5: Feedforward loop

![](image/202cf41062c3177a940c0d8b8878fc4c3e996da84a06fa656d4281240db4a607.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    X --> P2["P2"]
    P2 --> P1["P1/P2"]
    P1 --> sum((+))
    sum --> Y
    Y -->|±| sum
    sum -->|feedback| P2
```
</details>

Figure A.6: Transformed feedforward loop
