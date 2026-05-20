$$\left\{\boldsymbol {A} ^ {d n + d + 1} \right\} _ {I J} = \lambda_ {p} ^ {d} \left\{\boldsymbol {A} ^ {d n + h} \right\} _ {I J}, \quad \forall I, J, n > n _ {0}.$$

对一般的 $h$ ，只要在上述证明中，把寻找 $j_1$ 到 $j$ 的弧的手续类似地做 $h$ 次，得到一条 $j_1$ 到 $j$ 长为 $h$ 的路，就可以类似地完成全部证明，并得到

$$\{A ^ {d n + d + h} \} _ {I J} = \lambda_ {p} ^ {d} \{A ^ {d n + h} \} _ {I J}, \quad \forall I, J, n > n _ {0}, 0 \leqslant h < d.$$

所以 A 是 d 阶 A 分块周期阵，且 $\lambda_{IJ} = \lambda_{p}$ .

由式 (11.4.23) 与 $\lambda_{IJ} = \lambda_p$ 可知

$$
(\lambda_ {I K} \oplus \lambda_ {K J}) S _ {I K} S _ {K J} = \left\{ \begin{array}{l l} \max \{\lambda_ {I K}, \lambda_ {K J} \}, & \text {若} \lambda_ {I K}, \lambda_ {K J} \neq - \infty , \\ - \infty , & \text {否则,} \end{array} \right.

(\lambda_ {I} \oplus \lambda_ {J}) \widehat {S} _ {I J} = \left\{ \begin{array}{l l} {\max \{\lambda_ {I}, \lambda_ {J} \},} & {\qquad \text {若} G (A) \text {的凝图中} I \text {到} J \text {有路},} \\ {- \infty ,} & {\qquad \text {否则}.} \end{array} \right.
$$

所以式 (11.4.22) 右边确实表示了 $\lambda_{p}$ , 递推公式 (11.4.22) 成立.

(ii) 当 $G(A)$ 的凝图中 $I$ 到 $J$ 无路时， $G(A)$ 中每个 $i$ 到每个 $j$ 均无路，这时显然有

$$(Q _ {I J} (h)) _ {i j} = - \infty , \quad 0 \leqslant h < d, \forall i, j.$$

当 $I$ 到 $J$ 有路时, 类似于式 (11.4.33) 的证明, 可知 $i$ 到 $j$ 有长 $\equiv h (\bmod d), 0 \leqslant h < d$ 的路. 由式 (11.4.24), (11.4.29) 有

$$
\begin{array}{l} \left(\boldsymbol {Q} _ {I J} (0)\right) _ {i j} = \sum_ {\boldsymbol {p} \in \mathcal {U} _ {I J}} \sum_ {i _ {0} \in \mathcal {N} _ {\boldsymbol {p}}} \left(\boldsymbol {A} _ {\lambda_ {I J}} ^ {d}\right) _ {i _ {0}} ^ {+} \left(\boldsymbol {A} _ {\lambda_ {I J}} ^ {d}\right) _ {i _ {0} j} ^ {+} \\ = \sum_ {p \in \mathcal {U} _ {I J}} \sum_ {i _ {0} \in \mathcal {N} _ {p}} \left(\left\{\left(A _ {\lambda_ {I J}} ^ {d} \right\rbrace_ {I p}\right) _ {i i _ {0}} \left(\left\{\left(A _ {\lambda_ {I J}} ^ {d}\right) ^ {+} \right\rbrace_ {p J}\right) _ {i _ {0} j} \right. \\ = \sum_ {p \in \mathcal {U} _ {I J}} \sum_ {i _ {0} \in \mathcal {N} _ {p}} ((\{(A _ {\lambda_ {I J}} ^ {d}) ^ {+} \} _ {I p}) _ {. i _ {0}} \otimes (\{(A _ {\lambda_ {I J}} ^ {d}) ^ {+} \} _ {p J}) _ {i _ {0}.}) _ {i j}. \\ \end{array}
$$

从而式 (11.4.25) 成立. 由 $A_{\lambda}$ 的定义及式 (11.4.33) 有
