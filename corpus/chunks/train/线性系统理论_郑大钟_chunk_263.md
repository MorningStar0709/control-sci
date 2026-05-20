# 6.12 史密斯形

史密斯（Smith）形是多项式矩阵的另一种重要的规范形。任一多项式矩阵都可同时通过初等行运算和列运算而化成为史密斯形。这一节中，我们首先来阐明史密斯形的特征，在此基础上进而研究与其有关的其他一些问题。

史密斯形 设有 $q \times p$ 的多项式矩阵 $Q(s)$ , $\operatorname{rank} Q(s) = r$ , $0 \leqslant r \leqslant \min(q, p)$ . 如果可找到相应维数的单模阵 $\{V(s), U(s)\}$ , 使有

$$
U (s) Q (s) V (s) = \Lambda (s) = \left[ \begin{array}{c c c c} \lambda_ {1} (s) & & 0 \\ & \ddots & \vdots \\ & & \lambda_ {r} (s) & 0 \\ - & - & - & - \\ 0 & \dots & \dots & 0 \end{array} \right] \tag {6.99}
$$

其中 $\{\lambda_i(s)\}$ 是满足整除性

$$\lambda_ {i} (s) \mid \lambda_ {i + 1} (s), i = 1, 2, \dots , r - 1 \tag {6.100}$$

的非零首1多项式。则称 $\Lambda(s)$ 为多项式矩阵 $Q(s)$ 的史密斯形。

求史密斯形的算法 给定多项式矩阵 $Q(s)$ ，则其史密斯形 $\Lambda(s)$ 可按如下步骤来求得。

(1) 如果 $Q(s) \equiv 0$ ，则其本身就是史密斯规范形。如果 $Q(s) \neq 0$ ，则在非零的元素中，将最低次数的元素，通过行交换及列交换，换到(1,1)的位置上，记为 $q_{\mathrm{II}}(s)$ 。

(2) 将所得矩阵的第 1 行和第 1 列的各元素用 $q_{11}(s)$ 除之, 求出商和余式:

$$
\left\{ \begin{array}{l} q _ {1 i} (s) = q _ {1 1} (s) p _ {1 i} (s) + f _ {1 i} (s) \\ q _ {k 1} (s) = q _ {1 1} (s) p _ {k 1} (s) + f _ {k 1} (s) \end{array} \right. \tag {6.101}
$$

如果余式 $f_{1i}(s)$ 和 $f_{k1}(s)$ 均为0，则即转入下一步。如果余式 $f_{1i}(s)$ 和 $f_{k1}(s)$ 不全为0，则在不为0的余式中找出次数最低的，例如 $f_{\alpha 1}(s)$ ，作如下的运算：

$$\text {行} \alpha^ {\prime \prime} - \text {行} 1 \times p _ {\alpha 1} (s) ^ {\prime \prime} \tag {6.102}$$

然后转回到步骤(1)。而且, 步骤(1)—(2)每进行一次, (1,1)处的元素的次数至少降低一次。这样, 经过有限次之后, 就达到所有的余式均为0, 此后转入下一步。

(3) 作如下的行和列运算:

$$
\left\{ \begin{array}{l l} “ \text {行} k ” - “ \text {行} 1 \times \tilde {p} _ {k 1} (s) ”, & k = 2, \dots , q \\ “ \text {列} i ” - “ \text {列} 1 \times \tilde {p} _ {1 i} (s) ”, & i = 2, \dots , p \end{array} \right. \tag {6.103}
$$

其中 $\widetilde{p}_{k1}(s)$ 和 $\widetilde{p}_{i j}(s)$ 为第1列和第1行中的商。于是，便得到如下形式的多项式矩阵：

$$
\left[ \begin{array}{c c c} \lambda_ {1} ^ {*} (s) & 0 & \dots & 0 \\ \hline 0 & & \\ \vdots & Q _ {2} (s) \\ 0 & & \end{array} \right] \tag {6.104}
$$

(4) 对 $Q_{2}(s)$ 重复步骤(1)—(3)，进而得到

$$
\left[ \begin{array}{c c} \lambda_ {1} ^ {*} (s) & \\ & \lambda_ {2} ^ {*} (s) \\ \hline & Q _ {3} (s) \end{array} \right] \tag {6.105}
$$

● ● ● ● ● ●

$(r+2)$ 对最后一个剩余子阵重复步骤(1)—(3)，于是可得到

$$
\left[ \begin{array}{c c c c c} \lambda_ {1} ^ {*} (s) & & & & 0 \\ & \lambda_ {2} ^ {*} (s) & & & \vdots \\ & & \ddots & & \vdots \\ & & & \lambda_ {r} ^ {*} (s) & 0 \\ \hline 0 & \dots & \dots & 0 & 0 \end{array} \right] \tag {6.106}
$$

$(r+3)$ 如果 $\{\lambda_{i}^{*}(s)\}$ 已是满足整除性

$$\lambda_ {i} ^ {*} (s) \mid \lambda_ {i + 1} ^ {*} (s), \quad i = 1, 2, \dots , r - 1 \tag {6.107}$$
