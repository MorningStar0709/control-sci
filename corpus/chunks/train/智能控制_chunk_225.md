# 4.5.2 仿真实例

被控对象为

$$G _ {\mathrm{p}} (s) = \frac {1 3 3}{s ^ {2} + 2 5 s}$$

采样时间为 1ms, 采用 z 变换进行离散化, 离散化后的被控对象为

$$y (k) = - \mathrm{den} (2) y (k - 1) - \mathrm{den} (3) y (k - 2) + \mathrm{num} (2) u (k - 1) + \mathrm{num} (3) u (k - 2)$$

位置指令为幅值为1.0的阶跃信号， $r(k)=1.0$ 。仿真时，先运行模糊推理系统设计程序chap4\_7a.m，实现模糊推理系统fuzzpid.fis，并将此模糊推理系统调入内存中，然后运行模糊控制程序chap4\_7b.m。在程序chap4\_7a.m中，根据表4-11至表4-12，分别对e、ec、 $k_{p}$ 、 $k_{i}$ 进行隶属函数的设计。根据位置指令、初始误差和经验设计e、ec、 $k_{p}$ 、 $k_{i}$ 的范围。

在 Matlab 环境下, 对生成的模糊系统运行 plotmf 命令, 可得到模糊系统 $e, \varepsilon c, k_{p}, k_{i}$ 的隶属函数, 如图 4-22 至图 4-25 所示, 运行命令 showrule 可显示模糊规则, 可显示 9 条模糊规则, 描述如下:

(1) If (e is N) and (ec is N) then (kp is N)(ki is Z) (1)   
(2) If (e is N) and (ec is Z) then (kp is N)(ki is Z) (1)   
(3) If (e is N) and (ec is P) then (kp is N)(ki is Z) (1)   
(4) If (e is Z) and (ec is N) then (kp is N)(ki is P) (1)   
(5) If (e is Z) and (ec is Z) then (kp is P)(ki is P) (1)   
(6) If (e is Z) and (ec is P) then (kp is P)(ki is P) (1)

![](image/8b188d3119a71860f22e68f0fca5c35404d8b39a9a377ea25a064aef2ebad2cb.jpg)

<details>
<summary>line</summary>

| e | Degree of membership |
| --- | --- |
| -1.0 | 1.0 |
| -0.8 | 0.8 |
| -0.6 | 0.4 |
| -0.4 | 0.2 |
| -0.2 | 0.4 |
| 0.0 | 1.0 |
| 0.2 | 0.8 |
| 0.4 | 0.4 |
| 0.6 | 0.2 |
| 0.8 | 0.4 |
| 1.0 | 1.0 |
</details>

图4-22 误差的隶属函数

![](image/6c16b6ecad297fd454dec9a8afd2414c818350f6a579e35a3293c1a080ce19fd.jpg)

<details>
<summary>line</summary>

| ec | Degree of membership (N) | Degree of membership (P) |
| --- | --- | --- |
| -1.0 | 1.0 | 0.0 |
| -0.8 | 0.8 | 0.2 |
| -0.6 | 0.4 | 0.4 |
| -0.4 | 0.2 | 0.6 |
| -0.2 | 0.0 | 0.8 |
| 0.0 | 0.0 | 1.0 |
| 0.2 | 0.0 | 0.8 |
| 0.4 | 0.0 | 0.4 |
| 0.6 | 0.2 | 0.2 |
| 0.8 | 0.4 | 0.0 |
| 1.0 | 1.0 | 0.0 |
</details>

图4-23 误差变化率的隶属函数

![](image/cd8c421e65e7e6d9843d33c3b5d1a8e1316d8c832b442823bb972f5340bcdcc2.jpg)

<details>
<summary>line</summary>

| k_p | Degree of membership |
| --- | --- |
| -3 | 1.0 |
| -2 | 0.4 |
| -1 | 0.0 |
| 0 | 1.0 |
| 1 | 0.4 |
| 2 | 0.0 |
| 3 | 1.0 |
</details>

图4-24 $k_{\mathrm{p}}$ 的隶属函数  
![](image/8b1a3d4fb1dcba1df6710473ce3568049b1705263ab73c4681ece66bd144b4f8.jpg)

<details>
<summary>line</summary>

| ki | Degree of membership (N) | Degree of membership (Z) | Degree of membership (P) |
| --- | --- | --- | --- |
| -0.1 | 1.0 | 0.0 | 0.0 |
| -0.08 | 0.8 | 0.2 | 0.0 |
| -0.06 | 0.4 | 0.4 | 0.0 |
| -0.04 | 0.2 | 0.6 | 0.0 |
| -0.02 | 0.0 | 0.8 | 0.0 |
| 0.0 | 0.0 | 1.0 | 0.0 |
| 0.02 | 0.0 | 0.8 | 0.0 |
| 0.04 | 0.2 | 0.6 | 0.0 |
| 0.06 | 0.4 | 0.4 | 0.0 |
| 0.08 | 0.8 | 0.2 | 0.0 |
| 0.1 | 1.0 | 0.0 | 1.0 |
</details>
