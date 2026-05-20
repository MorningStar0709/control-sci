$$u = \frac {x _ {1} + 2 h x _ {2}}{h ^ {2}} = \frac {x _ {2} + y / h}{h}, \left| x _ {2} + \frac {y}{h} \right| \leqslant h r, | y | \leqslant h ^ {2} r \tag {2.7.18}$$

这是等时区 $G(2)$ 之内的最优控制综合函数. 但是, 如果一个点的坐标 $(x_1, x_2)$ 满足 $|y| \leqslant h^2 r$ , 而 $|x_2 + y / h| > hr$ , 那么它位于两条平行线 $y = x_1 + hx_2 = \pm hr$ 之间, 但处于 $G(2)$ 之外, 即线段 $a_{-2}b_{-2}$ 的上方或线段 $a_{+2}b_{+2}$ 的下方. 当这种 $x_1, x_2$ 处于线段 $a_{-2}b_{-2}$ 的上方, 即 $x_2 + y / h > hr$ 时, 最优控制应该是 $u = -r$ , 而处于线段 $a_{+2}b_{+2}$ 的下方, 即 $x_2 + y / h < -hr$ 时, 最优控制应该取 $u = r$ , 即

$$
\begin{array}{l} u = - r \operatorname{sign} \left(x _ {2} + \frac {y}{h}\right) = - r \operatorname{sign} \left(\frac {x _ {2} + h y}{h}\right), \\ \left| x _ {2} + \frac {y}{h} \right| > h r, | y | \leqslant h ^ {2} r \tag {2.7.19} \\ \end{array}
$$

统一表达式(2.7.18)和式(2.7.19)，就得

$$u = - r \mathrm{sat} \left(\left(x _ {2} + \frac {y}{h}\right), h r\right), | y | \leqslant h ^ {2} r \tag {2.7.20}$$

根据以上分析,如果定义

$$
a \left(x _ {1}, x _ {2}, r, h\right) = \left\{ \begin{array}{c c} x _ {2} + \frac {\sqrt {h ^ {2} r ^ {2} + 8 r | y |} - h r}{2} \operatorname{sign} (y), & | y | > h ^ {2} r \\ x _ {2} + y / h, & | y | \leqslant h ^ {2} r \end{array} \right. \tag {2.7.21}
$$

那么由表达式(2.7.15)和式(2.7.20)就得离散系统(2.7.1)的快速最优控制综合函数表达式

$$u = - r \mathrm{sat} (a (x _ {1}, x _ {2}, r, h), h r) \tag {2.7.22}$$

这样,综合式(2.7.18) \~ 式(2.7.22),我们可以给出计算快速最优控制综合函数的如下具体算法:

$$
u = \operatorname{fhan} \left(x _ {1}, x _ {2}, r, h\right):
\left\{ \begin{array}{l} d = r h \\ d _ {0} = h d \\ y = x _ {1} + h x _ {2} \\ a _ {0} = \sqrt {d ^ {2} + 8 r | y |} \\ a = \left\{ \begin{array}{l l} x _ {2} + \frac {\left(a _ {0} - d\right)}{2} \operatorname{sign} (y), & | y | > d _ {0} \\ x _ {2} + \frac {\gamma}{h}, & | y | \leqslant d _ {0} \end{array} \right. \\ \text {fhan} = - \left\{ \begin{array}{l l} r \operatorname{sign} (a), & | a | > d \\ r \frac {a}{d}, & | a | \leqslant d \end{array} \right. \end{array} \right. \tag {2.7.23}
$$

或去掉条件语句,利用符号函数可改写成

$$
\left\{ \begin{array}{l} d = r h ^ {2}, a _ {0} = h x _ {2}, y = x _ {1} + a _ {0} \\ a _ {1} = \sqrt {d (d + 8 | y |)} \\ a _ {2} = a _ {0} + \operatorname{sign} (y) (a _ {1} - d) / 2 \\ s _ {y} = (\operatorname{sign} (y + d) - \operatorname{sign} (y - d)) / 2 \\ a = (a _ {0} + y - a _ {2}) s _ {y} + a _ {2} \\ s _ {a} = (\operatorname{sign} (a + d) - \operatorname{sign} (a - d)) / 2 \\ \text {fhan} = - r \left(\frac {a}{d} - \operatorname{sign} (a)\right) s _ {a} - r \operatorname{sign} (a) \end{array} \right. \tag {2.7.24}
$$

这就是我们常要用到的快速最优控制综合函数的离散形式.
