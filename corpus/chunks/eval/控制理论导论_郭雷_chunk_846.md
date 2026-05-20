$$
\begin{array}{l} \left\{A _ {\lambda_ {I J}} ^ {d n + h + 1} \right\} _ {I J} = \frac {1}{\lambda_ {I J} ^ {d n + h + 1}} \left\{A ^ {d n + h + 1} \right\} _ {I J} \\ = \sum_ {S} \frac {1}{\lambda_ {I J} ^ {d n + h + 1}} \left\{\boldsymbol {A} ^ {d n + h} \right\} _ {I S} \boldsymbol {A} _ {S J} \\ = \sum_ {S} \frac {\lambda_ {I S} ^ {d n + h} \lambda_ {S J}}{\lambda_ {I J} ^ {d n + h + 1}} \left\{\boldsymbol {A} _ {\lambda_ {I S}} ^ {d n + h} \right\} _ {I S} \left\{\boldsymbol {A} _ {\lambda_ {S J}} \right\} _ {S J}. \\ \end{array}
$$

当 $S \notin \mathcal{L}_{IJ}$ 时，由式 (11.4.21)，以及 $\lambda_{IS}$ 或 $\lambda_{SJ} = -\infty$ 知，上式中相应项为 $-\infty$ . 当 $S \in \mathcal{L}_{IJ}$ 时，注意到 $\lambda_{IS} \leqslant \lambda_{IJ}$ ，有

$$
\lim _ {n \to + \infty} {\frac {\lambda_ {I S} ^ {d n + h} \lambda_ {S J}}{\lambda_ {\lambda_ {I J}} ^ {d n + h + 1}}} = {\left\{ \begin{array}{l l} {- \infty ,} & {\qquad \text {若} \lambda_ {I S} <   \lambda_ {I J},} \\ {\lambda_ {S J} / \lambda_ {I J},} & {\qquad \text {若} \lambda_ {I S} = \lambda_ {I J}.} \end{array} \right.}
$$

所以

$$\boldsymbol {Q} _ {I J} (h + 1) = \lim _ {n \rightarrow + \infty} \left\{\boldsymbol {A} _ {\lambda_ {I J}} ^ {d n + h + 1} \right\} _ {I J} = \sum_ {S \in \mathcal {L} _ {I J}, \lambda_ {I S} = \lambda_ {I J}} \boldsymbol {Q} _ {I S} (h) \left\{\boldsymbol {A} \right\} _ {S J} / \lambda_ {I J},$$

式 (11.4.26) 获证.

(iii) 由方程 (11.4.2) 易知 $X(k) = X(0)A^k$ , 于是 $\forall k > n_0$ ,

$$
\begin{array}{l} \boldsymbol {X} _ {J} (k) = \sum_ {K = 1} ^ {J} \boldsymbol {X} _ {k} (0) \left\{\boldsymbol {A} ^ {k} \right\} _ {K J} = \sum_ {K = 1} ^ {J} \lambda_ {K J} ^ {k} \boldsymbol {X} _ {k} (0) \left\{\boldsymbol {A} _ {\lambda_ {K J}} ^ {k} \right\} _ {K J} \\ = \sum_ {K = 1} ^ {J} \lambda_ {K J} ^ {k} X _ {K} (0) \left\{A _ {\lambda_ {K J}} ^ {h + K d} \right\} _ {K J} = \sum_ {K = 1} ^ {J} \lambda_ {K J} ^ {k} X _ {K} (0) Q _ {K J} (h) \\ = \sum_ {K \in \mathcal {Y} _ {J}} \lambda_ {K J} ^ {k} X _ {K} (0) Q _ {K J} (h). \tag {11.4.37} \\ \end{array}
$$

当 $G(A^d)$ 的凝图中 $K$ 到 $J$ 无路时， $\lambda_{KJ} = -\infty$ ；有路时，由式 (11.4.33) 与 $Q_{KJ}(h)$ 定义式 (11.4.24) 易知 $Q_{KJ}(h)$ 的每个元素 $\neq -\infty, 0 \leqslant h < d$ 。因此当 $K \in \mathcal{Y}_J$ 时， $X_K(0)Q_{KJ}(h)$ 是每个分量均 $\neq -\infty$ 的一些常数组成的向量。由 $\mathcal{B}_J$ 定义式 (11.4.28)，可得

$$\widehat {\lambda} _ {J} ^ {k} \sum_ {K \in B _ {J}} X _ {K} (0) Q _ {K J} (h) > \sum_ {K \not \in B _ {J}, K \in \mathcal {Y} _ {J}} \lambda_ {K J} ^ {k} X _ {K} (0) Q _ {K J} (h),$$

这里对于两个向量 $X$ 和 $Y, X > Y$ 表示 $X$ 的每个分量均大于 $Y$ 的相应分量。再由式 (11.4.37) 得

$$\boldsymbol {X} _ {J} (k) = \widehat {\lambda} _ {J} ^ {k} \sum_ {K \in \mathcal {B} _ {J}} \boldsymbol {X} _ {K} (0) \boldsymbol {Q} _ {K J} (h).$$

从以上定理看出，为研究系统的稳态性能，并得到动态方程的解，需分析每个强连通块 $A_{L}$ 的特征值 $\lambda_{L}$ 对系统的影响。仿照传统线性系统理论中关于“振型”的说法，可以把 $\omega$ 个强连通块含的 $\omega$ 个特征值看作是系统内含的周期或“振型”，它们在动态方程的解中，有时只有一部分表现出来。而可约阵 $A$ 的特征值，仅有 $p \leqslant \omega$ 个。这一点更多地具有数学理论上的意义。这就是特征值理论与系统周期分析之间的联系与区别。
