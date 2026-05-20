# 6.1 多级决策的例子——最短时间问题

为了便于理解动态规划的思想,首先来研究图6-1所示的最短时间问题。设有人要从A点开车到E站,中间要经过任意三个中间站,站名在图中圆圈内表示。站与站之间称为段,每段路程所需时间(小时)标在段上。现要问,这人应如何选择路线才能最快到达目的地?

![](image/5e9f9b52412c6de7392bfa702e9af1aec7069f6402f5222421dd7b065c26ad5c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["节点A"] -->|3| B1["节点B1"]
    A -->|1| B2["节点B2"]
    B1 -->|4| C1["节点C1"]
    B2 -->|6| C2["节点C2"]
    C1 -->|1| D1["节点D1"]
    C2 -->|2| D1
    C2 -->|3| D2["节点D2"]
    D1 -->|5| E["节点E"]
    D2 -->|4| C3["节点C3"]
    E -->|1| D2
    style A fill:#f9f,stroke:#333
    style B1 fill:#f9f,stroke:#333
    style B2 fill:#f9f,stroke:#333
    style C1 fill:#ccf,stroke:#333
    style C2 fill:#ccf,stroke:#333
    style D1 fill:#ccf,stroke:#333
    style D2 fill:#ccf,stroke:#333
    style E fill:#ccf,stroke:#333
    note right of A: 由B1到E的最短时间
```
</details>

图6-1 按最短时间的路径选择
