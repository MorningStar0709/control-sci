# 11.5.3 仿真实例

考虑两输入两输出线性系统

$$
\begin{array}{l} \left[ \begin{array}{l} \dot {x} _ {1} (t) \\ \dot {x} _ {2} (t) \end{array} \right] = \left[ \begin{array}{c c} - 2 & 3 \\ 1 & 1 \end{array} \right] \left[ \begin{array}{l} x _ {1} (t) \\ x _ {2} (t) \end{array} \right] + \left[ \begin{array}{c c} 1 & 1 \\ 0 & 1 \end{array} \right] \left[ \begin{array}{l} u _ {1} (t) \\ u _ {2} (t) \end{array} \right] \\ \left[ \begin{array}{l} y _ {1} (t) \\ y _ {2} (t) \end{array} \right] = \left[ \begin{array}{l l} 2 & 0 \\ 0 & 1 \end{array} \right] \left[ \begin{array}{l} x _ {1} (t) \\ x _ {2} (t) \end{array} \right] \\ \end{array}
$$

期望跟踪轨迹为

$$
\left[ \begin{array}{l} y _ {1 \mathrm{d}} (t) \\ y _ {2 \mathrm{d}} (t) \end{array} \right] = \left[ \begin{array}{l} \sin (3 t) \\ \cos (3 t) \end{array} \right], t \in [ 0, 1 ]
$$

由于 $CB=\begin{bmatrix}2 & 2 \\ 0 & 1\end{bmatrix}$ ，取 $\Gamma=\begin{bmatrix}0.95 & 0 \\ 0 & 0.95\end{bmatrix}$ ，可满足定理1中的条件(1)，在控制律式(11.14)

中取 $L=\begin{bmatrix}2.0 & 0 \\ 0 & 2.0\end{bmatrix}$ ， $\Psi=0$ ，系统的初始状态为 $\begin{bmatrix}x_{1}(0) \\ x_{2}(0)\end{bmatrix}=\begin{bmatrix}0 \\ 1\end{bmatrix}$ 。

在 chap11\_2sim.mdl 程序中,选择 Simulink 的 Manual Switch 开关,将开关向下,取 PD 型开环迭代学习控制律式(11.14),仿真结果如图 11-4 至图 11-6 所示。将开关向上,采用 PD 型闭环迭代学习控制律,仿真结果如图 11-7 至图 11-9 所示。可见,闭环收敛速度好于开环收敛速度。

线性时变连续系统迭代学习控制仿真实例程序包括: ① 主程序, chap11\_2main.m; ② Simulink 程序, chap11\_2sim.mdl; ③ 被控对象子程序, chap11\_2plant.m; ④ 控制器子程序, chap11\_2ctrl.m; ⑤ 指令程序, chap11\_2input.m。程序见本章附录。

![](image/89a72b67aacc67709eaf5821e2cadeaf82fecaf7d7fae8f49571a514f9acc5a3.jpg)

<details>
<summary>line</summary>

| time(s) | x_d^2x_1 | x_2d^2x_1 | x_2d^2x_2 |
| --- | --- | --- | --- |
| 0.0 | 0 | 0 | 0 |
| 0.2 | 0 | 0 | 0 |
| 0.4 | 0 | 0 | 0 |
| 0.6 | 0 | 0 | 0 |
| 0.8 | 0 | 0 | 0 |
| 1.0 | 0 | 0 | 0 |
</details>

图 11-4 30 次迭代学习的跟踪过程(开环 PD 控制)

![](image/b29d2f05d648b5fde62c1c481473441c06b3d2fe0927045cfbfc9428a0373c12.jpg)

<details>
<summary>line</summary>

| time(s) | Position tracking of x₁ | Position tracking of x₂ |
| --- | --- | --- |
| 0.0 | 0.0 | 1.0 |
| 0.2 | 0.5 | 0.8 |
| 0.4 | 0.9 | 0.5 |
| 0.6 | 1.0 | 0.0 |
| 0.8 | 0.7 | -0.5 |
| 1.0 | 0.1 | -1.0 |
</details>

图 11-5 第 30 次迭代学习的位置跟踪(开环 PD 控制)

![](image/ac98f3167fb8280407012488519d320307910baa4ae0aba03933e4266c21a52c.jpg)

<details>
<summary>line</summary>
