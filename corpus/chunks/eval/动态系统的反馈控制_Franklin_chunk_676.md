```mermaid
graph TD
    A["重复序列"] --> B["工作区1 r"]
    A --> C["示波器2"]
    B --> D["+"]
    C --> E["+"]
    D --> F["k₁ K·u 矩阵增益1"]
    E --> G["+"]
    F --> H["积分器 1/s"]
    G --> I["+"]
    H --> J["饱和非线性"]
    I --> J
    J --> K["灯管倒置 In 1 Out 1 子系统2"]
    K --> L["电压功率 In 1 Out 1 子系统1"]
    L --> M["矩阵增益4"]
    M --> N["K·u"]
    N --> O["估计器 x'=Ax+Bu y=Cx+Du 状态空间1"]
    O --> P["矩阵增益5"]
    P --> Q["K·u"]
    Q --> R["灯管不确定性 K·u"]
    R --> S["矩阵增益3"]
    S --> T["非线性被控对象 Out 1 In 1 子系统"]
    T --> U["工作区2 y"]
    U --> V["工作区2"]
    V --> W["示波器4"]
    W --> X["抗积分器 K·u 矩阵增益2"]
    X --> Y["+"]
    Y --> Z["+"]
    Z --> AA["示波器3"]
    AA --> AB["工作区2 u"]
    AB --> AC["示波器1"]
```
</details>

a）非线性闭环

![](image/d4a49b286345388e2e6dbb485c0c959cb416460317eeee3abb3032a1c83dd052.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["输入1"] --> B["输入流量 K·u"]
    B --> C["增加流量 + -求和"]
    C --> D["M_inv"]
    D --> E["积分器 xo ω 301.35 1/s"]
    E --> F["输出 1"]
    G["矩阵增益4"] --> C
    H["矩阵增益5"] --> I["波尔兹曼函数 u^v"]
    I --> J["矩阵增益2"]
    J --> K["Mux 3"]
    K --> L["控制信号"]
    M["矩阵增益3"] --> N["多路解调器2"]
    N --> O["传导"]
    O --> P["常数 301.352135"]
    Q["辐射"] --> I
    R["频率计时器"] --> I
    S["频率计时器"] --> J
    T["频率计时器"] --> K
    U["频率计时器"] --> L
    V["频率计时器"] --> O
```
</details>

b）非线性装置   
图 10.71 非线性 RTP 闭环系统的仿真框图

![](image/824fd568344a1546ac88b26a956ecb916a8b1edd63163aac9ede704b511c77ee.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["输入1"] --> B["饱和非线性"]
    B --> C["+"]
    D["常数1"] --> C
    E["常数1 1.6"] --> C
    C --> F["数学函数 u^v"]
    F --> G["输出1"]
```
</details>

a）电压功率转换子系统

![](image/653aebfb9c4c0b2d142ef35c130999f85ab22e5ea257b4bb00519395e1e0a43a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["1 输入1"] --> B["数学函数 u^v"]
    C["常数1 0.625"] --> B
    D["常数 1"] --> E["+"]
    B --> E
    E --> F["1 输入1"]
```
</details>

b）灯管模型子系统

图 10.72 非线性 RTP 闭环系统的仿真框图  
![](image/9ff1c38994dc79a5869b3bc36c12119e50ab40bc5400ee6714f3081b7d5acf1a.jpg)

<details>
<summary>line</summary>

| 时间/s | 温度/K |
| --- | --- |
| 40 | 315 |
| 60 | 333 |
| 100 | 333 |
| 140 | 315 |
| 160 | 315 |
</details>

a）温度跟踪响应

![](image/7a99cef04e9af3aa19565d365d6493cc515d5287206359c74aed84ab411219a3.jpg)

<details>
<summary>line</summary>

| 时间/s | 灯管电压/V |
| --- | --- |
| 40 | 1.0 |
| 50 | 2.5 |
| 60 | 3.8 |
| 70 | 2.5 |
| 80 | 2.5 |
| 90 | 2.5 |
| 100 | 2.5 |
| 110 | 1.5 |
| 120 | 1.0 |
| 130 | 0.5 |
| 140 | 0.3 |
| 150 | 0.9 |
| 160 | 0.9 |
| 170 | 0.9 |
| 180 | 0.9 |
</details>

b）控制效果  
图 10.73 鲁棒伺服机构控制器的非线性闭环响应
