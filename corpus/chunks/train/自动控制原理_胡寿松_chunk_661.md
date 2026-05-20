# (1) 状态空间表达式的线性变换

在研究线性定常连续系统状态空间表达式的建立方法时可以看到,选取不同的状态变量便有不同形式的动态方程。若两组状态变量之间用一个非奇异矩阵联系着,则两组动态方程的系数矩阵与该非奇异矩阵有确定关系。

设系统动态方程为

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {b} \boldsymbol {u}, \quad \boldsymbol {y} = \boldsymbol {c x} \tag {9-163}$$

令

$$\boldsymbol {x} = \boldsymbol {P} \bar {\boldsymbol {x}} \tag {9-164}$$

式中， $P$ 为非奇异线性变换矩阵，它将 $\pmb{x}$ 变换为 $\pmb{x}$ ，变换后的动态方程为

$$\dot {\boldsymbol {x}} = \bar {\boldsymbol {A}} \bar {\boldsymbol {x}} + \bar {\boldsymbol {b}} \boldsymbol {u}, \quad \bar {\boldsymbol {y}} = \bar {\boldsymbol {c}} \bar {\boldsymbol {x}} = \boldsymbol {y} \tag {9-165}$$

式中

$$\bar {\boldsymbol {A}} = \boldsymbol {P} ^ {- 1} \boldsymbol {A} \boldsymbol {P}, \quad \bar {\boldsymbol {b}} = \boldsymbol {P} ^ {- 1} \boldsymbol {b}, \quad \bar {\boldsymbol {c}} = \boldsymbol {c} \boldsymbol {P} \tag {9-166}$$

并称为对系统进行 $P$ 变换。对系统进行线性变换的目的在于使 $\overline{A}$ 阵规范化，以便于揭示系统特性及分析计算，并不会改变系统的原有性质，故称为等价变换。待获得所需结果之后，再引入反变换关系 $\bar{x} = P^{-1}x$ ，换算回原来的状态空间中去，得出最终结果。

下面概括给出本章中常用的几种线性变换关系。

1) 化 A 阵为对角型。

① 设 A 阵为任意形式的方阵，且有 n 个互异实数特征值 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$ ，则可由非奇异线性变换化为对角阵 $\Lambda$ 。

$$
\boldsymbol {\Lambda} = \boldsymbol {P} ^ {- 1} \boldsymbol {A} \boldsymbol {P} = \left[ \begin{array}{c c c c} \lambda_ {1} & & & 0 \\ & \lambda_ {2} & & \\ 0 & & \ddots & \\ & & & \lambda_ {n} \end{array} \right] \tag {9-167}
$$

P 阵由 A 阵的实数特征向量 $p_{i}(i=1,2,\cdots,n)$ 组成

$$
\boldsymbol {P} = \left[ \begin{array}{l l l l} \boldsymbol {p} _ {1} & \boldsymbol {p} _ {2} & \dots & \boldsymbol {p} _ {n} \end{array} \right] \tag {9-168}
$$

特征向量满足

$$\boldsymbol {A} \boldsymbol {p} _ {i} = \lambda_ {i} \boldsymbol {p} _ {i}; \quad i = 1, 2, \dots , n \tag {9-169}$$

② 若 A 阵为友矩阵，且有 n 个互异实数特征值 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$ ，则下列的范德蒙特 (Vandermode) 矩阵 P 可使 A 对角化：

$$
\mathbf {A} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & & \vdots \\ 0 & 0 & 0 & \dots & 1 \\ - a _ {0} & - a _ {1} & - a _ {2} & \dots & - a _ {n - 1} \end{array} \right], \quad \mathbf {P} = \left[ \begin{array}{c c c c} 1 & 1 & \dots & 1 \\ \lambda_ {1} & \lambda_ {2} & \dots & \lambda_ {n} \\ \lambda_ {1} ^ {2} & \lambda_ {2} ^ {2} & \dots & \lambda_ {n} ^ {2} \\ \vdots & \vdots & & \vdots \\ \lambda_ {1} ^ {n - 1} & \lambda_ {2} ^ {n - 1} & \dots & \lambda_ {n} ^ {n - 1} \end{array} \right] \tag {9-170}
$$

2) 化 A 阵为约当型。
