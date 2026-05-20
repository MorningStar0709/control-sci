COAST GUARD
902
902
0' 10' 20' 30' 40' 50'
</details>

图 5.60 习题 5.39 的美国海岸警卫艇 Tampa(902)

![](image/a954703287eab3fd3997609f182b22985be30831159ddf3e7332b2adab755873.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["θr"] --> B["Σ"]
    B --> C["K/(s+10)"]
    C --> D["Σ"]
    D --> E["飞机动态"]
    E --> F["1/s"]
    F --> G["θ"]
    H["姿态传感器"] --> I["1"]
    I --> B
    J["速率陀螺仪"] --> K["K_T"]
    K --> D
    L["Mp"] --> D
    M["Me"] --> D
    N["K_Tθ̇"] --> K
    O["-"] --> B
```
</details>

图 5.61 Golden Nugget 航空公司的自动驾驶仪

(b) 对于速度输出(测速计)反馈，令

$$H (s) = 1 + K _ {\mathrm{T}} s \text {和} D _ {\mathrm{c}} (s) = K$$

选择 $K_{T}$ 和 K 使主导根的位置与(a)问中相同。计算 $K_{v}$ 。若可以，请给出采用输出微分反馈时， $K_{v}$ 值减小的物理解释。

(c) 对于滞后网络，令

$$H (s) = 1 \text {和} D _ {\mathrm{c}} (s) = K \frac {s + 1}{s + p}$$

应用比例控制，在 $\zeta=0.4$ 时，能否有 $K_{v}=12$ ？选择 K 和 p，使主导根与比例控制的情况相同，不过对应的 $K_{v}=100$ 而不是 $K_{v}=12$ 。

![](image/bbe79835be5d0fadac8a70c045a88a62286326ac8f3d90fe342a97141c904e38.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R -->|+| Sum
    Sum --> Dc["补偿器 Dc(s)"]
    Dc --> u["u"]
    u --> Int["1/(s² + 51s + 550)"]
    Int --> Int2["1/s"]
    Int2 --> Y
    Y --> Hs["H(s)"]
    Hs -->|反馈| Sum
    Sum -->|-| Sum
```
</details>

图 5.62 习题 5.41 的控制系统
