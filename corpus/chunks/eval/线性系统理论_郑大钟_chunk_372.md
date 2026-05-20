# 10.5 系统矩阵

系统矩阵 给定系统的多项式矩阵描述

$$
\left\{ \begin{array}{l} P (s) \hat {\zeta} (s) = Q (s) \hat {u} (s) \\ \hat {y} (s) = R (s) \hat {\zeta} (s) + W (s) \hat {u} (s) \end{array} \right. \tag {10.98}
$$

其中，各系数矩阵 $P(s), Q(s), R(s)$ 和 $W(s)$ 分别是 $m \times m, m \times p, q \times m$ 和 $q \times p$ 的。现将上述式(10.98)进一步表为增广变量方程的形式，有

$$
\left[ \begin{array}{l l} P (s) & Q (s) \\ - R (s) & W (s) \end{array} \right] \left[ \begin{array}{c} \hat {\xi} (s) \\ - \hat {u} (s) \end{array} \right] = \left[ \begin{array}{c} 0 \\ - \hat {y} (s) \end{array} \right] \tag {10.99}
$$

并且，称分块矩阵

$$
S (s) = \left[ \begin{array}{c c} P (s) & Q (s) \\ \underbrace {- R (s)} _ {m} & \underbrace {W (s)} _ {p} \end{array} \right] \} ^ {m} \tag {10.100}
$$

为它的系统矩阵。对于状态空间描述 $(A, B, C, E(p))$ ，其系统矩阵具有如下的形式：

$$
S (s) = \left[ \begin{array}{c c} s I - A & B \\ - C & E (s) \end{array} \right] \tag {10.101}
$$

而矩阵分式描述 $N(s)D^{-1}(s)$ 和 $D_{L}^{-1}(s)N_{L}(s)$ 的系统矩阵则为：

$$
S (s) = \left[ \begin{array}{c c} D (s) & I _ {p} \\ - N (s) & \mathbf {0} \end{array} \right] \quad \text {和} \quad S (s) = \left[ \begin{array}{c c} D _ {L} (s) & N _ {L} (s) \\ - I _ {q} & \mathbf {0} \end{array} \right] \tag {10.102}
$$

系统矩阵以集中的和简洁的形式表征了系统的所有结构性质。一旦系统矩阵 $S(s)$ 的具体形式给出，则通过判断是否存在使其前 $m$ 行和前 $m$ 列降秩的 $s$ 值，就可确定系统是否是不可简约的。如果已确认为是不可简约的，则由判断使左上方的 $m \times m$ 分块阵降秩的 $s$ 值和使整个 $S(s)$ 降秩的 $s$ 值，就可决定出系统的极点和传输零点。而当确认为是可简约时，那么由判断使前 $m$ 行和前 $m$ 列为降秩的 $s$ 值，而可定出系统的输入解耦零点和输出解耦零点。此外，引入系统矩阵，也为讨论同一类型的不同描述间的关系，以及不同类型描述间的关系，提供了方便。

增广系统矩阵 通常，对同一系统，其不同类型的描述的系统矩阵在维数上是不同的；即便是同一类型的不同描述，它们的系统矩阵也常常有着不同的维数。为了克服由此而引起的不便，可对系统矩阵(10.100)引入增广系统矩阵，其定义为：

$$
S _ {e} (s) = \left[ \begin{array}{c c} P _ {e} (s) & Q _ {e} (s) \\ - R _ {e} (s) & W (s) \end{array} \right] \triangleq \left[ \begin{array}{c c c} I _ {t} & 0 & 0 \\ 0 & P (s) & Q (s) \\ \hdashline 0 - R (s) & W (s) \end{array} \right] \tag {10.103}
$$

其中，正整数 $l$ 是可选择的。通过适当选取 $l$ 的数值，可做到使一个描述的增广系统矩阵和另一个描述的系统矩阵在维数上相等。

增广系统矩阵 $S_{e}(s)$ 和原来的系统矩阵 $S(s)$ 有着等同的特性，也即可以证明：

① $S_{\sigma}(s)$ 的不可简约等价于 $S(s)$ 的不可简约。  
② $\{P_{c}(s), Q_{c}(s)\}$ 的左互质等价于 $\{P(s), Q(s)\}$ 的左互质， $\{P_{c}(s), R_{c}(s)\}$ 的右互质等价于 $\{P(s), R(s)\}$ 的右互质。  
③ 当 $S_{c}(s)$ 和 $S(s)$ 为不可简约时，两者具有相同的极点和传输零点。  
④ 当 $S_{c}(s)$ 和 $S(s)$ 为可简约时，两者具有等同的输入解耦零点和输出解耦零点。  
⑤ $S_{c}(s)$ 和 $S(s)$ 具有等同的传递函数矩阵和等同的分母阵多项式，即

$$R _ {e} (s) P _ {e} ^ {- 1} (s) Q _ {e} (s) + W (s) = R (s) P ^ {- 1} (s) Q (s) + W (s) \tag {10.104}$$

和

$$\det P _ {e} (s) = \det P (s) \tag {10.105}$$

由此可见，引入增广系统矩阵并将其代替系统矩阵 $S(s)$ 来讨论不同描述间的关系，将不会损失特性上的等价性。
