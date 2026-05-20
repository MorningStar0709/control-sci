$$
\left[ \begin{array}{l} \hat {\boldsymbol {b}} _ {r 1 1} \\ \hat {\boldsymbol {b}} _ {r 1 2} \end{array} \right] \tag {3.50}
$$

为行线性无关。类似地，可对 $\lambda_{2}$ 推证而导出相应的结果。从而，论断(2)得证。于是，证明完成 $^{10}$ 。

例1 已知线性定常系统的对角线规范形为：

$$
\left[ \begin{array}{c} \dot {\bar {x}} _ {1} \\ \dot {\bar {x}} _ {2} \\ \dot {\bar {x}} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} - 7 & 0 & 0 \\ 0 & - 2 & 0 \\ 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{c} \bar {x} _ {1} \\ \bar {x} _ {2} \\ \bar {x} _ {3} \end{array} \right] + \left[ \begin{array}{c c} 0 & 2 \\ 4 & 0 \\ 0 & 1 \end{array} \right] u
$$

不难看出，此规范形中 $\bar{B}$ 不包含元素全为零的行，因此系统为完全能控。

例2 给定线性定常系统的约当规范形为:

$$
\dot {\hat {x}} = \left[ \begin{array}{c c} - 2 & 1 \\ 0 & - 2 \\ \hline & \end{array} \right] \left[ \begin{array}{c c c c} & & & \\ - 2 & & & \\ - 2 & & & \\ \hline & 3 & 1 \\ & 0 & 3 \\ \hline & & & 3 \end{array} \right] \hat {x} + \left[ \begin{array}{c c c} 0 & 0 & 0 \\ 1 & 0 & 0 \\ \hline 0 & 4 & 0 \\ \hline 0 & 0 & 7 \\ \hline 0 & 0 & 0 \\ 1 & 1 & 0 \\ \hline 0 & 4 & 1 \end{array} \right] u
$$

容易定出：

$$
\left[ \begin{array}{l} \hat {\boldsymbol {b}} _ {r 1 1} \\ \hat {\boldsymbol {b}} _ {r 1 2} \\ \hat {\boldsymbol {b}} _ {r 1 3} \end{array} \right] = \left[ \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 7 \end{array} \right] \quad \left[ \begin{array}{l} \hat {\boldsymbol {b}} _ {r 2 1} \\ \hat {\boldsymbol {b}} _ {r 2 2} \end{array} \right] = \left[ \begin{array}{l l l} 1 & 1 & 0 \\ 0 & 4 & 1 \end{array} \right]
$$

显然，它们都是行线性无关的，所以可知系统为完全能控。

能控性指数 考察完全能控的线性定常系统(3.7)，其中A和B分别是 $n \times n$ 和 $n \times p$ 的常值矩阵。定义

$$Q _ {k} = [ B \mid A B \mid A ^ {2} B \mid \dots \mid A ^ {k - 1} B ] \tag {3.51}$$

为 $n \times kp$ 常阵, 其中 $k$ 为正整数。显然, 因为系统为能控, 因此当 $k = n$ 时 $Q_{n}$ 即为能控性矩阵 $Q_{e}$ , 且 $\operatorname{rank} Q_{n} = n$ 。现在, 依次将 $k$ 由 1 增加, 直到使 $\operatorname{rank} Q_{\mu} = n$ 。那么, 便称这个使成立 $\operatorname{rank} Q_{k} = n$ 的 $k$ 的最小正整数 $\mu$ 为系统的能控性指数。

下面，我们来给出估计能控性指数 $\mu$ 的一个关系式。令 $\operatorname{rank} B = r \leqslant p$ ，则必成立

$$\frac {n}{p} \leqslant \mu \leqslant n - r + 1 \tag {3.52}$$

将可很容易证明此关系式：考虑到 $Q_{\mu}$ 为 $n \times \mu p$ 阵，所以欲使 $Q_{\mu}$ 的秩为 n，其必要的前提是矩阵 $Q_{\mu}$ 的列数必须大于或等于它的行数，也即应成立 $\mu p \geqslant n$ 。由此就导出了 (3.52) 的左不等式。再由 rank B = r，而 $AB, A^{2}B, \cdots, A^{\mu-1}B$ 的每一个矩阵由能控性指数定义知至少有一个列向量和 $Q_{\mu}$ 中其左侧所有线性独立的列向量线性无关，因此成立 $r + \mu - 1 \leqslant n$ 即 $\mu \leqslant n - r + 1$ 。于是，(3.52) 的右不等式得证。

进一步，从(3.52)出发，还可对能控性指数给出如下的几点推论。

① 对于单输入系统，也即 p = 1 时，系统的能控性指数为 $\mu = n_{0}$

② 对线性定常系统 (3.7)，可导出简化的能控性的秩判据为：系统完全能控的充分必要条件是
