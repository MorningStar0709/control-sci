# 1. 结构

专家控制的基本结构如图 2-2 所示。

![](image/99bdf0c239f754fa49a25a31b80a2798e03a9022fc4d2eef71d20b727da8a8e9.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["知识库"] <--> B["实时推理机"]
    B <--> C["控制算法库"]
    C --> D["D/A"]
    D <--> E["被控对象"]
    E <--> F["A/D"]
    F --> A
```
</details>

图 2-2 专家控制的基本结构
