# 10.3.2 最优化控制初探——LQR 控制器

![](image/b0f0a4a21acf9800ca807714aaa188eba14a983569b6bfd9b781c8655468feb2.jpg)

在设计反馈控制 K 的时候,如何选择闭环状态矩阵的特征值涉及最优化控制,从这点入手可以发展出一整个单独的学科和研究领域。本节将稍作试探,为读者介绍一个基础的最优化控制器——LQR 控制器。LQR 的全称为 Linear Quadratic Regulator,字面意义就是线性二次型调节器。

在式(10.3.7)和式(10.3.8)中,当使用线性状态反馈控制时,令 $u(t)=-Kz(t)$ ,可以得到闭环控制系统的状态空间方程,即

$$
\frac {\mathrm{d} \boldsymbol {z} (t)}{\mathrm{d} t} = (\boldsymbol {A} - \boldsymbol {B K}) \boldsymbol {z} (t) = \boldsymbol {A} _ {\mathrm{cl}} \boldsymbol {z} (t) \tag {10.3.14}
$$

此时通过设计不同的 K 值可以改变闭环状态矩阵 $A_{cl}$ 的特征值。在 10.3.1 节中选取了 $\lambda_{1,2} = -1$ ，这样做可以保证系统的稳定性。同时， $A_{cl}$ 特征值的不同将决定不同状态的收敛速度及输入的大小。为了更好地选择特征值，引入代价函数 (Cost Function)

$$
J = \int_ {0} ^ {\infty} z ^ {T} (t) Q z (t) + u ^ {T} (t) R u (t) d t \tag {10.3.15}
$$

控制器设计的目标是选择合适的 K，从而得到 $J_{\min}$ （代价函数 J 的最小值）。式(10.3.15)中，矩阵 Q 和矩阵 R 分别是状态变量和控制量（即动态系统的输入）的权重矩阵，都是正定的对称矩阵。一般情况下，Q 和 R 会选择为对角矩阵，且对角线上的元素都大于 0，即

$$
\boldsymbol {Q} _ {n \times n} = \left( \begin{array}{c c c c c} q _ {1} & & \dots & & 0 \\ & q _ {2} & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ & 0 & \dots & q _ {n - 1} \\ 0 & & \dots & & q _ {n} \end{array} \right), \quad \boldsymbol {R} _ {p \times p} = \left( \begin{array}{c c c c c} r _ {1} & & \dots & & 0 \\ & r _ {2} & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ & 0 & \dots & r _ {p - 1} \\ 0 & & \dots & & r _ {p} \end{array} \right) \tag {10.3.16}
$$

其中， $n$ 代表状态变量 $z(t)$ 的维度， $p$ 代表输入 $\pmb{u}(t)$ 的维度。通过设计不同的对角元素的值可以得到不同的代价函数。考虑一个例子：

$$
\frac {\mathrm{d} \boldsymbol {z} (t)}{\mathrm{d} t} = \boldsymbol {A} \boldsymbol {z} (t) + \boldsymbol {B}, \quad \text {其中,} \boldsymbol {A} = \left[ \begin{array}{c c} 0 & - 3 \\ - 1 & 2 \end{array} \right], \boldsymbol {B} = \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \tag {10.3.17}
$$

它是一个二状态单输入系统， $n = 2, p = 1$ ，所以 $\pmb{Q} = \begin{bmatrix} q_1 & 0 \\ 0 & q_2 \end{bmatrix}, \pmb{R} = r$ 。代入式(10.3.15)可得

$$
\begin{array}{l} J = \int_ {0} ^ {\infty} \left[ z _ {1} (t) - z _ {2} (t) \right] \left[ \begin{array}{c c} q _ {1} & 0 \\ 0 & q _ {2} \end{array} \right] \left[ \begin{array}{l} z _ {1} (t) \\ z _ {2} (t) \end{array} \right] + u (t) r u (t) d t \\ = \int_ {0} ^ {\infty} q _ {1} z _ {1} ^ {2} (t) + q _ {2} z _ {2} ^ {2} (t) + r u ^ {2} (t) \mathrm{d} t \tag {10.3.18} \\ \end{array}
$$
