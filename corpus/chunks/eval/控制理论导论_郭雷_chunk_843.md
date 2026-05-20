$$Q _ {I J} (h) = \lim _ {n \rightarrow + \infty} \left\{A _ {\lambda_ {I J}} ^ {d n + h} \right\} _ {I J}, \quad 0 \leqslant h < d. \tag {11.4.24}$$

在 $G(A)$ 的凝图中，当 $I$ 到 $J$ 无路时， $Q_{IJ}(h) = \phi$ ；当 $I$ 到 $J$ 有路时，

$$Q _ {I J} (0) = \sum_ {p \in \mathcal {U} _ {I J}} \sum_ {i _ {0} \in \mathcal {N} _ {p}} (\{(A _ {\lambda_ {I J}} ^ {d}) ^ {+} \} _ {I p}) _ {. i _ {0}} \oplus (\{(A _ {\lambda_ {I J}} ^ {d}) ^ {+} \} _ {p J}) _ {i _ {0}}, \tag {11.4.25}\boldsymbol {Q} _ {I J} (h + 1) = \sum_ {S \in \mathcal {L} _ {I J}, \lambda_ {I S} = \lambda_ {I J}} \boldsymbol {Q} _ {I S} (h) \{\boldsymbol {A} \} _ {S J} / \lambda_ {I J}, \quad 0 \leqslant h < d - 1, \tag {11.4.26}$$

其中 $\mathcal{U}_{IJ} = \{L\mid \lambda_L = \lambda_p\} ,\lambda_p$ 定义见式(11.4.21).

(iii) 动态方程 (11.4.2) 的解为

$$\boldsymbol {X} (k) = \left[ \boldsymbol {X} _ {1} (k), \boldsymbol {X} _ {2} (k), \dots , \boldsymbol {X} _ {\omega} (k) \right],$$

其中 $X(k)$ 的分块与 $A^d$ 的列分块相同，而

$$\boldsymbol {X} _ {J} (k) = \widehat {\lambda} _ {J} ^ {k} \sum_ {K \in B _ {J}} \boldsymbol {X} _ {K} (0) \boldsymbol {Q} _ {K J} (h), \quad \forall J, \tag {11.4.27}$$

这里 $k = h + \tilde{K} d, \tilde{K} \geqslant (n_0 - h) / d, 0 \leqslant h < d,$

$$\mathcal {Y} _ {J} = \{K \mid X _ {K} (0) \neq \phi , 1 \leqslant K \leqslant J \},\widehat {\lambda} _ {J} - \max _ {K \in \mathcal {Y} _ {J}} \left\{\lambda_ {K J} \right\},\mathcal {B} _ {J} = \{K \mid K \in \mathcal {Y} _ {J}, \lambda_ {K J} = \widehat {\lambda} _ {J} \}. \tag {11.4.28}$$

证明 (i) 先令 $\lambda_{p} = e, d$ 如式 (11.4.5) 所示。把 $A_{IJ}$ 中任一元素记为 $(A)_{ij}$ . $G(A^{d})$ 中 $i$ 到 $j$ 有路时，设 $v_{rs}^{p}$ 是 $i$ 到 $j$ 路上的权 $= e$ 的回路，其他经过的回路都有权 $< e$ 。类似于定理 11.4.2(i) 的证明， $G(A^{d})$ 中 $i$ 到 $j$ 的长为 $n > n_{0}$ 的最重路必经过 $i_{0} \in$ 某 $v_{rs}^{p}$ 所以， $\forall n > n_{0}$ ，有

$$(A ^ {d n + d}) _ {i j} = (A ^ {d n}) _ {i j} = \sum_ {p \in U _ {i j}} \sum_ {i _ {0} \in \mathcal {N} _ {p}} (A ^ {d}) _ {i i _ {0}} ^ {+} (A ^ {d}) _ {i _ {0} j} ^ {A} \stackrel {\text { def }} {=} c. \tag {11.4.29}$$

当 $\lambda_p \neq e$ 时，有

$$(\boldsymbol {A} ^ {d n + d}) _ {i j} = \lambda_ {p} ^ {d} (\boldsymbol {A} ^ {d n}) _ {i j}, \quad \forall n > n _ {0}.$$

当 $i$ 到 $j$ 无路时，有

$$(A ^ {d n}) _ {i j} = - \infty , \quad \forall n > 0.$$

所以总有

$$\{A ^ {d n + d} \} _ {I J} = \lambda_ {p} ^ {d} \{A ^ {d n} \} _ {I J}, \quad \forall I, J, n > n _ {0}. \tag {11.4.30}$$

注意我们不能像定理11.4.1证明中那样，用在式(11.4.30)两边同乘 $A^h$ 的方法把式(11.4.30)由 $h = 0$ 变为 $h \neq 0$ . 为解决这个复杂的新问题，假设 $H_2$ 是一个充分条件.
