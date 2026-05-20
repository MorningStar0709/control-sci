# 2.1 微分方程问题的提出

常微分方程是描述物质运动的一种数学工具。通过分析相应微分方程的各种特性，能够对所研究物质的运动获得某些定性和定量的了解。本节我们将通过实例说明一些物理、力学的某些定律如何导致微分方程问题。

例 2.1.1 单摆运动。单摆又称为钟摆或数学摆。所谓单摆运动是指一质量为 m > 0 的小球用长度为 l 的柔软细绳拴住，细绳的一端固定在某点 O 处，小球在垂直平面内运动。略去空气的阻力和细绳在 O 点处的摩擦力，并且认为细绳的长度 l 不变，仅考虑地球的引力和细绳对小球的拉力（图 2.1.1）。

![](image/db918bf39a7d63cdf101ff6a06108484206bdc1443dc229adb781aa7c2a7eae3.jpg)

<details>
<summary>text_image</summary>

O
θ
l
m
θ
mg
</details>

图2.1.1

根据牛顿第二定律得到单摆运动的规律为

$$\frac {\mathrm{d}}{\mathrm{d} t} (m v) = - m g \sin \theta . \tag {2.1.1}$$

根据圆周运动规律有 $l\frac{\mathrm{d}\theta}{\mathrm{d}t} = v$ 于是从式(2.1.1)得出

$$l \frac {\mathrm{d} ^ {2} \theta}{\mathrm{d} t ^ {2}} = - g \sin \theta . \tag {2.1.2}$$

当 $\theta$ 的绝对值 $|\theta|$ 比较小时，可用 $\theta$ 来近似 $\sin \theta$ 。这样得到式 (2.1.2) 的线性化微分方程为

$$l \frac {\mathrm{d} ^ {2} \theta}{\mathrm{d} t ^ {2}} = - g \theta . \tag {2.1.3}$$

例2.1.2 电容器的放电规律。电容器 $C$ 的极板通过电感 $L$ 和电阻 $R$ 相连接，如图2.1.2所示。

![](image/b8139cd2e68e478ec3b780c336adbda85cd6cb5483a2963f126942282bbe4a03.jpg)

<details>
<summary>natural_image</summary>

Simple electrical circuit diagram with resistor, inductor, and capacitor (no text labels beyond component symbols)
</details>

图2.1.2

设电容器极板上的电荷量为 $Q$ ，这时电路中的电流强度 $I$ 等于电荷量对时间的变化率，即

$$I = \frac {\mathrm{d} Q}{\mathrm{d} t}.$$

令电容器两极板上 $t$ 时刻的电位差为 $V(t)$ 。于是电路中总电位降为 $IR + V$ 。根据 Kirchhoff 定律，电路中总电位降等于作用的电动势。由于该电路中仅有自感电动势 $-L\frac{\mathrm{d}I}{\mathrm{d}t}$ ，故有如下等式关系：

$$I R + V = - I \frac {\mathrm{d} I}{\mathrm{d} t}. \tag {2.1.4}$$

由于 $V = \frac{Q}{C}, I = \frac{\mathrm{d}Q}{\mathrm{d}t}$ , 所以由式 (2.1.4) 得电容器的放电规律为

$$L \frac {\mathrm{d} ^ {2} Q}{\mathrm{d} t ^ {2}} + R \frac {\mathrm{d} Q}{\mathrm{d} t} + \frac {Q}{C} = 0. \tag {2.1.5}$$

例 2.1.3 人造地球卫星的运动规律. 人造卫星绕地球运动的规律与行星绕太阳运动的规律是一样的, 因而它们的受力状况也是一样的. 由于人造地球卫星绕地球的初始条件能够给出, 所以它绕地球的运动完全确定 (图 2.1.3).

由角动量守恒定律知，人造地球卫星的运动轨道是一平面曲线。设当 $t = 0$ 时，人造地球卫星运动的初始条件为

![](image/e0ae037ccc977bf0b44a72bdd0fcae3dc6aa346feaa645fa13692d11cf78110b.jpg)

<details>
<summary>text_image</summary>

m
r
φ
0
r₀
m₀
v₀
α
</details>

图2.1.3

$$
\left\{ \begin{array}{l} r _ {0} = r (0) = R + h, \\ \varphi_ {0} = \varphi (0), \\ \dot {r} _ {0} = \dot {r} (0) = v _ {0} \cos \alpha , \\ \dot {\varphi} _ {0} = \dot {\varphi} (0) = \frac {v _ {0}}{r _ {0}} \sin \alpha , \end{array} \right. \tag {2.1.6}
$$
