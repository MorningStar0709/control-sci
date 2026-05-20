# 10.6 严格系统等价

定义 给定两个不同的多项式矩阵描述,其系统矩阵分别为

$$
S _ {1} (s) = \left[ \begin{array}{l l} P _ {1} (s) & Q _ {1} (s) \\ - R _ {1} (s) & W _ {1} (s) \end{array} \right], \quad S _ {2} (s) = \left[ \begin{array}{l l} P _ {2} (s) & Q _ {2} (s) \\ - R _ {2} (s) & W _ {2} (s) \end{array} \right]. \tag {10.106}
$$

其中，各系数矩阵 $P_{i}(s), Q_{i}(s), R_{i}(s)$ 和 $W_{i}(s)$ 分别为 $m_{i} \times m_{i}, m_{i} \times p, q \times m_{i}$ 和 $q \times p$ 维，而 $i = 1, 2$ 。不妨设 $m_{1} = m_{2} = m$ ，因为如若不然则其中维数较小的一个系统矩阵可用其增广系统矩阵代替，使之有上述维数等式。基于这种考虑，所以通常总有 $m \geqslant \deg \det P_{i}(s), i = 1, 2$ 。于是，称系统矩阵 $S_{1}(s)$ 和 $S_{2}(s)$ 是严格系统等价的，当且仅当存在 $m \times m$ 的单模阵 $U(s)$ 和 $V(s)$ ，以及 $q \times m$ 和 $m \times p$ 的多项式矩阵 $X(s)$ 和 $Y(s)$ ，使成立

$$
\left[ \begin{array}{l l} U (s) & 0 \\ X (s) & I _ {q} \end{array} \right] \left[ \begin{array}{c c} P _ {1} (s) & Q _ {1} (s) \\ - R _ {1} (s) & W _ {1} (s) \end{array} \right] \left[ \begin{array}{c c} V (s) & Y (s) \\ 0 & I _ {p} \end{array} \right] = \left[ \begin{array}{c c} P _ {2} (s) & Q _ {2} (s) \\ - R _ {2} (s) & W _ {2} (s) \end{array} \right] \tag {10.107}
$$

并且简记为 $S_{1}(s) \sim S_{2}(s)$ 。

从上述定义出发,容易证明,严格系统等价变换满足下述的一些属性:

对称性：若 $S_{1}(s)\sim S_{2}(s)$ ，则 $S_{2}(s)\sim S_{1}(s)$ 。

自反性： $S_{1}(s) \sim S_{1}(s)$ 。

传递性：若 $S_{1}(s)\sim S_{2}(s)$ 和 $S_{2}(s)\sim S_{3}(s)$ ，则 $S_{1}(s)\sim S_{3}(s)$

严格系统等价变换的一些重要性质 下面,我们来指出,系统的各种类型的描述,在严格系统等价变换下所具有的一些重要性质。

结论1 给定两个系统矩阵 $S_{1}(s)$ 和 $S_{2}(s)$ 如(10.106)所示，则当它们为严格系统等价时， $S_{1}(s)$ 和 $S_{2}(s)$ 之间满足如下的关系：

① $P_{1}(s)$ 和 $P_{2}(s)$ 具有相同的不变多项式，即成立

$$\det P _ {2} (s) = \beta_ {0} \det P _ {1} (s) \tag {10.108}$$

其中 $\beta_{0}$ 为非零常数。

② $S_{1}(s)$ 和 $S_{2}(s)$ 具有相同的传递函数矩阵，即成立

$$R _ {1} (s) P _ {1} ^ {- 1} (s) Q _ {1} (s) + W _ {1} (s) = R _ {2} (s) P _ {2} ^ {- 1} (s) Q _ {2} (s) + W _ {2} (s) \tag {10.109}$$

证 由严格等价性定义可知， $S_{1}(s)$ 和 $S_{2}(s)$ 满足式(10.107)。现将(10.107)的等式左边乘出，得到：

$$
\begin{array}{l} \left[ \begin{array}{c c} U (s) P _ {1} (s) V (s) & U (s) P _ {1} (s) Y (s) + U (s) Q _ {1} (s) \\ - \left(R _ {1} (s) - X (s) P _ {1} (s)\right) V (s) & \left(X (s) P _ {1} (s) - R _ {1} (s)\right) Y (s) + \left(X (s) Q _ {1} (s) + W _ {1} (s)\right) \end{array} \right] \\ = \left[ \begin{array}{c c} P _ {2} (s) & Q _ {2} (s) \\ - R _ {2} (s) & W _ {2} (s) \end{array} \right] \tag {10.110} \\ \end{array}
$$

于是，由此即可导出

$$P _ {2} (s) = U (s) P _ {1} (s) V (s) \tag {10.111}$$

考虑到 $U(s)$ 和 $V(s)$ 为单模阵，并表 $\beta_0 = \det U(s) \det V(s)$ ，那么即可证得

$$\det P _ {2} (s) = \det U (s) \det V (s) \det P _ {1} (s) = \beta_ {0} \det P _ {1} (s) \tag {10.112}$$
