# 6.1.1 微分器描述

韩京清 $^{[1]}$ 利用二阶最速开关系统构造出跟踪不连续输入信号并提取近似微分信号的机构，提出了非线性跟踪-微分器的概念。韩京清所提出的一种离散形式的非线性微分跟踪器在一些运动控制系统中得到了应用。离散形式的非线性微分跟踪器为

$$
\left\{ \begin{array}{l} r _ {1} (k + 1) = r _ {1} (k) + h r _ {2} (k) \\ r _ {2} (k + 1) = r _ {2} (k) + h \mathrm{fst} \left(r _ {1} (k) - v (k), r _ {2} (k), \delta , h\right) \end{array} \right. \tag {6.1}
$$

式中，h 为采样周期； $v(k)$ 为第 k 时刻的输入信号； $\delta$ 为决定跟踪快慢的参数。 $\mathrm{fst}(\cdot)$ 函数为最速控制综合函数，描述如下：

$$
\operatorname{fst} \left(x _ {1}, x _ {2}, \delta , h\right) = \left\{ \begin{array}{l l} - \delta \operatorname{sgn} (a) & | a | > d \\ - \delta \frac {a}{d} & | a | \leqslant d \end{array} \right.

a = \left\{ \begin{array}{l l} x _ {2} + \frac {a _ {0} - d}{2} \mathrm{sgn} (y) & | y | > d _ {0} \\ x _ {2} + y / h & | y | \leqslant d _ {0} \end{array} \right. \tag {6.2}
$$

式中， $d = \delta h$ ； $d_0 = hd$ ； $y = x_{1} + hx_{2}$ ； $a_0 = \sqrt{d^2 + 8\delta|y|}$ 。

输入信号为 $v(k)$ ，则采用微分器式（6.1），可实现 $r_{1}(k) \rightarrow v(k)$ ， $r_{2}(k) \rightarrow \dot{v}(k)$ 。并且如果 $v(k)$ 是带有噪声的信号，微分器可同时实现滤波。

![](image/62869fcbd76330fa3ab7ce239ce734734d59bbe06c75f8bc273f0721fc108649.jpg)
