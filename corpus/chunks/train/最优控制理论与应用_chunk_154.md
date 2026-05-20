```mermaid
graph TD
    A["W(t)"] --> B["G(t)"]
    B --> C["+"]
    C --> D["1/s"]
    D --> E["+"]
    E --> F["H(t)"]
    F --> G["+"]
    G --> H["Z(t)"]
    H --> I["+"]
    I --> J["K(t)"]
    J --> K["+"]
    K --> L["1/s"]
    L --> M["+"]
    M --> N["H(t)"]
    N --> O["+"]
    O --> P["X̂(t₀)"]
    P --> Q["+"]
    Q --> R["A(t)"]
    R --> S["-Lₖ"]
    S --> T["U(t)"]
    T --> C
    U["X(t₀)"] --> V["V(t)"]
    V --> W["+"]
    W --> X["H(t)"]
    X --> Y["+"]
    Y --> Z["X̂(t)"]
    Z --> AA["+"]
    AA --> AB["+"]
    AB --> AC["H(t)"]
    AC --> AD["+"]
    AD --> AE["X̂(t₀)"]
    AE --> AF["+"]
    AF --> AG["A(t)"]
    AG --> AH["-Lₖ"]
    AH --> AI["U(t)"]
    AI --> AJ["X(t)"]
    AJ --> AK["+"]
    AK --> AL["H(t)"]
    AL --> AM["X̂(t₀)"]
    AM --> AN["+"]
    AN --> AO["X̂(t)"]
    AO --> AP["A(t)"]
    AP --> AQ["-Lₖ"]
    AQ --> AR["U(t)"]
    AR --> AS["X(t)"]
```
</details>

图8-2 连续随机线性系统最优控制的方块图

例 8-1 图 8-3 是汽车自动控制系统的示意图。汽车沿着道路上设置的制导电缆自动行驶，汽车偏移电缆的横向位移由传感器测出。图 8-4 是自动控制系统的原理方块图。图中 W 为作用在汽车上的干扰力（例如路面不平等引起），U 为方向舵控制力，V 为传感器测量噪声，X 为汽车侧向位移。

![](image/e4629c0cc7b024dd0ec3fdd37a0460347e9327870677d371e7d984c502f233e8.jpg)

<details>
<summary>text_image</summary>

传感器
线圈
传感器
线圈
制导电缆
</details>

图8-3 汽车制导传感器原理图  
![](image/e83ba44678785d4dafe68b80051c35b5fa634e8e87db9ffacecc4aee615fc9b6.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["航线基准"] --> B["+"]
    B --> C["控制器"]
    C --> D["+"]
    D --> E["汽车"]
    E --> F["X"]
    F --> G["传感器"]
    G --> H["+"]
    H --> I["V"]
    I --> J["-"]
    J --> B
    K["W"] --> D
```
</details>

图8-4 汽车制导方块图
