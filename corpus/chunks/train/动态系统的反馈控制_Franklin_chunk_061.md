# 例2.5 旋转运动：摆

（1）写出图 2.14 所示单摆的运动方程，其中所有质量都集中到终端，枢轴处有扭矩 $T_{c}$ 。

![](image/6372015ece3ae2e1fed809cc73ddc3c7b6cf002734f31455ee3c71e1b177b851.jpg)

<details>
<summary>text_image</summary>

Tc
l
θ
mg
</details>

图2.14 摆

（2）给定 $1 ~N \cdot m$ 的阶跃输入 $T_{c}$ ，利用 Matlab 工具确定 $\theta$ 与时间的关系曲线。假设 $l = 1 ~m, m = 1 ~kg, g = 9.81 ~m/s^{2}$ 。

解答。

（1）运动方程：折合到枢轴点的转动惯量 $I=ml^{2}$ 。相对于枢轴点的所有力矩之和包括由重力产生的力矩以及施加的力矩 $T_{c}$ 。由式(2.14)得到运动方程为

$$T _ {\mathrm{c}} - m g l \sin \theta = I \ddot {\theta} \tag {2.21}$$

通常可改写为

$$\ddot {\theta} + \frac {g}{l} \sin \theta = \frac {T _ {\mathrm{c}}}{m l ^ {2}} \tag {2.22}$$

由于在方程中存在 $\sin\theta$ 项，所以该方程是非线性的，非线性方程将在第9章讨论。然而，我们可以假定摆的运动是小范围的，即 $\sin\theta\approx\theta$ ，因而可对系统进行线性化处理，那么式(2.22)可变成线性方程，即

$$\ddot {\theta} + \frac {g}{l} \theta = \frac {T _ {\mathrm{c}}}{m l ^ {2}} \tag {2.23}$$

如果没有外加力矩，这就是一个谐波振荡器的固有运动方程，其固有频率为 $^{①}$

$$\omega_ {\mathrm{n}} = \sqrt {\frac {g}{l}} \tag {2.24}$$

由式 $(2.7)$ 的形式，得传递函数为

$$\frac {\Theta (s)}{T _ {c} (s)} = \frac {\frac {1}{m l ^ {2}}}{s ^ {2} + \frac {g}{l}} \tag {2.25}$$

（2）时间关系曲线图：系统动态可以根据其传递函数描述成 Matlab 语句，且其阶跃响应用 step 函数实现，Matlab 语句如下：

t = 0:0.02:10; % vector of times for output, 0 to 10 at 0.02 increments
m = 1; % value of mass (Kg)
L = 1; % value of length (m)
g = 9.81; % value of gravity, g (m/sec $^{2}$ )
s = tf('s'); % sets up transfer function input mode
sys = (1/(m*L^2))/(s^2 + g/L)
y = step(sys,t); % computes step responses at times given by t for step at t = 0
Rad2Deg = 57.3; % converts radians to degrees
plot(t, Rad2Deg*y) % converts output from radians to degrees and plots step response

则可得到如图 2.15 所示的时间关系曲线图。

正如本例所见，导出的运动方程通常是非线性的。这类方程比线性方程更难求解，并且由非线性模型产生的可能的运动种类比那些由线性模型产生的更难划分。因此，为了利用线性分析方法，有必要对模型进行线性化。线性模型和线性分析可能仅用来设计控制系统（其作用是维持系统在线性区域内）。一旦在线性分析基础上设计了一个控制系统，且具有期望的性能，那么为了验证其性能，需谨慎进行进一步的分析或对具有重要非线性的系统进行准确的数值仿真。Simulink 软件是实施仿真的便利工具，可处理大部分的非线性问题，这一仿真工具是通过搭建运动方程的框图 $^{①}$ 来实现的。例 2.5 中，由式(2.23)可得具有参数的摆的线性运动方程为

![](image/69d1b1e00a8fde1bca59a514451fb32c42bedbfb5b3fa71d343af029644a7114.jpg)

<details>
<summary>line</summary>

| 时间/s | 摆角θ(°) |
| --- | --- |
| 0 | 0 |
| 1 | 12 |
| 2 | 0 |
| 3 | 12 |
| 4 | 0 |
| 5 | 12 |
| 6 | 0 |
| 7 | 12 |
| 8 | 0 |
| 9 | 12 |
| 10 | 0 |
</details>

图 2.15 $1N \cdot m$ 的阶跃输入下摆的响应曲线

$$\ddot {\theta} = - 9. 8 1 \theta + 1 \tag {2.26}$$

由 Simulink 得出的框图如图 2.16 所示。注意图形左侧部分圆圈中 “+” 号和 “-” 号是表征式 (2.26) 的相加和相减。
