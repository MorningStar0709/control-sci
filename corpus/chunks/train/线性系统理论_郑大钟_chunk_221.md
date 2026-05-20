现将上述方程中，第一个方程乘以 $\alpha_0$ ，第二个方程乘以 $\alpha_{1}$ ，依此类推，最后一个方程乘以1，然后把所得结果相加。由此，再经化简和整理，可得到：

$$
T a (A) - a (F) T = [ G F G \dots F ^ {n - 1} G ] \left[ \begin{array}{c c c c} \alpha_ {1} I _ {q} & \alpha_ {2} I _ {q} \dots \alpha_ {n - 1} I _ {q} & I _ {q} \\ \alpha_ {2} I _ {q} & \alpha_ {3} I _ {q} \dots & I _ {q} & 0 \\ \vdots & \vdots & \vdots & \vdots \\ \alpha_ {n - 1} I _ {q} & I _ {q} \dots & 0 & 0 \\ I _ {q} & 0 \dots & 0 & 0 \end{array} \right]

\cdot \left[ \begin{array}{c} C \\ C A \\ \vdots \\ C A ^ {n - 2} \\ C A ^ {n - 1} \end{array} \right] \triangleq U _ {F} \Lambda_ {q} V _ {A} \tag {5.320}
$$

其中， $U_{F}$ 为 $\{F, G\}$ 的能控性判别阵， $V_{A}$ 为 $\{A, C\}$ 的能观测性判别阵，而 $A_{q}$ 为 $nq \times nq$ 矩阵。但是，前已证得， $a(A) = 0$ ， $a(F)$ 为非奇异矩阵。所以由 (5.320) 还可导出：

$$T = - [ \alpha (F) ] ^ {- 1} U _ {F} \Lambda_ {q} V _ {A} \tag {5.321}$$

由此可见，若 $\operatorname{rank} U_P < n$ 或 $\operatorname{rank} V_A < n$ ，则必有 $\operatorname{rank} T < n$ 。因此， $\operatorname{rank} T = n$ 的必要条件是 $\operatorname{rank} U_P = n$ 和 $\operatorname{rank} V_A = n$ ，也即 $T$ 为非奇异的必要条件是 $\{F, G\}$ 为能控和 $\{A, C\}$ 为能观测。然而， $\operatorname{rank} U_P = n$ 和 $\operatorname{rank} V_A = n$ 并不能导出 $T$ 为非奇异，故它们不是充分条件。

再来考虑 $q = 1$ 的情况。此时， $U_{F}$ 和 $V_{A}$ 均变为 $n \times n$ 方阵，而 $\Lambda_{q}$ 为 $n \times n$ 非奇异阵。于是，此种情况下，由(5.321)即可导出， $T$ 为非奇异的充分必要条件是 $\operatorname{rank} U_{F} = n$ 和 $\operatorname{rank} V_{A} = n$ ，也即 $\{F, G\}$ 能控和 $\{A, C\}$ 能观测。至此，证明完成。

在上述结论的基础上，就可给出设计全维状态观测器(5.313)的算法。

算法 给定被估计系统 $\{A, B, C\}$ ，其中 $\{A, B\}$ 能控和 $\{A, C\}$ 能观测，则全维观测器的设计步骤为：

第1步：选取 $n \times n$ 矩阵 $F$ ，使其全部特征值均具有负实部，且 $\lambda_i(F) \neq \lambda_i(A), i, = 1, 2, \cdots, n$ 。

第2步：选取 $n \times q$ 矩阵 $G$ ，使 $\{F, G\}$ 为能控。

第3步：求解矩阵方程 $TA - FT = GC^{1)}$ ，定出其唯一解阵 $T$ 。

第 4 步：如果 T 为非奇异，计算 H = TB，且所要设计的全维观测器就为：

$$\dot {z} = F z + G y + H u$$

而估计状态 $\hat{\pmb{x}} = T^{-1}\pmb{z}$ ; 若 $T$ 为奇异, 则需重新选取 $F$ 或/和 $G$ , 也即返回第 1 步。

降维状态观测器 考虑到系统的输出 y 中已包含有系统状态 x 的部分信息, 因此在直接利用这部分信息的基础上, 可以构造出维数低于被估计系统的状态观测器。通常, 称这类观测器为降维状态观测器。如果被估计系统为 n 维线性定常系统

$$
\begin{array}{l} \dot {\boldsymbol {x}} = A \boldsymbol {x} + B \boldsymbol {u} \\ \boldsymbol {u} = C \boldsymbol {u} \end{array} \tag {5.322}
\mathbf {y} = C \mathbf {x}
$$

其中，A, B 和 C 分别为 $n \times n, n \times p$ 和 $q \times n$ 实常阵，且假定 $\{A, C\}$ 为能观测，C 为满秩阵即有 rank C = q。那么，降维观测器的最小维数可为 n - q。这表明，降维观测器只需要较少的积分器来构成，简化了观测器的结构，因而在工程应用上具有重要意义。一般，常可采用两种方法来设计降维状态观测器。

方法 I: 给定被估计系统 $\{A, B, C\}$ ，已知 $\operatorname{rank} C = q$ ，且 $\{A, C\}$ 为能观测，则其 n - q 维的降维观测器可按如下的步骤来进行设计。

(1) 定义 $n \times n$ 矩阵
