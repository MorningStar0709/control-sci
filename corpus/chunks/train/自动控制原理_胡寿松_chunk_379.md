# 6-8 设单位反馈系统的开环传递函数

$$G _ {0} (s) = \frac {K}{s (0 . 1 s + 1) (0 . 0 1 s + 1)}$$

试设计串联校正装置,使系统特性满足下列指标:

(1) 静态速度误差系数 $K_{v} \geqslant 250 s^{-1}$ ;  
(2) 截止频率 $\omega_{c} \geqslant 30 rad/s$ ;   
(3) 相角裕度 $\gamma(\omega_{c})\geqslant45^{\circ}$

6-9 设复合校正控制系统如图 6-49 所示。若要求闭环回路过阻尼，且系统在斜坡输入作用下的稳态误差为零，试确定 K 值及前馈补偿装置 $G_{r}(s)$ 。

6-10 设复合校正控制系统如图 6-50 所示, 其中 $N(s)$ 为可量测扰动, $K_{1}$ 、 $K_{2}$ 、T 均为正常数。若要求系统输出 $C(s)$ 完全不受 $N(s)$ 的影响, 且跟踪阶跃指令的误差为零, 试确定前馈补偿装置 $G_{c1}(s)$ 和串联校正装置 $G_{c2}(s)$ 。

![](image/c9762d1ef58dcba4a498dac1eebe94f6fb3d0a16abf414d0a39d6212d8f315dc.jpg)

<details>
<summary>line</summary>

| ω | L(ω) |
| --- | --- |
| 0.1 | 0.1 |
| 1.0 | -20dB/dec |
| 10 | 0dB/dec |
| 100 | 0dB/dec |
</details>

![](image/c3c636abbe21ea6368aab8783fd06537a0a50bb440e60feb2ba75a38bbadc0d8.jpg)

<details>
<summary>line</summary>

| ω | L(ω) |
| --- | --- |
| 10 | 0 |
| 100 | 0dB/dec |
</details>

![](image/c029663e5e45ba1743888fdb45c065553cd8da24b8f23f0bb010ba1b6e4b6e23.jpg)

<details>
<summary>line</summary>

| ω | L(ω) |
| --- | --- |
| 0.1 | 0.0 |
| 1.0 | -20dB/dec |
| 2.0 | -20dB/dec |
| 10 | 0.0 |
| 40 | 0.0 |
| 100 | 0.0 |
</details>

图 6-48 推荐的校正网络特性  
![](image/02e3275a25070238715fe3f28af39d5c3b84b7c913e68fb06011a2d90f33ec4b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> G_r["G_r(s)"]
    G_r --> E["s"]
    E["s"] --> +[+]
    + --> K["K/(0.1s+1)"]
    K --> 10["10/(s(0.5s+1))"]
    10 --> C["s"]
    C["s"] --> -["-"]
    - --> E["s"]
```
</details>

图 6-49 复合控制系统

![](image/4c32e5dd9430fe9c989aad23f6bc25b5ee14ca4ca089b43d254c67165b26ab92.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> A["Sum"]
    A --> B["Gc2(s)"]
    B --> C["Sum"]
    C --> D["K1/s"]
    D --> E["Sum"]
    E --> F["K2/(Ts+1)"]
    F --> G["C(s)"]
    G --> H["N(s)"]
    H --> I["Gc1(s)"]
    I --> J["-"]
    J --> C
    C --> K["-"]
    K --> L["-"]
    L --> A
```
</details>

图 6-50 复合控制系统

6-11 设复合控制系统如图 6-51 所示。图中 $G_{n}(s)$ 为前馈补偿装置的传递函数， $G_{c}(s)=K_{t}s$ 为测速发电机的传递函数， $G_{1}(s)$ 和 $G_{2}(s)$ 为前向通路环节的传递函数， $N(s)$ 为可量测扰动。如果

$$G _ {1} (s) = K _ {1}, \quad G _ {2} (s) = \frac {1}{s ^ {2}}$$

![](image/2af1d097f136fe23ab655cd4d7e0d89ffb784a60095edbb10c353258dac0d7fd.jpg)

<details>
<summary>flowchart</summary>
