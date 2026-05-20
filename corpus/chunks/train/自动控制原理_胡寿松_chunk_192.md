# 例 3-19 磁盘驱动读取系统(续)

磁盘驱动器必须保证磁头的精确位置，并减小参数变化和外部振动对磁头定位造成的影响。作用于磁盘驱动器的扰动包括物理振动、磁盘转轴轴承的磨损和摆动，以及元器件老化引起的参数变化等。设图3-46磁盘驱动系统在考虑扰动作用时的结构如图3-47所示，根据表2-3给定的参数，图3-47可表示为图3-48所示。试讨论放大器增益 $K_{a}$ 值的选取对系统在单位阶跃指令作用下的动态响应、稳态误差以及抑制扰动能力的影响。

![](image/d6dc0226e7a0c4c88d94dc29ceef031409021a75fb23b8badd12cf18ceae211d.jpg)

<details>
<summary>text_image</summary>

磁盘
读/写磁头
期望位置
传感器
控制器
电机输入
</details>

图 3-46 磁盘驱动控制系统示意图

![](image/d6a910684dcbabce23d44a624c4ede32fd3643d37afb5d7a34a1e34e2e59bad5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["误差"]
    C --> D["放大器 Kα"]
    D --> E["V(s)"]
    E --> F["线圈 (Km/R+Ls)"]
    F --> G["+"]
    G --> H["载荷 (1/(s(Js+f))"]
    H --> I["C(s)"]
    I --> J["实际位置"]
    J --> K["H(s)=1"]
    K --> L["传感器"]
    L --> M["-"]
    M --> B
    N["N(s)"] --> G
    O["扰动"] --> G
```
</details>

图 3-47 磁盘驱动器磁头控制系统

![](image/ea77017f074c5ff3ce880814ebb19dee88abe70e503de58546378274e40d82f4.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["E(s)"]
    C --> D["Ka"]
    D --> E["线圈 G1(s) = 5000/(s+1000)"]
    E --> F["+"]
    F --> G["N(s)"]
    G --> H["扰动"]
    H --> I["-"]
    I --> J["负载 G2(s) = 1/(s(s+20))"]
    J --> K["C(s)"]
    K --> L["-"]
    L --> M["反馈"]
    M --> B
```
</details>

图 3-48 磁头控制系统结构图

解 1) 当 $N(s) = 0, R(s) = 1 / s$ 时。误差信号

$$E (s) = \frac {1}{1 + K _ {a} G _ {1} (s) G _ {2} (s)} R (s)$$

于是 $\lim_{t\to \infty}e(t) = \lim_{s\to 0}\left[\frac{1}{1 + K_aG_1(s)G_2(s)}\right]\frac{1}{s} = 0$

上式表明系统在单位阶跃输入作用下的稳态跟踪误差为零。这一结论与 $K_{a}$ 取值无关。

当 $N(s)=0$ 时，闭环传递函数为

$$\Phi (s) = \frac {C (s)}{R (s)} = \frac {K _ {a} G _ {1} (s) G _ {2} (s)}{1 + K _ {a} G _ {1} (s) G _ {2} (s)}$$

利用 MATLAB 文本, 可得 $K_{a}=10$ 和 $K_{a}=80$ 时系统的单位阶跃响应, 如图 3-49 所示, 当 $K_{a}=80$ 时, 系统对输入指令的响应速度明显加快, 但响应出现了较大振荡。

![](image/e2289030553c0a5128915f3d045843bb5f7a408ccd462e39444957efb937dee4.jpg)

<details>
<summary>line</summary>

| Time/sec | Amplitude |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.7 |
| 1.0 | 0.9 |
| 1.5 | 1.0 |
| 2.0 | 1.0 |
| 2.5 | 1.0 |
| 3.0 | 1.0 |
| 3.5 | 1.0 |
| 4.0 | 1.0 |
</details>

(a) $K_{a} = 10$ 时的阶跃响应曲线

![](image/3fcad3d2cde8aed7ff279bb00388436737664e264a9e06e03af5a9e14f4524ba.jpg)

<details>
<summary>line</summary>

| Time/sec | Amplitude |
| --- | --- |
| 0.0 | 0.0 |
| 0.2 | 1.2 |
| 0.4 | 1.0 |
| 0.6 | 1.0 |
| 0.8 | 1.0 |
| 1.0 | 1.0 |
| 1.2 | 1.0 |
| 1.4 | 1.0 |
| 1.6 | 1.0 |
| 1.8 | 1.0 |
| 2.0 | 1.0 |
</details>

(b) $K_{a} = 80$ 时的阶跃响应曲线  
图 3-49 磁头控制系统时间响应(MATLAB)
