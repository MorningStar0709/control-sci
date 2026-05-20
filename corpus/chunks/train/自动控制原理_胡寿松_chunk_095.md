# (4) 比较点和引出点的移动

在系统结构图简化过程中,有时为了便于进行方框的串联、并联或反馈连接的运算,需要移动比较点或引出点的位置。这时应注意在移动前后必须保持信号的等效性，而且比较点和引出点之间一般不宜交换其位置。此外，“一”号可以在信号线上越过方框移动，但不能越过比较点和引出点。

![](image/da0daeb098ff721089f70653929185b0362b958876cd0f6fa7381a9e65601279.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> A((+))
    A --> E["s"]
    E["s"] --> G["s"]
    G["s"] --> C["s"]
    C["s"] --> H["s"]
    H["s"] --> B["s"]
    B["s"] --> ±[±]
    ± --> A
```
</details>

(a)

![](image/defb8a0c76b17605234fd1297abb00567a1f93d4a72c7fd3f46c3eda4ea15d40.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["Block: G(s) / |∓ G(s) H(s)"]
    B --> C["C(s)"]
```
</details>

(b)   
图 2-26 方框的反馈连接及其简化

表 2-1 汇集了结构图简化(等效变换)的基本规则,可供查用。

表 2-1 结构图简化(等效变换)规则
