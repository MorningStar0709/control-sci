记 $\mathcal{L}_{ij}(h)$ 是 $G(A)$ 中 $i$ 到 $j$ 所有长 $\equiv h (\bmod d)$ 的路所经过的 $G(A_t)$ 的下标 $t$ 的集合。由于 $\mathcal{L}_{IJ}$ 的定义， $\mathcal{L}_{IJ}$ 也是 $G(A)$ 中 $i$ 到 $j$ 长为 $d$ 的倍数的路所经过的 $G(A_t)$ 的下标 $t$ 的集合（由 $H_2$ 知 $H_1$ 成立， $G(A_t^d)$ 为强连通，所以对 $A_{IJ}$ 中任意 $i$ 行 $j$ 列元素这个 $t$ 集是相同的），即 $\mathcal{L}_{ij}(0) = \mathcal{L}_{IJ}$ 。由 $H_2$ ，每个 $G(A_t)$ 中有一条 $i_t$ 到 $i_t$ 的长为 1 的回路，于是可构造一条长为 $q$ 的回路，从 $i$ 出发经过 $i_t$ 回到 $i$ ，然后，在经过 $i_t$ 时，绕 $i_t$ 的长为 1 的回路 $n$ 次，使路长增加为 $q + n, \forall n > 0$ 。所以， $G(A)$ 中 $i$ 到 $j$ 长 $\equiv 0 (\bmod d)$ 的不含回路的所有有限条路的每一条都可按上法构造出长 $\equiv h (\bmod d)$ 的路， $\forall h \not\equiv 0 (\bmod d)$ 。于是

$$\mathcal {L} _ {i j} (0) \subset \mathcal {L} _ {i j} (h), \quad \forall h \not \equiv 0 (\mathrm{mod} d). \tag {11.4.31}$$

类似地，从长为 $h \not\equiv 0 (\bmod d)$ 的路出发，也可构造出长 $\equiv 0 (\bmod d)$ 的路。所以

$$\mathcal {L} _ {i j} (h) \subset \mathcal {L} _ {i j} (0), \quad \forall h \not \equiv 0 (\mathrm{mod} d). \tag {11.4.32}$$

联合式 (11.4.31)\~(11.4.32)，有

$$\mathcal {L} _ {i j} (h) = \mathcal {L} _ {I J}, \quad 0 \leqslant h < d. \tag {11.4.33}$$

下面先研究 $h = 1$ 的情况，令 $\lambda_{p} = e$ 。我们不仅考虑 $G(A^{d})$ ，而且考虑 $G(A)$ 。导出式 (11.4.29) 时实际上已证明 $G(A^{d})$ 中当 $i$ 到 $j$ 有路时，对 $G(A_{j})$ 中所有点 $j$ ，长为 $dn > dn_{0}$ 的 $i$ 到 $j$ 最重路必经过 $i_{0} \in \text{某 } v_{rs}^{p}$ 。所以，可先任意取定一个 $j$ ，由 $G(A_{j})$ 的强连通性，至少能找到一条 $j_{1}$ 到 $j$ 的弧，令其重量为 $f$ 。由 $G(A_{j}^{d})$ 的强连通性， $i$ 到 $j_{1}$ 有长为 $d$ 的倍数的路。由式 (11.4.29) 有

$$\left(\boldsymbol {A} ^ {d n}\right) _ {i j _ {1}} = c, \quad \forall n > n _ {0}.$$

把长为 $dn > dn_0$ 的 $i$ 到 $j_{1}$ 的最重路，与 $j_{1}$ 到 $j$ 的弧连接，成为一条长为 $dn + 1$ 的路，易知有

$$(A ^ {d n + 1}) _ {i j} \geqslant (A ^ {d n}) _ {i j _ {1}} \cdot f = c \cdot f \neq - \infty , \quad \forall n > n _ {0}. \tag {11.4.34}$$

另一方面，由式(11.4.33)，类似定理11.4.2可证明， $G(A)$ 中若 $i$ 到 $j$ 长为 $dn + 1$ 的最重路不经过 $i_0\in \mathbb{C}v_{rs}^{p}$ ，则当 $n\to +\infty$ 时，这条路的权重 $\rightarrow -\infty$ .于是与式(11.4.34)矛盾．因此必须经过 $i_0\in \mathbb{C}v_{rs}^{p}$ ，从而有

$$(A ^ {d n + 1 + d}) _ {i j} = (A ^ {d n + 1}) _ {i j}, \quad \forall n > n _ {0}.$$

当 $\lambda_p \neq e$ 时有

$$(A ^ {d n + 1 + d}) _ {i j} = \lambda_ {p} ^ {d} (A ^ {d n + 1}) _ {i j}, \quad \forall n > n _ {0}. \tag {11.4.35}$$

当 $i$ 到 $j$ 没有长为 $d$ 的倍数的路时，由 $H_{1}, i$ 到 $G(A_{J})$ 中所有 $j$ 均没有长为 $d$ 的倍数的路。这时可证 $i$ 到 $j$ 也没有长为 $nd + 1$ 的路， $\forall n > n_0$ 。反设有这样的路，则类似于证明式 (11.4.33) 的方法，可证 $i$ 到 $j$ 有长为 $(n + n_0)d$ 的路，导出矛盾。因而

$$(A ^ {d n + 1}) _ {i j} = - \infty , \quad \forall n > n _ {0}. \tag {11.4.36}$$

联合式 (11.4.35)\~(11.4.36), 可得
