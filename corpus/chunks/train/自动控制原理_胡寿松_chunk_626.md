$$
\mathbf {G} _ {d} (s) = \boldsymbol {\Phi} ^ {\prime - 1} (s) \boldsymbol {\Phi} (s) = \left[ \begin{array}{c c} \frac {1}{2 (s + 1)} & 0 \\ \frac {2 s + 1}{2 (s + 2)} & \frac {1}{s + 2} \end{array} \right] ^ {- 1} \left[ \begin{array}{c c} \frac {1}{s + 1} & 0 \\ 0 & \frac {1}{5 s + 1} \end{array} \right]

= \left[ \begin{array}{c c} 2 (s + 1) & 0 \\ - (2 s + 1) (s + 1) & s + 2 \end{array} \right] \left[ \begin{array}{c c} \frac {1}{s + 1} & 0 \\ 0 & \frac {1}{5 s + 1} \end{array} \right]

= \left[ \begin{array}{c c} 2 & 0 \\ - (2 s + 1) & \frac {s + 2}{5 s + 1} \end{array} \right] = \left[ \begin{array}{l l} G _ {d 1 1} (s) & G _ {d 1 2} (s) \\ G _ {d 2 1} (s) & G _ {d 2 2} (s) \end{array} \right]
$$

式中， $G_{dij}(s)$ 表示 $U_{j}(s)$ 至 $U_{i}^{\prime}(s)(i,j=1,2)$ 通道的串联补偿器传递函数。

用前馈补偿器实现解耦的系统结构图见图 9-19。

![](image/14c236f37ff6eefff514ba9171e7f7bfa1788247f14f591b4ec15b502bb9d456.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    u1["u₁"] -->|+| sum1((+))
    e1["e₁"] --> Gc11["G_c11(s)"]
    e1 --> Gc21["G_c21(s)"]
    e1 --> Gc12["G_c12(s)"]
    e1 --> Gc22["G_c22(s)"]
    Gc11 --> add1((+))
    Gc21 --> add1
    Gc12 --> add2((+))
    Gc22 --> add2
    add1 --> integrator["1/(2s+1)"]
    add2 --> integrator
    integrator --> y1["y₁"]
    y1 --> y2["y₂"]
    y2 -->|+| sum1
    y2 -->|-| e2["e₂"]
    e2 --> Gc22
    Gc22 --> add3((+))
    add3 --> integrator
```
</details>

图 9-18 用串联补偿器实现解耦的系统结构图

![](image/7d58970152075c09db4645e9261bfbbd8fd92bed140c7c8f63942edd6bcad4a5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["u₁"] --> B["Gd11"]
    B --> C["+"]
    C --> D["u₁'"]
    D --> E["+"]
    E --> F["e₁"]
    F --> G["1/(2s+1)"]
    G --> H["y₁"]
    I["u₂"] --> J["Gd22"]
    J --> K["+"]
    K --> L["u₂'"]
    L --> M["e₂"]
    M --> N["1/(s+1)"]
    N --> O["+"]
    O --> P["y₂"]
    Q["Gd1"] --> R["Gd21"]
    R --> S["+"]
    S --> T["u₁'"]
    T --> U["-"]
    U --> V["e₁"]
    V --> W["1/(2s+1)"]
    W --> X["+"]
    X --> Y["y₂"]
    Z["Gd12"] --> AA["Gd22"]
    AA --> AB["+"]
    AB --> AC["u₂'"]
    AC --> AD["e₂"]
    AD --> AE["1/(s+1)"]
    AE --> AF["+"]
    AF --> AG["y₂"]
```
</details>

图 9-19 用前馈补偿器实现解耦的系统结构图
