$$
\begin{array}{l} \boldsymbol {x} (1) = G (0) \boldsymbol {x} _ {0} + H (0) \boldsymbol {u} (0) \\ \boldsymbol {x} (2) = G (1) G (0) \boldsymbol {x} _ {0} + G (1) H (0) \boldsymbol {u} (0) + H (1) \boldsymbol {u} (1) \\ \boldsymbol {x} (3) = G (2) G (1) G (0) \boldsymbol {x} _ {0} + G (2) G (1) H (0) \boldsymbol {u} (0) + G (2) H (1) \boldsymbol {u} (1) \\ + H (2) \boldsymbol {u} (2) \\ \end{array}
\bullet \quad \bullet \quad \bullet \quad \bullet \quad \bullet
\begin{array}{l} \boldsymbol {x} (k) = G (k - 1) \dots G (0) \boldsymbol {x} _ {0} + G (k - 1) \dots G (1) H (0) \boldsymbol {u} (0) \\ + G (k - 1) \dots G (2) H (1) u (1) + \dots + G (k - 1) H (k - 2) u (k - 2) \\ + H (k - 1) \boldsymbol {u} (k - 1) \tag {2.158} \\ \end{array}
$$

再知满足(2.157)的矩阵方程和初始条件的解阵为

$$\Phi (k, m) = G (k - 1) G (k - 2) \dots G (m) \tag {2.159}$$

于是，由（2.158）和（2.159）即可得到（2.155）或（2.156）。其中，和 $\pmb{u}$ 有关的项按由左至右顺序进行相加时导出(2.155)，而按由右至左顺序进行相加时导出(2.156)。从而，证明完成。

结论 2 对于由(2.150)所描述的线性定常离散系统,其状态运动的表达式为

$$x (k) = G ^ {k} x _ {0} + \sum_ {i = 0} ^ {k - 1} G ^ {k - i - 1} H u (i) \tag {2.160}$$

成

$$x (k) = G ^ {k} x _ {0} + \sum_ {i = 0} ^ {k - 1} G ^ {i} H u (k - i - 1) \tag {2.161}$$

证 对于定常情况,式(2.158)中可有

$$G (0) = G (1) = \dots = G (k - 1) = G \tag {2.162}$$

和

$$H (0) = H (1) = \dots = H (k - 1) = H \tag {2.163}$$

将(2.162)和(2.163)代入(2.158)，得到

$$
\begin{array}{l} x (k) = G ^ {k} x _ {0} + G ^ {k - 1} H u (0) + G ^ {k - 2} H u (1) + \dots \\ + G H \alpha (k - 2) + H \alpha (k - 1) \tag {2.164} \\ \end{array}
$$

于是，由此即可导出（2.160）或（2.161）。从而，证明完成。

结论3 令 $\Phi(k, m)$ 和 $\Phi(k - m)$ 分别为线性时变离散系统（2.149）和线性定常离散系统（2.150）的状态转移矩阵，即矩阵差分方程

$$\Phi (k + 1, m) = G (k) \Phi (k, m), \quad \Phi (m, m) = I \tag {2.165}$$

和

$$\Phi (k - m + 1) = G \Phi (k - m), \quad \Phi (0) = I \tag {2.166}$$

的解阵, 其中 $k = m, m + 1, \cdots$ 。则其表达式分别为:

$$\Phi (k, m) = G (k - 1) G (k - 2) \dots G (m) \tag {2.167}$$

和

$$\Phi (k - m) = G ^ {k - m} \tag {2.168}$$

其中， $G(m - 1)\triangle I,G^{0} = I_{0}$

证 采用迭代法, 即可由 (2.165) 导出

$$\Phi (m + 1, m) = G (m)\Phi (m + 2, m) = G (m + 1) G (m)\bullet \quad \bullet \quad \bullet \quad \bullet \quad \circ\Phi (k, m) = G (k - 1) G (k - 2) \dots G (m) \tag {2.169}$$

同理，由（2.166）则可导出

$$\Phi (k - m) = G G \dots G = G ^ {k - m} \tag {2.170}$$

于是，就完成了证明。

结论4 线性离散系统的状态转移矩阵的非奇异性依赖于系统矩阵 $G(k)$ ( $k=0, 1,2,\cdots$ ) 或 $G$ 的非奇异性。但是，对于连续系统的时间离散化系统，则其状态转移矩阵必是非奇异的。

证 结论的第一部分可由(2.167)或(2.168)直接导出。而由(2.138)或(2.144)，并注意到连续线性系统的状态转移矩阵必是非奇异的，即可导出结论的第二部分。

结论5 线性离散系统的运动也可分解为零输入响应和零状态响应两个部分，即
