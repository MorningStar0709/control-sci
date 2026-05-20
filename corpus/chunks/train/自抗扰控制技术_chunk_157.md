# 4.6 一类混沌系统的扩张状态观测

混沌系统的运动虽然表现出“无序现象”，但其运动轨线始终在相空间中的有限区域里，即其状态变量是在有界范围内变化，因此这些状态变量变化的加速度变化范围是有界的。这就有可能用扩张状态观测器来跟踪其运动。

设有混沌系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = f _ {1} \left(x _ {1}, x _ {2}, x _ {3}\right) \\ \dot {x} _ {2} = f _ {2} \left(x _ {1}, x _ {2}, x _ {3}\right) \\ \dot {x} _ {3} = f _ {3} \left(x _ {1}, x _ {2}, x _ {3}\right) \\ y = x _ {1} \end{array} \right. \tag {4.6.1}
$$

假定其中的 $f_{1}(x_{1},x_{2},x_{3}),f_{2}(x_{1},x_{2},x_{3}),f_{3}(x_{1},x_{2},x_{3})$ 连续可微，系统能观测.记

$$g \left(x _ {1}, x _ {2}, x _ {3}\right) = \frac {\partial f _ {1}}{\partial x _ {1}} f _ {1} + \frac {\partial f _ {1}}{\partial x _ {2}} f _ {2} + \frac {\partial f _ {1}}{\partial x _ {3}} f _ {3}$$

对系统(4.6.1) 实现坐标变换

$$
\left\{ \begin{array}{l} y _ {1} = x _ {1} \\ y _ {2} = f _ {1} (x _ {1}, x _ {2}, x _ {3}) \\ y _ {3} = g (x _ {1}, x _ {2}, x _ {3}) \end{array} \right. \tag {4.6.2}
$$

就得

$$
\left\{ \begin{array}{l} \dot {y} _ {1} = y _ {2} \\ \dot {y} _ {2} = y _ {3} \\ \dot {y} _ {3} = \frac {\partial g}{\partial x _ {1}} f _ {1} + \frac {\partial g}{\partial x _ {2}} f _ {2} + \frac {\partial g}{\partial x _ {3}} f _ {3} \\ y = y _ {1} \end{array} \right. \tag {4.6.3}
$$

现在对这个系统用如下扩张状态观测器对状态和总和扰动进行估计.

如果对扩张状态观测器

$$
\left\{ \begin{array}{l} e = z _ {1} - y, \mathrm{fe} _ {1} = \operatorname{fal} (e, 0. 5, \delta), \mathrm{fe} _ {2} = \operatorname{fal} (e, 0. 2 5, \delta) \\ \dot {z} _ {1} = z _ {2} - \beta_ {0 1} e \\ \dot {z} _ {2} = z _ {3} - \beta_ {0 2} \mathrm{fe} _ {1} \\ \dot {z} _ {3} = - \beta_ {0 3} \mathrm{fe} _ {2} \end{array} \right. \tag {4.6.4}
$$

适当选取参数 $\beta_{01}, \beta_{02}, \beta_{03}$ ，就能有

$$z _ {1} \rightarrow y _ {1}, z _ {2} \rightarrow y _ {2}, z _ {3} \rightarrow y _ {3} \tag {4.6.5}$$

1. 针对 Lorenz 系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = \sigma (x _ {2} - x _ {1}) \\ \dot {x} _ {2} = \rho x _ {1} - x _ {2} - x _ {1} x _ {3} \\ \dot {x} _ {3} = - b x _ {3} + x _ {1} x _ {2} \\ y = x _ {1} \end{array} \right. \tag {4.6.6}
$$

式中， $\sigma=10,\rho=28,b=\frac{8}{3},x_{1}(0)=-4.47,x_{2}(0)=-0.505,$ $x_{3}(0)=28.02$ 时产生混沌现象(图4.6.1).

![](image/154a2182d2b88f87cc29448befa625d9be246dbd03024e6e8b3798032afa6199.jpg)

<details>
<summary>natural_image</summary>

3D surface plot with a black butterfly-like shape centered at origin, displayed in a Cartesian coordinate system (no text or labels)
</details>

图4.6.1

这里
