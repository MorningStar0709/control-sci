# 1.4 状态方程的对角线规范形和约当规范形

本节只限于讨论线性定常系统。线性定常系统的系统矩阵 A 的特征值是表征系统的动力学特性的一个重要参量。系统的状态方程将可通过适当的线性非奇异变换而化为由特征值表征的规范形。并且，当特征值为两两相异时，规范形具有对角线规范形的形式；而当特征值为非互异时，规范形将为约当规范形。在下一章中将可看到，这种以特征值表征的规范形状态方程，对于分析系统的结构特性是很直观的。

对角线规范形 给定系统的状态方程

$$\dot {x} = A x + B u \tag {1.53}$$

系统的特征值定义为如下特征方程

$$\det (\lambda I - A) = 0 \tag {1.54}$$

的根。一个阶数为 n 的系统，必有且仅有 n 个特征值，它们可为实数或以共轭对出现的复数。称一个非零列向量 $v_{i}$ 为矩阵 A 的属于特征值 $\lambda_{i}$ 的特征向量，如果成立 $(A - \lambda_{i}I)v_{i} = 0$ 。特征向量不是唯一的。但是，当 n 个特征值 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$ 为两两相异时，任取的 n个特征向量 $v_{1}, v_{2}, \cdots, v_{n}$ 必是线性无关的。利用这一事实，我们可导出如下的结论。

结论1 对系统(1.53)，设其特征值 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$ 为两两相异，并利用它们的特征向量组成变换阵 $P = [v_{1}, \cdots, v_{n}]$ ，那么系统的状态方程在变换 $\bar{x} = P^{-1}x$ 下必可化为如下的对角线规范形：

$$
\dot {\bar {x}} = \left[ \begin{array}{c c c c} \lambda_ {1} & & & \\ & \lambda_ {2} & & \\ & & \ddots & \\ & & & \lambda_ {n} \end{array} \right] \bar {x} + \bar {B} \alpha , \quad \bar {B} \triangleq P ^ {- 1} B \tag {1.55}
$$

证 由 $x = P^{-1}x$ ，可导出

$$\dot {\bar {x}} = P ^ {- 1} \dot {x} = P ^ {- 1} A P \bar {x} + P ^ {- 1} B u = \bar {A} \bar {x} + \bar {B} u \tag {1.56}$$

其中 $\overline{A}=P^{-1}AP_{0}$ 再由 $P=[v_{1},\cdots,v_{n}]$ 和 $\lambda_{i}v_{i}=Av_{i}$ ，可得到

$$
A P = \left[ A v _ {1}, \dots , A v _ {n} \right] = \left[ \lambda_ {1} v _ {1}, \dots , \lambda_ {n} v _ {n} \right]
= \left[ v _ {1}, \dots , v _ {n} \right] \left[ \begin{array}{c c c} \lambda_ {1} & & \\ & \ddots & \\ & & \lambda_ {n} \end{array} \right] = P \left[ \begin{array}{c c c} \lambda_ {1} & & \\ & \ddots & \\ & & \lambda_ {n} \end{array} \right] \tag {1.57}
$$

从而，将式（1.57）左乘 $P^{-1}$ ，即得

$$
\bar {A} = P ^ {- 1} A P = \left[ \begin{array}{c c c} \lambda_ {1} & & \\ & \ddots & \\ & & \lambda_ {n} \end{array} \right] \tag {1.58}
$$

把(1.58)代入(1.56)就可导出(1.55)。证明完成。

例 给定线性定常系统的状态方程为:

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c} 2 & - 1 & - 1 \\ 0 & - 1 & 0 \\ 0 & 2 & 1 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 7 \\ 2 \\ 3 \end{array} \right] \boldsymbol {u}
$$

其特征值为：

$$\lambda_ {1} = 2, \quad \lambda_ {2} = 1, \quad \lambda_ {3} = - 1$$

相应的一组特征向量为:

$$
\boldsymbol {v} _ {1} = \left[ \begin{array}{l} 1 \\ 0 \\ 0 \end{array} \right], \quad \boldsymbol {v} _ {2} = \left[ \begin{array}{l} 1 \\ 0 \\ 1 \end{array} \right], \quad \boldsymbol {v} _ {3} = \left[ \begin{array}{l} 0 \\ 1 \\ - 1 \end{array} \right]
$$

于是，可得到变换阵 $P$ 和其逆 $P^{-1}$ 为：
