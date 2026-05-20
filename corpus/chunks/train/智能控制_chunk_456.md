# 9.10.2 仿真实例

仿真中,采用控制律式(9.53)和自适应律式(9.62)。在离散化自适应律式(9.62)微分方程时，取两种离散化方法：当 $S = 1$ 时，采用简单的差分方法进行离散化，当 $S = 2$ 时，采用RKM方法进行离散化。取 $m = 1, l = 1, g = 9.8, d = 0.5\sin (t), C_0 = 2, \Delta D = 0.8D_0, \Delta C = 0.8C_0, \Delta G = 0.8G_0$ 。系统的初始状态为 $x = [0,0]$ 。位置指令为 $q_{\mathrm{d}} = 0.5\sin (k \cdot t_{\mathrm{s}})$ ，采样时间取 $t_{\mathrm{s}} = 0.001$ ，取控制器参数为 $k_{\mathrm{p}} = 40, k_{\mathrm{v}} = 20, Q = \left[ \begin{array}{cc}2000 & 0 \\ 0 & 2000 \end{array} \right]$ ，取自适应律参数为 $\gamma = 5, k_1 = 0.01$ 。RBF网络的隐含层节点数取10，网络权值的初始值取0，高斯基参数初值的选取见控制器主程序chap9\_8.m。取 $M = 1$ ，未采用神经网络补偿，仿真结果如图9-36所示。取 $M = 2$ ，采用神经网络补偿，仿真结果如图9-37和图9-38所示。

![](image/1ee204dd3c2563b2f241ebc76ed5765784da74117819ca873c399653e5f2d815.jpg)

<details>
<summary>line</summary>

| time(s) | Position tracking of single link | Position tracking error of single link |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 1 | 0.6 | -0.1 |
| 2 | 0.5 | -0.12 |
| 3 | 0.2 | -0.13 |
| 4 | -0.2 | -0.14 |
| 5 | -0.5 | -0.15 |
| 6 | -0.2 | -0.14 |
| 7 | 0.4 | -0.12 |
| 8 | 0.6 | -0.1 |
| 9 | 0.3 | -0.12 |
| 10 | -0.1 | -0.13 |
</details>

图 9-36 未用神经网络补偿的位置跟踪及其误差 $(M=1)$

![](image/64790629403ff349885a8cee5360cfffcb040facd16872ca72fe558e3eb1df64.jpg)

<details>
<summary>line</summary>

| time(s) | Position tracking of single link | Position tracking error of single link (×10⁻³) |
| --- | --- | --- |
| 0 | 0.0 | -2.5 |
| 1 | 0.5 | -1.0 |
| 2 | 0.5 | -0.5 |
| 3 | 0.0 | -0.5 |
| 4 | -0.5 | -0.5 |
| 5 | -0.5 | -0.5 |
| 6 | 0.0 | -0.5 |
| 7 | 0.5 | -0.5 |
| 8 | 0.5 | 0.5 |
| 9 | 0.0 | 0.5 |
| 10 | -0.5 | 0.0 |
</details>

图 9-37 采用神经网络补偿的位置跟踪及其误差 $(M=2)$

![](image/929d50c4f08bbb5cafaf0d12bcb13520aac756d625b8616a6df48ce8033372c7.jpg)

<details>
<summary>line</summary>

| time(s) | f and f_p |
| --- | --- |
| 0 | 5 |
| 1 | 5 |
| 2 | 5 |
| 3 | 5 |
| 4 | 5 |
| 5 | 5 |
| 6 | 5 |
| 7 | 5 |
| 8 | 5 |
| 9 | 5 |
| 10 | 5 |
</details>

图 9-38 不确定项及其神经网络逼近结果 $(M=2)$

仿真程序为 chap9\_8.m 和 chap9\_8plant.m。
