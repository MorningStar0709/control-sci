由于状态反馈的引入不改变分母矩阵的列次数，所以可表 $D_{\kappa H}(s) = \widetilde{D}_{hc}S(s) + \widetilde{D}_{lc}\Psi (s)$ 则由 $N(s)D_{KH}^{-1}(s)$ 的控制器形实现 $(A_{c} - B_{c}HK,B_{c}H,C_{c})$ 的性质可进一步导出：

$$
\begin{array}{l} \det \left(\lambda_ {i} ^ {*} I - A _ {c} + B _ {c} H K\right) = (\det \bar {D} _ {h c}) ^ {- 1} \det D _ {K H} \left(\lambda_ {i} ^ {*}\right) = 0 \\ i = 1, 2, \dots , n \tag {11.120} \\ \end{array}
$$

这表明 $\lambda_{i}^{*}(i=1,2,\cdots,n)$ 为矩阵 $(A_{c}-B_{c}HK)$ 的特征值。再据控制器实现的性质可知，当 $\lambda_{i}^{*}$ 为 $(A_{c}-B_{c}HK)$ 的特征值且 $p_{i}$ 为使 $D_{KH}(\lambda_{i}^{*})p_{i}=0$ 的非零常数向量时， $(A_{c}-B_{c}HK)$ 的属于 $\lambda_{i}^{*}$ 的特征向量即为

$$\Psi \left(\lambda_ {i} ^ {*}\right) p _ {i} = f _ {i}, i = 1, 2, \dots , n \tag {11.121}$$

从而，就证明了在(11.111)的输入变换阵和(11.112)的状态反馈阵下，闭环状态反馈系统 $(A_{c}-B_{c}HK,B_{c}H,C_{c})$ 必以 $\{\lambda_{i}^{*},i=1,2,\cdots,n\}$ 和 $\{f_{i},i=1,2,\cdots,n\}$ 为特征值和特征向量。于是，证明完成。

例 给定 $G_{o}(s) = N(s)D^{-1}(s)$ ，其中

$$
N (s) = \left[ \begin{array}{c c} s ^ {2} + s & 0 \\ 2 s + 1 & - 1 \end{array} \right], \quad D (s) = \left[ \begin{array}{c c} s ^ {3} & 0 \\ - 2 s ^ {2} + s + 1 & 4 s + 1 \end{array} \right]
$$

矩阵 $D(s)$ 为列既约，其列次数 $k_{1} = 3$ 和 $k_{2} = 1$ ，且有

$$
\Psi (s) = \left[ \begin{array}{l l} s ^ {2} & 0 \\ s & 0 \\ 1 & 0 \\ 0 & 1 \end{array} \right], D _ {h c} = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 4 \end{array} \right], D _ {h c} ^ {- 1} = \left[ \begin{array}{l l} 1 & 0 \\ 0 & \frac {1}{4} \end{array} \right], D _ {l c} = \left[ \begin{array}{l l l l} 0 & 0 & 0 & 0 \\ - 2 & 1 & 1 & 1 \end{array} \right]
$$

再给定一组期望的特征值为:

$$\lambda_ {1} ^ {*} = - 2, \lambda_ {2, 3} ^ {*} = - 1 \pm j 2, \lambda_ {4} ^ {*} = - 5$$

且取一组期望的特征向量为：
