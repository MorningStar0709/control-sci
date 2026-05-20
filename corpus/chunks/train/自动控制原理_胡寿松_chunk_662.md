设 $\mathbf{A}$ 阵具有 $m$ 重实特征值 $\lambda_1$ ，其余为 $n - m$ 个互异实特征值，但在求解 $A p_i = \lambda_1 p_i$ 时只有一个独立实特征向量 $p_1$ ，则只能使 $\mathbf{A}$ 化为约当阵 $J$ 。

$$
\boldsymbol {J} = \boldsymbol {P} ^ {- 1} \boldsymbol {A} \boldsymbol {P} = \left[ \begin{array}{c c c c c c c c} \lambda_ {1} & 1 & & & & & \\ & \lambda_ {1} & \ddots & & & & \\ & & \ddots & 1 & & & \bigcirc \\ & & & \lambda_ {1} & & \\ & & & & \lambda_ {m + 1} & \\ & & \bigcirc & & & \ddots \\ & & & & & \lambda_ {n} \end{array} \right] \tag {9-171}
$$

J 中虚线示出存在一个约当块。

$$
\boldsymbol {P} = \left[ \begin{array}{l l l l l l l} \boldsymbol {p} _ {1} & \boldsymbol {p} _ {2} & \dots & \boldsymbol {p} _ {m} & \vdots & \boldsymbol {p} _ {m + 1} & \dots & \boldsymbol {p} _ {n} \end{array} \right] \tag {9-172}
$$

式中， $p_{2}, p_{3}, \cdots, p_{m}$ 是广义实特征向量，满足

$$
\left[ \begin{array}{l l l l} \boldsymbol {p} _ {1} & \boldsymbol {p} _ {2} & \dots & \boldsymbol {p} _ {m} \end{array} \right] \left[ \begin{array}{c c c c} \lambda_ {1} & 1 & & 0 \\ & \lambda_ {1} & \ddots & \\ 0 & & \ddots & 1 \\ & & & \lambda_ {1} \end{array} \right] = A \left[ \begin{array}{l l l l} \boldsymbol {p} _ {1} & \boldsymbol {p} _ {2} & \dots & \boldsymbol {p} _ {m} \end{array} \right] \tag {9-173}
$$

$p_{m+1},\cdots,p_{n}$ 是互异特征值对应的实特征向量。

3）化可控系统为可控标准型。

在前面研究状态空间表达式的建立问题时,曾得出单输入线性定常系统状态方程的可控标准型:

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \vdots \\ \dot {x} _ {n - 1} \\ \dot {x} _ {n} \end{array} \right] = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & & \vdots \\ 0 & 0 & 0 & \dots & 1 \\ - a _ {0} & - a _ {1} & - a _ {2} & \dots & - a _ {n - 1} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \vdots \\ x _ {n - 1} \\ x _ {n} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 0 \\ \vdots \\ 0 \\ 1 \end{array} \right] u \tag {9-174}
$$

与该状态方程对应的可控性矩阵 S 是一个右下三角阵, 其主对角线元素均为 1 , 故 $\det S \neq 0$ , 系统一定可控, 这就是形如式 (9-194) 中的 A, b 称为可控标准型名称的由来。其可控性矩阵 S 形如

$$
\boldsymbol {S} = \left[ \begin{array}{l l l l} \boldsymbol {b} & \boldsymbol {A b} & \dots & \boldsymbol {A ^ {n - 1}} \boldsymbol {b} \end{array} \right] = \left[ \begin{array}{c c c c c c} 0 & 0 & 0 & \dots & 0 & 1 \\ 0 & 0 & 0 & \dots & 1 & - a _ {n - 1} \\ \vdots & \vdots & \vdots & & \vdots & \vdots \\ 0 & 0 & 1 & \dots & \times & \times \\ 0 & 1 & - a _ {n - 1} & \dots & \times & \times \\ 1 & - a _ {n - 1} & - a _ {n - 2} & \dots & \times & \times \end{array} \right] \tag {9-175}
$$

一个可控系统, 当 A, b 不具有可控标准型时, 一定可以选择适当的变换化为可控标准型。设系统状态方程为
