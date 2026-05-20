# 3.2.2 特征值与特征向量的应用——线性方程组解耦

特征值与特征向量的一个重要应用是将矩阵转化成对角矩阵,从而达到解耦(Decouple)的效果。解耦即解除耦合,而耦合是指一个系统里面的两个或以上的状态变量存在相互影响、相互关联的作用。考虑一个包含两个状态变量的系统,它的微分方程组为

$$
\left\{ \begin{array}{l} \frac {\mathrm{d} z _ {1} (t)}{\mathrm{d} t} = z _ {1} (t) + z _ {2} (t) \\ \frac {\mathrm{d} z _ {2} (t)}{\mathrm{d} t} = 4 z _ {1} (t) - 2 z _ {2} (t) \end{array} \right. \tag {3.2.14}
$$

式(3.2.14)说明,系统状态变量 $z_{1}(t)$ 的变化率 $\frac{\mathrm{d}z_{1}(t)}{\mathrm{d}t}$ 除了与自身相关之外,还与 $z_{2}(t)$ 相关。而 $z_{2}(t)$ 的变化率 $\frac{\mathrm{d}z_{2}(t)}{\mathrm{d}t}$ 同时是 $z_{2}(t)$ 和 $z_{1}(t)$ 的函数,这样的两个状态变量就是耦合的。对于耦合系统,分析单个状态变量的变化需要同时考虑两个变量,这是不容易做到的。将上述系统写成紧凑的状态空间方程,得到

$$\frac {\mathrm{d} z (t)}{\mathrm{d} t} = A z (t) \tag {3.2.15}$$

其中

$$
\mathbf {A} = \left[ \begin{array}{c c} 1 & 1 \\ 4 & - 2 \end{array} \right]
$$

若要解耦这个系统,首先需要定义过渡矩阵(Transition Matrix):

$$
\boldsymbol {P} = \left[ \boldsymbol {v} _ {1}, \boldsymbol {v} _ {2} \right] = \left[ \begin{array}{l l} v _ {1 1} & v _ {2 1} \\ v _ {1 2} & v _ {2 2} \end{array} \right] \tag {3.2.16}
$$

其中， $v_{1}$ 、 $v_{2}$ 是矩阵A所对应的两个特征向量。用矩阵A左乘以过渡矩阵，可得

$$
\boldsymbol {A} \boldsymbol {P} = \boldsymbol {A} \left[ \begin{array}{l l} v _ {1 1} & v _ {2 1} \\ v _ {1 2} & v _ {2 2} \end{array} \right] = \left[ \boldsymbol {A} \left[ \begin{array}{l} v _ {1 1} \\ v _ {1 2} \end{array} \right] \boldsymbol {A} \left[ \begin{array}{l} v _ {2 1} \\ v _ {2 2} \end{array} \right] \right] \tag {3.2.17}
$$

因为 $\begin{bmatrix} v_{11}\\ v_{12} \end{bmatrix}$ 和 $\begin{bmatrix} v_{21}\\ v_{22} \end{bmatrix}$ 是矩阵 $\mathbf{A}$ 的特征向量，所以 $\mathbf{A}\left[ \begin{array}{c}v_{11}\\ v_{12} \end{array} \right] = \lambda_1\left[ \begin{array}{c}v_{11}\\ v_{12} \end{array} \right],\mathbf{A}\left[ \begin{array}{c}v_{21}\\ v_{22} \end{array} \right] = \lambda_2\left[ \begin{array}{c}v_{21}\\ v_{22} \end{array} \right],$

其中， $\lambda_{1}$ 和 $\lambda_{2}$ 是特征向量 $v_{1}$ 和 $v_{2}$ 所对应的特征值。式(3.2.17)可以写成
