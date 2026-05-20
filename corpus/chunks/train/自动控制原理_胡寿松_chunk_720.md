显然，本例设计的内模控制系统是渐近稳定的。对任意初始跟踪误差 $e(0)$ ，反馈控制信号都可以保证在 $t \to \infty$ 时， $e(t) \to 0$ 。在 MATLAB 的 Simulink 环境下，根据结构图 9-30 搭建内模控制系统模型，运行后可得图 9-31，其直观地表明了系统在单位阶跃参考输入时，跟踪误差的渐近收敛性。

考虑参考输入为斜坡信号的内模设计问题。设单位斜坡参考输入信号为 $r(t) = t$ ，并由下列系统生成：

$$
\begin{array}{l} \dot {\boldsymbol {x}} _ {r} = \boldsymbol {A} _ {r} \boldsymbol {x} _ {r} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right] \boldsymbol {x} _ {r} \\ r = \boldsymbol {d} _ {r} \boldsymbol {x} _ {r} = [ 1 \quad 0 ] \boldsymbol {x} _ {r} \\ \end{array}
$$

![](image/28f2a6e5f7c7f15a14069fbbffdcd764deba6a4c0e2bec34331a21d369ae1032.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    r --> |e| A["Circle"]
    A --> B["5"]
    B --> C["1/s"]
    C --> D["+"]
    D --> E["u"]
    E --> F["2"]
    F --> G["+"]
    G --> H["+"]
    H --> I["1/s"]
    I --> J["x2"]
    J --> K["+"]
    K --> L["1/s"]
    L --> M["x1=y"]
    M --> N["Output"]
    N --> O["5"]
    O --> P["+"]
    P --> Q["+"]
    Q --> R["2"]
    R --> S["+"]
    S --> T["+"]
    T --> U["2.5"]
    U --> V["+"]
    V --> W["+"]
    W --> X["+"]
    X --> Y["+"]
    Y --> Z["+"]
    Z --> AA["+"]
    AA --> AB["+"]
    AB --> AC["+"]
    AC --> AD["+"]
    AD --> AE["+"]
    AE --> AF["+"]
    AF --> AG["+"]
    AG --> AH["+"]
    AH --> AI["+"]
    AI --> AJ["+"]
    AJ --> AK["+"]
    AK --> AL["+"]
    AL --> AM["+"]
    AM --> AN["+"]
    AN --> AO["+"]
    AO --> AP["+"]
    AP --> AQ["+"]
    AQ --> AR["+"]
    AR --> AS["+"]
    AS --> AT["+"]
    AT --> AU["+"]
    AU --> AV["+"]
    AV --> AW["+"]
    AW --> AX["+"]
    AX --> AY["+"]
```
</details>

图 9-30 单位阶跃输入内模控制系统  
![](image/afd32ba622b37033c787e54e3237180164544ecb766ffc11e537c3c3e8a28bdd.jpg)

<details>
<summary>line</summary>

| Time/sec | 跟踪误差e(t) |
| --- | --- |
| 0 | 1.0 |
| 2 | -0.2 |
| 4 | -0.1 |
| 6 | 0.05 |
| 8 | 0.0 |
| 10 | 0.0 |
| 12 | 0.0 |
| 14 | 0.0 |
| 16 | 0.0 |
| 18 | 0.0 |
| 20 | 0.0 |
</details>

图 9-31 单位阶跃输入下内模控制系统的跟踪误差响应(MATLAB)

且有 $\ddot{r}(t)=0$ ，则对于单输入-单输出系统(9-268)，定义跟踪误差 e=r-y，有

$$\ddot {e} (t) = - \ddot {y} (t) = - c \ddot {x} (t)$$

令中间变量

$$z = \ddot {x}, w = \ddot {u}$$

有

$$z = \ddot {x} = A \dot {x} + b \dot {u}\dot {z} = A \ddot {x} + b \ddot {u} = A z + b w\ddot {e} = - \ddot {y} = - c \ddot {x} = - c z$$

构造增广系统

$$
\left[ \begin{array}{l} \dot {e} \\ \ddot {e} \\ \dot {z} \end{array} \right] = \left[ \begin{array}{l l l} 0 & 1 & 0 \\ 0 & 0 & - c \\ 0 & 0 & A \end{array} \right] \left[ \begin{array}{l} e \\ \dot {e} \\ z \end{array} \right] + \left[ \begin{array}{l} 0 \\ 0 \\ b \end{array} \right] w \tag {9-277}
$$

若系统(9-277)可控,即
