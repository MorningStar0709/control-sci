$$\boldsymbol {W} (s) = \frac {\beta_ {n - 1} s ^ {n - 1} + \beta_ {n - 2} s ^ {n - 2} + \cdots + \beta_ {1} s + \beta_ {0}}{s ^ {n} + \alpha_ {n - 1} s ^ {n - 1} + \cdots + \alpha_ {1} s + \alpha_ {0}}.$$

从这里看出，只要有了系统的标准形，就可直接写出它的传递函数来，这是定常线性系统标准形的优点之一。其实，无论是从能控标准形，还是从能观测标准形出发，得到的传递函数都是一样的。这是因为代数等价系统具有相同的传递函数。

现在研究多输入多输出定常线性系统的 Luenberger 标准形. 考察定常线性系统

$$
\left\{ \begin{array}{l} {\dot {x} (t) = A x (t) + B u (t),} \\ {y (t) = C x (t),} \end{array} \right. \tag {1.4.16}
$$

假设系统 (1.4.16) 完全能控和完全能观测，并且 $\operatorname{rank} B = r, \operatorname{rank} C = m$ 。令 $B = [b_1, b_2, \cdots, b_r]$ ，其中 $b_i$ 为矩阵 $B$ 的第 $i$ 列组成的向量， $i = 1, 2, \cdots, r$ 。因为系统 (1.4.16) 完全能控，所以它的能控性矩阵 $Q_c$ 满秩。展开 $Q_c$ 各列有

$$\boldsymbol {Q} _ {c} = \left[ b _ {1}, \dots , b _ {r}, \boldsymbol {A} b _ {1}, \dots , \boldsymbol {A} \boldsymbol {B} _ {r}, \dots , \boldsymbol {A} ^ {n - 1} b _ {1}, \dots , \boldsymbol {A} ^ {n - 1} b _ {r} \right].$$

为了把系统(1.4.16)化成某种标准形，可以从 $Q_{c}$ 的各列中选取状态空间中的一组基．选基时可按如下原则进行：

首先取 $b_{1}, b_{2}, \cdots, b_{r}$ . 然后再取 $Ab_{1}, Ab_{2}, \cdots, Ab_{r}$ . 如果在诸 $Ab_{i} (i = 1, 2, \cdots, r)$ 中有某 $Ab_{i}$ 与前面已选出的向量线性相关，那么就把它舍去，再继续选取 $A^{2}b_{1}, A^{2}b_{2}, \cdots, A^{2}b_{r}$ . 容易证明，如果 $A^{k}b_{i}$ 已被舍去，那么对任意的 $j \geqslant k, A^{j}b_{i}$ 也一定会被舍去. 依照这样的办法总可以选取状态空间的一组基，重新排列为

$$b _ {1}, A b _ {1}, \dots , A ^ {r _ {1} - 1} b _ {1}, b _ {2}, A b _ {2}, \dots , A ^ {r _ {2} - 1} b _ {2}, \dots , b _ {r}, A B _ {r}, \dots , A ^ {r _ {r} - 1} b _ {r}.$$

这里 $r_{1} + r_{2} + \cdots + r_{r} = n.$ 取

$$\boldsymbol {T} _ {1} = [ b _ {1}, \dots , \boldsymbol {A} ^ {r _ {1} - 1} b _ {1}, \dots , b _ {r}, \dots , \boldsymbol {A} ^ {r _ {r} - 1} b _ {r} ]. \tag {1.4.17}$$

显然矩阵 $T_{1}$ 是非奇异的，且在坐标变换 $\overline{x} = T_{1}^{-1}x$ 下，系统(1.4.16)变成如下代数等价的标准形式：

$$
\left\{ \begin{array}{l} \overline {{{x}}} (t) = \overline {{{A}}} _ {1} \overline {{{x}}} (t) + \overline {{{B}}} _ {1} u (t), \\ y (t) = \overline {{{C}}} _ {1} \overline {{{x}}} (t), \end{array} \right. \tag {1.4.18}
$$

其中 $\overline{A}_1 = T_1^{-1}AT_1, \overline{B}_1 = T_1^{-1}B.$ $\overline{C}_1 - CT_1$ ，并且 $\overline{A}_1$ 和 $\overline{B}_1$ 有如下特殊结构：

$$
\overline {{{A}}} _ {1} = \left[ \begin{array}{c c c} \overline {{{A}}} _ {1 1} & \dots & \overline {{{A}}} _ {1 r} \\ \vdots & & \vdots \\ \overline {{{A}}} _ {r 1} & \dots & \overline {{{A}}} _ {r r} \end{array} \right]. \quad \overline {{{B}}} _ {1} = \left[ \begin{array}{c} \overline {{{B}}} _ {1 1} \\ \vdots \\ \overline {{{B}}} _ {r r} \end{array} \right];
