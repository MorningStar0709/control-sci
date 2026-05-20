(1) 分别求出电位器传递系数 $K_{0}$ ，第一级和第二级放大器的比例系数 $K_{1}$ 和 $K_{2}$ ;  
(2) 画出系统结构图；  
(3) 简化结构图, 求系统传递函数 $\Theta_{o}(s)/\Theta_{i}(s)$ 。

![](image/221fe7b013d5c81d421ddff55b293eb7801c1318b46060529449882bb61495f5.jpg)

<details>
<summary>text_image</summary>

K0
θi
+15V
-15V 10kΩ
30kΩ
10kΩ
20kΩ
-K1
-K2
功放器
K3
SM
TG
+
-
+
-
K0
+15V
-15V
θo
</details>

图 2-54 位置随动系统原理图

2-16 设直流电动机双闭环调速系统的原理线路如图 2-55 所示, 要求:

(1) 分别求速度调节器和电流调节器的传递函数；  
(2) 画出系统结构图(设可控硅电路传递函数为 $K_{3} / (T_{3}s + 1)$ ; 电流互感器和测速发电机的传递系数分别为 $K_{4}$ 和 $K_{5}$ ; 直流电动机的结构图用题 2-14 的结果);  
(3) 简化结构图, 求系统传递函数 $\Omega(s)/U_{i}(s)$ 。

![](image/3a5857201a1cf0734e79517ec30a066b56823b65d4be5b480de9e109f3a0ae56.jpg)

<details>
<summary>text_image</summary>

电流
互感器
R
C1
R1
R2
C2
晶闸管
电路
R
-U1
R
-R
-K
- K
电流
调节器
Ua
扼流圈ω
SM
+
-
负
T G
</details>

图 2-55 直流电动机调速系统原理图

2-17 已知控制系统结构图如图 2-56 所示,试通过结构图等效变换求系统传递函数 $C(s)/R(s)$ 。  
2-18 试简化图 2-57 中的系统结构图, 并求传递函数 $C(s)/R(s)$ 和 $C(s)/N(s)$ 。  
2-19 试绘制图 2-56 中各系统结构图对应的信号流图, 并用梅森增益公式求各系统的传递函数 $C(s)/R(s)$ 。  
2-20 画出图 2-57 中各系统结构图对应的信号流图, 并用梅森增益公式求传递函数 $C(s)/R(s)$ 和 $C(s)/N(s)$ 。  
2-21 试绘制图 2-58 中系统结构图对应的信号流图, 并用梅森增益公式求传递函数 $C(s)/R(s)$ 和 $E(s)/R(s)$ 。

![](image/0a17449cd19e488377a14fb6f1277a5fed2b0a177b89f51e210aa0cfb2a22dd2.jpg)  
图 2-56 题 2-17 系统结构图

![](image/34517d97b9cc5860d0b8412797306a94f8c8c1e0eb986e0cc030ceaf1821033c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["R(s)"] --> A["+"]
    A --> B["+"]
    B --> C["G₁(s)"]
    C --> D["+"]
    D --> E["G₂(s)"]
    E --> F["+"]
    F --> G["N(s)"]
    G --> H["-"]
    H --> I["C'(s)"]
    I --> J["H₁(s)"]
    J --> K["-"]
    K --> A
```
</details>

(a)

![](image/ca229766c7e419dfd539934d6de483df57eb284fd9918351168e6708f8f5acde.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["R(s)"] --> G1["G₁(s)"]
    R --> G2["G₂(s)"]
    R --> G3["G₃(s)"]
    G1 --> G2
    G2 --> G3
    G3 --> G4["G₄(s)"]
    N["N(s)"] --> G2
    N --> G4
    G4 --> C["C(s)"]
    G1 --> G2
    G2 --> G4
    G3 --> G4
```
</details>

(b)   
图 2-57 题 2-18 系统结构图

![](image/67b6d55ddb5322dca4aefd8f99ae5575a3c8d1a6becf0a5d37bc7579cf713266.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    R["s"] --> A["Summing Junction"]
    A --> B["G1(s)"]
    B --> C["G2(s)"]
    C --> D["Summing Junction"]
    D --> E["G3(s)"]
    E --> F["C(s)"]
    F --> G["H2(s)"]
    G --> H["Summing Junction"]
    H --> I["H1(s)"]
    I --> J["Summing Junction"]
    J --> K["E(s)"]
    K --> A
    G --> L["G4(s)"]
    L --> D
```
</details>

(a)
