# 7-15 设离散系统如图 7-64 所示, 其中采样周期 T=0.2, K=10, $r(t)=1+t+t^{2}/2$ , 试用终值定理法计算系统的稳态误差 $e_{s}(\infty)$ 。

![](image/a0814567b16ed23501229ac918dd9dfd95282d7ae96822d65d1dac243f788837.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["r(t)"] --> B["Summing Junction"]
    B --> C["e(t)"]
    C --> D["e*(t)"]
    D --> E["1-e^(-sT)/s"]
    E --> F["K"]
    F --> G["1/(s²)"]
    G --> H["c(t)"]
    H --> I["0.5s"]
    I --> J["-"]
    J --> B
    C --> K["T"]
```
</details>

图 7-64 闭环离散系统

7-16 设离散系统如图 7-65 所示, 其中 $T = 0.1, K = 1, r(t) = t$ , 试求静态误差系数 $K_{p}, K_{v}$ , $K_{a}$ , 并求系统稳态误差 $e_{s}(\infty)$ 。  
7-17 已知离散系统如图 7-66 所示, 其中 ZOH 为零阶保持器, T=0.25。当 $r(t)=2+t$ 时, 欲使稳态误差小于 0.1, 试求 K 值。

![](image/49cf479fbf75cbbb51f541fe7e81a1a747d87d0ab690005471cf5b7edcc40429.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["r(t)"] --> B((+))
    B --> C["e(t)"]
    C --> D["T"]
    D --> E["e*(t)"]
    E --> F["1-e^(-sT)/s"]
    F --> G["K/(s(s+1))"]
    G --> H["c(t)"]
    H --> I["-"]
    I --> B
```
</details>

图 7-65 闭环离散系统

![](image/c00ef57a4bb6724abec68968c51a06cb775a30ff1be01304f38078d24e2726e2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["r(t)"] --> B((+))
    B --> C["ZOH"]
    C --> D["Ke^(-0.5s)/s"]
    D --> E["c(t)"]
    E --> F["Feedback"]
    F --> B
    G["-"] --> B
```
</details>

图 7-66 闭环离散系统

7-18 试分别求出图 7-64 和图 7-65 系统的单位阶跃响应 $c(nT)$ 。  
7-19 已知离散系统如图 7-67 所示, 其中采样周期 T=1, 连续部分传递函数

$$G _ {0} (s) = \frac {1}{s (s + 1)}$$

试求当 $r(t)=1(t)$ 时，系统无稳态误差、过渡过程在最少拍内结束的数字控制器 $D(z)$ 。

7-20 设离散系统如图 7-68 所示, 其中采样周期 T=1, 试求当 $r(t)=R_{0}1(t)+R_{1}t$ 时, 系统无稳态误差、过渡过程在最少拍内结束的 $D(z)$ 。

![](image/621c32b151d4ed62a1467f0c22e3f7d51e41319049a8247d44357228c67d65e1.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["r(t)"] --> B((+))
    B --> C["T"]
    C --> D["D(z)"]
    D --> E["T"]
    E --> F["G₀(s)"]
    F --> G["c(t)"]
    G --> H["Feedback"]
    H --> B
    I["E₁(z)"] --> C
    J["E₂(z)"] --> E
```
</details>

图 7-67 离散系统

![](image/324def9a984c02bf874870eeecfafc63bc53411f946c68c0e53a48deae0b3c6b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["r(t)"] --> B((+))
    B --> C["D(z)"]
    C --> D["ZOH"]
    D --> E["K/s"]
    E --> F["c(t)"]
    F --> G["Feedback"]
    G --> B
    H["E₁(z)"] --> C
    I["E₂(z)"] --> D
    J["T"] --> C
    K["T"] --> D
```
</details>

图 7-68 离散系统

7-21 试按无纹波最少拍系统设计方法,分别算出题 7-19 和题 7-20 的 $D(z)$ 。  
7-22 用来直播职业足球赛的新型可遥控摄像系统如图 7-69 所示。摄像机可在运动场上方上下移动。每个滑轮上的电机控制系统如图 7-70 所示，其中被控对象
