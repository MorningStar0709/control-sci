$$
\begin{array}{l} \bar {A} - \bar {b} \bar {k} = \left[ \begin{array}{c c} 0 & \\ \vdots & I _ {s - 1} \\ 0 & \\ - \alpha_ {0} & - \alpha_ {1} \dots - \alpha_ {s - 1} \end{array} \right] - \left[ \begin{array}{c} 0 \\ \vdots \\ 0 \\ 1 \end{array} \right] [ \alpha_ {0} ^ {*} - \alpha_ {0}, \dots , \alpha_ {s - 1} ^ {*} - \alpha_ {s - 1} ] \\ = \left[ \begin{array}{c c} 0 & \\ \vdots & I _ {s - 1} \\ 0 & \\ \hline - \alpha_ {0} ^ {*} & - \alpha_ {1} ^ {*} \dots - \alpha_ {s - 1} ^ {*} \end{array} \right] \tag {5.47} \\ \end{array}
$$

而且，成立

$$
\begin{array}{l} \det (s I - A + b k) = \det (s I - \bar {A} + \bar {b} \bar {k}) \\ = s ^ {n} + \alpha_ {n - 1} ^ {*} s ^ {n - 1} + \dots + \alpha_ {1} ^ {*} s + \alpha_ {0} ^ {*} = \alpha^ {*} (s) \tag {5.48} \\ \end{array}
$$

这表明，对任给 $\{\lambda_{1}^{*},\lambda_{2}^{*},\cdots,\lambda_{n}^{*}\}$ ，都必可找到 $k=\bar{k}P^{-1}$ ，使(5.48)成立，即可任意配置闭环极点。综合上面推证结果，就完成了充分性的证明。至此，整个证明完成。

考虑到实际问题中几乎所有的系统都是能控的，因此通常总可利用状态反馈来控制系统的特征值即振型，而这正是状态反馈的重要特性之一。

单输入极点配置问题的算法 现来讨论极点配置问题中确定状态反馈增益矩阵的计算问题,这里先就单输入的情况给出其算法。

算法 给定能控矩阵对 $\{A, b\}$ 和一组期望的闭环特征值 $\{\lambda_{1}^{*}, \lambda_{2}^{*}, \cdots, \lambda_{n}^{*}\}$ ，要确定 $1 \times n$ 的反馈增益矩阵 k，使成立 $\lambda_{i}(A - bk) = \lambda_{i}^{*}, i = 1, 2, \cdots, n.$

第1步：计算 $A$ 的特征多项式，即 $\operatorname{det}(sI - A) = s^n + \alpha_{n-1}s^{n-1} + \cdots + \alpha_1s + \alpha_0.$

第2步：计算由 $\{\lambda_1^*,\dots ,\lambda_n^*\}$ 所决定的多项式，即 $a^{*}(s) = (s - \lambda_{1}^{*})\dots (s - \lambda_{n}^{*}) = s^{*} + a_{n - 1}^{*}s^{n - 1} + \dots +a_{1}^{*}s + a_{0}^{*}$

第3步：计算 $\bar{k} = [\alpha_{0}^{*} - \alpha_{0}, \alpha_{1}^{*} - \alpha_{1}, \cdots, \alpha_{n-1}^{*} - \alpha_{n-1}]$ 。

第4步：计算变换阵

$$
P = \left[ A ^ {s - 1} \boldsymbol {b}, \dots , A \boldsymbol {b}, \boldsymbol {b} \right] \left[ \begin{array}{c c c c c c} 1 & & & & & \\ & \ddots & & & & \\ \alpha_ {s - 1} & \ddots & \ddots & & & \\ \vdots & & \ddots & \ddots & \ddots & \\ \alpha_ {1} & \dots & \alpha_ {s - 1} & 1 \end{array} \right]
$$

第5步：求 $Q = P^{-1}$ 。

第6步：所求的增益阵 $k=\bar{k}Q$ 。

例 给定单输入线性定常系统为:

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c} 0 & 0 & 0 \\ 1 & - 6 & 0 \\ 0 & 1 & - 1 2 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 1 \\ 0 \\ 0 \end{array} \right] \boldsymbol {u}
$$

再给定期望的一组闭环特征值为:

$$\lambda_ {1} ^ {*} = - 2, \quad \lambda_ {2} ^ {*} = - 1 + j, \quad \lambda_ {3} ^ {*} = - 1 - j$$

易知系统为完全能控，故满足可配置条件。现计算系统的特征多项式
