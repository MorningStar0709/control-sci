9-41 设内模控制系统如图 9-53 所示。试设计合适的内模控制器 $G_{c}(s)$ 和状态反馈增益向量 $k_{2}$ , 使系统闭环极点 $s_{1} = s_{2} = s_{3} = -2$ , 且对阶跃输入的稳态跟踪误差为零, 最后绘出系统的单位阶跃响应曲线。

![](image/60acf487da2cc69db8388c8d9bac580bcf409c50ad8a4cd30129b9f3b330745e.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> Kp["K_p"]
    Kp --> +
    + --> | - | Sum
    Sum --> K3["K_3"]
    K3 --> X3["X_3(s)"]
    X3 --> | - | Int["2/(s+4)"]
    Int --> X3
    X3 --> | + | Int["1/(s+2)"]
    Int --> X2["X_2(s)"]
    X2 --> | - | Int["1/(s+3)"]
    Int --> X1["X_1(s)=Y(s)"]
    X1 --> K1["K_1"]
    K1 --> K2["K_2"]
    K2 --> X2
    X2 --> | - | Sum
```
</details>

图 9-51 汽车悬架系统

![](image/0e2fbc7058045ec9f7d0c49f4b03d562f52758399f5e02552e0c3df0f0cfc239.jpg)

<details>
<summary>text_image</summary>

侧视图
正视图
游客
驾驶仓
支控
浮桥
电子控制式稳定器
</details>

(a)

![](image/168825db631dfce673022bfb1054dc896f994ad04fd0257956c3461ee15da19b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)=0"] --> B["+"]
    B --> C["60/(s+8)"]
    C --> D["X3(s)"]
    D --> E["+"]
    E --> F["2/(s+2)"]
    F --> G["X2(s)"]
    G --> H["1/s"]
    H --> I["X1(s)"]
    I --> J["Θ(s)"]
    J --> K["K2"]
    K --> L["K3"]
    L --> M["-"]
    M --> B
    N["N(s)"] --> E
    O["摇摆角"] --> I
```
</details>

(b)

图 9-52 游船摇摆控制系统  
![](image/09d918930b95fa1f4eabece07a3bf5962f5be935f2b1f8da35220d07a3ca92aa.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["R(s)"] -->|+| Sum((+))
    Sum --> E["E(s)"]
    E --> Gc["Gc(s)"]
    Gc -->|-| Sum
    U["U(s)"] --> 对象G0["对象G0(s)"]
    对象G0 --> 1["1/(s+1)(s+2)"]
    1 --> Y["Y(s)"]
    k2["k2"] -->|x| Sum
    Sum -->|-| Sum
```
</details>

图 9-53 内模控制系统
