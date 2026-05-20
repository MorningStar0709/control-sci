![](image/ac629a4fb1abedc1ce8237cd09c0234451fb6f888341d716d80c4c93625f5f9d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["控制器"]
    C --> D["Gc(s)"]
    D --> E["+"]
    E --> F["电机和天线"]
    F --> G["10/(s(s+5)(s+10))"]
    G --> H["C(s)"]
    H --> I["-"]
    I --> B
    J["N(s)"] --> E
```
</details>

(b) 结构图  
图 6-60 天线指向控制系统

框图如图 6-61(b) 所示, 其中

$$G _ {0} (s) = \frac {1}{s \left(s ^ {2} + 4 s + 5\right)}$$

而 $G_{c}(s)$ 为具有两个相同实零点的 PID 控制器。要求：

(1) 选择 PID 控制器的零点和增益, 使闭环系统有两对相等的特征根;  
(2) 考察(1)中得到的闭环系统,给出不考虑前置滤波器 $G_{p}(s)$ 与配置适当 $G_{p}(s)$ 时,系统的单位阶跃响应;  
(3) 当 $R(s)=0, N(s)=1/s$ 时，计算系统对单位阶跃扰动的响应。

![](image/7f83acc61872c12da29e1a29263a783c157e38c843378f536f3bbf702023fd23.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["热整平设备"] --> B["2号台"]
    B --> C["1号台"]
    C --> D["熔炉"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
```
</details>

(a)   
![](image/be48435a10069c5dda7f9ad6091cd2023117c03a753ac22664a15802812297d8.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s) 预期厚度"] --> B["Gp(s)"]
    B --> C["+"]
    C --> D["Gc(s)"]
    D --> E["+"]
    E --> F["G0(s)"]
    F --> G["C(s) 厚度"]
    G --> H["-"]
    H --> C
    I["扰动 N(s)"] --> E
```
</details>

(b)   
图 6-61 热轧机控制系统
