# 例 9-26 内模控制器

在许多实际场合,单纯的状态变量反馈方法并不是一种改善系统性能的实用方法。其主要原因是,状态变量反馈往往要求用具有无限带宽的 PD 控制器或 PID 控制器来实现,但实际部件和控制器都只有有限的带宽。

内模控制器是另一类校正控制器，能以零稳态误差渐近跟踪各类参考输入信号，如阶跃信号、斜坡信号及正弦信号等。众所周知，在经典控制理论中，对于阶跃输入信号，I型系统可以实现零稳态误差跟踪。如果在校正控制器中引入参考输入的内模，则可以在状态空间设计法中推广这一结论。采用类似的内模控制器方法，可以在更多的情况下实现零稳态误差跟踪。

设单输入-单输出系统的状态空间表达式为

$$\dot {\boldsymbol {x}} (t) = \boldsymbol {A} \boldsymbol {x} (t) + \boldsymbol {b} \boldsymbol {u} (t) \tag {9-268}y (t) = \mathbf {c x} (t)$$

式中， $x \in R^{n}$ 为状态向量；u 为标量输入；y 为标量输出；A, b 和 c 维数适当。

生成参考输入信号 $r(t)$ 的线性系统为

$$
\begin{array}{l} \dot {\boldsymbol {x}} _ {r} (t) = \mathbf {A} _ {r} \boldsymbol {x} _ {r} (t) \\ r (t) = \boldsymbol {d} _ {r} \boldsymbol {x} _ {r} (t) \tag {9-269} \\ \end{array}
$$

其中，初始条件未知。此外，参考输入信号 $r(t)$ 的生成系统也可以等效为

$$r ^ {(n)} (t) = \alpha_ {n - 1} r ^ {(n - 1)} (t) + \alpha_ {n - 2} r ^ {(n - 2)} (t) + \dots + \alpha_ {1} \dot {r} (t) + \alpha_ {0} r (t) \tag {9-270}$$

首先考虑参考输入 $r(t)$ 为单位阶跃信号时的内模控制器设计。此时， $r(t)$ 可由下列方程生成：

$$\dot {x} _ {r} (t) = 0, \quad r (t) = x _ {r} (t)$$

或等价为

$$\dot {r} (t) = 0$$

定义跟踪误差

$$e (t) = r (t) - y (t)$$

于是有

$$\dot {e} (t) = - \dot {y} (t) = - c \dot {x} (t) \tag {9-271}$$

现在，引入两个中间变量 $z(t)$ 和 $\pmb{w}(t)$ ，定义为

$$\mathbf {z} (t) = \dot {\mathbf {x}} (t), \quad w (t) = \dot {u} (t)$$

故有

$$
\begin{array}{l} \dot {z} (t) = \ddot {x} (t) = A \dot {x} (t) + b \dot {u} (t) \\ = \mathbf {A} \mathbf {z} (t) + \mathbf {b} \omega (t) \tag {9-272} \\ \end{array}
$$

则式(9-271)与式(9-272)构成如下增广系统方程：

$$
\left[ \begin{array}{l} \dot {e} \\ \dot {z} \end{array} \right] = \left[ \begin{array}{c c} 0 & - c \\ 0 & A \end{array} \right] \left[ \begin{array}{l} e \\ z \end{array} \right] + \left[ \begin{array}{l} 0 \\ b \end{array} \right] w \tag {9-273}
$$

当增广系统(9-273)可控时,即有

$$
\operatorname{rank} \left[ \begin{array}{c c c c c} 0 & - c b & - c A b & \dots & - c A ^ {n - 1} b \\ b & A b & A ^ {2} b & \dots & A ^ {n} b \end{array} \right] = n + 1 \tag {9-274}
$$

总可以找到反馈信号

$$w (t) = - k _ {1} e (t) - k _ {2} z (t) \tag {9-275}$$

使该系统渐近稳定。这表明跟踪误差 $e(t)$ 是渐近收敛的，因此系统输出能以零稳态误差跟踪参考输入信号。对式(9-275)求积分，可得系统内部的反馈控制信号为

$$u (t) = - k _ {1} \int_ {0} ^ {t} e (\tau) \mathrm{d} \tau - k _ {2} x (t) \tag {9-276}$$

与此对应的系统框图如图 9-29 所示。由图可见，在校正控制器中，除包含有状态变量反馈外，还包含了参考阶跃输入的内模（图中积分器环节），故称为内模控制器。

![](image/560b5d190efe3fabb113510a084dbb9e41f5952dbe29916214a56262f4c788c7.jpg)

<details>
<summary>flowchart</summary>
