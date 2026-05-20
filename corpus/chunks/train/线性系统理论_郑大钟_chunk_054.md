# 1.6 线性系统在坐标变换下的特性

坐标变换的基本含义, 是把系统在状态空间的一个坐标系上的表征, 化为另一个坐标系上的表征。事实上, 化状态方程为对角线规范形和约当规范形的变换, 就是一种特定的坐标变换。通过坐标变换, 可以突出系统的某些特性, 或者简化问题的分析计算。因此, 坐标变换是状态空间分析方法中应用很广的一种手段。

坐标变换的表征 坐标变换的实质是换基，即把状态空间的一个基底换成为另一个基底。设状态在基底 $\{e_{1}, e_{2}, \cdots, e_{n}\}$ 上的表征为

$$x = \left[ x _ {1}, x _ {2}, \dots , x _ {n} \right] ^ {T} \tag {1.102}$$

而其在另一个基底 $\{\bar{e}_{1},\bar{e}_{2},\cdots,\bar{e}_{n}\}$ 上的表征为

$$\bar {x} = \left[ \bar {x} _ {1}, \bar {x} _ {2}, \dots , \bar {x} _ {n} \right] ^ {T} \tag {1.103}$$

下面来给出 x 和 x 间的关系,也即坐标变换的代数表征。

考虑到 n 维状态空间中有且仅有 n 个线性无关的向量，而 $\{\bar{e}_{1},\bar{e}_{2},\cdots,\bar{e}_{n}\}$ 必是线性无关的，因此 $e_{1},e_{2},\cdots,e_{n}$ 均可表为 $\{\bar{e}_{1},\bar{e}_{2},\cdots,\bar{e}_{n}\}$ 的线性组合，且这种表示必是唯一的：

$$
\left\{ \begin{array}{l} e _ {1} = p _ {1 1} \bar {e} _ {1} + p _ {2 1} \bar {e} _ {2} + \dots + p _ {n 1} \bar {e} _ {n} \\ e _ {2} = p _ {1 2} \bar {e} _ {1} + p _ {2 2} \bar {e} _ {2} + \dots + p _ {n 2} \bar {e} _ {n} \\ \dots \dots \\ e _ {n} = p _ {1 n} \bar {e} _ {1} + p _ {2 n} \bar {e} _ {2} + \dots + p _ {n n} \bar {e} _ {n} \end{array} \right. \tag {1.104}
$$

表

$$
P = \left[ \begin{array}{c c c} p _ {1 1} & \dots & p _ {1 s} \\ \vdots & & \vdots \\ p _ {s 1} & \dots & p _ {s s} \end{array} \right] \tag {1.105}
$$

则还可将 $(1.104)$ 表示为：

$$\left[ e _ {1}, e _ {2}, \dots , e _ {n} \right] = \left[ \bar {e} _ {1}, \bar {e} _ {2}, \dots , \bar {e} _ {n} \right] P. \tag {1.106}$$

从而，可进一步导出

$$
\begin{array}{l} \left[ \bar {e} _ {1}, \bar {e} _ {2}, \dots , \bar {e} _ {n} \right] \left[ \begin{array}{c} \bar {x} _ {1} \\ \vdots \\ \bar {x} _ {n} \end{array} \right] = \left[ e _ {1}, e _ {2}, \dots , e _ {n} \right] \left[ \begin{array}{c} x _ {1} \\ \vdots \\ x _ {n} \end{array} \right] \\ - \left[ \bar {e} _ {1}, \bar {e} _ {2}, \dots , \bar {e} _ {s} \right] P \left[ \begin{array}{c} x _ {1} \\ \vdots \\ x _ {s} \end{array} \right] \tag {1.107} \\ \end{array}
$$

这表明,成立如下的关系式:

$$\bar {x} = P x \tag {1.108}$$

同理，也可导出

$$x - Q \bar {x} \tag {1.109}$$

于是，由（1.108）和（1.109）导出的关系式

$$
\left\{ \begin{array}{l} \bar {x} = P Q \bar {x} \\ x = Q P x \end{array} \right. \tag {1.110}
$$

即可得到

$$P Q = Q P - I \tag {1.111}$$

这说明 $Q = P^{-1}$ ，也即 $\pmb{x}$ 和 $\pmb{x}$ 之间为线性非奇异变换的关系。综上分析，可以得出结论：从代数上看，坐标变换就是一种线性非奇异变换，考察系统在坐标变换下的特性归结为研究其在线性非奇异变换下的基本属性。

系统状态空间描述在坐标变换下的特性

结论1 给定线性定常系统的状态空间描述为：

$$\Sigma : \dot {x} = A x + B u \tag {1.112}\mathbf {y} = C \mathbf {x} + D \mathbf {u}$$

引人变换 $\bar{x}=Px(\det P\neq0)$ ，并令变换后的状态空间描述为：
