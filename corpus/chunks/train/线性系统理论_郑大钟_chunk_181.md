其中， $\widetilde{A}_1$ 为 $n_1 \times n_1$ 常阵且 $\operatorname{Re} \lambda_i(\widetilde{A}_1) \geqslant 0 (i = 1, 2, \dots, n_1)$ ， $\widetilde{A}_2$ 为 $n_2 \times n_2$ 常阵且 $\operatorname{Re} \lambda_i(\widetilde{A}_2) < 0 (i = 1, 2, \dots, n_2)$ ， $\overline{A}_c$ 为 $n_c \times n_c$ 矩阵，并有 $n_1 + n_2 = n_c$ 。同时，求出 $Q^{-1}$ 。

第3步：利用极点配置问题算法，计算 $n_1 \times p$ 的反馈增益阵 $\tilde{K}_1$ ，使 $\lambda_i(\tilde{A}_1 - \tilde{B}_1\tilde{K}_1)$

$(i=1,2,\cdots,n_{1})$ 均具有负实部。

第4步：所求的镇定反馈增益矩阵 $K = [\widetilde{K}_1, 0]Q^{-1}P$ 。

可以看出，上述算法是通过只把位于右半闭复数平面上的极点“调整”到左半开复数平面上而实现镇定的。这种做法在理论上是很严密的，但计算过程的复杂性增加了；特别是要进行化 $\{\bar{A}_c, \bar{B}_c\}$ 为约当形 $\{\tilde{A}_c, \tilde{B}_c\}$ ，将导致复杂的计算和数值稳定性上的困难。因此，从实用的角度而言，特别是当 $\{A, B\}$ 为能控时，把镇定问题看成为极点配置问题，通过指定一组期望闭环极点并直接利用上节中给出的算法，将更为简单和方便。
