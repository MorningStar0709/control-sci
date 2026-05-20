# 7.2 矩阵分式描述的真性和严真性

真性和严真性 称一个 MFD 是真的, 如果它所代表的传递函数矩阵 $G(s)=(n_{ij}(s)/d_{ii}(s))$ 满足如下的关系式

$$\deg n _ {i j} (s) \leqslant \deg d _ {i j} (s), \forall i, j \tag {7.14}$$

称一个 MFD 是严格真的, 如果其传递函数矩阵 $G(s) = (n_{ij}(s) / d_{ij}(s))$ 满足关系式

$$\deg n _ {i j} (s) < \deg d _ {i j} (s), \forall i, j \tag {7.15}$$

矩阵分式描述的真性和严真性也可用另一种方式来定义。令 $G(s) = N(s)D^{-1}(s)$ ，则 $N(s)D^{-1}(s)$ 为真的，当且仅当

$$\lim _ {s \rightarrow \infty} G (s) = G _ {0} (\text {非零常阵}) \tag {7.16}$$

而 $N(s)D^{-1}(s)$ 为严格真的，当且仅当

$$\lim _ {s \rightarrow \infty} G (s) = 0 \tag {7.17}$$

对矩阵分式描述的真性和严真性的研究具有重要意义。只有当 MFD 为真的或严格真的时，它所表征的系统才是可以用实际的物理元件来构成的，或是才能正常地工作的。

判别准则 下面，我们来给出并证明可用于判断矩阵分式描述的真性和严真性的一些判据。

判据1 $[D(s)$ 为列既约的情况] 令 $N(s)$ 和 $D(s)$ 分别为 $q \times p$ 和 $p \times p$ 的多项式矩阵， $D(s)$ 为列既约，则矩阵分式描述 $N(s)D^{-1}(s)$ 是真的，当且仅当

$$\delta_ {c i} N (s) \leqslant \delta_ {c i} D (s), \quad i = 1, \dots , p. \tag {7.18}$$

而 $N(s)D^{-1}(s)$ 为严格真的，当且仅当

$$\delta_ {e i} N (s) < \delta_ {e i} D (s), i = 1, \dots , p \tag {7.19}$$

证 必要性： $N(s)D^{-1}(s)$ 为真(严真)，欲证式(7.18)或(7.19)成立。

令 $N(s)D^{-1}(s) = G(s)$ ，则可导出 $N(s) = G(s)D(s)$ 。再令 $n_{ij}(s)$ 为 $N(s)$ 的元， $d_{kj}(s)$ 为 $D(s)$ 的元，就有

$$
n _ {i j} (s) = \left[ g _ {i 1} (s) \dots g _ {i p} (s) \right] \left[ \begin{array}{c} d _ {1 j} (s) \\ \vdots \\ d _ {p j} (s) \end{array} \right] = \sum_ {k = 1} ^ {p} g _ {i k} (s) d _ {k j} (s) \tag {7.20}
$$

其中 $i=1,2,\cdots,q,\quad i=1,2,\cdots,p$ 。现知 $N(s)D^{-1}(s)=G(s)$ 为真的，则据定义有 $g_{ik}(s)$ 的分子的次数小于或等于分母的次数，因此由(7.20)即可看出， $n_{ij}(s)$ 的次数必小于或等于 $d_{kj}(s)(k=1,\cdots,p)$ 中的最高次数，也即

$$\deg n _ {i j} (s) \leqslant \max \left\{\deg d _ {k j} (s), k = 1, \dots , p \right\}, \forall i \tag {7.21}$$

因此，等价地有

$$\delta_ {c j} N (s) \leqslant \delta_ {c j} D (s), i = 1, \dots , p \tag {7.22}$$

类似地，当 $N(s)D^{-1}(s)$ 为严格真时，可导出

$$\delta_ {c j} N (s) < \delta_ {c j} D (s), i = 1, \dots , p \tag {7.23}$$

从而，必要性得证。

充分性：(7.18)或(7.19)成立，欲证 $N(s)D^{-1}(s)$ 为真或严格真的。

首先,利用列次表示式,将 $D(s)$ 和 $N(s)$ 表示为

$$D (s) = \left[ D _ {h c} + D _ {l c} (s) H _ {c} ^ {- 1} (s) \right] H _ {c} (s) \tag {7.24}N (s) = \left[ N _ {h c} + N _ {l c} (s) H _ {c} ^ {- 1} (s) \right] H _ {c} (s) \tag {7.25}$$

从而，就有

$$
\begin{array}{l} G (s) = N (s) D ^ {- 1} (s) \\ = \left[ N _ {b c} + N _ {l c} (s) H _ {c} ^ {- 1} (s) \right] \left[ D _ {b c} + D _ {l c} (s) H _ {c} ^ {- 1} (s) \right] ^ {- 1} \tag {7.26} \\ \end{array}
$$

再注意到 $\delta_{ei}D_{lc}(s) < \delta_{ei}H_{e}(s)$ ，而由(7.18)又可知 $\delta_{ei}N_{lc}(s) < \delta_{ei}H_{e}(s)$ ，故必成立
