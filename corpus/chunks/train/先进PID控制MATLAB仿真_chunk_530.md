# 13.3.2 柔性机械臂的偏微分方程建模

对于柔性臂控制的研究多数都是基于 ODE 动力学模型进行的，虽然 ODE 模型形式上简单而且方便控制器的设计，但难以准确描述柔性结构的分布参数特性，同时也可能会造成溢出不稳定的问题。相比于 ODE 模型，PDE 模型更能精确地反映柔性结构的动力学特性。

本节利用Hamilton方法建立系统的PDE动力学模型[8,9]。Hamilton方法的优点是：避免对系统做复杂的受力分析，而直接通过数学推导，不仅能求出系统的PDE方程，而且能够得到相应的系统的边界条件。

研究对象为水平移动的单杆柔性机械臂，如图 13-8 所示。单杆柔性机械臂在水平面运动，机械臂的末端有边界控制输入。不考虑重力情况下，XOY 是系统的惯性坐标系，xOy 为随动坐标系。

为了简单起见，在函数变量中省略时间 $t$ ，例如， $\theta (t)$ 表示为 $\theta$ 。柔性机械臂物理参数见表13-2，取 $(*)_x = \frac{\partial(*)}{\partial x}$ ， $(\ast) = \frac{\partial(\ast)}{\partial t}$ 。

![](image/5fe85ed35c6852d5362dcc1a6f25f60a76e67a2f23c2614e13aa6798d7b2d46a.jpg)

<details>
<summary>text_image</summary>

y
负载
F(t)
y(x,t)
x
θ(t)
xθ
电机
τ(t)
O
X
</details>

图 13-8 柔性机械臂的结构示意图

表 13-2 柔性机械臂物理参数

<table><tr><td>符号</td><td>物理意义</td><td>单位</td></tr><tr><td> $L$ </td><td>机械臂长度</td><td>m</td></tr><tr><td>EI</td><td>均匀梁的弯曲刚度</td><td> $N·m^{2}$ </td></tr><tr><td> $m$ </td><td>机械臂终端负载质量</td><td>kg</td></tr><tr><td> $I_{h}$ </td><td>中心转动惯量</td><td> $kg·m^{2}$ </td></tr><tr><td> $\tau$ </td><td>初始端点的电机控制输入力矩</td><td> $N·m$ </td></tr><tr><td> $F$ </td><td>末端负载的电机控制输入力矩</td><td> $N·m$ </td></tr><tr><td> $\theta(t)$ </td><td>未考虑变形时的关节转动角度</td><td>rad</td></tr><tr><td> $\rho$ </td><td>杆单位长度上的质量</td><td>kg/m</td></tr><tr><td> $y(x,t)$ </td><td>机械臂在 $x$ 点处的弹性变形</td><td>m</td></tr></table>

由任意时刻原点挠性弯曲为零，得 $y(0,t) = 0$ ，由任意时刻原点挠性弯曲沿 $x$ 轴变化率为零，得 $y_{x}(0,t) = 0$ ，则边界条件表示为

$$y (0) = y _ {x} (0) = 0 \tag {13.21}$$

可近似把柔性机械臂上在随动坐标系 $xOy$ 上任何一点 $[x, y(x, t)]$ 在惯性坐标系 $XOY$ 下表示为

$$z (x) = x \theta + y (x) \tag {13.22}$$

式中， $z(x)$ 为机械臂的偏移量。

由式（13.21）和式（13.22），可得

$$z (0) = 0 \tag {13.23}z _ {x} (0) = \theta \tag {13.24}\frac {\partial^ {n} z (x)}{\partial x ^ {n}} = \frac {\partial^ {n} y (x)}{\partial x ^ {n}}, (n \geqslant 2) \tag {13.25}$$

由式（13.25）可得 $z_{xx}(x)=y_{xx}(x)$ ， $\ddot{z}_{x}(0)=\ddot{\theta}$ ， $z_{xx}(0)=y_{xx}(0)$ ， $z_{xx}(L)=y_{xx}(L)$ ， $z_{xxx}(L)=y_{xxx}(L)$ 。

根据Hamilton原理有[9]

$$\int_ {t _ {1}} ^ {t _ {2}} \left(\delta E _ {\mathrm{k}} - \delta E _ {\mathrm{p}} + \delta W _ {\mathrm{c}}\right) \mathrm{d} t = 0 \tag {13.26}$$

式中， $\delta E_{k}$ 、 $\delta E_{p}$ 和 $\delta W_{c}$ 分别是动能、势能和非保守力做功的变分。
