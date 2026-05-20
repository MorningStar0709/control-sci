# 3.3 线性连续时间系统的能观测性判据

能观测性概念是对偶于能控性的。在讨论能观测性问题时通常总是考虑输入 $\pmb{u} = \pmb{0}$ 的情况。下面，分别就线性定常系统和线性时变系统，来介绍判别能观测性的一些常用判据。并且，由于许多讨论和论证都和上一节中对能控性的分析相类同，所以除了个别结论外，大多数的结果都将只给出结论而不再提供证明过程。

线性定常系统的能观测性判据 考虑输入 u = 0 时系统的状态方程和输出方程

$$\dot {x} = A x, x (0) = x _ {0}, t \geqslant 0 \tag {3.75}y = C x$$

其中，x 为 n 维状态向量，y 为 q 维输出向量，A 和 C 分别为 $n \times n$ 和 $q \times n$ 的常值矩阵。

结论1[格拉姆矩阵判据] 线性定常系统（3.75）为完全能观测的充分必要条件是，存在有限时刻 $t_1 > 0$ ，使如下定义的格拉姆矩阵

$$W _ {o} [ 0, t _ {1} ] \triangleq \int_ {0} ^ {t _ {1}} e ^ {A T _ {t}} C ^ {T} C e ^ {A t} d t \tag {3.76}$$

为非奇异。

证 充分性：已知 $W_{o}[0, t_{1}]$ 非奇异，欲证系统为完全能观测。

采用构造性方法来证明。 $W_{\bullet}$ 非奇异意味着 $W_{\bullet}^{-1}$ 存在，故可对 $[0, t_{1}]$ 上已知的输出 $y(t)$ 来构造：

$$
\begin{array}{l} W _ {e} ^ {- 1} [ 0, t _ {1} ] \int_ {0} ^ {t _ {1}} e ^ {A T t} C ^ {T} y (t) d t = W _ {e} ^ {- 1} [ 0, t _ {1} ] \int_ {0} ^ {t _ {1}} e ^ {A T t} C ^ {T} C e ^ {A t} d t x _ {0} \\ = W _ {o} ^ {- 1} \left[ 0, t _ {1} \right] W _ {o} \left[ 0, t _ {1} \right] x _ {0} = x _ {0} \tag {3.77} \\ \end{array}
$$

这表明，在 $W_{0}[0, t_{1}]$ 非奇异的条件下，总是可以根据 $[0, t_{1}]$ 上的输出 $y(t)$ 来构造出任意的非零初态 $x_{0}$ 的。因此，系统为完全能观测，充分性得证。

必要性：系统完全能观测，欲证 $W_{o}[0,t_{1}]$ 非奇异。

采用反证法。反设 $W$ 。奇异，也即反设存在某个非零 $\bar{x}_0 \in \mathcal{R}^n$ ，使成立

$$
\begin{array}{l} 0 = \bar {x} _ {0} ^ {T} W _ {\bullet} [ 0, t _ {1} ] \bar {x} _ {0} = \int_ {0} ^ {t _ {1}} \bar {x} _ {0} ^ {T} e ^ {A T t} C ^ {T} C e ^ {A t} \bar {x} _ {0} d t \\ - \int_ {0} ^ {t _ {1}} y ^ {T} (t) y (t) d t = \int_ {0} ^ {t} \| y (t) \| ^ {2} d t \tag {3.78} \\ \end{array}
$$

而这又意味着

$$\mathcal {Y} (t) = C e ^ {\lambda t} \bar {x} _ {0} \equiv 0, \forall t \in [ 0, t _ {1} ] \tag {3.79}$$

按定义知， $x_{0}$ 为状态空间中的不能观测状态。这和已知系统完全能观测相矛盾，所以反设不成立，必要性得证。从而，证明完成。

由于格拉姆矩阵判据中要用到矩阵指数函数 $e^{At}$ ，而这对维数较大的系统常需要较为复杂的计算。因此，此判据主要用于理论分析中。

结论 2 [秩判据] 线性定常系统 (3.75) 为完全能观测的充分必要条件是

$$
\operatorname{rank} \left[ \begin{array}{c} C \\ C A \\ \vdots \\ C A ^ {n - 1} \end{array} \right] = n \tag {3.80}
$$

或

$$\operatorname{rank} \left[ C ^ {T} \mid A ^ {T} C ^ {T} \mid \dots \mid (A ^ {T}) ^ {n - 1} C ^ {T} \right] = n \tag {3.81}$$

其中， $Q_{o}\triangleq[C^{T}|A^{T}C^{T}|\cdots|(A^{T})^{n-1}C^{T}]^{T}$ 称为系统的能观测性判别阵。

例1 考虑3.1节中给出的例1, 其输入 $u = 0$ 时的状态方程和输出方程为:

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c} 4 & 0 \\ 0 & - 5 \end{array} \right] \boldsymbol {x}, \quad n = 2
y = [ 0 \quad - 6 ] x
$$

通过计算可得

$$
Q _ {o} = \left[ \begin{array}{l} C \\ C A \end{array} \right] = \left[ \begin{array}{l l} 0 & - 6 \\ 0 & 3 0 \end{array} \right]
$$

容易断定，rank $Q_{o} = 1 < n = 2$ 。因此，系统为不完全能观测。
