1.13 图 1.22 的结构是一个机械系统的例子 $^{[7]}$ ，其摩擦力在某一区域可以为负。一个由线性弹簧固定的物体 m，在传动带上以速度 $v_{0}$ 做匀速运动，弹簧的弹性系数为 $k_{1}$ 和 $k_{2}$ 。由传动带施加的摩擦力 $h(v)$ 是相对速度 $v = v_{0} - \dot{y}$ 的函数。假设当 $|v| > 0$ 时， $h(v)$ 是光滑函数。除摩擦力外，假设还有一个线性黏滞摩擦力正比于 $\dot{y}$ 。

(a) 写出物体 m 的运动方程。  
(b) 只分析 $\left|\dot{y}\right|<<v_{0}$ 的区域, 可通过 $h(v_{0})-\dot{y}h'(v_{0})$ 用泰勒级数逼近 $h(v)$ , 利用该近似降价系统模型。  
(c) 考虑到 1.2.3 节讨论的摩擦力模型, 描述哪种摩擦力特性 $h(v)$ 会使系统具有负摩擦力?

1.14 图 1.23 所示为一个坡度为 $\theta$ 的道路上运动的车辆, v 是车的速度, M 是其质量, F 是由发动机产生的牵引力。假设摩擦力有库仑摩擦力和线性黏滞摩擦力, 拉力正比于 $v^{2}$ 。把 F 看成控制输入, $\theta$ 作为扰动输入, 求系统的状态模型。

![](image/e814e4f9bfb27dd920b1cf4bd482e799de2674623e07a7eef3ef3f7e0933bf9c.jpg)

<details>
<summary>text_image</summary>

k₁
m
y
k₂
v₀
</details>

图1.22 习题1.13

![](image/09a69aec3be07f2f37c30b3ff5e89f293417263c5fd5005f98c8fe2abfe41c4d.jpg)

<details>
<summary>text_image</summary>

v
F
Mg
θ
</details>

图1.23 习题1.14

1.15 考虑图 1.24 所示的倒摆 $^{[110]}$ 。单摆的支点装在一个沿水平方向运动的小车上，小车由电机驱动，电机在小车上施加水平方向的力 F。图中还给出了单摆的受力分析：重心的力 mg，水平方向的反作用力 H，以及作用于支点的竖直方向的反作用力 V。写出单摆重心在水平方向和竖直方向上的牛顿定律，有

$$m \frac {d ^ {2}}{d t ^ {2}} (y + L \sin \theta) = H, \qquad m \frac {d ^ {2}}{d t ^ {2}} (L \cos \theta) = V - m g$$

取对重心的力矩可得到转矩方程

$$I \ddot {\theta} = V L \sin \theta - H L \cos \theta$$

而小车在水平方向上的牛顿定律为

$$M \ddot {y} = F - H - k \dot {y}$$

其中，m 是单摆的质量，M 是小车的质量，L 是重心到支点的距离，I 是单摆对重心的转动惯量，k 是摩擦系数，y 是支点的位移， $\theta$ 是单摆转动的角度（顺时针测量），g 是重力加速度。

(a) 运用给定的微分法消去 V 和 H, 证明运动方程简化为:

$$I \ddot {\theta} = m g L \sin \theta - m L ^ {2} \ddot {\theta} - m L \ddot {y} \cos \thetaM \ddot {y} = F - m \left(\ddot {y} + L \ddot {\theta} \cos \theta - L \dot {\theta} ^ {2} \sin \theta\right) - k \dot {y}$$

(b) 对 $\ddot{\theta}$ 和 $\ddot{y}$ 解上面的方程, 证明

$$
\left[ \begin{array}{l} \ddot {\theta} \\ \ddot {y} \end{array} \right] = \frac {1}{\Delta (\theta)} \left[ \begin{array}{c c} m + M & - m L \cos \theta \\ - m L \cos \theta & I + m L ^ {2} \end{array} \right] \left[ \begin{array}{c} m g L \sin \theta \\ F + m L \dot {\theta} ^ {2} \sin \theta - k \dot {y} \end{array} \right]
$$

其中， $\Delta (\theta) = (I + mL^2)(m + M) - m^2 L^2\cos^2\theta \geqslant (I + mL^2)M + mI > 0$

(c) 用 $x_{1}=\theta, x_{2}=\dot{\theta}, x_{3}=y$ 和 $x_{4}=\dot{y}$ 作为状态变量，用 u=F 作为控制输入，写出状态方程。

![](image/0958fdc9a94b93234fe1982d715084eae401de2356f66f675cb8d119da7ae5a0.jpg)

<details>
<summary>text_image</summary>

单摆
小车
F
</details>
