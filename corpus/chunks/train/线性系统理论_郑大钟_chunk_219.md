$$
\begin{array}{l} \tilde {\boldsymbol {x}} = (A - L C) \tilde {\boldsymbol {x}}, \quad \tilde {\boldsymbol {x}} (0) = \tilde {\boldsymbol {x}} _ {0} = \boldsymbol {x} _ {0} - \hat {\boldsymbol {x}} _ {0} \\ \tilde {\boldsymbol {x}} _ {1} = \tilde {\boldsymbol {x}} _ {2} + \tilde {\boldsymbol {x}} _ {3}. \end{array} \tag {5.308}
$$

这表明，不管初始误差 $\tilde{\pmb{x}}_0$ 为多大，只要使矩阵 $(A - LC)$ 的特征值 $\lambda_{i}(A - LC)(i = 1,$

$2,\cdots,n)$ 均具有负实部,那么一定可做到使成立

$$\lim _ {t \rightarrow \infty} \hat {\boldsymbol {x}} (t) = \lim _ {t \rightarrow \infty} \boldsymbol {x} (t) \tag {5.309}$$

即实现状态的渐近重构。进而，如果可通过选择增益阵 L 而使 $\lambda_{i}(A-LC)(i=1,2,\cdots,n)$ 任意配置，则 $\tilde{\mathbf{x}}(t)$ 的衰减快慢是可被控制的。显然，若 $\lambda_{i}(A-LC)$ 均具有小于 $-\sigma$ 的负实部，则可断言 $\tilde{\mathbf{x}}(t)$ 的所有分量将以比 $e^{-\sigma t}$ 要快的速率衰减至零，即可使重构状态 $\hat{\mathbf{x}}(t)$ 很快地趋于真实状态 $\mathbf{x}(t)$ 。

下面,我们来给出可对全维状态观测器(5.307)进行任意极点配置的条件。

结论 设由(5.303)所给出的 $n$ 维线性定常系统是能观测的，即若 $\{A, C\}$ 为能观测，则必可采用由(5.307)所表述的全维观测器来重构其状态，并且必可通过选择增益阵 $L$ 而任意配置 $(A - LC)$ 的全部特征值。

证 利用对偶原理， $\{A,C\}$ 能观测意味着 $\{A^{T},C^{T}\}$ 能控。再利用极点配置问题的基本结论可知，对任意给定的 n 个实数或共轭复数特征值 $\{\lambda_{1}^{*},\lambda_{2}^{*},\cdots,\lambda_{n}^{*}\}$ ，必可找到一个实常阵 K，使成立

$$\lambda_ {i} \left(A ^ {T} - C ^ {T} K\right) = \lambda_ {i} ^ {*}, \quad i = 1, 2, \dots , n \tag {5.310}$$

进而由于 $(A^T - C^T K)$ 与其转置矩阵 $(A^T - C^T K)^T = (A - K^T C)$ 具有等同的特征值，故当取 $L = K^T$ 时就能使成立

$$\lambda_ {i} (A - L C) = \lambda_ {i} ^ {*}, \quad i = 1, 2, \dots , n \tag {5.311}$$

也即可任意配置 $(A-LC)$ 的全部特征值。于是，证明完成。

并且，由上述结论及其证明过程，还可容易归纳出设计全维状态观测器（5.307）的算法。

算法 给定被估计系统 $\dot{x}=Ax+Bu, y=Cx$ ，设 $\{A,C\}$ 为能观测，再对所要设计的全维观测器指定一组期望的极点 $\{\lambda_{1}^{*},\lambda_{2}^{*},\cdots,\lambda_{n}^{*}\}$ ，则设计全维状态观测器的步骤为：

第1步：导出对偶系统 $\{A^T, C^T, B^T\}$ 。

第2步：利用极点配置问题的算法 $^{①}$ ，对矩阵对 $\{A^{T}, C^{T}\}$ 来确定使

$$\lambda_ {i} (A ^ {T} - C ^ {T} K) = \lambda_ {i} ^ {*}, \quad i = 1, 2, \dots , n$$

的反馈增益阵 $K_{0}$

第3步：取 $L = K^T$ 。

第4步：计算 $(A - LC)$ ，则所要设计的全维状态观测器就为

$$\dot {\hat {x}} = (A - L C) \hat {x} + B u + L y$$

而 $\pmb{x}$ 即为 $\pmb{x}$ 的估计状态。

方法 II：给定能控且能观测的 n 维线性定常系统：

$$
\begin{array}{l} \dot {x} = A x + B u, \quad x (0) = x _ {0} \\ y = C x \tag {5.312} \\ \end{array}
$$

则将其全维状态观测器取为:

$$
\begin{array}{l} \dot {\boldsymbol {z}} = F \boldsymbol {z} + G \boldsymbol {y} + H \boldsymbol {u}, \quad \boldsymbol {z} (0) = \boldsymbol {z} _ {0} \\ \hat {\boldsymbol {x}} = T - 1, \end{array} \tag {5.313}
$$
