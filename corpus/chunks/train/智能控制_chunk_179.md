# 1. 单变量模糊控制器

在单变量模糊控制器(Single Variable Fuzzy Controller, SVFC)中, 将其输入变量的个数定义为模糊控制的维数, 如图 4-5 所示。

![](image/3660c97dd06a75fc390fe8e3577ac04244f22471591a0df9f5e180c16d541304.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["e"] --> B["一维模糊控制器"]
    B --> C["u"]
```
</details>

(a) 一维模糊控制器

![](image/0637efb7045f5e694c067c6b271e464483323b79dd84ca49bad999490c63d057.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    e --> d/dt
    d/dt --> 二维模糊控制器
    二维模糊控制器 --> u
    二维模糊控制器 -->|e| e
    二维模糊控制器 -->|ec| e
```
</details>

(b) 二维模糊控制器

![](image/ffd71a9659e7142ecc94aa39fa652ab1b0383198bfe136f5c7e355cda6e1ad63.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    e --> A["d/dt"]
    A --> B["..."]
    B --> C["三维模糊控制器"]
    C --> u
    A --> D["d/dt"]
    D --> E["ecc"]
    C --> F["e"]
    C --> G["e"]
```
</details>

(c) 三维模糊控制器  
图 4-5 单变量模糊控制器
