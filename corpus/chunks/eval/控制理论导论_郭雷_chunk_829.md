# 11.2 数学准备

本节介绍极大代数，图论，双子代数与极大极小函数的基础知识，以便为后面的各节做好数学准备。先介绍极大代数及其矩阵的基础知识。

用 $\mathbb{R}$ 记实数集， $\varepsilon \stackrel{\mathrm{def}}{=} -\infty$ ，令 $\overline{R} = \mathbb{R} \cup \{\varepsilon\}$ ，在 $\overline{R}$ 上定义加法 $\oplus$ 与乘法

$$a \oplus b \stackrel {\text { def }} {=} \max \{a, b \}, \quad a \cdot b \stackrel {\text { def }} {=} a + b, \qquad \forall a, b \in \overline {{R}},$$

其中 + 是一般意义下的加法，乘号·通常省略。令 $D = \{\overline{R}, \oplus, \cdot\}$ ，则 D 称为一个极大代数， $\varepsilon$ 和 0 分别是 D 的加法零元和乘法单位元。

用 $D^{m \times n}$ 表示极大代数上所有 $m \times n$ 矩阵组成的集合。设 $\mathbf{A}, \mathbf{B} \in D^{m \times n}, \mathbf{A} = (a_{ij}), \mathbf{B} = (b_{ij})$ ，矩阵的加法定义为

$$\boldsymbol {A} \oplus \boldsymbol {B} = (a _ {i j} \oplus b _ {i j}).$$

如果 $\pmb{A} \in D^{m \times p}, \pmb{B} \in D^{p \times n}$ , 则矩阵的乘法定义为

$$\boldsymbol {A} \boldsymbol {B} = (c _ {i j}),$$

其中

$$c _ {i j} = \sum_ {k - 1} ^ {\nu} \oplus a _ {i k} b _ {k j} := a _ {i 1} b _ {1 j} \oplus a _ {i 2} b _ {2 j} \oplus \dots \oplus a _ {\tau p} b _ {p j},$$

求和号 $\sum_{\oplus}$ 可简记为 $\sum$ 。用0作对角线元， $\epsilon$ 作其他元定义的 $D$ 上 $n$ 阶单位阵记为 $E_n$ 。设 $A \in D^{n \times n}$ ，若存在 $B \in D^{n \times n}$ 满足

$$\boldsymbol {A} \boldsymbol {B} = \boldsymbol {B} \boldsymbol {A} = E _ {n},$$

则称矩阵 $\pmb{A}$ 可逆， $\pmb{B}$ 称为 $\pmb{A}$ 的逆矩阵，记为 $A^{-1}$ . 设 $a \in \overline{R}, A \in D^{m \times n}$ ，则纯量与矩阵相乘定义为

$$a A = (a a _ {i j}).$$

用 $(A)_{ij}$ 表示 $A$ 的第 $i$ 行第 $j$ 列上的元素，而 $(A)_{i}$ 与 $(A)_{j}$ 分别表示 $A$ 的第 $i$ 行和第 $j$ 列.

下面介绍与极大代数密切相关的有向图与关联矩阵的基础知识.

一个有向图是一个二元组 $(U, V), U$ 是图中所有点的集合， $V$ 是所有弧的集合，可用自然数 $1, 2, \cdots, n$ 对图中所有 $n$ 个点进行编号，用有序数对 $(ij)$ 或 $ij$ 表示点 $i$ 到点 $j$ 的弧，这里 $i$ 和 $j$ 可以是同一个点.

从点 $i_0$ 到点 $i_k$ 的一条有向通道是点与弧的一个交替序列 $i_0, (i_0 i_1), i_1, \cdots, i_k$ , 简记为 $i_0 i_1 \cdots i_k$ . 有向通道的长度是它上面所有弧的条数, 所以 $i_0 i_1 \cdots i_k$ 的长度为 $k$ . 如果 $i_k = i_0$ , 即 $i_k$ 和 $i_0$ 是同一个点, 那么 $i_0 i_1 \cdots i_k$ 称为一条闭通道. 如果 $i_0 i_1 \cdots i_k$ 中所有点都不相同, 则称它为一条有向路. 如果一条闭通道上所有点都不相同, 则称它为一条回路. 在不致引起混乱的情况下, 有向通道与有向路通称为路, 而闭通道与回路通称为回路. 如果 $i$ 到其自身有一条弧 $(ii)$ , 则称 $(ii)$ 为一条自回路.

从点 $i_{0}$ 到点 $i_{k}$ 的一条半通道仍然是点与弧的一个交替序列 $i_{0}, x_{1}, i_{1}, \cdots, x_{k}, i_{k}$ ，但每一条弧 $x_{i}$ 可能是 $(i_{j-1}i_{j})$ ，也可能是 $(i_{j}i_{j-1})$ 。同样地可以定义半闭通道、半路和半回路。

一个有向图称为强连通的，如果对任意两点 $i$ 和 $j (i \neq j)$ ，从 $i$ 到 $j$ 以及从 $j$ 到 $i$ 都有路。特别地，只含一个点的有向图也看作是强连通的；如果任意两点 $i$ 和 $j (i \neq j)$ 之间存在一条半通道，称为弱连通的，弱连通图也称为连通图。
