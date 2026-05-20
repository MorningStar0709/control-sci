# 6.1 多变量系统的解耦控制

多输入－多输出系统的解耦控制方法无论是控制理论界还是控制工程界都是追求解决的重要问题．依靠系统模型的解决办法是有的，但是需要很大的计算量．用自抗扰控制技术来解决这个问题很简单，所需计算量也不大，特别是控制器的鲁棒性很好.

这一节将介绍自抗扰控制技术如何解决多变量控制系统的解耦控制问题.

设有多输入 - 多输出系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = f _ {1} \left(x _ {1}, \dot {x} _ {1}, \dots , x _ {\mathrm{m}}, \dot {x} _ {\mathrm{m}}\right) + b _ {1 1} u _ {1} + \dots + b _ {1 \mathrm{m}} u _ {\mathrm{m}} \\ \dot {x} _ {2} = f _ {2} \left(x _ {1}, \dot {x} _ {1}, \dots , x _ {\mathrm{m}}, \dot {x} _ {\mathrm{m}}\right) + b _ {2 1} u _ {1} + \dots + b _ {2 \mathrm{m}} u _ {\mathrm{m}} \\ \vdots \\ \ddot {x} _ {\mathrm{m}} = f _ {\mathrm{m}} \left(x _ {1}, \dot {x} _ {1}, \dots , x _ {\mathrm{m}}, \dot {x} _ {\mathrm{m}}\right) + b _ {\mathrm{m} 1} u _ {1} + \dots + b _ {\mathrm{mn}} u _ {\mathrm{m}} \\ y _ {1} = x _ {1}, y _ {2} = x _ {2}, \dots , y _ {\mathrm{m}} = x _ {\mathrm{m}} \end{array} \right. \tag {6.1.1}
$$

是 m 输入 - m 输出系统, 控制量的放大系数 $b_{ij}$ 是状态变量和时间的函数 $b_{ij}(x, \dot{x}, t)$ .

假定矩阵

$$
\boldsymbol {B} (x, \dot {x}, t) = \left[ \begin{array}{c c c} b _ {1 1} (x, \dot {x}, t) & \dots & b _ {1 m} (x, \dot {x}, t) \\ \vdots & \vdots & \vdots \\ b _ {m 1} (x, \dot {x}, t) & \dots & b _ {m n} (x, \dot {x}, t) \end{array} \right]
$$

可逆．在这里，我们把系统控制量之外的模型部分 $f(x_{1},x_{2},\cdots,x_{m})=[f_{1}f_{2}\cdots f_{m}]^{\mathrm{T}}$ 叫做“动态耦合”部分，而把 $U=B(x,\dot{x},t)u$ 部分叫做“静态耦合”部分.

记

$$\boldsymbol {x} = \left[ x _ {1} x _ {2} \dots x _ {m} \right] ^ {\mathrm{T}}, \boldsymbol {f} = \left[ f _ {1} f _ {2} \dots f _ {m} \right] ^ {\mathrm{T}}, u = \left[ u _ {1} u _ {2} \dots u _ {m} \right] ^ {\mathrm{T}}$$

并引入“虚拟控制量” $U = B(x, \dot{x}, t) u.$ 系统方程(6.1.1)变为

$$
\left\{ \begin{array}{l} \ddot {x} = f (x, \dot {x}, t) + U \\ y = x \end{array} \right. \tag {6.1.2}
$$

在这个系统中的第 i 通道的输入输出关系为

$$
\left\{ \begin{array}{l} \ddot {x} _ {i} = f _ {i} (x _ {1}, \dot {x} _ {1}, \dots , x _ {\mathrm{m}}, \dot {x} _ {\mathrm{m}}, t) + U _ {i} \\ y _ {i} = x _ {i} \end{array} \right. \tag {6.1.3}
$$

即第i通道上的输入为 $U_{i}$ ，而其输出为 $y_{i}=x_{i}$ 。这样每一个通道的虚拟控制量 $U_{i}$ 与被控输出 $y_{i}$ 之间是单输入－单输出关系，即第i通道的被控输出 $y_{i}$ 和“虚拟控制量” $U_{i}$ 之间已被完全解耦了，而 $f_{i}(x_{1},\dot{x}_{1},\cdots,x_{m},\dot{x}_{m},t)$ 则是作用于第i通道上的“扰动总和”，因此只要有被控量 $y_{i}$ 的目标值 $y_{i}^{*}(t)$ 且 $y_{i}$ 被测量，那么在 $U_{i}$ 和 $y_{i}$ 之间嵌入一个自抗扰控制器是完全能够让 $y_{i}$ 达到目标 $y_{i}^{*}(t)$ 。

这个过程的框图为图 6.1.1.
