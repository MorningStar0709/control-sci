# A.4 Eliminating a feedback loop

$$Y = P _ {1} (X \mp P _ {2} Y) \tag {A.4}$$

![](image/442dd0562286ce72f023c4fa53402975a8f27451c3f62210bb092d0fd4b2f4ba.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    X --> |+| Sum
    Sum --> P1
    P1 --> Y
    Y --> P2
    P2 --> |−| Sum
    Sum --> |+| +1
```
</details>

Figure A.7: Feedback loop

![](image/138cda2f4d618c980cfedffd56d3644081f759c66fa307752709410d2a775d81.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    X --> A["\frac{P_1}{1 \pm P_1 P 2}"]
    A --> Y
```
</details>

Figure A.8: Simplified feedback loop
