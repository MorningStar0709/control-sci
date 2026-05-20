# 11.2.2 一个典型伺服系统描述

以飞行模拟转台伺服系统为例，它是三轴伺服系统，正常情况下可简化为线性二阶环节的系统，在低速情况下具有较强的摩擦现象，此时控制对象就变为非线性，很难用传统控制方法达到高精度控制。任意框的伺服结构如图11-4所示，该系统采用直流电机，忽略电枢电感，电流环和速度环为开环，其中 $K_{u}$ 为PWM功率放大器放大系数，R为电枢电阻， $K_{m}$ 为电机力矩系数， $C_{e}$ 为电压反馈系数，J为该框的转动惯量， $\dot{\theta}(t)$ 为转速， $r(t)$ 为指令信号， $u(t)$ 为控制输入，即驱动力 $F(t)$ 。

![](image/9f34ac7d29504912a981e008848487b09f36a186e61bf6eb496bb38b692faafd.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["y_d(t)"] --> B["PID"]
    B --> C["u(t)"]
    C --> D["K"]
    D --> E["+"]
    E --> F["1/R"]
    F --> G["K_m"]
    G --> H["+"]
    H --> I["F(t)"]
    I --> J["1/Js"]
    J --> K["θ̇(t)"]
    K --> L["1/s"]
    L --> M["θ(t)"]
    M --> N["C_e"]
    N --> O["-"]
    O --> P["+"]
    P --> Q["1/R"]
    Q --> R["+"]
    R --> S["F(t)"]
    S --> T["1/S"]
    T --> U["θ̇(t)"]
    U --> V["C_e"]
    V --> W["-"]
    W --> X["+"]
    X --> Y["1/R"]
    Y --> Z["+"]
    Z --> AA["F(t)"]
    AA --> AB["1/S"]
    AB --> AC["θ̇(t)"]
    AC --> AD["C_e"]
    AD --> AE["-"]
    AE --> AF["+"]
    AF --> AG["1/R"]
    AG --> AH["+"]
    AH --> AI["F(t)"]
    AI --> AJ["1/S"]
    AJ --> AK["θ̇(t)"]
    AK --> AL["C_e"]
    AL --> AM["-"]
    AM --> AN["+"]
    AN --> AO["1/R"]
    AO --> AP["+"]
    AP --> AQ["F(t)"]
    AQ --> AR["1/S"]
    AR --> AS["θ̇(t)"]
    AS --> AT["C_e"]
    AT --> AU["-"]
    AU --> AV["+"]
    AV --> AW["1/R"]
    AW --> AX["+"]
    AX --> AY["F(t)"]
    AY --> AZ["1/S"]
    AZ --> BA["θ̇(t)"]
    BA --> BB["C_e"]
    BB --> BC["-"]
    BC --> BD["+"]
    BD --> BE["1/R"]
    BE --> BF["+"]
    BF --> BG["F(t)"]
    BG --> BH["1/S"]
    BH --> BI["θ̇(t)"]
    BI --> BJ["C_e"]
    BJ --> BK["-"]
    BK --> BL["+"]
    BL --> BM["1/R"]
    BM --> BN["+"]
    BN --> BO["F(t)"]
    BO --> BP["1/S"]
    BP --> BQ["θ̇(t)"]
```
</details>

图 11-4 转台伺服系统结构

伺服系统的动力学方程为

$$\ddot {\theta} = - \frac {K _ {\mathrm{m}} C _ {\mathrm{e}}}{J R} \dot {\theta} + K _ {\mathrm{u}} \frac {K _ {\mathrm{m}}}{J R} u (t) - \frac {1}{J} F _ {\mathrm{f}} (t) \tag {11.7}$$

转换为状态方程可描述如下:

$$
\left[ \begin{array}{l} \dot {x} _ {1} (t) \\ \dot {x} _ {2} (t) \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ 0 & - \frac {K _ {\mathrm{m}} C _ {\mathrm{e}}}{J R} \end{array} \right] \left[ \begin{array}{l} x _ {1} (t) \\ x _ {2} (t) \end{array} \right] + \left[ \begin{array}{c c} 0 & \\ K _ {\mathrm{u}} & \frac {K _ {\mathrm{m}}}{J R} \end{array} \right] u (t) - \left[ \begin{array}{l} 0 \\ \frac {1}{J} \end{array} \right] F _ {\mathrm{f}} (t) \tag {11.8}
$$

式中， $x_{1}(t)=\theta(t)$ 为转角； $x_{2}(t)=\dot{\theta}(t)$ 为转速。

![](image/2572aa5414125a611edbd294588faeb79d08b7c184a1f90e410a28ef17d35467.jpg)
