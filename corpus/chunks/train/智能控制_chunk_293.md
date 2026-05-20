# 5.4.4 仿真实例

被控对象为一个二阶系统

$$\ddot {x} = - 2 5 \dot {x} + 1 3 3 u$$

位置指令为 $\sin (\pi t)$ 。取以下6种隶属函数： $\mu_{\mathrm{N3}}(x) = 1 / (1 + \exp (5(x + 2)))$ ， $\mu_{\mathrm{N2}}(x) =$ $\exp (-x + 1.5)^2),\mu_{\mathrm{N1}}(x) = \exp (-x + 0.5)^2),\mu_{\mathrm{P1}}(x) = \exp (-x - 0.5)^2),\mu_{\mathrm{P2}}(x) =$ $\exp (-x - 1.5)^2),\mu_{\mathrm{P3}}(x) = 1 / (1 + \exp (-5(x - 2)))$ 。

系统初始状态为 $[1,0],\theta$ 中各元素的初始值均取0，采用控制律式(5.50)，自适应律取式(5.64)。取 $Q = \begin{bmatrix} 50 & 0 \\ 0 & 50 \end{bmatrix}, k_1 = 1, k_2 = 10$ ，自适应参数取 $\gamma = 50$ 。

根据隶属函数设计程序,可得到隶属函数图,如图 5-19 所示。在控制系统仿真程序中,分别用 FS2,FS1 和 FS 表示模糊系统 $\xi(x)$ 的分子、分母及 $\xi(x)$ ,仿真结果如图 5-20 和图 5-21 所示。

![](image/8f96dcf80a22aba8ad8dcaa2215e8827fb9c79db131a68869021055f47605e9b.jpg)

<details>
<summary>line</summary>

| x | Membership function degree |
| --- | --- |
| -3.0 | 1.0 |
| -2.5 | 0.8 |
| -2.0 | 0.6 |
| -1.5 | 0.4 |
| -1.0 | 0.2 |
| -0.5 | 0.0 |
| 0.0 | 0.2 |
| 0.5 | 0.4 |
| 1.0 | 0.6 |
| 1.5 | 0.8 |
| 2.0 | 1.0 |
| 2.5 | 0.8 |
| 3.0 | 0.6 |
</details>

图5-19 $x$ 的隶属函数

直接自适应模糊控制程序有5个:①隶属函数设计程序,chap5\_5mf.m;②Simulink主程序,chap5\_5sim.mdl;③控制器S函数程序,chap5\_5s.m;④被控对象S函数程序,chap5\_5plant.m;⑤作图程序,chap5\_5plot.m。程序见附录。

![](image/566815fd7927ebaa6e78f5214f76c26e78836aeff9a52c59990a9b37aa4458f8.jpg)

<details>
<summary>line</summary>

| time(s) | Position tracking |
| --- | --- |
| 0 | 0.0 |
| 1 | 1.0 |
| 2 | -1.0 |
| 3 | 1.0 |
| 4 | -1.0 |
| 5 | 1.0 |
| 6 | -1.0 |
| 7 | 1.0 |
| 8 | -1.0 |
| 9 | 1.0 |
| 10 | 0.0 |
</details>

图 5-20 位置跟踪

![](image/9facd79574f800ae71730f4dab210b0bc8dc8d48edaaf3135a741f9c19b56c47.jpg)

<details>
<summary>line</summary>

| time(s) | Position tracking error |
| --- | --- |
| 0 | -1.0 |
| 1 | -0.2 |
| 2 | 0.0 |
| 3 | 0.0 |
| 4 | 0.0 |
| 5 | 0.0 |
| 6 | 0.0 |
| 7 | 0.0 |
| 8 | 0.0 |
| 9 | 0.0 |
| 10 | 0.0 |
</details>

图5-21 跟踪误差
