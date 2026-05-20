# 波波夫形的一些基本特性

(1) 令 $D_{E}(s)$ 为 $\pmb{p}$ 维波波夫形多项式矩阵，表 $L = \max \{k_{ct}, \dots, k_{cp}\}$ ，且将 $D_{E}(s)$ 表示为

$$D _ {E} (s) = D _ {L} s ^ {L} + D _ {L - 1} s ^ {L - 1} + \dots + D _ {1} s + D _ {0} \tag {6.134}$$

其中 $D_{i}(i=0,1,\cdots,L)$ 为常数矩阵。现定义

$$\mathcal {D} _ {B} ^ {\prime} = \left[ D _ {0} ^ {\prime} D _ {1} ^ {\prime} \dots D _ {L} ^ {\prime} \right] \tag {6.135}$$

其中“”表示取转置，则 $\mathcal{D}_B'$ 必为阶梯形常数矩阵。而这也正是把波波夫形又称为多项式阶梯形的一个原因。

例 给定如下的波波夫形多项式矩阵 $D_{\varepsilon}(s)$ ，并表示为式(6.134)的形式：

$$
\begin{array}{l} D _ {E} (s) = \left[ \begin{array}{c c c} 5 s + 1 & s ^ {2} + 3 s + 2 & 4 s + 6 \\ 3 s + 4 & 2 s + 1 & s ^ {3} + s ^ {2} + 2 \\ s + 7 & 3 & 5 \end{array} \right] \\ = \left[ \begin{array}{l l l} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right] s ^ {3} + \left[ \begin{array}{l l l} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right] s ^ {2} + \left[ \begin{array}{l l l} 5 & 3 & 4 \\ 3 & 2 & 0 \\ 1 & 0 & 0 \end{array} \right] s + \left[ \begin{array}{l l l} 1 & 2 & 6 \\ 4 & 1 & 2 \\ 7 & 3 & 5 \end{array} \right] \\ \end{array}
$$

现组成常阵 $\mathcal{D}_{\beta}^{\prime}$ 为：

$$
\mathcal {D} _ {E} ^ {\prime} = \left[ \begin{array}{c c c c c c c c c c c} 1 & 4 & 7 & 5 & 3 & \overline {{①}} & 0 & 0 & 0 & 0 & 0 \\ 2 & 1 & 3 & 3 & 2 & 0 & \overline {{①}} & 0 & 0 & 0 & 0 \\ 6 & 2 & 5 & 4 & 0 & 0 & 0 & 1 & 0 & 0 & \overline {{①}} \end{array} \right]
$$

其中 $\mathcal{D}_B'$ 包含了波波夫形阵 $D_E(s)$ 的一切特征，且位于阶梯上的元“①”体现了主元多项式的各特征，并将其称为 $\mathcal{D}_B'$ 的主元。

(2) 令 $\alpha_{i} \triangleq \mathcal{D}_{B}^{\prime}$ 的第 $i$ 行中主元所处的列位置指数， $i = 1, 2, \cdots, p$ ，则列位置指数 $\{\alpha_{i}\}$ 是在强意义下不相等的，即成立

$$\alpha_ {i} \neq \alpha_ {j} \mod p, \quad i \neq j \tag {6.136}$$

这一特性可从上面的例子中看出。容易定出， $D_{b}^{\prime}$ 中各主元的列位置指数为

$$\alpha_ {1} = 6, \alpha_ {2} = 7, \alpha_ {3} = 1 1$$

而它们显然是强意义下不相等的。

（3）对波波夫形 $D_{E}(s)$ ，相应的常阵 $D_{B}^{\prime}$ 的组成形式中：①主元是其所在列中的唯一非零元。②所有的列 $(\alpha_{i} + \beta p)$ 均为零列，其中 $p = \dim D_{E}(s), \beta = 1, 2, \cdots$ 。

$\mathcal{D}_{\varepsilon}^{\prime}$ 的这一特性是由波波夫形定义中(2)的条件⑤所保证的。并且，从前面所讨论的例子中，也可不难看出 $\mathcal{D}_{\varepsilon}^{\prime}$ 的这个特性。

(4) 多项式矩阵 $D(s)$ 和 $D(s)V(s)$ ，其中 $V(s)$ 为单模阵，具有相同的波波夫形 $D_E(s)$ .

下面可知 $D_{E}(s)$ 是由 $D(s)$ 右乘适当的单模阵 $U(s)$ 所得的，即 $D_{E}(s) = D(s)U(s)$ ，它的具体算法将在下面给出。所以，由此就有

$$
\begin{array}{l} \overline {{{D}}} _ {E} (s) = [ D (s) V (s) ] \overline {{{U}}} (s) = D (s) V (s) [ V ^ {- 1} (s) U (s) ] \\ = D (s) U (s) = D _ {E} (s) \\ \end{array}
$$

其中已取 $\overline{U}(s) = V^{-1}(s)U(s)$ ，且这样取定的 $\overline{U}(s)$ 显然必为单模阵。从而证明了结论的正确性。
