$$
\left\{ \begin{array}{l} \dot {x} _ {c} (t) = A _ {c} x _ {c} (t) + B _ {c} y (t), \\ u (t) = F _ {c} x _ {c} (t) + F _ {0} y (t), \end{array} \right. \tag {1.6.20}
$$

其中 $x_{c}(t)$ 为 $l$ 维状态， $A_{c}, B_{c}, F_{c}, F_{0}$ 分别为 $l \times l, l \times m, r \times l, r \times m$ 常值矩阵。这个控制规律是由一个动力学系统给出的，其输入是原来开环系统的量测输出，输出则正是所要求的原来开环系统的控制输入。这类反馈控制规律叫做动态输出反馈。把这种反馈控制规律作用于系统 (1.6.1) 得闭环系统为

$$
\left\{ \begin{array}{l} {\left[ \begin{array}{c} \dot {x} (t) \\ \dot {x} _ {c} (t) \end{array} \right] = \left[ \begin{array}{c c} A + B F _ {0} C & B F _ {c c} \\ B _ {c} C & A _ {c c} \end{array} \right] \left[ \begin{array}{c} x (t) \\ x _ {c c} (t) \end{array} \right],} \\ y (t) = [ C 0 ] \left[ \begin{array}{c} x (t) \\ x _ {c c} (t) \end{array} \right]. \end{array} \right. \tag {1.6.21}
$$

这时闭环系统的极点由矩阵

$$
\left[ \begin{array}{c c} \boldsymbol {A} + \boldsymbol {B} \boldsymbol {F} _ {0} \boldsymbol {C} & \boldsymbol {B} \boldsymbol {F} _ {c} \\ \boldsymbol {B} _ {c} \boldsymbol {C} & \boldsymbol {A} _ {c} \end{array} \right]
$$

的特征值决定.

显然，在动态输出反馈作用下，闭环系统比开环系统提高了 $l$ 阶，因而闭环系统的极点也增加了 $l$ 个．动态输出反馈规律(1.6.20)又叫做系统(1.6.1)的一个动态补偿器.

今后为叙述简单起见，把静态输出反馈简称为输出反馈，这不会与动态输出反馈相混淆.

用静态输出反馈一般不能任意移动系统极点，即不能任意极点配置。于是，人们想到用动态输出反馈做极点配置。

假设系统 (1.6.1) 是完全能控和完全能观测的，因此有

$$\operatorname{rank} Q _ {c} = n, \quad \operatorname{rank} Q _ {o} = n.$$

如果存在最小的正整数 $\mu_0$ 和 $\nu_0$ ，使得

$$
\operatorname{rank} \left[ \begin{array}{c c c c} B & A B & \dots & A ^ {\mu_ {0} - 1} B \end{array} \right] = n,

\operatorname{rank} \left[ \begin{array}{c} C \\ C A \\ \vdots \\ C A ^ {\nu_ {0} - 1} \end{array} \right] = n,
$$

那么分别称 $\mu_0$ 和 $\nu_0$ 为系统 (1.6.1) 的能控指数和能观测指数.

为了讨论用动态输出反馈做极点配置的问题，先介绍一个有用的引理.

引理 1.6.1 $^{[1.15]}$ 已知定常线性系统 (1.6.1). 假设 $(A, B)$ 能控, $(A, C)$ 能观测, 则存在 $r \times m$ 矩阵 H, 使得 $(A + BHC, B)$ 能控, $(A + BHC, C)$ 能观测, 并且 $A + BHC$ 是循环矩阵, 即它的最小多项式是 n 次的.

需要指出的是，给定矩阵 A, B, C 后，几乎所有的 $r \times m$ 矩阵都可以用作 H. 所以在某种意义上说，这样的 H 可以随便取.

本节的主要定理如下：

定理 1.6.3 已知定常线性系统 (1.6.1). 假设这个系统完全能控和完全能观测, 并且它的能观测指数为 $\nu_0$ , 那么对任给的含有 $n + \nu_0 - 1$ 个复数的对称集合 $\Lambda$ , 都存在一个动态输出反馈控制规律 (1.6.20), 使得闭环系统 (1.6.21) 的极点集合为 $\Lambda$ , 其中矩阵 $A_c, B_c, F_c$ 和 $F_0$ 分别是 $(\nu_0 - 1) \times (\nu_0 - 1)$ , $(\nu_0 - 1) \times m, r \times (\nu_0 - 1)$ 和 $r \times m$ 常值矩阵.

证明 要解决的问题实际上是，在定理的假设下，寻找矩阵 $A_{c}, B_{c}, F_{c}$ 和 $F_{0}$ ，使得

$$
\sigma \left(\left[ \begin{array}{c c} A + B F _ {0} C & B F _ {c} \\ B _ {c} C & A _ {c} \end{array} \right]\right) = \Lambda .
$$
