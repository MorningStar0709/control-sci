其中 $n$ 为系统的维数。

从结论2出发，对单输入的线性定常离散系统，还可导出如下的一个有意义的推论。

推论 考虑单输入定常离散系统

$$\boldsymbol {x} (k + 1) = G \boldsymbol {x} (k) + h u (k), \quad k = 0, 1, 2, \dots \tag {3.123}$$

其中，x 为 n 维状态向量，u 为标量输入，G 假定为非奇异。则当系统为完全能控时，可

构造如下的控制

$$
\left[ \begin{array}{c} u (0) \\ u (1) \\ \vdots \\ u (n - 1) \end{array} \right] = - [ G ^ {- 1} h, G ^ {- 2} h, \dots , G ^ {- n} h ] ^ {- 1} x _ {0} \tag {3.124}
$$

使在 $n$ 步内将任意状态 $x(0) = x_0$ 转移到状态空间的原点。

证 由(3.123)可导出状态运动的表达式为:

$$
\begin{array}{l} x (n) = G ^ {n} x _ {0} + \left[ G ^ {n - 1} h u (0) + \dots + G h u (n - 2) + h u (n - 1) \right] \\ = G ^ {n} x _ {0} + G ^ {n} \left[ G ^ {- 1} h u (0) + \dots + G ^ {- (n - 1)} h u (n - 2) \right. \\ + G ^ {- n} h u (n - 1) ] \\ = G ^ {n} x _ {0} + G ^ {n} \left[ G ^ {- 1} h, \dots , G ^ {- n} h \right] \left[ \begin{array}{c} u (0) \\ \vdots \\ u (n - 1) \end{array} \right] \tag {3.125} \\ \end{array}
$$

再由系统为完全能控，以及

$$[ G ^ {n - 1} h, \dots , G h, h ] = G ^ {n} [ G ^ {- 1} h, \dots , G ^ {- n} h ] \tag {3.126}$$

又可推知

$$[ G ^ {- 1} h, G ^ {- 2} h, \dots , G ^ {- n} h ] \tag {3.127}$$

为非奇异，从而式(3.124)的控制是可构成的。这样，将(3.124)代入(3.125)，就即得到

$$
\begin{array}{l} x (n) = G ^ {n} x _ {0} - G ^ {n} \left[ G ^ {- 1} h, \dots , G ^ {- n} h \right] \left[ G ^ {- 1} h, \dots , G ^ {- n} h \right] ^ {- 1} x _ {0} \\ = G ^ {n} x _ {0} - G ^ {n} x _ {0} = 0 \tag {3.128} \\ \end{array}
$$

于是，推论得证。

能观测性及其判据 考虑时变离散系统

$$
\begin{array}{l} \boldsymbol {x} (k + 1) = G (k) \boldsymbol {x} (k) \\ (1) = G (1) (1) \end{array} \quad k \in J _ {k} \tag {3.129}
\mathbf {y} (k) = C (k) \mathbf {x} (k)
$$

如果对初始时刻 $h \in J_k$ 的任一非零初态 $\pmb{x}_0$ ，都存在有限时刻 $l \in J_k, l > h$ ，且可由 $[h, l]$ 上的输出 $\pmb{y}(k)$ 唯一地确定 $\pmb{x}_0$ ，则称系统在时刻 $h$ 是完全能观测的。

进一步,利用能控性和能观测性间的对偶关系,还可直接导出能观测性的判据和有关推论。

结论1[时变离散系统的格拉姆矩阵判据] 线性时变离散系统（3.129）在时刻 $h, h \in J_k$ ，为完全能观测的充分必要条件是，存在有限时刻 $l \in J_k, l > h$ ，使如下定义的格拉姆矩阵

$$W _ {o} [ h, l ] = \sum_ {k = h} ^ {l - 1} \Phi^ {T} (k + 1, h) C ^ {T} (k) C (k) \Phi (k + 1, h) \tag {3.130}$$

为非奇异。

结论2[定常离散系统的秩判据] 线性定常离散系统

$$
\begin{array}{l} x (k + 1) = G x (k), \quad k = 0, 1, 2, \dots \\ \mathbf {y} (k) = C \mathbf {x} (k) \tag {3.131} \\ \end{array}
$$

为完全能观测的充分必要条件是

$$
\operatorname{rank} \left[ \begin{array}{c} C \\ C G \\ \vdots \\ C G ^ {n - 1} \end{array} \right] = n \tag {3.132}
$$

或 $\operatorname{rank}[C^T | G^T C^T] \cdots |(G^T)^{n-1} C^T] = n$ (3.133)

推论 考虑单输出定常离散系统

$$\boldsymbol {x} (k + 1) = G \boldsymbol {x} (k), \quad k = 0, 1, 2, \dots \tag {3.134}y (k) = c x (k) \quad x (0) = x _ {0}$$

其中，x 为 n 维状态向量，y 为标量输出。则当系统为完全能观测时，可只利用 n 步内的输出值 $y(0)$ ， $y(1)$ ， $\cdots$ ， $y(n-1)$ 而构造出任意的非零初态 $x_{0}$ ：
