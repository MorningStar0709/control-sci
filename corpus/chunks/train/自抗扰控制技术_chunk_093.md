下面考察这个快速最优控制综合函数的线性近似公式．为此先考查等时区 $G(2)$ 内的快速最优控制综合函数，详细分析见本节相关内容.

在这里快速最优控制综合函数的计算基本上是线性的,因此

线性近似的关键在于等时区 $G(2)$ 之外区域的函数值的近似.

在等时区 $G(2)$ 之外，图2.7.3中上面曲线上方是最优控制量取 $-r$ 的区域，而下面曲线的下方是最优控制量取 $+r$ 的区域，中间曲线是最优控制量取0，而上下两条曲线夹着的区域是最优控制量取开区间 $(-r, +r)$ 内值的区域。上、下、中间三条曲线的表达式分别为式(2.7.8）中的三个方程。

![](image/3b3136648c8fba09b91566c451844b3ed03176b351bb130e271db22d3b23686f.jpg)

<details>
<summary>line</summary>

| x | y (solid) | y (dashed) |
| --- | --- | --- |
| -0.8 | 0.8 | 0.6 |
| -0.6 | 0.7 | 0.5 |
| -0.4 | 0.6 | 0.4 |
| -0.2 | 0.5 | 0.3 |
| 0 | 0.4 | 0.2 |
| 0.2 | 0.3 | 0.1 |
| 0.4 | 0.2 | 0.0 |
| 0.6 | 0.1 | -0.1 |
| 0.8 | 0.0 | -0.2 |
| 1.0 | -0.1 | -0.3 |
</details>

图2.7.3

$$
\frac {h ^ {2} r ^ {2} - 8 r y s}{4} = \left\{ \begin{array}{l} \left(x _ {2} + s \frac {h r}{2} - s h r\right) ^ {2} = x _ {2} ^ {2} - s h r x _ {2} + \frac {h ^ {2} r ^ {2}}{4} \\ \left(x _ {2} + s \frac {h r}{2} + s h r\right) ^ {2} = x _ {2} ^ {2} + 3 s h r x _ {2} + \frac {9}{4} h ^ {2} r ^ {2} \\ \left(x _ {2} + s \frac {h r}{2}\right) ^ {2} = x _ {2} ^ {2} + s h r x _ {2} + \frac {h ^ {2} r ^ {2}}{4} \end{array} \right. \tag {2.7.25}

\frac {h ^ {2} r ^ {2} - 8 r \mathrm{ys}}{4} = \left\{ \begin{array}{l} x _ {2} ^ {2} - s h r x _ {2} + \frac {h ^ {2} r ^ {2}}{4} \\ x _ {3} ^ {2} + 3 s h r x _ {2} + \frac {9}{4} h ^ {2} r ^ {2} \\ x _ {2} ^ {2} + s h r x _ {2} + \frac {h ^ {2} r ^ {2}}{4} \end{array} \right. \tag {2.7.26}
$$

两边乘符号函数 $s$ 得

$$
\frac {s h ^ {2} r ^ {2} - 8 r y}{4} = \left\{ \begin{array}{l l} x _ {2} | x _ {2} | - h r x _ {2} + s \frac {h ^ {2} r ^ {2}}{4} \\ x _ {2} | x _ {2} | + 3 h r x _ {2} + s \frac {9}{4} h ^ {2} r ^ {2} \\ x _ {2} | x _ {2} | + h r x _ {2} + s \frac {h ^ {2} r ^ {2}}{4} \end{array} \right. \tag {2.7.27}
$$

由于 $y = x_{1} + hx_{2}$ ，两边除 $2r$ ，得

$$
0 = \left\{ \begin{array}{l} x _ {1} + \frac {x _ {2} | x _ {2} |}{2 r} + \frac {h}{2} x _ {2} \\ x _ {1} + \frac {x _ {2} | x _ {2} |}{2 r} + \frac {5}{2} h x _ {2} + s h ^ {2} r \\ x _ {1} + \frac {x _ {2} | x _ {2} |}{2 r} + \frac {3}{2} h x _ {2} \end{array} \right. \tag {2.7.28}
$$

根据上述推理, 可以给出快速最优控制综合函数的如下近似表达式

$$
\begin{array}{l} y = x _ {1} + h x _ {2} \\ z = x _ {2} + \frac {y}{h} \\ a = x _ {1} + \frac {h}{2} x _ {2} + \frac {\mid x _ {2} \mid x _ {2}}{2 r} \\ \text { if } (\mid z \mid \leqslant h r \text { and } \mid y \mid \leqslant h ^ {2} r) \\ \text { then } \\ u = - r \operatorname{sat} (z, h r) \\ \text { else } \\ u = - r \operatorname{sign} (a) \\ \text { endif } \end{array} \tag {2.7.29}
$$

或
