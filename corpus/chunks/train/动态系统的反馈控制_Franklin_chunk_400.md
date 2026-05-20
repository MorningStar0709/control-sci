# 例 7.1 状态变量形式的卫星姿态控制模型

对例 2.3 中以状态变量形式描述的卫星姿态控制模型，试确定矩阵 A, B, C，和常数 D，其中 $M_{D}=0$ 。

解答。定义卫星姿态和角速度为状态变量，使得 $x \stackrel{\operatorname{def}}{=}[\theta - \omega]^{\mathrm{T} \ominus}$ 。则单个二阶方程（2.15）可以等价为 2 个一阶方程

$$\dot {\theta} = \omega\dot {\omega} = \frac {d}{I} F _ {\mathrm{c}}$$

437

利用式(7.3) $\dot{x}=Ax+Bu$ ，上述方程可以表示为

$$
\left[ \begin{array}{l} \dot {\theta} \\ \dot {\omega} \end{array} \right] = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{l} \theta \\ \omega \end{array} \right] + \left[ \begin{array}{l} 0 \\ d / I \end{array} \right] F _ {c}
$$

系统的输出是卫星的姿态， $y=\theta$ ，利用式(7.4)， $y=Cx+Du$ 此关系可以表示为

$$
y = \left[ \begin{array}{l l} 1 & 0 \end{array} \right] \left[ \begin{array}{l} \theta \\ \omega \end{array} \right]
$$

因此，状态变量形式的矩阵表示为

$$
\mathbf {A} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{l} 0 \\ d / I \end{array} \right], \quad \mathbf {C} = \left[ \begin{array}{l l} 1 & 0 \end{array} \right], \quad D = 0
$$

且输入为 $u \stackrel{\operatorname{def}}{=} F_{c}$ 。

对于这个非常简单的例子，微分方程的状态变量形式看起来比式(2.15)的二阶形式在写法上更加复杂。然而，对于大多数系统来说，这个方法并不复杂，并且标准形具有可以利用计算机辅助设计的优势，使得状态变量形式已经得到广泛的应用。

下面是一个更加复杂的例子，表明如何利用 Matlab 找到线性微分方程的解。
