$$
\begin{array}{l} u \left(x _ {1}, x _ {2}, x _ {3}\right) = - r \operatorname{sign} \left(x _ {1} + s \left(s x _ {2} + \frac {x _ {3} ^ {2}}{2 r}\right) \right. \\ \left(\frac {1}{\sqrt {r}} \sqrt {s x _ {2} + \frac {x _ {3} ^ {2}}{2 r}} + s \frac {x _ {3}}{r}\right) - \frac {x _ {3} ^ {3}}{6 r ^ {2}} \tag {3.6.13} \\ \end{array}
$$

或

$$
\left\{ \begin{array}{l} s = \operatorname{sign} \left(x _ {2} + \frac {\left| x _ {3} \right| x _ {3}}{2 r}\right) \\ a = s x _ {2} + \frac {x _ {3} ^ {2}}{2 r} \\ b = \frac {x _ {3}}{r} \\ u \left(x _ {1}, x _ {2}, x _ {3}\right) = - r \operatorname{sign} \left(x _ {1} + s a \left(\sqrt {\frac {a}{r}} + s b\right) - \frac {r}{6} b ^ {3}\right) \end{array} \right. \tag {3.6.14}
$$

开关曲面在空间的形状和在 $x_{1}$ 轴向高度的等高线在 $(x_{2}, x_{3})$ 平面上的投影曲线如图3.6.1和图3.6.2所示.

![](image/aeed89e53ae488daeeaade7324204704ee3035f23969cf53e1e356a212ce9ca2.jpg)

<details>
<summary>text_image</summary>

3D surface plot with labeled axes and a shaded region, likely from a mathematical or engineering context
</details>

图3.6.1  
![](image/643cbfa72dd17b67d2be35827cf292ef0e640bc3c60668a77285fe1d7e14a593.jpg)

<details>
<summary>natural_image</summary>

Grayscale gradient image with diagonal lines and scattered bright spots, no text or symbols present
</details>

图3.6.2

利用这个最速控制反馈函数可以构造出同时提取信号 $v(t)$ 的一阶、二阶微分的跟踪微分器

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = x _ {3} \\ \dot {x} _ {3} = u (x _ {1} - v (t), x _ {2}, x _ {3}) \end{array} \right.
$$
