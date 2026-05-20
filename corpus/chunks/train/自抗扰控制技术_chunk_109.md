# 3.3 最速反馈控制的不变性

下面将用变结构控制方法讨论具有直线滑动曲线的变结构控制和具有非线性滑动曲线的变结构控制在扰动抑制能力上的差异,然后指出最速控制综合函数形式的反馈控制所具有的特殊性质.

我们考察的被控对象为如下二阶系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = w + u \end{array} \right. \tag {3.3.1}
$$

式中，w 是对系统的所有扰动的总和，包括系统已建模动态、未建模动态（可称为系统的内扰）和所有外扰等作用的总和；u 是控制输入，可以取系统状态变量函数的反馈形式： $u = u(x_{1}, x_{2})$ .

今设

$$s = s \left(x _ {1}, x _ {2}\right) = 0, s (0, 0) = 0 \tag {3.3.2}$$

是把整个相平面分成 s > 0 和 s < 0 的两部分并且通过原点且位于二, 四象限的曲线.

对被控对象(3.3.1)取如下形式的反馈控制：

$$u = - r _ {1} \operatorname{sign} (s) \tag {3.3.3}$$

得闭环系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - r _ {1} \operatorname{sign} (s) + w \end{array} \right. \tag {3.3.4}
$$

先考察滑动曲线(3.3.2)为直线

$$s = x _ {1} + k x _ {2} \tag {3.3.5}$$

的情形(直线 s = 0 位于二, 四象限). 这时,

$$u = - r _ {1} \operatorname{sign} \left(x _ {1} + k x _ {2}\right) \tag {3.3.6}$$

的闭环系统(3.3.4)成为

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - r _ {1} \operatorname{sign} \left(x _ {1} + k x _ {2}\right) + w \end{array} \right. \tag {3.3.7}
$$

变结构控制系统到达滑动曲线 s = 0 的“到达条件”为

$$s \dot {s} < 0 \tag {3.3.8}$$

由于

$$
\begin{array}{l} \dot {s} = \frac {\partial s}{\partial x _ {1}} x _ {2} + \frac {\partial s}{\partial x _ {2}} (- r _ {1} \operatorname{sign} (s) + w) = \\ x _ {2} + k \left(- r _ {1} \operatorname{sign} (s) + w\right) \\ \end{array}
s \dot {s} = s x _ {2} - k s \left(r _ {1} \operatorname{sign} (s) - w\right) =\mid s \mid \left(\left(x _ {2} + k w\right) \operatorname{sign} (s) - k r _ {1}\right)
$$

欲使此式成为负,必须满足

$$\left(\frac {x _ {2}}{k} + w\right) \operatorname{sign} (s) < r _ {1} \tag {3.3.9}$$

如果假定 $w$ 是不确定扰动，满足限制条件 $\mid w\mid < r_2 < r_1$ ，那么当不等式

$$\left| \frac {x _ {2}}{k} \right| < r _ {1} - r _ {2} \tag {3.3.10}$$

成立时保证满足“到达条件”（式(3.3.8)），也就是说，在直线 $s = 0$ 上，不等式(3.3.10）所限定的线段 $L$ （如图3.3.1上连接点 $a, b$ 的线段）上的点是满足“到达条件”的.

由于闭环系统(3.3.7)的加速度的绝对值 $r$ 始终大于 $r_1 - r_2$ 线段 $L$ 邻近的轨线总是以有限时间到达 $L$ (图3.3.1).在 $L$ 上速的方向是按菲利波夫定义，是由 $L$ 两侧速度方向的凸组合，即 $\alpha [x_2, - r_1 + w] + (1 - \alpha)[x_2,r_1 + w] = [x_2,(1 - 2\alpha)r_1 + w]$ 与线段 $L$ 的相切条件 $x_{2} / k + (1 - 2\alpha)r_{1} + w = 0$ 来决定.于是线段 $L$ 上的运动方程变成

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - \frac {x _ {2}}{k} \end{array} \right.
$$

![](image/6750b9373f4433699820e3b63ec83aa947efe07b7756081eafe79f65fd6265d9.jpg)

<details>
<summary>contour</summary>
