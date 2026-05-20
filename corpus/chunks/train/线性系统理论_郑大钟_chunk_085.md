$$
\begin{array}{l} \begin{array}{l} \boldsymbol {x} (k + 1) = G \boldsymbol {x} (k) + H \boldsymbol {u} (k), \quad \boldsymbol {x} (0) = \boldsymbol {x} _ {0} \\ \boldsymbol {v} (k) = G \boldsymbol {v} (k) + D \boldsymbol {v} (k), \quad k = 0, t = 0. \end{array} \tag {2.143} \\ \mathbf {y} (k) = C \mathbf {x} (k) + D \mathbf {u} (k), \quad k = 0, 1, 2, \dots \\ \end{array}
$$

其中，系数矩阵 $G$ 和 $H$ 为：

$$G = e ^ {A T}H = \left(\int_ {0} ^ {T} e ^ {A t} d t\right) B \tag {2.144}$$

证 考虑到定常系统是时变系统的一种特殊情况,因此由(2.137)即可导出(2.143),而由(2.138)则可导出:

$$G = \Phi ((k + 1) T - k T) = \Phi (T) = e ^ {A T} \tag {2.145}$$

和

$$H = \int_ {k T} ^ {(k + 1) T} \Phi ((k + 1) T - \tau) B d \tau \tag {2.146}$$

对上式作变量置换 $t=(k+1)T-\tau$ ，相应地有

$$d \tau = - d t, \quad \int_ {k T} ^ {(k + 1) T} \cdot d \tau = \int_ {T} ^ {0} \cdot d t \tag {2.147}$$

于是，利用（2.147）还可把（2.146）改写成为：

$$H = \left(- \int_ {T} ^ {0} \Phi (t) d t\right) B = \left(\int_ {0} ^ {T} e ^ {A t} d t\right) B \tag {2.148}$$

从而，(2.144) 得证。证明完成。

上述两个基本结论提供了线性连续系统时间离散化问题的算法。而且，由此还可导出两点推论。第一，时间离散化不改变系统的时变性或定常性，即时变连续系统离散化后仍为时变系统，而定常连续系统离散化后仍为定常系统。第二，考虑到连续系统的状态转移矩阵必是非奇异的，因此不管连续系统矩阵 $A(t)$ 或 $A$ 是否为非奇异，但离散化系统的矩阵 $G(k)$ 或 $G$ 将一定是非奇异的。

例 给定线性连续定常系统

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ 0 & - 2 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] u, \quad t \geqslant 0
$$

且采样周期为 T = 0.1 秒，要求建立其时间离散化模型。

首先，定出给定连续系统的矩阵指数函数 $e^{At}$ 。考虑到

$$
(s I - A) ^ {- 1} = \left[ \begin{array}{c c} s & - 1 \\ 0 & s + 2 \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} \frac {1}{s} & \frac {1}{s (s + 2)} \\ 0 & \frac {1}{(s + 2)} \end{array} \right]
$$

将其求拉普拉斯反变换，即得

$$
e ^ {A t} = \left[ \begin{array}{c c} 1 & 0. 5 (1 - e ^ {- 2 t}) \\ 0 & e ^ {- 2 t} \end{array} \right]
$$

再利用(2.144)，可进而定出：
