# 5.3.3 仿真实例

被控对象取单级倒立摆,如图 5-12 所示,其动态方程为

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = \frac {g _ {0} \sin x _ {1} - m l x _ {2} ^ {2} \cos x _ {1} \sin x _ {1} / (m _ {\mathrm{c}} + m)}{l (4 / 3 - m \cos^ {2} x _ {1} / (m _ {\mathrm{c}} + m))} + \frac {\cos x _ {1} / (m _ {\mathrm{c}} + m)}{l (4 / 3 - m \cos^ {2} x _ {1} / (m _ {\mathrm{c}} + m))} u = f (x) + g (x) u \end{array}
$$

式中， $x_{1}$ 和 $x_{2}$ 分别为摆角和摆速， $g_{0}=9.8m/s^{2}$ ， $m_{c}=1kg$ 为小车质量，m 为摆杆质量，m=

0.1kg, l 为摆长的一半, l = 0.5m, u 为控制输入。

位置指令为 $x_{\mathrm{d}}(t) = 0.1\sin (\pi t)$ 。取以下5种隶属函数： $\mu_{\mathrm{NM}}(x_i) = \exp [-((x_i + \pi /6) / (\pi /24))^2],\mu_{\mathrm{NS}}(x_i) = \exp [-((x_i + \pi /12) / (\pi /24))^2],\mu_{\mathrm{Z}}(x_i) = \exp [-(x_i / (\pi /24))^2],$ $\mu_{\mathrm{PS}}(x_i) = \exp [-((x_i - \pi /12) / (\pi /24))^2],\mu_{\mathrm{PM}}(x_i) = \exp [-((x_i - \pi /6) / (\pi /24))^2]$ 。则用于逼近 $f$ 和 $g$ 的模糊规则分别有25条。

根据隶属函数设计程序,可得到隶属函数图,如图 5-13 所示。

![](image/244dbadaf712be5fb688c17c40682cbdba0c58467dadfe04d3abba40cd7076d7.jpg)

<details>
<summary>text_image</summary>

V
m
2l
θ
O
u
mc
H
x
</details>

图5-12 单级倒立摆系统示意图

![](image/cb2c92ffdc747baafe9f02a7c136549a4e63e6017f9eb815c8b2cabe00ce3707.jpg)

<details>
<summary>line</summary>

| x | Membership function degree |
| --- | --- |
| -0.8 | 0.0 |
| -0.6 | 0.5 |
| -0.4 | 0.9 |
| -0.2 | 0.5 |
| 0.0 | 0.0 |
| 0.2 | 0.5 |
| 0.4 | 0.9 |
| 0.6 | 0.5 |
</details>

图5-13 $x_{i}$ 的隶属函数

倒立摆初始状态为 $[\pi /60,0],\pmb{\theta}_f$ 和 $\pmb{\theta}_{g}$ 中各元素的初始值取0.10，采用控制律式(5.26)，自适应律采用式(5.28)和式(5.29)，取 $\pmb{\eta}(\pmb {x}) = \pmb {\xi}(\pmb {x})$ 。取 $Q = \left[ \begin{array}{cc}10 & 0\\ 0 & 10 \end{array} \right],k_{1} = 2,k_{2} = 1.$ 考虑到 $f(x_{1},x_{2})$ 的取值范围比 $g(x_{1},x_{2})$ 的取值范围大得多，自适应参数取 $\gamma_{1} = 50,\gamma_{2} = 1$

在程序中,分别用 FS1, FS2 和 FS 表示模糊系统 $\xi(x)$ 的分子、分母及 $\xi(x)$ ，仿真结果如图 5-14 至图 5-17 所示。

![](image/98c8587abfab854824bd3d06a9fa56f4ab00f815a72120dcbe6ff5ad59b92bd9.jpg)

<details>
<summary>line</summary>

| time(s) | Position tracking |
| --- | --- |
| 0 | 0.0 |
| 1 | 0.14 |
| 2 | -0.1 |
| 3 | 0.1 |
| 4 | -0.1 |
| 5 | 0.1 |
| 6 | -0.1 |
| 7 | 0.1 |
| 8 | -0.1 |
| 9 | 0.1 |
| 10 | 0.0 |
</details>

图5-14 位置跟踪

![](image/68b20881c3f05649f25f93cccdb3d18cfa6d0b3a07f9089e14c1a3f0e9630d02.jpg)

<details>
<summary>line</summary>

| time(s) | Control input |
| --- | --- |
| 0 | -3 |
| 1 | 2 |
| 2 | -2 |
| 3 | 2 |
| 4 | -2 |
| 5 | 2 |
| 6 | -2 |
| 7 | 2 |
| 8 | -2 |
| 9 | 2 |
| 10 | 0 |
</details>

图5-15 控制输入信号
