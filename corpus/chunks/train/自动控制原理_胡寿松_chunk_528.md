# 1. 相平面的基本概念

考虑可用下列常微分方程描述的二阶时不变系统：

$$\ddot {x} = f (x, \dot {x}) \tag {8-15}$$

其中 $f(x, \dot{x})$ 是 $x(t)$ 和 $\dot{x}(t)$ 的线性或非线性函数。该方程的解可以用 $x(t)$ 的时间函数曲线表示，也可以用 $\dot{x}(t)$ 和 $x(t)$ 的关系曲线表示，而 $t$ 为参变量。 $x(t)$ 和 $\dot{x}(t)$ 称为系统运动的相变量（状态变量），以 $x(t)$ 为横坐标， $\dot{x}(t)$ 为纵坐标构成的直角坐标平面称为相平面。相变量从初始时刻 $t_0$ 对应的状态点 $(x_0, \dot{x}_0)$ 起，随着时间 $t$ 的推移，在相平面上运动形成的曲线称为相轨迹。在相轨迹上用箭头符号表示参变量时间 $t$ 的增加方向。根据微分方程解的存在与唯一性定理，对于任一给定的初始条件，相平面上有一条相轨迹与之对应。多个初始条件下的运动对应多条相轨迹，形成相轨迹簇，而由一簇相轨迹所组成的图形称为相平面图。

若已知 $x$ 和 $\dot{x}$ 的时间响应曲线如图8-10(b)，(c)所示，则可根据任一时间点的 $x(t)$ 和 $\dot{x}(t)$ 的值，得到相轨迹上对应的点，并由此获得一条相轨迹，如图8-10(a)所示。

相轨迹在某些特定情况下,也可以通过积分法,直接由微分方程获得 $\dot{x}(t)$ 和 $x(t)$ 的解析关系式。因为

$$\ddot {x} = \frac {\mathrm{d} \dot {x}}{\mathrm{d} t} = \frac {\mathrm{d} \dot {x}}{\mathrm{d} x} \cdot \frac {\mathrm{d} x}{\mathrm{d} t} = \dot {x} \frac {\mathrm{d} \dot {x}}{\mathrm{d} x}$$

由式(8-15)，有

$$\dot {x} \frac {\mathrm{d} \dot {x}}{\mathrm{d} x} = f (x, \dot {x}) \tag {8-16}$$

若该式可以分解为

$$g (\dot {x}) \mathrm{d} \dot {x} = h (x) \mathrm{d} x \tag {8-17}$$

![](image/2dee771f28e414e075945a19f15eea058548d7bf609b3e311c13b1d9cdaaadfa.jpg)

<details>
<summary>text_image</summary>

x̂
t₁
t₄
t₂
t₃
(a)
x̂
0
t₁
t₂
t₃
t₄
(c)
x
0
1
x
t₁
t₂
t₃
t₄
σₘ
(b)
</details>

图 8-10 $x(t)$ , $\dot{x}(t)$ 及其相轨迹曲线

两端积分

$$\int_ {\dot {x} _ {0}} ^ {\dot {x}} g (\dot {x}) \mathrm{d} \dot {x} = \int_ {x _ {0}} ^ {x} h (x) \mathrm{d} x \tag {8-18}$$

由此可得 $\dot{x}$ 和 $x$ 的解析关系式，其中 $x_0$ 和 $\dot{x}_0$ 为初始条件。

例 8-1 某弹簧-质量运动系统如图 8-11 所示, 图中 m 为物体的质量, k 为弹簧的弹性系数, 若初始条件为 $x(0)=x_{0}, \dot{x}(0)=\dot{x}_{0}$ , 试确定系统自由运动的相轨迹。

解 描述系统自由运动的微分方程式为

$$\ddot {x} + x = 0 \tag {8-19}$$

将上式写为

$$\dot {x} \frac {\mathrm{d} \dot {x}}{\mathrm{d} x} = - x$$

令 $g(\dot{x}) = \dot{x}, h(x) = -x$ ，则按式(8-18)，有

$$\int_ {\dot {x} _ {0}} ^ {\dot {x}} g (\dot {x}) \mathrm{d} \dot {x} = \int_ {\dot {x} _ {0}} ^ {\dot {x}} \dot {x} \mathrm{d} \dot {x} = \frac {1}{2} (\dot {x} ^ {2} - \dot {x} _ {0} ^ {2})\int_ {x _ {0}} ^ {x} h (x) \mathrm{d} x = \int_ {x _ {0}} ^ {x} - x \mathrm{d} x = - \frac {1}{2} (x ^ {2} - x _ {0} ^ {2})$$

![](image/59503121608d835a05268319b546e45198b62517c68cc6ca48da470cb2099728.jpg)

<details>
<summary>text_image</summary>

k=1
m=1
x
平衡位置
</details>

图 8-11 弹簧-质量运动系统

整理得

$$x ^ {2} + \dot {x} ^ {2} = (x _ {0} ^ {2} + \dot {x} _ {0} ^ {2}) \tag {8-20}$$

该系统自由运动的相轨迹为以坐标原点为圆心、 $\sqrt{x_{0}^{2}+\dot{x}_{0}^{2}}$ 为半径的圆，如图8-12所示。
