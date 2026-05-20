# 1. 线性元件的微分方程

现举例说明控制系统中常用的电气元件、力学元件等微分方程的列写。

例 2-1 图 2-1 是由电阻 R、电感 L 和电容 C 组成的无源网络，试列写以 $u_{i}(t)$ 为输入量，以 $u_{o}(t)$ 为输出量的网络微分方程。

解 设回路电流为 $i(t)$ ，由基尔霍夫定律可写出回路方程为

$$L \frac {\mathrm{d} i (t)}{\mathrm{d} t} + \frac {1}{C} \int i (t) \mathrm{d} t + R i (t) = u _ {i} (t)u _ {o} (t) = \frac {1}{C} \int i (t) \mathrm{d} t$$

![](image/8fb4ae7794051e4c92c6977d5c001f97f266b5e8d2127f9748ec708193cabeef.jpg)

<details>
<summary>chemical</summary>

Electrical circuit diagram with inductor, resistor, and capacitor components labeled with time-dependent variables
</details>

图 2-1 RLC 无源网络

消去中间变量 $i(t)$ ，便得到描述网络输入输出关系的微分方程为

$$L C \frac {\mathrm{d} ^ {2} u _ {o} (t)}{\mathrm{d} t ^ {2}} + R C \frac {\mathrm{d} u _ {o} (t)}{\mathrm{d} t} + u _ {o} (t) = u _ {i} (t) \tag {2-1}$$

显然,这是一个二阶线性微分方程,也就是图 2-1 无源网络的时域数学模型。

例 2-2 试列写图 2-2 所示电枢控制直流电动机的微分方程, 要求取电枢电压 $u_{a}(t)$ 为输入量, 电动机转速 $\omega_{m}(t)$ 为输出量。图中 $R_{a}, L_{a}$ 分别是电枢电路的电阻和电感; $M_{c}$ 是折合到电动机轴上的总负载转矩。激磁磁通设为常值。

解 电枢控制直流电动机的工作实质是将输入的电能转换为机械能,也就是由输入的电枢电压 $u_{a}(t)$ 在电枢回路中产生电枢电流 $i_{a}(t)$ ,再由电流 $i_{a}(t)$ 与激磁磁通相互作用产生电磁转矩

![](image/3175d17a6c290ab7f9c21573f9998bceaff687ef5dec9969d25db07f81dd5e53.jpg)

<details>
<summary>text_image</summary>

+
if
-
Ia
Ra
ia
Ea
SM
ωm
负载
Jm,fm
ua
-
</details>

图 2-2 电枢控制直流电动机原理图
