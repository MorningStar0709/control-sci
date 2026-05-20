\left[ \begin{array}{c c c c c} L _ {g} h (x) & L _ {a d _ {f} g} h (x) & \dots & \dots & L _ {a d _ {f} ^ {\rho - 1} g} h (x) \\ L _ {g} L _ {f} h (x) & & & L _ {a d _ {f} ^ {\rho - 2} g} L _ {f} h (x) & * \\ \vdots & & & & \vdots \\ L _ {g} L _ {f} ^ {\rho - 1} h (x) & * & \dots & & * \end{array} \right]
$$

根据引理(C.9)，上式等号右边矩阵形如：

$$
\left[ \begin{array}{c c c c c} 0 & \dots & \dots & 0 & \diamond \\ 0 & & & \diamond & * \\ \vdots & & & & \vdots \\ 0 & \diamond & & & * \\ \diamond & * & \dots & & * \end{array} \right]
$$

其中◇表示非零元素。因此，矩阵是非奇异的，这就证明了引理 C.9，因为上式等号左边两个矩阵的任一矩阵的秩小于 $\rho$ ，则它们的积一定是奇异的。

引理 C.9 证明了 $\rho \leqslant n$ 。下面证明定理 13.1。 $\rho = n$ 时的情况由引理 C.9 证明，引理第一条说明 $[\partial T/\partial x]$ 是非奇异的。考虑 $\rho < n$ 时的情况，分布 $\Delta = \operatorname{span}\{g\}$ 是非奇异、对合的，且其维数为 1（注意任意一维非奇异分布都是对合的。）根据 Frobenius 定理， $\Delta$ 是完全可积的。因此，对于每个 $x_{0} \in D$ ，存在 $x_{0}$ 的邻域 $N_{1}$ ，以及 n - 1 个光滑函数 $\phi_{1}(x), \cdots, \phi_{n-1}(x)$ ，其微分是线性无关的，满足

$$L _ {g} \phi_ {i} (x) = 0, 1 \leqslant i \leqslant n - 1, \forall x \in N _ {1}$$

因为 $L_{g}L_{f}^{i}h(x) = 0, \quad 0 \leqslant i \leqslant \rho - 2$

且 $dh(x),\cdots,dL_{f}^{\rho-2}h(x)$ 是线性无关的，因此可用 $h,\cdots,L_{f}^{\rho-2}h$ 作为这 n-1 个函数的一部分。特别地，可取其为 $\phi_{n-\rho+1},\cdots,\phi_{n-1}$ 。由于 $L_{g}L_{f}^{\rho-1}h(x)\neq0$ ，行向量 $dL_{f}^{\rho-1}h(x_{0})$ 与行向量 $d\phi_{1}(x_{0}),\cdots,d\phi_{n-1}(x_{0})$ 是线性无关的。因此

$$\operatorname{rank} \left[ {\frac {\partial T}{\partial x}} (x _ {0}) \right] = n \Rightarrow {\frac {\partial T}{\partial x}} (x _ {0}) \text {是非奇异的}$$

且存在 $x_0$ 的邻域 $N_{2}$ , 使得约束在 $N_{2}$ 上的 $T(x)$ 在 $N_{2}$ 上是微分同胚的, 取 $N = N_{1} \cap N_{2}$ , 即完成了定理 13.1 的证明。
