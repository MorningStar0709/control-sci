$$\left(\boldsymbol {Q} _ {0}\right) _ {i j} = \sum_ {i _ {0} \in \mathcal {N}} \left(\boldsymbol {A} _ {\lambda} ^ {d}\right) _ {i i _ {0}} ^ {+} \left(\boldsymbol {A} _ {\lambda} ^ {d}\right) _ {i _ {0} j} ^ {+} = \sum_ {i _ {0} \in \mathcal {N}} \left(\left(\boldsymbol {A} _ {\lambda} ^ {d}\right) _ {. i _ {0}} ^ {+} \otimes \left(\boldsymbol {A} _ {\lambda} ^ {d}\right) _ {i _ {0}.} ^ {+}\right) _ {i j}.$$

(iii) 由方程 (11.4.2) 及式 (11.4.7) 知, $\forall K \geqslant \frac{n_0 - h}{d}, 0 \leqslant h < d, k = h + Kd$ , 有

$$
\begin{array}{l} \boldsymbol {X} (k) = \boldsymbol {X} (0) \boldsymbol {A} ^ {k} = \lambda^ {k} \boldsymbol {X} (0) \boldsymbol {A} _ {\lambda} ^ {k} = \lambda^ {k} \boldsymbol {X} (0) \boldsymbol {A} _ {\lambda} ^ {h + K d} \\ = \lambda^ {k} X (0) Q _ {h}. \\ \end{array}
$$

定义11.4.3 若存在一个正整数 $n_0$ 及 $\pmb{\Lambda}$ 阵

$$
\pmb {A} = \left[ \begin{array}{c c c c} {\lambda_ {1}} & {\lambda_ {1 2}} & {\dots} & {\lambda_ {1 \omega}} \\ {\varepsilon} & {\lambda_ {2}} & {\dots} & {\lambda_ {2 \omega}} \\ {\vdots} & {\vdots} & & {\vdots} \\ {\varepsilon} & {\varepsilon} & {\dots} & {\lambda_ {\omega}} \end{array} \right], \tag {11.4.19}
$$

使得

$$\{A ^ {n + d} \} _ {I J} = \lambda_ {I J} ^ {d} \{A ^ {n} \} _ {I J}, \quad \forall n > n _ {0}, I, J, \tag {11.4.20}$$

则称 A 为 d 阶 A 分块周期阵.

定理11.4.3 在假设 $H_{2}$ 之下，

(i) 可约阵 $\pmb{A}$ 是 $d$ 阶 $\pmb{\Lambda}$ 分块周期阵，且 $d$ 可如式(11.4.5)所示。 $\pmb{\Lambda}$ 的元素为

$$\lambda_ {I J} = \max _ {L \in \mathcal {L} _ {I J}} \{\lambda_ {L} \} \stackrel {\mathrm{def}} {=} \lambda_ {p}, \tag {11.4.21}$$

其中 $\lambda_L$ 为 $A_L$ 的特征值， $\mathcal{L}_{IJ}$ 为 $G(A^d)$ 的凝图中 $I$ 到 $J$ 所有路经过的点 $L$ 的集合（包括点 $I, J$ ）。式(11.4.21)中当 $\mathcal{L}_{IJ} =$ 空集（即 $I$ 到 $J$ 无路）时，定义 $\lambda_{IJ} = -\infty, \lambda_{IJ}$ 满足以下递推公式：

$$\lambda_ {I J} = \sum_ {K = I + 1} ^ {J - 1} (\lambda_ {I K} \oplus \lambda_ {K J}) S _ {I K} S _ {K J} \oplus (\lambda_ {I} \oplus \lambda_ {J}) \widehat {S} _ {I J}, \tag {11.4.22}$$

其中

$$
S _ {I K} = \left\{ \begin{array}{l l} {- \infty ,} & {\text {当} \lambda_ {I K} = - \infty ,} \\ {\mathbf {e},} & {\text {当} \lambda_ {I K} \neq - \infty ,} \end{array} \right. \qquad \widehat {S} _ {I J} = \left\{ \begin{array}{l l} {- \infty ,} & {\text {当} \{A ^ {d} \} _ {I J} = \phi ,} \\ {\mathbf {e},} & {\text {当} \{A ^ {d} \} _ {I J} \neq \phi ,} \end{array} \right. \qquad (1 1. 4. 2 3)
$$

这里 $\phi$ 是每个元素都为 $-\infty$ 的阵， $e \stackrel{\mathrm{def}}{=} 0.$

(ii) 令
