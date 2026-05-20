其中 $k = h + Kd, K \geqslant \frac{n_0 - h}{d}, 0 \leqslant h \leqslant d - 1.$

证明 (i) 充分性. 由 $\lambda$ 的定义知 $\lambda \neq -\infty$ . 先令 $\lambda = e \stackrel{\mathrm{def}}{=} 0$ , 并取 $d$ 如式 (11.4.5) 所示. 由 $H_{1}, A^{d}$ 的分块与 $A$ 相同. 设 $G(A^{d})$ 中 $i$ 到 $j$ 的权重最重的路 (简称最重路) 具有长度 $p \leqslant N - 1$ , 并经过某 $\gamma_{rs}^{t}$ 中的 $i_{0}$ . 于是

$$(A ^ {d}) _ {i j} ^ {+} = (A ^ {d p}) _ {i j} = (A ^ {d}) _ {i i _ {0}} ^ {+} (A ^ {d}) _ {i _ {0} j} ^ {+}. \tag {11.4.10}$$

由式 (11.4.5), $d_r^t | d, \forall t, r$ , 再由式 (11.4.3), 文献 [17] 与初等数论知识, 易知对每个 $n > n_0$ , 存在非负整数 $n_s$ 满足

$$d n = d _ {r} ^ {t} \cdot \frac {d}{d _ {r} ^ {t}} \cdot n = \sum_ {s} n _ {s} d _ {r s} ^ {t}. \tag {11.4.11}$$

于是可以在 $G(A)$ 中从 $i_0$ 出发绕各 $\gamma_{rs}^t, n_s$ 次回到 $i_0$ 而平均权重 $= e$ (这等价于在 $G(A^d)$ 中走长为 $n$ 的 $i_0$ 到 $i_0$ 的回路).

注意到对每个大于 $n_0$ 的 $n$ 都有式 (11.4.11), 所以对更大 $(>n_0 + p)$ 的 $n$ 与 $n + 1$ , 可在 $G(A^d)$ 中走长为 $n - p$ 与 $n + 1 - p$ 的 $i_0$ 到 $i_0$ 的回路, 然后用式 (11.4.10) 可得

$$(A ^ {d n + d}) _ {i j} = (A ^ {d n}) _ {i j} = (A ^ {d p}) _ {i j} = (A ^ {d}) _ {i i _ {0}} ^ {+} (A ^ {d}) _ {i _ {0} j} ^ {+}, \quad \forall n > n _ {0} + p. \tag {11.4.12}$$

上式中若把 $n_0 + p$ 记为新的 $n_0$ ，即 $n_0$ 看作可适当变大的充分大的正常数，则 $\forall n > n_0 + p$ 可改记为简洁的 $\forall n > n_0$ 。下面使用 $\forall n > n_0$ 时均含有这个意义。现取 $i_0$ 与 $j$ 在 $G(A^d)$ 的同一强连通支，则 $i_0$ 到 $j$ 总有路，然后在式 (11.4.12) 中取 $i = i_0$ ，得

$$(A ^ {d}) _ {i _ {0} j} ^ {+} = (A ^ {d n}) _ {i _ {0} j} = (A ^ {d n + d}) _ {i _ {0} j}, \quad \forall n > n _ {0}. \tag {11.4.13}$$

现设 $G(A^d)$ 中 $i$ 到 $j$ 有路， $i \notin \mathcal{N}$ ，且 $(A^d)_{ij}^+ = (A^{dp_j})_{ij}$ . 易知对式 (11.4.13) 中的 $i_0$ ，总有一条 $i$ 到 $j$ ，经过 $j$ 后再从 $j$ 到 $i_0$ 的路，所以有

$$(A ^ {d n}) _ {i j} \geqslant (A ^ {d p _ {i _ {0}}}) _ {i i _ {0}} (A ^ {d n - d p _ {i _ {0}}}) _ {i _ {0} j}.$$

由式 (11.4.13), $(A^{dn - dp_{i0}})_{i0j} = (A^d)_{i0j}^+ \neq -\infty, \forall n > n_0$ , 所以

$$\left(\boldsymbol {A} ^ {d n}\right) _ {i j} \geqslant \left(\boldsymbol {A} ^ {d p _ {i _ {0}}}\right) _ {i i _ {0}} \left(\boldsymbol {A} ^ {d}\right) _ {i _ {0} j} ^ {+} \neq - \infty , \quad \forall n > n _ {0}. \tag {11.4.14}$$

下面证明 $G(A^d)$ 中 $i$ 到 $j$ 长为 $n > n_0$ . 重为 $(A^{dn})_{ij}$ 的路 $\mu$ 必须经过一个点 $i_0 \in \mathcal{N}_{ij}$ . 反设 $\mu$ 不经过 $i_0$ . 记 $\eta$ 为 $G(A^d)$ 中平均权重为第二重的回路的平均权重, 则 $\eta < e, \mu$ 必经过一些平均权重 $\leqslant \eta < e$ 的回路. 设 $\mu$ 去掉所有回路后的长为 $\hat{p} < N$ , 则

$$(A ^ {d n}) _ {i j} \leqslant (A ^ {d \hat {p}}) _ {i j} \eta^ {n - \hat {p}} \leqslant (A ^ {d}) _ {i j} ^ {+} \eta^ {n - \hat {p}}.$$

当 $n \to +\infty$ 时上式 $\rightarrow -\infty$ . 这与式 (11.4.14) 矛盾. 于是, 类似式 (11.4.12) 有
