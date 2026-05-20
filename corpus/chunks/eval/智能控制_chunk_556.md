# 11.4.2 仿真实例

针对两关节机械手,介绍机器人 PD 型反馈迭代学习控制的仿真设计方法,式(11.9)各项表示为

$$
\begin{array}{l} \pmb {D} = [ d _ {i j} ] _ {2 \times 2} \\ d _ {1 1} = d _ {1} l _ {c 1} ^ {2} + d _ {2} (l _ {1} ^ {2} + l _ {c 2} ^ {2} + 2 l _ {1} l _ {c 2} \cos q _ {2}) + I _ {1} + I _ {2} \\ d _ {1 2} = d _ {2 1} = d _ {2} (l _ {c 2} ^ {2} + l _ {1} l _ {c 2} \cos q _ {2}) + l _ {2} \\ d _ {2 2} = d _ {2} l _ {c 2} ^ {2} + I _ {2} \\ \mathbf {C} = \left[ c _ {i j} \right] _ {2 \times 2} \\ c _ {1 1} = h \dot {q} _ {2}, \quad c _ {1 2} = h \dot {q} _ {1} + h \dot {q} _ {2}, \quad c _ {2 1} = - h \dot {q} _ {1}, \quad c _ {2 2} = 0, h = - m _ {2} l _ {1} l _ {c 2} \sin q _ {2} \\ \mathbf {G} = \left[ \begin{array}{c c} G _ {1} & G _ {2} \end{array} \right] ^ {\mathrm{T}} \\ G _ {1} = \left(d _ {1} l _ {c 1} + d _ {2} l _ {1}\right) g \cos q _ {1} + d _ {2} l _ {c 2} g \cos \left(q _ {1} + q _ {2}\right), \quad G _ {2} = d _ {2} l _ {c 2} g \cos \left(q _ {1} + q _ {2}\right) \\ \end{array}
$$

干扰项为 $\tau_{d}=\left[0.3\sin t\quad0.1(1-e^{-t})\right]^{T}$ ，机器人系统参数为 $d_{1}=d_{2}=1kg, l_{1}=l_{2}=0.5m, l_{c1}=l_{c2}=0.25m, I_{1}=I_{2}=0.1kg\cdot m^{2}, g=9.81m/s^{2}$ 。

采用 3 种闭环迭代学习控制律, 其中, M=1 为 D 型迭代学习控制, M=2 为 PD 型迭代学习控制, M=3 为指数变增益闭环 D 型迭代学习控制。

两个关节的位置指令分别为 $\sin(3t)$ 和 $\cos(3t)$ ，为了保证被控对象初始输出与指令初值一致，取被控对象的初始状态为 $x(0)=[0\quad3\quad1\quad0]^{T}$ 。取指数变增益闭环 D 型迭代学习控制，即 M=3，仿真结果如图 11-1 至图 11-3 所示。

![](image/f538c21634192962ed3f3f513bd167e7b0cb209ddeb9e252f053da288d4e017d.jpg)

<details>
<summary>line</summary>

| time(s) | q_id, q_i(rad) |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 1.0 |
| 1.0 | 0.0 |
| 1.5 | -1.0 |
| 2.0 | 0.0 |
| 2.5 | 1.0 |
| 3.0 | 0.0 |
</details>

![](image/1a817595b8da13dce66b0a5166996f6af2397aa5c5b0aad1d76e25b32f54cb59.jpg)

<details>
<summary>line</summary>

| time(s) | q₂₄ (rad) |
| --- | --- |
| 0.0 | 1.0 |
| 0.5 | 0.0 |
| 1.0 | -1.0 |
| 1.5 | 0.0 |
| 2.0 | 1.0 |
| 2.5 | 0.0 |
| 3.0 | -1.0 |
</details>

图 11-1 20 次迭代学习的跟踪过程

机械手轨迹跟踪迭代学习控制仿真实例程序包括:①主程序,chap11\_1main.m;②Simulink 程序,chap11\_1sim.mdl;③指令程序,chap11\_linput.m;④被控对象子程序,chap11\_lplant.m;⑤控制器子程序,chap11\_1ctrl.m。程序见本章附录。

![](image/a65f68cb93d0141668744cf41b1959705add297e966b7e2f30585a1c0532d8c3.jpg)

<details>
<summary>line</summary>

| time(s) | Position tracking of Link1 |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 1.0 |
| 1.0 | 0.0 |
| 1.5 | -1.0 |
| 2.0 | 0.0 |
| 2.5 | 1.0 |
| 3.0 | 0.0 |
</details>

![](image/3479a1409146c1160b7a3f8b49f11d95e5756707a8e597accefd277b73805f08.jpg)

<details>
<summary>line</summary>

| time(s) | Position tracking of Link2 |
| --- | --- |
| 0.0 | 1.0 |
| 0.5 | 0.0 |
| 1.0 | -1.0 |
| 1.5 | 0.0 |
| 2.0 | 1.0 |
| 2.5 | 0.0 |
| 3.0 | -1.0 |
</details>

图 11-2 第 20 次迭代学习的位置跟踪

![](image/d5957cde120e61d9c8b3baec0570cd8461ca5a931925617754c75b3f944b9665.jpg)

<details>
<summary>line</summary>

| time(s) | error1 and error2 |
| --- | --- |
| 0 | 0.3 |
| 1 | 0.05 |
| 2 | 0.01 |
| 3 | 0.005 |
| 4 | 0.002 |
| 5 | 0.001 |
| 6 | 0.001 |
| 7 | 0.001 |
| 8 | 0.001 |
| 9 | 0.001 |
| 10 | 0.001 |
| 11 | 0.001 |
| 12 | 0.001 |
| 13 | 0.001 |
| 14 | 0.001 |
| 15 | 0.001 |
| 16 | 0.001 |
| 17 | 0.001 |
| 18 | 0.001 |
| 19 | 0.001 |
| 20 | 0.001 |
</details>

图 11-3 20 次迭代过程中误差范数的收敛过程
