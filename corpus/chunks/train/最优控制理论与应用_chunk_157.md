# 8.3 随机线性跟踪器问题

前面讨论的问题是使系统状态变量和输出量尽量控制到零,这种问题称为调节器问题(使输出量跟踪常值外作用的问题可归化为这种问题)。但在实际工作中有时要求系统的输出跟踪一个随时间变化的外作用,这种问题称为跟踪问题。制导系统和随动系统就可归入这类。

设系统的动态方程和量测方程为

$$
\left\{ \begin{array}{l} \boldsymbol {X} _ {k + 1} = \boldsymbol {\Phi} _ {k + 1, k} \boldsymbol {X} _ {k} + \boldsymbol {\Gamma} _ {k} \boldsymbol {U} _ {k} + \boldsymbol {W} _ {k} \\ \boldsymbol {Z} _ {k} = \boldsymbol {H} _ {k} \boldsymbol {X} _ {k} + \boldsymbol {V} _ {k} \end{array} \right.
$$

另有一个输出方程为

$$\boldsymbol {C} _ {k} = \boldsymbol {M} _ {k} \boldsymbol {X} _ {k} \tag {8-80}$$

$X_{k}$ 为 n 维, $U_{k}$ 为 m 维, $Z_{k}$ 为 q 维, $C_{k}$ 为 s 维。要求 $C_{k}$ 跟踪一个指令作用 $D_{k}$ 。

性能指标为

$$J = E \left\{\sum_ {k = 1} ^ {N} \boldsymbol {e} _ {k} ^ {\mathrm{T}} \overline {{{\boldsymbol {Q}}}} _ {k} \boldsymbol {e} _ {k} + \boldsymbol {U} _ {k - 1} ^ {\mathrm{T}} \overline {{{\boldsymbol {R}}}} _ {k - 1} \boldsymbol {U} _ {k - 1} \right\} \tag {8-81}$$

其中

$$\boldsymbol {e} _ {k} = \boldsymbol {D} _ {k} - \boldsymbol {C} _ {k} \tag {8-82}$$

是跟踪误差。

设指令作用 $D_{k}$ 由另一个系统(如被跟踪的敌机)生成, 其状态方程和量测方程为

$$
\left\{ \begin{array}{l l} \mathbf {Y} _ {k + 1} = \boldsymbol {\psi} _ {k + 1, k} \mathbf {Y} _ {k} + \mathbf {B} _ {k} \boldsymbol {\xi} _ {k} & (8 - 8 3) \\ \mathbf {D} _ {k} = \mathbf {N} _ {k} \mathbf {Y} _ {k} & (8 - 8 4) \end{array} \right.
$$

其中， $\xi_{k}$ 是白噪声。

一种基本的处理方法是引入增广状态向量

$$
\boldsymbol {X} _ {k} ^ {a} = \left[ \begin{array}{l} \boldsymbol {X} _ {k} \\ \boldsymbol {Y} _ {k} \end{array} \right] \tag {8-85}
$$

和增广噪声向量

$$
\boldsymbol {\xi} _ {k} ^ {a} = \left[ \begin{array}{l} \boldsymbol {W} _ {k} \\ \boldsymbol {\xi} _ {k} \end{array} \right] \tag {8-86}
$$

于是,关于 $X_{k}^{a}$ 的动态方程是

$$\boldsymbol {X} _ {k + 1} ^ {a} = \boldsymbol {\Phi} _ {k + 1, k} ^ {a} \boldsymbol {X} _ {k} + \boldsymbol {\Gamma} _ {k} ^ {a} \boldsymbol {U} _ {k} + \boldsymbol {B} _ {k} ^ {a} \boldsymbol {\xi} ^ {a} \tag {8-87}$$

其中

$$
\boldsymbol {\Phi} _ {k + 1, k} ^ {a} = \left[ \begin{array}{c c} \boldsymbol {\Phi} _ {k + 1, k} & \mathbf {0} \\ \mathbf {0} & \boldsymbol {\psi} _ {k + 1, k} \end{array} \right], \quad \boldsymbol {\Gamma} _ {k} ^ {a} = \left[ \begin{array}{l} \boldsymbol {\Gamma} _ {k} \\ \mathbf {0} \end{array} \right], \quad \boldsymbol {B} _ {k} ^ {a} = \left[ \begin{array}{c c} 1 & \mathbf {0} \\ \mathbf {0} & \boldsymbol {B} _ {k} \end{array} \right]
$$

新的输出方程为
