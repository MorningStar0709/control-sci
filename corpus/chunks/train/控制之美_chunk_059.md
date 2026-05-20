将 $\mathbf{A} = \begin{bmatrix} 1 & 1 \\ 4 & -2 \end{bmatrix}$ 代入式(3.2.7)，可得

$$
\left| \begin{array}{c c} 1 - \lambda & 1 \\ 4 & - 2 - \lambda \end{array} \right| = 0 \tag {3.2.8a}
$$

即

$$(1 - \lambda) (- 2 - \lambda) - 1 \times 4 = 0\Rightarrow \lambda^ {2} + \lambda - 6 = 0 \tag {3.2.8b}$$

式(3.2.8b)称为矩阵 A 的特征方程(Characteristic Equation)。可以得到矩阵 A 的两个特征值：

$$
\left. \begin{array}{l} \lambda_ {1} = 2 \\ \lambda_ {2} = - 3 \end{array} \right\} \tag {3.2.9}
$$

将式(3.2.9)代入式(3.2.6)即可得到不同特征值所对应的特征向量。例如当 $\lambda_{1} = 2$ 时，对应的特征向量为 $v_{1} = [v_{11}, v_{12}]^{\mathrm{T}}$ ，根据式(3.2.6)，可得

$$
\left(\boldsymbol {A} - \lambda_ {1} \boldsymbol {I}\right) \boldsymbol {v} _ {1} = \left[ \begin{array}{c c} 1 - 2 & 1 \\ 4 & - 2 - 2 \end{array} \right] \left[ \begin{array}{l} v _ {1 1} \\ v _ {1 2} \end{array} \right] = \left[ \begin{array}{c c} - 1 & 1 \\ 4 & - 4 \end{array} \right] \left[ \begin{array}{l} v _ {1 1} \\ v _ {1 2} \end{array} \right] = 0

\Rightarrow \left\{ \begin{array}{l} - v _ {1 1} + v _ {1 2} = 0 \\ 4 v _ {1 1} - 4 v _ {1 2} = 0 \end{array} \right.
\Rightarrow v _ {1 1} = v _ {1 2} \tag {3.2.10}
$$

式(3.2.10)说明特征向量 $v_{1}$ 存在于 $v_{11}=v_{12}$ 这一条直线上。可以任意取其中的一组，例如选取 $v_{11}=v_{12}=1$ ，那么矩阵A对应于特征值 $\lambda_{1}=2$ 的特征向量为

$$
\boldsymbol {v} _ {1} = \left[ \begin{array}{l} v _ {1 1} \\ v _ {1 2} \end{array} \right] = \left[ \begin{array}{l} 1 \\ 1 \end{array} \right] \tag {3.2.11}
$$

$v_{1}$ 通过矩阵 A 的线性变换后得到 $Av_{1}=[2,2]^{T}=2v_{1}$ ，如图 3.2.1(b) 所示。

同理，可以计算 $v_{2}$ ，即特征值 $\lambda_2 = -3$ 时的特征向量，可得

$$
\left(\boldsymbol {A} - \lambda_ {2} \boldsymbol {I}\right) \boldsymbol {v} _ {2} = \left[ \begin{array}{c c} 1 + 3 & 1 \\ 4 & - 2 + 3 \end{array} \right] \left[ \begin{array}{l} v _ {2 1} \\ v _ {2 2} \end{array} \right] = \left[ \begin{array}{l l} 4 & 1 \\ 4 & 1 \end{array} \right] \left[ \begin{array}{l} v _ {2 1} \\ v _ {2 2} \end{array} \right] = 0

\left\{ \begin{array}{l} 4 v _ {2 1} + v _ {2 2} = 0 \\ 4 v _ {2 1} + v _ {2 2} = 0 \end{array} \right.
\Rightarrow v _ {2 1} = - \frac {1}{4} v _ {2 2} \tag {3.2.12}
$$

选取 $v_{21}=0.5, v_{22}=-2$ 。那么，矩阵 A 对应于特征值 $\lambda_{2}=-3$ 的特征向量为

$$
\boldsymbol {v} _ {2} = \left[ \begin{array}{l} v _ {2 1} \\ v _ {2 2} \end{array} \right] = \left[ \begin{array}{c} 0. 5 \\ - 2 \end{array} \right] \tag {3.2.13}
$$

此时， $Av_{2}=\begin{bmatrix}1&1\\ 4&-2\end{bmatrix}\begin{bmatrix}0.5\\ -2\end{bmatrix}=\begin{bmatrix}-1.5\\ 6\end{bmatrix}=-3v_{2}$ 。
