$$G (s) = \frac {K ^ {*}}{s ^ {2} (s + 2) (s + 5)}, \quad H (s) = 1$$

要求：

(1) 概略绘出系统根轨迹图, 并判断闭环系统的稳定性;

(2) 如果改变反馈通路传递函数, 使 $H(s) = 1 + 2s$ , 试判断 $H(s)$ 改变后的系统稳定性, 研究由于 $H(s)$ 改变所产生的效应。

4-11 试绘出下列多项式方程的根轨迹：

(1) $s^{3}+2s^{2}+3s+Ks+2K=0;$   
(2) $s^3 + 3s^2 + (K + 2)s + 10K = 0$ 。

4-12 设系统开环传递函数如下,试画出 b 从零变到无穷时的根轨迹图:

(1) $G(s) = \frac{20}{(s + 4)(s + b)};$   
(2) $G(s) = \frac{30(s + b)}{s(s + 10)}$

4-13 设控制系统的结构图如图 4-39 所示,试概略绘制其根轨迹图。

![](image/ba865ca7f0e1457aabc51df051b54130c1fd922ef2ea59d43fffe7edac8dd493.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B((+))
    B --> C["Block: (K*(s+1)²)/(s+2)²"]
    C --> D["C(s)"]
    D --> E["Feedback"]
    E --> B
```
</details>

图 4-39 控制系统

4-14 设单位反馈控制系统的开环传递函数为

$$G (s) = \frac {K ^ {*} (1 - s)}{s (s + 2)}$$

试绘制其根轨迹图，并求出使系统产生重实根和纯虚根的 $K^{*}$ 值。

4-15 设控制系统如图 4-40 所示, 试概略绘出 $K_{t} = 0, 0 < K_{t} < 1, K_{t} > 1$ 时的根轨迹。若取 $K_{t} = 0.5$ , 试求出 $K = 10$ 时的闭环零、极点, 并估算系统的动态性能。

![](image/12e448a21ba62c327cfe88ec290d1d65751d0244bcc9a48a9ff00f61b0efd952.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B((+))
    B --> C["K/(s(s+1))"]
    C --> D["C(s)"]
    D --> E["1+Kt s"]
    E --> B
    B --> F["-"]
```
</details>

图 4-40 控制系统

4-16 设控制系统开环传递函数为

$$G (s) = \frac {K ^ {*} (s + 1)}{s ^ {2} (s + 2) (s + 4)}$$

试分别画出正反馈系统和负反馈系统的根轨迹图，并指出它们的稳定情况有何不同？

4-17 设控制系统如图 4-41 所示, 其中 $G_{c}(s)$ 为改善系统性能而加入的校正装置。若 $G_{c}(s)$ 可从 $K_{t}s, K_{a}s^{2}$ 和 $K_{a}s^{2}/(s+20)$ 三种传递函数中任选一种, 你选择哪一种? 为什么?

![](image/a889d5ea3a65117453a2ec00934cc63b39cdbfd513dfc1bf12c5ed65d93b0f15.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> A["○"]
    A --> B["100/(s+20)"]
    B --> C["○"]
    C --> D["10/(s(s+10))"]
    D --> E["C(s)"]
    E --> F["Gc(s)"]
    F --> A
    A -->|-| A
    C -->|-| C
```
</details>

图 4-41 控制系统

4-18 设系统如图 4-42 所示。试作闭环系统根轨迹，并分析 K 值变化对系统在阶跃扰动作用下响应 $c_{n}(t)$ 的影响。

![](image/633402b31de9f902ee706f330ff4ac8312260f3f33739621f309dd5b76d7c2e7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B((+))
    B --> C["s²+2s+2"]
    C --> D["+"]
    D --> E["K/s³"]
    E --> F["C(s)"]
    F --> G["-"]
    G --> B
    H["N(s)"] --> D
```
</details>

图4-42 控制系统
