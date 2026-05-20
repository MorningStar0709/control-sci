# 4. 采样周期与开环增益对稳定性的影响

众所周知，连续系统的稳定性取决于系统的开环增益 K、系统的零极点分布和传输延迟等因素。但是，影响离散系统稳定性的因素，除与连续系统相同的上述因素外，还有采样周期 T 的数值。先看一个具体的例子。

![](image/005724b0679e6cf8935a83d2b2277ce28c6b7ac3427778679a34a518505f3533.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B((+))
    B --> C["T"]
    C --> D["1-e^(-Ts)/s"]
    D --> E["K/(s(s+1))"]
    E --> F["C(s)"]
    F --> G["Feedback"]
    G --> B
```
</details>

图 7-36 离散系统

例 7-26 设有零阶保持器的离散系统如图 7-36 所示, 试求:

1) 当采样周期 T 分别为 1s 和 0.5s 时, 系统的临界开环增益 $K_{c}$ ;

2) 当 $r(t) = 1(t), K = 1, T$ 分别为0.1s, 1s, 2s,

4s 时, 系统的输出响应 $c(kT)$ 。

解 不难求出,系统的开环脉冲传递函数

$$
\begin{array}{l} G (z) = \left(1 - z ^ {- 1}\right) \mathscr {Z} \left[ \frac {K}{s ^ {2} (s + 1)} \right] \\ = K \frac {\left(\mathrm{e} ^ {- T} + T - 1\right) z + \left(1 - \mathrm{e} ^ {- T} - T \mathrm{e} ^ {- T}\right)}{(z - 1) (z - \mathrm{e} ^ {- T})} \\ \end{array}
$$

相应的闭环特征方程为

$$D (z) = 1 + G (z) = 0$$

当 $T = 1\mathrm{s}$ 时，有

$$D (z) = z ^ {2} + (0. 3 6 8 K - 1. 3 6 8) z + (0. 2 6 4 K + 0. 3 6 8) = 0$$

令 $z = (w + 1) / (w - 1)$ ，得 $w$ 域特征方程

$$D (w) = 0. 6 3 2 K w ^ {2} + (1. 2 6 4 - 0. 5 2 8 K) w + (2. 7 3 6 - 0. 1 0 4 K) = 0$$

根据劳斯判据，得 $K_{c}=2.4$ 。

当 T=0.5s 时，w 域特征方程为

$$D (w) = 0. 1 9 7 K w ^ {2} + (0. 7 8 6 - 0. 1 8 K) w + (3. 2 1 4 - 0. 0 1 7 K) = 0$$

根据劳斯判据，得 $K_{c}=4.37$ 。

由于闭环系统脉冲传递函数

$$
\begin{array}{l} \Phi (z) = \frac {C (z)}{R (z)} = \frac {G (z)}{1 + G (z)} \\ = \frac {K \left[ \left(\mathrm{e} ^ {- T} + T - 1\right) z + \left(1 - \mathrm{e} ^ {- T} - T \mathrm{e} ^ {- T}\right) \right]}{z ^ {2} + \left[ K \left(\mathrm{e} ^ {- T} + T - 1\right) - \left(1 + \mathrm{e} ^ {- T}\right) \right] z + \left[ K \left(1 - \mathrm{e} ^ {- T} - T \mathrm{e} ^ {- T}\right) + \mathrm{e} ^ {- T} \right]} \\ \end{array}
$$

且有 $R(z) = z / (z - 1)$ ，因此不难求得 $C(z)$ 表达式。

令 K=1, T 分别为 0.1s, 1s, 2s, 4s，可由 $C(z)$ 的反变换求出 $c(kT)$ ，分别画于图 7-37 中。

![](image/74c841c0fe445c17cccdae02b39fb670f886e1386bdbd0f701bef0b422175d96.jpg)

<details>
<summary>line</summary>

| Time/sec | c(kT) |
| --- | --- |
| 0 | 0 |
| 5 | 1 |
| 10 | 1 |
| 15 | 1 |
</details>

![](image/2d6a985effde8c0dd03620e5ed98818cd5c2a3cdd5b0822b2cc6d604e92e247e.jpg)

<details>
<summary>line</summary>

| Time/sec | c(kT) |
| --- | --- |
| 0 | 0 |
| 1 | 0.5 |
| 2 | 1.0 |
| 3 | 1.5 |
| 4 | 1.0 |
| 5 | 0.5 |
| 6 | 1.0 |
| 7 | 1.2 |
| 8 | 1.0 |
| 9 | 1.0 |
| 10 | 1.0 |
| 11 | 1.0 |
| 12 | 1.0 |
| 13 | 1.0 |
| 14 | 1.0 |
| 15 | 1.0 |
| 16 | 1.0 |
| 17 | 1.0 |
| 18 | 1.0 |
| 19 | 1.0 |
| 20 | 1.0 |
| 21 | 1.0 |
| 22 | 1.0 |
| 23 | 1.0 |
| 24 | 1.0 |
| 25 | 1.0 |
</details>

![](image/5f946df88bcff5a76ca1486b38619118191e0b6e645f0afbf25dd0c67fe5fced.jpg)
