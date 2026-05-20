<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R -->|+| Sum
    Sum --> K1["-K"]
    K1 --> K2["-K"]
    K2 --> K3["-K"]
    K3 --> Y
    Y -->|feedback| Sum
    Sum -->|+| Sum
    Sum --> β3["β₃"]
```
</details>

c)

图 4.24 习题 4.2 中三种放大器拓扑  
![](image/68181bcb834e16b4d6252b1e314323dbc63c45d222746f05e0e7e6889fdff382.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R -->|+| Sum1["Σ"]
    Sum1 --> K1["K"]
    K1 -->|+| Sum2["Σ"]
    Sum2 --> K2["K"]
    K2 --> F1["F₁"]
    F1 -->|−| Sum1
    Sum1 --> H1["H₁"]
    H1 -->|−| Sum2
    Sum2 --> H2["H₁"]
    H2 -->|−| Sum1
```
</details>

a)   
![](image/be44e8f8b5548811470b43377a31e05e7a13e763e72c79b3e3fc23ad41ea90ee.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R -->|+| Sum
    Sum --> K1["K"]
    K1 --> K2["K"]
    K2 --> F2["F₂"]
    F2 --> H2["H₂"]
    H2 -->|-| Sum
```
</details>

b)   
图4.25 习题4.3框图

4.4 单位反馈控制系统的开环传递函数为

$$G (s) = \frac {A}{s (s + a)}$$

(a) 计算闭环传递函数对参数 A 变化的灵敏度。  
(b) 计算闭环传递函数对参数 a 变化的灵敏度。  
(c) 若反馈单位增益变为 $\beta \neq 1$ ，计算闭环系统传递函数对 $\beta$ 的灵敏度。

4.5 计算图 4.5 所示的反馈系统的系统误差方程。

4.2节习题  
4.6 考虑如图 4.26a 所示的具有速度(转速计)反馈的直流电动机控制系统。

(a) 找出使图 4.26b 和图 4.26a 所示系统有相同传递函数的 $K'$ 和 $k'$ 的值。  
(b) 确定跟踪输入为 $\theta_{r}$ 时的系统类型，并计算用参数 $K'$ 和 $k'$ 表示的系统误差常数 $K_{v}$ 。  
(c) 转速计反馈引入正数 $k_{t}$ 会使 $K_{v}$ 增大还是减小？

![](image/adad19995af73c44fb28392dbf4f2d7b612e564a1760915143f63cf57ba5cd12.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["θr"] --> B["Σ"]
    B --> C["Kp"]
    C --> D["Σ"]
    D --> E["K"]
    E --> F["(Km)/(s(1+τm)s)"]
    F --> G["1/k"]
    G --> H["θ"]
    H --> I["kt s"]
    I --> J["-"]
    J --> B
```
</details>

a)

![](image/492da15e4c17261136041f400024c5e55f7f49fd62d31cd7970812224d1027e4.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["θr"] --> B["Σ"]
    B --> C["K'/s(1+τm s)"]
    C --> D["θ"]
    D --> E["1+k't s"]
    E --> B
    B --> F["-"]
    F --> A
```
</details>

b)   
图 4.26 习题 4.6 控制系统

4.7 图 4.27 所示的控制系统框图。

(a) 若 r 是阶跃函数并且系统闭环稳定，那么稳态跟踪误差是什么？  
(b) 求系统类型。  
(c) 若 $K_{2}=2$ ，并且调整 $K_{1}$ 使系统在阶跃输入信号作用下系统超调量为 17%，求系统在斜率为 5.0 的斜坡输入作用下的稳态误差。

![](image/493cdac9f6e6aea5d88cd6f40cd33af10a9470175a118ba709815fadf31e950b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["R"] --> B["0.5"]
    B --> C["Σ"]
    C --> D["K₁ (s+3)/(s+10)"]
    D --> E["Σ"]
    E --> F["1/(s(s+10))"]
    F --> G["Y"]
    G --> H["K₂s"]
    H --> I["0.5"]
    I --> J["-"]
    J --> C
```
</details>

图 4.27 习题 4.7 闭环系统

4.8 一个标准反馈控制系统框图如图 4.5 所示，其中，
