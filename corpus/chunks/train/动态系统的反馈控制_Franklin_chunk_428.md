$$\ddot {\xi} = - a _ {1} \ddot {\xi} - a _ {2} \dot {\xi} - a _ {3} \xi + u \tag {7.78}$$

则很容易画出与之对应的框图。累加和在图 7.14b 中体现出来，其中方程右边的每个 $\xi$ 是通过 $\xi$ 顺序积分得到的。为了求得输出，我们再回到图 7.14a 中，并注意到：

$$Y (s) = b (s) \xi (s) \tag {7.79}$$

这意味着，有

$$y = b _ {1} \ddot {\xi} + b _ {2} \dot {\xi} + b _ {3} \xi \tag {7.80}$$

我们再选取积分器的输出，将它们与 $\{b_{i}\}$ 中相应的元素相乘，并且利用一个加法器可以得到式(7.74)等号右边的输出式，如图7.14c所示。在这种情况下，所有反馈环都回到输入或者“控制”变量的施加点处，因此这种形式成了7.4.1小节所讨论过的能控标准形。通过信号流图的梅森规则或者基本的框图法，可以将该结构化简，结果表明，该系统图的传递函数即为 $G(s)$ 。

取已编号的三个积分器的输出作为状态，通常从左边起，即

$$x _ {1} = \ddot {\xi} _ {1}, x _ {2} = \dot {\xi}, x _ {3} = \xi \tag {7.81}$$

![](image/cd16397fe822df83b7d5de24eb37e3ee58cb75ae586e183fc248fa31d71180b9.jpg)  
图 7.14 能控标准形的推导

我们得到

$$\dot {x} _ {1} = \stackrel {\dots} {\xi} = - a _ {1} x _ {1} - a _ {2} x _ {2} - a _ {3} x _ {3} + u\dot {x} _ {2} = x _ {1}\dot {x} _ {3} = x _ {2} \tag {7.82}$$

现在，可以写出描述能控标准形的一般矩阵分别为

$$
\mathbf {A} _ {\mathrm{c}} = \left[ \begin{array}{c c c c c} - a _ {1} & - a _ {2} & \dots & \dots & - a _ {\mathrm{n}} \\ 1 & 0 & \dots & \dots & 0 \\ 0 & 1 & 0 & \dots & 0 \\ \vdots & & \ddots & & \vdots \\ 0 & 0 & \dots & 1 & 0 \end{array} \right], \quad \mathbf {B} _ {\mathrm{c}} = \left[ \begin{array}{c} 1 \\ 0 \\ 0 \\ \vdots \\ 0 \end{array} \right] \tag {7.83a}

\boldsymbol {C} _ {\mathrm{c}} = \left[ \begin{array}{l l l l l} b _ {1} & b _ {2} & \dots & \dots & b _ {n} \end{array} \right], \quad D _ {\mathrm{c}} = 0 \tag {7.83b}
$$

这个系统矩阵的特殊结构称为上相伴形，因为特征方程为

$$a (s) = s ^ {n} + a _ {1} s ^ {n - 1} + a _ {2} s ^ {n - 2} + \dots + a _ {n}$$

该项系数为1的“相伴形”多项式各项系数就是系统矩阵 $A_{c}$ 的第一行元素。如果计算闭环系统矩阵 $A_{c}-B_{c}K_{c}$ ，则可得

$$
\mathbf {A} _ {\mathrm{c}} - \mathbf {B} _ {\mathrm{c}} \mathbf {K} _ {\mathrm{c}} = \left[ \begin{array}{c c c c c} - a _ {1} - K _ {1} & - a _ {2} - K _ {2} & \dots & \dots & - a _ {n} - K _ {n} \\ 1 & 0 & \dots & \dots & 0 \\ 0 & 1 & 0 & \dots & 0 \\ \vdots & & \ddots & & \vdots \\ 0 & 0 & \dots & 1 & 0 \end{array} \right] \tag {7.84}
$$

通过直观地比较式(7.83a)和式(7.84)，可知闭环系统的特征方程为

$$s ^ {n} + \left(a _ {1} + K _ {1}\right) s ^ {n - 1} + \left(a _ {2} + K _ {2}\right) s ^ {n - 2} + \dots + \left(a _ {n} + K _ {n}\right) = 0 \tag {7.85}$$

因此，如果由期望极点位置能够得到如下特征方程：

$$\alpha_ {c} (s) = s ^ {n} + \alpha_ {1} s ^ {n - 1} + \alpha_ {2} s ^ {n - 2} + \dots + \alpha_ {n} = 0 \tag {7.86}$$

那么，所需反馈增益可以通过比较式(7.85)和式(7.86)二式的系数得到：

$$K _ {1} = - a _ {1} + \alpha_ {1}, \quad K _ {2} = - a _ {2} + \alpha_ {2}, \dots , K _ {n} = - a _ {n} + \alpha_ {n} \tag {7.87}$$
