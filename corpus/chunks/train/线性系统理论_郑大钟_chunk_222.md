$$
P \triangleq \left[ \begin{array}{l} C \\ R \end{array} \right] \tag {5.323}
$$

其中， $R$ 为 $(n - q) \times n$ 常阵且将其取为使 $P$ 为非奇异，所以 $R$ 是非唯一的和任意的。再计算 $P$ 的逆，并表其为分块阵

$$Q \triangleq P ^ {- 1} = [ Q _ {1} \mid Q _ {2} ] \tag {5.324}$$

其中， $Q_{1}$ 和 $Q_{2}$ 分别为 $n \times q$ 和 $n \times (n - q)$ 矩阵。并且，显然有

$$
\begin{array}{l} I _ {n} = P Q = \left[ \begin{array}{l} C \\ R \end{array} \right] \left[ \begin{array}{l l} Q _ {1} & Q _ {2} \end{array} \right] = \left[ \begin{array}{l l} C Q _ {1} & C Q _ {2} \\ R Q _ {1} & R Q _ {2} \end{array} \right] \\ = \left[ \begin{array}{c c} I _ {q} & 0 \\ 0 & I _ {n - q} \end{array} \right] \tag {5.325} \\ \end{array}
$$

也即成立

$$C Q _ {1} = I _ {q}, \quad C Q _ {2} = 0 \tag {5.326}$$

(2) 对被估计系统 (5.322)，引入线性非奇异变换 $\bar{x} = Px$ ，可导出：

$$
\begin{array}{l} \dot {\bar {x}} = P A P ^ {- 1} \bar {x} + P B u = \bar {A} \bar {x} + \bar {B} u \\ \mathbf {y} = C P ^ {- 1} \bar {\mathbf {x}} = \left[ \begin{array}{l l} C Q _ {1} & C Q _ {2} \end{array} \right] \bar {\mathbf {x}} = \left[ \begin{array}{l l} I _ {q} & 0 \end{array} \right] \bar {\mathbf {x}} \tag {5.327} \\ \end{array}
$$

现令 $\bar{x}_1$ 和 $\bar{x}_2$ 分别为 $q$ 和 $(n - q)$ 维分状态，则可把上式进一步表示为：

$$
\begin{array}{l} \left[ \begin{array}{l} \dot {\bar {x}} _ {1} \\ \dot {\bar {x}} _ {2} \end{array} \right] = \left[ \begin{array}{l l} \bar {A} _ {1 1} & \bar {A} _ {1 2} \\ \bar {A} _ {2 1} & \bar {A} _ {2 2} \end{array} \right] \left[ \begin{array}{l} \bar {x} _ {1} \\ \bar {x} _ {2} \end{array} \right] + \left[ \begin{array}{l} \bar {B} _ {1} \\ \bar {B} _ {2} \end{array} \right] u \\ \mathbf {y} = \left[ I _ {q} \quad 0 \right] \left[ \begin{array}{l} \bar {x} _ {1} \\ \bar {x} _ {2} \end{array} \right] = \bar {x} _ {1} \tag {5.328} \\ \end{array}
$$

其中， $\overline{A}_{11}, \overline{A}_{12}, \overline{A}_{21}$ 和 $\overline{A}_{22}$ 分别为 $q \times q, q \times (n - q), (n - q) \times q$ 和 $(n - q) \times (n - q)$ 矩阵， $\overline{B}_1$ 和 $\overline{B}_2$ 分别为 $q \times p$ 和 $(n - q) \times p$ 矩阵。并且，由(5.328)可看出，对变换后状态 $\bar{x}$ ，其分状态 $\bar{x}_1$ 即为系统的输出 $y$ ，故可直接利用而无需对其重构。这里所要重构的仅是 $\bar{x}$ 的 $(n - q)$ 维分状态 $\bar{x}_2$ ，故知仅需要采用 $(n - q)$ 维状态观测器就能达到重构的目的。

(3) 由 (5.328) 导出相对于 $\bar{x}_2$ 的状态方程和输出方程:

$$
\begin{array}{l} \dot {\bar {x}} _ {2} = \bar {A} _ {2 2} \bar {x} _ {2} + (\bar {A} _ {2 1} y + \bar {B} _ {2} u) \\ \therefore \quad \bar {x} _ {2 2} = \bar {y} _ {2 1} - \bar {z} _ {2 2} \end{array} \tag {5.329}
\dot {y} - \bar {A} _ {1 1} y - \bar {B} _ {1 u} = \bar {A} _ {1 2} \bar {x} _ {2}
$$
